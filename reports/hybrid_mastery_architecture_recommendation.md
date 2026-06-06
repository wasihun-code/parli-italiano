# Hybrid Mastery Architecture Recommendation

## Should Hybrid Mastery be implemented?
**YES.**

## Why?
The current Scenario Mastery architecture contains extreme pedagogical friction. As demonstrated in the simulation, by the time a user reaches their fourth scenario, **over 40%** of the vocabulary presented to them consists of words they have already mastered in previous lessons. 

Furthermore, the collision analysis proves that out of the thousands of unique normalized words, only a small fraction are true homonyms requiring distinct concept tracking. The vast majority of the Italian language can be safely mapped to a 1:1 Global Dictionary.

## Global Vocabulary Layer V1 Architecture

### 1. Schema Updates
- **New Table:** `global_dictionary` `(id, normalized_text, english_primary, part_of_speech)`
- **New Table:** `scenario_vocab_mapping` `(scenario_id, vocab_id, global_dict_id)`
- **SRS Tracking:** `srs_items` will track `global_dict_id` for vocabulary, rather than `scenario_id + vocab_id`.

### 2. ID Strategy (Option C: Hybrid)
- **Default:** `word_[normalized_string]` (e.g., `word_grazie`). Generated deterministically.
- **Override:** `concept_[english_context]_[normalized_string]` (e.g., `concept_floor_piano`). Managed via a static `dictionary_overrides.json` file during the extraction phase.

### 3. Migration Strategy
1. **Freeze Factory:** No new scenarios generated during migration.
2. **Global Extraction Run:** A script aggregates all 116 scenarios, applying the normalization logic.
3. **Override Generation:** Manually review the `homonym_analysis.md` report and create the `dictionary_overrides.json` file.
4. **Curriculum Re-link:** Run a migration script that injects the `global_dict_id` into every `v*` item inside every `_vocabulary.json` file.
5. **App Upgrade:** Update `corpusLoader.ts` and `srsStore.ts` to read and write against the `global_dict_id`.
6. **Progress Migration (User Data):** For existing users, run a one-time migration aggregating all their `srs_items` where `item_type == 'vocabulary'`, taking the maximum `correctStreak` across scenarios and applying it to the new `global_dict_id`.
