# Mastery Database Specification

To support the Hybrid Mastery architecture, the underlying databases must be refactored. This specification outlines the required schema without executing any code.

## 1. Dexie Schema (Client-Side Curriculum)

The static curriculum database must transition from isolated arrays to a relational structure.

### `global_dictionary` Table
*Primary truth for all extractable words.*
- `id` (PK, string): The global identifier (e.g., `word_grazie`, `concept_floor_piano`).
- `italian` (string): Normalized Italian text.
- `english_primary` (string): Canonical translation.
- `part_of_speech` (string, optional).
- `audio_json` (string): Metadata or deterministic path.

### `scenario_vocab_mapping` Table
*Maps scenarios to their required global vocabulary.*
- `id` (PK, auto-increment integer).
- `scenario_id` (Index, integer): e.g., 22.
- `global_dict_id` (Index, string): e.g., `word_grazie`.
- `sort_order` (integer): For UI presentation.

### Unchanged Tables
- `scenarios` (id, title, category)
- `scenario_phrases` (id, scenario_id, italian, english...)
- `scenario_sentences` (id, scenario_id, italian, english...)

## 2. Zustand Schema (Client-Side Progress)

The `srsStore` manages the dynamic learning state.

### `SrsItem` Object
- `id` (string): Maps to `global_dict_id` for vocab, or `scenario_id-phrase_id` for phrases.
- `type` (enum): `'vocabulary' | 'phrase' | 'sentence' | 'foundation'`.
- `state` (enum): `'NEW' | 'LEARNING' | 'LEARNED' | 'REVIEW_DUE' | 'LAPSED' | 'RELEARNING' | 'MASTERED'`.
- `ease_factor` (float): Default 2.5.
- `interval` (float): Current interval in days.
- `due_at` (ISO string timestamp).
- `lapses` (integer): Number of times failed from LEARNED state.
- `streak` (integer): Consecutive correct answers.

## 3. Remote Backend Schema (Django PostgreSQL)

For cross-device sync and admin analytics, the backend must mirror the state.

### `GlobalDictionary` Model
- `id` (CharField, PK)
- `italian` (CharField)
- `english_primary` (CharField)

### `UserSrsProgress` Model
- `user` (ForeignKey -> User)
- `item_id` (CharField, indexed)
- `item_type` (CharField)
- `state` (CharField)
- `ease_factor` (FloatField)
- `interval` (FloatField)
- `due_at` (DateTimeField)
- `updated_at` (DateTimeField)

### `ReviewHistory` Model (Analytics)
*An append-only log of every SRS review to calculate retention curves.*
- `user` (ForeignKey -> User)
- `item_id` (CharField)
- `was_correct` (BooleanField)
- `duration_ms` (IntegerField)
- `created_at` (DateTimeField, auto_now_add=True)

## 4. Indexing & Performance
- **Dexie:** `scenario_vocab_mapping` MUST have a compound index on `[scenario_id+global_dict_id]` for rapid curriculum resolution during the `VocabularyTrainingScreen` mount phase.
- **Django:** `UserSrsProgress` requires a compound index on `[user_id+due_at]` to instantly query the Daily Review queue.
