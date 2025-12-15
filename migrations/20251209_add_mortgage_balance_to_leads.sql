-- Migration: Add mortgage_balance column to leads table
-- This stores the mortgage balance collected during qualification calls

-- Add the column
ALTER TABLE leads 
ADD COLUMN IF NOT EXISTS mortgage_balance NUMERIC
COMMENT 'Current mortgage balance on the property, collected during qualification';

-- Create index for filtering/sorting by mortgage balance
CREATE INDEX IF NOT EXISTS idx_leads_mortgage_balance ON leads(mortgage_balance);

-- Comment
COMMENT ON COLUMN leads.mortgage_balance IS 'Current mortgage balance on the property, collected during qualification calls';








