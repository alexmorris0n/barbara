-- Rollback: Remove pronunciations from theme_prompts.config

UPDATE theme_prompts
SET config = config - 'pronunciations'
WHERE vertical = 'reverse_mortgage';

-- Revert comment
COMMENT ON COLUMN theme_prompts.config IS 'JSONB object storing vertical-specific settings: models (llm/stt/tts), vad, eos_timeout_ms, record_call, telephony (auto_answer, ring_delay_ms), safety (blocked_phrases, max_tool_depth)';



