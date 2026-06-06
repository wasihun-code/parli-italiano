# Global Mastery Recommendation

## Pedagogical Analysis

When a learner masters a common word like **"grazie"**, the system must decide how to handle future occurrences.

### Options:
**A. Never show again**
- *Result:* The word disappears from all future lessons and conversations. 
- *Flaw:* Unnatural. Conversations become Swiss cheese, missing crucial connecting words.

**B. Hide from vocabulary lessons, Still show in conversations**
- *Result:* The user skips the flashcard in the "Vocabulary" mini-lesson, but sees it in context during the Conversation exercise.
- *Benefit:* Reduces flashcard fatigue while maintaining contextual reading practice.

**C. Spaced repetition review**
- *Result:* The word appears in global SRS reviews, but is entirely decoupled from scenario progression.
- *Benefit:* Optimal for long-term memory.

**D. Hybrid model**
- *Result:* Vocabulary is tracked globally. If a user opens a new scenario containing "grazie", the vocabulary mini-lesson dynamically excludes it (or marks it pre-mastered). However, the word still appears in Phrases, Sentences, and Conversations to reinforce context.

### Recommended Approach: Hybrid Mastery

The **Hybrid Mastery** model is the pedagogically superior choice. 
- **Vocabulary** should be tracked via a Global Knowledge Graph. This provides accurate "Known Words" metrics and prevents flashcard fatigue.
- **Phrases, Sentences, and Conversations** should remain Scenario-Specific. Language is contextual. Mastering "piano" (floor) in a hotel scenario does not mean the user understands "piano" (slowly) in a clarification scenario. Phrases and sentences provide the necessary contextual scaffolding.

## Migration Impact Estimation

| System | Migration Risk | Impact Description |
| :--- | :--- | :--- |
| `linguistic_extractor.py` | **HIGH** | Must normalize strings, generate deterministic global IDs (`word_grazie`), and resolve homonyms/context clashes. |
| `curriculum_designer.py` | **HIGH** | Must map global IDs to scenarios and potentially adjust lesson chunking logic if globally known words are filtered out. |
| `srsStore.ts` | **MEDIUM** | Needs to transition from `scenario_id-vocab_id` composite keys to tracking global `word_id` states. |
| `progressStore.ts` | **MEDIUM** | Scenario unlocking logic must become dynamic (e.g., "unlock if all scenario-specific phrases are done AND all associated global vocab is known"). |
| `training screens` | **HIGH** | UI needs to fetch global SRS state to dynamically filter out known vocabulary before rendering a lesson. |
| `conversation engine` | **LOW** | Conversations remain static text. Tracking choices would just reference global IDs instead of local ones. |
| `Dexie schema` | **HIGH** | Requires a new `global_dictionary` table and a many-to-many relationship mapping scenarios to global dictionary IDs. |
| `certification pipeline` | **HIGH** | Audits must verify bidirectional coverage against the new global dictionary mapping, vastly increasing audit complexity. |

## Final Recommendation

Parla Italiano should migrate to a **Hybrid Mastery** architecture. 

**Why?**
The current Scenario Mastery model forces learners to redundantly master the same 2,000 common words across 116 scenarios, leading to massive pedagogical friction. However, moving *everything* (phrases and sentences) to a global model destroys situational context.

The Hybrid approach solves both:
1. **Global Vocabulary:** Build a `global_dictionary.json` and track single words globally.
2. **Contextual Application:** Keep phrases and sentences scenario-bound to test the application of that global vocabulary in real-world contexts.

This approach offers the most rewarding user experience (unlocking known words automatically) while preserving the high-quality, contextual immersion that Parla Italiano is built upon.
