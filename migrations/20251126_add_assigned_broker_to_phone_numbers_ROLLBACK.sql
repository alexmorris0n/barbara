-- Rollback: Remove assigned_broker_id column from phone_numbers
DROP INDEX IF EXISTS idx_phone_numbers_assigned_broker;
ALTER TABLE phone_numbers DROP COLUMN IF EXISTS assigned_broker_id;

















