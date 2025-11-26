# Barbara MCP Server

A Model Context Protocol (MCP) server that exposes Barbara's functionality as tools for n8n AI Agent. This enables n8n workflows to trigger outbound calls and manage appointments through the Barbara system.

## Features

- **Outbound Calls**: Trigger calls to leads via SignalWire AI SDK (same Barbara agent handles inbound & outbound)
- **Calendar Management**: Check broker availability, book/cancel/reschedule appointments via Nylas
- **Lead Management**: Update lead contact information in Supabase
- **MCP Protocol**: Standard MCP interface for n8n integration

## Architecture

```
n8n Workflow → Barbara MCP → SignalWire / Bridge Server
                   │
                   ├─→ create_outbound_call → SignalWire Calls API → Barbara Agent
                   │
                   └─→ calendar/lead tools → Bridge Server → Nylas / Supabase
```

## Quick Start

### 1. Install Dependencies

```bash
cd barbara-mcp
npm install
```

### 2. Configure Environment

Copy `env.example` to `.env` and update:

```bash
cp env.example .env
```

Required variables:
- `BRIDGE_URL`: Bridge server URL for calendar/database operations
- `BRIDGE_API_KEY`: Secure API key for bridge authentication
- `SIGNALWIRE_PROJECT_ID`: Your SignalWire project ID
- `SIGNALWIRE_API_TOKEN`: Your SignalWire API token
- `SIGNALWIRE_SPACE_URL`: Your SignalWire space URL (e.g., `https://your-space.signalwire.com`)
- `SIGNALWIRE_PHONE_NUMBER`: Default outbound caller ID (E.164 format)
- `BARBARA_AGENT_URL`: URL to your Barbara agent endpoint (default: `https://barbara-swaig.fly.dev/agent/barbara`)

### 3. Run Locally

```bash
npm start
```

The server will start on port 3000 with the following endpoints:
- `GET /health` - Health check
- `POST /mcp` - MCP protocol endpoint for n8n

## API Reference

### Tools

#### create_outbound_call

Creates an outbound call to a lead using the Barbara AI agent.

**Parameters:**
- `to_phone` (required): Phone number to call (E.164 format)
- `lead_id` (required): Lead ID from the database
- `from_phone` (optional): SignalWire number to call from
- `broker_id` (optional): Broker ID (if not provided, uses lead's assigned broker)

**Response:**
```json
{
  "success": true,
  "message": "✅ Outbound Call Initiated!",
  "call_sid": "CA123...",
  "to_number": "+16505300051",
  "status": "queued"
}
```

#### check_broker_availability

Check broker calendar availability via Nylas.

**Parameters:**
- `broker_id` (required): Broker UUID
- `preferred_day` (optional): 'any', 'monday', 'tuesday', etc.
- `preferred_time` (optional): 'any', 'morning', 'afternoon'

#### book_appointment

Book an appointment on broker's calendar.

**Parameters:**
- `lead_id` (required): Lead UUID
- `broker_id` (required): Broker UUID
- `scheduled_for` (required): ISO 8601 datetime
- `notes` (optional): Appointment notes

#### cancel_appointment

Cancel an existing appointment.

**Parameters:**
- `lead_id` (required): Lead UUID

#### reschedule_appointment

Reschedule an existing appointment.

**Parameters:**
- `lead_id` (required): Lead UUID
- `new_scheduled_for` (required): New ISO 8601 datetime

#### update_lead_info

Update lead information in Supabase.

**Parameters:**
- `lead_id` (required): Lead UUID
- `first_name`, `last_name`, `primary_phone`, `primary_email`, `city`, `state`, `zipcode`, `age`, `property_value`, `mortgage_balance` (all optional)

### Endpoints

#### GET /health

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00.000Z",
  "signalwire_configured": true,
  "bridge_url": "https://bridge.northflank.app"
}
```

#### POST /mcp

MCP protocol endpoint for n8n integration.

**Request Body:**
```json
{
  "method": "tools/call",
  "params": {
    "name": "create_outbound_call",
    "arguments": {
      "to_phone": "+16505300051",
      "lead_id": "lead-123"
    }
  }
}
```

## Deployment

### Fly.io (Recommended)

```bash
cd barbara-mcp

# First time: create the app
fly apps create barbara-mcp

# Set secrets
fly secrets set \
  BRIDGE_URL=https://barbara-swaig.fly.dev \
  BRIDGE_API_KEY=your-api-key \
  SIGNALWIRE_PROJECT_ID=your-project-id \
  SIGNALWIRE_API_TOKEN=your-api-token \
  SIGNALWIRE_SPACE_URL=https://your-space.signalwire.com \
  SIGNALWIRE_PHONE_NUMBER=+1XXXXXXXXXX \
  BARBARA_AGENT_URL=https://barbara-swaig.fly.dev/agent/barbara

# Deploy
fly deploy
```

### Docker (Local)

```bash
docker build -t barbara-mcp .
docker run -p 3000:3000 \
  -e BRIDGE_URL=https://barbara-swaig.fly.dev \
  -e BRIDGE_API_KEY=your-api-key \
  -e SIGNALWIRE_PROJECT_ID=your-project-id \
  -e SIGNALWIRE_API_TOKEN=your-api-token \
  -e SIGNALWIRE_SPACE_URL=https://your-space.signalwire.com \
  -e SIGNALWIRE_PHONE_NUMBER=+1XXXXXXXXXX \
  barbara-mcp
```

## n8n Integration

1. Add "MCP Client Tool" node
2. Configure endpoint URL: `https://your-barbara-mcp-url/mcp`
3. Use tools in AI Agent workflows:
   - `create_outbound_call` - Trigger calls to leads
   - `check_broker_availability` - Check calendars before booking
   - `book_appointment` - Schedule appointments
   - `update_lead_info` - Update lead data

## Testing

```bash
# Health check
curl http://localhost:3000/health

# List tools
curl -X POST http://localhost:3000/mcp \
  -H "Content-Type: application/json" \
  -d '{"method": "tools/list"}'

# Create outbound call
curl -X POST http://localhost:3000/mcp \
  -H "Content-Type: application/json" \
  -d '{
    "method": "tools/call",
    "params": {
      "name": "create_outbound_call",
      "arguments": {
        "to_phone": "+16505300051",
        "lead_id": "test-lead-id"
      }
    }
  }'
```

## Troubleshooting

### Common Issues

1. **SignalWire Call Failed**
   - Verify all SignalWire env vars are set
   - Check phone number format (E.164)
   - Verify Barbara agent URL is accessible

2. **Bridge API Errors**
   - Check `BRIDGE_URL` and `BRIDGE_API_KEY`
   - Verify bridge server is running

3. **n8n Integration Issues**
   - Verify MCP endpoint URL is correct
   - Check n8n workflow logs

## License

MIT License
