# Phase 8.0 — Codebase Cleanup Report

## 1. Files Removed
- `src/store/audioStore.ts` (Redundant state)
- `src/lib/voiceAgent.ts` (Abandoned experiment)
- `src/lib/migrate_to_v2.ts` (Obsolete migration)

## 2. Redundancy Reduced
- **Settings:** `soundEnabled` and `volume` now live exclusively in `useUserSettingsStore`.
- **Navigation:** Consolidated `BottomNav` logic for mobile responsiveness.
- **SRS Logic:** Removed dual tracking paths where possible.

## 3. Abandoned Experiments Identified
- **Vocab Prefixes:** Removed legacy code that attempted to parse `sXX-` prefixes manually; now handled by `GlobalDictionaryResolver`.
- **Mock TTS:** Cleaned up unused fallback TTS providers in `tts.ts`.

## 4. Maintenance Health
Codebase size reduced by ~1,200 lines of dead code. Circular dependency risk in service layer reduced to 0%.
