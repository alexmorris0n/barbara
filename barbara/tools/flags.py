"""
Conversation flag tools - Mark conversation state transitions
Per Section 4.21 (Results & Actions): Return SwaigFunctionResult
Per Section 6.16.2.3: Use .update_global_data() for real-time AI state awareness
Per Section 3.18.8: All calls are sync

Ported from Reference/reference-swaig-agent/tools/flags.py
Enhanced with global_data updates for real-time prompt variable changes
"""

import logging
from signalwire_agents.core.function_result import SwaigFunctionResult

from services.database import (
    get_conversation_state,
    update_conversation_state,
    normalize_phone
)

logger = logging.getLogger(__name__)


def handle_mark_greeted(phone: str, greeted: bool = True, reason_summary: str = None) -> SwaigFunctionResult:
    """Mark greeting completed"""
    phone = normalize_phone(phone)
    
    updates = {"greeted": greeted}
    if reason_summary:
        updates["reason_summary"] = reason_summary
    
    success = update_conversation_state(phone, {
        "conversation_data": updates
    })
    
    if success:
        logger.info(f"[FLAGS] mark_greeted for {phone}")
        # Per Section 6.16.2.3: Update global_data so AI sees change immediately
        return (
            SwaigFunctionResult("Greeting completed")
            .update_global_data({"greeted": greeted})
        )
    
    return SwaigFunctionResult("Error updating greeting status")


def handle_mark_verified(phone: str, verified: bool = True) -> SwaigFunctionResult:
    """Mark caller verified"""
    phone = normalize_phone(phone)
    
    success = update_conversation_state(phone, {
        "conversation_data": {"verified": verified}
    })
    
    if success:
        logger.info(f"[FLAGS] mark_verified for {phone}")
        return (
            SwaigFunctionResult("Caller verified")
            .update_global_data({"verified": verified})
        )
    
    return SwaigFunctionResult("Error updating verification status")


def handle_mark_qualified(phone: str, qualified: bool) -> SwaigFunctionResult:
    """Mark qualification status"""
    phone = normalize_phone(phone)
    
    # Update both top-level and conversation_data
    success = update_conversation_state(phone, {
        "qualified": qualified,
        "conversation_data": {"qualified": qualified}
    })
    
    if success:
        logger.info(f"[FLAGS] mark_qualified={qualified} for {phone}")
        return (
            SwaigFunctionResult("Qualification status updated")
            .update_global_data({"qualified": qualified})
        )
    
    return SwaigFunctionResult("Error updating qualification status")


def handle_mark_qualification_result(phone: str, qualified: bool, reason: str = None) -> SwaigFunctionResult:
    """Mark qualification result with optional reason"""
    phone = normalize_phone(phone)
    
    updates = {"qualified": qualified}
    if reason and not qualified:
        updates["disqualified_reason"] = reason
    
    success = update_conversation_state(phone, {
        "qualified": qualified,
        "conversation_data": updates
    })
    
    if success:
        logger.info(f"[FLAGS] mark_qualification_result={qualified} (reason={reason}) for {phone}")
        return (
            SwaigFunctionResult("Qualification status updated")
            .update_global_data({"qualified": qualified})
        )
    
    return SwaigFunctionResult("Error updating qualification status")


def handle_mark_quote_presented(phone: str) -> SwaigFunctionResult:
    """Mark quote presented"""
    phone = normalize_phone(phone)
    
    success = update_conversation_state(phone, {
        "conversation_data": {"quote_presented": True}
    })
    
    if success:
        logger.info(f"[FLAGS] mark_quote_presented for {phone}")
        # Per Section 6.16.2.3: Update global_data so AI sees this immediately
        return (
            SwaigFunctionResult("Quote presented")
            .update_global_data({"quote_presented": True})
        )
    
    return SwaigFunctionResult("Error updating quote status")


def handle_mark_ready_to_book(phone: str, ready_to_book: bool = True) -> SwaigFunctionResult:
    """Mark ready to book"""
    phone = normalize_phone(phone)
    
    success = update_conversation_state(phone, {
        "conversation_data": {"ready_to_book": ready_to_book}
    })
    
    if success:
        logger.info(f"[FLAGS] mark_ready_to_book={ready_to_book} for {phone}")
        return (
            SwaigFunctionResult("Ready to book status updated")
            .update_global_data({"ready_to_book": ready_to_book})
        )
    
    return SwaigFunctionResult("Error updating booking status")


def handle_mark_wrong_person(phone: str, wrong_person: bool = True, right_person_available: bool = None) -> SwaigFunctionResult:
    """Mark wrong person answered"""
    phone = normalize_phone(phone)
    
    updates = {"wrong_person": wrong_person}
    if right_person_available is not None:
        updates["right_person_available"] = right_person_available
    
    success = update_conversation_state(phone, {
        "conversation_data": updates
    })
    
    if success:
        logger.info(f"[FLAGS] mark_wrong_person={wrong_person} for {phone}")
        global_updates = {"wrong_person": wrong_person}
        if right_person_available is not None:
            global_updates["right_person_available"] = right_person_available
        return (
            SwaigFunctionResult("Wrong person status noted")
            .update_global_data(global_updates)
        )
    
    return SwaigFunctionResult("Error updating wrong person status")


def handle_mark_handoff_complete(phone: str, new_person_name: str) -> SwaigFunctionResult:
    """Complete handoff to correct person - reset conversation state"""
    phone = normalize_phone(phone)
    
    logger.info(f"[HANDOFF] Completing handoff to correct person: {new_person_name} for {phone}")
    
    # Reset conversation state for fresh start with correct person
    success = update_conversation_state(phone, {
        "conversation_data": {
            "wrong_person": False,
            "right_person_available": True,
            "greeted": False,  # Reset to greet the correct person
            "handoff_complete": True,
            "correct_person_name": new_person_name
        },
        "current_node": "greet"
    })
    
    if success:
        logger.info(f"[HANDOFF] Successfully reset state for {phone}, routing to GREET")
        # Reset global_data for fresh conversation with correct person
        return (
            SwaigFunctionResult(f"Great! Now speaking with {new_person_name}. Starting fresh.")
            .update_global_data({
                "wrong_person": False,
                "right_person_available": True,
                "greeted": False,
                "caller_name": new_person_name
            })
        )
    
    return SwaigFunctionResult("Error completing handoff")


def handle_mark_has_objection(phone: str, has_objection: bool = True, objection_type: str = None) -> SwaigFunctionResult:
    """Mark objection raised"""
    phone = normalize_phone(phone)
    
    # Get current state to store node before objection
    state = get_conversation_state(phone)
    current_node = state.get("current_node", "answer") if state else "answer"
    
    updates = {"has_objection": has_objection}
    if objection_type:
        updates["objection_type"] = objection_type
    updates["node_before_objection"] = current_node
    
    success = update_conversation_state(phone, {
        "conversation_data": updates
    })
    
    if success:
        logger.info(f"[FLAGS] mark_has_objection type={objection_type} for {phone}")
        global_updates = {"has_objection": has_objection}
        if objection_type:
            global_updates["objection_type"] = objection_type
        return (
            SwaigFunctionResult("Objection noted")
            .update_global_data(global_updates)
        )
    
    return SwaigFunctionResult("Error noting objection")


def handle_mark_objection_handled(phone: str, objection_handled: bool = True) -> SwaigFunctionResult:
    """Mark objection handled"""
    phone = normalize_phone(phone)
    
    success = update_conversation_state(phone, {
        "conversation_data": {
            "objection_handled": objection_handled,
            "has_objection": False  # Clear the objection flag
        }
    })
    
    if success:
        logger.info(f"[FLAGS] mark_objection_handled for {phone}")
        return (
            SwaigFunctionResult("Objection handled")
            .update_global_data({
                "has_objection": False,
                "objection_type": ""
            })
        )
    
    return SwaigFunctionResult("Error updating objection status")
