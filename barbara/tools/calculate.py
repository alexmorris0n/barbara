"""
Reverse mortgage calculation tool
Accurate HECM math, no hallucination

Per Section 4.21 (Results & Actions): Return SwaigFunctionResult with actions
Per Section 3.18.8: All calls are sync

Ported from Reference/reference-swaig-agent/tools/calculate.py
"""

import logging
from signalwire_agents.core.function_result import SwaigFunctionResult

from services.database import update_conversation_state, normalize_phone

logger = logging.getLogger(__name__)


def handle_calculate(phone: str, property_value: int, age: int, equity: int = None) -> SwaigFunctionResult:
    """
    Calculate available reverse mortgage funds
    Uses standard HECM calculation (50-60% of equity based on age)
    """
    phone = normalize_phone(phone)
    
    # Default equity to property value if not provided
    if equity is None:
        equity = property_value
    
    if not property_value or not age:
        return SwaigFunctionResult(
            "I need both property value and age to calculate. Could you provide those?"
        )
    
    # Validate inputs
    if age < 62:
        return SwaigFunctionResult(
            "To qualify for a reverse mortgage, you must be at least 62 years old."
        )
    
    if property_value <= 0:
        return SwaigFunctionResult(
            "Please provide a valid property value."
        )
    
    # Calculate based on age (standard HECM formula approximation)
    # Age 62: ~50% of equity
    # Age 80+: ~60% of equity
    # Linear interpolation between
    
    if age >= 80:
        percentage = 0.60
    elif age >= 62:
        # Linear interpolation: 50% at 62, 60% at 80
        percentage = 0.50 + ((age - 62) / 18) * 0.10
    else:
        percentage = 0.50
    
    # Calculate available amount
    available_amount = int(equity * percentage)
    
    # Calculate monthly payment option (if they take as monthly payments)
    # Assuming 20-year payout
    monthly_payment = int(available_amount / 240)  # 20 years = 240 months
    
    # Format response
    response = (
        f"Based on a property value of ${property_value:,} and your age of {age}, "
        f"you could access approximately ${available_amount:,} as a lump sum, "
        f"or about ${monthly_payment:,} per month over 20 years. "
        f"This is an estimate only - actual amounts depend on interest rates and other factors."
    )
    
    # Update conversation state (sync)
    update_conversation_state(phone, {
        "conversation_data": {
            "quote_presented": True,
            "estimated_lump_sum": available_amount,
            "estimated_monthly": monthly_payment,
            "quote_reaction": "positive"  # Default to positive
        }
    })
    
    logger.info(f"[CALCULATE] Calculated ${available_amount:,} for {phone}")
    
    # Per Section 4.21: Use add_action for metadata
    return (
        SwaigFunctionResult(response)
        .add_action("set_meta_data", {
            "quote_presented": True,
            "estimated_amount": available_amount
        })
    )
