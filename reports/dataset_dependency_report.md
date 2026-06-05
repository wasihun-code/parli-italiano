# Dataset Dependency Report

## 1. `src/data/exports2/`
- **Created by:** `scripts/export_scenario_questions.ts`
- **Consumed by:** Nothing. No imports in the runtime or build code.
- **Legacy Status:** Yes. It was an intermediate format for generating questions.
- **Required:** No.

## 2. `src/data/scenarios/`
- **Created by:** Legacy generation scripts (now located in `archive/phase1_generation/`).
- **Consumed by:** Nothing. No imports in the runtime or build code.
- **Legacy Status:** Yes. It contains the old JSON format before the Gold Standard `exports/` structure was established.
- **Required:** No.
