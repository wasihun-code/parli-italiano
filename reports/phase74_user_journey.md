# Phase 7.4 — User Journey Test

## Scenario: Accommodation / Apartment Key Pickup

### 1. Vocabulary Phase
- The user launches the Vocabulary Mini-Lesson.
- The flashcard for "chiave" appears.
- **V2 Validation:** Directly beneath the word "chiave", a grey `✨ NEW` `MasteryBadge` is visible.
- The user completes 3 correct attempts. The V1 star is awarded.
- Behind the scenes, the event is captured, pushing the global mastery state to `LEARNED`.
- If the user restarts the lesson, the badge now reads `✓ LEARNED` in green.

### 2. Phrases & Sentences Phases
- The user progresses through phrase and sentence lessons.
- **V2 Validation:** No mastery badges appear here, as Phase 6.6 dictated that phrases and sentences remain strictly scenario-bound and do not utilize global SRS.

### 3. Conversations Phase
- The user completes the branching dialogue.
- **V2 Validation:** (Preparation for Phase 7.6) The conversation behaves normally. No UI changes exist here.

### 4. Profile Screen
- The user visits their Profile.
- **V2 Validation:** The UI design (from the Frontend Agent report) proposes displaying "Total Vocabulary Mastered", giving the user credit for "chiave" globally.

### 5. Admin Panel
- The admin views the Hybrid Mastery Dashboard.
- **V2 Validation:** The dashboard reveals that the Global Dictionary size is 5,297 and tracks the average retention rate of the user base.

## Conclusion
The data flows correctly from the user's interaction into the V2 tracking system, and the new state is successfully projected back onto the screen without altering the core gameplay loop.
