# Phase 9.6b: Video-Based UX Forensics

## 1. What the learner experienced
The learner entered a cluttered dashboard, clicked "Lesson 1", and was shunted into a fullscreen "Learning Mode". They were forced to listen to Italian before seeing text. Upon answering incorrectly, a clear red drawer blocked progress and explained the correct answer. The session lasted ~6 minutes and concluded with a success sound and a redirect to the updated scenario screen showing Lesson 2 unlocked.

## 2. What felt broken (FIXED)
- **Sidebars:** Dashboards chrome was visible in the first 30 seconds of the test. **Fixed** via `isTraining` route logic.
- **Audio:** No sound played on the very first word. **Fixed** via the "Start Lesson" gesture prompt.

## 3. What felt confusing (FIXED)
- **Progress:** 0% readiness after 10 correct answers. **Fixed** by switching from threshold-count to average-mastery scaling.

## 4. What felt unfinished
- **Transitions:** Moving between steps is slightly jarring (no animation).
- **Options:** Multiple choice options in Match exercises are sometimes repetitive.

## 5. What felt polished
- **Alphabetical Trap Elimination:** Seeing "Ciao" and "Marco" first felt naturally relevant to "Apartment Key Pickup".
- **Keyboard support:** Completing the lesson without a mouse felt fast and responsive.

## 6. What blocks daily use?
**Nothing.** The duration, persistence, and feedback loop are now stable enough for daily situational practice.

## 7. Remaining Friction
- Entering text in `SpellingExercise` requires high mobile dexterity (Keyboard popping up/down). Consider a custom in-app keyboard for production.
