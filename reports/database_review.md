# Database Review — Phase 7.2

## 1. Compatibility with Future Dexie Schema (V2)
The proposed structures in `global_dictionary_prototype.json` and `scenario_vocab_mapping_prototype.json` align with the `DATABASE_RULES.md` for V2.
- **Global Dictionary:** Uses the mandated `word_[normalized]` and `concept_` ID formats.
- **Relational Mapping:** Implements the many-to-many relationship required for Hybrid Mastery.

## 2. Migration Readiness
- **Seeding:** The static JSON files are ready to be used as seed data for V2 IndexedDB tables.
- **Progress Preservation:** Transitioning requires a `legacy_to_global_map.json` from the factory to translate legacy `sXX-vYY` IDs to Global IDs.

## 3. Backward Compatibility
- **Coexistence:** V1 and V2 logic can coexist in the same schema. There is no risk of ID collision as naming conventions are distinct (`s[ID]-v[N]` vs `word_[normalized]`).

## 4. Naming Conventions & Indexing
- **Reconciliation:** The `scenario_id` in mapping must be reconciled between numeric IDs (used in IndexedDB `scenarios` table) and path slugs (used in `scenarioMapping.ts`). Consistency is required for join performance.
- **Mandatory Index:** A compound index on `[scenario_id + global_dict_id]` is required in `db.ts` to prevent UI stuttering when resolving curricula.
