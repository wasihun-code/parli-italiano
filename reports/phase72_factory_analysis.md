# Phase 7.2 — Factory Analysis Report

## 1. Current Vocabulary Generation
Vocabulary is currently extracted on a per-scenario basis by `scripts/linguistic_extractor.py`. 
- **Input:** `conversations.json` for a specific scenario.
- **Process:**
  1. Tokenizes `host` lines and `correct` choices using a regex that preserves Italian characters (`àèìòùé`) but removes punctuation.
  2. Filters tokens with length > 2 and non-digits.
  3. Sorts unique tokens alphabetically.
  4. Assigns sequential IDs: `v1`, `v2`, `v3`, etc.
  5. Merges English translations from previous runs if available.
- **Output:** `[prefix]_vocabulary.json` (e.g., `travel_airport_arrival_vocabulary.json`).

## 2. Extraction Flow
The extraction is part of the `build_and_certify_scenario.py` pipeline.
1. `linguistic_extractor.py` (Vocab/Phrase/Sentence JSONs)
2. `curriculum_designer.py` (Mini Lessons JSON)
3. `distractor_generator.py` (Choices for lessons)
4. `audio_manifest_updater.py` (Audio metadata)

## 3. Integration Points for Global Dictionary
The Global Dictionary layer must be integrated into `linguistic_extractor.py` or as a new post-extraction step.
- **Integration point:** After per-scenario vocabulary is extracted, it should be mapped to the `global_dictionary.json`.
- **Mapping:** A new `scenario_vocab_mapping.json` must be generated to link the scenario-specific IDs (or the words themselves) to global IDs.

## 4. Risks
- **ID Stability:** If the global dictionary is regenerated, IDs must remain stable to avoid breaking existing user progress in future phases.
- **Collisions:** Words like "piano" (floor vs. slowly) must be disambiguated using the `concept_` override strategy defined in `HYBRID_MASTERY.md`.
- **Normalization:** Normalization must be 100% consistent with the runtime tokenization to ensure the `corpusLoader` and `srsStore` can resolve the correct global item.
- **Backward Compatibility:** Existing `_vocabulary.json` files must remain untouched or functionally identical to avoid breaking the current Scenario Mastery UI.
- **Accents:** Naive regexes often strip Italian accents; the current `tokenize` function in `linguistic_extractor.py` preserves them, which is correct.
