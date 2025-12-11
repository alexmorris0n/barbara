-- Rollback: Remove interaction lead linking trigger

DROP TRIGGER IF EXISTS trg_link_interaction_to_lead ON interactions;
DROP FUNCTION IF EXISTS link_interaction_to_lead();

-- Note: Does not un-link already linked interactions







