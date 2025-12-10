-- Rollback: Remove context filler configurations

DELETE FROM contexts_config 
WHERE vertical = 'reverse_mortgage' 
  AND context_name IN ('book', 'objections', 'answer');

-- Clear fillers from quote (keep the row for isolation setting)
UPDATE contexts_config 
SET enter_fillers = '[]'::jsonb, exit_fillers = '[]'::jsonb
WHERE vertical = 'reverse_mortgage' AND context_name = 'quote';




