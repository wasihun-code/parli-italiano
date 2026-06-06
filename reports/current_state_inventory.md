# Current State Inventory

This report details the current architecture and state of the Parla Italiano platform prior to the Hybrid Mastery V2 migration.

## 1. Database (Dexie: `src/lib/db.ts`)
- **Current Purpose:** Stores extracted scenario data (vocabulary, phrases, sentences, mini-lessons) using scenario-specific IDs (e.g., `s22-v1`).
- **Future Purpose:** Will transition `scenario_vocabulary` to a relational model (`global_dictionary` and `scenario_vocab_mapping`). Phrases and sentences will remain scenario-specific.
- **Migration Risk:** **HIGH**. Altering indexedDB schemas requires careful versioning (`SEED_VERSION`) and data migration logic to avoid corrupting existing offline data.

## 2. Progress State (Zustand: `src/store/progressStore.ts`)
- **Current Purpose:** Tracks high-level scenario completion via boolean flags (`vocabularyCompleted: boolean`, `phraseCompleted: boolean`, etc.).
- **Future Purpose:** `vocabularyCompleted` will become a dynamic getter that checks the global SRS store against the `scenario_vocab_mapping`.
- **Migration Risk:** **MEDIUM**. Logic must shift from static writes to dynamic reads without causing infinite re-renders.

## 3. SRS Engine (Zustand: `src/store/srsStore.ts`)
- **Current Purpose:** Tracks spaced repetition using scenario-specific IDs (`s22-v15`). Employs a basic streak system.
- **Future Purpose:** Will track global IDs (`word_grazie`). Will implement the FSRS-Lite algorithm for intervals.
- **Migration Risk:** **HIGH**. The core algorithm is being replaced. Existing user progress must be translated from hundreds of local IDs to their global counterparts.

## 4. Training Screens (e.g., `VocabularyTrainingScreen.tsx`)
- **Current Purpose:** Loads a static array of exercise IDs from a scenario's mini-lesson and forces the user to drill them via flashcards until `streak >= 3`.
- **Future Purpose:** Will dynamically filter out exercise IDs if `globalSrsStore[global_id].learned === true`. Will auto-complete if the array is empty.
- **Migration Risk:** **MEDIUM**. Complex state management required to handle instant auto-completion and UI transitions.

## 5. Conversation Engine (`ScriptedConversationScreen.tsx`)
- **Current Purpose:** Renders static, branching dialogue trees. Success grants generic XP and marks the conversation as complete.
- **Future Purpose:** Will parse the text of the conversation upon completion, identify all used `global_dict_id`s, and award "Implicit Review Credit" to the `srsStore`.
- **Migration Risk:** **LOW**. The conversation UI itself doesn't change; only the `onComplete` handler logic expands.

## 6. Admin Panel (`src/screens/admin/`)
- **Current Purpose:** Reads current corpus data and provides high-level metrics. Factory execution is mocked.
- **Future Purpose:** Will gain a Global Dictionary viewer and advanced SRS analytics (retention rates, most difficult words).
- **Migration Risk:** **LOW**. Admin panel is internal and easily updated.
