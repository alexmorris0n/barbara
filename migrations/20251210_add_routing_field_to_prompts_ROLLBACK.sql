-- Rollback: Remove routing field from prompt_versions content JSONB
-- Date: 2025-12-10

-- Remove routing field from all prompt versions
UPDATE prompt_versions
SET content = content - 'routing'
WHERE content ? 'routing';

-- Verify
SELECT node_name, content->>'routing' as routing
FROM active_node_prompts
WHERE vertical = 'reverse_mortgage'
ORDER BY node_name;






