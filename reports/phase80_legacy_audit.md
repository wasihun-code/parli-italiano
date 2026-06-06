# Phase 8.0 — Legacy System Audit

This report evaluates the current state of legacy systems in Parla Italiano during the transition to Hybrid Mastery V2.

| System | Technology | Role | Status |
| :--- | :--- | :--- | :--- |
| **`progressStore.ts`** | Zustand/LocalStorage | XP, Streaks, Onboarding | **KEEP** (Critical for metadata) |
| **`srsStore.ts`** | Zustand/LocalStorage | Scenario-bound streaks | **DEPRECATE** (Data redundant with Dexie) |
| **`audioStore.ts`** | Zustand/LocalStorage | soundEnabled, volume | **REMOVE** (Merged into UserSettings) |
| **`migrate_to_v2.ts`** | TypeScript/Script | One-time data bridge | **REMOVE** (Obsolete post-Phase 7) |
| **`voiceAgent.ts`** | TypeScript/Service | Voice interaction experiment | **REMOVE** (Abandoned) |
| **`localStorage` (Large Data)** | Browser API | Storing `srsItems` | **DEPRECATE** (Favoring Dexie) |

## Cleanup Recommendation
1.  **Consolidation:** Move `xp` and `streak` from `progressStore.ts` into a unified `userStateStore.ts`.
2.  **Deprecation:** Stop writing to `srsStore.ts` in Phase 8.1 and rely solely on `GlobalProgressService`.
3.  **Migration Cleanup:** Delete all Phase 1-6 migration artifacts to prevent maintenance confusion.
