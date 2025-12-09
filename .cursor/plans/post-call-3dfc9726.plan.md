---
name: Post-Call Data Collection (Debug Webhook)
overview: ""
todos:
  - id: 664edb12-bd81-4c80-8b66-e96611f57581
    content: Add debug_webhook_url and debug_webhook_level to set_params()
    status: completed
  - id: 7a6fa4ef-6e63-49c6-991d-186ed62a695d
    content: Create /debug-log endpoint using agent.get_app()
    status: completed
  - id: 244fb18d-51d8-4c97-984f-8542e92fa748
    content: Create /recording-status endpoint for recording webhook
    status: pending
  - id: be419531-e4c8-48d9-bf94-38d6aa5226ad
    content: Add record_call post-answer verb with status_url
    status: pending
  - id: cd4379c4-f4f3-450a-80d9-a44e18b3547b
    content: Add insert_call_debug_log() to database.py
    status: completed
  - id: c104db61-2d7e-43ee-847c-7ee3d05aa3c2
    content: Create migration for call_debug_logs table
    status: completed
  - id: 4cee2c95-eddc-4628-8e78-3a3cc1edd751
    content: Test call to verify debug webhook payload structure
    status: completed
---

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