# Audit Review: Mastery Integrity Validation (Phase 7.3)

## 1. Objective
Ensure the structural and logical integrity of the Hybrid Mastery V2 system, specifically focusing on the transition from scenario-bound vocabulary to the Global Dictionary and the correctness of SRS state transitions.

## 2. Audit Scope
- **Data Sources:**
    - `generated/global_dictionary.json`
    - `generated/scenario_vocab_mapping.json`
    - `src/store/srsStore.ts` (State Logic)
    - All scenario-level `vocabulary.json` files.
- **Entities:**
    - Global Vocabulary IDs
    - Scenario-bound Phrases and Sentences
    - SRS Progress Records

## 3. Specifications for `scripts/mastery_integrity_audit.py`

### A. Referential Integrity Checks
1.  **Global Dictionary Uniqueness:** Validate that every `id` in `global_dictionary.json` is unique.
2.  **Mapping Consistency:** 
    - Every `global_id` in `scenario_vocab_mapping.json` must exist in `global_dictionary.json`.
    - Every scenario in `benchmarks/` must be present in the mapping.
    - Local IDs (e.g., `v1`, `v2`) in the mapping must match the IDs in the scenario's `vocabulary.json`.
3.  **Orphan Detection:** Identify any global IDs that are defined but never mapped to a scenario (unless they are "Common Core" words intended for future use).

### B. Mastery State Validation (Logic Simulation)
The script must simulate the state machine defined in `HYBRID_MASTERY.md` to verify transition validity:
- **Valid States:** `UNKNOWN`, `LEARNING`, `LEARNED`, `ADVANCED`, `MASTERED`, `LAPSED`, `RELEARNING`.
- **Transitions:**
    - `UNKNOWN` -> `LEARNING` (on first encounter)
    - `LEARNING` -> `LEARNED` (on `streak >= 3`)
    - `LEARNED` -> `ADVANCED` (on `interval > 7 days`)
    - `ADVANCED` -> `MASTERED` (on `interval > 30 days`)
    - `*` -> `LAPSED` (on any failure)
    - `LAPSED` -> `RELEARNING` (on first success after lapse)
    - `RELEARNING` -> `LEARNED` (on 2 consecutive successes)

### C. Migration Correctness
- Verify that `vocabulary` type items in the SRS store use `word_*` or `concept_*` ID formats.
- Ensure no legacy `s[ID]-v[ID]` formats persist for vocabulary items.
- Phrases and Sentences must retain scenario-bound IDs (e.g., `s22-p1`).

## 4. Success Criteria
- **Pass:** 100% resolution of global IDs, 0 invalid state transitions in simulation, 0 orphan progress records.
- **Fail:** Any missing IDs, mismatched mappings, or legacy vocabulary IDs in the SRS structure.

## 5. Execution Plan
1.  Develop `scripts/mastery_integrity_audit.py` using Python.
2.  Integrate with the existing `certify_scenario.py` if necessary, or run as a standalone global audit.
3.  Generate a forensic report `reports/mastery_integrity_report.md`.
