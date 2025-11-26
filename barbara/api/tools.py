"""
REST API endpoints for MCP/n8n integration.

These endpoints expose the same functionality as the SWAIG tools
but via HTTP REST API for external orchestration.

Endpoints:
- POST /api/tools/check_broker_availability
- POST /api/tools/book_appointment
- POST /api/tools/cancel_appointment
- POST /api/tools/reschedule_appointment
- POST /api/tools/update_lead_info
"""

import os
import logging
from datetime import datetime
from typing import Optional
import pytz

from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

# Import services
from services.database import (
    get_lead_by_phone,
    normalize_phone
)
from services.availability import fetch_broker_availability, format_slots_for_llm, filter_slots_by_time_of_day

logger = logging.getLogger(__name__)

# API Key for authentication (optional)
API_KEY = os.getenv("BARBARA_API_KEY")

# Supabase client for direct updates
try:
    from supabase import create_client
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_KEY")
    if supabase_url and supabase_key:
        supabase = create_client(supabase_url, supabase_key)
    else:
        supabase = None
except Exception:
    supabase = None

# Nylas config
NYLAS_API_KEY = os.getenv("NYLAS_API_KEY")
NYLAS_API_BASE = "https://api.us.nylas.com/v3"

try:
    import httpx
except ImportError:
    httpx = None


def verify_api_key(request: Request) -> bool:
    """Verify API key if configured"""
    if not API_KEY:
        return True  # No auth required if not configured
    
    auth_header = request.headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        token = auth_header[7:]
        return token == API_KEY
    return False


async def check_broker_availability(request: Request) -> JSONResponse:
    """
    Check broker calendar availability.
    
    Request body:
    {
        "broker_id": "uuid",
        "preferred_day": "monday" | "tuesday" | ... | "any",
        "preferred_time": "morning" | "afternoon" | "any"
    }
    """
    if not verify_api_key(request):
        return JSONResponse({"success": False, "error": "Unauthorized"}, status_code=401)
    
    try:
        body = await request.json()
    except Exception:
        return JSONResponse({"success": False, "error": "Invalid JSON"}, status_code=400)
    
    broker_id = body.get("broker_id")
    preferred_day = body.get("preferred_day")
    preferred_time = body.get("preferred_time")
    
    if not broker_id:
        return JSONResponse({"success": False, "error": "broker_id is required"}, status_code=400)
    
    # Look up broker from Supabase
    if not supabase:
        return JSONResponse({"success": False, "error": "Database not configured"}, status_code=500)
    
    try:
        result = supabase.table("brokers").select("*").eq("id", broker_id).single().execute()
        broker = result.data if result else None
    except Exception as e:
        logger.error(f"[API] Error fetching broker: {e}")
        return JSONResponse({"success": False, "error": f"Broker not found: {broker_id}"}, status_code=404)
    
    if not broker:
        return JSONResponse({"success": False, "error": f"Broker not found: {broker_id}"}, status_code=404)
    
    # Fetch availability
    slots = fetch_broker_availability(broker, days_ahead=14, max_slots=20)
    
    # Filter by time preference if specified
    if preferred_time and preferred_time != "any":
        broker_tz = broker.get("timezone", "America/Los_Angeles")
        slots = filter_slots_by_time_of_day(slots, preferred_time, broker_tz)
    
    broker_name = broker.get("contact_name", "Broker")
    
    return JSONResponse({
        "success": True,
        "broker_id": broker_id,
        "broker_name": broker_name,
        "available_slots": slots,
        "message": f"Found {len(slots)} available slots for {broker_name}"
    })


async def book_appointment(request: Request) -> JSONResponse:
    """
    Book an appointment with a broker.
    
    Request body:
    {
        "lead_id": "uuid",
        "broker_id": "uuid",
        "scheduled_for": "2025-01-15T14:00:00Z",
        "notes": "optional notes"
    }
    """
    if not verify_api_key(request):
        return JSONResponse({"success": False, "error": "Unauthorized"}, status_code=401)
    
    try:
        body = await request.json()
    except Exception:
        return JSONResponse({"success": False, "error": "Invalid JSON"}, status_code=400)
    
    lead_id = body.get("lead_id")
    broker_id = body.get("broker_id")
    scheduled_for = body.get("scheduled_for")
    notes = body.get("notes", "")
    
    if not all([lead_id, broker_id, scheduled_for]):
        return JSONResponse({
            "success": False, 
            "error": "lead_id, broker_id, and scheduled_for are required"
        }, status_code=400)
    
    if not supabase:
        return JSONResponse({"success": False, "error": "Database not configured"}, status_code=500)
    
    # Get lead and broker
    try:
        lead_result = supabase.table("leads").select("*").eq("id", lead_id).single().execute()
        lead = lead_result.data if lead_result else None
        
        broker_result = supabase.table("brokers").select("*").eq("id", broker_id).single().execute()
        broker = broker_result.data if broker_result else None
    except Exception as e:
        logger.error(f"[API] Error fetching lead/broker: {e}")
        return JSONResponse({"success": False, "error": str(e)}, status_code=500)
    
    if not lead:
        return JSONResponse({"success": False, "error": f"Lead not found: {lead_id}"}, status_code=404)
    if not broker:
        return JSONResponse({"success": False, "error": f"Broker not found: {broker_id}"}, status_code=404)
    
    # Parse scheduled time
    try:
        from dateutil import parser as date_parser
        appointment_dt = date_parser.parse(scheduled_for)
    except Exception as e:
        return JSONResponse({"success": False, "error": f"Invalid date format: {scheduled_for}"}, status_code=400)
    
    broker_tz_name = broker.get("timezone", "America/Los_Angeles")
    duration_minutes = broker.get("appointment_duration_minutes", 30)
    
    # Calculate Unix timestamps for Nylas
    start_unix = int(appointment_dt.timestamp())
    end_unix = start_unix + (duration_minutes * 60)
    
    # Create Nylas event
    nylas_grant_id = broker.get("nylas_grant_id")
    calendar_invite_sent = False
    event_id = None
    
    if nylas_grant_id and NYLAS_API_KEY and httpx:
        try:
            event_data = {
                "title": f"Reverse Mortgage Consultation - {lead.get('first_name', 'Client')}",
                "description": f"Reverse mortgage consultation.\n\nLead: {lead.get('first_name', '')} {lead.get('last_name', '')}\nPhone: {lead.get('primary_phone', '')}\nNotes: {notes or 'None'}",
                "when": {
                    "start_time": start_unix,
                    "end_time": end_unix,
                },
                "participants": []
            }
            
            # Add lead email as participant if available
            if lead.get("primary_email"):
                event_data["participants"].append({"email": lead["primary_email"]})
            
            with httpx.Client(timeout=10.0) as client:
                response = client.post(
                    f"{NYLAS_API_BASE}/grants/{nylas_grant_id}/events?calendar_id=primary",
                    headers={
                        "Authorization": f"Bearer {NYLAS_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json=event_data
                )
            
            if response.status_code in [200, 201]:
                result = response.json()
                event_id = result.get("data", {}).get("id")
                calendar_invite_sent = bool(lead.get("primary_email"))
                logger.info(f"[API] Nylas event created: {event_id}")
            else:
                logger.error(f"[API] Nylas API error: {response.status_code} - {response.text}")
                
        except Exception as e:
            logger.error(f"[API] Nylas booking error: {e}")
    
    # Create interaction record in Supabase
    try:
        interaction_data = {
            "lead_id": lead_id,
            "broker_id": broker_id,
            "type": "appointment",
            "direction": "outbound",
            "scheduled_for": scheduled_for,
            "outcome": "appointment_booked",
            "content": notes,
            "metadata": {
                "nylas_event_id": event_id,
                "source": "mcp_api"
            }
        }
        
        supabase.table("interactions").insert(interaction_data).execute()
        logger.info(f"[API] Appointment booked: lead={lead_id}, broker={broker_id}, time={scheduled_for}")
        
    except Exception as e:
        logger.error(f"[API] Error creating interaction: {e}")
    
    # Format friendly time for response
    broker_tz = pytz.timezone(broker_tz_name)
    friendly_time = appointment_dt.astimezone(broker_tz).strftime("%A, %B %d at %-I:%M %p %Z")
    
    return JSONResponse({
        "success": True,
        "appointment_id": event_id,
        "lead_id": lead_id,
        "broker_id": broker_id,
        "scheduled_for": scheduled_for,
        "friendly_time": friendly_time,
        "calendar_invite_sent": calendar_invite_sent,
        "message": f"Appointment booked for {friendly_time}"
    })


async def cancel_appointment(request: Request) -> JSONResponse:
    """
    Cancel an existing appointment.
    
    Request body:
    {
        "lead_id": "uuid"
    }
    """
    if not verify_api_key(request):
        return JSONResponse({"success": False, "error": "Unauthorized"}, status_code=401)
    
    try:
        body = await request.json()
    except Exception:
        return JSONResponse({"success": False, "error": "Invalid JSON"}, status_code=400)
    
    lead_id = body.get("lead_id")
    
    if not lead_id:
        return JSONResponse({"success": False, "error": "lead_id is required"}, status_code=400)
    
    if not supabase:
        return JSONResponse({"success": False, "error": "Database not configured"}, status_code=500)
    
    # Find the most recent scheduled appointment for this lead
    try:
        result = supabase.table("interactions")\
            .select("*, brokers!broker_id(nylas_grant_id, contact_name)")\
            .eq("lead_id", lead_id)\
            .eq("type", "appointment")\
            .eq("outcome", "appointment_booked")\
            .order("scheduled_for", desc=True)\
            .limit(1)\
            .execute()
        
        if not result.data:
            return JSONResponse({
                "success": False, 
                "error": "No active appointment found for this lead"
            }, status_code=404)
        
        appointment = result.data[0]
        appointment_id = appointment.get("id")
        nylas_event_id = appointment.get("metadata", {}).get("nylas_event_id")
        broker = appointment.get("brokers", {})
        nylas_grant_id = broker.get("nylas_grant_id") if broker else None
        
        # Cancel Nylas event if exists
        if nylas_event_id and nylas_grant_id and NYLAS_API_KEY and httpx:
            try:
                with httpx.Client(timeout=10.0) as client:
                    response = client.delete(
                        f"{NYLAS_API_BASE}/grants/{nylas_grant_id}/events/{nylas_event_id}?calendar_id=primary",
                        headers={"Authorization": f"Bearer {NYLAS_API_KEY}"}
                    )
                if response.status_code in [200, 204]:
                    logger.info(f"[API] Nylas event deleted: {nylas_event_id}")
                else:
                    logger.warning(f"[API] Nylas delete failed: {response.status_code}")
            except Exception as e:
                logger.error(f"[API] Nylas cancel error: {e}")
        
        # Update interaction record
        supabase.table("interactions")\
            .update({"outcome": "cancelled", "metadata": {**appointment.get("metadata", {}), "cancelled_at": datetime.utcnow().isoformat()}})\
            .eq("id", appointment_id)\
            .execute()
        
        return JSONResponse({
            "success": True,
            "cancelled_appointment": {
                "id": appointment_id,
                "scheduled_for": appointment.get("scheduled_for"),
                "broker_name": broker.get("contact_name") if broker else None
            },
            "message": "Appointment cancelled successfully"
        })
        
    except Exception as e:
        logger.error(f"[API] Cancel appointment error: {e}")
        return JSONResponse({"success": False, "error": str(e)}, status_code=500)


async def reschedule_appointment(request: Request) -> JSONResponse:
    """
    Reschedule an existing appointment.
    
    Request body:
    {
        "lead_id": "uuid",
        "new_scheduled_for": "2025-01-15T14:00:00Z"
    }
    """
    if not verify_api_key(request):
        return JSONResponse({"success": False, "error": "Unauthorized"}, status_code=401)
    
    try:
        body = await request.json()
    except Exception:
        return JSONResponse({"success": False, "error": "Invalid JSON"}, status_code=400)
    
    lead_id = body.get("lead_id")
    new_scheduled_for = body.get("new_scheduled_for")
    
    if not all([lead_id, new_scheduled_for]):
        return JSONResponse({
            "success": False, 
            "error": "lead_id and new_scheduled_for are required"
        }, status_code=400)
    
    if not supabase:
        return JSONResponse({"success": False, "error": "Database not configured"}, status_code=500)
    
    # Parse new time
    try:
        from dateutil import parser as date_parser
        new_dt = date_parser.parse(new_scheduled_for)
    except Exception:
        return JSONResponse({"success": False, "error": f"Invalid date format: {new_scheduled_for}"}, status_code=400)
    
    # Find existing appointment
    try:
        result = supabase.table("interactions")\
            .select("*, brokers!broker_id(nylas_grant_id, contact_name, timezone, appointment_duration_minutes)")\
            .eq("lead_id", lead_id)\
            .eq("type", "appointment")\
            .eq("outcome", "appointment_booked")\
            .order("scheduled_for", desc=True)\
            .limit(1)\
            .execute()
        
        if not result.data:
            return JSONResponse({
                "success": False, 
                "error": "No active appointment found for this lead"
            }, status_code=404)
        
        appointment = result.data[0]
        old_scheduled_for = appointment.get("scheduled_for")
        appointment_id = appointment.get("id")
        nylas_event_id = appointment.get("metadata", {}).get("nylas_event_id")
        broker = appointment.get("brokers", {})
        nylas_grant_id = broker.get("nylas_grant_id") if broker else None
        duration_minutes = broker.get("appointment_duration_minutes", 30) if broker else 30
        broker_tz_name = broker.get("timezone", "America/Los_Angeles") if broker else "America/Los_Angeles"
        
        # Update Nylas event if exists
        calendar_invite_sent = False
        if nylas_event_id and nylas_grant_id and NYLAS_API_KEY and httpx:
            try:
                start_unix = int(new_dt.timestamp())
                end_unix = start_unix + (duration_minutes * 60)
                
                with httpx.Client(timeout=10.0) as client:
                    response = client.put(
                        f"{NYLAS_API_BASE}/grants/{nylas_grant_id}/events/{nylas_event_id}?calendar_id=primary",
                        headers={
                            "Authorization": f"Bearer {NYLAS_API_KEY}",
                            "Content-Type": "application/json"
                        },
                        json={
                            "when": {
                                "start_time": start_unix,
                                "end_time": end_unix
                            }
                        }
                    )
                
                if response.status_code == 200:
                    calendar_invite_sent = True
                    logger.info(f"[API] Nylas event updated: {nylas_event_id}")
                else:
                    logger.warning(f"[API] Nylas update failed: {response.status_code}")
                    
            except Exception as e:
                logger.error(f"[API] Nylas reschedule error: {e}")
        
        # Update interaction record
        supabase.table("interactions")\
            .update({
                "scheduled_for": new_scheduled_for,
                "metadata": {
                    **appointment.get("metadata", {}),
                    "rescheduled_at": datetime.utcnow().isoformat(),
                    "old_scheduled_for": old_scheduled_for
                }
            })\
            .eq("id", appointment_id)\
            .execute()
        
        # Format friendly time
        broker_tz = pytz.timezone(broker_tz_name)
        friendly_time = new_dt.astimezone(broker_tz).strftime("%A, %B %d at %-I:%M %p %Z")
        
        return JSONResponse({
            "success": True,
            "old_scheduled_for": old_scheduled_for,
            "new_scheduled_for": new_scheduled_for,
            "friendly_time": friendly_time,
            "calendar_invite_sent": calendar_invite_sent,
            "message": f"Appointment rescheduled to {friendly_time}"
        })
        
    except Exception as e:
        logger.error(f"[API] Reschedule error: {e}")
        return JSONResponse({"success": False, "error": str(e)}, status_code=500)


async def update_lead_info(request: Request) -> JSONResponse:
    """
    Update lead contact information.
    
    Request body:
    {
        "lead_id": "uuid",
        "first_name": "optional",
        "last_name": "optional",
        "primary_phone": "optional",
        "primary_email": "optional",
        "city": "optional",
        "state": "optional",
        "zipcode": "optional",
        "age": optional int,
        "property_value": optional number,
        "mortgage_balance": optional number
    }
    """
    if not verify_api_key(request):
        return JSONResponse({"success": False, "error": "Unauthorized"}, status_code=401)
    
    try:
        body = await request.json()
    except Exception:
        return JSONResponse({"success": False, "error": "Invalid JSON"}, status_code=400)
    
    lead_id = body.get("lead_id")
    
    if not lead_id:
        return JSONResponse({"success": False, "error": "lead_id is required"}, status_code=400)
    
    if not supabase:
        return JSONResponse({"success": False, "error": "Database not configured"}, status_code=500)
    
    # Build update dict with provided fields
    field_mapping = {
        "first_name": "first_name",
        "last_name": "last_name",
        "primary_phone": "primary_phone",
        "primary_email": "primary_email",
        "city": "property_city",
        "state": "property_state",
        "zipcode": "property_zip",
        "age": "age",
        "property_value": "property_value",
        "mortgage_balance": "mortgage_balance"
    }
    
    updates = {}
    for api_field, db_field in field_mapping.items():
        if api_field in body and body[api_field] is not None:
            updates[db_field] = body[api_field]
    
    if not updates:
        return JSONResponse({
            "success": False, 
            "error": "No fields to update"
        }, status_code=400)
    
    try:
        result = supabase.table("leads")\
            .update(updates)\
            .eq("id", lead_id)\
            .execute()
        
        if result.data:
            logger.info(f"[API] Lead updated: {lead_id}, fields: {list(updates.keys())}")
            return JSONResponse({
                "success": True,
                "lead_id": lead_id,
                "updated_fields": list(updates.keys()),
                "message": f"Updated {len(updates)} field(s)"
            })
        else:
            return JSONResponse({
                "success": False, 
                "error": f"Lead not found: {lead_id}"
            }, status_code=404)
            
    except Exception as e:
        logger.error(f"[API] Update lead error: {e}")
        return JSONResponse({"success": False, "error": str(e)}, status_code=500)


async def health_check(request: Request) -> JSONResponse:
    """Health check endpoint"""
    return JSONResponse({
        "status": "healthy",
        "service": "barbara-agent-api",
        "timestamp": datetime.utcnow().isoformat()
    })


# Define routes
routes = [
    Route("/api/health", health_check, methods=["GET"]),
    Route("/api/tools/check_broker_availability", check_broker_availability, methods=["POST"]),
    Route("/api/tools/book_appointment", book_appointment, methods=["POST"]),
    Route("/api/tools/cancel_appointment", cancel_appointment, methods=["POST"]),
    Route("/api/tools/reschedule_appointment", reschedule_appointment, methods=["POST"]),
    Route("/api/tools/update_lead_info", update_lead_info, methods=["POST"]),
]

# Create Starlette app with CORS
middleware = [
    Middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
]

api_app = Starlette(routes=routes, middleware=middleware)

