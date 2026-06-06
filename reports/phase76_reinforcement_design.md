# Phase 7.6 — Reinforcement Design

## 1. Objective
Enable Conversations to act as "Implicit Review" engines, awarding mastery credit to vocabulary items encountered in context.

## 2. Evidence Weighting

### Exercise Evidence (Flashcards)
- **Weight:** 1.0 (Standard)
- **Rationale:** Flashcards test isolated, out-of-context retrieval. It is the baseline evidence of memory retention.

### Conversation Evidence (Implicit Review)
- **Weight:** 2.0 (High)
- **Rationale:** Using or understanding a word within a branching, real-time dialogue requires higher cognitive load. The user must parse host intent (passive recognition), filter distractors (contextual comprehension), and select the right path (active production). Therefore, succeeding in a conversation is superior evidence of mastery compared to an isolated flashcard.

## 3. Conversation Outcome Rules

When a conversation is completed, the engine calculates the overall "Conversation Success Score" based on the number of mistakes made across all nodes.

| Outcome | Mistake Threshold | Reinforcement Award | SRS Equivalent |
| :--- | :--- | :--- | :--- |
| **Perfect** | 0 Mistakes | 100% | `EASY` (Maximum interval extension) |
| **Minor Mistakes** | 1-2 Mistakes | 75% | `GOOD` (Standard interval extension) |
| **Repeated Mistakes** | 3+ Mistakes | 25% | `HARD` (Minimal extension, avoids lapse) |
| **Abandoned** | Did not reach END | 0% | No state change |

## 4. Double Counting Prevention
If a word (e.g., `word_chiave`) appears 5 times in a single dialogue tree, it is only reinforced **once** per conversation completion. The payload sent to `ConversationReinforcementService` must be a `Set` of unique Global IDs encountered.
