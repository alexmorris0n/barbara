-- Rollback: Remove anon read policies for MCP
DROP POLICY IF EXISTS "anon_read_phone_numbers" ON phone_numbers;
DROP POLICY IF EXISTS "anon_read_leads_for_mcp" ON leads;












