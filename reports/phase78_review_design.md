# Phase 7.8 — Review Queue Design

## 1. Architectural Conflict Resolution
The objective of Phase 7.8 requests the ability to review "due phrases" and "due sentences". However, Phase 6.6 (`reports/final_phrase_sentence_mastery_recommendation.md`) strictly concluded:
> "Should phrases have SRS? NO. Should sentences have SRS? ABSOLUTELY NOT. Sentences exist purely for immediate reading comprehension."

To comply with the pedagogical constraints of Hybrid Mastery V2 while fulfilling the requirement to integrate phrases, the architecture is modified as follows:

- **Vocabulary:** Full SRS implementation (Daily Review Queue).
- **Core Phrases:** A small, globally managed set of high-frequency connectors (e.g., "Va bene", "Per favore") will be treated as `vocabulary` and eligible for SRS review.
- **Scenario Phrases & Sentences:** EXCLUDED from the explicit Daily Review Queue.
- **Compromise:** Sentences and scenario-bound phrases will instead be utilized on the "back" of the Vocabulary flashcards to provide context. When reviewing `word_grazie`, the flashcard will display a sentence from a scenario utilizing "grazie", thereby exposing the user to the sentence without forcing a discrete SRS interval on it.

## 2. Queue Sources & Priority
The `ReviewQueueService` will fetch items from IndexedDB `global_progress` that match either:
- `next_review_at <= now` (Overdue)
- `mastery_level == LAPSED` or `RELEARNING` (Broken trace)

**Priority Hierarchy:**
1. `LAPSED` (Must rebuild broken memory immediately)
2. `RELEARNING` (In-session recovery)
3. `DUE` (Standard SRS review)
4. `LEARNING` (Initial inter-day reinforcement)

## 3. Daily Cap Enforcement
The service applies a hard slice (`.slice(0, 100)`) after prioritizing the queue. If a user is absent for 6 months and accrues 1,200 due items, the app will only present the 100 most critical items per day, protecting against burnout.
