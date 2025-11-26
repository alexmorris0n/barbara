-- ROLLBACK: Remove broker business hours columns
-- Run this to undo the add_broker_business_hours and add_broker_minimum_lead_time migrations

ALTER TABLE brokers 
DROP COLUMN IF EXISTS business_hours_start,
DROP COLUMN IF EXISTS business_hours_end,
DROP COLUMN IF EXISTS business_days,
DROP COLUMN IF EXISTS appointment_duration_minutes,
DROP COLUMN IF EXISTS buffer_between_appointments_minutes,
DROP COLUMN IF EXISTS minimum_booking_lead_time_minutes;

