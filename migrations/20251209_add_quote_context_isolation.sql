-- Add context config for QUOTE with isolation enabled
-- Per SDK Section 6.10.1: Isolated contexts truncate conversation history
-- This gives the AI a fresh start when entering QUOTE, focusing purely on calculations

INSERT INTO contexts_config (vertical, context_name, isolated, enter_fillers, exit_fillers)
VALUES (
  'reverse_mortgage',
  'quote',
  true,  -- Isolated = fresh history for cleaner calculations
  '[]'::jsonb,
  '[]'::jsonb
)
ON CONFLICT DO NOTHING;






