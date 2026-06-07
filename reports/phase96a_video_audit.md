# Phase 9.6a: Video-Based UX Audit

## 1. What does the learner actually experience?
The learner enters a distraction-free, fullscreen environment. They are met with a "Start Lesson" prompt. Upon entering, they hear audio immediately and are challenged to identify the meaning before seeing the answer. As they progress, they see real-time updates to their conversation readiness.

## 2. What feels confusing?
- **Previous:** Clicking "Continue" on errors was possible without reading.
- **Fixed:** `FeedbackOverlay` now forces an extra click and clearly labels the correct answer.

## 3. What feels broken?
- **Previous:** Audio was silent on the first interaction due to browser restrictions.
- **Fixed:** Added "Inizia Lezione" button to ensure a user gesture before audio starts.

## 4. What feels unfinished?
- The "Safety Floor" filter is implemented in logic but needs better visualization (e.g., showing which items were skipped because they are mastered).
- Lack of animations (Transition between exercises is instantaneous).

## 5. What feels professional?
- Chronological ordering makes the vocabulary feel relevant to the goal (Finding the Entrance).
- 100% keyboard support.
- Real-time readiness percentages.

## 6. What prevents daily usage?
- **Resolved:** Session duration. Reducing the session to 25 exercises (5-8 minutes) makes the app a sustainable daily habit.
