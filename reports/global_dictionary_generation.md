# Global Dictionary Generation Pipeline

This document defines how the Python factory will construct the Global Dictionary during Phase 7.1.

## ID Generation Rules

1. **Standard Normalization:** 
   - Lowercase the Italian string.
   - Remove punctuation and duplicate spaces.
   - Replace spaces with underscores.
   - Example: "Grazie mille!" -> `word_grazie_mille`.

2. **Collision Handling (Polysemy/Homonyms):**
   - The script parses `dictionary_overrides.json` before generating IDs.
   - If a word is flagged (e.g., "piano"), the script examines the `english` translation field in the scenario's JSON.
   - If English contains "floor" -> `concept_floor_piano`.
   - If English contains "slowly" -> `concept_slow_piano`.
   - The exact semantic mapping must be defined manually once by the curriculum engineers in the overrides file.

## Integration of Future Scenarios

When a new scenario (e.g., Scenario 117) is added:
1. `linguistic_extractor.py` parses the new `conversations.json`.
2. It generates normalized IDs.
3. It checks `global_dictionary.json`.
   - If the ID exists, it simply creates a new link in `scenario_vocab_mapping`.
   - If the ID does *not* exist, it appends the new word to `global_dictionary.json`.
4. The factory then builds the `mini_lessons.json` referencing these global IDs.
