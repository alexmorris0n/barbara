"""
Appointment booking tools
Creates Nylas calendar events with assigned broker

Per Section 4.21 (Results & Actions): Return SwaigFunctionResult
Per Section 6.16.2.3: Use .update_global_data() for real-time AI state awareness
Note: Using sync httpx.Client() - SWAIG handlers run synchronously

Ported from Reference/reference-swaig-agent/tools/booking.py
Enhanced with global_data updates for real-time prompt variable changes
"""

import os
import logging
from datetime import datetime
from signalwire_agents.core.function_result import SwaigFunctionResult

try:
    import httpx
except ImportError:
    httpx = None

from services.database import (
    get_lead_by_phone,
    update_conversation_state,
    normalize_phone
)

logger = logging.getLogger(__name__)

NYLAS_API_KEY = os.getenv("NYLAS_API_KEY")
N8N_MANUAL_BOOKING_WEBHOOK = os.getenv("N8N_MANUAL_BOOKING_WEBHOOK")


def _trigger_manual_booking_webhook(
    lead_id: str = None,
    broker_id: str = None,
    phone: str = None,
    error: str = None,
    requested_time: str = None,
    notes: str = None
) -> None:
    """Trigger n8n webhook to notify about manual booking requirement (sync)"""
    webhook_url = N8N_MANUAL_BOOKING_WEBHOOK
    if not webhook_url or not httpx:
        logger.warning("[WEBHOOK] N8N_MANUAL_BOOKING_WEBHOOK not configured or httpx not available")
        return
    
    try:
        # Use sync client
        with httpx.Client(timeout=10.0) as client:
            response = client.post(
                webhook_url,
                json={
                    "lead_id": lead_id,
                    "broker_id": broker_id,
                    "phone": phone,
                    "error": error,
                    "error_type": type(error).__name__ if error else "Unknown",
                    "requested_time": requested_time,
                    "notes": notes,
                    "timestamp": datetime.utcnow().isoformat(),
                    "source": "signalwire_agent"
                }
            )
            
            if response.status_code == 200:
                logger.info(f"[WEBHOOK] Manual booking webhook triggered successfully for lead {lead_id}")
            else:
                logger.error(f"[WEBHOOK] Manual booking webhook failed: {response.status_code}")
                
    except Exception as webhook_error:
        logger.error(f"[WEBHOOK] Failed to trigger manual booking webhook: {webhook_error}")


def _parse_appointment_time(preferred_time: str, broker_tz_name: str = 'America/Los_Angeles', duration_minutes: int = 30) -> tuple:
    """
    Parse preferred_time string into Unix timestamps for Nylas.
    
    Handles:
    - ISO datetime: "2025-11-26T14:00:00-08:00"
    - Unix timestamp: "1732654800"
    - Natural language: "tomorrow at 2pm" (best effort)
    
    Returns: (start_unix, end_unix) or (None, None) on error
    """
    import pytz
    from dateutil import parser as date_parser
    
    try:
        broker_tz = pytz.timezone(broker_tz_name)
        
        # Check if it's a Unix timestamp
        if preferred_time.isdigit():
            start_unix = int(preferred_time)
            end_unix = start_unix + (duration_minutes * 60)
            return start_unix, end_unix
        
        # Try to parse as datetime
        dt = date_parser.parse(preferred_time)
        
        # If no timezone, assume broker's timezone
        if dt.tzinfo is None:
            dt = broker_tz.localize(dt)
        
        start_unix = int(dt.timestamp())
        end_unix = start_unix + (duration_minutes * 60)
        
        return start_unix, end_unix
        
    except Exception as e:
        logger.warning(f"[BOOKING] Could not parse time '{preferred_time}': {e}")
        return None, None


def handle_booking(phone: str, preferred_time: str, notes: str = None) -> SwaigFunctionResult:
    """Book appointment with assigned broker via Nylas (sync)"""
    phone = normalize_phone(phone)
    
    if not preferred_time:
        return SwaigFunctionResult(
            "What time would work best for you? I can check availability."
        )
    
    # Get lead to find assigned broker (sync)
    lead = get_lead_by_phone(phone)
    if not lead:
        return SwaigFunctionResult(
            "I couldn't find your information. Let me connect you with our team."
        )
    
    # Get broker Nylas grant ID
    broker = lead.get('brokers')
    if not broker or not broker.get('nylas_grant_id'):
        return SwaigFunctionResult(
            "I'll need to assign you a broker first. Let me connect you with our team."
        )
    
    nylas_grant_id = broker['nylas_grant_id']
    broker_name = broker.get('contact_name', 'Broker')
    broker_tz = broker.get('timezone', 'America/Los_Angeles')
    duration = broker.get('appointment_duration_minutes', 30)
    lead_id = lead.get('id')
    broker_id = broker.get('id') if broker else None
    
    # Parse the preferred time into Unix timestamps
    start_unix, end_unix = _parse_appointment_time(preferred_time, broker_tz, duration)
    
    if not start_unix:
        return SwaigFunctionResult(
            f"I couldn't understand that time. Could you say it like 'Tuesday at 2pm' or 'November 26th at 10am'?"
        )
    
    # Format for confirmation message
    from datetime import datetime
    import pytz
    tz = pytz.timezone(broker_tz)
    appointment_dt = datetime.fromtimestamp(start_unix, tz=tz)
    friendly_time = appointment_dt.strftime("%A, %B %d at %-I:%M %p")
    
    # Create Nylas event with Unix timestamps
    event_data = {
        "title": f"Reverse Mortgage Consultation - {lead.get('first_name', 'Client')}",
        "description": f"Reverse mortgage consultation call.\n\nLead Phone: {phone}\nNotes: {notes or 'None'}",
        "when": {
            "start_time": start_unix,
            "end_time": end_unix,
        },
        "participants": [
            {"email": lead.get('primary_email', '')},
        ]
    }
    
    # Call Nylas API
    if not httpx or not NYLAS_API_KEY:
        # Mock response when Nylas not configured
        logger.warning("[BOOKING] Nylas not configured, using mock response")
        
        update_conversation_state(phone, {
            "conversation_data": {
                "appointment_booked": True,
                "appointment_time": appointment_dt.isoformat(),
                "ready_to_book": False
            }
        })
        
        # Per Section 6.16.2.3: Update global_data so AI sees booking is complete
        return (
            SwaigFunctionResult(
                f"Perfect! I've scheduled your consultation with {broker_name} "
                f"for {friendly_time}. You'll receive a confirmation shortly. "
                f"Is there anything else I can help you with?"
            )
            .update_global_data({
                "appointment_booked": True,
                "ready_to_book": False
            })
        )
    
    try:
        # Use sync client
        with httpx.Client(timeout=10.0) as client:
            response = client.post(
                f"https://api.nylas.com/v3/grants/{nylas_grant_id}/events",
                headers={
                    "Authorization": f"Bearer {NYLAS_API_KEY}",
                    "Content-Type": "application/json"
                },
                json=event_data
            )
        
        if response.status_code == 200:
            event = response.json()
            event_id = event.get('data', {}).get('id', 'unknown')
            
            # Update conversation state (sync)
            update_conversation_state(phone, {
                "conversation_data": {
                    "appointment_booked": True,
                    "appointment_time": appointment_dt.isoformat(),
                    "appointment_id": event_id,
                    "ready_to_book": False
                }
            })
            
            logger.info(f"[BOOKING] Appointment created: {event_id} for {phone} at {friendly_time}")
            
            # Per Section 6.16.2.3: Update global_data so AI sees booking is complete
            return (
                SwaigFunctionResult(
                    f"Perfect! I've scheduled your consultation with {broker_name} "
                    f"for {friendly_time}. You'll receive a confirmation email shortly. "
                    f"Is there anything else I can help you with?"
                )
                .update_global_data({
                    "appointment_booked": True,
                    "ready_to_book": False
                })
            )
        else:
            logger.error(f"[BOOKING] Nylas API error: {response.status_code}")
            
            # Set manual booking required flag (sync)
            update_conversation_state(phone, {
                "conversation_data": {
                    "manual_booking_required": True,
                    "booking_error": f"Nylas API error: {response.status_code}"
                }
            })
            
            # Trigger n8n webhook for manual booking (sync)
            _trigger_manual_booking_webhook(
                lead_id=lead_id,
                broker_id=broker_id,
                phone=phone,
                error=f"Nylas API error: {response.status_code}",
                requested_time=preferred_time,
                notes=notes
            )
            
            return SwaigFunctionResult(
                "I'm having trouble accessing the calendar right now. "
                "Let me have someone call you directly to schedule. Is this the best number to reach you at?"
            )
                
    except Exception as e:
        logger.error(f"[BOOKING] Error creating appointment: {e}")
        
        # Set manual booking required flag (sync)
        update_conversation_state(phone, {
            "conversation_data": {
                "manual_booking_required": True,
                "booking_error": str(e)
            }
        })
        
        # Trigger n8n webhook for manual booking (sync)
        _trigger_manual_booking_webhook(
            lead_id=lead_id,
            broker_id=broker_id,
            phone=phone,
            error=str(e),
            requested_time=preferred_time,
            notes=notes
        )
        
        return SwaigFunctionResult(
            "I encountered an issue scheduling your appointment. "
            "Let me have someone call you directly to schedule. Is this the best number to reach you at?"
        )


def handle_check_broker_availability(phone: str, preferred_date: str = None, preferred_time: str = None) -> SwaigFunctionResult:
    """
    Check broker availability for appointment (sync).
    
    Note: Slots are pre-loaded in global_data at call start.
    This tool is for when user requests a specific time not in pre-loaded slots.
    """
    phone = normalize_phone(phone)
    
    # Get lead to find assigned broker (sync)
    lead = get_lead_by_phone(phone)
    if not lead:
        return SwaigFunctionResult(
            "I couldn't find your information. Let me connect you with our team."
        )
    
    # Get broker info
    broker = lead.get('brokers')
    if not broker:
        return SwaigFunctionResult(
            "I'll need to assign you a broker first. Let me connect you with our team."
        )
    
    broker_name = broker.get('contact_name', 'your broker')
    
    # Import availability service for real-time check
    try:
        from services.availability import fetch_broker_availability, format_slots_for_llm, filter_slots_by_time_of_day
        
        # Fetch fresh availability (in case pre-loaded slots are stale)
        slots = fetch_broker_availability(broker, days_ahead=7, max_slots=20)  # Get more slots for filtering
        
        if not slots:
            return SwaigFunctionResult(
                f"I'm having trouble checking {broker_name}'s calendar right now. "
                f"Let me have someone call you to schedule. Is this the best number to reach you?"
            )
        
        # Filter by time of day if requested
        broker_tz = broker.get('timezone', 'America/Los_Angeles')
        if preferred_time:
            preferred_time_lower = preferred_time.lower()
            # Check if user requested morning or afternoon
            if any(word in preferred_time_lower for word in ['morning', 'am', 'before noon', 'before 12']):
                slots = filter_slots_by_time_of_day(slots, 'morning', broker_tz)
                time_filter = 'morning'
            elif any(word in preferred_time_lower for word in ['afternoon', 'pm', 'after noon', 'after 12', 'evening']):
                slots = filter_slots_by_time_of_day(slots, 'afternoon', broker_tz)
                time_filter = 'afternoon'
            else:
                time_filter = None
            
            # No slots match the time preference
            if not slots and time_filter:
                return SwaigFunctionResult(
                    f"I don't see any {time_filter} slots available in the next few days. "
                    f"Would you like me to check for other times, or would you prefer someone call you to schedule?"
                )
        
        if not slots:
            # No slots at all (fetch failed or broker has no availability)
            return SwaigFunctionResult(
                f"I'm having trouble finding available times for {broker_name}. "
                f"Would you prefer someone call you to schedule?"
            )
        
        # Format slots for response
        slots_display = format_slots_for_llm(slots, max_display=5)
        next_slot = slots[0]['display'] if slots else "soon"
        
        if preferred_date or preferred_time:
            return SwaigFunctionResult(
                f"Let me check for {preferred_date or ''} {preferred_time or ''}... "
                f"The closest available time is {next_slot}. "
                f"Other options:\n{slots_display}\n"
                f"Which works best for you?"
            )
        else:
            return SwaigFunctionResult(
                f"{broker_name} has these times available:\n{slots_display}\n"
                f"Which works best for you?"
            )
            
    except Exception as e:
        logger.error(f"[BOOKING] Error checking availability: {e}")
        return SwaigFunctionResult(
            f"{broker_name} is generally available during business hours. "
            f"What day and time would work best for you?"
        )
