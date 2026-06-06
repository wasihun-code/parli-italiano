# Hybrid Mastery Implementation Roadmap

Migrating the Parla Italiano platform from Scenario Mastery to Hybrid Mastery is a complex operation spanning the Python generation factory, the React frontend, and the Django backend. This roadmap organizes the implementation into 5 logical phases.

---

## Phase 1: Global Dictionary Infrastructure
**Goal:** Modify the Factory V2 pipeline to extract and generate the Global Dictionary without touching user-facing code.

1.  **Refactor `linguistic_extractor.py`**: Implement the normalization rules to generate `word_` and `concept_` IDs.
2.  **Override Support**: Create `dictionary_overrides.json` to handle the ~400 identified homonyms (e.g., `concept_floor_piano`).
3.  **Schema Updates**: Update the Dexie `db.ts` to include `global_dictionary` and `scenario_vocab_mapping` (increment `SEED_VERSION`).
4.  **Factory Output**: Ensure `build_and_certify_scenario.py` produces the new mapping files seamlessly.
*   **Risk:** Medium.
*   **Effort:** 3-5 days.

---

## Phase 2: The SRS Engine Overhaul
**Goal:** Rip out the basic streak system and implement the FSRS-Lite (Custom Hybrid) spaced repetition algorithm.

1.  **Refactor `srsStore.ts`**: Implement the state machine (`NEW`, `LEARNING`, `LEARNED`, `LAPSED`, `MASTERED`).
2.  **Implement Algorithm**: Code the ease factor, interval calculation, and fuzzing math.
3.  **Migration Script (`migrate_to_v2.ts`)**: Write the critical script that maps existing user progress from `sXX-vYY` to the new `word_` IDs, preserving their highest historical streak.
*   **Risk:** High. (Risk of losing user data if the migration script fails).
*   **Effort:** 4-7 days.

---

## Phase 3: The Daily Review Queue
**Goal:** Build the UI for users to complete their spaced repetition reviews globally.

1.  **UI Components**: Create `DailyReviewScreen.tsx`.
2.  **Queue Logic**: Build the selector that pulls `REVIEW_DUE` and `RELEARNING` items from the `srsStore`, capped at 100/day.
3.  **Dashboard Integration**: Update the Home Screen to display "Reviews Due" and the "Global Vocabulary Size".
*   **Risk:** Low.
*   **Effort:** 3-4 days.

---

## Phase 4: Scenario Adaptation
**Goal:** Connect the Global Knowledge Graph back to the individual scenarios to eliminate flashcard fatigue.

1.  **Dynamic Filtering**: Update `VocabularyTrainingScreen.tsx` to read the `scenario_vocab_mapping` and filter out any IDs where `globalStore[id].learned === true`.
2.  **Auto-Completion Logic**: Ensure scenarios properly unlock the Conversation phase even if 100% of the vocabulary lesson was skipped because it was already known.
3.  **UX Polish**: Add the "X words already known!" notification toast.
*   **Risk:** Medium. (Edge cases in React rendering if a lesson is instantly completed).
*   **Effort:** 3-5 days.

---

## Phase 5: Admin Integration & Analytics
**Goal:** Bring the Admin Panel up to date with the new architecture.

1.  **Global Dictionary Viewer**: Add a tab in the Admin Panel to browse the full `global_dictionary`.
2.  **User Metrics**: Update the User Detail view to show SRS retention rates and true vocabulary size.
3.  **Django Backend**: Create the models for `UserSrsProgress` and `ReviewHistory`, and wire up the sync endpoints to back up the new Zustand store.
*   **Risk:** Low.
*   **Effort:** 3-4 days.

---

**Total Estimated Effort:** 16-25 Days.
**Overall Migration Complexity:** HIGH, but highly modularized to ensure safety.
