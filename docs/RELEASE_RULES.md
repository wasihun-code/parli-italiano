# Production Release Rules

Every scenario and feature release MUST satisfy this checklist before merging to the `main` branch.

## 1. Pre-Release Validation
- No manual edits allowed in `mini_lessons.json` or extracted linguistic files. All changes must originate from `conversations.json` or `dictionary_overrides.json`.
- The codebase must be free of `Placeholder` components and dead routes.

## 2. Required Audits & Certifications
- **`certify_all.py`:** Must return 100% PASS across all scenarios.
- **Global Dictionary Validation:** Coverage must be 100%, and Round Trip reconstruction must be 100%.

## 3. Regression Testing
- Changes to core python scripts (`linguistic_extractor.py`, `curriculum_designer.py`) must pass `benchmark_audit.py` to ensure legacy gold standard scenarios (`apartment_key_pickup`) are uncorrupted.

## 4. Audio Validation
- Explicit audio paths must resolve.
- Missing audio metadata must successfully generate deterministic SHA-1 hashes that exist in `public/audio_manifest.json`.

## 5. Curriculum & Dictionary Validation
- Bidirectional coverage rule enforced: `extracted_ids == taught_ids`.
- Homonyms must be explicitly managed via `concept_` mappings to prevent global dictionary collisions.

## 6. Hybrid Mastery Validation (Post-V2)
- SRS math tests must pass.
- Progress migration scripts must execute without data loss in isolated test environments.

## 7. Go/No-Go Checklist
- [ ] Build passes (`npm run build`).
- [ ] E2E Playwright tests pass.
- [ ] Factory Certification passes.
- [ ] `MEMORY.md` is updated with the latest run timestamp.
