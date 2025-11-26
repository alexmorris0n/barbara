"""
Granular qualification tools - Mark individual qualification criteria

Per Section 4.21 (Results & Actions): Return SwaigFunctionResult
Per Section 6.16.2.3: Use .update_global_data() for real-time AI state awareness
Per Section 3.18.8: All calls are sync

Ported from Reference/reference-swaig-agent/tools/qualification.py
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


def _check_and_set_qualified(phone: str) -> bool:
    """
    Check if all four qualification criteria are met.
    If so, set the main 'qualified' flag on conversation_state and leads.
    Returns True if fully qualified, False otherwise.
    """
    if not sb:
        return False
    
    lead = get_lead_by_phone(phone)
    if not lead:
        return False
    
    age_qualified = lead.get('age_qualified', False)
    homeowner_qualified = lead.get('homeowner_qualified', False)
    primary_residence_qualified = lead.get('primary_residence_qualified', False)
    equity_qualified = lead.get('equity_qualified', False)
    
    if age_qualified and homeowner_qualified and primary_residence_qualified and equity_qualified:
        # Update both conversation_state and leads (sync)
        update_conversation_state(phone, {
            "qualified": True,
            "conversation_data": {"qualified": True}
        })
        
        # Update lead as well
        lead_id = lead.get('id')
        if lead_id:
            try:
                sb.table("leads")\
                    .update({"qualified": True})\
                    .eq("id", lead_id)\
                    .execute()
            except Exception as e:
                logger.error(f"[QUALIFY] Error setting qualified on lead: {e}")
        
        logger.info(f"[QUALIFY] All qualifications complete for {phone}, setting qualified=true")
        return True
    
    return False


def handle_mark_age_qualified(phone: str) -> SwaigFunctionResult:
    """Mark that caller is 62+ (FHA requirement)"""
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
                .update({"age_qualified": True})\
                .eq("id", lead_id)\
                .execute()
            
            logger.info(f"[QUALIFY] Age qualified for lead {lead_id}")
            
            # Check if all qualifications complete
            fully_qualified = _check_and_set_qualified(phone)
            
            global_updates = {"age_qualified": True}
            if fully_qualified:
                global_updates["qualified"] = True
            
            return (
                SwaigFunctionResult("Age requirement confirmed")
                .update_global_data(global_updates)
            )
        except Exception as e:
            logger.error(f"[QUALIFY] Error marking age qualified: {e}")
    
    return SwaigFunctionResult("Error updating age qualification")


def handle_mark_homeowner_qualified(phone: str) -> SwaigFunctionResult:
    """Mark that caller owns the property"""
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
                .update({"homeowner_qualified": True})\
                .eq("id", lead_id)\
                .execute()
            
            logger.info(f"[QUALIFY] Homeowner qualified for lead {lead_id}")
            
            # Check if all qualifications complete
            fully_qualified = _check_and_set_qualified(phone)
            
            global_updates = {"homeowner_qualified": True}
            if fully_qualified:
                global_updates["qualified"] = True
            
            return (
                SwaigFunctionResult("Homeownership confirmed")
                .update_global_data(global_updates)
            )
        except Exception as e:
            logger.error(f"[QUALIFY] Error marking homeowner qualified: {e}")
    
    return SwaigFunctionResult("Error updating homeowner qualification")


def handle_mark_primary_residence_qualified(phone: str) -> SwaigFunctionResult:
    """Mark that property is caller's primary residence"""
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
                .update({"primary_residence_qualified": True})\
                .eq("id", lead_id)\
                .execute()
            
            logger.info(f"[QUALIFY] Primary residence qualified for lead {lead_id}")
            
            # Check if all qualifications complete
            fully_qualified = _check_and_set_qualified(phone)
            
            global_updates = {"primary_residence_qualified": True}
            if fully_qualified:
                global_updates["qualified"] = True
            
            return (
                SwaigFunctionResult("Primary residence confirmed")
                .update_global_data(global_updates)
            )
        except Exception as e:
            logger.error(f"[QUALIFY] Error marking primary residence qualified: {e}")
    
    return SwaigFunctionResult("Error updating primary residence qualification")


def handle_mark_equity_qualified(phone: str) -> SwaigFunctionResult:
    """Mark that caller has sufficient equity"""
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
                .update({"equity_qualified": True})\
                .eq("id", lead_id)\
                .execute()
            
            logger.info(f"[QUALIFY] Equity qualified for lead {lead_id}")
            
            # Check if all qualifications complete
            fully_qualified = _check_and_set_qualified(phone)
            
            global_updates = {"equity_qualified": True}
            if fully_qualified:
                global_updates["qualified"] = True
            
            return (
                SwaigFunctionResult("Equity requirement confirmed")
                .update_global_data(global_updates)
            )
        except Exception as e:
            logger.error(f"[QUALIFY] Error marking equity qualified: {e}")
    
    return SwaigFunctionResult("Error updating equity qualification")
