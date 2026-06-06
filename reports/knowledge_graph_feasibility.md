# Knowledge Graph Feasibility

## Primary Identifier Strategy

### Option A: Normalized Word IDs (e.g., `word_grazie`)
- **Advantages:** Simple to generate programmatically via hashing or string replacement. 1:1 mapping with the vast majority of the corpus (3927/5293 words are safe).
- **Disadvantages:** Breaks completely on polysemy/homonyms. If `piano` means "floor" and "slowly", the system merges two distinct concepts into a single learning metric.

### Option B: Concept IDs (e.g., `concept_greeting_thanks`, `concept_floor_piano`)
- **Advantages:** Perfect pedagogical tracking. Never merges distinct meanings.
- **Disadvantages:** Impossible to generate deterministically from text alone. Requires an LLM to assign concept IDs to every extracted word, defeating the purpose of the deterministic Factory V2 extraction pipeline.

### Option C: Hybrid (Normalized Word IDs + Collision Fallbacks)
- **Advantages:** 90%+ of the corpus is handled deterministically via Option A. The 558 unsafe words are handled via a manual lookup dictionary (`concept_dictionary.json`) that maps the specific text+english pair to a concept ID.
- **Disadvantages:** Requires maintaining a manual override dictionary.

### Recommendation
**Option C (Hybrid)** is the most viable path forward for a deterministic, offline-first application.
