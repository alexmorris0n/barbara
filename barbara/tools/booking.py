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
    get_conversation_state,
    update_conversation_state,
    normalize_phone,
    create_appointment,
    update_appointment,
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
    
    # Build notes with requested time included
    notes_with_time = notes or ""
    if requested_time:
        time_note = f"Requested booking time: {requested_time}"
        if notes_with_time:
            notes_with_time = f"{notes_with_time} | {time_note}"
        else:
            notes_with_time = time_note
    
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
                    "notes": notes_with_time,
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
    import re
    import pytz
    from datetime import datetime, timedelta, time as dtime
    from dateutil import parser as date_parser
    
    try:
        broker_tz = pytz.timezone(broker_tz_name)
        now = datetime.now(tz=broker_tz)
        
        # Check if it's a Unix timestamp
        if preferred_time.isdigit():
            start_unix = int(preferred_time)
            end_unix = start_unix + (duration_minutes * 60)
            return start_unix, end_unix

        raw = preferred_time.strip()
        lower = raw.lower()

        # Handle common relative-date phrasing (dateutil does not parse "tomorrow"/"next friday")
        base_date = None

        if re.search(r"\btomorrow\b", lower):
            base_date = (now + timedelta(days=1)).date()
        elif re.search(r"\btoday\b", lower):
            base_date = now.date()
        else:
            weekday_map = {
                "monday": 0,
                "tuesday": 1,
                "wednesday": 2,
                "thursday": 3,
                "friday": 4,
                "saturday": 5,
                "sunday": 6,
            }
            for name, idx in weekday_map.items():
                if re.search(rf"\b(next\s+)?{name}\b", lower):
                    is_next = bool(re.search(rf"\bnext\s+{name}\b", lower))
                    days_ahead = (idx - now.weekday()) % 7
                    if days_ahead == 0:
                        days_ahead = 7
                    if is_next:
                        days_ahead += 7
                    base_date = (now + timedelta(days=days_ahead)).date()
                    break

        if base_date is not None:
            # Extract time of day from phrase
            if re.search(r"\bnoon\b", lower):
                hour, minute = 12, 0
            elif re.search(r"\bmidnight\b", lower):
                hour, minute = 0, 0
            else:
                m = re.search(r"\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)\b", lower)
                if not m:
                    return None, None
                hour = int(m.group(1))
                minute = int(m.group(2) or "0")
                ampm = m.group(3)
                if hour == 12:
                    hour = 0
                if ampm == "pm":
                    hour += 12

            dt = broker_tz.localize(datetime.combine(base_date, dtime(hour=hour, minute=minute)))

            # If it's in the past (e.g., "today 9am" but it's already afternoon), push to next week/day.
            if dt <= now and re.search(r"\btoday\b", lower):
                return None, None

            start_unix = int(dt.timestamp())
            end_unix = start_unix + (duration_minutes * 60)
            return start_unix, end_unix
        
        # Try to parse as datetime
        # Provide a default so missing year/month/day components resolve in broker timezone.
        dt = date_parser.parse(preferred_time, default=now.replace(second=0, microsecond=0), fuzzy=True)
        
        # If no timezone, assume broker's timezone
        if dt.tzinfo is None:
            dt = broker_tz.localize(dt)
        
        start_unix = int(dt.timestamp())
        end_unix = start_unix + (duration_minutes * 60)
        
        return start_unix, end_unix
        
    except Exception as e:
        logger.warning(f"[BOOKING] Could not parse time '{preferred_time}': {e}")
        return None, None


def _trigger_persona_sms_webhook(
    to_number: str,
    persona_name: str,
    lead_first_name: str,
    broker_name: str,
    friendly_time: str,
    appointment_iso: str,
    sms_consent: bool = False
) -> None:
    """
    Trigger n8n webhook to send personalized SMS from persona.
    n8n will add a delay before sending to make it feel natural.
    
    ONLY sends if sms_consent=True (caller agreed to receive texts).
    """
    if not sms_consent:
        logger.info(f"[WEBHOOK] Skipping persona SMS - no consent for {to_number}")
        return
    
    webhook_url = "https://n8n.instaroute.com/webhook/persona-sms"
    
    if not httpx:
        logger.warning("[WEBHOOK] httpx not available - skipping persona SMS webhook")
        return
    
    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.post(
                webhook_url,
                json={
                    "to_number": to_number,
                    "persona_name": persona_name or "Your advisor",
                    "lead_first_name": lead_first_name or "there",
                    "broker_name": broker_name,
                    "friendly_time": friendly_time,
                    "appointment_iso": appointment_iso,
                    "sms_consent": sms_consent,
                    "timestamp": datetime.utcnow().isoformat(),
                    "source": "barbara_agent"
                }
            )
            
            if response.status_code == 200:
                logger.info(f"[WEBHOOK] Persona SMS webhook triggered for {to_number}")
            else:
                logger.error(f"[WEBHOOK] Persona SMS webhook failed: {response.status_code}")
                
    except Exception as e:
        logger.error(f"[WEBHOOK] Failed to trigger persona SMS webhook: {e}")


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
    nylas_calendar_id = broker.get('nylas_calendar_id') or 'primary'  # Use specific calendar or default to primary
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
    # NOTE: Avoid platform-specific strftime modifiers like "%-I" (fails on Windows).
    time_part = appointment_dt.strftime("%I:%M %p")
    # Only strip a single leading zero (e.g., "09:00 AM" -> "9:00 AM").
    # Using lstrip("0") is broader than intended.
    if time_part.startswith("0"):
        time_part = time_part[1:]
    friendly_time = f"{appointment_dt.strftime('%A, %B')} {appointment_dt.day} at {time_part}"
    
    # Get SMS consent from conversation state (needed for appointment record)
    state = get_conversation_state(phone)
    sms_consent = state.get('conversation_data', {}).get('sms_consent', False) if state else False

    # Create appointment record FIRST to stop race with webhook
    # We'll embed its UUID into the Nylas event description so the webhook can map the event deterministically.
    appointment_row = None
    appointment_id = None
    try:
        appointment_row = create_appointment(
            lead_id=lead_id,
            broker_id=broker_id,
            appointment_time=appointment_dt.isoformat(),
            nylas_event_id=None,
            sms_consent=sms_consent,
            status="scheduling",
        )
        appointment_id = appointment_row.get("id") if appointment_row else None
    except Exception as e:
        logger.error(f"[BOOKING] Failed to create pre-book appointment record: {e}")

    # Create Nylas v3 event - requires timezone in 'when' object
    lead_name = f"{lead.get('first_name', '')} {lead.get('last_name', '')}".strip() or "Client"
    lead_email = lead.get('primary_email', '')
    
    marker = f"ECG_APPOINTMENT_ID={appointment_id}" if appointment_id else "ECG_APPOINTMENT_ID=unknown"

    event_data = {
        "title": f"Reverse Mortgage Consultation - {lead_name}",
        "description": (
            "Reverse mortgage consultation call.\n"
            f"{marker}\n"
            "ECG_SOURCE=barbara_agent\n\n"
            f"Lead Phone: {phone}\n"
            f"Notes: {notes or 'None'}"
        ),
        "busy": True,
        "when": {
            "start_time": start_unix,
            "end_time": end_unix,
            "start_timezone": broker_tz,
            "end_timezone": broker_tz
        },
        "participants": [
            {"name": lead_name, "email": lead_email}
        ] if lead_email else []
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
        # Use sync client - Nylas v3 US region API
        with httpx.Client(timeout=10.0) as client:
            response = client.post(
                f"https://api.us.nylas.com/v3/grants/{nylas_grant_id}/events?calendar_id={nylas_calendar_id}",
                headers={
                    "Authorization": f"Bearer {NYLAS_API_KEY}",
                    "Content-Type": "application/json"
                },
                json=event_data
            )
        
        if response.status_code in (200, 201):  # 201 = Created
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

            # Update appointment record with Nylas event id (stop race + enable webhook idempotency)
            try:
                if appointment_id:
                    update_appointment(
                        appointment_id,
                        {"nylas_event_id": event_id, "status": "scheduled"}
                    )
                else:
                    # Fallback: if we failed to create pre-book record, create it now (legacy behavior)
                    appointment_row2 = create_appointment(
                        lead_id=lead_id,
                        broker_id=broker_id,
                        appointment_time=appointment_dt.isoformat(),
                        nylas_event_id=event_id,
                        sms_consent=sms_consent,
                        status="scheduled",
                    )
                    appointment_id = appointment_row2.get("id") if appointment_row2 else None
            except Exception as e:
                logger.error(f"[BOOKING] Failed to update/create appointment record: {e}")
            
            # Trigger n8n to send personalized SMS from persona (with delay)
            # Only sends if sms_consent=True
            persona_name = (lead.get('persona_sender_name') or '').split()[0] if lead.get('persona_sender_name') else ''
            lead_first_name = lead.get('first_name', '')
            _trigger_persona_sms_webhook(
                to_number=phone,
                persona_name=persona_name,
                lead_first_name=lead_first_name,
                broker_name=broker_name,
                friendly_time=friendly_time,
                appointment_iso=appointment_dt.isoformat(),
                sms_consent=sms_consent
            )
            
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
            # Log full error details for debugging
            error_body = response.text[:500] if response.text else "No response body"
            logger.error(f"[BOOKING] Nylas API error: {response.status_code} - {error_body}")
            
            # Set manual booking required flag (sync)
            update_conversation_state(phone, {
                "conversation_data": {
                    "manual_booking_required": True,
                    "booking_error": f"Nylas API error: {response.status_code} - {error_body}"
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
    
    # Build requested time string for webhook notes
    requested_time_str = None
    if preferred_date or preferred_time:
        parts = [p for p in [preferred_date, preferred_time] if p]
        requested_time_str = " ".join(parts) if parts else None
    
    # Get lead to find assigned broker (sync)
    lead = get_lead_by_phone(phone)
    if not lead:
        # Trigger webhook - can't find lead
        _trigger_manual_booking_webhook(
            phone=phone,
            error="Lead not found during availability check",
            requested_time=requested_time_str,
            notes="Availability lookup failed - lead not found in database"
        )
        return SwaigFunctionResult(
            "I couldn't find your information. Let me connect you with our team."
        )
    
    lead_id = lead.get('id')
    
    # Get broker info
    broker = lead.get('brokers')
    if not broker:
        # Trigger webhook - no broker assigned
        _trigger_manual_booking_webhook(
            lead_id=lead_id,
            phone=phone,
            error="No broker assigned during availability check",
            requested_time=requested_time_str,
            notes="Availability lookup failed - no broker assigned to lead"
        )
        return SwaigFunctionResult(
            "I'll need to assign you a broker first. Let me connect you with our team."
        )
    
    broker_id = broker.get('id')
    
    broker_name = broker.get('contact_name', 'your broker')
    
    # Import availability service for real-time check
    try:
        from services.availability import fetch_broker_availability, format_slots_for_llm, filter_slots_by_time_of_day
        
        # Fetch fresh availability (in case pre-loaded slots are stale)
        slots = fetch_broker_availability(broker, days_ahead=7, max_slots=20)  # Get more slots for filtering
        
        if not slots:
            # Trigger webhook - availability fetch returned no slots
            _trigger_manual_booking_webhook(
                lead_id=lead_id,
                broker_id=broker_id,
                phone=phone,
                error="Nylas availability returned no slots",
                requested_time=requested_time_str,
                notes="Availability lookup failed - calendar returned no available slots"
            )
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
        
        # Trigger webhook - exception during availability check
        _trigger_manual_booking_webhook(
            lead_id=lead_id,
            broker_id=broker_id,
            phone=phone,
            error=f"Availability check exception: {str(e)}",
            requested_time=requested_time_str,
            notes="Availability lookup failed - exception during calendar check"
        )
        
        return SwaigFunctionResult(
            f"{broker_name} is generally available during business hours. "
            f"What day and time would work best for you?"
        )
