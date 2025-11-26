import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { CallToolRequestSchema, ListToolsRequestSchema } from '@modelcontextprotocol/sdk/types.js';
import fastify from 'fastify';
import cors from '@fastify/cors';

// Initialize Fastify for HTTP streaming transport
const app = fastify({
  logger: {
    level: 'info',
    transport: {
      target: 'pino-pretty',
      options: {
        colorize: true,
        translateTime: 'HH:MM:ss',
        ignore: 'pid,hostname'
      }
    }
  }
});

// Register CORS
await app.register(cors, {
  origin: true,
  credentials: true
});

// Environment variables
const BRIDGE_URL = process.env.BRIDGE_URL || 'https://bridge.northflank.app';
const BRIDGE_API_KEY = process.env.BRIDGE_API_KEY;

// SignalWire credentials for outbound calls
const SIGNALWIRE_PROJECT_ID = process.env.SIGNALWIRE_PROJECT_ID;
const SIGNALWIRE_API_TOKEN = process.env.SIGNALWIRE_API_TOKEN;
const SIGNALWIRE_SPACE_URL = process.env.SIGNALWIRE_SPACE_URL;
const SIGNALWIRE_PHONE_NUMBER = process.env.SIGNALWIRE_PHONE_NUMBER;

// Barbara Agent URL (SignalWire AI SDK)
// Must point to the SWML endpoint: /agent/barbara
const BARBARA_AGENT_URL = process.env.BARBARA_AGENT_URL || 'https://barbara-agent.fly.dev/agent/barbara';

const SIGNALWIRE_FEATURES_ENABLED = Boolean(
  SIGNALWIRE_PROJECT_ID &&
  SIGNALWIRE_API_TOKEN &&
  SIGNALWIRE_SPACE_URL &&
  SIGNALWIRE_PHONE_NUMBER
);

if (!BRIDGE_API_KEY) {
  app.log.error('BRIDGE_API_KEY environment variable is required');
  process.exit(1);
}

if (!SIGNALWIRE_FEATURES_ENABLED) {
  app.log.warn('⚠️  SignalWire credentials not fully configured - outbound calls will fail');
  app.log.warn('   Required: SIGNALWIRE_PROJECT_ID, SIGNALWIRE_API_TOKEN, SIGNALWIRE_SPACE_URL, SIGNALWIRE_PHONE_NUMBER');
}

// SignalWire Fabric guest token config
const SIGNALWIRE_ALLOWED_ADDRESSES = process.env.SIGNALWIRE_ALLOWED_ADDRESSES || '';
const SIGNALWIRE_GUEST_TOKEN_PATH = process.env.SIGNALWIRE_GUEST_TOKEN_PATH || '/api/fabric/guests/tokens';

const parsedAllowedAddresses = SIGNALWIRE_ALLOWED_ADDRESSES
  .split(',')
  .map(addr => addr.trim())
  .filter(Boolean);

function getSignalWireAuthHeader() {
  return `Basic ${Buffer.from(`${SIGNALWIRE_PROJECT_ID}:${SIGNALWIRE_API_TOKEN}`).toString('base64')}`;
}

function buildSignalWireUrl(path) {
  try {
    return new URL(path, SIGNALWIRE_SPACE_URL).toString();
  } catch (error) {
    return `${SIGNALWIRE_SPACE_URL}${path}`;
  }
}

// Guest token endpoint for web deployment (SignalWire Fabric)
app.post('/api/token', async (request, reply) => {
  if (!SIGNALWIRE_FEATURES_ENABLED) {
    return reply.status(500).send({ error: 'SignalWire credentials are not configured' });
  }

  if (!parsedAllowedAddresses.length) {
    return reply.status(500).send({ error: 'SIGNALWIRE_ALLOWED_ADDRESSES is not configured' });
  }

  const expiresAt = new Date(Date.now() + 60 * 60 * 1000).toISOString();
  const payload = {
    allowed_addresses: parsedAllowedAddresses,
    ttl: 3600,
    expires_at: expiresAt,
    state: {
      type: 'barbara-web-call'
    }
  };

  try {
    const response = await fetch(buildSignalWireUrl(SIGNALWIRE_GUEST_TOKEN_PATH), {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: getSignalWireAuthHeader()
      },
      body: JSON.stringify(payload)
    });

    const data = await response.json().catch(() => ({}));

    if (!response.ok) {
      app.log.error({ status: response.status, data }, 'Failed to generate guest token');
      return reply.status(500).send({ error: data.message || 'Failed to generate guest token' });
    }

    const token = data.token || data.jwt_token || data.jwt || data.access_token;

    if (!token) {
      app.log.error({ data }, 'Guest token response missing token property');
      return reply.status(500).send({ error: 'Guest token response missing token' });
    }

    app.log.info('✅ Guest token generated for web deployment');
    return reply.send({ token, expires_at: expiresAt });
  } catch (error) {
    app.log.error({ error }, 'Error generating guest token');
    return reply.status(500).send({ error: 'Failed to generate guest token' });
  }
});

// Tool definitions
const tools = [
  {
    name: 'check_broker_availability',
    description: 'Check broker calendar availability using Nylas Free/Busy API. Returns available time slots for the next 14 days with smart prioritization (today > tomorrow > next week). Business hours: 10 AM - 5 PM with 2-hour minimum notice.',
    inputSchema: {
      type: 'object',
      properties: {
        broker_id: {
          type: 'string',
          description: 'Broker UUID to check availability for'
        },
        preferred_day: {
          type: 'string',
          enum: ['any', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday'],
          description: 'Preferred day of week (optional, default: any)'
        },
        preferred_time: {
          type: 'string',
          enum: ['any', 'morning', 'afternoon'],
          description: 'Preferred time of day (optional, default: any). Morning = 10 AM-12 PM, Afternoon = 12 PM-5 PM'
        }
      },
      required: ['broker_id']
    }
  },
  {
    name: 'book_appointment',
    description: 'Book an appointment with a broker using Nylas Events API. Creates calendar event on broker\'s calendar and sends calendar invite to lead (if email provided).',
    inputSchema: {
      type: 'object',
      properties: {
        lead_id: {
          type: 'string',
          description: 'Lead UUID'
        },
        broker_id: {
          type: 'string',
          description: 'Broker UUID'
        },
        scheduled_for: {
          type: 'string',
          description: 'Appointment date/time in ISO 8601 format (e.g., "2025-10-22T10:00:00Z")'
        },
        notes: {
          type: 'string',
          description: 'Optional notes about the appointment (e.g., "Interested in accessing equity for medical expenses")'
        }
      },
      required: ['lead_id', 'broker_id', 'scheduled_for']
    }
  },
  {
    name: 'cancel_appointment',
    description: 'Cancel an existing appointment with a broker. Removes the Nylas calendar event and notifies all participants.',
    inputSchema: {
      type: 'object',
      properties: {
        lead_id: {
          type: 'string',
          description: 'Lead UUID'
        }
      },
      required: ['lead_id']
    }
  },
  {
    name: 'reschedule_appointment',
    description: 'Reschedule an existing appointment to a new time. Updates the Nylas calendar event and sends updated invites to all participants.',
    inputSchema: {
      type: 'object',
      properties: {
        lead_id: {
          type: 'string',
          description: 'Lead UUID'
        },
        new_scheduled_for: {
          type: 'string',
          description: 'New appointment date/time in ISO 8601 format (e.g., "2025-10-22T14:00:00Z")'
        }
      },
      required: ['lead_id', 'new_scheduled_for']
    }
  },
  {
    name: 'update_lead_info',
    description: 'Update lead contact information in the database. Used to collect or correct phone, email, name, address, etc.',
    inputSchema: {
      type: 'object',
      properties: {
        lead_id: {
          type: 'string',
          description: 'Lead UUID'
        },
        primary_phone: {
          type: 'string',
          description: 'Primary phone number (E.164 format recommended)'
        },
        primary_email: {
          type: 'string',
          description: 'Primary email address'
        },
        first_name: {
          type: 'string',
          description: 'First name'
        },
        last_name: {
          type: 'string',
          description: 'Last name'
        },
        city: {
          type: 'string',
          description: 'City'
        },
        state: {
          type: 'string',
          description: 'State'
        },
        zipcode: {
          type: 'string',
          description: 'ZIP code'
        },
        age: {
          type: 'number',
          description: 'Age'
        },
        property_value: {
          type: 'number',
          description: 'Estimated property value'
        },
        mortgage_balance: {
          type: 'number',
          description: 'Current mortgage balance'
        }
      },
      required: ['lead_id']
    }
  },
  {
    name: 'create_outbound_call',
    description: 'Create an outbound call to a lead using SignalWire AI SDK (Barbara agent). The same Barbara agent handles both inbound and outbound calls.',
    inputSchema: {
      type: 'object',
      properties: {
        to_phone: {
          type: 'string',
          description: 'Phone number to call (will be normalized to E.164 format)'
        },
        lead_id: {
          type: 'string',
          description: 'Lead ID from the database'
        },
        from_phone: {
          type: 'string',
          description: 'Optional SignalWire number to call FROM. If not provided, uses default.'
        },
        broker_id: {
          type: 'string',
          description: 'Optional broker ID (if not provided, will use lead\'s assigned broker)'
        }
      },
      required: ['to_phone', 'lead_id']
    }
  }
];

// Tool execution function
async function executeTool(name, args) {
  switch (name) {
    case 'check_broker_availability': {
      app.log.info({ broker_id: args.broker_id }, '📅 Checking broker availability');
      
      try {
        const response = await fetch(`${BRIDGE_URL}/api/tools/check_broker_availability`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${BRIDGE_API_KEY}`
          },
          body: JSON.stringify(args)
        });
        
        const result = await response.json();
        
        if (result.success) {
          app.log.info({ slots: result.available_slots?.length }, '✅ Availability checked');
          return {
            content: [
              {
                type: 'text',
                text: `✅ Availability Check Complete\n\n` +
                      `📅 Broker: ${result.broker_name}\n` +
                      `⏰ Available Slots: ${result.available_slots?.length || 0}\n` +
                      `💬 ${result.message}\n\n` +
                      `📋 Slots:\n` +
                      (result.available_slots || []).slice(0, 5).map(slot => 
                        `  • ${slot.display}${slot.is_same_day ? ' (TODAY)' : slot.is_tomorrow ? ' (TOMORROW)' : ''}`
                      ).join('\n')
              }
            ]
          };
        } else {
          throw new Error(result.error || 'Availability check failed');
        }
      } catch (error) {
        app.log.error({ error }, '❌ Availability check error');
        return {
          content: [
            {
              type: 'text',
              text: `❌ Availability check failed: ${error.message}`
            }
          ],
          isError: true
        };
      }
    }
    
    case 'book_appointment': {
      app.log.info({ lead_id: args.lead_id, broker_id: args.broker_id }, '📅 Booking appointment');
      
      try {
        const response = await fetch(`${BRIDGE_URL}/api/tools/book_appointment`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${BRIDGE_API_KEY}`
          },
          body: JSON.stringify(args)
        });
        
        const result = await response.json();
        
        if (result.success) {
          app.log.info({ appointment_id: result.appointment_id }, '✅ Appointment booked');
          return {
            content: [
              {
                type: 'text',
                text: `✅ Appointment Booked Successfully!\n\n` +
                      `📅 Time: ${new Date(args.scheduled_for).toLocaleString()}\n` +
                      `👤 Lead ID: ${args.lead_id}\n` +
                      `🏢 Broker ID: ${args.broker_id}\n` +
                      `📧 Calendar invite sent: ${result.calendar_invite_sent ? 'Yes' : 'No (email missing)'}\n` +
                      `📝 Notes: ${args.notes || 'None'}`
              }
            ]
          };
        } else {
          throw new Error(result.error || 'Appointment booking failed');
        }
      } catch (error) {
        app.log.error({ error }, '❌ Appointment booking error');
        return {
          content: [
            {
              type: 'text',
              text: `❌ Appointment booking failed: ${error.message}`
            }
          ],
          isError: true
        };
      }
    }
    
    case 'cancel_appointment': {
      app.log.info({ lead_id: args.lead_id }, '🗑️ Canceling appointment');
      
      try {
        const response = await fetch(`${BRIDGE_URL}/api/tools/cancel_appointment`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${BRIDGE_API_KEY}`
          },
          body: JSON.stringify(args)
        });
        
        const result = await response.json();
        
        if (result.success) {
          app.log.info('✅ Appointment cancelled');
          return {
            content: [
              {
                type: 'text',
                text: `✅ Appointment Cancelled Successfully!\n\n` +
                      `👤 Lead ID: ${args.lead_id}\n` +
                      `📅 Original Time: ${result.cancelled_appointment?.scheduled_for ? new Date(result.cancelled_appointment.scheduled_for).toLocaleString() : 'N/A'}\n` +
                      `🏢 Broker: ${result.cancelled_appointment?.broker_name || 'N/A'}\n` +
                      `💬 ${result.message}`
              }
            ]
          };
        } else {
          throw new Error(result.error || 'Appointment cancellation failed');
        }
      } catch (error) {
        app.log.error({ error }, '❌ Appointment cancellation error');
        return {
          content: [
            {
              type: 'text',
              text: `❌ Appointment cancellation failed: ${error.message}`
            }
          ],
          isError: true
        };
      }
    }
    
    case 'reschedule_appointment': {
      app.log.info({ lead_id: args.lead_id, new_time: args.new_scheduled_for }, '📅 Rescheduling appointment');
      
      try {
        const response = await fetch(`${BRIDGE_URL}/api/tools/reschedule_appointment`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${BRIDGE_API_KEY}`
          },
          body: JSON.stringify(args)
        });
        
        const result = await response.json();
        
        if (result.success) {
          app.log.info('✅ Appointment rescheduled');
          return {
            content: [
              {
                type: 'text',
                text: `✅ Appointment Rescheduled Successfully!\n\n` +
                      `👤 Lead ID: ${args.lead_id}\n` +
                      `📅 Old Time: ${result.old_scheduled_for ? new Date(result.old_scheduled_for).toLocaleString() : 'N/A'}\n` +
                      `📅 New Time: ${new Date(args.new_scheduled_for).toLocaleString()}\n` +
                      `📧 Calendar invite sent: ${result.calendar_invite_sent ? 'Yes' : 'No (email missing)'}\n` +
                      `💬 ${result.message}`
              }
            ]
          };
        } else {
          throw new Error(result.error || 'Appointment rescheduling failed');
        }
      } catch (error) {
        app.log.error({ error }, '❌ Appointment rescheduling error');
        return {
          content: [
            {
              type: 'text',
              text: `❌ Appointment rescheduling failed: ${error.message}`
            }
          ],
          isError: true
        };
      }
    }
    
    case 'update_lead_info': {
      app.log.info({ lead_id: args.lead_id, updates: Object.keys(args).filter(k => k !== 'lead_id') }, '📝 Updating lead info');
      
      try {
        const response = await fetch(`${BRIDGE_URL}/api/tools/update_lead_info`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${BRIDGE_API_KEY}`
          },
          body: JSON.stringify(args)
        });
        
        const result = await response.json();
        
        if (result.success) {
          app.log.info('✅ Lead info updated');
          const updates = Object.keys(args).filter(k => k !== 'lead_id');
          return {
            content: [
              {
                type: 'text',
                text: `✅ Lead Info Updated Successfully!\n\n` +
                      `👤 Lead ID: ${args.lead_id}\n` +
                      `📝 Updated fields: ${updates.join(', ')}`
              }
            ]
          };
        } else {
          throw new Error(result.error || 'Lead info update failed');
        }
      } catch (error) {
        app.log.error({ error }, '❌ Lead info update error');
        return {
          content: [
            {
              type: 'text',
              text: `❌ Lead info update failed: ${error.message}`
            }
          ],
          isError: true
        };
      }
    }
    
    case 'create_outbound_call': {
      app.log.info({ 
        to_phone: args.to_phone, 
        lead_id: args.lead_id,
        from_phone: args.from_phone || SIGNALWIRE_PHONE_NUMBER,
        space_url: SIGNALWIRE_SPACE_URL,
        agent_url: BARBARA_AGENT_URL
      }, '📞 Creating outbound call via SignalWire REST API');
      
      if (!SIGNALWIRE_FEATURES_ENABLED) {
        app.log.error({
          project_id: !!SIGNALWIRE_PROJECT_ID,
          api_token: !!SIGNALWIRE_API_TOKEN,
          space_url: !!SIGNALWIRE_SPACE_URL,
          phone_number: !!SIGNALWIRE_PHONE_NUMBER
        }, '❌ SignalWire credentials missing');
        return {
          content: [
            {
              type: 'text',
              text: `❌ Outbound call failed: SignalWire credentials not configured.\n\n` +
                    `Required env vars: SIGNALWIRE_PROJECT_ID, SIGNALWIRE_API_TOKEN, SIGNALWIRE_SPACE_URL, SIGNALWIRE_PHONE_NUMBER`
            }
          ],
          isError: true
        };
      }
      
      try {
        const auth = Buffer.from(`${SIGNALWIRE_PROJECT_ID}:${SIGNALWIRE_API_TOKEN}`).toString('base64');
        
        // Build the agent URL with lead context
        // This URL must serve SWML (not LaML)
        const agentUrl = new URL(BARBARA_AGENT_URL);
        agentUrl.searchParams.set('lead_id', args.lead_id);
        if (args.broker_id) {
          agentUrl.searchParams.set('broker_id', args.broker_id);
        }
        agentUrl.searchParams.set('direction', 'outbound');
        
        app.log.info({ swml_url: agentUrl.toString() }, '📍 SWML URL for outbound call');
        
        // Normalize phone number to E.164 format
        let toPhone = args.to_phone;
        if (toPhone && !toPhone.startsWith('+')) {
          // Remove any non-digit characters
          const digits = toPhone.replace(/\D/g, '');
          // If 10 digits, assume US and add +1
          if (digits.length === 10) {
            toPhone = `+1${digits}`;
          } else if (digits.length === 11 && digits.startsWith('1')) {
            toPhone = `+${digits}`;
          } else {
            toPhone = `+${digits}`;
          }
        }
        
        app.log.info({ normalized_phone: toPhone }, '📱 Normalized phone number');
        
        // Use SignalWire REST API (LaML compatible) - more universally available
        // POST /api/laml/2010-04-01/Accounts/{ProjectID}/Calls.json
        const apiUrl = `${SIGNALWIRE_SPACE_URL}/api/laml/2010-04-01/Accounts/${SIGNALWIRE_PROJECT_ID}/Calls.json`;
        
        app.log.info({ api_url: apiUrl }, '🔗 SignalWire REST API URL');
        
        // Build form data for REST API (LaML uses form encoding, not JSON)
        const formData = new URLSearchParams();
        formData.append('To', toPhone);
        formData.append('From', args.from_phone || SIGNALWIRE_PHONE_NUMBER);
        // Use Url parameter with SWML endpoint - SignalWire will fetch SWML from this URL
        formData.append('Url', agentUrl.toString());
        // Tell SignalWire the URL returns SWML, not LaML/TwiML
        formData.append('MachineDetection', 'Enable');
        formData.append('MachineDetectionTimeout', '5');
        
        app.log.info({ 
          form_data: {
            To: toPhone,
            From: args.from_phone || SIGNALWIRE_PHONE_NUMBER,
            Url: agentUrl.toString()
          }
        }, '📋 Request form data');
        
        const response = await fetch(apiUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': `Basic ${auth}`
          },
          body: formData.toString()
        });
        
        const responseText = await response.text();
        app.log.info({ 
          status: response.status, 
          statusText: response.statusText,
          response_text: responseText.substring(0, 500) 
        }, '📞 SignalWire REST API response');
        
        let result;
        try {
          result = JSON.parse(responseText);
        } catch (e) {
          app.log.error({ responseText }, '❌ Failed to parse SignalWire response as JSON');
          throw new Error(`SignalWire returned invalid JSON (${response.status}): ${responseText.substring(0, 200)}`);
        }
        
        if (!response.ok) {
          app.log.error({ result, status: response.status }, '❌ SignalWire API error');
          throw new Error(result.message || result.error_message || result.code || `Call creation failed (${response.status})`);
        }
        
        // REST API returns 'sid' for call ID
        const callId = result.sid || result.call_sid || result.id;
        
        app.log.info({ call_id: callId, result }, '✅ Outbound call created successfully');
        
        return {
          content: [
            {
              type: 'text',
              text: `✅ Outbound Call Initiated!\n\n` +
                    `📞 Call SID: ${callId || 'pending'}\n` +
                    `📱 From: ${args.from_phone || SIGNALWIRE_PHONE_NUMBER}\n` +
                    `📱 To: ${toPhone}\n` +
                    `👤 Lead ID: ${args.lead_id}\n` +
                    `🤖 Agent: Barbara (SignalWire AI SDK)\n` +
                    `🔗 SWML URL: ${agentUrl.toString()}\n` +
                    `💬 Status: ${result.status || 'queued'}`
            }
          ]
        };
        
      } catch (error) {
        app.log.error({ 
          error: error.message,
          stack: error.stack,
          to_phone: args.to_phone,
          lead_id: args.lead_id
        }, '❌ Outbound call failed');
        return {
          content: [
            {
              type: 'text',
              text: `❌ Outbound call failed: ${error.message}`
            }
          ],
          isError: true
        };
      }
    }
    
    default:
      throw new Error(`Unknown tool: ${name}`);
  }
}

// Health check endpoint
app.get('/health', async (request, reply) => {
  return { 
    status: 'healthy', 
    timestamp: new Date().toISOString(),
    signalwire_configured: SIGNALWIRE_FEATURES_ENABLED,
    bridge_url: BRIDGE_URL
  };
});

// MCP endpoint for n8n
app.post('/mcp', async (request, reply) => {
  const { id = null, jsonrpc = '2.0', method, params = {} } = request.body || {};

  app.log.info({ method, params, id }, '🔧 MCP request received');

  const respond = (payload) => {
    return reply.send({ jsonrpc: '2.0', id, ...payload });
  };

  try {
    switch (method) {
      case 'initialize': {
        return respond({
          result: {
            protocolVersion: '2025-03-26',
            capabilities: {
              tools: {
                list: true,
                call: true
              }
            },
            serverInfo: {
              name: 'barbara-mcp',
              version: '2.0.0'
            }
          }
        });
      }

      case 'tools/list': {
        return respond({
          result: {
            tools: tools.map(tool => ({
              name: tool.name,
              description: tool.description,
              inputSchema: tool.inputSchema
            }))
          }
        });
      }

      case 'tools/call': {
        const { name, arguments: args } = params;
        if (!name) {
          return respond({
            error: {
              code: -32602,
              message: 'Missing tool name in request'
            }
          });
        }

        const toolResult = await executeTool(name, args || {});
        return respond({ result: toolResult });
      }

      default:
        return respond({
          error: {
            code: -32601,
            message: `Unknown method: ${method}`
          }
        });
    }
  } catch (error) {
    app.log.error({ error }, '❌ MCP request error');
    return respond({
      error: {
        code: -32000,
        message: error.message || 'Internal MCP error'
      }
    });
  }
});

// Start server
const port = process.env.PORT || 3000;
const host = process.env.HOST || '0.0.0.0';

app.listen({ port, host }, (err, address) => {
  if (err) {
    app.log.error(err);
    process.exit(1);
  }
  app.log.info(`🚀 Barbara MCP Server v2.0 running on ${address}`);
  app.log.info(`📡 Bridge URL: ${BRIDGE_URL}`);
  app.log.info(`🤖 Barbara Agent URL: ${BARBARA_AGENT_URL}`);
  app.log.info(`📞 SignalWire: ${SIGNALWIRE_FEATURES_ENABLED ? 'Configured ✅' : 'Not configured ⚠️'}`);
  app.log.info(`🔧 MCP endpoint: ${address}/mcp`);
});

// Graceful shutdown
process.on('SIGTERM', async () => {
  app.log.info('🛑 Shutting down gracefully...');
  await app.close();
  process.exit(0);
});

process.on('SIGINT', async () => {
  app.log.info('🛑 Shutting down gracefully...');
  await app.close();
  process.exit(0);
});
