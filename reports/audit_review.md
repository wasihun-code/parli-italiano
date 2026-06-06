# Phase 7.2 Audit Review: Global Dictionary Integrity

## 1. Overview
This document specifies the validation suite for the Global Dictionary layer (Phase 7.2). The primary goal is to ensure mathematical integrity, linguistic consistency, and bidirectional traceability between the scenario-bound vocabulary and the central repository.

## 2. 'scripts/dictionary_integrity_audit.py' Logic
The audit script MUST implement the following validation passes:

### Pass A: Global Uniqueness (Dictionary Level)
- **Constraint**: Every `id` in `global_dictionary.json` must be unique.
- **Check**: Aggregate all IDs and verify `len(ids) == len(set(ids))`.
- **Failure**: `CRITICAL ERROR` - Blocking Release.

### Pass B: Mapping Integrity (Mapping Level)
- **Constraint**: Every scenario-vocabulary pair must resolve to exactly one global entry.
- **Check**: 
    1. For every scenario in `scenario_vocab_mapping.json`, verify no duplicate `original_id` entries.
    2. Verify that every `global_dict_id` referenced in the mapping exists in the Global Dictionary.
- **Failure**: `CRITICAL ERROR` - Blocking Release.

### Pass C: Exhaustive Coverage (Scenario Level)
- **Constraint**: 100% of scenario vocabulary must be globalized.
- **Check**: 
    1. Iterate through all `src/data/exports/**/*_vocabulary.json` files.
    2. For every entry, confirm its `(scenario_id, vocab_id)` exists in the mapping file.
- **Failure**: `CRITICAL ERROR` - Incomplete globalization.

### Pass D: Translation & Content Quality
- **Constraint**: No empty or placeholder data.
- **Check**:
    1. `italian` and `english_primary` must be non-empty strings.
    2. `audio_json.italian` must point to a valid `/audio/*.opus` path (format check).
- **Failure**: `MAJOR WARNING` - Content Gap.

### Pass E: Collision & Homonym Resolution
- **Constraint**: Identical Italian words with semantically distinct English meanings must use `concept_N_` IDs.
- **Check**: 
    1. Group Global Dictionary entries by `italian`.
    2. If a group has multiple entries using the same `word_` ID pattern (impossible by ID uniqueness, but check for manual override errors).
    3. If multiple entries have the same `italian` but distinct `english_primary` and are NOT using `concept_` IDs, flag for review.
- **Failure**: `MAJOR WARNING` - Potential Unresolved Polysemy.

### Pass F: Orphan Detection
- **Constraint**: Minimize dead data.
- **Check**: Identify any entry in the Global Dictionary that is NOT referenced by any mapping.
- **Failure**: `MINOR INFO` - Clean-up recommended.

## 3. Round-Trip Validation Logic
To prove the integrity of the transformation, the script must perform a 'Round Trip' check on a sample of 10% of scenarios (randomly selected):

1. **Extraction**: Load local `scenario_vocabulary.json`.
2. **Resolution**: Use `scenario_vocab_mapping.json` to find the `global_dict_id`.
3. **Retrieval**: Fetch the entry from `global_dictionary.json`.
4. **Comparison**: Verify that `local.italian == global.italian` (after normalization).
5. **Reconstruction**: Re-generate a mock local vocabulary file from the Global Dictionary data and verify it is functionally identical to the original (excluding IDs).

## 4. Phase 7.2 Certification Pass/Fail Conditions

| Condition | Level | Description |
| :--- | :--- | :--- |
| Duplicate Global IDs | **CRITICAL** | Any ID collision in the dictionary file. |
| Missing Mappings | **CRITICAL** | A scenario word exists but has no mapping. |
| Dangling References | **CRITICAL** | Mapping points to an ID that doesn't exist in the dictionary. |
| Empty Translations | **MAJOR** | `english_primary` is null, empty, or placeholder. |
| Audio Path Mismatch | **MAJOR** | Audio path doesn't follow project naming conventions. |
| Unresolved Homonyms | **WARNING** | Same word, different meaning, same learnable ID (merging concepts). |
| Orphan Records | **INFO** | Unused vocabulary entries. |

## 5. Execution Protocol
1. Run `scripts/dictionary_integrity_audit.py`.
2. Generate `reports/dictionary_integrity_report.md`.
3. If any **CRITICAL** errors exist, `OVERALL: FAIL`.
4. Certification is only granted when 100% of Scenarios are mapped and 0 Critical errors remain.
