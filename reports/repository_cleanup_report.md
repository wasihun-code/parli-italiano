# Repository Cleanup Report — Parla Italiano

This report classifies every file and directory in the repository to identify cleanup opportunities while ensuring safety of the production environment.

## 1. Directory Classification

| Path | Classification | Reason |
| :--- | :--- | :--- |
| `src/` | Production Code | Core React frontend application. |
| `backend/` | Production Code | Core Django backend application. |
| `public/` | Application Asset | Static assets, including production audio corpus. |
| `scripts/` | Build Infrastructure | Active automation scripts (audits, builds, extractors). |
| `reports/` | Generated Artifact | Output of certification and cleanup audits. |
| `benchmarks/` | Test Infrastructure | Snapshots of core scenarios for regression tracking. |
| `docs/` | Documentation | Pedagogical and technical rules. |
| `e2e/` | Test Infrastructure | Playwright end-to-end tests. |
| `dist/` | Cache / Artifact | Build output (safe to delete, recreate with `npm run build`). |
| `node_modules/` | Cache / Virtual Env | npm packages (safe to delete, recreate with `npm install`). |
| `backend/venv/` | Virtual Environment | Python virtual env (safe to delete, recreate). |
| `backend/media/` | Application Asset | User-uploaded media or dev-specific media. |
| `backend/static/` | Application Asset | Collected Django static files. |
| `test-results/` | Cache / Test Infra | Playwright failure artifacts. |
| `backup/` | Candidate For Archiving | Redundant local backups. |
| `src/data/exports2/`| Legacy/Unused | Superseded by the `exports/` folder structure. |
| `src/data/scenarios/`| Legacy/Unused | Sparse old scenario data format. |

## 2. Root Script Analysis

Over 180 scripts were found in the root directory. Most are one-time migration or generation scripts from earlier project phases.

### Key Essential Scripts (Production/Config)
- `package.json`, `package-lock.json`: Essential Build/Dependency config.
- `tsconfig.json`, `vite.config.ts`, `vitest.config.ts`: Essential build/test config.
- `eslint.config.js`: Essential linting config.
- `MEMORY.md`, `GEMINI.md`, `README.md`, `LICENSE`: Essential documentation.

### Candidates for Archiving (Legacy Scripts)
~140 scripts in root are identified as one-time migration/generation tools.

**Sample of Candidates for Archiving:**
- `gen_*.py`: Scenario-specific generators (e.g., `gen_s10.py`).
- `fill_*.py`: Vocabulary/Translation fillers (e.g., `fill_police_vocab.py`).
- `apply_*.py`: Translation appliers (e.g., `apply_translations_v71.py`).
- `fix_*.py`: Data repair scripts (e.g., `fix_conv_schema.py`).
- `extract_*.py`: Legacy extraction logic (superseded by `scripts/linguistic_extractor.py`).

| Path | Referenced? | Imported? | Safe to Archive? | Safe to Delete? | Confidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `gen_*.py` | No | No | Yes | Yes | High |
| `fill_*.py` | No | No | Yes | Yes | High |
| `test_*.py` | No | No | Yes | Yes | High |
| `*.txt` (root) | No | No | Yes | Yes | High |
| `*.mp3` (root) | No | No | Yes | Yes | High |

## 3. Stale Generated Data & Artifacts
- `tree_output.txt` (2.2MB): Unused directory tree dump.
- `actual_audio.txt`, `used_audio.txt`, `orphaned_audio.txt`: Temporary analysis files.
- `exported-content.json`, `generated_data.json`: Old data exports.

## 4. Static Analysis Results

- **Python files never imported**: ~140 root scripts (most function as standalone CLIs).
- **Dead Code**: `src/lib/llm.ts` contains `initLlama` and `unloadLlama` as empty functions, but they are hooks for potential future browser-LLM usage.
- **Duplicate Datasets**: `src/data/exports2/` is a 100% duplicate of data generated from `src/data/scenarios.ts`, which is now superseded by the Gold Standard `exports/`.
- **Duplicate Audio Assets**: `dist/audio` (529MB) is a complete duplicate of a subset of `public/audio`.
- **Unused npm packages**: `@google/generative-ai`, `@mlc-ai/web-llm`, `edge-tts-universal`.
- **Directories containing only generated files**: `dist/`, `test-results/`, `reports/`.
- **Orphaned Assets**: **44,785 orphaned audio files** in `public/audio` (524 MB) not referenced in any production scenario.
