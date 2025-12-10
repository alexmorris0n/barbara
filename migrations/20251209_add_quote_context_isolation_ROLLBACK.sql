-- Rollback: Remove quote context isolation config

DELETE FROM contexts_config 
WHERE vertical = 'reverse_mortgage' 
  AND context_name = 'quote';



