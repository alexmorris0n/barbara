"""
Barbara Agent - SignalWire AI Agents SDK Implementation
Refactored from SWAIG bridge to SDK v1.0.4

Per Manual:
- Section 3.11: AgentBase constructor pattern
- Section 3.18.3: Dynamic agents with on_swml_request
- Section 4.14: @tool decorator with name, description, parameters, handler(self, args, raw_data)
- Section 4.21: SwaigFunctionResult
- Section 6.8-6.11: Context and step configuration
"""

import os
import logging
from typing import Optional, Dict, Any

from dotenv import load_dotenv
load_dotenv()  # Load .env file

from signalwire_agents import AgentBase
from signalwire_agents.core.function_result import SwaigFunctionResult

# Import services
from services.database import (
    get_lead_by_phone,
    get_lead_by_id,
    get_conversation_state,
    update_conversation_state,
    get_theme_prompt,
    get_node_config,
    get_context_config,
    get_active_signalwire_models,
    get_pronunciations,
    normalize_phone,
    insert_call_summary,
)
# build_context_injection replaced by set_global_data per SDK Section 6.16
from services.fallbacks import get_fallback_node_config
from services.availability import fetch_broker_availability, format_slots_for_llm

# Import tool handlers
from tools.flags import (
    handle_mark_greeted,
    handle_set_caller_goal,
    handle_mark_verified,
    handle_mark_qualified,
    handle_mark_qualification_result,
    handle_mark_quote_presented,
    handle_mark_ready_to_book,
    handle_mark_wrong_person,
    handle_mark_handoff_complete,
    handle_mark_has_objection,
    handle_mark_objection_handled,
    handle_mark_sms_consent,
)
from tools.verification import (
    handle_mark_phone_verified,
    handle_mark_email_verified,
    handle_mark_address_verified,
)
from tools.qualification import (
    handle_mark_age_qualified,
    handle_mark_homeowner_qualified,
    handle_mark_primary_residence_qualified,
    handle_mark_equity_qualified,
)
from tools.calculate import handle_calculate
from tools.knowledge import handle_knowledge_search
from tools.booking import handle_booking, handle_check_broker_availability
from tools.lead import handle_verify_caller_identity, handle_update_lead_info

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# All 8 nodes in Barbara's conversation flow
ALL_NODES = ["greet", "verify", "qualify", "quote", "answer", "objections", "book", "goodbye"]


class BarbaraAgent(AgentBase):
    """
    Barbara - Reverse Mortgage Voice Assistant
    
    Per Section 3.11: AgentBase subclass with constructor calling super().__init__()
    Per Section 3.18.3: Dynamic config via on_swml_request override
    """
    
    def __init__(self):
        """
        Per Section 3.11 (Creating an Agent):
        Initialize with name and route, then configure base settings.
        
        Per Section 6.8: Contexts must be defined in __init__, NOT in on_swml_request.
        """
        # Per Section 11980: Call Recording
        # record_call=True enables automatic recording
        # record_stereo=True puts caller on left channel, agent on right (better for transcription)
        # Disclosure handled in GREET: "calling on a recorded line"
        super().__init__(
            name="barbara",
            route="/agent/barbara",
            record_call=True,
            record_stereo=True,
            record_format="wav"
        )
        
        # Base prompt section (required even with contexts per Section 6.8)
        self.prompt_add_section(
            "Role",
            "You are Barbara, a warm and professional voice assistant helping homeowners explore reverse mortgage options."
        )
        
        # Add math skill per Section 5.18.3
        # Provides: calculate - Evaluate mathematical expressions
        self.add_skill("math")
        
        # Add datetime skill per Section 5.18
        # Provides: get_current_datetime - AI can know what day/time it is for booking
        # Critical for interpreting "tomorrow", "next Tuesday", etc.
        self.add_skill("datetime")
        
        # Per Section 3.22: Speech hints improve recognition for domain-specific vocabulary
        # Critical for financial terms seniors may use
        self.add_hints([
            # Industry terms (often misheard)
            "HECM", "reverse mortgage", "FHA", "HUD", "equity",
            "home equity conversion mortgage", "lump sum", "line of credit",
            "tenure", "term", "principal limit", "mortgage insurance premium",
            
            # Company & agent names
            "Equity Connect", "Barbara",
            
            # Property terms
            "my home", "my house", "primary residence", "owner occupied",
            "property value", "home value", "mortgage balance", "payoff",
            
            # Age-related (seniors saying their age)
            "sixty two", "sixty three", "sixty four", "sixty five",
            "sixty six", "sixty seven", "sixty eight", "sixty nine",
            "seventy", "seventy one", "seventy two", "seventy three",
            "seventy four", "seventy five", "eighty", "eighty five", "ninety",
            
            # Common senior phrases
            "fixed income", "social security", "retirement", "pension",
            "supplemental income", "monthly payments", "no monthly payments",
            
            # Booking terms
            "appointment", "schedule", "consultation", "call back",
            "tomorrow", "next week", "morning", "afternoon",
            
            # Objection-related
            "scam", "too good to be true", "catch", "hidden fees",
            "lose my home", "heirs", "inheritance", "children",
            
            # Mortgage amount shorthand (helps STT with context)
            "hundred thousand", "two hundred thousand", "three hundred thousand",
            "four hundred thousand", "five hundred thousand", "half a million",
            "six hundred thousand", "seven hundred thousand", "eight hundred thousand",
            "two fifty", "three fifty", "four fifty", "five fifty",
            "K", "grand",
        ])
        
        # Build contexts at init time (per Section 6.8 - contexts in __init__)
        # Contexts are static; dynamic caller info goes in prompt sections via on_swml_request
        self._build_contexts()
        
        # Per Section 6.16.4: Post-prompt extracts structured data after call ends
        # This generates a call summary that gets sent to on_summary callback
        self.set_post_prompt("""
Analyze this call and provide a JSON summary:
{
    "outcome": "<booked|not_booked|disqualified|wrong_person|transferred|callback_requested>",
    "appointment_time": "<ISO datetime if booked, null otherwise>",
    "qualification_status": "<qualified|not_qualified|unknown>",
    "objections_raised": ["<objection1>", "<objection2>"],
    "caller_sentiment": "<positive|neutral|negative|frustrated>",
    "follow_up_needed": <true|false>,
    "summary": "<2-3 sentence summary of the call>"
}

Rules:
- outcome "booked" ONLY if appointment was successfully scheduled
- outcome "disqualified" if caller doesn't meet age/ownership/equity requirements
- outcome "wrong_person" if someone other than the lead answered
- Include ALL objections mentioned (scam concerns, fees, losing home, etc.)
- Be accurate with sentiment - frustrated seniors are common, note it
""")
        
        logger.info("[BARBARA] Agent initialized with %d contexts", len(ALL_NODES))
    
    def on_swml_request(self, request_data: dict, callback_path: str = None, request = None, *args, **kwargs) -> None:
        # NOTE: SDK passes 4 args but manual documents 2. Using *args, **kwargs as workaround.
        """
        Per Section 3.18.3 (The on_swml_request Method):
        Called before SWML is generated for each request.
        Load all config from database dynamically.
        
        Per Section 3.18.8: Database calls are sync to avoid latency issues.
        
        request_data contains:
        - call_id: Unique call identifier
        - caller_id_num: Caller's phone number
        - caller_id_name: Caller's name (if available)
        - called_id_num: Number that was called
        - direction: "inbound" or "outbound"
        """
        # Extract call data from SignalWire request
        call_data = request_data.get("call", {})
        direction = call_data.get("direction") or request_data.get("direction", "inbound")
        
        # Get query params from URL (for outbound calls with lead_id)
        query_params = {}
        if request:
            try:
                query_params = dict(request.query_params) if hasattr(request, 'query_params') else {}
            except:
                pass
        
        lead_id_from_url = query_params.get("lead_id")
        direction_from_url = query_params.get("direction", direction)
        
        # Use direction from URL if provided (more reliable for outbound)
        if direction_from_url:
            direction = direction_from_url
        
        # For OUTBOUND calls: use the TO number (lead's phone) and lead_id from URL
        # For INBOUND calls: use the FROM number (caller's phone)
        if direction == "outbound":
            # Outbound: we're calling the lead, so use "to" number
            caller_num = (
                call_data.get("to") or 
                call_data.get("to_number") or
                request_data.get("called_id_num") or
                ""
            )
            logger.info(f"[BARBARA] Outbound call to: {caller_num}, lead_id from URL: {lead_id_from_url}")
        else:
            # Inbound: caller is calling us, use "from" number
            caller_num = (
                call_data.get("from") or 
                call_data.get("from_number") or
                request_data.get("caller_id_num") or
                ""
            )
        
        phone = normalize_phone(caller_num) if caller_num else "unknown"
        
        logger.info(f"[BARBARA] Call direction: {direction}, phone: {caller_num} (normalized: {phone})")
        
        # CRITICAL: Store call_direction in conversation_state so it persists to on_summary
        # This fixes the bug where outbound calls were being logged as "inbound"
        if phone and phone != "unknown":
            update_conversation_state(phone, {
                'conversation_data': {
                    'call_direction': direction
                }
            })
            logger.info(f"[BARBARA] Stored call_direction='{direction}' in conversation_state")
        
        # PRE-ANSWER: Ringback tone for INBOUND only
        # Per SDK 1.0.4: Use add_pre_answer_verb with auto_answer=False
        # For OUTBOUND: No ringback - person already answered their phone
        if direction == "inbound":
            self.add_pre_answer_verb("play", {
                "urls": ["ring:us"],
                "auto_answer": False  # CRITICAL: prevents play from answering prematurely
            })
            logger.info("[BARBARA] Added US ringback for inbound call")
        
        # POST-ANSWER: Immediate greeting for OUTBOUND calls
        # This plays BEFORE the AI loads, filling the silence gap
        # Prevents leads from saying "Hello?" multiple times and hanging up
        # Includes required recording disclosure upfront
        # 
        # NOTE: We load the voice from DB here since we need it for the greeting
        # before the main models are loaded later in this method
        if direction == "outbound":
            # Get voice from database (needed for greeting before full config loads)
            models_for_voice = get_active_signalwire_models()
            outbound_voice = models_for_voice.get("tts_voice_string", "elevenlabs.rachel")
            self.add_post_answer_verb("play", {
                "url": "say:This is Barbara from Equity Connect calling on a recorded line. How are you?",
                "say_voice": outbound_voice
            })
            logger.info(f"[BARBARA] Added outbound greeting with voice: {outbound_voice}")
        
        # Load lead data from database
        # For OUTBOUND: try lead_id from URL first, then fall back to phone lookup
        # For INBOUND: use phone lookup
        lead = None
        if lead_id_from_url:
            lead = get_lead_by_id(lead_id_from_url)
            if lead:
                logger.info(f"[BARBARA] Found lead by ID: {lead.get('first_name')} (from URL param)")
        
        if not lead:
            lead = get_lead_by_phone(phone)
            if lead:
                logger.info(f"[BARBARA] Found lead by phone: {lead.get('first_name')}")
        
        state = get_conversation_state(phone)
        theme_prompt = get_theme_prompt("reverse_mortgage")
        models = get_active_signalwire_models()
        
        # Sync lead status to conversation_state on call start
        if lead:
            lead_qualified = lead.get('qualified', False)
            lead_verified = lead.get('verified', False)
            update_conversation_state(phone, {
                'qualified': lead_qualified,
                'conversation_data': {
                    'verified': lead_verified
                }
            })
            state = get_conversation_state(phone)
            logger.info(f"[BARBARA] Synced lead status: qualified={lead_qualified}, verified={lead_verified}")
        
        # FIX: Reset stale flags for OUTBOUND calls
        # wrong_person and greeted should not persist from previous calls
        if direction == "outbound":
            update_conversation_state(phone, {
                'conversation_data': {
                    'wrong_person': False,
                    'greeted': False,
                    'right_person_available': False
                }
            })
            state = get_conversation_state(phone)
            logger.info(f"[BARBARA] Reset stale flags for outbound call")
        
        # Per SDK Section 6.16.2: Set global_data for dynamic prompt variables
        # This replaces text-block injection with structured data the AI can reference
        conversation_data = state.get('conversation_data', {}) if state else {}
        
        # Extract broker info
        broker = lead.get('brokers', {}) if lead else {}
        broker_name = broker.get('contact_name', 'your broker') if broker else 'your broker'
        broker_company = broker.get('company_name', '') if broker else ''
        broker_phone = broker.get('primary_phone_e164', '') if broker else ''  # E.164 for transfers
        
        # Fetch broker availability (sync call to Nylas or generate from business hours)
        # This pre-loads slots so LLM can offer them immediately in BOOK node
        available_slots = []
        available_slots_display = "No slots available"
        if broker:
            available_slots = fetch_broker_availability(broker, days_ahead=5, max_slots=10)
            available_slots_display = format_slots_for_llm(available_slots, max_display=5)
            logger.info(f"[BARBARA] Fetched {len(available_slots)} available slots for broker {broker_name}")
        
        self.set_global_data({
            # Caller identity
            "caller_phone": phone,
            "caller_name": lead.get('first_name', 'there') if lead else 'there',
            "caller_last_name": lead.get('last_name', '') if lead else '',
            "caller_age": lead.get('age', 0) if lead else 0,
            
            # Persona info (from email campaign)
            # Extract first name safely - handle NULL, whitespace-only, and missing values
            "persona_name": ((lead.get('persona_sender_name') or '').split()[0] 
                           if lead and (lead.get('persona_sender_name') or '').strip() 
                           else ''),
            
            # Property info
            "property_address": lead.get('property_address', '') if lead else '',
            "property_city": lead.get('property_city', '') if lead else '',
            "property_state": lead.get('property_state', '') if lead else '',
            "property_zip": lead.get('property_zip', '') if lead else '',
            "property_value": lead.get('property_value', 0) if lead else 0,
            "estimated_equity": lead.get('estimated_equity', 0) if lead else 0,
            "mortgage_balance": lead.get('current_balance', 0) if lead else 0,  # DB column: current_balance
            
            # Verification status (from leads table)
            "phone_verified": lead.get('phone_verified', False) if lead else False,
            "email_verified": lead.get('email_verified', False) if lead else False,
            "address_verified": lead.get('address_verified', False) if lead else False,
            "verified": lead.get('verified', False) if lead else False,
            
            # Qualification status (from leads table)
            "age_qualified": lead.get('age_qualified', False) if lead else False,
            "homeowner_qualified": lead.get('homeowner_qualified', False) if lead else False,
            "primary_residence_qualified": lead.get('primary_residence_qualified', False) if lead else False,
            "equity_qualified": lead.get('equity_qualified', False) if lead else False,
            "qualified": lead.get('qualified', False) if lead else False,
            
            # Conversation state (from conversation_state table)
            "caller_goal": conversation_data.get('caller_goal', ''),  # Why they want a reverse mortgage
            "greeted": conversation_data.get('greeted', False),
            "quote_presented": conversation_data.get('quote_presented', False),
            "ready_to_book": conversation_data.get('ready_to_book', False),
            "appointment_booked": conversation_data.get('appointment_booked', False),
            "wrong_person": conversation_data.get('wrong_person', False),
            "right_person_available": conversation_data.get('right_person_available', False),
            "has_objection": conversation_data.get('has_objection', False),
            "objection_type": conversation_data.get('objection_type', ''),
            
            # Broker info
            "broker_name": broker_name,
            "broker_company": broker_company,
            "broker_phone": broker_phone,  # E.164 format for .connect() transfers
            
            # Availability (pre-fetched for instant booking)
            "available_slots": available_slots,  # Full slot data for booking
            "available_slots_display": available_slots_display,  # Formatted for LLM to read aloud
            "next_available_slot": available_slots[0]['display'] if available_slots else "No slots available",
            
            # Call info
            "call_direction": direction,
            "lead_id": lead.get('id', '') if lead else '',
            "lead_status": lead.get('status', 'new') if lead else 'new',
        })
        
        # Set theme prompt
        if theme_prompt:
            self.prompt_add_section("Theme", theme_prompt)
        
        # Add caller context using global_data variables
        # Per SDK Section 6.16.2.4: Use ${global_data.key} in prompts
        self.prompt_add_section(
            "Caller Context",
            """You are speaking with ${global_data.caller_name} (phone: ${global_data.caller_phone}).

=== CAMPAIGN INFO ===
Persona (who sent email): ${global_data.persona_name}
Caller's Goal: ${global_data.caller_goal}

=== PROPERTY INFO ===
Address: ${global_data.property_address}
City: ${global_data.property_city}, ${global_data.property_state} ${global_data.property_zip}
Estimated Value: ${global_data.property_value}
Mortgage Balance: ${global_data.mortgage_balance}
Estimated Equity: ${global_data.estimated_equity}
Age: ${global_data.caller_age}

=== VERIFICATION STATUS ===
Phone Verified: ${global_data.phone_verified}
Email Verified: ${global_data.email_verified}
Address Verified: ${global_data.address_verified}
Fully Verified: ${global_data.verified}

=== QUALIFICATION STATUS ===
Age 62+ Qualified: ${global_data.age_qualified}
Homeowner Qualified: ${global_data.homeowner_qualified}
Primary Residence Qualified: ${global_data.primary_residence_qualified}
Equity Qualified: ${global_data.equity_qualified}
Fully Qualified: ${global_data.qualified}

=== CONVERSATION STATUS ===
Greeted: ${global_data.greeted}
Quote Presented: ${global_data.quote_presented}
Ready to Book: ${global_data.ready_to_book}
Appointment Booked: ${global_data.appointment_booked}
Wrong Person: ${global_data.wrong_person}
Has Objection: ${global_data.has_objection}

=== ASSIGNED BROKER ===
Name: ${global_data.broker_name}
Company: ${global_data.broker_company}

=== AVAILABLE APPOINTMENT SLOTS ===
Next Available: ${global_data.next_available_slot}
All Available Slots:
${global_data.available_slots_display}

When booking, offer the next available slot first. If they need a different time, offer alternatives from the list above.
"""
        )
        
        # Configure AI models from database
        # Per Section 3.21 (AI Parameters)
        # All LLM params (temperature, top_p, frequency_penalty, presence_penalty) loaded from agent_params table
        self.set_params({
            "ai_model": models.get("llm_model", "gpt-4.1-mini"),
            "openai_asr_engine": models.get("stt_model", "deepgram:nova-3"),
            "end_of_speech_timeout": models.get("end_of_speech_timeout", 700),
            "attention_timeout": models.get("attention_timeout", 5000),
            "temperature": models.get("temperature", 0.3),  # Low for reliable routing
            "top_p": models.get("top_p", 1.0),  # Nucleus sampling diversity
            "frequency_penalty": models.get("frequency_penalty", 0.4),  # Reduces repetitive phrasing
            "presence_penalty": models.get("presence_penalty", 0.2),   # Encourages slight variety
            "enable_barge": "complete,partial",
            "transparent_barge": models.get("transparent_barge", True),
            "wait_for_user": direction == "outbound",  # Wait for senior to answer on outbound calls
            "save_conversation": True,
            "conversation_id": phone,
            "conscience": "Remember to stay in character as Barbara, a warm and friendly reverse mortgage specialist. Always use the calculate_reverse_mortgage function for any financial calculations - never estimate or guess numbers.",
            "local_tz": "America/Los_Angeles",
            # Debug webhook sends full transcripts to Supabase Edge Function
            # Anon key in URL allows JWT verification to pass
            "debug_webhook_url": "https://mxnqfwuhvurajrgoefyg.supabase.co/functions/v1/debug-webhook?apikey=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im14bnFmd3VodnVyYWpyZ29lZnlnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk4NzU3OTAsImV4cCI6MjA3NTQ1MTc5MH0.QMoZAjIKkB05Vr9nM1FKbC2ke5RTvfv6zrSDU0QMuN4",
            "debug_webhook_level": 2,  # Level 2 = full verbosity (transcripts, tool calls, etc.)
        })
        
        # Configure voice
        # Per Section 3.20 (Voice & Language)
        voice_string = models.get("tts_voice_string", "elevenlabs.rachel")
        
        # Per Section 3.20.3: function_fillers are spoken while tools execute
        # REMOVED global fillers - they play on EVERY tool call including fast flag-setters
        # Fillers are now only on slow tools: calculate, search_knowledge, book_appointment
        self.add_language(
            name="English",
            code="en-US",
            voice=voice_string,
            function_fillers=[]  # No global fillers - per-tool only
        )
        
        # Per Section 3.20.6: Pronunciation rules fix TTS mispronunciations
        # Load from theme_prompts.config.pronunciations (editable in Vue portal)
        pronunciations = get_pronunciations("reverse_mortgage")
        if pronunciations:
            self.set_pronunciations(pronunciations)
            logger.info(f"[BARBARA] Applied {len(pronunciations)} pronunciation rules")
        
        # NOTE: Contexts are built in __init__ (per Section 6.8), NOT here.
        # on_swml_request is for dynamic prompts and params only.
        
        logger.info(f"[BARBARA] Dynamic config loaded for {phone}")
        logger.info(f"[BARBARA]   LLM: {models.get('llm_model')}")
        logger.info(f"[BARBARA]   STT: {models.get('stt_model')}")
        logger.info(f"[BARBARA]   TTS: {voice_string}")
    
    def on_summary(self, summary: Optional[Dict[str, Any]], raw_data: Optional[Dict[str, Any]] = None) -> None:
        """
        Per Section 10.17.1: Handle post-prompt summaries.
        Called after call ends with structured data from set_post_prompt.
        
        Writes call summary to Supabase interactions table.
        
        NOTE: This callback may be triggered multiple times during a call (e.g., on context switches).
        We only save to DB when we have actual post_prompt_data with an outcome.
        """
        if not summary and not raw_data:
            logger.warning("[BARBARA] on_summary called with no data")
            return
        
        try:
            # Extract data from the callback
            post_prompt_data = {}
            if summary:
                post_prompt_data = summary
            elif raw_data:
                post_prompt_data = raw_data.get("post_prompt_data", {})
                # Handle parsed JSON if available
                if isinstance(post_prompt_data, dict) and "parsed" in post_prompt_data:
                    post_prompt_data = post_prompt_data["parsed"]
            
            # CRITICAL: Only save to DB if we have actual post_prompt_data with content
            # The callback can be triggered multiple times with empty data during context switches
            if not post_prompt_data or not post_prompt_data.get("outcome"):
                logger.info(f"[BARBARA] on_summary called without outcome - skipping DB insert (context switch?)")
                return
            
            # Get call metadata
            call_id = raw_data.get("call_id", "") if raw_data else ""
            duration = raw_data.get("call_duration", 0) if raw_data else 0
            
            # Extract phone number - location depends on call direction
            # For OUTBOUND: device.params.to_number (the lead we called)
            # For INBOUND: caller_id_num or device.params.from_number
            caller_num = ""
            if raw_data:
                # Check nested device.params first (actual SignalWire structure)
                device_params = raw_data.get("params", {}).get("device", {}).get("params", {})
                direction = raw_data.get("params", {}).get("direction", "")
                
                if direction == "outbound":
                    # Outbound: lead's phone is in to_number
                    caller_num = device_params.get("to_number", "")
                else:
                    # Inbound: lead's phone is in from_number or caller_id_num
                    caller_num = (
                        device_params.get("from_number") or
                        raw_data.get("caller_id_num") or
                        ""
                    )
                
                # Fallback to top-level keys if nested didn't work
                if not caller_num:
                    caller_num = (
                        raw_data.get("caller_id_num") or 
                        raw_data.get("from") or
                        raw_data.get("to") or
                        raw_data.get("conversation_id") or
                        ""
                    )
            
            phone = normalize_phone(caller_num)
            
            # Log what we found for debugging
            if not phone:
                logger.warning(f"[BARBARA] ⚠️ Could not find phone. Keys: {list(raw_data.keys()) if raw_data else []}")
                if raw_data and raw_data.get("params"):
                    logger.warning(f"[BARBARA] ⚠️ params keys: {list(raw_data.get('params', {}).keys())}")
            
            logger.info(f"[BARBARA] 📝 Post-prompt received for {phone}")
            logger.info(f"[BARBARA]   Call ID: {call_id}")
            logger.info(f"[BARBARA]   Duration: {duration}s")
            logger.info(f"[BARBARA]   Outcome: {post_prompt_data.get('outcome', 'unknown')}")
            
            # Look up lead and broker IDs
            lead = get_lead_by_phone(phone) if phone else None
            lead_id = lead.get("id") if lead else None
            broker_id = lead.get("assigned_broker_id") if lead else None
            
            # Get call direction from conversation_state
            state = get_conversation_state(phone) if phone else None
            # Default to inbound if not found
            direction = "inbound"
            if state and state.get("conversation_data"):
                # Check if we stored direction
                direction = state.get("conversation_data", {}).get("call_direction", "inbound")
            
            # Extract transcript from raw_data (call_log is cleaned, raw_call_log is full)
            call_log = raw_data.get("call_log", []) if raw_data else []
            
            # Insert into interactions table
            success = insert_call_summary(
                phone=phone,
                lead_id=lead_id,
                broker_id=broker_id,
                call_id=call_id,
                duration_seconds=duration,
                direction=direction,
                outcome=post_prompt_data.get("outcome", "unknown"),
                summary_data=post_prompt_data,
                call_log=call_log
            )
            
            if success:
                logger.info(f"[BARBARA] ✅ Call summary saved to interactions table")
            else:
                logger.warning(f"[BARBARA] ⚠️ Failed to save call summary")
                
        except Exception as e:
            logger.error(f"[BARBARA] ❌ Error in on_summary: {e}", exc_info=True)
    
    def _build_contexts(self) -> None:
        """
        Build 8 contexts from database using SDK Context system.
        
        Per Section 6.8 (Basic Context Example):
        - define_contexts() returns ContextBuilder
        - add_context("name") returns ContextStepBuilder
        - add_step("step_name") returns Step with chainable methods
        """
        contexts = self.define_contexts()
        
        for node_name in ALL_NODES:
            # Load config from database (sync)
            config = get_node_config(node_name, "reverse_mortgage")
            
            if not config:
                config = get_fallback_node_config(node_name)
            
            instructions = config.get('instructions', f'Continue the conversation in the {node_name} stage.')
            valid_contexts = config.get('valid_contexts', [])
            functions = config.get('functions', [])
            step_criteria = config.get('step_criteria', '')
            
            # Create context
            # Per Section 6.10 (Context Configuration)
            context = contexts.add_context(node_name)
            
            # Load context-level config from DB (isolation, fillers)
            # Per Section 6.10.1: Isolated contexts truncate conversation history
            context_config = get_context_config(node_name, "reverse_mortgage")
            if context_config:
                if context_config.get('isolated'):
                    context.set_isolated(True)
                    logger.info(f"[BARBARA] Context '{node_name}' set to isolated (fresh history)")
                
                # Per Section 11444: Enter/exit fillers for smooth transitions
                enter_fillers = context_config.get('enter_fillers', [])
                exit_fillers = context_config.get('exit_fillers', [])
                
                if enter_fillers:
                    context.add_enter_filler("en-US", enter_fillers)
                    logger.info(f"[BARBARA] Context '{node_name}' has {len(enter_fillers)} enter fillers")
                
                if exit_fillers:
                    context.add_exit_filler("en-US", exit_fillers)
                    logger.info(f"[BARBARA] Context '{node_name}' has {len(exit_fillers)} exit fillers")
            
            # Add single step per context (Barbara's nodes are single-step)
            # Per Section 6.9 (Step Configuration)
            step = context.add_step("main")
            step.set_text(instructions)
            
            if step_criteria:
                step.set_step_criteria(step_criteria)
            
            if valid_contexts:
                step.set_valid_contexts(valid_contexts)
            
            if functions:
                step.set_functions(functions)
            
            logger.info(f"[BARBARA] Built context '{node_name}' with {len(valid_contexts)} valid transitions, {len(functions)} functions")
        
        # NOTE: First context added ("greet") is the default per Section 6.8 examples.
        # define_contexts() does NOT have set_default_context() method.
        
        logger.info(f"[BARBARA] Built {len(ALL_NODES)} contexts (first/default: greet)")
    
    # =========================================================================
    # TOOLS - Per Section 4.14 (The @tool Decorator)
    # Pattern: @AgentBase.tool(name, description, parameters) + def handler(self, args, raw_data)
    # =========================================================================
    
    # ----- FLAG TOOLS -----
    
    @AgentBase.tool(
        name="mark_greeted",
        description="Mark that greeting has been completed",
        parameters={
            "type": "object",
            "properties": {
                "greeted": {
                    "type": "boolean",
                    "description": "Whether greeting is complete (default true)"
                },
                "reason_summary": {
                    "type": "string",
                    "description": "Optional summary of greeting outcome"
                }
            }
        }
    )
    def mark_greeted(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        greeted = args.get("greeted", True)
        reason_summary = args.get("reason_summary")
        return handle_mark_greeted(phone, greeted, reason_summary)
    
    @AgentBase.tool(
        name="set_caller_goal",
        description="Save the caller's goal or reason for wanting a reverse mortgage. Call this after they share what they want to accomplish.",
        parameters={
            "type": "object",
            "properties": {
                "goal": {
                    "type": "string",
                    "description": "The caller's goal (e.g., 'pay off mortgage', 'supplement income', 'home repairs', 'help family', 'travel')"
                },
                "goal_details": {
                    "type": "string",
                    "description": "Optional additional details about their goal"
                }
            },
            "required": ["goal"]
        }
    )
    def set_caller_goal(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        goal = args.get("goal", "")
        goal_details = args.get("goal_details", "")
        return handle_set_caller_goal(phone, goal, goal_details)
    
    @AgentBase.tool(
        name="mark_verified",
        description="Mark that caller identity has been verified",
        parameters={
            "type": "object",
            "properties": {
                "verified": {
                    "type": "boolean",
                    "description": "Whether caller is verified (default true)"
                }
            }
        }
    )
    def mark_verified(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        verified = args.get("verified", True)
        return handle_mark_verified(phone, verified)
    
    @AgentBase.tool(
        name="mark_qualified",
        description="Mark caller qualification status (age 62+, owner-occupied, equity)",
        parameters={
            "type": "object",
            "properties": {
                "qualified": {
                    "type": "boolean",
                    "description": "Whether caller qualifies for reverse mortgage"
                }
            },
            "required": ["qualified"]
        }
    )
    def mark_qualified(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        qualified = args.get("qualified")
        return handle_mark_qualified(phone, qualified)
    
    @AgentBase.tool(
        name="mark_qualification_result",
        description="Mark caller qualification status with optional reason. Same as mark_qualified.",
        parameters={
            "type": "object",
            "properties": {
                "qualified": {
                    "type": "boolean",
                    "description": "Whether caller qualifies"
                },
                "reason": {
                    "type": "string",
                    "description": "Reason for qualification/disqualification"
                }
            },
            "required": ["qualified"]
        }
    )
    def mark_qualification_result(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        qualified = args.get("qualified")
        reason = args.get("reason")
        return handle_mark_qualification_result(phone, qualified, reason)
    
    @AgentBase.tool(
        name="mark_quote_presented",
        description="Mark that financial quote has been presented to the caller",
        parameters={
            "type": "object",
            "properties": {}
        }
    )
    def mark_quote_presented(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        return handle_mark_quote_presented(phone)
    
    @AgentBase.tool(
        name="mark_ready_to_book",
        description="Mark that caller is ready to schedule appointment",
        parameters={
            "type": "object",
            "properties": {
                "ready_to_book": {
                    "type": "boolean",
                    "description": "Whether caller is ready to book (default true)"
                }
            }
        }
    )
    def mark_ready_to_book(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        ready_to_book = args.get("ready_to_book", True)
        return handle_mark_ready_to_book(phone, ready_to_book)
    
    @AgentBase.tool(
        name="mark_wrong_person",
        description="Mark that wrong person answered the call",
        parameters={
            "type": "object",
            "properties": {
                "wrong_person": {
                    "type": "boolean",
                    "description": "Whether wrong person answered (default true)"
                },
                "right_person_available": {
                    "type": "boolean",
                    "description": "Whether the right person is available to come to the phone"
                }
            }
        }
    )
    def mark_wrong_person(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        wrong_person = args.get("wrong_person", True)
        right_person_available = args.get("right_person_available")
        return handle_mark_wrong_person(phone, wrong_person, right_person_available)
    
    @AgentBase.tool(
        name="mark_handoff_complete",
        description="Complete handoff when correct person gets on the phone. Resets conversation state.",
        parameters={
            "type": "object",
            "properties": {
                "new_person_name": {
                    "type": "string",
                    "description": "Name of the correct person now on the phone"
                }
            },
            "required": ["new_person_name"]
        }
    )
    def mark_handoff_complete(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        new_person_name = args.get("new_person_name")
        return handle_mark_handoff_complete(phone, new_person_name)
    
    @AgentBase.tool(
        name="mark_has_objection",
        description="Mark that caller has raised an objection or concern",
        parameters={
            "type": "object",
            "properties": {
                "has_objection": {
                    "type": "boolean",
                    "description": "Whether caller has an objection (default true)"
                },
                "objection_type": {
                    "type": "string",
                    "description": "Type of objection (e.g., 'scam_concern', 'losing_home', 'hidden_fees')"
                }
            }
        }
    )
    def mark_has_objection(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        has_objection = args.get("has_objection", True)
        objection_type = args.get("objection_type")
        return handle_mark_has_objection(phone, has_objection, objection_type)
    
    @AgentBase.tool(
        name="mark_objection_handled",
        description="Mark that caller's objection has been resolved",
        parameters={
            "type": "object",
            "properties": {
                "objection_handled": {
                    "type": "boolean",
                    "description": "Whether objection is resolved (default true)"
                }
            }
        }
    )
    def mark_objection_handled(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        objection_handled = args.get("objection_handled", True)
        return handle_mark_objection_handled(phone, objection_handled)
    
    @AgentBase.tool(
        name="mark_sms_consent",
        description="Record whether caller consented to receive SMS text reminders for their appointment. MUST ask before booking.",
        parameters={
            "type": "object",
            "properties": {
                "sms_consent": {
                    "type": "boolean",
                    "description": "Whether caller agreed to receive text reminders"
                }
            },
            "required": ["sms_consent"]
        }
    )
    def mark_sms_consent(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        sms_consent = args.get("sms_consent")
        return handle_mark_sms_consent(phone, sms_consent)
    
    # ----- VERIFICATION TOOLS -----
    
    @AgentBase.tool(
        name="mark_phone_verified",
        description="Mark that caller's phone number has been verified",
        parameters={
            "type": "object",
            "properties": {}
        }
    )
    def mark_phone_verified(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        return handle_mark_phone_verified(phone)
    
    @AgentBase.tool(
        name="mark_email_verified",
        description="Mark that caller's email address has been verified",
        parameters={
            "type": "object",
            "properties": {}
        }
    )
    def mark_email_verified(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        return handle_mark_email_verified(phone)
    
    @AgentBase.tool(
        name="mark_address_verified",
        description="Mark property address verified. For OUTBOUND calls, this auto-verifies phone and email too. Pass call_direction='outbound' to enable. Pass new_address if collecting a missing/corrected address.",
        parameters={
            "type": "object",
            "properties": {
                "call_direction": {
                    "type": "string",
                    "description": "Pass 'outbound' to auto-verify phone+email too, or 'inbound' for address only",
                    "enum": ["outbound", "inbound"]
                },
                "new_address": {
                    "type": "string",
                    "description": "New/corrected property address if collecting missing info"
                }
            }
        }
    )
    def mark_address_verified(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        call_direction = args.get("call_direction")
        new_address = args.get("new_address")
        return handle_mark_address_verified(phone, call_direction, new_address)
    
    # ----- QUALIFICATION TOOLS -----
    
    @AgentBase.tool(
        name="mark_age_qualified",
        description="Mark that the caller is 62+ years old (FHA requirement)",
        parameters={
            "type": "object",
            "properties": {}
        }
    )
    def mark_age_qualified(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        return handle_mark_age_qualified(phone)
    
    @AgentBase.tool(
        name="mark_homeowner_qualified",
        description="Mark that the caller owns the property",
        parameters={
            "type": "object",
            "properties": {}
        }
    )
    def mark_homeowner_qualified(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        return handle_mark_homeowner_qualified(phone)
    
    @AgentBase.tool(
        name="mark_primary_residence_qualified",
        description="Mark that the property is caller's primary residence (not rental)",
        parameters={
            "type": "object",
            "properties": {}
        }
    )
    def mark_primary_residence_qualified(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        return handle_mark_primary_residence_qualified(phone)
    
    @AgentBase.tool(
        name="mark_equity_qualified",
        description="Mark that the caller has sufficient equity",
        parameters={
            "type": "object",
            "properties": {}
        }
    )
    def mark_equity_qualified(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        return handle_mark_equity_qualified(phone)
    
    # ----- CALCULATION TOOL -----
    
    @AgentBase.tool(
        name="calculate_reverse_mortgage",
        description="ALWAYS call this when presenting a quote or answering 'how much can I get?' questions. Calculate available reverse mortgage funds using accurate HECM formulas with PLF tables - NEVER estimate or guess amounts.",
        parameters={
            "type": "object",
            "properties": {
                "property_value": {
                    "type": "integer",
                    "description": "Current home value in dollars"
                },
                "age": {
                    "type": "integer",
                    "description": "Age of the youngest borrower (must be 62+)"
                },
                "mortgage_balance": {
                    "type": "integer",
                    "description": "Current mortgage balance to pay off (0 if home is paid off)"
                }
            },
            "required": ["property_value", "age"]
        },
        fillers={
            "en-US": [
                "Let me run those numbers for you...",
                "Calculating what you might qualify for...",
                "One moment while I crunch the numbers..."
            ]
        }
    )
    def calculate_reverse_mortgage(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        property_value = args.get("property_value")
        age = args.get("age")
        mortgage_balance = args.get("mortgage_balance", 0)
        return handle_calculate(phone, property_value, age, mortgage_balance)
    
    # ----- KNOWLEDGE TOOL -----
    
    @AgentBase.tool(
        name="search_knowledge",
        description="Search knowledge base for reverse mortgage questions",
        parameters={
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The question or topic to search for"
                }
            },
            "required": ["query"]
        },
        fillers={
            "en-US": [
                "Let me look that up for you...",
                "Good question, let me find that information...",
                "One moment while I check on that..."
            ]
        }
    )
    def search_knowledge(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        query = args.get("query")
        return handle_knowledge_search(phone, query)
    
    # ----- BOOKING TOOLS -----
    
    @AgentBase.tool(
        name="book_appointment",
        description="Schedule consultation with assigned broker",
        parameters={
            "type": "object",
            "properties": {
                "preferred_time": {
                    "type": "string",
                    "description": "Preferred appointment time (e.g., 'tomorrow at 2pm', '2025-01-15 14:00')"
                },
                "notes": {
                    "type": "string",
                    "description": "Optional notes for the appointment"
                }
            },
            "required": ["preferred_time"]
        },
        fillers={
            "en-US": [
                "Let me schedule that for you...",
                "Booking your appointment now...",
                "One moment while I get that set up..."
            ]
        }
    )
    def book_appointment(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        preferred_time = args.get("preferred_time")
        notes = args.get("notes")
        return handle_booking(phone, preferred_time, notes)
    
    @AgentBase.tool(
        name="check_broker_availability",
        description="Check assigned broker's calendar availability. Call this BEFORE suggesting specific times.",
        parameters={
            "type": "object",
            "properties": {
                "preferred_date": {
                    "type": "string",
                    "description": "Preferred date to check (e.g., 'tomorrow', '2025-01-15')"
                },
                "preferred_time": {
                    "type": "string",
                    "description": "Preferred time of day (e.g., 'morning', 'afternoon', '2pm')"
                }
            }
        },
        fillers={
            "en-US": [
                "Let me check the calendar...",
                "Looking at available times...",
                "One moment while I check availability..."
            ]
        }
    )
    def check_broker_availability(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        preferred_date = args.get("preferred_date")
        preferred_time = args.get("preferred_time")
        return handle_check_broker_availability(phone, preferred_date, preferred_time)
    
    # ----- LEAD TOOLS -----
    
    @AgentBase.tool(
        name="verify_caller_identity",
        description="Verify caller identity by name and phone. Creates lead if new.",
        parameters={
            "type": "object",
            "properties": {
                "first_name": {
                    "type": "string",
                    "description": "Caller's first name"
                }
            },
            "required": ["first_name"]
        },
        fillers={
            "en-US": [
                "Let me verify that...",
                "One moment while I look you up...",
                "Let me pull up your information..."
            ]
        }
    )
    def verify_caller_identity(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        first_name = args.get("first_name")
        return handle_verify_caller_identity(phone, first_name)
    
    @AgentBase.tool(
        name="update_lead_info",
        description="Update lead information (name, address, property details, etc.)",
        parameters={
            "type": "object",
            "properties": {
                "first_name": {
                    "type": "string",
                    "description": "Caller's first name"
                },
                "last_name": {
                    "type": "string",
                    "description": "Caller's last name"
                },
                "property_address": {
                    "type": "string",
                    "description": "Property street address"
                },
                "property_city": {
                    "type": "string",
                    "description": "Property city"
                },
                "property_state": {
                    "type": "string",
                    "description": "Property state (2-letter code)"
                },
                "property_zip": {
                    "type": "string",
                    "description": "Property ZIP code"
                },
                "age": {
                    "type": "integer",
                    "description": "Caller's age"
                },
                "property_value": {
                    "type": "number",
                    "description": "Estimated property value"
                },
                "estimated_equity": {
                    "type": "number",
                    "description": "Estimated equity (property value minus mortgage)"
                },
                "mortgage_balance": {
                    "type": "number",
                    "description": "Current mortgage balance (0 if paid off)"
                }
            }
        }
    )
    def update_lead_info(self, args, raw_data):
        phone = raw_data.get("caller_id_num", "")
        return handle_update_lead_info(
            phone,
            first_name=args.get("first_name"),
            last_name=args.get("last_name"),
            property_address=args.get("property_address"),
            property_city=args.get("property_city"),
            property_state=args.get("property_state"),
            property_zip=args.get("property_zip"),
            age=args.get("age"),
            property_value=args.get("property_value"),
            estimated_equity=args.get("estimated_equity"),
            mortgage_balance=args.get("mortgage_balance")
        )
    
    # ----- TRANSFER TOOL -----
    
    @AgentBase.tool(
        name="transfer_to_broker",
        description="Transfer caller to their assigned broker. Use when: 1) Booking system fails, 2) Caller explicitly requests to speak with a person, 3) Complex questions beyond your expertise, 4) Caller is frustrated and needs human touch.",
        parameters={
            "type": "object",
            "properties": {
                "reason": {
                    "type": "string",
                    "description": "Why the transfer is needed (e.g., 'booking_failed', 'customer_request', 'complex_question', 'frustrated_caller')"
                }
            }
        },
        fillers={
            "en-US": [
                "Let me connect you with your broker now...",
                "I'll transfer you to someone who can help...",
                "Connecting you now, one moment please..."
            ]
        }
    )
    def transfer_to_broker(self, args, raw_data):
        """
        Per SDK Section 6.18: Transfer calls using .connect()
        Uses final=True for permanent handoff to broker
        """
        phone = raw_data.get("caller_id_num", "")
        reason = args.get("reason", "customer_request")
        
        # Get broker info from global_data (set in on_swml_request)
        # Note: We can't access self.get_global_data() in tool handlers,
        # so we look up the lead again
        lead = get_lead_by_phone(phone)
        broker = lead.get('brokers', {}) if lead else {}
        broker_name = broker.get('contact_name', 'your broker') if broker else 'your broker'
        broker_phone = broker.get('primary_phone_e164', '') if broker else ''
        
        # Log the transfer
        logger.info(f"[TRANSFER] Transferring {phone} to broker {broker_name} ({broker_phone}), reason: {reason}")
        
        # Update conversation state to track the transfer
        update_conversation_state(phone, {
            'conversation_data': {
                'transferred_to_broker': True,
                'transfer_reason': reason
            }
        })
        
        if not broker_phone:
            # No broker phone - can't transfer, offer callback instead
            logger.warning(f"[TRANSFER] No broker phone for {phone}, cannot transfer")
            return SwaigFunctionResult(
                f"I'm sorry, I'm having trouble connecting you right now. "
                f"But don't worry - {broker_name} will call you back shortly. "
                f"Is there anything else I can help you with in the meantime?"
            )
        
        # Perform the transfer
        return (
            SwaigFunctionResult(
                f"I'm connecting you with {broker_name} now. "
                f"They're a licensed reverse mortgage specialist who will take great care of you. "
                f"It was wonderful speaking with you!"
            )
            .connect(broker_phone, final=True)
        )


# Entry point
if __name__ == "__main__":
    agent = BarbaraAgent()
    agent.run()
