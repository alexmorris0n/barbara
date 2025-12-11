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

# Principal Limit Factors (PLF) - HUD HECM table
# Based on age and expected interest rate of ~7%
# Source: HUD HECM PLF tables
HECM_PLF_TABLE = {
    62: 0.396, 63: 0.404, 64: 0.412, 65: 0.420, 66: 0.428,
    67: 0.436, 68: 0.445, 69: 0.454, 70: 0.463, 71: 0.472,
    72: 0.481, 73: 0.491, 74: 0.501, 75: 0.512, 76: 0.522,
    77: 0.533, 78: 0.545, 79: 0.556, 80: 0.568, 81: 0.580,
    82: 0.593, 83: 0.606, 84: 0.619, 85: 0.633, 86: 0.647,
    87: 0.661, 88: 0.675, 89: 0.689, 90: 0.703, 91: 0.717,
    92: 0.731, 93: 0.744, 94: 0.756, 95: 0.767, 96: 0.777,
    97: 0.785, 98: 0.792, 99: 0.798
}

# Jumbo Reverse Mortgage PLF table (2026 data)
# Jumbo PLFs are typically LOWER than HECM for ages 70+, but HIGHER for younger borrowers
# Rates vary by lender - these are estimates based on 2026 market data
JUMBO_PLF_TABLE = {
    62: 0.410, 63: 0.415, 64: 0.420, 65: 0.424, 66: 0.428,
    67: 0.432, 68: 0.437, 69: 0.442, 70: 0.453, 71: 0.460,
    72: 0.467, 73: 0.474, 74: 0.481, 75: 0.497, 76: 0.505,
    77: 0.513, 78: 0.521, 79: 0.529, 80: 0.544, 81: 0.555,
    82: 0.566, 83: 0.577, 84: 0.588, 85: 0.600, 86: 0.612,
    87: 0.624, 88: 0.636, 89: 0.648, 90: 0.660, 91: 0.672,
    92: 0.684, 93: 0.696, 94: 0.708, 95: 0.720, 96: 0.730,
    97: 0.738, 98: 0.745, 99: 0.750
}

# Estimated closing costs calculation
# HECM: FHA insurance (2% of lesser of home value or lending limit, capped),
#       origination fee (capped at $6,000), plus third-party fees (~$3k-$5k)
# Jumbo: Similar structure but typically higher flat amounts for high-value homes


def get_plf(age: int, is_jumbo: bool = False) -> float:
    """Get Principal Limit Factor for age
    
    Args:
        age: Borrower age (youngest if couple)
        is_jumbo: True for jumbo reverse mortgage, False for standard HECM
    
    Returns:
        PLF rate as decimal (e.g., 0.396 = 39.6%)
    """
    if age < 62:
        return 0.0
    
    table = JUMBO_PLF_TABLE if is_jumbo else HECM_PLF_TABLE
    max_age = 99
    
    if age >= max_age:
        return table[max_age]
    return table.get(age, table[max_age])


def calculate_closing_costs(property_value: int, max_claim_amount: int, is_jumbo: bool) -> int:
    """
    Calculate realistic closing costs for reverse mortgage.
    
    For HECM:
    - FHA upfront MIP: 2% of lesser of home value or HECM lending limit (capped)
    - Origination fee: Capped at $6,000
    - Third-party fees: ~$3,000-$5,000 (title, escrow, recording, appraisal, counseling)
    
    For Jumbo:
    - Similar structure but typically higher flat amounts for high-value homes
    - Typically $15k-$25k for very large loans
    
    Args:
        property_value: Full home value
        max_claim_amount: The amount used for PLF calculation (capped for HECM, full value for jumbo)
        is_jumbo: True for jumbo reverse mortgage, False for standard HECM
    
    Returns:
        Estimated closing costs in dollars
    """
    if is_jumbo:
        # Jumbo: Use flat dollar estimates based on home value bands
        # More realistic than percentage of full value
        if property_value >= 2_000_000:
            return 25_000  # High-value jumbo: $25k flat estimate
        elif property_value >= 1_500_000:
            return 20_000  # Mid-high jumbo: $20k flat estimate
        elif property_value >= 1_200_000:
            return 18_000  # Lower jumbo: $18k flat estimate
        else:
            return 15_000  # Just over HECM limit: $15k flat estimate
    else:
        # HECM: Use capped calculations
        # FHA upfront MIP: 2% of lesser of home value or HECM lending limit
        effective_base = min(property_value, HECM_LENDING_LIMIT)
        fha_mip = int(effective_base * 0.02)  # 2% upfront MIP
        
        # Origination fee: Capped at $6,000
        origination_fee = 6_000
        
        # Third-party fees: title, escrow, recording, appraisal, counseling
        # Typically $3,000-$5,000 for standard HECM
        third_party_fees = 4_000
        
        return fha_mip + origination_fee + third_party_fees


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
    
    # ===== HECM/JUMBO CALCULATION =====
    
    # Step 1: Determine if this is a jumbo case (over HECM limit)
    is_over_hecm_limit = property_value > HECM_LENDING_LIMIT
    
    # Step 2: Check equity requirement for jumbo (must have at least 50% equity)
    actual_equity = property_value - mortgage_balance
    equity_percentage = (actual_equity / property_value) if property_value > 0 else 0
    
    if is_over_hecm_limit and equity_percentage < 0.50:
        return SwaigFunctionResult(
            f"Jumbo reverse mortgages require at least 50% equity in your home. "
            f"Based on your home value of ${property_value:,} and ${mortgage_balance:,} mortgage balance, "
            f"you currently have {equity_percentage:.1%} equity. "
            f"Your specialist can review whether standard HECM options or other solutions might work better for your situation."
        )
    
    # Step 3: For jumbo, use full property value; for standard HECM, cap at limit
    # Jumbo reverse mortgages don't have the HECM lending limit cap
    if is_over_hecm_limit:
        max_claim_amount = property_value  # Jumbo: use full value
    else:
        max_claim_amount = min(property_value, HECM_LENDING_LIMIT)  # Standard: cap at limit
    
    # Step 4: Get Principal Limit Factor based on age and loan type
    # Jumbo uses different (typically lower) PLF rates than standard HECM
    plf = get_plf(age, is_jumbo=is_over_hecm_limit)
    
    # Step 5: Calculate gross principal limit
    gross_principal_limit = int(max_claim_amount * plf)
    
    # Step 6: Calculate realistic closing costs (capped for HECM, flat for jumbo)
    estimated_closing_costs = calculate_closing_costs(
        property_value, max_claim_amount, is_over_hecm_limit
    )
    
    # Step 7: Subtract existing mortgage payoff (MANDATORY - must pay off existing mortgage)
    # Step 8: Calculate net available to borrower
    net_available = gross_principal_limit - estimated_closing_costs - mortgage_balance
    
    # Can't be negative
    net_available = max(0, net_available)
    
    # Calculate tenure payment (monthly for life while living in home)
    # Using actuarial estimate based on life expectancy
    # Simplified: assume 15-year average tenure for calculation
    tenure_months = 180  # 15 years
    monthly_tenure = int(net_available / tenure_months) if net_available > 0 else 0
    
    # Build response - always show both lump sum and monthly payment
    response = f"Based on an estimated home value of ${property_value:,}"
    if mortgage_balance > 0:
        response += f" and paying off your ${mortgage_balance:,} mortgage"
    
    # Always show both lump sum and monthly payment values
    response += (
        f", you could potentially access around ${net_available:,} as a lump sum"
    )
    
    # Add monthly payment (even if $0)
    if monthly_tenure > 0:
        response += f", or roughly ${monthly_tenure:,} per month"
    else:
        response += f", with ${monthly_tenure:,} per month"
    
    # Add context about loan type (jumbo is common in California)
    if is_over_hecm_limit:
        response += (
            f". This calculation uses jumbo reverse mortgage terms, which apply to homes over ${HECM_LENDING_LIMIT:,}. "
        )
    else:
        response += (
            f". This calculation uses standard HECM terms. "
        )
    
    response += (
        f"These are preliminary estimates only - actual amounts depend on current interest rates and a full application review."
    )
    
    # If net_available is 0 or negative, add helpful context
    if net_available <= 0:
        if is_over_hecm_limit:
            response += (
                f" Your specialist can review jumbo options that may offer better terms for your situation."
            )
        else:
            response += (
                f" Your specialist can review all available options, including jumbo programs for higher-value homes."
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
