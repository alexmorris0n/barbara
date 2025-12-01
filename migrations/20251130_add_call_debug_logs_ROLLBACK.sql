-- Rollback: Remove call_debug_logs table

-- Drop indexes first
DROP INDEX IF EXISTS idx_call_debug_logs_call_id;
DROP INDEX IF EXISTS idx_call_debug_logs_lead_id;
DROP INDEX IF EXISTS idx_call_debug_logs_event_type;

-- Drop table
DROP TABLE IF EXISTS call_debug_logs;


