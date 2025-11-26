"""
Knowledge base search tool - Fast keyword search (no embeddings)

Per Section 4.21 (Results & Actions): Return SwaigFunctionResult
Per Section 3.18.8: All calls are sync to avoid event loop issues

Ported from Reference/reference-swaig-agent/tools/knowledge.py
"""

import re
import logging
from typing import Optional
from signalwire_agents.core.function_result import SwaigFunctionResult

from services.database import normalize_phone

logger = logging.getLogger(__name__)

# Try to import supabase, handle gracefully if not available
try:
    import os
    from supabase import create_client
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_KEY")
    if supabase_url and supabase_key:
        sb = create_client(supabase_url, supabase_key)
    else:
        sb = None
except Exception:
    sb = None


# Fallback responses for common questions when KB search fails/times out
FALLBACK_RESPONSES = {
    "fees": (
        "Fees vary by lender, but typically include origination fees and closing costs. "
        "Your assigned broker will provide exact figures based on your property and loan amount."
    ),
    "how much": (
        "The amount depends on your age, property value, and existing mortgage balance. "
        "Your broker will calculate the exact amount based on your specific situation."
    ),
    "death": (
        "When the borrower passes away, the home can be sold or the heirs can pay off the loan. "
        "Your broker can explain all the options for estate planning with reverse mortgages."
    ),
    "die": (
        "When the borrower passes away, the home can be sold or the heirs can pay off the loan. "
        "Your broker can explain all the options for estate planning with reverse mortgages."
    ),
    "spouse": (
        "If both spouses are on the loan, the reverse mortgage continues even if one passes away. "
        "This is an important topic - your broker can walk you through how it works for your situation."
    ),
    "mortgage": (
        "Reverse mortgages are available even if you have an existing mortgage. "
        "The reverse mortgage proceeds would first pay off your existing mortgage, then provide you with access to the remaining equity."
    ),
    "equity": (
        "The amount you can access depends on your age, property value, and existing mortgage balance. "
        "Your broker will calculate the exact amount available to you."
    ),
    "cost": (
        "There are some upfront costs like origination fees and closing costs. "
        "Your broker can provide exact figures and explain what's included."
    ),
}


def get_fallback_response(query: str) -> str:
    """Get fallback response based on query keywords"""
    query_lower = query.lower()
    
    for keyword, response in FALLBACK_RESPONSES.items():
        if keyword in query_lower:
            return response
    
    return (
        "That's a great question about reverse mortgages. "
        "I'll make sure we cover all those specifics during your appointment with the broker - "
        "they can walk you through exactly how that works for your situation."
    )


def _perform_keyword_search(query: str) -> list:
    """Perform the actual keyword search in Supabase (sync)"""
    if not sb:
        return []
    
    # Extract meaningful keywords (skip common words)
    tokens = [tok.lower() for tok in re.split(r"[^A-Za-z0-9]+", query or "") if tok]
    
    # Remove stop words
    stop_words = {"a", "an", "the", "is", "are", "was", "were", "be", "been", "being", 
                  "have", "has", "had", "do", "does", "did", "will", "would", "should", 
                  "could", "may", "might", "can", "about", "if", "in", "on", "at", "to",
                  "for", "of", "with", "by", "from", "up", "out", "as", "but", "or", "and",
                  "i", "you", "he", "she", "it", "we", "they", "my", "your", "his", "her"}
    
    keywords = [tok for tok in tokens if tok not in stop_words and len(tok) > 2]
    
    # Use the most specific keyword (prefer longer, domain-specific terms)
    priority_terms = ["spouse", "mortgage", "equity", "hecm", "borrower", "lien", 
                      "property", "house", "home", "die", "dies", "death", "airbnb", 
                      "rent", "rental", "income", "foreclosure", "payoff", "grandson",
                      "granddaughter", "family", "relative", "live", "living"]
    
    pattern = None
    for term in priority_terms:
        if term in keywords:
            pattern = term
            break
    
    # If no priority term, use longest keyword
    if not pattern and keywords:
        pattern = max(keywords, key=len)
    
    # Fallback to first token or default
    if not pattern:
        pattern = tokens[0] if tokens else "reverse mortgage"
    
    logger.info(f"[KNOWLEDGE] KB search using keyword: '{pattern}' (from query: '{query[:50]}...')")
    
    # Direct SQL keyword search - MUCH faster than embeddings (sync)
    response = sb.table("vector_embeddings")\
        .select("content, metadata")\
        .eq("content_type", "reverse_mortgage_kb")\
        .ilike("content", f"%{pattern}%")\
        .limit(3)\
        .execute()
    
    return response.data or []


def handle_knowledge_search(phone: str, query: str) -> SwaigFunctionResult:
    """
    Search knowledge base for reverse mortgage questions using fast keyword search (sync).
    """
    if not query:
        return SwaigFunctionResult(
            "What would you like to know about reverse mortgages?"
        )
    
    logger.info(f"[KNOWLEDGE] Search query: {query}")
    
    try:
        # Perform sync search
        results = _perform_keyword_search(query)
        
        if results:
            # Format results
            formatted_knowledge = "\n\n---\n\n".join([
                item.get('content', '') for item in results if item.get('content')
            ])
            
            response_text = (
                f"Based on your question, here's what I can tell you: {formatted_knowledge[:500]}. "
                "Would you like more specific information about any aspect?"
            )
            
            logger.info(f"[KNOWLEDGE] ✅ Search completed successfully ({len(results)} results)")
            
            return SwaigFunctionResult(response_text)
        else:
            # No results found - use fallback
            logger.info('[KNOWLEDGE] ⚠️  No matching knowledge base content found, using fallback')
            fallback = get_fallback_response(query)
            
            return SwaigFunctionResult(
                f"{fallback} Would you like me to have a licensed advisor provide more detailed information?"
            )
    
    except Exception as e:
        logger.error(f"[KNOWLEDGE] ❌ Search error: {e}")
        
        # Return fallback response
        fallback = get_fallback_response(query)
        
        return SwaigFunctionResult(
            f"{fallback} "
            "I'm having trouble accessing the information right now. "
            "Would you like me to have someone call you with more details?"
        )
