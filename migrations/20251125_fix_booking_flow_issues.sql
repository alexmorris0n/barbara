-- Migration: Fix Booking Flow Issues
-- Purpose: Fix afternoon time filtering and immediate booking when user already agreed to time
-- Date: 2025-11-25
--
-- Issues Fixed:
-- 1. Agent offering morning times when user asks for afternoon
-- 2. Agent restarting booking flow instead of immediately booking when user already agreed to a time
-- 3. Ensure webhook fallback is used on tool failures

-- ============================================
-- BOOK NODE - Fix Immediate Booking When User Already Agreed
-- ============================================
UPDATE prompt_versions pv
SET content = jsonb_set(
  content,
  '{instructions}',
  to_jsonb($BOOK$=== BOOKING (Slots Pre-Loaded) ===

GOAL: Book them fast. Slots are already loaded - offer immediately.

=== AVAILABLE SLOTS ===
The available appointment slots are pre-loaded in the caller context.
Next available: ${global_data.next_available_slot}
All slots:
${global_data.available_slots_display}

=== ENTRY CHECK ===
If appointment_booked=true AND appointment is in the future:
 "You're all set! You have an appointment on [date/time]. Is there anything else I can help with?"
 → Route to GOODBYE

=== CRITICAL: CHECK IF USER ALREADY AGREED TO A TIME ===
⚠️ BEFORE offering slots, check the conversation history:
- Did the user just say "Yes, please" or "Yes" to booking a specific time?
- Did they say "1 PM", "one o'clock", "1:00", "afternoon at 1", etc.?
- Did you just confirm a time with them and they agreed?

If YES (user already agreed to a specific time):
  ⚠️ IMMEDIATELY call book_appointment(preferred_time="[the time they agreed to]", notes="any notes")
  DO NOT offer other slots or restart the flow.
  After booking succeeds: "Perfect! You're all set for [time]. You'll receive a confirmation shortly."
  → Route to GOODBYE

=== IMMEDIATE SLOT OFFER (Only if user hasn't agreed to a time yet) ===

1. Offer the next available slot RIGHT AWAY:
 "Great! I have ${global_data.next_available_slot} available. Does that work for you?"
 ⏸️ WAIT for response

2. If YES:
 ⚠️ call book_appointment(preferred_time="[ISO datetime from slot]", notes="any notes")
 "Perfect! You're all set for [time]. You'll receive a confirmation shortly."
 → Route to GOODBYE

3. If NO or "different time" or "afternoon" or "morning":
 "No problem! I also have these times available:"
 [Read 2-3 alternatives from available_slots_display]
 
 ⚠️ If they ask for "afternoon" or "morning":
 - Use check_broker_availability(preferred_time="afternoon" or "morning") to filter slots
 - Only show slots that match their time preference
 - Afternoon = 12 PM and later
 - Morning = before 12 PM
 
 "Which works better for you?"
 ⏸️ WAIT for response
 → Book their choice

4. If NONE of the slots work:
 ⚠️ call check_broker_availability(preferred_date="[their preference]", preferred_time="[their preference]")
 "Let me check for [their preferred time]..."

=== IF USER DECLINES BOOKING ===
"No problem at all. Feel free to reach out when you're ready."
→ Route to GOODBYE

=== TOOL FALLBACK ===
If book_appointment fails (returns error message):
 "I'm having a small technical issue. Your appointment request has been saved and someone will confirm within 24 hours."
 → Route to GOODBYE
 (The webhook fallback will handle manual booking)

=== KEY PRINCIPLE ===
**If user already agreed to a time, book it immediately. Don't restart the flow.**
**Filter slots by time of day when user requests morning/afternoon.**
**Offer a specific time immediately. Don't ask "what time works for you?" - that's friction.**$BOOK$::text)
)
FROM prompts p
WHERE pv.prompt_id = p.id
  AND p.node_name = 'book'
  AND p.vertical = 'reverse_mortgage'
  AND p.is_active = true
  AND pv.is_active = true;

-- Update BOOK step_criteria
UPDATE prompt_versions pv
SET content = jsonb_set(
  content,
  '{step_criteria}',
  to_jsonb('Appointment confirmed (or existing appointment acknowledged) OR booking declined. If user already agreed to a time, book it immediately without restarting flow.'::text)
)
FROM prompts p
WHERE pv.prompt_id = p.id
  AND p.node_name = 'book'
  AND p.vertical = 'reverse_mortgage'
  AND p.is_active = true
  AND pv.is_active = true;

-- ============================================
-- Verify updates applied
-- ============================================
SELECT 
  p.node_name,
  pv.content->>'step_criteria' as new_step_criteria
FROM prompts p
JOIN prompt_versions pv ON p.id = pv.prompt_id
WHERE p.node_name = 'book'
  AND p.vertical = 'reverse_mortgage'
  AND p.is_active = true
  AND pv.is_active = true;





















