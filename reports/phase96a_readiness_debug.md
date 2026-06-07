# Phase 9.6a: Readiness Debug Report

## 1. Problem
Readiness meters for Vocab, Phrases, and Sentences remain at 0% throughout the session.

## 2. Root Cause
In `LearningSystemV3PilotScreen.tsx`, the `localMastery` state is initialized as an empty object `{}`. 
While `handleComplete` updates this local state correctly for the *current session*, it never loads the *existing* mastery from the database upon mount.

**Code Audit:**
```typescript
const [localMastery, setLocalMastery] = useState<Record<string, number>>({});
```

The `readiness` calculation in the `useMemo` block depends on `localMastery`. If the user has 300 words to learn, and they complete 1, they have 0.33% mastery, which rounds down to 0% in the current Stat display.

## 3. Fix Strategy
1. **Initialize Mastery:** In the `initPilot` effect, query `db.global_progress` for all item IDs in the scenario and populate the `localMastery` map with their current `mastery_level`.
2. **Normalized Percentage:** Ensure the Stat component handles decimals or rounds up to 1% to provide better visual feedback.
3. **Database Sync:** Confirm `GlobalProgressService.recordAnswer` is correctly writing to IndexedDB (verified in Phase 9.6 audit, but needs re-verification in live UI).

## 4. Conclusion
The issue is one of **Initial State Injection**. The UI is disconnected from the persistence layer's historical data.
