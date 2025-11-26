# **BarbGraph Trace Testing**

---

## **🎯 CRITICAL BUSINESS GOAL: BOOK APPOINTMENTS**

**WE GET PAID WHEN WE BOOK APPOINTMENTS.**

- Use an educational, non-pushy approach
- Guide leads through: verify → qualify → quote → answer questions → **BOOK** → goodbye
- Every conversation path should aim toward booking when appropriate
- If qualified and quoted, always attempt to book before ending

**The Golden Route (Outbound Call):**
GREET → VERIFY → QUALIFY → QUOTE → ANSWER → **BOOK** → GOODBYE

---

## **What This Accomplishes**

### **Why Trace Scenarios:**
1. **Finds routing bugs** - "Wait, this should go to OBJECTIONS but routes to ANSWER"
2. **Identifies missing flags** - "We never set `quote_presented=true` in this path"
3. **Exposes tool gaps** - "We need a tool that doesn't exist"
4. **Validates completion criteria** - "Node says it's complete but key data missing"
5. **Tests edge case handling** - "What happens if they say X at this node?"

**Think of it as:** Unit testing your conversation architecture before deploying.

---

## **Current Node Configuration**

### **GREET**
- **valid_contexts:** `['answer', 'verify', 'quote']`
- **tools:** `['mark_wrong_person']`
- **step_criteria:** Route based on user response - questions → ANSWER, calculation → QUOTE, otherwise → VERIFY

### **VERIFY**
- **valid_contexts:** `['qualify', 'answer', 'quote', 'objections']`
- **tools:** `['verify_caller_identity', 'update_lead_info']`
- **step_criteria:** Complete when info confirmed/updated. Route: amounts → QUOTE, questions → ANSWER, concerns → OBJECTIONS, else → QUALIFY

### **QUALIFY**
- **valid_contexts:** `['goodbye', 'quote', 'objections']`
- **tools:** `['mark_qualification_result', 'update_lead_info']`
- **step_criteria:** Complete after qualification. Route: objections → OBJECTIONS, qualified=true → QUOTE, qualified=false → GOODBYE

### **QUOTE**
- **valid_contexts:** `['answer', 'book', 'goodbye', 'objections']`
- **tools:** `['calculate_reverse_mortgage', 'mark_quote_presented']`
- **step_criteria:** Complete after presenting quote and gauging reaction. Route: positive reaction → ANSWER (for questions) or BOOK (if ready), objections → OBJECTIONS, else → ANSWER

### **ANSWER**
- **valid_contexts:** `['goodbye', 'book', 'objections', 'quote']`
- **tools:** `['search_knowledge', 'mark_ready_to_book']`
- **step_criteria:** CRITICAL: Calculation questions → QUOTE immediately. Other questions → answer, then route: ready to book → BOOK, objections → OBJECTIONS, more questions → stay in ANSWER, else → BOOK (attempt booking)

### **OBJECTIONS**
- **valid_contexts:** `['answer', 'book', 'goodbye']`
- **tools:** `['search_knowledge', 'mark_objection_handled', 'mark_has_objection']`
- **step_criteria:** Complete when objection resolved. Route: resolved → BOOK (always attempt booking after resolution), more questions → ANSWER, persistent hesitation → BOOK (offer consultation), else → GOODBYE

### **BOOK**
- **valid_contexts:** `['goodbye']`
- **tools:** `['check_broker_availability', 'book_appointment']`
- **step_criteria:** Appointment booked or declined
- **Sets `appointment_datetime` flag on successful booking**

### **GOODBYE**
- **valid_contexts:** `['answer']`
- **tools:** `[]`
- **step_criteria:** Said farewell and caller responded or stayed silent

---

## **Recommended Scenarios to Trace**

### **Category 1: Happy Path (3 scenarios)**

#### **Scenario 1: Perfect Qualified Lead (Golden Route)**
```
SETUP:
- OUTBOUND call to lead
- Lead is 68, owns home, $400k value, $200k mortgage
- Interested, has a few questions, no objections
- Ready to book after questions answered

EXPECTED TRACE:
GREET → outbound greeting, lead responds warmly → route to VERIFY
VERIFY → confirm contact (collect missing, confirm existing) → route to QUALIFY
QUALIFY → collect 4 gates → mark_qualification_result(qualified=true) → route to QUOTE
QUOTE → calculate_reverse_mortgage(200000, 68) → present $80k net → mark_quote_presented(positive) → route to ANSWER
ANSWER → lead asks questions → search_knowledge() → answer questions → mark_ready_to_book(true) → route to BOOK
BOOK → check_broker_availability → book_appointment → set appointment_datetime → route to GOODBYE
GOODBYE → warm farewell, confirm appointment details

FLAGS SET:
- greeted=true (automatic in GREET)
- verified=true (verify_caller_identity in VERIFY)
- qualified=true (mark_qualification_result in QUALIFY)
- quote_presented=true (mark_quote_presented in QUOTE)
- quote_reaction='positive' (mark_quote_presented in QUOTE)
- appointment_datetime='2025-11-21T14:00:00' (book_appointment in BOOK)

TOOLS CALLED:
1. verify_caller_identity (VERIFY)
2. update_lead_info (VERIFY - if needed)
3. mark_qualification_result(qualified=true) (QUALIFY)
4. calculate_reverse_mortgage(200000, 68) (QUOTE)
5. mark_quote_presented(reaction='positive') (QUOTE)
6. search_knowledge() (ANSWER - for questions)
7. mark_ready_to_book(true) (ANSWER)
8. check_broker_availability() (BOOK)
9. book_appointment() (BOOK)

VALIDATION CHECKS:
- Does VERIFY use "collect missing, confirm existing" pattern?
- Does QUALIFY route to QUOTE after qualified=true?
- Does QUOTE call calculate_reverse_mortgage correctly?
- Does QUOTE route to ANSWER (not directly to BOOK) when questions are expected?
- Does ANSWER handle questions and then route to BOOK?
- Does BOOK set appointment_datetime flag?
- Does each node complete and route correctly?
- **CRITICAL: Does the flow end with a booked appointment?**
```

#### **Scenario 2: Unqualified Lead Asking Amounts**
```
SETUP:
- OUTBOUND call to lead
- Lead asks "How much can I get?" immediately in GREET
- But they're only 58 years old (doesn't qualify)

EXPECTED TRACE:
GREET → user asks "How much can I get?" → route to QUOTE
QUOTE → attempt calculate_reverse_mortgage → discover age missing/invalid
QUOTE → realizes they need qualification data → route to QUALIFY
QUALIFY → ask age → discover 58 → mark_qualification_result(qualified=false, reason='age_below_62')
QUALIFY → route to GOODBYE
GOODBYE → empathetic disqualification

FLAGS SET:
- qualified=false
- disqualified_reason='age_below_62'

VALIDATION CHECKS:
- Does GREET route calculation questions to QUOTE?
- Does QUOTE handle missing data gracefully?
- Does QUALIFY correctly disqualify based on age?
- Does GOODBYE have empathetic disqualification script?
```

#### **Scenario 3: Pre-Qualified Returning Caller**
```
SETUP:
- OUTBOUND call (follow-up to previous call)
- Lead called 3 days ago, got to QUOTE, said "need to think"
- conversation_data: greeted=true, verified=true, qualified=true, quote_presented=true, quote_reaction='skeptical'
- Now ready to book

EXPECTED TRACE:
Initial node determination: _get_initial_context() sees qualified=true, quote_presented=true, quote_reaction='skeptical' → starts at ANSWER or GREET?
If GREET: detects returning caller → asks "How can I help?" → user says "ready to book" → route to BOOK
If ANSWER: user says "ready to book" → mark_ready_to_book(true) → route to BOOK
BOOK → check_broker_availability → book_appointment → route to GOODBYE

VALIDATION CHECKS:
- Does _get_initial_context() correctly determine starting node for returning callers?
- Can user route directly to BOOK if already qualified and quoted?
- Does BOOK work correctly for returning callers?
```

---

### **Category 2: Objection Paths (3 scenarios)**

#### **Scenario 4: Objection After Quote**
```
SETUP:
- Gets to QUOTE
- Reacts positively to numbers
- Then says "But my daughter told me these are scams"

EXPECTED TRACE:
QUOTE → present numbers → mark_quote_presented(positive) → user raises objection
QUOTE → detect objection → route to OBJECTIONS
OBJECTIONS → mark_has_objection(type='third_party_approval') → address concern → search_knowledge("family objections reverse mortgages")
OBJECTIONS → offer adult children FAQ → mark_objection_handled() → ask if concerns resolved
If resolved: route to BOOK (CRITICAL: Always attempt booking after objection resolved)
If still hesitant: route to GOODBYE with follow-up offer (but still mention booking opportunity)

FLAGS SET:
- quote_reaction='positive'
- has_objection=true
- objection_type='third_party_approval'
- objection_handled=true (if resolved)

VALIDATION CHECKS:
- Does QUOTE correctly detect this as objection (not question)?
- Does OBJECTIONS have search_knowledge tool?
- Does mark_has_objection capture objection type?
- Does OBJECTIONS route correctly based on resolution?
```

#### **Scenario 5: Multiple Objections**
```
SETUP:
- Gets to QUOTE
- Objection 1: "What about fees?" → resolved
- Objection 2: "Will my kids lose the house?" → resolved
- Objection 3: "I'm still nervous" → unresolved

EXPECTED TRACE:
QUOTE → route to OBJECTIONS
OBJECTIONS → mark_has_objection(type='cost_fees') → search_knowledge("reverse mortgage fees") → mark_objection_handled()
User immediately raises heirs concern (still in OBJECTIONS)
OBJECTIONS → mark_has_objection(type='heirs_inheritance') → search_knowledge("heirs inheritance reverse mortgage") → mark_objection_handled()
User still hesitant "I'm still nervous"
OBJECTIONS → recognize general hesitation → offer broker consultation → route to BOOK (attempt to book consultation appointment)
If booking declined: route to GOODBYE with follow-up offer

VALIDATION CHECKS:
- Can OBJECTIONS handle multiple objections in sequence?
- Does mark_has_objection/mark_objection_handled get called for each?
- After 2+ objections, does it recognize persistent hesitation?
- Does GOODBYE offer appropriate follow-up?
```

#### **Scenario 6: Objection During QUALIFY**
```
SETUP:
- QUALIFY asking "Are you 62+?"
- Lead says "Why does that matter? Are you discriminating?"

EXPECTED TRACE:
QUALIFY → detects objection/concern → route to OBJECTIONS
OBJECTIONS → mark_has_objection(type='age_discrimination') → explain FHA requirements → mark_objection_handled()
OBJECTIONS → route back to ANSWER (for more questions) or directly ask to continue qualification?
If returns to QUALIFY: resume qualification questions

VALIDATION CHECKS:
- Does QUALIFY detect objections (not just answers)?
- Can QUALIFY route to OBJECTIONS mid-qualification?
- After OBJECTIONS resolved, can system return to QUALIFY?
- Does conversation_data track "interrupted_at_gate_question"?
```

---

### **Category 3: Edge Cases (4 scenarios)**

#### **Scenario 7: Calculation Question in ANSWER**
```
SETUP:
- User is in ANSWER context (asking general questions)
- Suddenly asks: "So how much can I actually get?"

EXPECTED TRACE:
ANSWER → detects calculation question → ⚠️ CRITICAL ROUTING RULE triggers
ANSWER → "Let me calculate that for you..." → IMMEDIATELY route to QUOTE
QUOTE → calculate_reverse_mortgage(equity, age) → present results

FLAGS SET:
- None (routing only)

VALIDATION CHECKS:
- Does ANSWER detect calculation triggers ("how much", "calculate", "money available")?
- Does ANSWER route to QUOTE (not answer itself)?
- Does step_criteria explicitly say "IMMEDIATELY route to QUOTE"?
- Does QUOTE handle mid-conversation calculations correctly?
```

#### **Scenario 8: Wrong Person Then Right Person**
```
SETUP:
- OUTBOUND call to lead
- Wife answers phone
- Says "Let me get him" (right_person_available=true)
- Husband comes on line

EXPECTED TRACE:
GREET → mark_wrong_person(right_person_available=true) → route to GOODBYE (to wait)
GOODBYE → "I'll wait while you get [name]" → wait for handoff detection
[System detects new person speaking - voice change or explicit handoff]
GOODBYE → detects new person → route back to GREET for husband
GREET → re-greet husband warmly → "Hi [name], I'm calling about..." → route to VERIFY
VERIFY → continue with golden route (verify → qualify → quote → answer → BOOK → goodbye)

FLAGS SET:
- wrong_person=true (initially)
- right_person_available=true
- wrong_person=false (cleared when husband comes on)

VALIDATION CHECKS:
- Does GOODBYE have "wait for handoff" logic?
- How does system detect new person on line? (voice change detection, explicit handoff signal, or timeout?)
- Does GREET restart fresh for the correct person?
- Does mark_wrong_person flag get cleared when right person comes on?
- After re-greeting, does the conversation continue through the full golden route?
- **CRITICAL: Does the conversation still end with BOOK attempt?**
```

#### **Scenario 9: Borderline Equity (Low Net Proceeds)**
```
SETUP:
- $300k home, $270k mortgage
- 68 years old, qualifies
- Net proceeds after payoff: ~$15k

EXPECTED TRACE:
QUALIFY → qualified=true, borderline_equity=true → route to QUOTE
QUOTE → calculate_reverse_mortgage(30000, 68) → returns ~$15k
QUOTE → present numbers with reframing: "You'd have $15k available, plus your mortgage payment would be eliminated"
Lead says "That's way less than I expected"
QUOTE → detect disappointment → mark_quote_presented(reaction='negative') → route to OBJECTIONS or ANSWER?
OBJECTIONS/ANSWER → address concerns → still attempt BOOK (even with low equity, consultation may be valuable)

FLAGS SET:
- qualified=true
- borderline_equity=true (from QUALIFY)
- quote_reaction='negative'

VALIDATION CHECKS:
- Does QUALIFY set borderline_equity flag?
- Does QUOTE use low-equity reframing script?
- Does QUOTE route appropriately for disappointed reactions?
- Can OBJECTIONS handle expectations management?
```

#### **Scenario 10: Booked Lead Calls Back with Questions**
```
SETUP:
- Lead booked appointment 3 days ago
- conversation_data: appointment_booked=true, appointment_datetime='2025-11-21T14:00:00'
- Now calling back with questions before the appointment

EXPECTED TRACE:
Initial node: _get_initial_context() sees appointment_booked=true → starts at GOODBYE
GOODBYE → "Hi [name]! You have an appointment on [date]. How can I help?" (uses appointment_datetime)
User: "I have some questions"
GOODBYE → route to ANSWER
ANSWER → user asks questions → search_knowledge() → answer questions
ANSWER → "Any other questions?" → user satisfied → route back to GOODBYE
GOODBYE → reconfirm appointment → end call

FLAGS SET:
- No new flags (appointment details already set)

VALIDATION CHECKS:
- Does _get_initial_context() correctly route appointment_booked=true to GOODBYE?
- Does GOODBYE acknowledge the appointment using appointment_datetime?
- Can GOODBYE route to ANSWER for questions?
- Can ANSWER route back to GOODBYE after questions?
- Does system preserve appointment_datetime throughout?
```

---

### **Category 4: Failure Modes (3 scenarios)**

#### **Scenario 11: Tool Failure During BOOK**
```
SETUP:
- Everything perfect until BOOK
- check_broker_availability times out or returns error

EXPECTED TRACE:
BOOK → call check_broker_availability() → TIMEOUT/ERROR
BOOK → fallback logic → "I'm having trouble accessing the calendar right now"
BOOK → set manual_booking_required=true → route to GOODBYE
GOODBYE → "Someone will call you within 24 hours to schedule"

FLAGS SET:
- manual_booking_required=true
- appointment_booked=false

VALIDATION CHECKS:
❓ Does BOOK wrap tool calls in try/catch?
❓ Does BOOK have fallback script for tool failures?
❓ Does system set manual_booking_required flag?
❓ Does GOODBYE handle manual booking follow-up messaging?
```

#### **Scenario 12: Knowledge Base Search Timeout**
```
SETUP:
- In ANSWER node
- Caller asks "How do fees work?"
- search_knowledge times out (20s timeout)

EXPECTED TRACE:
ANSWER → call search_knowledge("reverse mortgage fees") → TIMEOUT after 20s
ANSWER → fallback response: "Fees vary by lender, but typically include origination and closing costs..."
ANSWER → "Would you like me to have a licensed advisor provide exact details?" → route to BOOK or GOODBYE

VALIDATION CHECKS:
❓ Is there timeout handling in search_knowledge tool?
❓ Does ANSWER have fallback responses for common questions?
❓ Does system log KB failures for debugging?
```

#### **Scenario 13: Unexpected Disqualification in QUOTE**
```
SETUP:
- QUALIFY marked them qualified=true (asked about primary residence, they said yes)
- In QUOTE, they reveal "Oh, it's actually a rental property I live in"

EXPECTED TRACE:
QUOTE → detects late disqualifier (rental property)
QUOTE → call mark_qualification_result(qualified=false, reason='non_primary_residence')
QUOTE → "I understand. Unfortunately, reverse mortgages require the home to be your primary residence..."
QUOTE → route to GOODBYE
GOODBYE → empathetic disqualification

FLAGS SET:
- qualified=false (overrides previous true)
- disqualified_reason='non_primary_residence'
- disqualified_in_quote=true

VALIDATION CHECKS:
- Can QUOTE call mark_qualification_result(qualified=false)?
- Does QUOTE have authority to override QUALIFY?
- Does conversation_data track late disqualification?
- Does GOODBYE have empathetic disqualification script for each reason?
```

---

## **How to Execute This Trace Test**

### **Step 1: Prepare the Context**

Gather the current configurations:
1. All 8 node instructions (from database)
2. All valid_contexts arrays (from database)
3. All step_criteria (from database)
4. All 21 tool definitions (from code)
5. All conversation flags (from docs/conversation_flags.md)

### **Step 2: Trace Each Scenario**

For each scenario, trace:
1. **Starting node** - Where does _get_initial_context() place them?
2. **Node flow** - Which nodes do they visit?
3. **Tools called** - Which tools are invoked at each node?
4. **Flags set** - Which conversation_data flags are updated?
5. **Routing decisions** - Why did it route to the next node?
6. **Completion criteria** - Was step_criteria met?

### **Step 3: Document Issues**

Log any issues found:
```
SCENARIO 1 ISSUES:
- [Document any issues found]

SCENARIO 2 ISSUES:
- [Document any issues found]

SCENARIO 7 ISSUES:
- [Document any issues found]
```

### **Step 4: Validate Configuration**

Ensure these configurations are working correctly:
- VERIFY's valid_contexts enable flexible routing
- VERIFY's "collect missing, confirm existing" pattern
- QUALIFY's valid_contexts allow objection handling
- ANSWER's CRITICAL ROUTING RULE for calculation questions
- appointment_datetime flag is set and used correctly
- "end" node is not in any routing paths

---

## **Expected Output Format**

For each scenario, produce:

```markdown
## SCENARIO 1: Perfect Qualified Lead

### Node Flow
GREET → VERIFY → QUALIFY → QUOTE → BOOK → GOODBYE

### Detailed Trace

**GREET:**
- Input: Inbound call, lead.first_name="John"
- Actions: Greet warmly, build rapport
- Tools Called: None
- Flags Set: greeted=true (automatic)
- Completion: User responds warmly
- Routing: User responds → VERIFY
- Result: [PASS/FAIL]

**VERIFY:**
- Input: greeted=true, lead data from DB
- Actions: Collect missing info, confirm existing
- Tools Called: verify_caller_identity(), update_lead_info() (if needed)
- Flags Set: verified=true
- Completion: Info confirmed/updated
- Routing: verified=true, qualified=null → QUALIFY
- Result: [PASS/FAIL]

**QUALIFY:**
- Input: verified=true
- Actions: Ask 4 gate questions
- Tools Called: mark_qualification_result(qualified=true)
- Flags Set: qualified=true
- Completion: All 4 gates answered
- Routing: qualified=true → QUOTE
- Result: [PASS/FAIL]

[Continue for each node...]

### Issues Found:
- [Document any issues found]

### Validation Checks:
- [Document validation results]
```

---

## **What Success Looks Like**

After tracing all 13 scenarios:

- **All happy paths work** (Scenarios 1-3) → **End with BOOKED APPOINTMENT**
- **Objections are handled** (Scenarios 4-6) → **Route to BOOK after resolution**
- **Edge cases route correctly** (Scenarios 7-10) → **Still attempt BOOK when appropriate**
- **Failure modes degrade gracefully** (Scenarios 11-13) → **Fallback to manual booking if needed**
- **All configurations validated** (valid_contexts, step_criteria, instructions, flags)
- **CRITICAL: Every qualified, quoted lead gets a BOOK attempt before GOODBYE**

**Then you're ready for real-world testing with live calls!** 🚀

---

## **TL;DR**

**Purpose:**
This document provides a comprehensive trace testing framework for validating conversation flow, routing logic, tool usage, and flag management across 13 different scenarios.

**Golden Route (Outbound Call):**
GREET → VERIFY → QUALIFY → QUOTE → ANSWER → **BOOK** → GOODBYE

**Critical Goal:** Every qualified, quoted lead should get a BOOK attempt before ending the conversation.

**Process:**
1. Trace these 13 scenarios using current configurations
2. Document any issues found (especially booking attempts)
3. Validate that configurations are working correctly
4. Ensure all paths attempt booking when appropriate
5. Fix critical issues before live testing
6. Deploy and test with real calls

**This is regression testing for conversation design with booking as the primary success metric.**

Ready to start tracing! 🎯
