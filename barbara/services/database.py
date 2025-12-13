"""
Database service for Supabase integration
Handles leads, conversation_state, and prompt queries

Ported from Reference/reference-swaig-agent/services/database.py
Business logic unchanged - only adapted for SDK context

NOTE: All functions are SYNC per SDK manual Section 3.18.8:
"Cache expensive lookups - Database calls in on_swml_request add latency"
"""

import os
from supabase import create_client, Client
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_KEY")

if not supabase_url or not supabase_key:
    logger.warning("SUPABASE_URL and SUPABASE_SERVICE_KEY not set - using mock mode")
    supabase: Optional[Client] = None
else:
    supabase: Client = create_client(supabase_url, supabase_key)


def normalize_phone(phone: str) -> str:
    """
    Normalize phone number to E.164 format: +1XXXXXXXXXX
    Handles: +16505300051, 16505300051, 6505300051, (650) 530-0051
    Returns consistent format to avoid duplicate records in conversation_state.
    """
    if not phone:
        return ""
    
    # Remove all non-digit characters
    digits = ''.join(c for c in phone if c.isdigit())
    
    # If 11 digits starting with 1, strip the country code
    if len(digits) == 11 and digits.startswith('1'):
        digits = digits[1:]
    
    # Return E.164 format with +1 prefix for consistency
    if len(digits) == 10:
        return f"+1{digits}"
    
    return digits


def get_lead_by_phone(phone: str) -> Optional[Dict[str, Any]]:
    """
    Get lead by phone number
    CRITICAL: Uses 'primary_phone' field (not 'phone')
    """
    if not supabase:
        return None
        
    normalized = normalize_phone(phone)
    if not normalized:
        # Guardrail: never query with an empty/invalid phone, or we can match arbitrary leads
        # (e.g., ilike '%%' would match the first row).
        logger.warning("[DB] get_lead_by_phone called with empty/invalid phone - skipping lookup")
        return None
    # Also build E.164 format for matching primary_phone_e164 field
    e164_format = f"+1{normalized}" if not normalized.startswith('+') else normalized
    
    try:
        response = supabase.table('leads')\
            .select('*, brokers!assigned_broker_id(id, contact_name, company_name, phone, email, nmls_number, nylas_grant_id, timezone, business_hours_start, business_hours_end, business_days, appointment_duration_minutes, buffer_between_appointments_minutes, minimum_booking_lead_time_minutes)')\
            .or_(f'primary_phone.ilike.%{normalized}%,primary_phone_e164.eq.{e164_format}')\
            .limit(1)\
            .execute()
        
        if response.data:
            logger.info(f"[DB] Lead found: {response.data[0].get('first_name', 'Unknown')}")
            return response.data[0]
        
        logger.info(f"[DB] No lead found for phone: {normalized}")
        return None
        
    except Exception as e:
        logger.error(f"[DB] Error fetching lead: {e}")
        return None


def get_lead_by_id(lead_id: str) -> Optional[Dict[str, Any]]:
    """
    Get lead by UUID
    Used for outbound calls where lead_id is passed in URL params
    """
    if not supabase or not lead_id:
        return None
    
    try:
        response = supabase.table('leads')\
            .select('*, brokers!assigned_broker_id(id, contact_name, company_name, phone, email, nmls_number, nylas_grant_id, timezone, business_hours_start, business_hours_end, business_days, appointment_duration_minutes, buffer_between_appointments_minutes, minimum_booking_lead_time_minutes)')\
            .eq('id', lead_id)\
            .limit(1)\
            .execute()
        
        if response.data:
            logger.info(f"[DB] Lead found by ID: {response.data[0].get('first_name', 'Unknown')} (id: {lead_id})")
            return response.data[0]
        
        logger.info(f"[DB] No lead found for ID: {lead_id}")
        return None
        
    except Exception as e:
        logger.error(f"[DB] Error fetching lead by ID: {e}")
        return None


def get_conversation_state(phone: str) -> Optional[Dict[str, Any]]:
    """Get or create conversation state"""
    if not supabase:
        return None
        
    normalized = normalize_phone(phone)
    
    try:
        response = supabase.table('conversation_state')\
            .select('*')\
            .eq('phone_number', normalized)\
            .limit(1)\
            .execute()
        
        if response.data:
            return response.data[0]
        
        # Create new state if doesn't exist
        new_state = {
            'phone_number': normalized,
            'current_node': 'greet',
            'conversation_data': {},
            'qualified': None,
            'call_count': 0
        }
        
        insert_response = supabase.table('conversation_state')\
            .insert(new_state)\
            .execute()
        
        if insert_response.data:
            logger.info(f"[DB] Created new conversation state for: {normalized}")
            return insert_response.data[0]
        
        return None
        
    except Exception as e:
        logger.error(f"[DB] Error fetching conversation state: {e}")
        return None


def update_conversation_state(phone: str, updates: Dict[str, Any]) -> bool:
    """Update conversation state"""
    if not supabase:
        return False
        
    normalized = normalize_phone(phone)
    
    try:
        # Handle conversation_data updates (merge with existing)
        if 'conversation_data' in updates:
            # Get current state first (sync call now)
            current = get_conversation_state(phone)
            if current:
                existing_data = current.get('conversation_data', {})
                if isinstance(existing_data, dict) and isinstance(updates['conversation_data'], dict):
                    updates['conversation_data'] = {**existing_data, **updates['conversation_data']}
        
        response = supabase.table('conversation_state')\
            .update(updates)\
            .eq('phone_number', normalized)\
            .execute()
        
        if response.data:
            logger.info(f"[DB] Updated conversation state for: {normalized}")
            return True
        
        return False
        
    except Exception as e:
        logger.error(f"[DB] Error updating conversation state: {e}")
        return False


def get_node_prompt(node_name: str, vertical: str = "reverse_mortgage") -> Optional[str]:
    """
    Get node prompt from database
    Returns the instructions text from prompt_versions.content JSONB
    """
    if not supabase:
        return None
        
    try:
        # First get the prompt_id
        prompt_response = supabase.table('prompts')\
            .select('id')\
            .eq('node_name', node_name)\
            .eq('vertical', vertical)\
            .eq('is_active', True)\
            .limit(1)\
            .execute()
        
        if not prompt_response.data:
            logger.warning(f"[DB] No prompt found for node: {node_name}, vertical: {vertical}")
            return None
        
        prompt_id = prompt_response.data[0]['id']
        
        # Get active version
        version_response = supabase.table('prompt_versions')\
            .select('content')\
            .eq('prompt_id', prompt_id)\
            .eq('is_active', True)\
            .order('version_number', desc=True)\
            .limit(1)\
            .execute()
        
        if version_response.data:
            content = version_response.data[0].get('content', {})
            instructions = content.get('instructions', '')
            # Append routing if present
            routing = content.get('routing', '')
            if routing:
                instructions = f"{instructions}\n\n=== ROUTING ===\n{routing}"
            logger.info(f"[DB] Loaded prompt for node: {node_name}")
            return instructions
        
        logger.warning(f"[DB] No active version found for prompt_id: {prompt_id}")
        return None
        
    except Exception as e:
        logger.error(f"[DB] Error fetching node prompt: {e}")
        return None


def get_node_config(node_name: str, vertical: str = "reverse_mortgage") -> Optional[Dict[str, Any]]:
    """
    Get full node configuration from database
    Returns dict with instructions, valid_contexts, functions, step_criteria
    """
    if not supabase:
        # Return fallback if no DB
        from services.fallbacks import get_fallback_node_config
        return get_fallback_node_config(node_name)
        
    try:
        # First get the prompt_id
        prompt_response = supabase.table('prompts')\
            .select('id')\
            .eq('node_name', node_name)\
            .eq('vertical', vertical)\
            .eq('is_active', True)\
            .limit(1)\
            .execute()
        
        if not prompt_response.data:
            logger.warning(f"[DB] No prompt found for node: {node_name}, vertical: {vertical}")
            from services.fallbacks import log_node_config_fallback, get_fallback_node_config
            log_node_config_fallback(node_name, vertical, "No prompt row found", is_exception=False)
            return get_fallback_node_config(node_name)
        
        prompt_id = prompt_response.data[0]['id']
        
        # Get active version
        version_response = supabase.table('prompt_versions')\
            .select('content')\
            .eq('prompt_id', prompt_id)\
            .eq('is_active', True)\
            .order('version_number', desc=True)\
            .limit(1)\
            .execute()
        
        if version_response.data:
            content = version_response.data[0].get('content', {})
            # Vue portal saves as 'tools', but SignalWire expects 'functions'
            # Support both for backward compatibility
            functions = content.get('functions', []) or content.get('tools', [])
            
            # Assemble instructions with routing (if present)
            # Vue edits them separately, but we combine for the agent
            instructions = content.get('instructions', '')
            routing = content.get('routing', '')
            logger.info(f"[DB] Node {node_name}: routing field = '{routing[:50]}...' (len={len(routing)})" if routing else f"[DB] Node {node_name}: routing field is EMPTY")
            if routing:
                instructions = f"{instructions}\n\n=== ROUTING ===\n{routing}"
                logger.info(f"[DB] Node {node_name}: Appended routing section")
            
            config = {
                'instructions': instructions,
                'valid_contexts': content.get('valid_contexts', []),
                'functions': functions,
                'step_criteria': content.get('step_criteria', '')
            }
            logger.info(f"[DB] Loaded full config for node: {node_name}")
            logger.info(f"[DB]   - valid_contexts: {config.get('valid_contexts', [])}")
            logger.info(f"[DB]   - functions: {config.get('functions', [])}")
            return config
        
        # Fallback for missing data
        from services.fallbacks import log_node_config_fallback, get_fallback_node_config
        log_node_config_fallback(node_name, vertical, "No active version found for prompt_id", is_exception=False)
        return get_fallback_node_config(node_name)
        
    except Exception as e:
        # Fallback for exception
        from services.fallbacks import log_node_config_fallback, get_fallback_node_config
        log_node_config_fallback(node_name, vertical, f"{type(e).__name__}: {str(e)}", is_exception=True)
        return get_fallback_node_config(node_name)


def get_context_config(context_name: str, vertical: str = "reverse_mortgage") -> Optional[Dict[str, Any]]:
    """
    Get context-level configuration from contexts_config table.
    Returns dict with: isolated, enter_fillers, exit_fillers
    
    Per SDK Section 6.10: Context configuration for isolation and fillers
    """
    if not supabase:
        return None
    
    try:
        response = supabase.table('contexts_config')\
            .select('isolated, enter_fillers, exit_fillers')\
            .eq('context_name', context_name)\
            .eq('vertical', vertical)\
            .limit(1)\
            .execute()
        
        if response.data:
            config = response.data[0]
            logger.info(f"[DB] Loaded context config for '{context_name}': isolated={config.get('isolated')}")
            return config
        
        return None
        
    except Exception as e:
        logger.error(f"[DB] Error fetching context config: {e}")
        return None


def get_theme_prompt(vertical: str = "reverse_mortgage") -> Optional[str]:
    """Get theme prompt (universal personality)"""
    if not supabase:
        from services.fallbacks import get_fallback_theme
        return get_fallback_theme()
        
    try:
        response = supabase.table('theme_prompts')\
            .select('content_structured, content')\
            .eq('vertical', vertical)\
            .eq('is_active', True)\
            .limit(1)\
            .execute()
        
        if response.data:
            row = response.data[0]
            
            # PREFER: Structured format (content_structured JSONB)
            if row.get('content_structured'):
                # Assemble theme from structured sections
                theme_data = row['content_structured']
                sections = []
                if theme_data.get('identity'):
                    sections.append(theme_data['identity'])
                if theme_data.get('personality'):
                    sections.append(f"# Personality\n\n{theme_data['personality']}")
                if theme_data.get('output_rules'):
                    sections.append(f"# Output rules\n\n{theme_data['output_rules']}")
                if theme_data.get('conversational_flow'):
                    sections.append(f"# Conversational flow\n\n{theme_data['conversational_flow']}")
                if theme_data.get('tools'):
                    sections.append(f"# Tools\n\n{theme_data['tools']}")
                if theme_data.get('guardrails'):
                    sections.append(f"# Guardrails\n\n{theme_data['guardrails']}")
                return '\n\n'.join(sections)
            
            # FALLBACK: Old format (content TEXT) for backward compatibility
            if row.get('content'):
                return row['content']
        
        # Fallback for missing data
        from services.fallbacks import log_theme_fallback, get_fallback_theme
        log_theme_fallback(vertical, "No rows returned from theme_prompts query", is_exception=False)
        return get_fallback_theme()
        
    except Exception as e:
        # Fallback for exception
        from services.fallbacks import log_theme_fallback, get_fallback_theme
        log_theme_fallback(vertical, f"{type(e).__name__}: {str(e)}", is_exception=True)
        return get_fallback_theme()


def get_pronunciations(vertical: str = "reverse_mortgage") -> list:
    """
    Get TTS pronunciation rules from theme_prompts.config
    Returns list of dicts: [{"replace": "HECM", "with": "heck-em"}, ...]
    
    Per SDK Section 3.20.6: Pronunciation rules fix TTS mispronunciations
    """
    if not supabase:
        # Fallback pronunciations for reverse mortgage industry terms
        return [
            {"replace": "HECM", "with": "heck-em"},
            {"replace": "HUD", "with": "H U D"},
            {"replace": "FHA", "with": "F H A"},
        ]
    
    try:
        response = supabase.table('theme_prompts')\
            .select('config')\
            .eq('vertical', vertical)\
            .eq('is_active', True)\
            .limit(1)\
            .execute()
        
        if response.data and response.data[0].get('config'):
            config = response.data[0]['config']
            pronunciations = config.get('pronunciations', [])
            if pronunciations:
                logger.info(f"[DB] ✅ Loaded {len(pronunciations)} pronunciation rules")
                return pronunciations
        
        logger.info(f"[DB] No pronunciation rules found for vertical: {vertical}")
        return []
        
    except Exception as e:
        logger.error(f"[DB] Error fetching pronunciations: {e}")
        return []


def get_active_signalwire_models(vertical: str = 'reverse_mortgage', language: str = 'en-US') -> Dict[str, Any]:
    """
    Get active SignalWire models and behavior params from database
    Returns: {llm_model, stt_model, tts_voice_string, end_of_speech_timeout, attention_timeout, transparent_barge}
    
    Per SignalWire docs:
    - ai_model: Just model name (e.g., "gpt-4o-mini", "gpt-4.1-mini", "gpt-4.1-nano")
    - openai_asr_engine: Colon format (e.g., "deepgram:nova-2", "deepgram:nova-3")
    - voice: Dot format (e.g., "elevenlabs.rachel", "amazon.Joanna:neural:en-US")
    - end_of_speech_timeout: milliseconds (default 700)
    - attention_timeout: milliseconds (default 5000)
    - transparent_barge: boolean (default True)
    """
    from services.fallbacks import get_fallback_models
    
    if not supabase:
        return {
            **get_fallback_models(),
            "end_of_speech_timeout": 700,
            "attention_timeout": 5000,
            "transparent_barge": True
        }
    
    try:
        # Load active LLM model
        llm_result = supabase.table('signalwire_available_llm_models')\
            .select('model_id_full')\
            .eq('is_active', True)\
            .maybe_single()\
            .execute()
        
        fallbacks = get_fallback_models()
        
        if llm_result and llm_result.data:
            llm_model = llm_result.data.get('model_id_full', fallbacks['llm_model'])
            logger.info(f"[DB] ✅ Loaded active LLM: {llm_model}")
        else:
            llm_model = fallbacks['llm_model']
            logger.warning(f"[DB] ⚠️ No active LLM model found, using fallback: {llm_model}")
        
        # Load active STT model
        stt_result = supabase.table('signalwire_available_stt_models')\
            .select('model_id_full')\
            .eq('is_active', True)\
            .maybe_single()\
            .execute()
        
        if stt_result and stt_result.data:
            stt_model = stt_result.data.get('model_id_full', fallbacks['stt_model'])
            logger.info(f"[DB] ✅ Loaded active STT: {stt_model}")
        else:
            stt_model = fallbacks['stt_model']
            logger.warning(f"[DB] ⚠️ No active STT model found, using fallback: {stt_model}")
        
        # Load active TTS voice
        tts_result = supabase.table('signalwire_available_voices')\
            .select('voice_id_full')\
            .eq('is_active', True)\
            .maybe_single()\
            .execute()
        
        if tts_result and tts_result.data:
            tts_voice_string = tts_result.data.get('voice_id_full', fallbacks['tts_voice_string'])
            logger.info(f"[DB] ✅ Loaded active TTS: {tts_voice_string}")
        else:
            tts_voice_string = fallbacks['tts_voice_string']
            logger.warning(f"[DB] ⚠️ No active TTS voice found, using fallback: {tts_voice_string}")
        
        # Load behavior params from agent_params table
        params_result = supabase.table('agent_params')\
            .select('end_of_speech_timeout, attention_timeout, transparent_barge, temperature, top_p, frequency_penalty, presence_penalty')\
            .eq('vertical', vertical)\
            .eq('language', language)\
            .eq('is_active', True)\
            .maybe_single()\
            .execute()
        
        # Set defaults
        end_of_speech_timeout = 700
        attention_timeout = 5000
        transparent_barge = True
        temperature = 0.3  # SDK default - deterministic for booking agent
        top_p = 1.0  # SDK default
        frequency_penalty = 0.4  # Reduces repetitive phrasing
        presence_penalty = 0.2  # Encourages slight variety
        
        if params_result and params_result.data:
            end_of_speech_timeout = params_result.data.get('end_of_speech_timeout', 700)
            attention_timeout = params_result.data.get('attention_timeout', 5000)
            transparent_barge = params_result.data.get('transparent_barge', True)
            temperature = float(params_result.data.get('temperature', 0.3))
            top_p = float(params_result.data.get('top_p', 1.0))
            frequency_penalty = float(params_result.data.get('frequency_penalty', 0.4))
            presence_penalty = float(params_result.data.get('presence_penalty', 0.2))
            logger.info(f"[DB] ✅ Loaded behavior params: temp={temperature}, top_p={top_p}, freq_pen={frequency_penalty}, pres_pen={presence_penalty}")
        else:
            logger.warning(f"[DB] ⚠️ No agent_params found for {vertical}/{language}, using defaults")
        
        return {
            "llm_model": llm_model,
            "stt_model": stt_model,
            "tts_voice_string": tts_voice_string,
            "end_of_speech_timeout": end_of_speech_timeout,
            "attention_timeout": attention_timeout,
            "transparent_barge": transparent_barge,
            "temperature": temperature,
            "top_p": top_p,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty
        }
        
    except Exception as e:
        logger.error(f"[DB] Failed to load active SignalWire models: {e}, using fallbacks", exc_info=True)
        return {
            **get_fallback_models(),
            "end_of_speech_timeout": 700,
            "attention_timeout": 5000,
            "transparent_barge": True
        }


def build_voice_string(engine: str, voice_name: str) -> str:
    """Build provider-specific voice string per SignalWire format"""
    formats = {
        "elevenlabs": f"elevenlabs.{voice_name}",
        "openai": f"openai.{voice_name}",
        "google": f"gcloud.{voice_name}",
        "gcloud": f"gcloud.{voice_name}",
        "amazon": f"amazon.{voice_name}",
        "polly": f"amazon.{voice_name}",
        "azure": voice_name,  # Azure uses full voice code as-is
        "microsoft": voice_name,
        "cartesia": f"cartesia.{voice_name}",
        "rime": f"rime.{voice_name}"
    }
    return formats.get(engine.lower(), f"{engine}.{voice_name}")


def insert_call_summary(
    phone: str,
    lead_id: Optional[str],
    broker_id: Optional[str],
    call_id: str,
    duration_seconds: int,
    direction: str,
    outcome: str,
    summary_data: Dict[str, Any],
    call_log: Optional[list] = None
) -> bool:
    """
    Insert call summary into interactions table.
    Called from on_summary callback after call ends.
    
    Per SDK Section 6.16.4: Post-prompt data is received after call ends.
    
    Args:
        call_log: The call transcript from SignalWire (array of message objects)
                  Saved to transcript (JSONB) and transcript_text (human-readable)
    """
    if not supabase:
        logger.warning("[DB] Cannot insert call summary - no Supabase connection")
        return False
    
    try:
        # Map outcome to interactions.outcome enum values
        outcome_map = {
            "booked": "appointment_booked",
            "not_booked": "neutral",
            "disqualified": "negative",
            "wrong_person": "no_response",
            "transferred": "positive",
            "callback_requested": "follow_up_needed",
        }
        mapped_outcome = outcome_map.get(outcome, "neutral")
        
        interaction_data = {
            "type": "ai_call",
            "direction": direction,
            "duration_seconds": duration_seconds,
            "outcome": mapped_outcome,
            "content": summary_data.get("summary", ""),
            "metadata": {
                "call_id": call_id,
                "phone": phone,  # Store phone for trigger-based lead linking
                "post_prompt_data": summary_data,
                "qualification_status": summary_data.get("qualification_status"),
                "objections": summary_data.get("objections_raised", []),
                "sentiment": summary_data.get("caller_sentiment"),
                "follow_up_needed": summary_data.get("follow_up_needed", False),
                "appointment_time": summary_data.get("appointment_time"),
            }
        }
        
        # Add lead_id if we have it
        if lead_id:
            interaction_data["lead_id"] = lead_id
        
        # Add broker_id if we have it
        if broker_id:
            interaction_data["broker_id"] = broker_id
        
        # If appointment was booked, set scheduled_for
        if summary_data.get("appointment_time"):
            interaction_data["scheduled_for"] = summary_data["appointment_time"]
        
        # Save transcript if provided
        if call_log:
            # Save full transcript as JSONB
            interaction_data["transcript"] = call_log
            
            # Generate human-readable transcript text
            transcript_lines = []
            for msg in call_log:
                role = msg.get("role", "unknown")
                content = msg.get("content", "")
                
                # Skip system messages and empty content
                if role in ("system", "system-log") or not content:
                    continue
                
                # Format role for readability
                if role == "user":
                    speaker = "Caller"
                elif role == "assistant":
                    speaker = "Barbara"
                elif role == "tool":
                    # Skip tool results in readable transcript
                    continue
                else:
                    speaker = role.capitalize()
                
                transcript_lines.append(f"{speaker}: {content.strip()}")
            
            interaction_data["transcript_text"] = "\n".join(transcript_lines)
            logger.info(f"[DB] 📝 Transcript saved: {len(transcript_lines)} lines")
        
        response = supabase.table("interactions").insert(interaction_data).execute()
        
        if response.data:
            logger.info(f"[DB] ✅ Inserted call summary for call_id: {call_id}, outcome: {mapped_outcome}")
            return True
        
        logger.warning(f"[DB] ⚠️ No data returned when inserting call summary")
        return False
        
    except Exception as e:
        logger.error(f"[DB] ❌ Error inserting call summary: {e}")
        return False


def create_appointment(
    lead_id: str,
    broker_id: str,
    appointment_time: str,
    nylas_event_id: Optional[str] = None,
    sms_consent: bool = False,
    status: str = "scheduled",
) -> Optional[Dict[str, Any]]:
    """
    Create a new appointment record (used for reminders + email confirmation idempotency).

    Returns the created row (including its UUID id) on success; otherwise None.
    """
    if not supabase:
        return None

    try:
        data: Dict[str, Any] = {
            "lead_id": lead_id,
            "broker_id": broker_id,
            "appointment_time": appointment_time,
            "status": status,
            "sms_consent": sms_consent,
            # Reminders/confirmations will be sent by Edge Function later
            "confirmation_sent": False,
            "reminder_24h_sent": False,
            "reminder_1h_sent": False,
        }

        if nylas_event_id:
            data["nylas_event_id"] = nylas_event_id

        response = supabase.table("appointments").insert(data).execute()

        if response.data and len(response.data) > 0:
            row = response.data[0]
            logger.info(
                f"[DB] ✅ Created appointment record id={row.get('id')} for lead {lead_id} "
                f"(status={status}, sms_consent={sms_consent})"
            )
            return row

        logger.warning("[DB] ⚠️ No data returned when creating appointment")
        return None

    except Exception as e:
        logger.error(f"[DB] ❌ Error creating appointment: {e}", exc_info=True)
        return None


def update_appointment(appointment_id: str, updates: Dict[str, Any]) -> bool:
    """
    Update an appointment record by ID.
    """
    if not supabase:
        return False

    if not appointment_id:
        return False

    try:
        response = supabase.table("appointments").update(updates).eq("id", appointment_id).execute()
        return bool(response.data)
    except Exception as e:
        logger.error(f"[DB] ❌ Error updating appointment {appointment_id}: {e}", exc_info=True)
        return False


def get_appointment_by_nylas_event_id(nylas_event_id: str) -> Optional[Dict[str, Any]]:
    """
    Get the oldest appointment row matching a given Nylas event id.
    (Defensive against duplicates.)
    """
    if not supabase:
        return None
    if not nylas_event_id:
        return None

    try:
        response = (
            supabase.table("appointments")
            .select("*")
            .eq("nylas_event_id", nylas_event_id)
            .order("created_at", desc=False)
            .limit(1)
            .execute()
        )
        if response.data and len(response.data) > 0:
            return response.data[0]
        return None
    except Exception as e:
        logger.error(f"[DB] ❌ Error fetching appointment for nylas_event_id={nylas_event_id}: {e}", exc_info=True)
        return None


def insert_call_debug_log(
    call_id: str,
    event_type: Optional[str],
    event_data: Dict[str, Any],
    lead_id: Optional[str] = None
) -> bool:
    """
    Insert debug webhook data into call_debug_logs table.
    Called from /debug-log endpoint when SignalWire sends debug events.
    
    Per SDK line 23689: debug_webhook_url receives debug data including
    transcripts, tool calls, and other conversation events.
    
    Args:
        call_id: The SignalWire call ID
        event_type: Type of event (e.g., 'speech', 'tool_call', 'context_switch')
        event_data: Full JSON payload from the debug webhook
        lead_id: Optional lead UUID if we can match from call data
    """
    if not supabase:
        logger.warning("[DB] Cannot insert debug log - no Supabase connection")
        return False
    
    try:
        log_data = {
            "call_id": call_id,
            "event_type": event_type,
            "event_data": event_data,
        }
        
        # Add lead_id if provided
        if lead_id:
            log_data["lead_id"] = lead_id
        
        response = supabase.table("call_debug_logs").insert(log_data).execute()
        
        if response.data:
            logger.info(f"[DB] ✅ Inserted debug log for call_id: {call_id}, type: {event_type}")
            return True
        
        logger.warning(f"[DB] ⚠️ No data returned when inserting debug log")
        return False
        
    except Exception as e:
        logger.error(f"[DB] ❌ Error inserting debug log: {e}")
        return False
