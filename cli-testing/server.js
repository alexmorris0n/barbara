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
// Default to quieter logs in production, but allow override (e.g., set LOG_LEVEL=info on Fly when debugging).
const LOG_LEVEL = process.env.LOG_LEVEL || (NODE_ENV === 'development' ? 'info' : 'warn');

function normalizePhoneE164US(input) {
  if (!input) return '';
  const raw = String(input).trim();
  if (!raw) return '';

  // Keep E.164 if already provided
  if (raw.startsWith('+') && raw.length > 1) {
    return raw;
  }

  // Strip non-digits
  let digits = raw.replace(/\D/g, '');

  // If 11 digits starting with 1, strip leading 1
  if (digits.length === 11 && digits.startsWith('1')) {
    digits = digits.slice(1);
  }

  // If 10-digit NANP, add +1
  if (digits.length === 10) {
    return `+1${digits}`;
  }

  // Fallback: best-effort E.164
  return digits ? `+${digits}` : '';
}

// SignalWire outbound call config
const SIGNALWIRE_SPACE_URL = process.env.SIGNALWIRE_SPACE_URL;
const SIGNALWIRE_PROJECT_ID = process.env.SIGNALWIRE_PROJECT_ID;
const SIGNALWIRE_API_TOKEN = process.env.SIGNALWIRE_API_TOKEN;
const SIGNALWIRE_PHONE_NUMBER = process.env.SIGNALWIRE_PHONE_NUMBER;
const SWAIG_AGENT_URL = process.env.SWAIG_AGENT_URL || 'https://barbara-agent.fly.dev/agent/barbara';

// Initialize Fastify
const app = Fastify({
  logger: {
    level: LOG_LEVEL,
    transport: NODE_ENV === 'development' ? {
      target: 'pino-pretty',
      options: { colorize: true }
    } : undefined
  }
});

// Always surface crash reasons in Fly logs (otherwise restarts look "silent")
process.on('unhandledRejection', (reason) => {
  try {
    app.log.error({ err: reason }, '[process] unhandledRejection');
  } catch (e) {
    // eslint-disable-next-line no-console
    console.error('[process] unhandledRejection', reason);
  }
});

process.on('uncaughtException', (err) => {
  try {
    app.log.fatal({ err }, '[process] uncaughtException - exiting');
  } catch (e) {
    // eslint-disable-next-line no-console
    console.error('[process] uncaughtException', err);
  } finally {
    // Allow logs to flush, then exit so Fly restarts cleanly
    setTimeout(() => process.exit(1), 250);
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

    const normalizedTo = normalizePhoneE164US(to_phone);
    const normalizedFrom = normalizePhoneE164US(from_phone || SIGNALWIRE_PHONE_NUMBER);
    if (!normalizedTo) {
      return reply.code(400).send({
        success: false,
        error: `Invalid to_phone: ${to_phone}`
      });
    }
    if (!normalizedFrom) {
      return reply.code(500).send({
        success: false,
        error: 'Missing/invalid from phone. Set SIGNALWIRE_PHONE_NUMBER or pass from_phone in request body (E.164 preferred).'
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
    
    app.log.info({ 
      to_phone: normalizedTo,
      to_phone_raw: to_phone,
      lead_id,
      from_phone: normalizedFrom,
      from_phone_raw: from_phone || SIGNALWIRE_PHONE_NUMBER,
      agent_url: agentUrl.replace(/:[^:@]+@/, ':***@')  // mask password in logs
    }, '[trigger-call] Creating outbound call via SignalWire Calling API');
    
    const auth = Buffer.from(`${SIGNALWIRE_PROJECT_ID}:${SIGNALWIRE_API_TOKEN}`).toString('base64');
    
    // Use Calling API (SWML-native) instead of LaML API
    const response = await fetch(`${SIGNALWIRE_SPACE_URL}/api/calling/calls`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': `Basic ${auth}`
      },
      body: JSON.stringify({
        command: 'dial',
        params: {
          url: agentUrl,
          // Keep from + caller_id aligned to avoid inconsistent caller-id presentation.
          from: normalizedFrom,
          to: normalizedTo,
          caller_id: normalizedFrom,
          timeout: 60,
          max_duration: 3600
        }
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
      app.log.error({ result, status: response.status }, '[trigger-call] SignalWire call creation failed');
      return reply.code(500).send({
        success: false,
        error: result.message || result.error || `SignalWire API error (${response.status})`
      });
    }
    
    const callId = result.id || result.call_id || result.sid;
    app.log.info({
      call_id: callId,
      status: response.status,
      to_phone: normalizedTo,
      from_phone: normalizedFrom
    }, '[trigger-call] Call created');
    
    return reply.code(200).send({
      success: true,
      call_id: callId,
      message: 'Outbound call initiated via SignalWire Calling API'
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

