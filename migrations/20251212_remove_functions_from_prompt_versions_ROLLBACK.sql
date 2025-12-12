-- Rollback for 20251212_remove_functions_from_prompt_versions.sql
-- Restores content.tools and content.functions from legacy_*_backup keys (when present),
-- and removes the backup keys.

UPDATE prompt_versions pv
SET content =
  (
    (
      CASE
        WHEN pv.content->'legacy_functions_backup' IS NULL THEN
          (
            CASE
              -- Restore tools if we have a non-null backup; otherwise keep current tools as-is
              WHEN pv.content->'legacy_tools_backup' IS NULL THEN pv.content
              ELSE jsonb_set(pv.content, '{tools}', pv.content->'legacy_tools_backup', true)
            END
          ) - 'functions'
        ELSE
          jsonb_set(
            (
              CASE
                WHEN pv.content->'legacy_tools_backup' IS NULL THEN pv.content
                ELSE jsonb_set(pv.content, '{tools}', pv.content->'legacy_tools_backup', true)
              END
            ),
            '{functions}',
            pv.content->'legacy_functions_backup',
            true
          )
      END
    )
    - 'legacy_tools_backup'
    - 'legacy_functions_backup'
  )
WHERE pv.is_active = true;


