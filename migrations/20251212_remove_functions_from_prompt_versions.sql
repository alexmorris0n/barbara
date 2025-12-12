-- Remove legacy "functions" field from prompt_versions.content and standardize on "tools"
-- This prevents hidden "functions" from overriding what Vue shows/edits.
--
-- Strategy (reversible):
-- 1) Backup existing content.tools and content.functions into:
--    - content.legacy_tools_backup
--    - content.legacy_functions_backup
-- 2) Ensure content.tools contains the union of (tools ∪ functions) with duplicates removed
-- 3) Remove content.functions
--
-- Scope:
-- - Active prompt_versions only (is_active = true)
-- - All verticals / node prompts (safe because we retain backups)

UPDATE prompt_versions pv
SET content =
  (
    jsonb_set(
      jsonb_set(
        jsonb_set(
          pv.content,
          '{legacy_tools_backup}',
          COALESCE(pv.content->'tools', 'null'::jsonb),
          true
        ),
        '{legacy_functions_backup}',
        COALESCE(pv.content->'functions', 'null'::jsonb),
        true
      ),
      '{tools}',
      (
        SELECT COALESCE(
          jsonb_agg(DISTINCT to_jsonb(fn_name)) FILTER (WHERE fn_name IS NOT NULL AND fn_name <> ''),
          '[]'::jsonb
        )
        FROM (
          SELECT jsonb_array_elements_text(
                   CASE
                     WHEN jsonb_typeof(pv.content->'tools') = 'array' THEN pv.content->'tools'
                     ELSE '[]'::jsonb
                   END
                 ) AS fn_name
          UNION
          SELECT jsonb_array_elements_text(
                   CASE
                     WHEN jsonb_typeof(pv.content->'functions') = 'array' THEN pv.content->'functions'
                     ELSE '[]'::jsonb
                   END
                 ) AS fn_name
        ) s
      ),
      true
    )
    - 'functions'
  )
WHERE pv.is_active = true;


