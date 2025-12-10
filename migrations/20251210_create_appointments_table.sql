-- Migration: Create appointments table for reminders
-- Date: 2025-12-10

CREATE TABLE IF NOT EXISTS appointments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    lead_id UUID REFERENCES leads(id),
    broker_id UUID REFERENCES brokers(id),
    appointment_time TIMESTAMPTZ NOT NULL,
    status TEXT NOT NULL DEFAULT 'scheduled',
    nylas_event_id TEXT,
    
    -- SMS consent (CRITICAL for compliance)
    sms_consent BOOLEAN DEFAULT FALSE,
    
    -- Reminder tracking
    confirmation_sent BOOLEAN DEFAULT FALSE,
    reminder_24h_sent BOOLEAN DEFAULT FALSE,
    reminder_1h_sent BOOLEAN DEFAULT FALSE,
    
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index for finding upcoming appointments for reminders
CREATE INDEX idx_appointments_time_status ON appointments(appointment_time, status);

-- Trigger to update updated_at
CREATE OR REPLACE FUNCTION update_appointments_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_appointments_updated_at
    BEFORE UPDATE ON appointments
    FOR EACH ROW
    EXECUTE FUNCTION update_appointments_updated_at();

