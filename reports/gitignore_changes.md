# Gitignore Hardening Report

The following entries were appended to `.gitignore` to prevent tracking of generated, temporary, or unneeded files:

- `__pycache__/`
- `*.pyc`
- `reports/*.json`
- `reports/failures/*.md`
- `archive/`
- `legacy_archive/`
- `actual_audio.txt`, `used_audio.txt`, `orphaned_audio.txt`
- `tree_output.txt`, `file_list_for_report.txt`, `root_files_analysis.json`, `check_refs.py`

`dist/` and `test-results/` were confirmed to already be present.
