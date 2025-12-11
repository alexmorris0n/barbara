-- Migration: Revert change_context tool from prompts
-- This removes change_context from tools lists and reverts routing to "Route to X" style
-- Created: 2025-12-11

-- Remove change_context from all tools arrays
UPDATE prompt_versions pv
SET content = jsonb_set(
  content,
  '{tools}',
  COALESCE(
    (
      SELECT jsonb_agg(tool)
      FROM jsonb_array_elements_text(content->'tools') AS tool
      WHERE tool != 'change_context'
    ),
    '[]'::jsonb
  )
)
FROM prompts p
WHERE pv.prompt_id = p.id
AND pv.is_active = true
AND jsonb_array_length(COALESCE(content->'tools', '[]'::jsonb)) > 0;

-- Update routing to "Route to X" style
UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ If appointment_booked=true: Route to ANSWER or GOODBYE\n→ If quote_presented=true: Route to ANSWER\n→ If qualified=true: Route to QUOTE\n→ If verified=true: Route to QUALIFY\n→ Otherwise: Route to VERIFY"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'greet' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ After address confirmed: Route to QUALIFY"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'verify' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ If age < 62: Route to GOODBYE (disqualify)\n→ If qualified (all gates pass): Route to QUOTE\n→ If objection raised: Route to OBJECTIONS"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'qualify' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ If age < 62 discovered: Route to GOODBYE (disqualify)\n→ If caller asks a question: Route to ANSWER\n→ If caller has concerns/objections: Route to OBJECTIONS\n→ If caller says \"no questions\" or ready to book: Route to BOOK\n→ If hard NO / not interested: Route to GOODBYE"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'quote' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ If caller asks about amounts/numbers: Route to QUOTE\n→ If caller has concerns/pushback: Route to OBJECTIONS\n→ If caller is satisfied and ready: Route to BOOK\n→ If caller says not interested: Route to GOODBYE"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'answer' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ If objection resolved and caller agrees to book: Route to BOOK\n→ If caller has more questions: Route to ANSWER\n→ If caller still hesitant but open: Offer callback, then Route to GOODBYE\n→ If hard NO: Route to GOODBYE"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'objections' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ After appointment booked and confirmed: Route to GOODBYE\n→ If booking fails repeatedly: Route to GOODBYE (with manual follow-up)\n→ If caller wants to reschedule: Stay in BOOK"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'book' AND pv.is_active = true;

UPDATE prompt_versions pv
SET content = jsonb_set(content, '{routing}', '"→ If caller has last-minute questions: Route to ANSWER\n→ Otherwise: End call"')
FROM prompts p
WHERE pv.prompt_id = p.id AND p.node_name = 'goodbye' AND pv.is_active = true;

