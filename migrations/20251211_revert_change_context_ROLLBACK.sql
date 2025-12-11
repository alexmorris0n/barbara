-- ROLLBACK: Restore change_context tool to prompts
-- This adds change_context back to tools lists and updates routing to use "call change_context()" style
-- Run this to restore the context switching functionality

-- Add change_context to greet tools
UPDATE prompt_versions pv
SET content = jsonb_set(
  content,
  '{tools}',
  (content->'tools') || '["change_context"]'::jsonb
)
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'greet' AND pv.is_active = true;

-- Add change_context to verify tools  
UPDATE prompt_versions pv
SET content = jsonb_set(
  content,
  '{tools}',
  (content->'tools') || '["change_context"]'::jsonb
)
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'verify' AND pv.is_active = true;

-- Add change_context to qualify tools
UPDATE prompt_versions pv
SET content = jsonb_set(
  content,
  '{tools}',
  (content->'tools') || '["change_context"]'::jsonb
)
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'qualify' AND pv.is_active = true;

-- Add change_context to quote tools
UPDATE prompt_versions pv
SET content = jsonb_set(
  content,
  '{tools}',
  (content->'tools') || '["change_context"]'::jsonb
)
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'quote' AND pv.is_active = true;

-- Add change_context to answer tools
UPDATE prompt_versions pv
SET content = jsonb_set(
  content,
  '{tools}',
  (content->'tools') || '["change_context"]'::jsonb
)
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'answer' AND pv.is_active = true;

-- Add change_context to objections tools
UPDATE prompt_versions pv
SET content = jsonb_set(
  content,
  '{tools}',
  (content->'tools') || '["change_context"]'::jsonb
)
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'objections' AND pv.is_active = true;

-- Add change_context to book tools
UPDATE prompt_versions pv
SET content = jsonb_set(
  content,
  '{tools}',
  (content->'tools') || '["change_context"]'::jsonb
)
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'book' AND pv.is_active = true;

-- Add change_context to goodbye tools
UPDATE prompt_versions pv
SET content = jsonb_set(
  content,
  '{tools}',
  (content->'tools') || '["change_context"]'::jsonb
)
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'goodbye' AND pv.is_active = true;

-- Update routing to "call change_context()" style
UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ If appointment_booked=true: call change_context(\"answer\") or change_context(\"goodbye\")\n→ If quote_presented=true: call change_context(\"answer\")\n→ If qualified=true: call change_context(\"quote\")\n→ If verified=true: call change_context(\"qualify\")\n→ Otherwise: call change_context(\"verify\")"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'greet' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ After address confirmed: call change_context(\"qualify\")"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'verify' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ If age < 62: call change_context(\"goodbye\") (disqualify)\n→ If qualified (all gates pass): call change_context(\"quote\")\n→ If objection raised: call change_context(\"objections\")"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'qualify' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ If age < 62 discovered: call change_context(\"goodbye\") (disqualify)\n→ If caller asks a question: call change_context(\"answer\")\n→ If caller has concerns/objections: call change_context(\"objections\")\n→ If caller says \"no questions\" or ready to book: call change_context(\"book\")\n→ If hard NO / not interested: call change_context(\"goodbye\")"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'quote' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ If caller asks about amounts/numbers: call change_context(\"quote\")\n→ If caller has concerns/pushback: call change_context(\"objections\")\n→ If caller is satisfied and ready: call change_context(\"book\")\n→ If caller says not interested: call change_context(\"goodbye\")"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'answer' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ If objection resolved and caller agrees to book: call change_context(\"book\")\n→ If caller has more questions: call change_context(\"answer\")\n→ If caller still hesitant but open: Offer callback, then call change_context(\"goodbye\")\n→ If hard NO: call change_context(\"goodbye\")"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'objections' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ After appointment booked and confirmed: call change_context(\"goodbye\")\n→ If booking fails repeatedly: call change_context(\"goodbye\") (with manual follow-up)\n→ If caller wants to reschedule: Stay in BOOK"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'book' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ If caller has last-minute questions: call change_context(\"answer\")\n→ Otherwise: End call"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'goodbye' AND pv.is_active = true;

