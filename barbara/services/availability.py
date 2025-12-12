"""
Broker availability service - Fetches available slots from Nylas
Uses broker business hours from database + Nylas calendar API

Note: Using sync httpx.Client() - SWAIG handlers run synchronously
"""

import os
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import pytz

try:
    import httpx
except ImportError:
    httpx = None

logger = logging.getLogger(__name__)

NYLAS_API_KEY = os.getenv("NYLAS_API_KEY")
NYLAS_API_BASE = "https://api.us.nylas.com/v3"


def fetch_broker_availability(
    broker: Dict[str, Any],
    days_ahead: int = 5,
    max_slots: int = 10
) -> List[Dict[str, Any]]:
    """
    Fetch available appointment slots for a broker.
    
    Uses Nylas Availability API with broker's business hours.
    Falls back to generated slots if Nylas unavailable.
    
    Args:
        broker: Broker dict with nylas_grant_id, timezone, business hours
        days_ahead: How many days ahead to check (default 5)
        max_slots: Maximum slots to return (default 10)
    
    Returns:
        List of slot dicts: [{"start": "2025-11-26T14:00:00-08:00", "display": "Tuesday Nov 26 at 2:00 PM"}, ...]
    """
    if not broker:
        logger.warning("[AVAILABILITY] No broker provided")
        return []
    
    nylas_grant_id = broker.get('nylas_grant_id')
    broker_email = (broker.get('email') or '').strip() if isinstance(broker.get('email'), str) else ''
    broker_tz_name = broker.get('timezone', 'America/Los_Angeles')
    
    # Get broker business hours with defaults
    business_start = broker.get('business_hours_start', '09:00:00')
    business_end = broker.get('business_hours_end', '17:00:00')
    business_days = broker.get('business_days', ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
    appointment_duration = broker.get('appointment_duration_minutes', 30)
    min_lead_time = broker.get('minimum_booking_lead_time_minutes', 60)
    
    # Parse time strings (handle "09:00:00" format from DB)
    if isinstance(business_start, str):
        business_start = business_start[:5]  # "09:00:00" -> "09:00"
    if isinstance(business_end, str):
        business_end = business_end[:5]  # "17:00:00" -> "17:00"
    
    # Convert days to Nylas format (0=Sunday, 1=Monday, etc.)
    day_map = {
        'sunday': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3,
        'thursday': 4, 'friday': 5, 'saturday': 6
    }
    nylas_days = [day_map.get(d.lower(), 1) for d in business_days]
    
    # Calculate time range
    broker_tz = pytz.timezone(broker_tz_name)
    now = datetime.now(broker_tz)
    
    # Start time = now + minimum lead time, rounded up to next 30-min slot
    start_dt = now + timedelta(minutes=min_lead_time)
    # Round up to next :00 or :30
    minutes = start_dt.minute
    if minutes < 30:
        start_dt = start_dt.replace(minute=30, second=0, microsecond=0)
    else:
        start_dt = start_dt.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    
    # End time = days_ahead from now
    end_dt = now + timedelta(days=days_ahead)
    
    # Convert to Unix timestamps for Nylas
    start_unix = int(start_dt.timestamp())
    end_unix = int(end_dt.timestamp())
    
    # Try Nylas API if available
    # Nylas v3 free/busy requires at least one email in the request body.
    if nylas_grant_id and broker_email and httpx and NYLAS_API_KEY:
        slots = _fetch_from_nylas(
            nylas_grant_id=nylas_grant_id,
            broker_email=broker_email,
            start_unix=start_unix,
            end_unix=end_unix,
            broker_tz_name=broker_tz_name,
            business_start=business_start,
            business_end=business_end,
            nylas_days=nylas_days,
            appointment_duration=appointment_duration,
            max_slots=max_slots
        )
        if slots:
            return slots
        logger.warning("[AVAILABILITY] Nylas returned no slots, falling back to generated")
    else:
        if not nylas_grant_id:
            logger.warning("[AVAILABILITY] Broker nylas_grant_id missing - using generated slots")
        elif not broker_email:
            logger.warning("[AVAILABILITY] Broker email missing - cannot query Nylas free/busy, using generated slots")
        else:
            logger.info("[AVAILABILITY] Nylas not configured (missing API key), using generated slots")
    
    # Fallback: Generate slots from business hours
    return _generate_slots(
        broker_tz=broker_tz,
        start_dt=start_dt,
        days_ahead=days_ahead,
        business_start=business_start,
        business_end=business_end,
        business_days=business_days,
        appointment_duration=appointment_duration,
        max_slots=max_slots
    )


def _fetch_from_nylas(
    nylas_grant_id: str,
    broker_email: str,
    start_unix: int,
    end_unix: int,
    broker_tz_name: str,
    business_start: str,
    business_end: str,
    nylas_days: List[int],
    appointment_duration: int,
    max_slots: int
) -> List[Dict[str, Any]]:
    """Fetch free/busy from Nylas API v3 using grant-specific endpoint"""
    try:
        # Nylas v3 free-busy endpoint: /v3/grants/{grant_id}/calendars/free-busy
        # This is more reliable than the global availability endpoint because it uses
        # grant_id directly in the URL, not requiring email matching
        request_body = {
            "start_time": start_unix,
            "end_time": end_unix,
            # Nylas v3 free/busy requires at least one email. Use the broker's email on file.
            "emails": [broker_email],
        }
        
        with httpx.Client(timeout=5.0) as client:
            # Grant-specific free-busy endpoint - uses grant_id in URL path
            response = client.post(
                f"{NYLAS_API_BASE}/grants/{nylas_grant_id}/calendars/free-busy",
                headers={
                    "Authorization": f"Bearer {NYLAS_API_KEY}",
                    "Content-Type": "application/json"
                },
                json=request_body
            )
        
        if response.status_code != 200:
            logger.error(f"[AVAILABILITY] Nylas API error: {response.status_code} - {response.text}")
            return []
        
        data = response.json()
        
        # Free-busy returns busy periods in data[].time_slots[]
        # We need to extract busy times and filter them from generated slots
        busy_periods = []
        for calendar_data in (data.get('data') or []):
            if not isinstance(calendar_data, dict):
                continue
            for busy_slot in (calendar_data.get('time_slots') or []):
                if not isinstance(busy_slot, dict):
                    continue
                busy_start = busy_slot.get('start_time')
                busy_end = busy_slot.get('end_time')
                if busy_start and busy_end:
                    busy_periods.append((busy_start, busy_end))
        
        logger.info(f"[AVAILABILITY] Nylas returned {len(busy_periods)} busy periods")
        
        # Generate all possible slots from business hours
        broker_tz = pytz.timezone(broker_tz_name)
        start_dt = datetime.fromtimestamp(start_unix, tz=broker_tz)
        
        all_slots = _generate_business_hour_slots(
            broker_tz=broker_tz,
            start_dt=start_dt,
            end_unix=end_unix,
            business_start=business_start,
            business_end=business_end,
            nylas_days=nylas_days,
            appointment_duration=appointment_duration,
            max_slots=max_slots * 3  # Generate more, we'll filter
        )
        
        # Filter out slots that overlap with busy periods
        available_slots = []
        for slot in all_slots:
            slot_start = slot['start_unix']
            slot_end = slot_start + (appointment_duration * 60)
            
            is_busy = False
            for busy_start, busy_end in busy_periods:
                # Check if slot overlaps with busy period
                if slot_start < busy_end and slot_end > busy_start:
                    is_busy = True
                    break
            
            if not is_busy:
                available_slots.append(slot)
                if len(available_slots) >= max_slots:
                    break
        
        logger.info(f"[AVAILABILITY] {len(available_slots)} slots available after filtering busy times")
        return available_slots
        
    except Exception as e:
        logger.error(f"[AVAILABILITY] Nylas fetch failed: {e}")
        return []


def _generate_business_hour_slots(
    broker_tz: Any,
    start_dt: datetime,
    end_unix: int,
    business_start: str,
    business_end: str,
    nylas_days: List[int],
    appointment_duration: int,
    max_slots: int
) -> List[Dict[str, Any]]:
    """Generate slots from business hours using Nylas day format (0=Sunday, 1=Monday, etc.)"""
    slots = []
    
    # Parse business hours
    start_hour, start_min = map(int, business_start.split(':'))
    end_hour, end_min = map(int, business_end.split(':'))
    
    # Convert Python weekday (0=Monday) to Nylas weekday (0=Sunday)
    # Python: Monday=0, Tuesday=1, ..., Sunday=6
    # Nylas:  Sunday=0, Monday=1, ..., Saturday=6
    
    current_date = start_dt.date()
    end_date = datetime.fromtimestamp(end_unix, tz=broker_tz).date()
    
    while current_date <= end_date and len(slots) < max_slots:
        # Convert Python weekday to Nylas format
        python_weekday = current_date.weekday()  # 0=Monday
        nylas_weekday = (python_weekday + 1) % 7  # Convert to 0=Sunday
        
        if nylas_weekday not in nylas_days:
            current_date += timedelta(days=1)
            continue
        
        # Generate slots for this day
        slot_time = broker_tz.localize(
            datetime.combine(current_date, datetime.min.time().replace(hour=start_hour, minute=start_min))
        )
        day_end = broker_tz.localize(
            datetime.combine(current_date, datetime.min.time().replace(hour=end_hour, minute=end_min))
        )
        
        while slot_time < day_end and len(slots) < max_slots:
            # Skip if slot is before our start time
            if slot_time >= start_dt:
                slots.append({
                    "start": slot_time.isoformat(),
                    "start_unix": int(slot_time.timestamp()),
                    "display": _format_slot_display(slot_time)
                })
            
            slot_time += timedelta(minutes=appointment_duration)
        
        current_date += timedelta(days=1)
    
    return slots


def _generate_slots(
    broker_tz: Any,
    start_dt: datetime,
    days_ahead: int,
    business_start: str,
    business_end: str,
    business_days: List[str],
    appointment_duration: int,
    max_slots: int
) -> List[Dict[str, Any]]:
    """Generate available slots from business hours (fallback when Nylas unavailable)"""
    slots = []
    
    # Parse business hours
    start_hour, start_min = map(int, business_start.split(':'))
    end_hour, end_min = map(int, business_end.split(':'))
    
    # Day name mapping
    day_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    current_date = start_dt.date()
    end_date = current_date + timedelta(days=days_ahead)
    
    while current_date <= end_date and len(slots) < max_slots:
        # Check if this day is a business day
        day_name = day_names[current_date.weekday()]
        if day_name not in [d.lower() for d in business_days]:
            current_date += timedelta(days=1)
            continue
        
        # Generate slots for this day
        slot_time = broker_tz.localize(
            datetime.combine(current_date, datetime.min.time().replace(hour=start_hour, minute=start_min))
        )
        day_end = broker_tz.localize(
            datetime.combine(current_date, datetime.min.time().replace(hour=end_hour, minute=end_min))
        )
        
        while slot_time < day_end and len(slots) < max_slots:
            # Skip if slot is in the past
            if slot_time > start_dt:
                slots.append({
                    "start": slot_time.isoformat(),
                    "start_unix": int(slot_time.timestamp()),
                    "display": _format_slot_display(slot_time)
                })
            
            slot_time += timedelta(minutes=appointment_duration)
        
        current_date += timedelta(days=1)
    
    logger.info(f"[AVAILABILITY] Generated {len(slots)} slots from business hours")
    return slots


def _format_slot_display(dt: datetime) -> str:
    """Format datetime for display: 'Tuesday Nov 26 at 2:00 PM'"""
    # NOTE: Avoid platform-specific strftime modifiers like "%-I" (fails on Windows).
    # Format "2:00 PM" by using "%I" and stripping the leading zero.
    time_part = dt.strftime("%I:%M %p")
    # Only strip a single leading zero (e.g., "09:00 AM" -> "9:00 AM").
    # Using lstrip("0") is broader than intended.
    if time_part.startswith("0"):
        time_part = time_part[1:]
    return f"{dt.strftime('%A %b')} {dt.day} at {time_part}"


def filter_slots_by_time_of_day(slots: List[Dict[str, Any]], time_preference: str, broker_tz_name: str = 'America/Los_Angeles') -> List[Dict[str, Any]]:
    """
    Filter slots by time of day preference.
    
    Args:
        slots: List of slot dicts with 'start' ISO datetime strings
        time_preference: "morning" (before 12 PM), "afternoon" (12 PM and later), or None
        broker_tz_name: Timezone name for the broker
    
    Returns:
        Filtered list of slots
    """
    if not time_preference or not slots:
        return slots
    
    broker_tz = pytz.timezone(broker_tz_name)
    filtered = []
    
    time_pref_lower = time_preference.lower()
    
    for slot in slots:
        # Parse the ISO datetime string
        slot_start = slot.get('start')
        if not slot_start:
            continue
        
        try:
            # Handle both ISO string and Unix timestamp
            if isinstance(slot_start, str):
                slot_dt = datetime.fromisoformat(slot_start.replace('Z', '+00:00'))
                if slot_dt.tzinfo is None:
                    slot_dt = broker_tz.localize(slot_dt)
            elif isinstance(slot_start, (int, float)):
                slot_dt = datetime.fromtimestamp(slot_start, tz=broker_tz)
            else:
                continue
            
            hour = slot_dt.hour
            
            # Filter based on time preference
            if time_pref_lower in ['morning', 'am']:
                # Morning = before 12 PM (hour < 12)
                if hour < 12:
                    filtered.append(slot)
            elif time_pref_lower in ['afternoon', 'pm', 'evening']:
                # Afternoon = 12 PM and later (hour >= 12)
                if hour >= 12:
                    filtered.append(slot)
            else:
                # Unknown preference, include all
                filtered.append(slot)
                
        except Exception as e:
            logger.warning(f"[AVAILABILITY] Error filtering slot {slot_start}: {e}")
            continue
    
    return filtered


def format_slots_for_llm(slots: List[Dict[str, Any]], max_display: int = 5) -> str:
    """Format slots as a readable string for the LLM prompt"""
    if not slots:
        return "No available slots found. Ask the caller for their preferred time."
    
    lines = [f"- {slot['display']}" for slot in slots[:max_display]]
    
    if len(slots) > max_display:
        lines.append(f"- ...and {len(slots) - max_display} more slots available")
    
    return "\n".join(lines)


