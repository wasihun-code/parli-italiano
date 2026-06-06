# Implementation Roadmap: Hybrid Mastery V2

## Phase 7.2: Global Dictionary Infrastructure
- **Objectives:** Generate the foundational Global Knowledge Graph.
- **Deliverables:** Refactored `linguistic_extractor.py`, `global_dictionary.json`, `scenario_vocab_mapping.json`, `dictionary_overrides.json`.
- **Dependencies:** None.
- **Risks:** Breaking existing scenario loading if mapping schemas conflict.
- **Success Criteria:** 100% Round-trip validation passes on all 116 scenarios.

## Phase 7.3: Global Progress Tracking
- **Objectives:** Refactor the client-side database and state management to track global IDs.
- **Deliverables:** Updated `db.ts` (Dexie), updated `srsStore.ts`, `migrate_to_v2.ts`.
- **Dependencies:** Phase 7.2.
- **Risks:** Irreversible loss of user data during IndexedDB migration.
- **Success Criteria:** User streaks safely merged using the "Max Streak" rule.

## Phase 7.4: Scenario Adaptation
- **Objectives:** Connect scenario mini-lessons to the global store to eliminate flashcard fatigue.
- **Deliverables:** `VocabularyTrainingScreen.tsx` updates (dynamic filtering and auto-completion).
- **Dependencies:** Phase 7.3.
- **Risks:** React render loops or out-of-bounds crashes when exercise lists empty out.
- **Success Criteria:** Scenarios silently skip globally known words.

## Phase 7.5: Review Queue
- **Objectives:** Build a dedicated, global spaced-repetition interface.
- **Deliverables:** `DailyReviewScreen.tsx`, queue prioritization algorithm (Lapsed -> Due).
- **Dependencies:** Phase 7.3.
- **Risks:** Low UI risk.
- **Success Criteria:** Users can clear up to 100 global reviews per day outside of any specific scenario.

## Phase 7.6: Conversation Reinforcement
- **Objectives:** Implement implicit learning credit.
- **Deliverables:** `ScriptedConversationScreen.tsx` updates.
- **Dependencies:** Phase 7.3.
- **Risks:** Main thread blocking during bulk SRS dispatch.
- **Success Criteria:** Completing a conversation pushes `due_at` timers forward for contained vocabulary.

## Phase 7.7: Admin Integration
- **Objectives:** Expose new mastery metrics to operations staff.
- **Deliverables:** Admin Analytics updates, Global Dictionary Viewer component.
- **Dependencies:** Phases 7.2, 7.3.
- **Risks:** Minimal.
- **Success Criteria:** Admin panel accurately tracks "Vocabulary Size" and "Lapse Rates".

## Phase 7.8: Hybrid Mastery Certification
- **Objectives:** Final systemic QA and deployment strategy.
- **Deliverables:** `hybrid_mastery_audit.py`, Feature Flag wrappers, final Global Certification run.
- **Dependencies:** All previous phases.
- **Risks:** Critical release risk.
- **Success Criteria:** The entire platform builds, certifies, and operates flawlessly under the V2 architecture.
