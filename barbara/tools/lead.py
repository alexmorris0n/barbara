"""
Lead management tools
Verify identity and update lead information

Per Section 4.21 (Results & Actions): Return SwaigFunctionResult
Per Section 6.16.2.3: Use .update_global_data() for real-time AI state awareness
Per Section 3.18.8: All calls are sync

Ported from Reference/reference-swaig-agent/tools/lead.py
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


def handle_verify_caller_identity(phone: str, first_name: str) -> SwaigFunctionResult:
    """
    Verify caller identity by name and phone
    Creates a new lead if phone not found
    """
    phone = normalize_phone(phone)
    
    if not first_name:
        return SwaigFunctionResult(
            "Could you please tell me your name?"
        )
    
    # Look up lead (sync)
    lead = get_lead_by_phone(phone)
    
    if lead:
        lead_name = lead.get('first_name', '')
        
        # Check if name matches
        if lead_name and lead_name.lower() == first_name.lower():
            # Match! Mark as verified (sync)
            update_conversation_state(phone, {
                "conversation_data": {"verified": True}
            })
            
            logger.info(f"[LEAD] Identity verified for {phone} (name: {first_name})")
            
            # Update global_data so AI uses correct name immediately
            return (
                SwaigFunctionResult(
                    f"Great, I've confirmed your identity, {first_name}. How can I help you today?"
                )
                .update_global_data({
                    "verified": True,
                    "caller_name": first_name
                })
            )
        else:
            # Name doesn't match but phone number found
            logger.warning(f"[LEAD] Name mismatch for {phone}: expected '{lead_name}', got '{first_name}'")
            
            return SwaigFunctionResult(
                f"I have a different name on file for this phone number. "
                f"Can you confirm your full name and address?"
            )
    else:
        # New caller - create lead
        if sb:
            try:
                new_lead = {
                    "first_name": first_name,
                    "primary_phone": phone,
                    "primary_phone_e164": phone,
                    "status": "new",
                    "source": "signalwire_inbound"
                }
                
                result = sb.table("leads").insert(new_lead).execute()
                
                if result.data:
                    logger.info(f"[LEAD] Created new lead for {phone} (name: {first_name})")
                    
                    # Mark as verified since we just created (sync)
                    update_conversation_state(phone, {
                        "conversation_data": {"verified": True}
                    })
                    
                    # Update global_data for new caller
                    new_lead_id = result.data[0].get('id', '') if result.data else ''
                    return (
                        SwaigFunctionResult(
                            f"Nice to meet you, {first_name}! "
                            f"I've created a record for you. How can I help you today?"
                        )
                        .update_global_data({
                            "caller_name": first_name,
                            "verified": True,
                            "lead_id": new_lead_id,
                            "lead_status": "new"
                        })
                    )
            except Exception as e:
                logger.error(f"[LEAD] Error creating lead: {e}")
        
        # Even without DB, update global_data with their name
        return (
            SwaigFunctionResult(
                f"Nice to meet you, {first_name}. "
                f"I don't have your information on file yet. "
                f"Would you like me to tell you about reverse mortgages?"
            )
            .update_global_data({"caller_name": first_name})
        )


def handle_update_lead_info(
    phone: str,
    first_name: str = None,
    last_name: str = None,
    property_address: str = None,
    property_city: str = None,
    property_state: str = None,
    property_zip: str = None,
    age: int = None,
    property_value: float = None,
    estimated_equity: float = None,
    mortgage_balance: float = None
) -> SwaigFunctionResult:
    """Update lead information in the database"""
    phone = normalize_phone(phone)
    
    # Get existing lead (sync)
    lead = get_lead_by_phone(phone)
    
    if not lead:
        return SwaigFunctionResult(
            "I couldn't find your information. Let me verify your identity first."
        )
    
    lead_id = lead.get('id')
    if not lead_id:
        return SwaigFunctionResult(
            "I couldn't update your information. Let me transfer you to someone who can help."
        )
    
    # Build update dict with only provided fields
    updates = {}
    if first_name:
        updates['first_name'] = first_name
    if last_name:
        updates['last_name'] = last_name
    if property_address:
        updates['property_address'] = property_address
    if property_city:
        updates['property_city'] = property_city
    if property_state:
        updates['property_state'] = property_state
    if property_zip:
        updates['property_zip'] = property_zip
    if age is not None:
        updates['age'] = age
    if property_value is not None:
        updates['property_value'] = property_value
        updates['estimated_property_value'] = property_value  # Alias
    if estimated_equity is not None:
        updates['estimated_equity'] = estimated_equity
    if mortgage_balance is not None:
        updates['mortgage_balance'] = mortgage_balance
    
    if not updates:
        return SwaigFunctionResult(
            "No information to update. What would you like me to change?"
        )
    
    # Update in database (sync)
    if sb:
        try:
            result = sb.table("leads")\
                .update(updates)\
                .eq("id", lead_id)\
                .execute()
            
            if result.data:
                # Build human-readable summary
                updated_fields = []
                if first_name:
                    updated_fields.append(f"first name to {first_name}")
                if last_name:
                    updated_fields.append(f"last name to {last_name}")
                if property_address:
                    updated_fields.append("property address")
                if property_city or property_state or property_zip:
                    updated_fields.append("property location")
                if age:
                    updated_fields.append(f"age to {age}")
                if property_value:
                    updated_fields.append(f"property value to ${property_value:,.0f}")
                if estimated_equity:
                    updated_fields.append(f"equity to ${estimated_equity:,.0f}")
                if mortgage_balance is not None:
                    updated_fields.append(f"mortgage balance to ${mortgage_balance:,.0f}")
                
                summary = ", ".join(updated_fields) if updated_fields else "your information"
                
                logger.info(f"[LEAD] Updated lead {lead_id}: {updates}")
                
                # Build global_data updates to match DB updates
                # This ensures AI sees corrected/new info immediately
                global_updates = {}
                if first_name:
                    global_updates["caller_name"] = first_name
                if last_name:
                    global_updates["caller_last_name"] = last_name
                if property_address:
                    global_updates["property_address"] = property_address
                if property_city:
                    global_updates["property_city"] = property_city
                if property_state:
                    global_updates["property_state"] = property_state
                if property_zip:
                    global_updates["property_zip"] = property_zip
                if age is not None:
                    global_updates["caller_age"] = age
                if property_value is not None:
                    global_updates["property_value"] = property_value
                if estimated_equity is not None:
                    global_updates["estimated_equity"] = estimated_equity
                if mortgage_balance is not None:
                    global_updates["mortgage_balance"] = mortgage_balance
                
                return (
                    SwaigFunctionResult(
                        f"I've updated {summary}. Is there anything else?"
                    )
                    .update_global_data(global_updates)
                )
        except Exception as e:
            logger.error(f"[LEAD] Error updating lead: {e}")
    
    return SwaigFunctionResult(
        "I had trouble updating that information. Let me make a note and have someone follow up."
    )
