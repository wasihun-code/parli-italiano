# Cleanup Verification Report

## Deletion Candidates
- `dist/`: Generated artifact. Not imported. Reproducible via `npm run build`. Safe to delete.
- `test-results/`: Playwright failure artifacts. Safe to delete.
- `tree_output.txt`: Stale artifact. Not imported. Safe to delete.
- `file_list_for_report.txt`: Temp artifact. Safe to delete.
- `root_files_analysis.json`: Temp artifact. Safe to delete.
- `actual_audio.txt`: Temp artifact. Safe to delete.
- `used_audio.txt`: Temp artifact. Safe to delete.
- `orphaned_audio.txt`: Temp artifact. Safe to delete.
- `check_refs.py`: Temp artifact. Safe to delete.

## Root Script Archival Candidates
- `*.py` files in root (e.g. `gen_*.py`, `fill_*.py`). Audited via script. None are referenced in `src/`, `scripts/`, `backend/`, `e2e/`, `package.json`, or documentation (except for false positives where the script name matches a script in `scripts/`). They are legacy migration/generation scripts. Safe to move to `archive/phase1_generation/`.

## Dataset Deletion Candidates
- `src/data/exports2/`: Duplicate dataset. Investigated in Step 5.
- `src/data/scenarios/`: Old legacy dataset. Investigated in Step 5.

## NPM Packages Candidates
- `@google/generative-ai`, `@mlc-ai/web-llm`, `edge-tts-universal`. Investigated in Step 4.

## Audio Deletion Candidates
- Orphaned audio. Investigated in Step 6.
