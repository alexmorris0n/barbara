-- Migration: Add call_debug_logs table for storing debug webhook data
-- This captures transcripts, tool calls, and other conversation events from SignalWire
-- Per SDK line 23689: debug_webhook_url receives debug data

-- Table for debug webhook data (transcripts, tool calls, events)
CREATE TABLE IF NOT EXISTS call_debug_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    call_id TEXT NOT NULL,
    lead_id UUID REFERENCES leads(id),
    event_type TEXT,  -- 'speech', 'tool_call', 'context_switch', etc.
    event_data JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index for looking up events by call_id
CREATE INDEX IF NOT EXISTS idx_call_debug_logs_call_id ON call_debug_logs(call_id);

-- Index for looking up events by lead_id
CREATE INDEX IF NOT EXISTS idx_call_debug_logs_lead_id ON call_debug_logs(lead_id);

-- Index for filtering by event_type
CREATE INDEX IF NOT EXISTS idx_call_debug_logs_event_type ON call_debug_logs(event_type);

-- Comment on table
COMMENT ON TABLE call_debug_logs IS 'Stores debug webhook data from SignalWire including transcripts and tool calls';













