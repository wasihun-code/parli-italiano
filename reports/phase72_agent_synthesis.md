# Phase 7.2 — Agent Synthesis & Implementation Plan

## 1. Findings Summary
The multi-agent review has confirmed that the Global Dictionary infrastructure is the correct path forward for Parla Italiano, but the current prototype and extraction scripts require immediate hardening before implementation.

- **Architecture:** Confirmed that a relational mapping strategy is superior to rewriting ID references in curriculum files, ensuring 100% backward compatibility.
- **Factory:** Identified the need for a central `global_registry_manager.py` to maintain deterministic ID stability.
- **Database:** Highlighted the need to reconcile scenario IDs (path slugs vs numeric) and the requirement for a compound index for performance.
- **QA:** Exposed critical data loss in the current `linguistic_extractor.py` (discarding words <= 2 chars and breaking elisions) and ASCII ID collisions (e.g., `più`).
- **Audit:** Designed a comprehensive 100% Round-Trip validation suite.

## 2. Identified Conflicts
- **Table Deletion:** The initial migration plan proposed deleting `scenario_vocabulary`, which violates the `DATABASE_RULES.md`. Legacy tables MUST be retained.
- **ID Stability:** The prototype's index-based IDs (`concept_0_word`) are unstable. Architecture requires semantic IDs (`concept_[english]_[word]`).
- **Mapping Strategy:** Conflicts between direct ID replacement (Strategy B) and mapping files (Strategy A).

## 3. Final Implementation Plan

### Step A: Extraction Hardening
1. **Update `scripts/linguistic_extractor.py`**:
   - Remove the `len > 2` tokenization constraint.
   - Refine regex to preserve Italian accented characters and handle elisions (apostrophes) correctly.
2. **Standardize Overrides**: Create `src/data/dictionary_overrides.json` to handle the ~400 identified homonyms using semantic descriptors.

### Step B: Deterministic Generation
1. **Implement `scripts/global_dictionary_generator.py`**:
   - Aggregate all 116 scenarios.
   - Use the hardened extraction rules.
   - Generate `global_dictionary.json` with stable, UTF-8 compatible IDs.
2. **Generate Mapping**: Produce `scenario_vocab_mapping.json` linking `[scenario_slug]:[local_id]` to `global_dict_id`.

### Step C: Validation & Integration
1. **Implement `scripts/dictionary_integrity_audit.py`**: Execute round-trip and coverage checks.
2. **Factory Integration**: Add the generation step to `certify_all.py` as a post-processing hook.

## 4. Go / No-Go Recommendation
**GO (Conditional)**
Proceed to implementation only after the `len > 2` constraint is removed from the factory pipeline to ensure the most frequent 30% of the Italian language is captured.
