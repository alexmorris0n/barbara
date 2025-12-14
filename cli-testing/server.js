/**
 * Barbara CLI Testing Service
 * 
 * Provides HTTP API for:
 * - Testing prompt nodes via swaig-test CLI
 * - Triggering outbound test calls via SignalWire
 */

require('dotenv').config();
const Fastify = require('fastify');
const { executeCliTest } = require('./test-cli');

// Configuration
const PORT = process.env.PORT || 8080;
const NODE_ENV = process.env.NODE_ENV || 'development';

// SignalWire outbound call config
const SIGNALWIRE_SPACE_URL = process.env.SIGNALWIRE_SPACE_URL;
const SIGNALWIRE_PROJECT_ID = process.env.SIGNALWIRE_PROJECT_ID;
const SIGNALWIRE_API_TOKEN = process.env.SIGNALWIRE_API_TOKEN;
const SIGNALWIRE_PHONE_NUMBER = process.env.SIGNALWIRE_PHONE_NUMBER;
const SWAIG_AGENT_URL = process.env.SWAIG_AGENT_URL || 'https://barbara-agent.fly.dev/agent/barbara';

// In-memory cache to prevent duplicate calls (cleared after 5 minutes)
const recentCalls = new Map();
const DUPLICATE_CALL_WINDOW_MS = 5 * 60 * 1000; // 5 minutes

// Supabase config for broker phone lookup
const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_ANON_KEY = process.env.SUPABASE_ANON_KEY;

// Initialize Fastify
const app = Fastify({
  logger: {
    level: NODE_ENV === 'development' ? 'info' : 'warn',
    transport: NODE_ENV === 'development' ? {
      target: 'pino-pretty',
      options: { colorize: true }
    } : undefined
  }
});

// Register CORS plugin for Portal UI
app.register(require('@fastify/cors'), {
  origin: (origin, cb) => {
    // Allow requests with no origin (mobile apps, curl, etc)
    if (!origin) return cb(null, true);
    
    // Allow localhost for development
    if (origin.includes('localhost') || origin.includes('127.0.0.1')) {
      return cb(null, true);
    }
    
    // Allow all Vercel deployments
    if (origin.includes('.vercel.app')) {
      return cb(null, true);
    }
    
    // Allow specific production domains
    const allowedOrigins = [
      process.env.PORTAL_URL,
      'https://app.barbarapro.com',
      'https://barbara-portal.vercel.app'
    ].filter(Boolean);
    
    if (allowedOrigins.includes(origin)) {
      return cb(null, true);
    }
    
    // Log blocked origins for debugging
    console.log(`CORS blocked origin: ${origin}`);
    cb(null, false);
  },
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
});

/**
 * Normalize phone number to E.164 format: +1XXXXXXXXXX
 * Handles: +16505300051, 16505300051, 6505300051, (650) 530-0051
 * Returns null if invalid
 */
function normalizePhoneNumber(phone) {
  if (!phone || typeof phone !== 'string') {
    return null;
  }
  
  // Remove all non-digit characters
  const digits = phone.replace(/\D/g, '');
  
  // If 11 digits starting with 1, strip the country code
  let normalized = digits;
  if (digits.length === 11 && digits.startsWith('1')) {
    normalized = digits.substring(1);
  }
  
  // Must be exactly 10 digits for US numbers
  if (normalized.length !== 10) {
    return null;
  }
  
  // Return E.164 format with +1 prefix
  return `+1${normalized}`;
}

/**
 * Check if a call was recently made to prevent duplicates
 */
function isDuplicateCall(toPhone, fromPhone) {
  const key = `${toPhone}:${fromPhone}`;
  const lastCallTime = recentCalls.get(key);
  
  if (lastCallTime && (Date.now() - lastCallTime) < DUPLICATE_CALL_WINDOW_MS) {
    return true;
  }
  
  // Record this call
  recentCalls.set(key, Date.now());
  
  // Clean up old entries periodically
  if (recentCalls.size > 1000) {
    const now = Date.now();
    for (const [k, v] of recentCalls.entries()) {
      if (now - v > DUPLICATE_CALL_WINDOW_MS) {
        recentCalls.delete(k);
      }
    }
  }
  
  return false;
}

/**
 * Look up broker's assigned phone number from Supabase
 * Matches MCP behavior - uses broker's phone instead of default
 */
async function getBrokerPhoneNumber(leadId, brokerId = null) {
  if (!SUPABASE_URL || !SUPABASE_ANON_KEY) {
    app.log.warn('⚠️ Supabase not configured - using default phone');
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
      
      if (!leadResponse.ok) {
        app.log.warn({ status: leadResponse.status }, '⚠️ Lead lookup failed');
        return null;
      }
      
      const leads = await leadResponse.json();
      if (leads.length > 0 && leads[0].assigned_broker_id) {
        brokerIdToUse = leads[0].assigned_broker_id;
        app.log.info({ lead_id: leadId, broker_id: brokerIdToUse }, '📍 Found broker for lead');
      } else {
        app.log.warn({ lead_id: leadId }, '⚠️ Lead found but no assigned_broker_id');
      }
    }

    if (!brokerIdToUse) {
      app.log.warn({ lead_id: leadId }, '⚠️ No broker_id found for lead');
      return null;
    }

    // Look up the broker's phone number
    const phoneUrl = `${SUPABASE_URL}/rest/v1/phone_numbers?assigned_broker_id=eq.${brokerIdToUse}&is_active=eq.true&select=phone_number,label&order=label.asc&limit=1`;
    app.log.info({ url: phoneUrl }, '🔍 Fetching broker phone number');
    
    const phoneResponse = await fetch(phoneUrl, {
      headers: {
        'apikey': SUPABASE_ANON_KEY,
        'Authorization': `Bearer ${SUPABASE_ANON_KEY}`
      }
    });
    
    if (!phoneResponse.ok) {
      app.log.warn({ status: phoneResponse.status }, '⚠️ Phone lookup failed');
      return null;
    }
    
    const phones = await phoneResponse.json();
    if (phones.length > 0) {
      const brokerPhone = phones[0].phone_number;
      // Normalize the broker phone number to E.164 format
      const normalizedBrokerPhone = normalizePhoneNumber(brokerPhone);
      if (normalizedBrokerPhone) {
        app.log.info({ broker_id: brokerIdToUse, phone: normalizedBrokerPhone, label: phones[0].label }, '✅ Found broker phone');
        return normalizedBrokerPhone;
      } else {
        app.log.warn({ broker_id: brokerIdToUse, phone: brokerPhone }, '⚠️ Broker phone number is invalid format');
        return null;
      }
    }
    
    app.log.warn({ broker_id: brokerIdToUse }, '⚠️ No phone number found for broker');
    return null;
    
  } catch (err) {
    app.log.error({ err: err.message }, '❌ Error looking up broker phone');
    return null;
  }
}

/**
 * Health Check Endpoint
 */
app.get('/healthz', async (request, reply) => {
  return reply.code(200).send({
    status: 'ok',
    service: 'barbara-cli-testing',
    timestamp: new Date().toISOString()
  });
});

/**
 * Test CLI API
 * Execute swaig-test for prompt node testing from Portal UI
 * POST /api/test-cli
 * 
 * Body: { versionId?, vertical, nodeName, promptContent? }
 * Returns: { success, output, stderr, exitCode, duration }
 */
app.post('/api/test-cli', async (request, reply) => {
  try {
    const { versionId, vertical, nodeName, promptContent } = request.body || {};
    
    if (!vertical || !nodeName) {
      return reply.code(400).send({
        success: false,
        error: 'Missing required fields: vertical, nodeName'
      });
    }

    if (!versionId && !promptContent) {
      return reply.code(400).send({
        success: false,
        error: 'Provide either versionId or promptContent for validation'
      });
    }
    
    app.log.info({ 
      versionId: versionId || 'inline',
      vertical, 
      nodeName,
      hasPromptOverride: Boolean(promptContent)
    }, '[test-cli] Received test request');
    
    // Execute test (this may take 10-45 seconds)
    const result = await executeCliTest({ 
      versionId: versionId || null, 
      vertical, 
      nodeName,
      promptContent: promptContent || null
    });
    
    const guardrailError = mapGuardrailError(result);
    if (guardrailError) {
      app.log.warn({ guardrailError }, '[test-cli] Guardrail validation failure');
      return reply.code(422).send(guardrailError);
    }
    
    app.log.info({ 
      success: result.success,
      exitCode: result.exitCode,
      duration: result.duration
    }, '[test-cli] Test completed');
    
    return reply.code(result.success ? 200 : 500).send(result);
    
  } catch (err) {
    app.log.error({ err }, '[test-cli] Error executing test');
    return reply.code(500).send({
      success: false,
      error: err.message,
      stderr: err.stderr || ''
    });
  }
});

/**
 * Trigger Outbound Call API
 * Triggers an outbound call to a lead via SignalWire
 * POST /trigger-call
 * 
 * Body: { to_phone, lead_id?, from_phone? }
 * Returns: { success, call_id, message }
 */
app.post('/trigger-call', async (request, reply) => {
  try {
    const { to_phone, lead_id, from_phone } = request.body || {};
    
    if (!to_phone) {
      return reply.code(400).send({
        success: false,
        error: 'Missing required field: to_phone'
      });
    }
    
    // Check SignalWire credentials
    if (!SIGNALWIRE_PROJECT_ID || !SIGNALWIRE_API_TOKEN || !SIGNALWIRE_SPACE_URL) {
      return reply.code(500).send({
        success: false,
        error: 'SignalWire credentials not configured. Set SIGNALWIRE_PROJECT_ID, SIGNALWIRE_API_TOKEN, SIGNALWIRE_SPACE_URL'
      });
    }
    
    // Normalize and validate phone numbers
    const normalizedTo = normalizePhoneNumber(to_phone);
    if (!normalizedTo) {
      return reply.code(400).send({
        success: false,
        error: `Invalid phone number format: ${to_phone}. Must be E.164 format (+1XXXXXXXXXX) or 10-digit US number.`
      });
    }
    
    // Build agent URL with lead_id if provided
    let agentUrl = SWAIG_AGENT_URL;
    if (lead_id) {
      const url = new URL(SWAIG_AGENT_URL);
      url.searchParams.set('lead_id', lead_id);
      url.searchParams.set('direction', 'outbound');
      agentUrl = url.toString();
    }
    
    // Look up broker's assigned phone number (matches MCP behavior)
    let fromPhone = from_phone;
    if (!fromPhone && lead_id) {
      const brokerPhone = await getBrokerPhoneNumber(lead_id);
      if (brokerPhone) {
        fromPhone = brokerPhone;
        app.log.info({ broker_phone: brokerPhone }, '[trigger-call] Using broker assigned phone');
      }
    }
    fromPhone = fromPhone || SIGNALWIRE_PHONE_NUMBER;
    
    // Normalize from phone number
    const normalizedFrom = normalizePhoneNumber(fromPhone);
    if (!normalizedFrom) {
      return reply.code(400).send({
        success: false,
        error: `Invalid from phone number format: ${fromPhone}. Must be E.164 format (+1XXXXXXXXXX) or 10-digit US number.`
      });
    }
    
    // Check for duplicate calls
    if (isDuplicateCall(normalizedTo, normalizedFrom)) {
      app.log.warn({ 
        to: normalizedTo, 
        from: normalizedFrom 
      }, '[trigger-call] Duplicate call prevented');
      return reply.code(429).send({
        success: false,
        error: 'Duplicate call prevented. Please wait before calling again.'
      });
    }
    
    app.log.info({ 
      to_phone: normalizedTo, 
      lead_id,
      from_phone: normalizedFrom,
      using_broker_phone: normalizedFrom !== normalizePhoneNumber(SIGNALWIRE_PHONE_NUMBER),
      agent_url: agentUrl.replace(/:[^:@]+@/, ':***@')  // mask password in logs
    }, '[trigger-call] Creating outbound call via SignalWire Relay REST API');
    
    const auth = Buffer.from(`${SIGNALWIRE_PROJECT_ID}:${SIGNALWIRE_API_TOKEN}`).toString('base64');
    
    // Use Relay REST API for outbound calls with SWML script URL
    // This is the correct endpoint for outbound calls with AI agents
    const response = await fetch(`${SIGNALWIRE_SPACE_URL}/api/relay/rest/calls`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': `Basic ${auth}`
      },
      body: JSON.stringify({
        to: normalizedTo,
        from: normalizedFrom,
        url: agentUrl,
        timeout: 30  // Reduced timeout to prevent long ring times
      })
    });
    
    const responseText = await response.text();
    let result;
    try {
      result = JSON.parse(responseText);
    } catch (e) {
      app.log.error({ responseText }, '[trigger-call] Failed to parse response');
      return reply.code(500).send({
        success: false,
        error: `Invalid response from SignalWire: ${responseText}`
      });
    }
    
    if (!response.ok) {
      app.log.error({ 
        result, 
        status: response.status,
        to: normalizedTo,
        from: normalizedFrom
      }, '[trigger-call] SignalWire call creation failed');
      
      // Provide helpful error message
      let errorMsg = result.message || result.error || `SignalWire API error (${response.status})`;
      if (response.status === 404) {
        errorMsg += '. The API endpoint may be incorrect. Verify the SignalWire API endpoint for outbound calls.';
      } else if (response.status === 400) {
        errorMsg += '. Check that phone numbers are in E.164 format and the URL is accessible.';
      }
      
      return reply.code(500).send({
        success: false,
        error: errorMsg,
        details: result
      });
    }
    
    const callId = result.id || result.call_id || result.sid || result.call_sid;
    if (!callId) {
      app.log.warn({ result }, '[trigger-call] No call ID in response');
    }
    
    app.log.info({ call_id: callId, to: normalizedTo, from: normalizedFrom }, '[trigger-call] Call created successfully');
    
    return reply.code(200).send({
      success: true,
      call_id: callId,
      to: normalizedTo,
      from: normalizedFrom,
      message: 'Outbound call initiated via SignalWire Relay REST API'
    });
    
  } catch (err) {
    app.log.error({ err }, '[trigger-call] Error triggering call');
    return reply.code(500).send({
      success: false,
      error: err.message
    });
  }
});

/**
 * Detect guardrail errors (empty/missing contexts) and map to structured payload.
 */
function mapGuardrailError(result = {}) {
  const combinedOutput = `${result.stderr || ''}\n${result.output || ''}`;
  if (!combinedOutput.includes('Contexts validation failed')) {
    return null;
  }
  
  const regex = /Contexts validation failed\. Missing contexts: (?<missing>.+?) \| Empty contexts: (?<empty>.+)/;
  const match = combinedOutput.match(regex);
  const missingRaw = match?.groups?.missing?.trim() || '[]';
  const emptyRaw = match?.groups?.empty?.trim() || '[]';
  
  const missingContexts = parseContextList(missingRaw);
  const emptyContexts = parseContextList(emptyRaw);
  
  const details = { missingContexts, emptyContexts };
  let errorCode = 'EMPTY_CONTEXT';
  if (missingContexts.length && !emptyContexts.length) {
    errorCode = 'MISSING_CONTEXT';
  } else if (missingContexts.length && emptyContexts.length) {
    errorCode = 'MISSING_AND_EMPTY_CONTEXTS';
  }
  
  const friendlyParts = [];
  if (missingContexts.length) {
    friendlyParts.push(
      `${missingContexts.join(', ')} ${missingContexts.length === 1 ? 'context is missing' : 'contexts are missing'} from Supabase`
    );
  }
  if (emptyContexts.length) {
    friendlyParts.push(
      `${emptyContexts.join(', ')} ${emptyContexts.length === 1 ? 'context has no steps' : 'contexts have no steps'}`
    );
  }
  const friendlyMessage = friendlyParts.length
    ? `Fix prompt content: ${friendlyParts.join('; ')}.`
    : 'Context guardrail blocked this save. Please ensure every node has instructions.';
  
  return {
    success: false,
    errorCode,
    error: friendlyMessage,
    details,
    exitCode: result.exitCode,
    duration: result.duration,
    rawError: combinedOutput
  };
}

function parseContextList(raw) {
  if (!raw || raw === '[]' || raw.toLowerCase() === 'none') {
    return [];
  }
  const normalized = raw.replace(/'/g, '"');
  try {
    const parsed = JSON.parse(normalized);
    return Array.isArray(parsed) ? parsed : [];
  } catch (err) {
    return raw
      .replace(/[\[\]]/g, '')
      .split(',')
      .map((str) => str.trim())
      .filter(Boolean);
  }
}

// Start server
async function start() {
  try {
    await app.listen({ 
      port: PORT, 
      host: '0.0.0.0' 
    });
    
    console.log('\n Barbara CLI Testing Service Started');
    console.log(`   Environment: ${NODE_ENV}`);
    console.log(`   Health: http://localhost:${PORT}/healthz`);
    console.log(`   Test API: POST http://localhost:${PORT}/api/test-cli`);
    console.log(`   Trigger Call: POST http://localhost:${PORT}/trigger-call\n`);
    
  } catch (err) {
    app.log.error(err);
    process.exit(1);
  }
}

start();

