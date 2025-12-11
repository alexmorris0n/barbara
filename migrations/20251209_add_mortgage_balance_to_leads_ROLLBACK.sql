-- Rollback: Remove mortgage_balance column from leads table

-- Drop the index first
DROP INDEX IF EXISTS idx_leads_mortgage_balance;

-- Remove the column
ALTER TABLE leads DROP COLUMN IF EXISTS mortgage_balance;







