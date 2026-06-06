# Parla Italiano: Architecture

## 1. Source Of Truth Hierarchy
Parla Italiano operates on a strict, cascading source-of-truth model. Upstream artifacts define downstream artifacts.

`Conversation` → `Extraction` → `Curriculum` → `Certification`

1. **Conversations (`conversations.json`)**: The absolute source of truth. All learning material derives from the dialogues.
2. **Extraction (`vocabulary.json`, etc.)**: Deterministically parsed from conversations.
3. **Curriculum (`mini_lessons.json`)**: Deterministically chunked from extracted data.
4. **Certification**: Mathematically proves the integrity of steps 1-3.

## 2. Factory Architecture (V2)
The Scenario Factory is an automated Python pipeline.
- **Data Flow:** `Agent 1/2` writes conversations -> `linguistic_extractor.py` tokenizes -> `curriculum_designer.py` maps to 6 lessons -> `distractor_generator.py` adds choices -> `build_and_certify_scenario.py` audits.
- **Constraint:** Determinism. LLMs generate the creative conversations; Python scripts handle the rigorous data mapping.

## 3. Learning Architecture
- **Current (V1):** Scenario Mastery. All progress is isolated within a scenario.
- **Future (V2):** Hybrid Mastery. Global Vocabulary layer supported by Scenario-bound contextual phrases and sentences.

## 4. Curriculum Architecture
- Every scenario contains exactly **6 Mini Lessons**.
- Lessons transition from Explicit (Vocabulary flashcards) to Implicit (Conversations).
- IDs are prefix-free within the JSON (e.g., `v1`, not `s22-v1`) to allow the `corpusLoader` to dynamically assign namespaces during ingestion.

## 5. Audio Architecture
- **Primary:** Explicit metadata paths (`/audio/123abc.opus`).
- **Fallback:** Deterministic hashing. If `audio` is missing, the frontend calculates `SHA1("text|voice")` to resolve the asset.
- Over 44,000 assets operate safely via the fallback hash method.

## 6. Admin Architecture
- A React-based, desktop-first operational control center (`/admin`).
- Bypasses traditional backend APIs by using Vite's `import.meta.glob` to read Factory JSON reports directly into the browser.
- **Data Flow:** Python Factory outputs `global_certification.json` -> React Admin Dashboard renders live metrics.

## 7. Hybrid Mastery Architecture (Target)
- **Database:** `global_dictionary` replaces `scenario_vocabulary`.
- **UI:** `VocabularyTrainingScreen` dynamically filters out globally known words based on the `scenario_vocab_mapping` table.

## 8. Certification Architecture
- A suite of isolated `.py` audits ensuring 100% compliance.
- Orchestrated by `certify_all.py` for global regressions.
- **Core Rule:** Bidirectional coverage (`extracted_ids == taught_ids`).
