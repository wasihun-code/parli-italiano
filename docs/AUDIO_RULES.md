# Audio Rules

## 1. Deterministic Generation
Audio generation MUST be deterministic. The same text should always resolve to the same audio hash and filename. We do not generate duplicate files for the same string.

## 2. Asset Reuse
*   Global Manifest: All audio maps to a central manifest (e.g., `public/audio_manifest.json`).
*   If a phrase appears in both a Conversation and a Mini Lesson, they must reference the exact same audio file.
*   Distractors used across multiple exercises should reuse the same audio asset.

## 3. Coverage Requirements
100% of the following items MUST have a valid, referencing `audio` object:
*   Conversation Host lines
*   Conversation User choices (all correct and distractors)
*   Vocabulary items (and their choices)
*   Phrase items (and their choices)
*   Sentence items (and their choices)

## 4. Runtime Playback Flow
*   **Conversations:** Host audio autoplays immediately. User audio is strictly MANUAL (via a speaker icon).
*   **Mini Lessons:** Choice audio plays IMMEDIATELY upon selection (click or keyboard 1-4). There is no "leak" of the correct answer audio prior to selection.

## 5. Audit Compliance
The `scripts/audio_audit.py` and `scripts/runtime_audio_audit.py` scripts must pass, proving that the files exist on disk, are referenced correctly in the JSON, and adhere to the playback logic constraints.
