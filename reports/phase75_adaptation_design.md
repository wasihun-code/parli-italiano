# Phase 7.5 — Adaptation Design

## Goal
Eliminate flashcard fatigue by skipping already-mastered vocabulary.

## State Handlers
When constructing the `VocabularyTrainingScreen` and `MiniLessonTrainingScreen` exercise lists, the `curriculumAdaptationService.ts` will fetch the global state for each item.

| State | Action | Visibility | Explanation |
| :--- | :--- | :--- | :--- |
| **UNKNOWN** | Include | **Visible** | User has never seen this word. Needs full pedagogical cycle. |
| **LEARNING** | Include | **Visible** | User is actively building the initial memory trace (`streak < 3`). |
| **LEARNED** | Filter | **Hidden** | User has passed the initial lesson. Transferred to SRS queue. |
| **ADVANCED** | Filter | **Hidden** | Mature SRS item. |
| **MASTERED** | Filter | **Hidden** | Highly mature SRS item (> 30d interval). |
| **LAPSED** | Include | **Visible** | User failed a review. Must rebuild short-term trace. |
| **RELEARNING**| Include | **Visible** | Recovering from a lapse. |

## Explanation of Strategy
- **Visible Items** (UNKNOWN, LEARNING, LAPSED, RELEARNING) form the active flashcard deck. The user must actively drill these until they graduate to `LEARNED`.
- **Hidden Items** (LEARNED, ADVANCED, MASTERED) are excluded from the flashcard deck. They will only reappear contextually in the Conversation phase, or explicitly in the Daily Review queue when their interval expires.
