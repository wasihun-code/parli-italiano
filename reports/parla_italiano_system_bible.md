# Parla Italiano: System Bible

## 1. Executive Summary

Parla Italiano is an offline-capable, gamified web application for learning Italian at the A1-A2 level, structured around 116 real-world scenarios. The system architecture is uniquely deterministic: a **Python-based Factory V2 pipeline** processes LLM-generated conversations into rigidly structured learning assets, which are then eagerly loaded by a **React/Vite Frontend** and stored locally via **Dexie.js** (IndexedDB). A **Django Backend** handles user state, progression sync, and analytics. 

The application is currently transitioning from an isolated Scenario Mastery model (V1) to a **Hybrid Mastery V2** model, where vocabulary is tracked globally using FSRS-lite spaced repetition, while phrases and sentences remain situationally bound to preserve context.

## 2. Scenario Architecture (e.g., Apartment Key Pickup)

The `apartment_key_pickup` scenario (ID 22) serves as the V1 reference implementation. 
- **conversations.json**: The absolute source of truth. Contains branching dialogues (e.g., handling the keypad, finding the lockbox). 
- **vocabulary.json / phrases.json / sentences.json**: Deterministically extracted from the conversations.
- **mini_lessons.json**: Deterministically chunked into 6 sequential lessons (e.g., "Finding the Entrance", "Using the Intercom").
- **Certification Files**: JSON/MD reports proving mathematical coverage (e.g., `extracted_ids == taught_ids`).

**Runtime Usage**: The frontend's `corpusLoader.ts` dynamically imports these JSON files and seeds the Dexie local database to construct the UI flashcards and conversation trees.

## 3. Content Pipeline

The Factory V2 content creation pipeline operates sequentially to ensure determinism and integrity:

1. **Scenario Creation** (`Agent 1/2` - not part of the runtime python scripts) -> generates `conversations.json`.
2. **Extraction** (`linguistic_extractor.py`) -> Parses words, phrases, and sentences from the dialogue.
3. **Curriculum Design** (`curriculum_designer.py`) -> Distributes extracted items evenly across exactly 6 `mini_lessons.json`.
4. **Distractor Generation** (`distractor_generator.py`) -> Adds 2-3 incorrect choices for every exercise.
5. **Translation & Audio** (`audio_manifest_updater.py`, `mock_audio_files.py`) -> Synthesizes or hashes audio files.
6. **Certification** (`build_and_certify_scenario.py`, `certify_scenario.py`) -> Runs 10+ audits to mathematically prove the integrity of the data.

## 4. Mini Lesson Architecture

Every scenario features exactly **6 Mini Lessons**.
- **Structure:** Each lesson contains exactly 4 sections: `Vocabulary`, `Phrase`, `Sentence`, and a final `Mastery Check`. 
- **Exercise Types:** Predominantly multiple-choice recognition (1 correct, 2-3 distractors). The UI is strictly keyboard-accessible (1-4 keys).
- **Progression Model:** The curriculum moves from explicit instruction (Vocab flashcards) to implicit context (Phrases/Sentences). Completing all 6 lessons unlocks the full conversation simulator.

## 5. Conversation Architecture

Conversations simulate real-world interactions.
- **Branching Structure:** Minimum 4 conversations per scenario, 10-20 turns each. The "host" (Italian speaker) always initiates.
- **Progression:** The user navigates by selecting 1 of 3 replies. Choices have dynamic feedback based on correctness (e.g., cultural faux pas vs. correct response).
- **Audio:** Audio autoplays for the host; user choices require manual playback. Translations are hidden by default to enforce listening comprehension.
- **Files:** Managed centrally within `conversations.json`, with audio linked via hashes.

## 6. Hybrid Mastery V2

The transition to Hybrid Mastery fixes the isolated silo problem of V1.
- **Global Dictionary:** A centralized store (`global_dictionary.json`, loaded into `db.global_dictionary`) tracking all unique vocabulary.
- **Mappings:** `scenario_vocab_mapping.json` ties local scenario IDs to global dictionary IDs.
- **Global Progress:** Tracked via `db.global_progress` using an FSRS-lite model with 7 states: `UNKNOWN`, `LEARNING`, `LEARNED`, `ADVANCED`, `MASTERED`, `LAPSED`, `RELEARNING`.
- **Adaptation (`CurriculumAdaptationService`):** At runtime, the local mini-lessons filter out globally known vocabulary, preserving a minimum of 2 words as a "Safety Floor" for context.
- **Reinforcement (`ConversationReinforcementService`):** Successfully completing a conversation grants implicit SRS review credit to the underlying global vocabulary, acting as a "Pass" without requiring an explicit flashcard review.
- **Review Queue (`ReviewQueueService`):** Generates a daily maximum queue of 100 FSRS items.

## 7. Database Architecture

The application relies on a robust offline-first IndexedDB schema managed by Dexie (`src/lib/db.ts`).
- **Legacy Stores (V1):** `scenario_vocabulary`, `scenario_phrases`, `scenario_sentences`, `srs_items`.
- **Hybrid Mastery Stores (V2/V3):** `global_dictionary`, `global_progress`, `global_review_history`, `scenario_vocab_mapping_cache`.
- **Backend Sync:** A Django Backend APIs track persistent cloud state via models like `UserLanguageProgress`, `ScenarioProgress`, and `MasteredItem`. The frontend uses Zustand (`progressStore.ts`) to manage local XP/Streaks and periodically pushes to Django via `apiClient.ts`.

## 8. Audio Architecture

Audio is massive (44,000+ files) and aggressively optimized.
- **Manifest:** `public/audio_manifest.json` acts as a central registry mapping text strings to hashes.
- **Hashing System:** If a file path isn't explicit, the system generates a 12-char SHA-1 hash of `text|voice_id` (e.g., `text|elsa`) to dynamically resolve the file path (`/audio/{hash}.opus`).
- **Generation:** Synthesized via python pipelines (`audio_manager.py`) using tools like Azure TTS (Elsa) or Edge-TTS.

## 9. Admin Panel

The Admin Panel (`/admin`) is a React-based, desktop-first control center built directly into the client.
- **Pages:** Includes `AdminDashboard`, `ScenarioBrowser`, `AudioDashboard`, `CertificationDashboard`, and `FactoryOperations`.
- **Data Source:** Uniquely, it bypasses the backend API for structural data, instead using Vite's `import.meta.glob` to read the Factory JSON reports directly from the file system.
- **Mocked Backend:** While it reads Django data for users/analytics, it utilizes mock adapters where the backend is not yet fully scaffolded to ensure unblocked frontend development.

## 10. Factory V2 Scripts

The `scripts/` directory is the engine of Parla Italiano.
**Generation Scripts:**
- `linguistic_extractor.py`: Extracts tokens.
- `curriculum_designer.py`: Scaffolds the 6 lessons.
- `distractor_generator.py`: Generates multiple choices.
- `audio_manifest_updater.py`, `global_dictionary_generator.py`.
- `build_and_certify_scenario.py`: Orchestrates the whole build pipeline.

**Audit & Certification Scripts:**
- `certify_scenario.py`, `certify_all.py`: Orchestrators.
- Dozens of specific audits: `audio_audit.py`, `conversation_audit.py`, `curriculum_audit.py`, `scenario_integrity_audit.py`, `domain_audit.py`, `lesson_quality_audit.py`.

## 11. Source of Truth Analysis

The architecture enforces a strict downward cascade to guarantee data integrity:
- **`conversations.json`**: **SOURCE OF TRUTH**. The creative core.
- **`vocabulary.json`, `phrases.json`, `sentences.json`**: **GENERATED**. Derivative artifacts mapped directly from conversations.
- **`mini_lessons.json`**: **GENERATED**. Derived chunking of linguistic artifacts.
- **`global_dictionary.json`**: **GENERATED**. Aggregated projection of all scenario vocabularies.
- **Dexie Database (`db.ts`)**: **RUNTIME ONLY**. The browser ingests JSON exports at runtime to populate UI components.

## 12. Active vs Dead Code

- **Active Elements**: `GlobalProgressService`, `CurriculumAdaptationService`, `ConversationReinforcementService`, `progressStore.ts`, the new `/admin` screens. Factory V2 Python Scripts.
- **Dead/Deprecating Elements**: The original `srsStore.ts` (currently bridging to `GlobalProgressService`, slated for removal). Legacy `scenario_vocabulary` tables (must be kept for migrations but will be unused by V3).

## 13. Data Flow Diagrams

### Content Generation Flow
```text
[LLM Agent] -> conversations.json 
                      |
                      v
[linguistic_extractor.py] -> vocabulary.json, phrases.json, sentences.json
                      |
                      v
[curriculum_designer.py] -> mini_lessons.json
                      |
                      v
[certify_scenario.py] -> Validation Markdown/JSON Reports
```

### Hybrid Mastery Runtime Flow
```text
[corpusLoader.ts] -> Loads Scenario JSON 
                      |
                      v
[CurriculumAdaptationService] -> Queries db.global_progress
                      |
                      v
[VocabularyTrainingScreen] -> Displays Filtered Vocab (Safety Floor = 2)
                      |
                      v
[GlobalProgressService] -> Writes to db.global_progress + db.global_review_history
                      |
                      v
[apiClient.ts] -> Syncs to Django Backend
```

## 14. Learning System Analysis

**Current Methodology:**
The learner relies heavily on receptive skills. The loop is: Read/Hear Italian -> Identify correct English translation (or vice-versa) from 4 choices.

**Weaknesses:**
- **Lack of Active Production:** The system currently does not require the user to actively generate Italian text or speak Italian into a microphone. It is a highly optimized multiple-choice engine.
- **Context Silos (V1):** Prior to Hybrid Mastery V2, the learner could "master" a word in Scenario 1 and be forced to relearn it from scratch in Scenario 10. Hybrid Mastery mitigates this.

## 15. Redesign Readiness

If the UI/UX is redesigned, the following must be adhered to:
**Preserve:**
- The Factory Pipeline (Python scripts). Any change to learning models must happen *downstream* in the UI or DB, never upstream by hand-editing `conversations.json` or `mini_lessons.json`.
- The Deterministic Audio System (hashing logic in `audio_manifest.json`).
- The Dexter IndexedDB schema layout to prevent migration failures.

**Can Safely Change:**
- The React component visual layer (`src/screens/*`).
- The specific FSRS-lite weighting algorithm in `globalProgressService.ts`.
- The backend Django endpoints (provided they fulfill the sync contract).
