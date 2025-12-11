-- Migration: Fix interaction broker_id linking
-- Problem: Interactions are created with broker_id = NULL
-- Solution: 
--   1. Update trigger to also set broker_id from lead's assigned_broker_id
--   2. Backfill existing interactions

-- Update the trigger function to also set broker_id
CREATE OR REPLACE FUNCTION link_interaction_to_lead()
RETURNS TRIGGER AS $$
DECLARE
    found_lead_id UUID;
    found_broker_id UUID;
    phone_number TEXT;
BEGIN
    -- Only process if lead_id is NULL and we have a phone in metadata
    IF NEW.lead_id IS NULL AND NEW.metadata->>'phone' IS NOT NULL THEN
        phone_number := NEW.metadata->>'phone';
        
        -- Look up lead by phone (try both formats)
        SELECT id, assigned_broker_id INTO found_lead_id, found_broker_id
        FROM leads
        WHERE primary_phone = phone_number
           OR primary_phone_e164 = '+1' || phone_number
           OR primary_phone_e164 = phone_number
        LIMIT 1;
        
        -- Update the lead_id and broker_id if found
        IF found_lead_id IS NOT NULL THEN
            NEW.lead_id := found_lead_id;
            NEW.broker_id := found_broker_id;  -- Also set broker_id!
        END IF;
    END IF;
    
    -- If lead_id is set but broker_id is NULL, look up the broker
    IF NEW.lead_id IS NOT NULL AND NEW.broker_id IS NULL THEN
        SELECT assigned_broker_id INTO found_broker_id
        FROM leads
        WHERE id = NEW.lead_id;
        
        IF found_broker_id IS NOT NULL THEN
            NEW.broker_id := found_broker_id;
        END IF;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Recreate trigger
DROP TRIGGER IF EXISTS trg_link_interaction_to_lead ON interactions;
CREATE TRIGGER trg_link_interaction_to_lead
    BEFORE INSERT ON interactions
    FOR EACH ROW
    EXECUTE FUNCTION link_interaction_to_lead();

-- Backfill existing interactions with NULL broker_id
UPDATE interactions i
SET broker_id = l.assigned_broker_id
FROM leads l
WHERE i.lead_id = l.id
  AND i.broker_id IS NULL
  AND l.assigned_broker_id IS NOT NULL;

COMMENT ON FUNCTION link_interaction_to_lead() IS 'Auto-links interactions to leads based on phone number in metadata, and sets broker_id from lead';








