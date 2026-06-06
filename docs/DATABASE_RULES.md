# Database Governance & Rules

## 1. Current Dexie Schema (V1)
- `scenarios`: Metadata.
- `scenario_vocabulary`: Local extracted words.
- `scenario_phrases`: Local extracted phrases.
- `scenario_sentences`: Local extracted sentences.
- `srs_items`: Local fallback tracking.

## 2. Future Hybrid Mastery Schema (V2)
- `global_dictionary`: The definitive word list (`id`, `italian`, `english_primary`, `audio_json`).
- `scenario_vocab_mapping`: Relational join table (`scenario_id`, `global_dict_id`, `sort_order`).
- `core_phrases`: (Optional) Global conversational connectors.

## 3. Mandatory Migration Rules
1. **Never delete tables during migration.** Deprecated tables (like `scenario_vocabulary`) must be retained in the schema definition but ignored by active code until V3.
2. **Always support rollback.** Before running `migrate_to_v2.ts`, the app must dump the user's `srsStore` state into a backup IndexedDB table (`srs_backup_v1`).
3. **Always preserve user progress.** Use the "Max Streak" rule when merging hundreds of duplicate local IDs into a single global ID.
4. **Create new tables before deprecating old ones.**

## 4. Versioning Rules
- Database versions MUST strictly increment `SEED_VERSION` in `db.ts`.
- Any change to the corpus structure in the Python factory requires a corresponding `SEED_VERSION` bump so the client knows to purge and reload the base JSON data.

## 5. Naming Conventions & Index Rules
- **Vocabulary IDs:** `word_[normalized]` (e.g., `word_grazie`).
- **Concept Overrides:** `concept_[english]_[normalized]` (e.g., `concept_floor_piano`).
- **Local IDs:** `p1`, `s1` (prefix-free in JSON, resolved at runtime to `s22-p1`).
- **Indexes:** The mapping table MUST have a compound index on `[scenario_id+global_dict_id]` for fast runtime filtering.
