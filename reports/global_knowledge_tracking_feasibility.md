# Global Knowledge Tracking Feasibility Report

This report evaluates the viability of migrating Parla Italiano from its current "Scenario Mastery" architecture to a "Global Knowledge Mastery" architecture.

## 1. Current Architecture: Scenario Mastery
The application currently tracks learning progress locally within the context of each isolated scenario. When a user encounters a word like "grazie" in the "Ordering Pizza" scenario, they learn it as ID `s29-v14`. When they encounter "grazie" again in "Hotel Check-In", they learn it as a completely new entity, ID `s17-v42`.

### Pros
- **Simplicity:** Extremely easy to conceptualize, debug, and reset. Progress is a simple boolean switch at the scenario level.
- **Contextual Isolation:** Allows users to practice the same word in different grammatical or situational contexts without cross-contamination of spaced repetition (SRS) penalties.
- **Database Locality:** Extracting and loading data for a specific training screen requires zero cross-referencing against a global dictionary.

### Cons
- **Massive Redundancy:** Forensic analysis reveals that over 50% of the 5,294 unique extracted vocabulary words appear in multiple scenarios. "grazie" alone is duplicated 119 times.
- **User Fatigue:** Users are forced to manually "learn" basic words like "sì", "no", and "grazie" over a hundred times, leading to severe pedagogical friction and frustration.
- **No True Language Profile:** The system cannot answer the fundamental question "How many Italian words does this user actually know?" It only knows how many scenario JSON files they have completed.

## 2. Future Architecture: Global Knowledge Mastery (Knowledge Graph)
A Global Knowledge Mastery architecture would decouple tracking from the scenario JSON files. Instead of tracking arbitrary IDs (`s29-v14`), the SRS database would track a normalized string hash or a central dictionary ID representing the actual Italian concept (e.g., `word_grazie`).

### Pros
- **Zero Redundancy:** A user learns "grazie" once. When they open a new scenario, the system automatically detects that "grazie" is already in their global knowledge graph and skips it in the vocabulary training screen.
- **Cross-Scenario Unlocking:** Mastering enough foundational words could automatically unlock complex conversations across multiple scenarios simultaneously, providing a "magic" and highly rewarding user experience.
- **Accurate Analytics:** The platform could accurately report "You know 1,200 Italian words" and construct a true language proficiency model (A1/A2 scoring).

### Cons
- **Context Loss:** "Piano" means "floor" in a hotel, but "slowly" when asking for clarification. Tracking by a global string (`word_piano`) merges these distinct concepts, which could confuse the SRS algorithm if the user knows one definition but not the other.
- **Significant Migration Complexity:** The entire backend pipeline and frontend tracking logic would require a massive refactor.

## 3. Migration Complexity Estimation: HIGH

Transitioning to a Global Knowledge Tracking architecture requires a fundamental rewrite of several core systems:

1. **Extraction Pipeline Refactor:** `linguistic_extractor.py` must be rewritten. Instead of generating `v1`, `v2`, etc., it must either generate a deterministic ID based on the word itself (e.g., a hash of the Italian text + English translation to solve the "piano" context issue) or look up against a master `global_dictionary.json`.
2. **Curriculum Mapping Rewrite:** `mini_lessons.json` and `scenarioMapping.ts` would need to be updated to reference global IDs instead of scenario-prefixed IDs.
3. **Frontend Store Overhaul:** `srsStore.ts` and `progressStore.ts` must be refactored to check global mastery states. Training screens (`VocabularyTrainingScreen.tsx`) would need logic to dynamically skip items that exist in the scenario's payload but are already marked as `learned: true` in the global store.
4. **Data Migration:** Any existing user progress tied to scenario-prefixed IDs would be lost unless a complex migration script is written to map old IDs to the new global identifiers.

**Conclusion:** 
While the current architecture is computationally simple, the pedagogical cost of forcing users to relearn "grazie" 119 times is unacceptable for a production-grade language application. The migration is highly complex but absolutely necessary for the long-term viability of Parla Italiano.
