# Repository Cleanup Plan — Parla Italiano

This plan outlines a phased approach to restoring repository clarity and recovering significant disk space.

## 1. Immediate Deletions (Generated/Stale Artifacts)
These files/folders are safely regeneratable or confirmed as redundant analysis artifacts.

- `dist/`: Build output (558MB). Recreate with `npm run build`.
- `test-results/`: Playwright failure logs.
- `tree_output.txt`, `file_list_for_report.txt`, `root_files_analysis.json`: Analysis temp files.
- `actual_audio.txt`, `used_audio.txt`, `orphaned_audio.txt`: Audio audit temp files.
- `exported-content.json`, `generated_data.json`: Old data exports.

## 2. Archival Candidates (Legacy Infrastructure)
These scripts should be moved to a `legacy/` or `archive/` directory to clean up the root folder.

- **One-time scripts**: All root-level `gen_*.py`, `fill_*.py`, `apply_*.py`, `update_*.py`. (~140 files).
- **Development tests**: Standalone `test_*.py`, `test-*.js` files in root.
- **Root MP3s**: `airport.mp3`, `dialogue.mp3`, `friend.mp3`, `receptionist.mp3`, `traveler.mp3`, `waiter.mp3`, `test.mp3`, `tech.mp3`. (These are dev samples, production audio is in `public/audio/`).

## 3. Orphaned Asset Cleanup
- **Orphaned Audio**: 44,785 files in `public/audio/` are not referenced by any curriculum.
- **Recommendation**: Move orphaned files to a temporary backup outside the repository for 30 days before permanent deletion.

## 4. Duplicate Dataset Deletion
- `src/data/exports2/`: Fully redundant.
- `src/data/scenarios/` (directory): Legacy format.
- `backup/` (directory): Redundant local backups.

## 5. Dependency Optimization
- **npm**: Uninstall `@google/generative-ai`, `@mlc-ai/web-llm`, `edge-tts-universal`.
- **Space Recovery**: ~50-100MB from `node_modules`.

## 6. Git Configuration Updates
Add the following to `.gitignore` to prevent future clutter:
- `backend/venv/`
- `reports/*.json`
- `reports/*.md` (except reference ones)
- `backup/`
- `legacy/` (after move)
- `*.txt` (root analysis files)
- `*.opus` (root test files)
- `*.mp3` (root test files)
