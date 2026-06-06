# Phase 7.5 — User Journey Test

## 1. Fresh User
**Scenario:** Apartment Key Pickup
- **Initial State:** 34 vocabulary items. Global Dictionary is empty for this user.
- **Experience:** The Adaptation Engine detects 34 `UNKNOWN` items. No words are skipped. The user studies all 34 flashcards.
- **Result:** The user establishes baseline mastery for words like "grazie", "sì", and "chiave".

## 2. Intermediate User
**Scenario:** Hotel Check-In
- **Initial State:** Has completed "Apartment Key Pickup". Knows 34 basic words.
- **Experience:** The user opens Hotel Check-In. The Adaptation Engine analyzes the 40 vocabulary items. It finds 15 words overlapping with the previous scenario (e.g., "grazie", "sì", "buongiorno").
- **UI Interaction:** The "Transparency UI" (Boost Screen) appears: *"15 words already mastered!"*.
- **Learning:** The user only drills the 25 truly `UNKNOWN` words (e.g., "prenotazione", "passaporto").
- **Result:** Flashcard fatigue is reduced by 37.5%.

## 3. Advanced User
**Scenario:** Hostel Dorm
- **Initial State:** Has completed 10 scenarios. Knows 400 basic words.
- **Experience:** The user opens Hostel Dorm. The Adaptation Engine analyzes the 30 vocabulary items. It finds that 29 words are already `MASTERED`.
- **Safety Floor Activation:** The strict adaptation rule would filter out 29 words, leaving only 1 flashcard. The Safety Floor activates, grabbing the 1 most recently lapsed or lowest-mastery word to bring the visible deck up to 2 items.
- **UI Interaction:** The Boost Screen appears: *"28 words already mastered!"*
- **Learning:** The user studies the 1 truly new word and completes 1 "Contextual Refresh" warm-up exercise.
- **Result:** The user bypasses 93% of the flashcards, immediately jumping into the Phrases and Conversation phases where their true ability is challenged.
