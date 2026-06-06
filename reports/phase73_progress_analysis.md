# Phase 7.3 — Progress Analysis

## 1. Current Schema Analysis
- `db.ts` tracks scenario-specific entities (`scenario_vocabulary`, `srs_items`).
- `srsStore.ts` persists spaced repetition state to local storage via Zustand, using legacy local keys (e.g., `s22-v1`).
- `progressStore.ts` tracks scenario completion (booleans like `vocabularyCompleted`).

## 2. Current Progress Flow
1. User enters `VocabularyTrainingScreen`.
2. Items are registered in `srsStore` using local IDs.
3. User answers are logged via `recordAnswer`, updating local streaks.
4. When all items reach a streak of 3, `progressStore` flags `vocabularyCompleted: true`.

## 3. Integration Points
- **V1/V2 Coexistence:** V1 progress must remain untouched. V2 progress (Global Tracking) must be hooked into the existing `srsStore` actions.
- **Event Capture:** The `recordAnswer` and `registerItem` functions in `srsStore.ts` are the optimal integration points. They must dispatch events to a new `globalProgressService.ts` asynchronously.
- **Scenario Unlock Logic:** `progressStore.ts` must eventually transition to dynamic computed properties based on global mastery, but for Phase 7.3, it remains static to prevent UI changes.

## 4. Migration Risks
- **ID Collisions:** If legacy IDs mix with global IDs, progress may be corrupted.
- **Max Streak Merge:** Failing to merge legacy streaks correctly during migration will result in data loss.
- **Storage Limits:** Running parallel tracking increases local storage footprint; `global_progress` should live in Dexie.
