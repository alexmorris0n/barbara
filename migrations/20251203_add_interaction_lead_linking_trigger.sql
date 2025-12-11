-- Migration: Add trigger to auto-link interactions to leads based on phone in metadata
-- This allows the agent to save interactions without needing to know the lead_id,
-- and the database will automatically link them based on phone number.

-- Trigger function to auto-link interactions to leads based on phone in metadata
CREATE OR REPLACE FUNCTION link_interaction_to_lead()
RETURNS TRIGGER AS $$
DECLARE
    found_lead_id UUID;
    phone_number TEXT;
BEGIN
    -- Only process if lead_id is NULL and we have a phone in metadata
    IF NEW.lead_id IS NULL AND NEW.metadata->>'phone' IS NOT NULL THEN
        phone_number := NEW.metadata->>'phone';
        
        -- Look up lead by phone (try both formats)
        SELECT id INTO found_lead_id
        FROM leads
        WHERE primary_phone = phone_number
           OR primary_phone_e164 = '+1' || phone_number
           OR primary_phone_e164 = phone_number
        LIMIT 1;
        
        -- Update the lead_id if found
        IF found_lead_id IS NOT NULL THEN
            NEW.lead_id := found_lead_id;
        END IF;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create trigger on interactions table
DROP TRIGGER IF EXISTS trg_link_interaction_to_lead ON interactions;
CREATE TRIGGER trg_link_interaction_to_lead
    BEFORE INSERT ON interactions
    FOR EACH ROW
    EXECUTE FUNCTION link_interaction_to_lead();

COMMENT ON FUNCTION link_interaction_to_lead() IS 'Auto-links interactions to leads based on phone number in metadata';








