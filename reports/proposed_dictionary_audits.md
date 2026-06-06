# Proposed Dictionary Audits

These audits must be integrated into Factory V2 to maintain the Global Knowledge Graph safely.

### 1. `dictionary_integrity_audit.py`
- **Purpose:** Verifies `global_dictionary.json` has no duplicate IDs, no empty strings, and valid `audio_json` structures.

### 2. `dictionary_collision_audit.py`
- **Purpose:** Scans newly extracted words. If a word is found in `global_dictionary.json` but the new English translation is >40% semantically different, it flags a `WARNING` suggesting a manual `concept_` override.

### 3. `mapping_integrity_audit.py`
- **Purpose:** Verifies that every `global_dict_id` referenced in `scenario_vocab_mapping.json` actually exists in the global dictionary. Prevents broken foreign keys.

### 4. `round_trip_audit.py`
- **Purpose:** For a given scenario, extracts vocabulary from `conversations.json`, normalizes it, and mathematically proves that every resulting item maps 1:1 to an entry in the Global Dictionary via the Scenario Mapping file.
