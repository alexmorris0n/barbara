# Barbara Agent - Daily Status

**Last Updated:** 2025-12-10  
**Agent Version:** SDK v1.0.2  
**Deployment:** Fly.io (`barbara-agent`)

---

## 🟢 Current State: PRODUCTION READY

### Today's Changes (Dec 10)
- ✅ Added `persona_name` to global_data (from email campaign sender)
- ✅ Added `caller_goal` tracking with `set_caller_goal` tool
- ✅ Added personality section to theme prompts
- ✅ Updated GREET v9: persona intro, goal capture, emotional intelligence
- ✅ Updated VERIFY: removed redundant intro
- ✅ Updated QUALIFY: removed redundant intro, mortgage balance recording
- ✅ Updated QUOTE v2: ties to goal, "any questions?" before booking, disqualification handling
- ✅ Updated ANSWER v3: cleaner QUOTE→ANSWER→BOOK flow
- ✅ Updated BOOK v3: post-booking reinforcement, commitment check
- ✅ Updated GOODBYE v2: goal-tied summary, hostile caller handling
- ✅ Updated conversational_flow in theme prompts
- ✅ Activated all new prompt versions in database
- ✅ Fixed voice mismatch (greeting now uses DB voice, not hardcoded)
- ✅ Fixed `booking-notifications` edge function grant_id extraction
- ✅ Added privacy filter to skip non-booking calendar events
- ✅ Created `prompts_v1_baseline.md` snapshot
- ✅ Traced 80% coverage scenarios (golden route, disqualification, objections, returning callers)

### Recent Changes (Dec 9)
- ✅ Added `debug_webhook_url` pointing to Supabase Edge Function
- ✅ Created `debug-webhook` Edge Function for full call transcripts
- ✅ Created `call_debug_logs` table for storing debug data
- ✅ Fixed SWML null response issue (removed broken get_full_url usage)

- ✅ Created `appointments` table for reminder tracking
- ✅ Added persona SMS webhook trigger (n8n adds delay for natural feel)
- ✅ Updated `booking` tool to record appointments for reminders

### Blocking Issues
- [ ] JWT verification must be manually disabled for edge functions (Supabase limitation)

---

## 📊 Key Metrics (Update Daily)

| Metric | Today | Yesterday | Notes |
|--------|-------|-----------|-------|
| Calls Handled | - | - | |
| Appointments Booked | - | - | |
| Booking Rate | - | - | Target: 15%+ |
| Avg Call Duration | - | - | |
| Transfers to Broker | - | - | |

---

## 🔧 Configuration

### Database Tables
| Table | Purpose |
|-------|---------|
| `leads` | Lead data, verification, qualification status, `persona_sender_name` |
| `conversation_state` | Per-call state tracking, `caller_goal` |
| `interactions` | Call summaries, outcomes |
| `brokers` | Broker info, Nylas grants, phone numbers |
| `agent_params` | Temperature, timeouts, behavior settings |
| `prompts` | Node prompt definitions |
| `prompt_versions` | Versioned prompt content with `is_active` flag |
| `active_node_prompts` | View joining prompts to active versions |
| `theme_prompts` | Global personality, identity, guardrails |
| `contexts_config` | Node routing, isolation settings |
| `call_debug_logs` | Full debug webhook data (transcripts, tool calls) |

### Current Prompt Versions
| Node | Active Version | Key Features |
|------|----------------|--------------|
| GREET | v9 | Persona intro, goal capture, emotional intelligence |
| VERIFY | v5 | No redundant intro, address check only |
| QUALIFY | v5 | No redundant intro, mortgage balance recorded |
| QUOTE | v2 | Goal-tied presentation, questions before booking |
| ANSWER | v3 | Clean flow to BOOK |
| OBJECTIONS | v2 | Family concerns, "think about it" handling |
| BOOK | v3 | Post-booking reinforcement, commitment check |
| GOODBYE | v2 | Goal-tied summary, hostile caller handling |

### Current Settings
| Setting | Value | Table |
|---------|-------|-------|
| Temperature | 0.3 | `agent_params` |
| TTS Voice | Dynamic from DB | `signalwire_available_voices` |
| LLM | gpt-4.1-mini | `signalwire_available_llm_models` |
| STT | deepgram:nova-3 | `signalwire_available_stt_models` |
| Debug Webhook | Level 2 (full) | Supabase Edge Function |

---

## 🎯 Golden Route (Outbound Call)

```
GREET → VERIFY → QUALIFY → QUOTE → ANSWER → BOOK → GOODBYE
```

### Conversation Flow
1. **GREET**: Persona intro ("Carlos asked me to call..."), goal capture, emotional intelligence
2. **VERIFY**: Confirm address (10-15 seconds)
3. **QUALIFY**: Age, home value, mortgage balance
4. **QUOTE**: Calculate, tie to goal, "any questions before booking?"
5. **ANSWER**: Answer questions, route to BOOK
6. **BOOK**: Offer slot, book, commitment check, tax bill reminder
7. **GOODBYE**: Goal-tied summary, confirmation email mention

### Key Features
- **Goal Tracking**: Captured in GREET, stored in DB, referenced throughout
- **Emotional Intelligence**: Empathetic for medical/family, warm for travel/home
- **Returning Callers**: Reference previous goal from `caller_goal`
- **Post-Booking Reinforcement**: Tax bill prep, conflict check, goal reminder

---

## 📋 Implementation Checklist

### ✅ Completed
- [x] Function fillers (5 tools)
- [x] Post-prompt call summaries
- [x] Speech recognition hints
- [x] Temperature tuning (0.3)
- [x] Broker transfer tool
- [x] wait_for_user (conditional on direction)
- [x] frequency_penalty + presence_penalty
- [x] Dynamic TTS voice from DB
- [x] Persona-based greetings
- [x] Goal tracking (`caller_goal`)
- [x] Emotional intelligence in prompts
- [x] Post-booking reinforcement
- [x] Commitment check (reduce no-shows)
- [x] Hostile caller handling
- [x] Debug webhook (full transcripts)
- [x] Booking notification emails (Edge Function)
- [x] Quote context isolation disabled
- [x] Smooth node transitions (no redundant intros)
- [x] 80% trace coverage validated

### 🟡 In Progress
- [ ] SMS appointment confirmation (blocked: 10DLC)
- [ ] Test call validation (morning Dec 11)

### 📝 Backlog (Medium Priority)
- [ ] Pronunciation rules (HECM → "heck-em")
- [ ] Context enter/exit fillers
- [ ] Call recording
- [ ] DateTime skill
- [ ] Wrong person handoff detection

### 💡 Future (Nice to Have)
- [ ] Toggle functions based on state
- [ ] Back-to-back functions
- [ ] DataMap for simple API calls
- [ ] Voice change detection for handoffs

---

## 🐛 Known Issues

| Issue | Severity | Status | Notes |
|-------|----------|--------|-------|
| JWT verification on Edge Functions | Low | Workaround | Must manually disable in Supabase Dashboard |
| Double-click triggers 2 calls | Low | UI Bug | Need debounce in Vue portal |

---

## 📝 Notes

**Dec 10:**
- Major prompt update focused on personality and goal-tracking
- All new prompts activated and traced through golden route
- 80% scenario coverage validated (golden, disqualification, objections, returning)
- Created `prompts_v1_baseline.md` as production snapshot

**Dec 9:**
- Fixed call hanging issue (SWML returning null)
- Root cause: incorrect `get_full_url()` usage in debug webhook setup
- Added Supabase Edge Function for debug webhooks

**Nov 25:**
- Voice quality concern raised - switched from Kendra Neural to Joanna Generative
- Low temperature (0.3) is correct for routing reliability
- Added penalties to reduce repetitive phrasing

---

## 🔗 Quick Links

- **GitHub:** github.com/alexmorris0n/barbara
- **Fly.io Dashboard:** fly.io/apps/barbara-agent
- **Supabase:** supabase.com/dashboard/project/mxnqfwuhvurajrgoefyg
- **SDK Docs:** `aiagentssdk_manual.md`
- **Prompt Baseline:** `prompts_v1_baseline.md`
- **Trace Tests:** `trace_test.md`

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `barbara/barbara_agent.py` | Main agent, tools, global_data |
| `barbara/services/database.py` | DB queries, theme/prompt loading |
| `barbara/tools/flags.py` | State management tools |
| `prompts_v1_baseline.md` | Flattened production prompts |
| `trace_test.md` | Conversation trace scenarios |
| `supabase/functions/debug-webhook/` | Debug log Edge Function |
| `supabase/functions/booking-notifications/` | Email confirmation Edge Function |
