# Factory V2 Review: Global Dictionary & Hybrid Mastery (Phase 7.2)

## 1. Proposed Implementation Logic

### A. Data Structures
- **`global_dictionary.json`**: A centralized array of unique vocabulary concepts.
  ```json
  [
    {
      "id": "word_caffe",
      "italian": "caffè",
      "english_primary": "coffee",
      "audio": "/audio/vocab/caffe.opus"
    },
    {
      "id": "concept_floor_piano",
      "italian": "piano",
      "english_primary": "floor",
      "audio": "/audio/vocab/piano_floor.opus"
    }
  ]
  ```
- **`scenario_vocab_mapping.json`**: A map connecting local scenario IDs to global dictionary IDs.
  ```json
  {
    "dining/ordering_coffee": [
      { "local_id": "v1", "global_dict_id": "word_caffe" },
      { "local_id": "v2", "global_dict_id": "word_per_favore" }
    ]
  }
  ```
- **`dictionary_overrides.json`**: Manual resolution for homonyms/polysemy.
  ```json
  {
    "piano": {
      "floor": "concept_floor_piano",
      "slowly": "concept_slowly_piano"
    }
  }
  ```

### B. Generation Algorithm (`global_registry_manager.py`)
1. **Extraction**: Read `_vocabulary.json` from the target scenario.
2. **Normalization**: Apply accent-safe rules to the `italian` field.
3. **Registry Lookup**: 
   - Check if the (normalized_italian, english) pair exists in the `global_dictionary.json`.
   - If a collision is detected (same normalized_italian, significantly different english), check `dictionary_overrides.json`.
   - If no override exists, use a deterministic index: `concept_N_<slug>`.
4. **Update**: 
   - Append new words to `global_dictionary.json`.
   - Update the scenario entry in `scenario_vocab_mapping.json`.
5. **Deterministic Ordering**: Always sort the dictionary by ID and the mapping by scenario slug to prevent git churn.

## 2. Accent-Safe Normalization Rules

To ensure consistency across 116 scenarios, we define two levels of normalization:

| Level | Purpose | Rules | Example (`caffè`) |
| :--- | :--- | :--- | :--- |
| **Canonical** | Comparison Key | `lower()`, straight apostrophes, remove punctuation, **keep accents**. | `caffè` |
| **Slug** | ID Generation | Strip accents (`à`->`a`), replace spaces/apostrophes with `_`. | `caffe` |

**Collision Handling for Short Words:**
- `e` (and) -> `word_e`
- `è` (is) -> `word_e_is` (Manual override required in `dictionary_overrides.json` to avoid collision with `e`).

## 3. Integration Plan

### A. Pipeline Update (`build_and_certify_scenario.py`)
Add a new Step 1.5 after Linguistic Extraction:
```python
# 1. Linguistic Extraction
if not run_script("linguistic_extractor.py", scenario_slug): sys.exit(1)

# 1.5 Global Registry Sync (New)
if not run_script("global_registry_manager.py", scenario_slug): sys.exit(1)
```

### B. Linguistic Extractor Refinement
Update `linguistic_extractor.py` to:
- Use the standard `normalize_text` function.
- Ensure `_vocabulary.json` output remains stable for the Registry Manager to read.

## 4. Certification & Validation

### New Audit: `global_dictionary_audit.py`
Integrated into `certify_scenario.py`, this audit will verify:
1. **Mapping Completeness**: Every `v*` ID in the scenario has a `global_dict_id` mapping.
2. **Registry Integrity**: Every `global_dict_id` in the mapping exists in `global_dictionary.json`.
3. **Translation Consistency**: The `english_primary` in the global dictionary is reasonably similar to the scenario's local translation.

## 5. Compatibility Statement
This approach is **100% backward compatible**. By using a separate mapping file (`scenario_vocab_mapping.json`) rather than modifying the `v*` IDs in `mini_lessons.json`, all existing curriculum and lesson audits will continue to pass without modification.
