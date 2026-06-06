# Final Phase 7 Recommendation

Based on the extensive forensic and architectural planning conducted, here are the final recommendations to transition Parla Italiano to Hybrid Mastery V2.

### 1. Is Hybrid Mastery V2 ready for implementation?
**YES.**
The architectural blueprints, database schemas, risk assessments, and migration strategies are fully documented. The factory is stable, and the flaws in the current Scenario Mastery model (e.g., 85% vocabulary redundancy causing severe user fatigue) mathematically justify the migration.

### 2. What is the safest implementation order?
A strict, bottom-up approach to prevent data corruption:
1. **Data:** Generate the Global Dictionary in the Python Factory.
2. **State:** Build the FSRS-Lite `srsStore` logic and test it in isolation.
3. **Migration:** Write and test the user data migration script.
4. **UI:** Update the training screens to consume the new state.
5. **Rollout:** Deploy behind a Feature Flag.

### 3. What should Phase 7.1 contain?
**Only Factory-Side Scripts.** Phase 7.1 must be restricted to modifying `linguistic_extractor.py` to output the `global_dictionary.json` and the mapping tables. The React frontend should not be touched until the Factory can flawlessly build and certify these new data structures.

### 4. What should NOT be implemented initially?
- **Do not implement Backend Database Syncing initially.** Keep the FSRS-Lite math entirely within the client-side Zustand/Dexie stores. Writing complex Django models and GraphQL/REST sync endpoints adds massive overhead. Syncing can wait for Phase 8.
- **Do not implement Concept Mapping initially.** Rely purely on `word_[normalized]` for the first iteration. The ~400 homonyms identified can tolerate slight ambiguity for now; attempting to build the manual `dictionary_overrides.json` file immediately will stall the engineering effort.

### 5. What is the minimum viable Hybrid Mastery system?
The absolute MVP consists of:
1. Extracting the `global_dictionary.json`.
2. A basic `DailyReviewScreen.tsx` that pops up before a scenario.
3. Updating `VocabularyTrainingScreen.tsx` to hide any word that the user has already answered correctly 3 times across *any* scenario. 

This MVP eliminates 90% of the user fatigue without requiring the complex FSRS-Lite algorithm or Conversation Reinforcement mechanics, which can be layered in subsequent iterations.
