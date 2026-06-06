# PARLA ITALIANO — MASTER OPERATING SYSTEM

## 1. Project Overview
Parla Italiano is a comprehensive, offline-capable, gamified web application for learning Italian at the A1–A2 level. It teaches through 116 real-world scenarios, interactive mini-lessons, scripted conversations, and deterministic audio.

## 2. Current Project Status
- **Scenarios:** 116/116 Generated and Certified (Gold Standard V1.0).
- **Factory:** Upgraded to V2 (Deterministic, Bidirectional Audits).
- **Admin Panel:** Scaffolded and Operationalized (Phase 5).
- **Learning Architecture:** Preparing to transition from Scenario Mastery to Hybrid Mastery.

## 3. Current Phase
**Phase 7.1 — Architecture Documentation Foundation**
Establishing the permanent, authoritative architectural source of truth for the entire platform.

## 4. Mandatory Development Workflow
Every action in this repository MUST follow this sequence:
1. **Analyze**: Understand current state and dependencies without modifying code.
2. **Plan**: Design the architecture, schema, or UI changes.
3. **Audit**: Review the plan against Gold Standard rules.
4. **Implement**: Execute code changes safely.
5. **Validate**: Run static checks, linting, and local tests.
6. **Certify**: Run the automated Factory Certification pipeline.
7. **Update Memory**: Record the finalized state in `MEMORY.md`.

## 5. Mandatory Sub-Agent Usage
Delegation is required for complex tasks. Use the following specialized agents:
- **Architecture Agent**: For system design, documentation, and roadmap planning.
- **Factory Agent**: For scenario generation, linguistic extraction, and dataset compilation.
- **Database Agent**: For Dexie schemas, Zustand stores, and data migrations.
- **Frontend Agent**: For React components, styling, and UI logic.
- **Audit Agent**: For running compliance checks and generating forensic reports.
- **QA Agent**: For end-to-end testing, visual validation, and edge-case discovery.

## 6. Gold Standard Rules
- **Benchmark:** `accommodation/apartment_key_pickup` is the reference implementation.
- **Conversations:** Minimum 4 conversations per scenario, 10+ turns each, Host starts.
- **Distractors:** Must match the correct answer length by +/- 40%.
- **Translations:** 100% natural English coverage. No placeholders.

## 7. Factory V2 Rules
- **Deterministic Curriculum:** `mini_lessons.json` MUST be generated programmatically by `curriculum_designer.py`. No LLM hallucination of IDs.
- **Bidirectional Coverage:** `scenario_integrity_audit.py` MUST mathematically prove `extracted_ids == taught_ids`.

## 8. Hybrid Mastery Rules
- **Vocabulary** is tracked globally (Global Dictionary).
- **Phrases and Sentences** are scenario-bound to preserve context.
- **Conversations** provide implicit review credit to global vocabulary.

## 9. Certification Rules
A scenario is ONLY complete when it passes all automated audits in `certify_scenario.py`. Manual QA does not override a failed script. An `OVERALL: FAIL` blocks release.

## 10. Forbidden Actions
- **DO NOT** manually edit `mini_lessons.json` or `vocabulary.json` to bypass audits; fix the source `conversations.json` and rebuild.
- **DO NOT** delete database tables during migrations.
- **DO NOT** leave placeholder UI in production components.
- **DO NOT** commit untested or uncertified scenario data.

## 11. Required Validation Sequence
1. `conversations.json` generation
2. `linguistic_extractor.py` execution
3. `curriculum_designer.py` execution
4. `distractor_generator.py` execution
5. Translation fulfillment
6. `certify_scenario.py` execution

## 12. Update Procedure For MEMORY.md
`MEMORY.md` is the absolute live state of the project. It MUST be updated at the end of every successful phase or certification run. It must reflect actual audit states, not assumptions.
