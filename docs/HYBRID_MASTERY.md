# Hybrid Mastery Specification

This document is the authoritative design for the Hybrid Mastery V2 architecture.

## 1. Architectural Split
- **Global Dictionary:** Vocabulary is tracked globally. A user learns "grazie" once.
- **Local Curriculum:** Phrases and Sentences are scenario-bound to provide situational context.

## 2. Global Progress (FSRS-Lite)
Spaced repetition operates exclusively on global vocabulary IDs. 

### Vocabulary Lifecycle & Mastery States
1. **New:** Exists in dictionary, never encountered.
2. **Learning:** In a current lesson, `streak < 3`.
3. **Learned:** Passed initial lesson, entered multi-day spaced repetition.
4. **Advanced:** Review interval `> 7 days`.
5. **Mastered:** Review interval `> 30 days`. Stored in long-term memory.
6. **Lapsed:** Failed a review. Interval slashed to 20%.
7. **Relearning:** Must pass 2 consecutive micro-steps to return to `Learned`.

## 3. Daily Review
- **Queue:** Prioritizes `RELEARNING` -> `LEARNING` (Interday) -> `REVIEW_DUE`.
- **Cap:** Maximum 100 items per day.
- **UI:** A dedicated global flashcard screen accessible from the dashboard.

## 4. Conversation Reinforcement
- Reading and successfully completing a conversation provides **Implicit Review Credit**.
- If `word_chiave` is due for review, encountering it naturally in a scenario conversation pushes its SRS interval forward, acting as a "Pass" without requiring a flashcard.

## 5. Phrase & Sentence Strategy
- **Sentences:** Discarded immediately after scenario completion. No SRS. Used purely for reading comprehension.
- **Phrases:** 95% scenario-bound. A tiny subset (e.g., "Va bene") may be elevated to a **Core Phrase Strategy** using global IDs if redundancy becomes overwhelming, but default behavior is local short-term mastery (`score >= 85`).

## 6. Future FSRS Integration
The custom FSRS-Lite algorithm handles difficulty automatically via binary Pass/Fail inputs, adjusting the `ease_factor` up by `0.1` for success and down by `0.2` for lapses, eliminating the need for user self-reporting.
