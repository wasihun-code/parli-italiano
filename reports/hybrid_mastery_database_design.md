# Hybrid Mastery Database Design

To support Global Knowledge Tracking without breaking the offline, client-side nature of Parla Italiano, both the static Dexie schema (curriculum data) and the dynamic Zustand schema (user progress) require structural refactoring.

## 1. Dexie Schema Changes (Curriculum Data)

The `scenario_vocabulary` table currently holds isolated, redundant records. It will be replaced by a relational model.

### New Table: `global_dictionary`
Stores the canonical definition of a word or concept.
- `id` (PK): e.g., `word_grazie` or `concept_floor_piano`.
- `italian`: The normalized Italian string ("grazie").
- `english_primary`: The canonical translation ("thank you").
- `audio_json`: Deterministic path or explicit metadata.
- `part_of_speech`: (Optional) noun, verb, etc.

### New Table: `scenario_vocab_mapping`
Acts as a many-to-many join table, linking a scenario to its required global vocabulary.
- `id` (PK): Compound key or auto-increment.
- `scenario_id` (FK): e.g., 22.
- `global_dict_id` (FK): e.g., `word_grazie`.
- `sort_order`: Order of appearance in the scenario.

### Unchanged Tables
- `scenarios`
- `scenario_phrases`
- `scenario_sentences`
*(Phrases and Sentences remain isolated and scenario-specific to preserve contextual application).*

## 2. Zustand Schema Changes (User Progress)

The `useSrsStore` and `useProgressStore` currently track progress using compound keys like `s22-v15`. 

### `srsStore.ts` Updates
- The `items: Record<string, SrsItem>` dictionary will now use `global_dict_id` as the key for vocabulary items.
- Phrases and sentences will continue to use `[scenario_id]-[phrase_id]` as keys.
- **Impact:** Calling `recordAnswer('word_grazie', true)` updates the SRS streak globally.

### `progressStore.ts` Updates
Currently, `scenarioProgress` tracks boolean flags like `vocabularyCompleted: boolean`.
- This logic becomes dynamic.
- `vocabularyCompleted` will no longer be a hardcoded boolean saved to local storage. 
- Instead, it will be a computed property (a getter):
  ```typescript
  isVocabularyCompleted(scenarioId): boolean {
    const requiredGlobalIds = db.getRequiredVocabForScenario(scenarioId);
    return requiredGlobalIds.every(id => srsStore.getState().items[id]?.learned);
  }
  ```
- **Impact:** Unlocking a scenario's Conversation phase is now dependent on the user's Global Knowledge Graph state.
