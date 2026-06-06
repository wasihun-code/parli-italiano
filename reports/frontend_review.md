# Frontend Review: Global Progress Tracking Integration (Phase 7.3)

## 1. Overview
This report outlines the strategy for capturing learning events (exposure, correct, and incorrect answers) and routing them to the new `globalProgressService.ts`. The goal is to establish a unified global progress system while preserving existing scenario-based mastery and UI behavior.

## 2. Learning Event Definitions
Standardized events to be captured across all learning activities:

| Event Type | Trigger | Data Captured |
|:---|:---|:---|
| **EXPOSURE** | Item is first presented in a training exercise or conversation. | `itemId`, `timestamp`, `scenarioId`, `activityType` |
| **CORRECT** | User provides a correct or nearly correct answer. | `itemId`, `timestamp`, `scenarioId`, `activityType`, `responseTime` |
| **INCORRECT** | User provides an incorrect answer. | `itemId`, `timestamp`, `scenarioId`, `activityType` |

## 3. Global Progress Service Design
The `globalProgressService.ts` will act as a central orchestrator, decoupling the UI from specific store implementations and ensuring data consistency across multiple targets (Zustand stores, Dexie, and Analytics).

### Interface Sketch
```typescript
export interface ActivityMetadata {
  scenarioId: number;
  activityType: 'vocabulary' | 'phrase' | 'sentence' | 'review' | 'conversation';
  itemType: 'vocabulary' | 'phrase' | 'sentence';
}

export const globalProgressService = {
  /**
   * Primary entry point for all learning events.
   */
  async recordActivity(
    itemId: string,
    result: 'exposure' | 'correct' | 'incorrect',
    metadata: ActivityMetadata
  ): Promise<void> {
    // 1. Map legacy ID to Global ID if applicable
    const globalId = this.mapToGlobalId(itemId);

    // 2. Update SRS Store (Reactive UI State)
    if (result !== 'exposure') {
      useSrsStore.getState().recordAnswer(itemId, result === 'correct');
    }

    // 3. Record to Global Review History (IndexedDB/Dexie)
    await db.global_review_history.add({
      item_id: globalId,
      timestamp: new Date().toISOString(),
      result: result === 'correct',
      scenario_id: metadata.scenarioId
    });

    // 4. Update Global Progress (FSRS-Lite in Dexie)
    await this.updateGlobalMastery(globalId, result);

    // 5. Sync Gamification (XP, Streaks)
    const progressStore = useProgressStore.getState();
    if (result === 'correct') {
      progressStore.addXP(10);
    } else if (result === 'incorrect') {
      progressStore.addXP(-2);
    }
    
    // 6. Trigger Scenario Completion Checks
    this.revalidateScenarioProgress(metadata.scenarioId);
  }
};
```

## 4. Integration Strategy

### A. Capturing from Training Screens
The `VocabularyTrainingScreen`, `PhraseTrainingScreen`, and `SentenceTrainingScreen` currently call `recordAnswer` and `addXP` directly. These will be refactored to call `globalProgressService.recordActivity`.

- **Exposure Capture:** Implement a `useEffect` within training components that fires when the `activeTerm`/`activeItem` changes, ensuring every encounter is logged even if the user leaves without answering.
- **UI Preservation:** Since `useSrsStore` and `useProgressStore` are still being updated, existing progress bars, checkmarks, and completion screens will continue to function without modification.

### B. Capturing from srsStore.ts
To ensure events are captured even if triggered outside the standard training screens (e.g., via the Placement Test or future Review screens), the `srsStore.ts` will be enhanced with a side-effect hook:

```typescript
// src/store/srsStore.ts refinement
recordAnswer: (id, correct) => {
  set(state => { /* ... existing logic ... */ });
  
  // Implicitly notify the global service of the event
  // This ensures that any direct store manipulation is still tracked globally
  globalProgressService.onStoreAnswerRecorded(id, correct);
}
```

## 5. Backward Compatibility & Data Integrity
- **Legacy IDs:** The service will utilize the `scenario_vocab_mapping_cache` to translate scenario-bound IDs (e.g., `s01-v05`) to global dictionary IDs (e.g., `word_ciao`).
- **Scenario Progress:** Scenario completion logic (e.g., `maybeCompleteVocabularyPhase`) will remain in place but will eventually transition to reading from the global service's aggregated state.
- **Max Streak Rule:** During Phase 7.3 migration, existing user data will be aggregated into the global store using the "Max Streak" rule to ensure no progress is lost.

## 6. Next Steps
1. Create `src/services/globalProgressService.ts`.
2. Refactor `srsStore.ts` to include the global service notification.
3. Update `VocabularyTrainingScreen.tsx` as the first pilot for the new event capture flow.
4. Validate that scenario completion still triggers correctly upon mastering all vocabulary.
