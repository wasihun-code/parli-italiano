# Global Dictionary Certification Rules

To pass Factory V2 Certification, the following conditions must be met:

1. **Coverage 100%:** Every extracted word must be present in the mapping table.
2. **Round Trip 100%:** Reconstructing the scenario from the mapping must yield the exact normalized Italian strings.
3. **Collision Resolution Documented:** Any homonym identified by the semantic checker must have an explicit `concept_` override in `dictionary_overrides.json`.
4. **No Missing Vocabulary:** The global dictionary cannot contain empty `italian` or `english_primary` fields.
5. **No Duplicate IDs:** The global dictionary keys must be strictly unique.
6. **No Broken Mappings:** No dangling foreign keys in the mapping table.
