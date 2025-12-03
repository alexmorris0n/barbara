"""
Reverse mortgage calculation tool
Accurate HECM math using HUD Principal Limit Factors

Per Section 4.21 (Results & Actions): Return SwaigFunctionResult with actions
Per Section 3.18.8: All calls are sync

Ported from Reference/reference-swaig-agent/tools/calculate.py
"""

import logging
from signalwire_agents.core.function_result import SwaigFunctionResult

from services.database import update_conversation_state, normalize_phone

logger = logging.getLogger(__name__)

# 2024 HECM Lending Limit (FHA max claim amount)
HECM_LENDING_LIMIT = 1149825

# Current expected interest rate assumption (updates periodically)
# This affects PLF - lower rates = higher PLF
EXPECTED_INTEREST_RATE = 7.0  # Approximate current rate

# Principal Limit Factors (PLF) - HUD table approximation
# Based on age and expected interest rate of ~7%
# Source: HUD HECM PLF tables
PLF_TABLE = {
    62: 0.396, 63: 0.404, 64: 0.412, 65: 0.420, 66: 0.428,
    67: 0.436, 68: 0.445, 69: 0.454, 70: 0.463, 71: 0.472,
    72: 0.481, 73: 0.491, 74: 0.501, 75: 0.512, 76: 0.522,
    77: 0.533, 78: 0.545, 79: 0.556, 80: 0.568, 81: 0.580,
    82: 0.593, 83: 0.606, 84: 0.619, 85: 0.633, 86: 0.647,
    87: 0.661, 88: 0.675, 89: 0.689, 90: 0.703, 91: 0.717,
    92: 0.731, 93: 0.744, 94: 0.756, 95: 0.767, 96: 0.777,
    97: 0.785, 98: 0.792, 99: 0.798
}

# Estimated closing costs as percentage (origination, MIP, title, etc.)
ESTIMATED_CLOSING_COST_PERCENT = 0.05  # ~5% of home value


def get_plf(age: int) -> float:
    """Get Principal Limit Factor for age"""
    if age < 62:
        return 0.0
    if age >= 99:
        return PLF_TABLE[99]
    return PLF_TABLE.get(age, PLF_TABLE[99])


def handle_calculate(phone: str, property_value: int, age: int, mortgage_balance: int = 0) -> SwaigFunctionResult:
    """
    Calculate available reverse mortgage funds using HECM formula.
    
    Args:
        phone: Caller phone number
        property_value: Current home value
        age: Borrower age (youngest if couple)
        mortgage_balance: Current mortgage payoff amount (default 0 if paid off)
    
    Returns:
        SwaigFunctionResult with calculated amounts
    """
    phone = normalize_phone(phone)
    
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
    
    # Ensure mortgage_balance is a valid number
    if mortgage_balance is None:
        mortgage_balance = 0
    mortgage_balance = max(0, int(mortgage_balance))
    
    # ===== HECM CALCULATION =====
    
    # Step 1: Apply HECM lending limit (can't borrow against value above limit)
    max_claim_amount = min(property_value, HECM_LENDING_LIMIT)
    
    # Step 2: Get Principal Limit Factor based on age
    plf = get_plf(age)
    
    # Step 3: Calculate gross principal limit
    gross_principal_limit = int(max_claim_amount * plf)
    
    # Step 4: Subtract estimated closing costs
    estimated_closing_costs = int(property_value * ESTIMATED_CLOSING_COST_PERCENT)
    
    # Step 5: Subtract existing mortgage payoff (MANDATORY - must pay off existing mortgage)
    # Step 6: Calculate net available to borrower
    net_available = gross_principal_limit - estimated_closing_costs - mortgage_balance
    
    # Can't be negative
    net_available = max(0, net_available)
    
    # Calculate actual equity for reference
    actual_equity = property_value - mortgage_balance
    
    # Calculate tenure payment (monthly for life while living in home)
    # Using actuarial estimate based on life expectancy
    # Simplified: assume 15-year average tenure for calculation
    tenure_months = 180  # 15 years
    monthly_tenure = int(net_available / tenure_months) if net_available > 0 else 0
    
    # Build response with safe/disclaimer language
    if net_available <= 0:
        response = (
            f"Based on an estimated home value of ${property_value:,} and mortgage balance of ${mortgage_balance:,}, "
            f"there may not be enough equity available after closing costs. "
            f"Your specialist can review all the options with you."
        )
    else:
        response = f"Based on an estimated home value of ${property_value:,}"
        if mortgage_balance > 0:
            response += f" and paying off your ${mortgage_balance:,} mortgage"
        response += (
            f", you could potentially access around ${net_available:,} as a lump sum, "
            f"or roughly ${monthly_tenure:,} per month. "
            f"These are preliminary estimates only - actual amounts depend on current interest rates and a full application review."
        )
    
    # Update conversation state (sync)
    update_conversation_state(phone, {
        "conversation_data": {
            "quote_presented": True,
            "estimated_lump_sum": net_available,
            "estimated_monthly": monthly_tenure,
            "quote_property_value": property_value,
            "quote_mortgage_balance": mortgage_balance,
            "quote_gross_principal": gross_principal_limit,
            "quote_closing_costs": estimated_closing_costs
        }
    })
    
    logger.info(f"[CALCULATE] HECM calc for {phone}: value=${property_value:,}, age={age}, "
                f"mortgage=${mortgage_balance:,}, PLF={plf:.3f}, gross=${gross_principal_limit:,}, "
                f"net=${net_available:,}")
    
    # Per Section 4.21: Use add_action for metadata
    return (
        SwaigFunctionResult(response)
        .add_action("set_meta_data", {
            "quote_presented": True,
            "estimated_amount": net_available,
            "plf_used": plf
        })
    )
