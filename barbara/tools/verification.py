"""
Granular verification tools - Mark individual verification steps

Per Section 4.21 (Results & Actions): Return SwaigFunctionResult
Per Section 6.16.2.3: Use .update_global_data() for real-time AI state awareness
Per Section 3.18.8: All calls are sync

Ported from Reference/reference-swaig-agent/tools/verification.py
Enhanced with global_data updates for real-time prompt variable changes
"""

import os
import logging
from signalwire_agents.core.function_result import SwaigFunctionResult

from services.database import (
    get_lead_by_phone,
    update_conversation_state,
    normalize_phone
)

logger = logging.getLogger(__name__)

# Try to import supabase for lead updates
try:
    from supabase import create_client
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_KEY")
    if supabase_url and supabase_key:
        sb = create_client(supabase_url, supabase_key)
    else:
        sb = None
except Exception:
    sb = None


def _check_and_set_verified(phone: str) -> bool:
    """
    Check if all three granular verifications are complete.
    If so, set the main 'verified' flag on conversation_state.
    Returns True if fully verified, False otherwise.
    """
    if not sb:
        return False
    
    lead = get_lead_by_phone(phone)
    if not lead:
        return False
    
    phone_verified = lead.get('phone_verified', False)
    email_verified = lead.get('email_verified', False)
    address_verified = lead.get('address_verified', False)
    
    if phone_verified and email_verified and address_verified:
        update_conversation_state(phone, {
            "conversation_data": {"verified": True}
        })
        logger.info(f"[VERIFY] All verifications complete for {phone}, setting verified=true")
        return True
    
    return False


def handle_mark_phone_verified(phone: str) -> SwaigFunctionResult:
    """Mark phone number as verified"""
    phone = normalize_phone(phone)
    
    lead = get_lead_by_phone(phone)
    if not lead:
        return SwaigFunctionResult(
            "I couldn't find your information."
        )
    
    lead_id = lead.get('id')
    
    if sb and lead_id:
        try:
            sb.table("leads")\
                .update({"phone_verified": True})\
                .eq("id", lead_id)\
                .execute()
            
            logger.info(f"[VERIFY] Phone verified for lead {lead_id}")
            
            # Check if all verifications complete
            fully_verified = _check_and_set_verified(phone)
            
            # Per Section 6.16.2.3: Update global_data so AI sees change immediately
            global_updates = {"phone_verified": True}
            if fully_verified:
                global_updates["verified"] = True
            
            return (
                SwaigFunctionResult("Phone number verified")
                .update_global_data(global_updates)
            )
        except Exception as e:
            logger.error(f"[VERIFY] Error marking phone verified: {e}")
    
    return SwaigFunctionResult("Error verifying phone")


def handle_mark_email_verified(phone: str) -> SwaigFunctionResult:
    """Mark email address as verified"""
    phone = normalize_phone(phone)
    
    lead = get_lead_by_phone(phone)
    if not lead:
        return SwaigFunctionResult(
            "I couldn't find your information."
        )
    
    lead_id = lead.get('id')
    
    if sb and lead_id:
        try:
            sb.table("leads")\
                .update({"email_verified": True})\
                .eq("id", lead_id)\
                .execute()
            
            logger.info(f"[VERIFY] Email verified for lead {lead_id}")
            
            # Check if all verifications complete
            fully_verified = _check_and_set_verified(phone)
            
            global_updates = {"email_verified": True}
            if fully_verified:
                global_updates["verified"] = True
            
            return (
                SwaigFunctionResult("Email verified")
                .update_global_data(global_updates)
            )
        except Exception as e:
            logger.error(f"[VERIFY] Error marking email verified: {e}")
    
    return SwaigFunctionResult("Error verifying email")


def handle_mark_address_verified(phone: str) -> SwaigFunctionResult:
    """Mark property address as verified"""
    phone = normalize_phone(phone)
    
    lead = get_lead_by_phone(phone)
    if not lead:
        return SwaigFunctionResult(
            "I couldn't find your information."
        )
    
    lead_id = lead.get('id')
    
    if sb and lead_id:
        try:
            sb.table("leads")\
                .update({"address_verified": True})\
                .eq("id", lead_id)\
                .execute()
            
            logger.info(f"[VERIFY] Address verified for lead {lead_id}")
            
            # Check if all verifications complete
            fully_verified = _check_and_set_verified(phone)
            
            global_updates = {"address_verified": True}
            if fully_verified:
                global_updates["verified"] = True
            
            return (
                SwaigFunctionResult("Property address verified")
                .update_global_data(global_updates)
            )
        except Exception as e:
            logger.error(f"[VERIFY] Error marking address verified: {e}")
    
    return SwaigFunctionResult("Error verifying address")
