# Data Migration Strategy

Migrating existing users to the Hybrid Mastery architecture requires careful handling to prevent progress loss.

## Migration Rules

1. **Mapping:** The factory will generate a `legacy_to_global_map.json` file. It will map every old ID (`s22-v1`) to its corresponding new Global ID (`word_grazie`).
2. **Execution:** The migration runs completely client-side in the React application immediately after a version update.
3. **Merging Streaks (Max Rule):** If a user learned "grazie" in Scenario 1 (`correctStreak` = 3) but failed it in Scenario 2 (`correctStreak` = 0), the migration script will always assign the **maximum** `correctStreak` to the new `word_grazie` entry.
4. **Interval Calculation:** For merged items, the `due_at` timestamp will be set to `now + 1 day` to force an initial review in the new FSRS-Lite system, initializing their ease factors safely.
5. **Scenario Progress:** The high-level `vocabularyCompleted` flag in `progressStore.ts` will be dropped. Scenario conversation locks will now dynamically read the new global state. If a user previously had access to a conversation, but the dynamic check fails (because they forgot a word globally), they must review the word to regain access.

## Fallback & Rollback Rules

1. **Fallback:** If an old ID (`s22-v99`) is not found in `legacy_to_global_map.json` (e.g., it was deleted from the curriculum), the progress record is safely dropped. No error is thrown.
2. **Rollback:** Before the migration script mutates `srs_items`, it copies the entire old state into a new Dexie table `srs_items_v1_backup`. If the user complains of massive progress loss, an Admin function can restore this backup table.
