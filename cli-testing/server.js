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

// SignalWire Fabric WebRTC config (for browser-based test calls)
const SIGNALWIRE_ALLOWED_ADDRESSES = process.env.SIGNALWIRE_ALLOWED_ADDRESSES || '';
const SIGNALWIRE_GUEST_TOKEN_PATH = process.env.SIGNALWIRE_GUEST_TOKEN_PATH || '/api/fabric/guests/tokens';

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
 * Health Check Endpoint
 */
app.get('/healthz', async (request, reply) => {
  return reply.code(200).send({
    status: 'ok',
    service: 'barbara-cli-testing',
    timestamp: new Date().toISOString(),
    webrtc_enabled: Boolean(SIGNALWIRE_ALLOWED_ADDRESSES)
  });
});

/**
 * SignalWire Fabric Guest Token API
 * Generate a short-lived token for browser-based WebRTC test calls
 * POST /api/test-call/token
 * 
 * Returns: { token, expires_at }
 */
app.post('/api/test-call/token', async (request, reply) => {
  // Check SignalWire credentials
  if (!SIGNALWIRE_PROJECT_ID || !SIGNALWIRE_API_TOKEN || !SIGNALWIRE_SPACE_URL) {
    return reply.code(500).send({
      error: 'SignalWire credentials not configured'
    });
  }

  const parsedAllowedAddresses = SIGNALWIRE_ALLOWED_ADDRESSES
    .split(',')
    .map(addr => addr.trim())
    .filter(Boolean);

  if (!parsedAllowedAddresses.length) {
    return reply.code(500).send({
      error: 'SIGNALWIRE_ALLOWED_ADDRESSES not configured. Set to comma-separated SIP addresses (e.g., "sip:barbara@example.sip.signalwire.com")'
    });
  }

  const expiresAt = new Date(Date.now() + 60 * 60 * 1000).toISOString(); // 1 hour
  const payload = {
    allowed_addresses: parsedAllowedAddresses,
    ttl: 3600,
    expires_at: expiresAt,
    state: {
      type: 'barbara-web-test'
    }
  };

  try {
    const auth = Buffer.from(`${SIGNALWIRE_PROJECT_ID}:${SIGNALWIRE_API_TOKEN}`).toString('base64');
    const tokenUrl = new URL(SIGNALWIRE_GUEST_TOKEN_PATH, SIGNALWIRE_SPACE_URL).toString();

    app.log.info({ tokenUrl }, '[test-call/token] Requesting guest token from SignalWire Fabric');

    const response = await fetch(tokenUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Basic ${auth}`
      },
      body: JSON.stringify(payload)
    });

    const data = await response.json().catch(() => ({}));

    if (!response.ok) {
      app.log.error({ status: response.status, data }, '[test-call/token] Failed to generate guest token');
      return reply.code(500).send({
        error: data.message || 'Failed to generate guest token'
      });
    }

    const token = data.token || data.jwt_token || data.jwt || data.access_token;

    if (!token) {
      app.log.error({ data }, '[test-call/token] Response missing token property');
      return reply.code(500).send({
        error: 'Guest token response missing token'
      });
    }

    app.log.info('[test-call/token] ✅ Guest token generated for browser WebRTC');
    return reply.send({ token, expires_at: expiresAt });

  } catch (err) {
    app.log.error({ err }, '[test-call/token] Error generating guest token');
    return reply.code(500).send({
      error: 'Failed to generate guest token: ' + err.message
    });
  }
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
    
    app.log.info({ 
      to_phone, 
      lead_id,
      from_phone: from_phone || SIGNALWIRE_PHONE_NUMBER
    }, '[trigger-call] Creating outbound call via SignalWire');
    
    const auth = Buffer.from(`${SIGNALWIRE_PROJECT_ID}:${SIGNALWIRE_API_TOKEN}`).toString('base64');
    
    const response = await fetch(`${SIGNALWIRE_SPACE_URL}/api/laml/2010-04-01/Accounts/${SIGNALWIRE_PROJECT_ID}/Calls.json`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': `Basic ${auth}`
      },
      body: new URLSearchParams({
        To: to_phone,
        From: from_phone || SIGNALWIRE_PHONE_NUMBER,
        Url: SWAIG_AGENT_URL,
        Method: 'POST'
      })
    });
    
    const result = await response.json();
    
    if (!result.sid) {
      app.log.error({ result }, '[trigger-call] SignalWire call creation failed');
      return reply.code(500).send({
        success: false,
        error: result.message || result.error || 'SignalWire call creation failed'
      });
    }
    
    app.log.info({ 
      call_sid: result.sid
    }, '[trigger-call] Call created');
    
    return reply.code(200).send({
      success: true,
      call_id: result.sid,
      message: 'Outbound call initiated via SignalWire'
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
    
    console.log('\n🧪 Barbara CLI Testing Service Started');
    console.log(`   Environment: ${NODE_ENV}`);
    console.log(`   Health: http://localhost:${PORT}/healthz`);
    console.log(`   Test CLI: POST http://localhost:${PORT}/api/test-cli`);
    console.log(`   WebRTC Token: POST http://localhost:${PORT}/api/test-call/token`);
    console.log(`   Trigger Call: POST http://localhost:${PORT}/trigger-call`);
    console.log(`   WebRTC: ${SIGNALWIRE_ALLOWED_ADDRESSES ? '✅ Configured' : '⚠️ SIGNALWIRE_ALLOWED_ADDRESSES not set'}\n`);
    
  } catch (err) {
    app.log.error(err);
    process.exit(1);
  }
}

start();

