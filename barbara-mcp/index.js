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

// Supabase config for looking up broker phone numbers
const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_ANON_KEY = process.env.SUPABASE_ANON_KEY;

/**
 * Get the broker's SignalWire phone number for outbound calls
 * Looks up: lead_id -> assigned_broker_id -> phone_numbers.assigned_broker_id
 * Returns the first active phone number for the broker, or null if not found
 */
async function getBrokerPhoneNumber(leadId, brokerId = null) {
  app.log.info({ lead_id: leadId, broker_id: brokerId, supabase_configured: !!(SUPABASE_URL && SUPABASE_ANON_KEY) }, '🔍 Starting broker phone lookup');
  
  if (!SUPABASE_URL || !SUPABASE_ANON_KEY) {
    app.log.warn('⚠️ Supabase not configured - cannot look up broker phone');
    return null;
  }

  try {
    let brokerIdToUse = brokerId;

    // If no broker_id provided, look it up from the lead
    if (!brokerIdToUse && leadId) {
      const leadUrl = `${SUPABASE_URL}/rest/v1/leads?id=eq.${leadId}&select=assigned_broker_id`;
      app.log.info({ url: leadUrl }, '🔍 Fetching lead to get broker_id');
      
      const leadResponse = await fetch(leadUrl, {
        headers: {
          'apikey': SUPABASE_ANON_KEY,
          'Authorization': `Bearer ${SUPABASE_ANON_KEY}`
        }
      });
      
      const leadResponseText = await leadResponse.text();
      app.log.info({ status: leadResponse.status, body: leadResponseText.substring(0, 500) }, '📋 Lead query response');
      
      let leads;
      try {
        leads = JSON.parse(leadResponseText);
      } catch (parseError) {
        app.log.error({ error: parseError.message, body: leadResponseText }, '❌ Failed to parse lead response');
        return null;
      }
      
      if (leads.length > 0 && leads[0].assigned_broker_id) {
        brokerIdToUse = leads[0].assigned_broker_id;
        app.log.info({ lead_id: leadId, broker_id: brokerIdToUse }, '📍 Found broker for lead');
      } else {
        app.log.warn({ lead_id: leadId, leads_count: leads.length }, '⚠️ Lead found but no assigned_broker_id');
      }
    }

    if (!brokerIdToUse) {
      app.log.warn({ lead_id: leadId }, '⚠️ No broker_id found for lead');
      return null;
    }

    // Look up the broker's phone numbers
    const phoneUrl = `${SUPABASE_URL}/rest/v1/phone_numbers?assigned_broker_id=eq.${brokerIdToUse}&is_active=eq.true&select=phone_number,label&order=label.asc&limit=1`;
    app.log.info({ url: phoneUrl }, '🔍 Fetching broker phone number');
    
    const phoneResponse = await fetch(phoneUrl, {
      headers: {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': `Bearer ${SUPABASE_ANON_KEY}`
      }
    });
    
    const phoneResponseText = await phoneResponse.text();
    app.log.info({ status: phoneResponse.status, body: phoneResponseText.substring(0, 500) }, '📋 Phone query response');
    
    let phones;
    try {
      phones = JSON.parse(phoneResponseText);
    } catch (parseError) {
      app.log.error({ error: parseError.message, body: phoneResponseText }, '❌ Failed to parse phone response');
      return null;
    }
    
    if (phones.length > 0) {
      app.log.info({ broker_id: brokerIdToUse, phone: phones[0].phone_number, label: phones[0].label }, '📞 Found broker SignalWire number');
      return phones[0].phone_number;
    }

    app.log.warn({ broker_id: brokerIdToUse, phones_count: phones.length }, '⚠️ No phone numbers found for broker');
    return null;
  } catch (error) {
    app.log.error({ error: error.message, stack: error.stack }, '❌ Error looking up broker phone');
    return null;
  }
}

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
      // =======================================================================
      // PRE-WARMED OUTBOUND CALLS
      // =======================================================================
      // Instead of calling SignalWire directly, we call Barbara's /api/outbound
      // endpoint which:
      // 1. Pre-loads ALL data (lead, broker, models, availability)
      // 2. Caches it with a session_id  
      // 3. Triggers SignalWire with session_id in URL
      // 4. When SignalWire requests SWML, Barbara responds INSTANTLY (cached!)
      //
      // This eliminates the 2-3 second delay where users say "hello? hello?"
      // =======================================================================
      
      app.log.info({ 
        lead_id: args.lead_id,
        to_phone: args.to_phone,
        from_phone: args.from_phone
      }, '📞 Creating outbound call via Barbara /api/outbound (pre-warmed)');
      
      if (!BARBARA_AGENT_URL) {
        return {
          content: [
            {
              type: 'text',
              text: `❌ Outbound call failed: BARBARA_AGENT_URL not configured`
            }
          ],
          isError: true
        };
      }
      
      try {
        // Build the Barbara /api/outbound URL
        // Strip auth from URL for API endpoint (it uses API key auth)
        let barbaraBaseUrl = BARBARA_AGENT_URL.replace(/\/agent\/barbara.*$/, '');
        // Remove basic auth credentials if present in URL
        barbaraBaseUrl = barbaraBaseUrl.replace(/\/\/[^:]+:[^@]+@/, '//');
        const outboundUrl = `${barbaraBaseUrl}/api/outbound`;
        
        app.log.info({ outbound_url: outboundUrl }, '🔗 Barbara /api/outbound URL');
        
        // Build request payload - Barbara will handle everything else
        const payload = {
          lead_id: args.lead_id
        };
        
        // Optional overrides
        if (args.to_phone) {
          payload.to_phone = args.to_phone;
        }
        if (args.from_phone) {
          payload.from_phone = args.from_phone;
        }
        
        app.log.info({ payload }, '📋 Request payload');
        
        const response = await fetch(outboundUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
            // Note: API key auth can be added here if needed
          },
          body: JSON.stringify(payload)
        });
        
        const responseText = await response.text();
        app.log.info({ 
          status: response.status, 
          response_preview: responseText.substring(0, 500) 
        }, '📞 Barbara /api/outbound response');
        
        let result;
        try {
          result = JSON.parse(responseText);
        } catch (e) {
          app.log.error({ responseText }, '❌ Failed to parse Barbara response as JSON');
          throw new Error(`Barbara returned invalid JSON (${response.status}): ${responseText.substring(0, 200)}`);
        }
        
        if (!response.ok || !result.success) {
          app.log.error({ result, status: response.status }, '❌ Barbara /api/outbound error');
          throw new Error(result.error || result.message || `Call creation failed (${response.status})`);
        }
        
        app.log.info({ 
          call_id: result.call_id,
          session_id: result.session_id,
          from: result.from_phone,
          to: result.to_phone
        }, '✅ Outbound call initiated via Barbara (pre-warmed!)');
        
        return {
          content: [
            {
              type: 'text',
              text: `✅ Outbound Call Initiated (Pre-Warmed)!\n\n` +
                    `📞 Call ID: ${result.call_id || 'pending'}\n` +
                    `🔑 Session: ${result.session_id}\n` +
                    `📱 From: ${result.from_phone}\n` +
                    `📱 To: ${result.to_phone}\n` +
                    `👤 Lead: ${result.lead_name || args.lead_id}\n` +
                    `👔 Broker: ${result.broker_name || 'N/A'}\n` +
                    `⚡ Status: Data pre-loaded - instant response when answered!`
            }
          ]
        };
        
      } catch (error) {
        app.log.error({ 
          error: error.message,
          stack: error.stack,
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
