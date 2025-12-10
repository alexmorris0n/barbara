-- Add pronunciations array to theme_prompts.config
-- These are TTS pronunciation rules for industry-specific terms
-- Per SDK Section 3.20.6: Pronunciation rules fix TTS mispronunciations

UPDATE theme_prompts
SET config = jsonb_set(
  COALESCE(config, '{}'::jsonb),
  '{pronunciations}',
  '[
    {"replace": "HECM", "with": "heck-em"},
    {"replace": "HUD", "with": "H U D"},
    {"replace": "FHA", "with": "F H A"},
    {"replace": "PLF", "with": "P L F"},
    {"replace": "MIP", "with": "M I P"},
    {"replace": "LOC", "with": "line of credit"},
    {"replace": "LESA", "with": "L E S A"}
  ]'::jsonb
)
WHERE vertical = 'reverse_mortgage';

-- Add comment explaining the field
COMMENT ON COLUMN theme_prompts.config IS 'JSONB object storing vertical-specific settings: models (llm/stt/tts), vad, eos_timeout_ms, record_call, telephony (auto_answer, ring_delay_ms), safety (blocked_phrases, max_tool_depth), pronunciations (array of {replace, with} objects for TTS)';





