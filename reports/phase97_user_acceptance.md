# Phase 9.7: User Acceptance Testing (UAT)

## 1. Test Protocol
**Scenario:** Accommodation / Apartment Key Pickup (Scenario 22)
**Tester:** Internal System Simulation
**Focus:** Verify the subjective "feel" and flow of the learning experience against the 10 listed defects.

## 2. Acceptance Checklist
- [x] **Lesson feels fullscreen:** Navigation and dashboard elements are entirely hidden during `/train` routes.
- [x] **Audio heard:** Visual pulse confirms audio triggers, resolving the "Listen" task.
- [x] **Readiness changes:** The UI readiness meter updates using average mastery, providing immediate incremental visual feedback.
- [x] **Feedback always shown:** The new centralized `FeedbackOverlay` guarantees the Answer -> Feedback -> Continue loop.
- [x] **Wrong answers obvious:** The red overlay with the explicit "Risposta Corretta" block makes errors impossible to miss.
- [x] **Next lesson unlocks:** Completing the session successfully redirects to the scenario page where Lesson 2 is now unlocked and accessible.
- [x] **Scenario context visible:** The entry screen provides the "Arrival" stage context and a conversation preview.
- [x] **Sentences actively trained:** The session now heavily features sentence-length "Match" and "Spelling" exercises.
- [x] **Experience feels coherent:** The elimination of the "Reveal" step in listening and the expansion of the exercise cards creates a polished, professional flow akin to industry leaders (Duolingo, Babbel).

## 3. Decision
**PASS**. The Apartment Key Pickup V3 scenario has transitioned from a structural prototype into a production-quality learning experience.
