-- Ensure QUALIFY captures exact numeric age and QUOTE is tool-first.
-- This keeps DB prompts aligned with the code/tool expectations and fallback prompts.
--
-- Safety:
-- - Only touches active prompt_versions (is_active = true)
-- - Backs up prior instructions + step_criteria into content.backup_20251212_{node}

-- QUALIFY: require exact numeric age capture (update_lead_info(age=X))
UPDATE prompt_versions pv
SET content =
  jsonb_set(
    jsonb_set(
      jsonb_set(
        pv.content,
        '{backup_20251212_qualify}',
        jsonb_build_object(
          'instructions', COALESCE(pv.content->>'instructions',''),
          'step_criteria', COALESCE(pv.content->>'step_criteria','')
        ),
        true
      ),
      '{instructions}',
      to_jsonb(
        COALESCE(pv.content->>'instructions','') ||
        E'\n\n=== EXACT AGE (REQUIRED FOR QUOTE) ===\nAfter confirming they are 62+, ask: "What is your exact age?" Then call update_lead_info(age=<age>).'
      ),
      true
    ),
    '{step_criteria}',
    to_jsonb(
      'Age confirmed 62+ and exact numeric age captured via update_lead_info(age=X). Home value and mortgage collected. Route to QUOTE.'::text
    ),
    true
  )
FROM prompts p
WHERE p.id = pv.prompt_id
  AND p.vertical = 'reverse_mortgage'
  AND p.is_active = true
  AND p.node_name = 'qualify'
  AND pv.is_active = true;

-- QUOTE: enforce calculate-first and require exact age if missing
UPDATE prompt_versions pv
SET content =
  jsonb_set(
    jsonb_set(
      jsonb_set(
        pv.content,
        '{backup_20251212_quote}',
        jsonb_build_object(
          'instructions', COALESCE(pv.content->>'instructions',''),
          'step_criteria', COALESCE(pv.content->>'step_criteria','')
        ),
        true
      ),
      '{instructions}',
      to_jsonb(
        COALESCE(pv.content->>'instructions','') ||
        E'\n\n=== CRITICAL (DB ENFORCED) ===\nBefore stating ANY dollar amounts, call calculate_reverse_mortgage(). Do NOT estimate.\nIf age is only "62+" (not exact), ask for the exact age and call update_lead_info(age=<age>) first.\nAfter presenting the estimate, call mark_quote_presented().'
      ),
      true
    ),
    '{step_criteria}',
    to_jsonb(
      'Quote presented via calculate tool (no estimating), mark_quote_presented() called, booking offered.'::text
    ),
    true
  )
FROM prompts p
WHERE p.id = pv.prompt_id
  AND p.vertical = 'reverse_mortgage'
  AND p.is_active = true
  AND p.node_name = 'quote'
  AND pv.is_active = true;


