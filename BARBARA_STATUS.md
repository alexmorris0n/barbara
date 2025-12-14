# Barbara Agent - Current Status

**Last Updated:** 2025-12-14  
**Agent Version:** SDK v1.0.2  
**Deployment:** Fly.io (`barbara-agent`)

---

## 🟢 Current State: PRODUCTION READY

### What's Working End-to-End

**Call Flow:**
```
GREET → VERIFY → QUALIFY → QUOTE → ANSWER → BOOK → GOODBYE
```

**Outbound Calls:**
- ✅ AI starts with "Hi, may I speak with [name]?"
- ✅ Identity confirmation → mark_greeted()
- ✅ Goal capture → set_caller_goal()
- ✅ Address verification → mark_address_verified()
- ✅ Age/value/mortgage collection → update_lead_info()
- ✅ Quote calculation → calculate_reverse_mortgage()
- ✅ Questions answered → search_knowledge()
- ✅ Appointment booking → book_appointment()
- ✅ SMS consent → mark_sms_consent()
- ✅ Graceful goodbye

**Inbound Calls:**
- ✅ "Hello! This is Barbara from Equity Connect..."
- ✅ Returning caller recognition
- ✅ New caller flow
- ✅ Same tool chain as outbound

---

## 🔧 Architecture

### Prompt System (4o-mini Optimized)
- **Theme:** Global personality, output rules, guardrails
- **Nodes:** 8 nodes with clean numbered instructions
- **Format:** Inline constraints, no separate ROUTING section
- **Placeholders:** `${global_data.X}` resolved in Python before sending

### Context Isolation
- Only current node's instructions loaded
- `change_context()` lazy-loads target node
- Old instructions cleared on context switch
- Prevents hallucination from other nodes

### Database Tables
| Table | Purpose |
|-------|---------|
| `leads` | Lead data, broker assignment |
| `conversation_state` | Per-call state, flags |
| `prompts` + `prompt_versions` | Node instructions |
| `theme_prompts` | Global theme |
| `contexts_config` | Fillers (enter/exit) |
| `appointments` | Booking records |

---

## 🛠 Tools Available

| Tool | Node(s) | Purpose |
|------|---------|---------|
| `mark_greeted` | greet | Identity confirmed |
| `mark_wrong_person` | greet | Wrong person answered |
| `set_caller_goal` | greet | Capture their reason |
| `mark_address_verified` | verify | Address confirmed |
| `update_lead_info` | verify, qualify | Save lead data |
| `mark_age_qualified` | qualify | Age 62+ confirmed |
| `mark_equity_qualified` | qualify | Equity calculated |
| `calculate_reverse_mortgage` | quote | Get quote numbers |
| `mark_quote_presented` | quote | Quote given |
| `search_knowledge` | answer, objections | KB lookup |
| `check_broker_availability` | book | Get time slots |
| `book_appointment` | book | Create calendar event |
| `mark_sms_consent` | book | Record SMS permission |
| `change_context` | all | Switch nodes |

---

## 📊 Current Settings

| Setting | Value | Source |
|---------|-------|--------|
| LLM | gpt-4o-mini | `signalwire_available_llm_models` |
| STT | deepgram:nova-3 | `signalwire_available_stt_models` |
| TTS | amazon.Danielle:neural | `signalwire_available_voices` |
| Temperature | 0.4 | `agent_params` |

---

## ✅ Recent Fixes (Dec 14)

- **4o-mini Optimization:** All prompts rewritten for smaller model
- **Routing Removed:** No more separate ROUTING section (inline only)
- **Vue Cleanup:** Routing field removed from portal
- **Fallbacks Updated:** Match production prompts
- **Webhook Fixed:** Manual booking webhook has default URL
- **Phone Ringing:** Recording settings removed (was causing ghost answer)

---

## 🔗 Quick Links

- **GitHub:** github.com/alexmorris0n/barbara
- **Fly.io:** fly.io/apps/barbara-agent
- **Supabase:** supabase.com/dashboard/project/mxnqfwuhvurajrgoefyg

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `barbara/barbara_agent.py` | Main agent, on_swml_request, tools |
| `barbara/services/database.py` | DB queries, prompt assembly |
| `barbara/services/fallbacks.py` | Emergency fallback prompts |
| `barbara/tools/booking.py` | Booking + availability tools |
| `barbara/tools/flags.py` | State management tools |
| `portal/src/views/admin/Verticals.vue` | Prompt editor UI |
