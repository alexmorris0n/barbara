-- ROLLBACK: Drop appointments table
-- Date: 2025-12-10

DROP TRIGGER IF EXISTS update_appointments_updated_at ON appointments;
DROP FUNCTION IF EXISTS update_appointments_updated_at;
DROP TABLE IF EXISTS appointments;

