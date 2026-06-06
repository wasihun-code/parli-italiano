# Phase 7.3 — Migration Plan

## 1. Objectives
- Preserve 100% of existing user progress from `srsStore` local storage.
- Safely initialize new Dexie `global_progress` tables.
- Protect against ID collisions and duplicated tracking issues.

## 2. Migration Execution (`migrate_to_v2.ts`)
The migration is a client-side process triggered after a version update.
1. It fetches `legacy_to_global_map.json` (or uses a fallback normalization generator for V1 legacy keys).
2. It iterates through all `vocabulary` items in the Zustand `srsStore`.
3. It applies the **Max Streak Merge Rule**: If `s22-v1` has a streak of 3, and `s50-v5` has a streak of 0, the resulting `word_grazie` will inherit the streak of 3.
4. Total attempts are aggregated across all instances.
5. The unified record is written to `global_progress` in Dexie.

## 3. Rollback Support
Because this phase mandates no UI changes, the `srsStore` is NOT deleted or pruned during migration. The old `sXX-vYY` records remain perfectly intact in local storage. If the global progress migration fails, the app falls back seamlessly to the V1 scenario mastery logic with zero data loss.

## 4. Phase 7.3 Limitations
This migration creates the initial global tracking records, but does not yet *consume* them to enforce scenario unlocking. That will occur in Phase 7.4.
