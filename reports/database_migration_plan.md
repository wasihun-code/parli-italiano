# Database Migration Plan

To support Hybrid Mastery, the IndexedDB schema managed by Dexie (`src/lib/db.ts`) requires structural changes. No implementation is performed in this phase.

## Current Schema (Excerpt)
- `scenario_vocabulary`: `id, scenario_id, sort_order`

## Future Schema

### 1. `global_dictionary`
The unified source of truth for all vocabulary.
- **Primary Key:** `id` (string). Format: `word_[normalized]` or `concept_[context]_[normalized]`.
- **Indexes:** `normalized_text`
- **Fields:** `italian` (string), `english_primary` (string), `audio_json` (string).

### 2. `scenario_vocab_mapping`
Many-to-many relationship linking a scenario to its required global vocabulary.
- **Primary Key:** `[scenario_id+global_dict_id]` (compound).
- **Indexes:** `scenario_id`, `global_dict_id`.
- **Fields:** `sort_order` (integer).

### 3. `core_phrases`
A small subset of highly common conversational glue.
- **Primary Key:** `id` (string). Format: `phrase_[normalized]`.
- **Fields:** `italian` (string), `english_primary` (string), `audio_json` (string).

## Tables to be Dropped
- `scenario_vocabulary`

## Remote Backend Mirror (Django)
If synced, the backend requires identical tables to support cross-device progression and admin analytics:
- `GlobalDictionary`
- `CorePhrase`
- `UserSrsProgress` (Tracks `item_id`, `ease_factor`, `interval`, `due_at`).
- `ReviewHistory` (Append-only log for analytics).
