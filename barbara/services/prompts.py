"""
Prompt building service
Builds context injection for caller information

Ported from Reference/reference-swaig-agent/services/prompts.py
"""

from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)


def build_context_injection(
    lead_context: Optional[Dict[str, Any]], 
    phone: str, 
    conversation_data: Optional[Dict[str, Any]] = None, 
    call_type: str = "inbound"
) -> str:
    """
    Build context string to inject into prompt
    Creates formatted text block with call-specific information
    """
    if not lead_context and not conversation_data:
        return ""
    
    context_parts = [
        "=== CALLER INFORMATION ===",
        f"Phone: {phone}",
    ]
    
    # Add lead information if available
    if lead_context:
        if lead_context.get('id'):
            context_parts.append(f"Lead ID: {lead_context['id']}")
        
        if lead_context.get('first_name'):
            context_parts.append(f"Name: {lead_context['first_name']}")
            if lead_context.get('last_name'):
                context_parts[-1] += f" {lead_context['last_name']}"
        
        if lead_context.get('qualified') is not None:
            context_parts.append(f"Qualified: {'Yes' if lead_context['qualified'] else 'No'}")
        
        # Property information
        if lead_context.get('property_address'):
            context_parts.append(f"Property Address: {lead_context['property_address']}")
        elif lead_context.get('property_city'):
            city = lead_context['property_city']
            if lead_context.get('property_state'):
                city += f", {lead_context['property_state']}"
            context_parts.append(f"Property Location: {city}")
        
        if lead_context.get('estimated_equity'):
            context_parts.append(f"Estimated Equity: ${lead_context['estimated_equity']:,}")
        
        if lead_context.get('property_value'):
            context_parts.append(f"Property Value: ${lead_context['property_value']:,}")
        
        if lead_context.get('age'):
            context_parts.append(f"Age: {lead_context['age']}")
        
        # Broker information
        if lead_context.get('assigned_broker_id') and lead_context.get('brokers'):
            broker = lead_context['brokers']
            broker_name = broker.get('contact_name', 'Unknown')
            if broker.get('company_name'):
                broker_name += f" ({broker['company_name']})"
            context_parts.append(f"Assigned Broker: {broker_name}")
        
        # Status
        if lead_context.get('status'):
            context_parts.append(f"Lead Status: {lead_context['status']}")
        
        # Individual verification flags (CRITICAL for routing decisions)
        if lead_context.get('phone_verified') is not None:
            context_parts.append(f"phone_verified: {str(lead_context['phone_verified']).lower()}")
        if lead_context.get('email_verified') is not None:
            context_parts.append(f"email_verified: {str(lead_context['email_verified']).lower()}")
        if lead_context.get('address_verified') is not None:
            context_parts.append(f"address_verified: {str(lead_context['address_verified']).lower()}")
        if lead_context.get('verified') is not None:
            context_parts.append(f"verified: {str(lead_context['verified']).lower()}")
        
        # Qualification flags (for routing)
        if lead_context.get('age_qualified') is not None:
            context_parts.append(f"age_qualified: {str(lead_context['age_qualified']).lower()}")
        if lead_context.get('homeowner_qualified') is not None:
            context_parts.append(f"homeowner_qualified: {str(lead_context['homeowner_qualified']).lower()}")
        if lead_context.get('primary_residence_qualified') is not None:
            context_parts.append(f"primary_residence_qualified: {str(lead_context['primary_residence_qualified']).lower()}")
        if lead_context.get('equity_qualified') is not None:
            context_parts.append(f"equity_qualified: {str(lead_context['equity_qualified']).lower()}")
    
    context_parts.append("===================")
    
    # Add conversation state flags if provided
    if conversation_data:
        context_parts.append("")
        context_parts.append("=== CONVERSATION STATUS ===")
        
        # Wrong person flags
        if conversation_data.get('wrong_person') is not None:
            context_parts.append(f"wrong_person: {str(conversation_data['wrong_person']).lower()}")
        
        if conversation_data.get('right_person_available') is not None:
            context_parts.append(f"right_person_available: {str(conversation_data['right_person_available']).lower()}")
        
        # Other relevant flags
        if conversation_data.get('verified') is not None:
            context_parts.append(f"verified: {str(conversation_data['verified']).lower()}")
        
        if conversation_data.get('greeted') is not None:
            context_parts.append(f"greeted: {str(conversation_data['greeted']).lower()}")
        
        if conversation_data.get('qualified') is not None:
            context_parts.append(f"qualified: {str(conversation_data['qualified']).lower()}")
        
        if conversation_data.get('quote_presented') is not None:
            context_parts.append(f"quote_presented: {str(conversation_data['quote_presented']).lower()}")
        
        context_parts.append("===================")
    
    return "\n".join(context_parts)


