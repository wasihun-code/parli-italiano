# Audit Rules & Specification

This document serves as the single source of truth for the Factory V2 Certification Pipeline.

## Current Audits

### `curriculum_audit.py`
- **Purpose:** Verifies that all vocabulary, phrases, and sentences extracted exist in the conversations.
- **Inputs:** `conversations.json`, `*_vocabulary.json`, `*_phrases.json`, `*_sentences.json`.
- **Outputs:** Coverage percentage.
- **Pass Conditions:** Extracted items <= Conversation items.
- **Fail Conditions:** Extracted item is not found in dialogue (Hallucination).

### `audio_audit.py` / `mini_lesson_audio_audit.py`
- **Purpose:** Verifies audio metadata and playback flow.
- **Inputs:** Linguistic JSONs, `mini_lessons.json`.
- **Outputs:** Verification of `audio` keys and missing file paths.
- **Pass Conditions:** Explicit audio paths exist or deterministic hashes can be resolved.
- **Fail Conditions:** Broken paths or unresolvable hashes.

### `conversation_audit.py`
- **Purpose:** Validates structural integrity of dialogue trees.
- **Inputs:** `conversations.json`.
- **Outputs:** Turn counts, role verification.
- **Pass Conditions:** >= 4 conversations, >= 10 turns each, Host starts.
- **Fail Conditions:** Too few turns, user starts, dead-end branches.

### `scenario_integrity_audit.py`
- **Purpose:** Mathematically proves bidirectional curriculum coverage.
- **Inputs:** Linguistic JSONs, `mini_lessons.json`.
- **Outputs:** Missing IDs, Untaught IDs.
- **Pass Conditions:** `extracted_ids == taught_ids`.
- **Fail Conditions:** A lesson references an ID that wasn't extracted, or an extracted ID is left out of all lessons.

---

## Future Audits (Hybrid Mastery)

### `dictionary_integrity_audit.py`
- **Purpose:** Verifies global dictionary health.
- **Inputs:** `global_dictionary.json`.
- **Pass Conditions:** No duplicate IDs, no empty English strings.
- **Fail Conditions:** Unresolved collisions, missing primary translations.

### `mastery_integrity_audit.py`
- **Purpose:** Validates FSRS-Lite state transitions in simulated environments.
- **Inputs:** Mock SRS sequences.
- **Pass Conditions:** Lapsed items drop to 20% interval; learned items scale correctly.

### `review_queue_audit.py`
- **Purpose:** Ensures the daily review queue respects the 100-item cap and priority sorting.

### `hybrid_mastery_audit.py`
- **Purpose:** Validates that scenario unlocks properly compute global vocabulary states.
- **Inputs:** `scenario_vocab_mapping.json`.
- **Pass Conditions:** Scenario remains locked if global mapping requirements are unmet.
