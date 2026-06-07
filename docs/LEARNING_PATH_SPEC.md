# Learning Path Specification

This document defines the canonical logic for the Learning System V3 Path Generator. It ensures that the transition from static JSON artifacts to a dynamic, adaptive learning experience is deterministic and pedagogically sound.

## SECTION 1: Path Generation Principles

1.  **Deterministic Generation:** Given the same Input State (Scenario ID + User Mastery + Review Queue), the generated sequence of exercises MUST be identical across all runs.
2.  **Mastery-Aware Adaptation:** The generator filters and prioritizes items based on the user's global mastery level, reducing redundancy for known terms.
3.  **Conversation-First Design:** Exercise ordering is determined by the chronological appearance of tokens in the `conversations.json`, not alphabetical order.
4.  **Semantic Progression:** Items are grouped by situational relevance within the path.
5.  **No Curriculum Mutation:** The generator reads but NEVER modifies the source JSON artifacts or IndexedDB schemas.

## SECTION 2: Vocabulary Flow

### UNKNOWN WORD (State: UNKNOWN or LEARNING)
A new word must pass through the following sequence:
1.  **Listen:** Initial exposure (Audio + Text).
2.  **Listen & Choose:** Recognition (Audio -> EN).
3.  **Match:** Recognition (EN -> IT).
4.  **Build Sentence:** Recall (Scrambled context).
5.  **Recall:** Active recall (Fill-in-the-blank).
6.  **Dictation:** Production (Audio -> Typed IT).
7.  **Speaking:** Production (Oral).
8.  **Conversation:** Situational Application.
9.  **Review Queue:** Long-term maintenance.

### MASTERED WORD (State: ADVANCED or MASTERED)
To minimize friction, mastered words skip recognition phases:
1.  **Dictation:** Accuracy check.
2.  **Speaking:** Fluency check.
3.  **Conversation:** Situational Application.

**Transition Rules:**
- Failure at any step moves the item back exactly one phase in the sequence (e.g., failure at Recall moves back to Build Sentence).
- Three consecutive successes in Recognition move the item to Recall.

## SECTION 3: Phrase Flow

### UNKNOWN PHRASE
1.  **Reading:** Visual exposure.
2.  **Listen:** Auditory exposure.
3.  **Build Sentence:** Syntax assembly.
4.  **Recall:** Contextual recall.
5.  **Dictation:** Structural accuracy.
6.  **Speaking:** Oral fluency.
7.  **Conversation:** Application.

### MASTERED PHRASE
1.  **Speaking:** Verification.
2.  **Conversation:** Application.

## SECTION 4: Sentence Flow

### UNKNOWN SENTENCE
1.  **Reading:** Comprehension.
2.  **Listen:** Prosody recognition.
3.  **Assembly:** Scrambled construction.
4.  **Recall:** Cloze/Gap fill.
5.  **Dictation:** Transcription.
6.  **Speaking:** Performance.
7.  **Conversation:** Situational use.

### MASTERED SENTENCE
1.  **Speaking:** Verification.
2.  **Conversation:** Application.

## SECTION 5: Conversation Flow

-   **Conversation Readiness:** A conversation path is unlocked ONLY when 80% of the constituent vocabulary and 100% of required phrases have reached the "Production" phase.
-   **Entry Rules:** The host always starts.
-   **Failure Rules:** If a learner makes 3 mistakes in a conversation, the path terminates and triggers a "Recovery Review" of the specific failed items.
-   **Recovery Rules:** Recovery Review presents one "Recall" exercise for each failed item before allowing a conversation restart.
-   **Mastery Rules:** Completing a conversation grants implicit +0.5 Mastery score to all words used.

## SECTION 6: Adaptation Rules

-   **0% Mastery:** Full sequence for all items. Lesson size restricted to 10 new items max.
-   **25% Mastery:** Introduction of "Accelerated Recall" (skipping Listen & Choose if Match is passed first try).
-   **50% Mastery:** Vocabulary "Safety Floor" of 5 items. Mastered items appear only in Production roles.
-   **75% Mastery:** "Review-Heavy" path. Generator prioritizes Lapsed items from other scenarios that appear in this conversation.
-   **100% Mastery:** "Conversation-Only" path. User goes straight to dialogue with Production-level checks on key terms.

## SECTION 7: Determinism Rules

The Path Generator is a pure function of its inputs:
`f(ScenarioID, GlobalMasteryMap, ReviewQueue) -> OrderedExerciseList`

-   No `Math.random()` allowed unless seeded by ScenarioID + UserID.
-   Item sorting must follow a stable algorithm (e.g., Conversation Turn Index -> Item ID).
-   The number of exercises generated for a specific state must be constant.
