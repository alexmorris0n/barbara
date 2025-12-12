-- Rollback for 20251212_quote_numeric_age.sql
-- Restores instructions + step_criteria from content.backup_20251212_{node}

-- QUALIFY rollback
UPDATE prompt_versions pv
SET content =
  (
    jsonb_set(
      jsonb_set(
        pv.content,
        '{instructions}',
        to_jsonb(COALESCE(pv.content #>> '{backup_20251212_qualify,instructions}', pv.content->>'instructions')),
        true
      ),
      '{step_criteria}',
      to_jsonb(COALESCE(pv.content #>> '{backup_20251212_qualify,step_criteria}', pv.content->>'step_criteria')),
      true
    ) - 'backup_20251212_qualify'
  )
FROM prompts p
WHERE p.id = pv.prompt_id
  AND p.vertical = 'reverse_mortgage'
  AND p.is_active = true
  AND p.node_name = 'qualify'
  AND pv.is_active = true
  AND (pv.content ? 'backup_20251212_qualify');

-- QUOTE rollback
UPDATE prompt_versions pv
SET content =
  (
    jsonb_set(
      jsonb_set(
        pv.content,
        '{instructions}',
        to_jsonb(COALESCE(pv.content #>> '{backup_20251212_quote,instructions}', pv.content->>'instructions')),
        true
      ),
      '{step_criteria}',
      to_jsonb(COALESCE(pv.content #>> '{backup_20251212_quote,step_criteria}', pv.content->>'step_criteria')),
      true
    ) - 'backup_20251212_quote'
  )
FROM prompts p
WHERE p.id = pv.prompt_id
  AND p.vertical = 'reverse_mortgage'
  AND p.is_active = true
  AND p.node_name = 'quote'
  AND pv.is_active = true
  AND (pv.content ? 'backup_20251212_quote');


