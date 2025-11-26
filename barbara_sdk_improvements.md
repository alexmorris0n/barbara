# Barbara SDK Improvement Checklist

## Project Goal
Improve appointment booking success rate by implementing unused SignalWire AI Agents SDK features.

**Target Audience:** Seniors (62+) needing patience and clear communication  
**Revenue Model:** Only paid when appointments are booked  
**Scale Goal:** 100 brokers

---

## 🔴 HIGH PRIORITY - Implement First

### 1. [x] Function Fillers ✅ COMPLETED
**Impact:** Eliminates dead silence during tool execution - critical for seniors  
**Effort:** Low  
**Section:** 4.13

~~Currently NO fillers on any tools. When `calculate_reverse_mortgage` or `check_broker_availability` runs, there's silence.~~

**Added fillers to:**
- [x] `calculate_reverse_mortgage` - "Let me run those numbers for you...", "Calculating what you might qualify for...", "One moment while I crunch the numbers..."
- [x] `check_broker_availability` - "Let me check the calendar...", "Looking at available times...", "One moment while I check availability..."
- [x] `book_appointment` - "Let me schedule that for you...", "Booking your appointment now...", "One moment while I get that set up..."
- [x] `search_knowledge` - "Let me look that up for you...", "Good question, let me find that information...", "One moment while I check on that..."
- [x] `verify_caller_identity` - "Let me verify that...", "One moment while I look you up...", "Let me pull up your information..."

---

### 2. [x] Post-Prompt Call Summaries ✅ COMPLETED
**Impact:** Business intelligence - track why calls don't convert  
**Effort:** Medium  
**Section:** 6.16.4

~~No post-prompt = losing all call outcome data.~~

**Implementation:**
- [x] Add `set_post_prompt()` with JSON schema in `__init__`
- [x] Add `on_summary()` callback to handle post-prompt data
- [x] Write to existing `interactions` table (no new table needed)
- [ ] Build n8n workflow to process summaries (optional - data already in Supabase)

**Data captured:**
- ✅ Outcome (booked/not_booked/disqualified/wrong_person/transferred/callback_requested)
- ✅ Appointment time (if booked) → `interactions.scheduled_for`
- ✅ Qualification status → `interactions.metadata.qualification_status`
- ✅ Objections raised → `interactions.metadata.objections`
- ✅ Caller sentiment → `interactions.metadata.sentiment`
- ✅ Follow-up needed → `interactions.metadata.follow_up_needed`
- ✅ Call summary → `interactions.content`

---

### 3. [x] Speech Recognition Hints ✅ COMPLETED
**Impact:** Better STT accuracy for industry terms  
**Effort:** Low  
**Section:** 3.22

~~No hints = STT struggles with financial terms.~~

**Added hints for:**
- [x] Industry: "HECM", "reverse mortgage", "FHA", "HUD", "equity", "principal limit", "tenure", etc.
- [x] Company: "Equity Connect", "Barbara"
- [x] Property: "my home", "my house", "mortgage balance", "property value", "payoff"
- [x] Ages: "sixty two" through "ninety" (seniors stating their age)
- [x] Senior phrases: "fixed income", "social security", "retirement", "pension"
- [x] Booking: "appointment", "schedule", "tomorrow", "morning", "afternoon"
- [x] Objections: "scam", "hidden fees", "lose my home", "heirs", "inheritance"
- [ ] Broker names (dynamic from database) - Future: add in on_swml_request

---

### 4. [ ] SMS Appointment Confirmation
**Impact:** Reduces no-shows, professional touch  
**Effort:** Low  
**Section:** 4.21.5

Appointments booked but NO confirmation sent.

**Implementation:**
- [ ] Add `.send_sms()` to `book_appointment` result
- [ ] Include: appointment time, broker name, broker phone
- [ ] Configure SignalWire number for SMS

---

### 5. [~] AI Timing Parameters for Seniors (PARTIAL)
**Impact:** Prevents premature hangups, allows thinking time  
**Effort:** Low  
**Section:** 3.21

**Changes:**
- [x] `attention_timeout` - Already configurable in Vue portal/DB ✓
- [x] `inactivity_timeout` - Already configurable in Vue portal/DB ✓
- [x] `wait_for_user`: Now conditional on call direction - `True` for outbound (wait for senior to answer), `False` for inbound (Barbara greets first)

---

### 5.5. [x] Temperature Parameter Tuning ✅ COMPLETED
**Impact:** More deterministic routing, fewer wrong context switches  
**Effort:** Very Low (5 min)  
**Section:** 3.21.3.4

**Implementation:**
- [x] `temperature` already exists in `agent_params` table
- [x] Now loaded via `get_active_signalwire_models()` 
- [x] Used in `set_params({"temperature": ...})` in `on_swml_request`
- [x] Updated DB from 0.8 → **0.3** (SDK default, appropriate for booking agent)
- [ ] A/B test values with real calls (0.2-0.4 range)

**Reference values:**
- 0.2 = FAQ bot (very consistent)
- **0.3 = SDK default** ← Barbara uses this
- 0.5 = Customer service (balanced)
- 0.9 = Entertainment (creative)

---

### 6. [x] Direct Broker Transfer (Fallback) ✅ COMPLETED
**Impact:** Salvages calls when automated booking fails  
**Effort:** Medium  
**Section:** 6.18

~~Currently says "someone will call you" but doesn't transfer.~~

**Implementation:**
- [x] Add `broker_phone` to global_data (E.164 format from `brokers.primary_phone_e164`)
- [x] Add `transfer_to_broker` tool with fillers
- [x] Use `.connect(broker_phone, final=True)` for permanent handoff
- [x] Trigger when: booking fails, customer requests human, complex questions, frustrated caller
- [x] Graceful fallback if broker phone missing (offer callback instead)
- [x] Logs transfer reason to conversation_state

---

## 🟡 MEDIUM PRIORITY - Implement After High Priority

### 7. [ ] Pronunciation Rules
**Impact:** Professional polish, clearer TTS  
**Effort:** Low  
**Section:** 3.20.6

Financial terms may sound robotic.

**Add pronunciations:**
- [ ] "HECM" → "heck-em"
- [ ] "HUD" → "H U D"
- [ ] "FHA" → "F H A"
- [ ] Company/broker names as needed

---

### 8. [ ] Context Enter/Exit Fillers
**Impact:** Smoother conversation transitions  
**Effort:** Low  
**Section:** 6.10.6

No transition phrases between contexts.

**Add fillers to contexts:**
- [ ] `greet` → `verify`: "Great! Let me just verify a few details..."
- [ ] `verify` → `qualify`: "Perfect, now let me ask a few questions..."
- [ ] `qualify` → `quote`: "Wonderful! Let me calculate what you might qualify for..."
- [ ] `quote` → `book`: "Excellent! Let's get you scheduled..."
- [ ] Any → `objections`: "I understand your concern..."

---

### 8.5. [ ] Context Isolation for QUOTE
**Impact:** Cleaner calculations without conversation history noise  
**Effort:** Low  
**Section:** 6.10.1

QUOTE context could benefit from fresh start - just the numbers.

**Implementation:**
- [ ] Add `.set_isolated(True)` to QUOTE context in `__init__`
- [ ] Test if it improves calculation accuracy
- [ ] Consider for BOOK as well (focused booking flow)

---

### 9. [x] Global Data for Dynamic Prompts ✅ COMPLETED
**Impact:** Cleaner code, easier maintenance  
**Effort:** Medium  
**Section:** 6.16.2

~~Currently building context manually.~~

**Implementation:**
- [x] Use `set_global_data()` in `on_swml_request`
- [x] Replace context injection with `${global_data.X}` variables
- [x] Store: caller_name, property_city, broker_name, is_qualified, is_verified
- [x] Update all tool handlers with `.update_global_data()` for real-time state
- [x] Update fallback node configs to reference `${global_data.X}`
- [x] Handle scenario: wrong data corrected mid-call
- [x] Handle scenario: fresh caller builds global_data as info collected

---

### 10. [ ] Call Recording
**Impact:** Compliance, QA, training  
**Effort:** Medium  
**Section:** 6.17

No recording for quality assurance.

**Implementation:**
- [ ] Add recording consent announcement
- [ ] Use `.record_call()` with stereo=True
- [ ] Configure recording storage
- [ ] Add pause/resume for sensitive info (SSN, etc.)

---

### 11. [ ] DateTime Skill
**Impact:** Better date/time handling for booking  
**Effort:** Low  
**Section:** 5.18

Only using "math" skill.

**Implementation:**
- [ ] Add `self.add_skill("datetime")`
- [ ] Helps with: "What day is tomorrow?", natural date parsing

---

## 🟢 NICE TO HAVE - Future Improvements

### 12. [ ] Toggle Functions Based on State
**Impact:** Prevents premature booking attempts  
**Effort:** Medium  
**Section:** 4.21.11.5

**Implementation:**
- [ ] Disable booking tools until verified/qualified
- [ ] Use `.toggle_functions()` in verification results

---

### 13. [ ] Back-to-Back Functions
**Impact:** Smoother sequential operations  
**Effort:** Low  
**Section:** 4.21.11.5

**Implementation:**
- [ ] Enable for availability check → booking sequence
- [ ] Use `.back_to_back_functions(True)`

---

### 14. [ ] DataMap for Simple API Calls
**Impact:** Serverless calendar checks  
**Effort:** Medium  
**Section:** 4.22

**Consider for:**
- [ ] Broker availability (if simple REST API)
- [ ] Property value lookup

---

## Implementation Notes

### Testing Each Feature
1. Use `swaig-test` CLI for function testing
2. Test with actual senior callers (or simulate slow speech)
3. Monitor post-prompt data for improvements

### Rollout Order
1. Function fillers + timing params (immediate UX improvement)
2. Post-prompt (start collecting data)
3. Speech hints + pronunciation (accuracy)
4. SMS confirmation (reduce no-shows)
5. Broker transfer (fallback path)
6. Recording + remaining items

### Database Changes Needed
- [ ] `call_summaries` table for post-prompt data
- [ ] `call_recordings` table for recording URLs
- [ ] Update `conversation_state` for new flags

---

## Reference

**SDK Documentation:** `aiagentssdk_manual.md`  
**Current Agent:** `barbara/barbara_agent.py`  
**Fallback Configs:** `barbara/services/fallbacks.py`

