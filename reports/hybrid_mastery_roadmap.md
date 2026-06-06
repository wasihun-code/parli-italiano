# Final Implementation Roadmap

This document serves as the master execution plan for the engineering team to build Hybrid Mastery V2.

## Phase 7.1: Global Dictionary (Factory-Side)
- **Objectives:** Generate the Global Knowledge Graph without touching the frontend.
- **Deliverables:** `linguistic_extractor.py` updates, `dictionary_overrides.json`, `global_dictionary.json`, `scenario_vocab_mapping.json`.
- **Dependencies:** Factory V2 completion.
- **Complexity:** Medium
- **Success Criteria:** Factory can generate the new dictionaries and still pass all integrity audits.

## Phase 7.2: Global Progress (Client Data Layer)
- **Objectives:** Implement the FSRS-Lite tracking stores and database schemas.
- **Deliverables:** `srsStore.ts` (FSRS math), `db.ts` (Dexie global schema).
- **Dependencies:** Phase 7.1.
- **Complexity:** High
- **Success Criteria:** Store logic tests pass (e.g., correctly calculating `due_at` based on binary correct/incorrect inputs).

## Phase 7.3: Review Queue (Client UI)
- **Objectives:** Build the Daily Review feature.
- **Deliverables:** `DailyReviewScreen.tsx`, updated `HomeScreen.tsx` metrics.
- **Dependencies:** Phase 7.2.
- **Complexity:** Low
- **Success Criteria:** User can clear a queue of 100 due items and see their "Vocabulary Size" metric increase.

## Phase 7.4: Scenario Adaptation (Client UI)
- **Objectives:** Blend global knowledge into local scenarios to eliminate flashcard fatigue.
- **Deliverables:** Updates to `VocabularyTrainingScreen.tsx` to hide `LEARNED` global IDs.
- **Dependencies:** Phase 7.2.
- **Complexity:** Medium
- **Success Criteria:** A scenario with 100% known vocabulary auto-completes its flashcard phase.

## Phase 7.5: Conversation Reinforcement (Client UI)
- **Objectives:** Implement implicit learning.
- **Deliverables:** Updates to `ScriptedConversationScreen.tsx` to dispatch SRS updates for words encountered in the dialogue.
- **Dependencies:** Phase 7.2.
- **Complexity:** Medium
- **Success Criteria:** Completing a conversation pushes the `due_at` date forward for all global vocabulary used in it.

## Phase 7.6: Admin Integration
- **Objectives:** Operationalize the new metrics.
- **Deliverables:** Updates to `AdminDashboard.tsx`, `AnalyticsDashboard.tsx`, and `UserDetailView.tsx`.
- **Dependencies:** Phase 7.2.
- **Complexity:** Low
- **Success Criteria:** Admins can view "Most Lapsed Words" and "Global Dictionary Coverage."

## Phase 7.7: Hybrid Mastery Certification & Rollout
- **Objectives:** Safely migrate existing users.
- **Deliverables:** `migrate_to_v2.ts`, Feature Flags.
- **Dependencies:** Phases 7.1 - 7.6.
- **Complexity:** Critical
- **Success Criteria:** 100% of existing user progress is mapped to the Global Dictionary without data loss.
