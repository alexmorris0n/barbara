<!-- 3dfc9726-2db2-4ac4-ab20-5441a102ee19 1cfd8b00-88c3-4ff1-a9c4-6518a5eba734 -->
# Post-Call Data Collection (Debug Webhook)

## Summary

Capture transcripts and tool calls from SignalWire calls using `debug_webhook_url` parameter. Recording is deferred - SignalWire may already handle it.

---

## What We're Implementing

Add `debug_webhook_url` to receive conversation data including:

- Transcript (speech events)
- Tool calls made during the call
- Context/routing changes (possibly)

---

## Implementation Steps

### 1. Add debug_webhook params to agent

In [barbara/barbara_agent.py](barbara/barbara_agent.py) line ~402 in `set_params()`, add:

```python
"debug_webhook_url": f"{self.get_full_url()}/debug-log",
"debug_webhook_level": 2,  # Max verbosity per SDK line 23690
```

### 2. Create endpoint to receive debug data

Add custom route using `agent.get_app()` at bottom of [barbara/barbara_agent.py](barbara/barbara_agent.py):

```python
from fastapi import Request

# After: agent = BarbaraAgent()
app = agent.get_app()

@app.post("/debug-log")
async def receive_debug_log(request: Request):
    data = await request.json()
    logger.info(f"[DEBUG-WEBHOOK] Received: {data}")
    # Initially just log to see structure
    # Later: store to database
    return {"status": "ok"}
```

### 3. Create database table (migration)

Create `migrations/YYYYMMDD_add_call_debug_logs.sql`:

```sql
CREATE TABLE IF NOT EXISTS call_debug_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    call_id TEXT NOT NULL,
    lead_id UUID REFERENCES leads(id),
    event_type TEXT,
    event_data JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_call_debug_logs_call_id ON call_debug_logs(call_id);
```

### 4. Add database insert function

In [barbara/services/database.py](barbara/services/database.py), add `insert_call_debug_log()`.

### 5. Test and verify payload structure

Make a test call, check logs to see what data actually comes through, then adjust schema/insert logic accordingly.

---

## Files to Modify

| File | Changes |

|------|---------|

| [barbara/barbara_agent.py](barbara/barbara_agent.py) | Add debug_webhook params + /debug-log endpoint |

| [barbara/services/database.py](barbara/services/database.py) | Add insert_call_debug_log() function |

| migrations/ | New migration + rollback for call_debug_logs table |

---

## SDK References (All Verified)

- `debug_webhook_url`: Line 23689
- `debug_webhook_level`: Line 23690 (0-2, higher = more verbose)
- `get_full_url()`: Line 17308-17315
- `get_app()`: Line 17358

### To-dos

- [x] Add debug_webhook_url and debug_webhook_level to set_params()
- [x] Create /debug-log endpoint using agent.get_app()
- [ ] Create /recording-status endpoint for recording webhook
- [ ] Add record_call post-answer verb with status_url
- [x] Add insert_call_debug_log() to database.py
- [x] Create migration for call_debug_logs table
- [x] Test call to verify debug webhook payload structure