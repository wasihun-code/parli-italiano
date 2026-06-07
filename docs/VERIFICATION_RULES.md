# Verification Rules for Learning System V3

Before any phase of Learning System V3 is considered complete, it must pass the following verification rules.

## Core Mandates
1. **Immutable Content:** No runtime logic may modify, rewrite, or replace `conversations.json`, `vocabulary.json`, `phrases.json`, `sentences.json`, or `mini_lessons.json`.
2. **Certifiability:** The `certify_scenario.py` script must continue to pass 100% for all 116 scenarios.

## Required Audits
Every PR or major phase commit must be accompanied by the successful execution of the following audit scripts:
- `scripts/content_integrity_audit.py`
- `scripts/exercise_coverage_audit.py`
- `scripts/progression_audit_v3.py`
- `scripts/production_balance_audit.py`
- `scripts/scenario_fidelity_audit.py`

## Pass / Fail Criteria
- **PASS:** All scripts return exit code `0`. No JSON files are mutated. The progression flow mathematically verifies the `Recognition -> Recall -> Production` constraint.
- **FAIL:** Any script returns `>0`. Any JSON file is modified. Any production exercise appears before a recognition exercise in the generated path.

## Required Reports
Upon completion of a phase, the corresponding report template (e.g., `reports/phase91_architecture.md`) must be filled out, detailing the implementation, the audit results, and the justification for the design.
