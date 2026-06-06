# SRS Implementation Plan

The transition to FSRS-Lite will occur over 5 sequential phases.

### Phase 7.1: Global Dictionary
- **Tasks:** Update `linguistic_extractor.py`, generate `global_dictionary.json`, generate `scenario_vocab_mapping`.
- **Dependencies:** None.
- **Risks:** High risk of breaking the build script if JSON schemas mismatch.
- **Success Criteria:** All 116 scenarios successfully extract and map to global IDs without errors.

### Phase 7.2: Global Progress
- **Tasks:** Update Dexie `db.ts` schema. Update `srsStore.ts` to support `LEARNING`, `LEARNED`, `MASTERED` states and `ease_factor`.
- **Dependencies:** Phase 7.1.
- **Risks:** High risk of corrupting existing local user data.
- **Success Criteria:** `migrate_to_v2.ts` runs on app load and correctly maps old progress to new global states.

### Phase 7.3: Review Queue
- **Tasks:** Build `DailyReviewScreen.tsx`. Implement the 100-item prioritization queue algorithm.
- **Dependencies:** Phase 7.2.
- **Risks:** Low. Isolated UI feature.
- **Success Criteria:** Users can successfully execute flashcards that update the global interval timers.

### Phase 7.4: Scenario Adaptation
- **Tasks:** Update `VocabularyTrainingScreen.tsx` to dynamically filter `exerciseIds`.
- **Dependencies:** Phase 7.2.
- **Risks:** Medium. UI might break if a lesson filters to 0 items.
- **Success Criteria:** Scenarios automatically skip known vocabulary.

### Phase 7.5: Conversation Reinforcement
- **Tasks:** Update `ScriptedConversationScreen.tsx`'s `onComplete` handler to push SRS intervals forward.
- **Dependencies:** Phase 7.2.
- **Risks:** Medium. Could trigger massive re-renders if updating 40 global items at once.
- **Success Criteria:** Completing a conversation successfully delays the next review date for its contained vocabulary.
