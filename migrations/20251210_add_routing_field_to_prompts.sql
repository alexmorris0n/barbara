-- Migration: Add routing field to prompt_versions content JSONB
-- Date: 2025-12-10
-- Purpose: Separate routing logic from instructions for cleaner editing
-- NOTE: No schema change needed - routing is added to existing content JSONB
-- This migration documents the field addition and populates existing nodes

-- GREET routing
UPDATE prompt_versions
SET content = content || jsonb_build_object('routing', 
'→ If appointment_booked=true: Route to ANSWER or GOODBYE
→ If quote_presented=true: Route to ANSWER
→ If qualified=true: Route to QUOTE
→ If verified=true: Route to QUALIFY
→ Otherwise: Route to VERIFY')
WHERE prompt_id = (SELECT id FROM prompts WHERE node_name = 'greet' AND vertical = 'reverse_mortgage')
AND is_active = true
AND NOT (content ? 'routing');

-- VERIFY routing
UPDATE prompt_versions
SET content = content || jsonb_build_object('routing',
'→ After address confirmed: Route to QUALIFY')
WHERE prompt_id = (SELECT id FROM prompts WHERE node_name = 'verify' AND vertical = 'reverse_mortgage')
AND is_active = true
AND NOT (content ? 'routing');

-- QUALIFY routing
UPDATE prompt_versions
SET content = content || jsonb_build_object('routing',
'→ If age < 62: Route to GOODBYE (disqualify)
→ If qualified (all gates pass): Route to QUOTE
→ If objection raised: Route to OBJECTIONS')
WHERE prompt_id = (SELECT id FROM prompts WHERE node_name = 'qualify' AND vertical = 'reverse_mortgage')
AND is_active = true
AND NOT (content ? 'routing');

-- QUOTE routing
UPDATE prompt_versions
SET content = content || jsonb_build_object('routing',
'→ If age < 62 discovered: Route to GOODBYE (disqualify)
→ If caller asks a question: Route to ANSWER
→ If caller has concerns/objections: Route to OBJECTIONS
→ If caller says "no questions" or ready to book: Route to BOOK
→ If hard NO / not interested: Route to GOODBYE')
WHERE prompt_id = (SELECT id FROM prompts WHERE node_name = 'quote' AND vertical = 'reverse_mortgage')
AND is_active = true
AND NOT (content ? 'routing');

-- ANSWER routing
UPDATE prompt_versions
SET content = content || jsonb_build_object('routing',
'→ If caller asks about amounts/numbers: Route to QUOTE
→ If caller has concerns/pushback: Route to OBJECTIONS
→ If caller is satisfied and ready: Route to BOOK
→ If caller says not interested: Route to GOODBYE')
WHERE prompt_id = (SELECT id FROM prompts WHERE node_name = 'answer' AND vertical = 'reverse_mortgage')
AND is_active = true
AND NOT (content ? 'routing');

-- OBJECTIONS routing
UPDATE prompt_versions
SET content = content || jsonb_build_object('routing',
'→ If objection resolved and caller agrees to book: Route to BOOK
→ If caller has more questions: Route to ANSWER
→ If caller still hesitant but open: Offer callback, then Route to GOODBYE
→ If hard NO: Route to GOODBYE')
WHERE prompt_id = (SELECT id FROM prompts WHERE node_name = 'objections' AND vertical = 'reverse_mortgage')
AND is_active = true
AND NOT (content ? 'routing');

-- BOOK routing
UPDATE prompt_versions
SET content = content || jsonb_build_object('routing',
'→ After appointment booked and confirmed: Route to GOODBYE
→ If booking fails repeatedly: Route to GOODBYE (with manual follow-up)
→ If caller wants to reschedule: Stay in BOOK')
WHERE prompt_id = (SELECT id FROM prompts WHERE node_name = 'book' AND vertical = 'reverse_mortgage')
AND is_active = true
AND NOT (content ? 'routing');

-- GOODBYE routing
UPDATE prompt_versions
SET content = content || jsonb_build_object('routing',
'→ If caller has last-minute questions: Route to ANSWER
→ Otherwise: End call')
WHERE prompt_id = (SELECT id FROM prompts WHERE node_name = 'goodbye' AND vertical = 'reverse_mortgage')
AND is_active = true
AND NOT (content ? 'routing');

-- Verify
SELECT node_name, content->>'routing' as routing
FROM active_node_prompts
WHERE vertical = 'reverse_mortgage'
ORDER BY node_name;






