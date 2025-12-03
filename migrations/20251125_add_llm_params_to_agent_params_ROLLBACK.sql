-- ROLLBACK: Remove LLM parameters from agent_params table
-- Reverses: 20251125_add_llm_params_to_agent_params.sql

ALTER TABLE agent_params DROP COLUMN IF EXISTS top_p;
ALTER TABLE agent_params DROP COLUMN IF EXISTS frequency_penalty;
ALTER TABLE agent_params DROP COLUMN IF EXISTS presence_penalty;

















