-- Migration: Add LLM parameters to agent_params table
-- Purpose: Enable Vue portal control of top_p, frequency_penalty, presence_penalty
-- Currently these are hardcoded in barbara_agent.py

-- Add top_p column (SDK default: 1.0)
ALTER TABLE agent_params 
ADD COLUMN IF NOT EXISTS top_p DECIMAL(3,2) DEFAULT 1.0;

-- Add frequency_penalty column (currently hardcoded as 0.4)
ALTER TABLE agent_params 
ADD COLUMN IF NOT EXISTS frequency_penalty DECIMAL(3,2) DEFAULT 0.4;

-- Add presence_penalty column (currently hardcoded as 0.2)
ALTER TABLE agent_params 
ADD COLUMN IF NOT EXISTS presence_penalty DECIMAL(3,2) DEFAULT 0.2;

-- Add comments for Vue portal reference
COMMENT ON COLUMN agent_params.top_p IS 'Controls diversity via nucleus sampling. Range: 0.0-1.0. Default: 1.0';
COMMENT ON COLUMN agent_params.frequency_penalty IS 'Reduces repetitive phrasing. Range: 0.0-2.0. Default: 0.4';
COMMENT ON COLUMN agent_params.presence_penalty IS 'Encourages topic variety. Range: 0.0-2.0. Default: 0.2';

-- Update existing rows with current hardcoded values
UPDATE agent_params 
SET 
    top_p = 1.0,
    frequency_penalty = 0.4,
    presence_penalty = 0.2
WHERE top_p IS NULL 
   OR frequency_penalty IS NULL 
   OR presence_penalty IS NULL;





















