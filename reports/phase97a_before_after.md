# Phase 9.7a: Before and After (Pedagogical Repair)

## 1. Goal
Transform a technically functional prototype into a pedagogically effective language-learning experience.

## 2. Defects & Resolutions

### Defect 1: Lesson Unlock Flow
*   **Before:** `completeMiniLesson` hardcoded `scenarioId` as `22`. The unlock check assumed a missing criteria meant the lesson remained locked forever.
*   **After:** Dynamic routing via `useParams()` accurately extracts `scenarioId`. The unlock check cascades to `complete_previous`, allowing progression.
*   **Proof:** See `reports/phase97a_unlock_validation.md`.

### Defect 2: Universal Feedback
*   **Before:** The `Listen` exercise had a floating "Reveal" state that occasionally bypassed standard error validation.
*   **After:** A centralized `FeedbackOverlay` dictates progression. Every single submission invokes `onComplete` resulting in a unified, unavoidable feedback loop.

### Defect 3 & 8: Meaningless Progress
*   **Before:** The footer measured absolute scenario mastery (150+ items), so 25 correct answers yielded ~0.5% progress. 
*   **After:** The footer calculates relative mastery for the *active lesson scope* (`Lesson Mastery`) alongside the global `Scenario Readiness`. Growth is immediate and tangible.

### Defect 4: Sentence Training Rebalance
*   **Before:** `SessionGenerator.ts` passively sliced the first 25 chronologically sorted items, resulting in sessions composed 100% of vocabulary.
*   **After:** Explicit categorical distribution limits vocabulary to 50% max, forcing 30% of the session to train sentences.

### Defect 5: Scenario Immersion
*   **Before:** A generic entry screen ("Situazione: Arrivo al Palazzo") decoupled from the actual mini-lesson goal.
*   **After:** A dynamic context banner and SMS-style preview prime the user for the specific conversational goal (e.g., "Using the Intercom") prior to commencement.

### Defect 6: Layout & Spacing
*   **Before:** Restricted `maxWidth: 800px` created a tiny, textbook-style card surrounded by whitespace.
*   **After:** The UI expands to `maxWidth: 1000px` with `flex: 1`. Typography is massive (`48px`), resembling premium consumer applications.

### Defect 7: Audio as a Learning Tool
*   **Before:** Audio played automatically, but the Italian and English strings were eventually revealed without requiring active listening.
*   **After:** The `Listen` exercise acts as an MCQ prompt. The user must recognize the spoken Italian and choose the corresponding text to proceed.

## 3. Conclusion
The V3 Pilot is no longer just a technical foundation. It is an optimized, active, and rewarding learning loop fully prepared to replace the legacy system in Phase 10.
