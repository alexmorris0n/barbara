"""
Reverse mortgage calculation tool
Accurate HECM math using HUD Principal Limit Factors

Per Section 4.21 (Results & Actions): Return SwaigFunctionResult with actions
Per Section 3.18.8: All calls are sync

Ported from Reference/reference-swaig-agent/tools/calculate.py
"""

import logging
from typing import Optional, Tuple
from signalwire_agents.core.function_result import SwaigFunctionResult

from services.database import update_conversation_state, normalize_phone, get_lead_by_phone

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


def _coerce_int(value) -> Optional[int]:
    if value is None:
        return None
    try:
        # Strings like "500,000" or "$500000"
        if isinstance(value, str):
            cleaned = "".join(ch for ch in value if ch.isdigit() or ch == "-")
            if cleaned == "" or cleaned == "-":
                return None
            return int(cleaned)
        return int(value)
    except Exception:
        return None


def _fill_missing_from_lead(
    phone: str,
    property_value: Optional[int],
    age: Optional[int],
    mortgage_balance: Optional[int],
) -> Tuple[Optional[int], Optional[int], int]:
    """
    Best-effort fill missing inputs from the lead record.
    Returns (property_value, age, mortgage_balance) where mortgage_balance is always an int.
    """
    lead = get_lead_by_phone(phone)
    if lead:
        if property_value is None:
            property_value = _coerce_int(lead.get("property_value"))
        if age is None:
            age = _coerce_int(lead.get("age"))
        if mortgage_balance is None:
            mortgage_balance = _coerce_int(lead.get("mortgage_balance"))
    mb = _coerce_int(mortgage_balance)
    return property_value, age, max(0, mb or 0)


def handle_calculate(
    phone: str,
    property_value: Optional[int] = None,
    age: Optional[int] = None,
    mortgage_balance: Optional[int] = 0,
) -> SwaigFunctionResult:
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

    # Coerce + fill from lead if possible (so the AI can call the tool without perfect args)
    property_value = _coerce_int(property_value)
    age = _coerce_int(age)
    mortgage_balance = _coerce_int(mortgage_balance)
    property_value, age, mortgage_balance = _fill_missing_from_lead(phone, property_value, age, mortgage_balance)

    missing = []
    if not property_value:
        missing.append("home value")
    if not age:
        missing.append("age (youngest homeowner)")
    if missing:
        # Be explicit: we do not estimate without required inputs.
        missing_text = " and ".join(missing) if len(missing) <= 2 else ", ".join(missing[:-1]) + f", and {missing[-1]}"
        return SwaigFunctionResult(
            f"I can calculate an accurate estimate, but I need your {missing_text}. "
            "What is your age, and what would you estimate the home is worth today?"
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
    
    # Ensure mortgage_balance is a valid number (already normalized, but keep defensive)
    mortgage_balance = max(0, int(mortgage_balance or 0))
    
    # ===== HECM CALCULATION =====
    
    # Step 1: Apply HECM lending limit (can't borrow against value above limit)
    max_claim_amount = min(property_value, HECM_LENDING_LIMIT)
    is_over_hecm_limit = property_value > HECM_LENDING_LIMIT
    
    # Step 2: Get Principal Limit Factor based on age
    plf = get_plf(age)
    
    # Step 3: Calculate gross principal limit
    gross_principal_limit = int(max_claim_amount * plf)
    
    # Step 4: Subtract estimated closing costs (based on max_claim_amount, NOT full property value)
    # FIX: Closing costs apply to the HECM amount, not the home value
    estimated_closing_costs = int(max_claim_amount * ESTIMATED_CLOSING_COST_PERCENT)
    
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
        # Check if this is a high-value home that exceeds HECM limits
        # These leads are EXCELLENT candidates for jumbo reverse mortgages
        if is_over_hecm_limit and actual_equity > 200000:
            response = (
                f"Great news! With a home value of ${property_value:,} and ${actual_equity:,} in equity, "
                f"you're actually an excellent candidate for a jumbo reverse mortgage. "
                f"The standard government HECM program has a ${HECM_LENDING_LIMIT:,} limit, "
                f"but there are jumbo options for higher-value homes like yours that can access much more. "
                f"Your specialist will have better numbers for you based on those programs."
            )
        elif mortgage_balance > gross_principal_limit:
            # High mortgage relative to principal limit
            response = (
                f"Based on your home value of ${property_value:,}, the reverse mortgage would first need to pay off "
                f"your ${mortgage_balance:,} existing mortgage. With the current rates and lending limits, "
                f"your specialist can review whether a jumbo product or other options might work better for your situation."
            )
        else:
            response = (
                f"Based on an estimated home value of ${property_value:,} and mortgage balance of ${mortgage_balance:,}, "
                f"the standard program may be limited. Your specialist can review all available options with you, "
                f"including jumbo programs that may offer more flexibility."
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
        # Add note about jumbo options for high-value homes
        if is_over_hecm_limit:
            response += (
                f" And since your home exceeds the standard ${HECM_LENDING_LIMIT:,} limit, "
                f"there may be jumbo options that could offer even more."
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
                f"net=${net_available:,}, over_hecm_limit={is_over_hecm_limit}, equity=${actual_equity:,}")
    
    # Per Section 4.21: Use add_action for metadata
    return (
        SwaigFunctionResult(response)
        .add_action("set_meta_data", {
            "quote_presented": True,
            "estimated_amount": net_available,
            "plf_used": plf
        })
    )
