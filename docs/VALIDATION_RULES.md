# Validation Framework Rules

## Objective
To eliminate human error and subjective review from the scenario generation process. A scenario is either mathematically proven to be compliant, or it is rejected.

## Pass/Fail Criteria

Every script in the `scripts/` directory corresponding to an audit must output a strict `PASS` or `FAIL` based on the following criteria:

### 1. Curriculum Coverage (`curriculum_audit.py`)
*   **PASS:** 100% of unique conversation words, phrases, and sentences exist in the respective curriculum JSON files and are referenced by the mini-lessons.
*   **FAIL:** Anything < 100%.

### 2. Audio Integrity (`audio_audit.py`)
*   **PASS:** 100% of nodes contain an `audio` object mapping to an existing file in `public/audio/...`.
*   **FAIL:** Missing metadata, or file does not exist on disk.

### 3. Conversation Logic (`conversation_audit.py`)
*   **PASS:** ≥ 4 conversations, ≥ 10 turns each, no dead ends (every path reaches `END`), no missing `nextMessageId` logic.
*   **FAIL:** Any structural defect or failure to meet minimum counts.

### 4. Distractor Quality (`distractor_audit.py`)
*   **PASS:** All choices have 3-4 options, no duplicates, lengths are within +/- 40% of correct answer, no placeholder strings.
*   **FAIL:** Violations of choice structure.

### 5. Lesson Integrity (`lesson_audit.py`)
*   **PASS:** Every lesson has a `title` and `goal`. All `exerciseIds` map to valid items in the registry. No duplicate exercises in a single lesson.
*   **FAIL:** Missing fields or broken references.

### 6. Progression Validation (`progression_audit.py`)
*   **PASS:** Every word encountered in a conversation has been introduced in the preceding mini-lessons.
*   **FAIL:** Vocabulary leap detected (unknown word in conversation).

### 7. Translation Completeness (`translation_audit.py`)
*   **PASS:** 100% of required fields have English translations. No string contains "Translation of" or "English for".
*   **FAIL:** Missing or placeholder translations.

### 8. Keyboard & UI (`keyboard_audit.py`)
*   **PASS:** Source code statically verifies presence of `e.key` mappings for 1-4, Enter, Space, T, and Escape.
*   **FAIL:** Missing keyboard event handlers in training screens.

### 9. Domain Consistency (`domain_audit.py`)
*   **PASS:** 0% contamination based on forbidden term lists.
*   **FAIL:** Unrelated domain term detected.

### 10. Runtime Audio (`runtime_audio_audit.py`)
*   **PASS:** Playback policies (Host autoplay = YES, User autoplay = NO, MiniLesson Choice autoplay = YES) are statically verified in the React codebase.
*   **FAIL:** Audio leak or bad autoplay logic detected.

## Master Orchestration
The script `scripts/gold_standard_audit.py` or `scripts/certify_scenario.py` manages the execution of all individual audits. A single `FAIL` in any sub-audit results in an `OVERALL: FAIL` for the scenario.
