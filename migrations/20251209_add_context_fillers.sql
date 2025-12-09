-- Add context config rows for key contexts (fillers empty by default)
-- Per SDK Section 11444: Enter/exit fillers available for smooth transitions
-- Currently empty - add via Vue portal if needed

-- BOOK context
INSERT INTO contexts_config (vertical, context_name, isolated, enter_fillers, exit_fillers)
VALUES (
  'reverse_mortgage',
  'book',
  false,
  '[]'::jsonb,
  '[]'::jsonb
)
ON CONFLICT DO NOTHING;

-- OBJECTIONS context
INSERT INTO contexts_config (vertical, context_name, isolated, enter_fillers, exit_fillers)
VALUES (
  'reverse_mortgage',
  'objections',
  false,
  '[]'::jsonb,
  '[]'::jsonb
)
ON CONFLICT DO NOTHING;

-- ANSWER context
INSERT INTO contexts_config (vertical, context_name, isolated, enter_fillers, exit_fillers)
VALUES (
  'reverse_mortgage',
  'answer',
  false,
  '[]'::jsonb,
  '[]'::jsonb
)
ON CONFLICT DO NOTHING;

-- Note: QUOTE context already exists with isolated=true from previous migration
