# Troubleshooting & Historical Lessons

This document tracks known failure modes and historical lessons learned to prevent future regressions.

## 1. Curriculum Drift (The "Midpoint" Failure)
- **Symptom:** Scenarios fail certification because `mini_lessons.json` only covers half the vocabulary.
- **Root Cause:** Historically, `conversations.json` was expanded from 5 turns to 10 turns. `linguistic_extractor.py` was re-run, but `mini_lessons.json` was manually drafted by an LLM and never updated, leaving items 21-40 untaught.
- **Fix:** Factory V2 introduced the deterministic `curriculum_designer.py` and the bidirectional `scenario_integrity_audit.py` to mathematically prevent this.

## 2. Vocab ID Prefix Corruption
- **Symptom:** Scenario Integrity Audit fails saying `Lesson l1 references missing item ID: s53-v5`.
- **Root Cause:** Curriculum designers added `sXX-` prefixes directly into the JSON arrays. 
- **Fix:** IDs in JSON must be clean (`v1`, `p1`). The `corpusLoader.ts` dynamically handles namespacing.

## 3. Audio Coverage "Failures" (False Positives)
- **Symptom:** Over 44,000 files in `public/audio` appeared orphaned, and 18,000 JSON items lacked an `audio` key.
- **Root Cause:** Misunderstanding of the deterministic hash fallback.
- **Fix:** DO NOT delete `public/audio/`. The frontend dynamically hashes text (e.g., `SHA1("text|voice")`) to resolve missing metadata. 

## 4. Dictionary Collisions (Polysemy)
- **Symptom:** Round-trip validation fails (e.g., `per` != `però`).
- **Root Cause:** Naive regex normalization stripped Italian accents (`àèìòùé`), causing distinct words to merge into the same ID.
- **Fix:** Normalization must preserve accents. True homonyms (e.g., `piano` = floor/slowly) must be handled manually via `dictionary_overrides.json` to generate `concept_` IDs instead of `word_` IDs.

## 5. Recovery Procedures
- **If Factory build fails globally:** Revert to the last commit defined in `benchmarks/core_scripts_hashes.json`.
- **If User Progress is corrupted:** Instruct the user/admin to trigger the `restore_v1_backup()` function, reversing the Dexie migration.
