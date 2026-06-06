# Hybrid Mastery System Design

## 1. System Overview
The Hybrid Mastery system decouples Vocabulary from individual Scenarios, moving it to a Global Knowledge Graph, while keeping Phrases and Sentences strictly Scenario-bound to preserve context.

## 2. Handling Known Words in New Scenarios
When a learner encounters a "known" word (e.g., `word_grazie`) in a new scenario:
- The system checks the global `srsStore`.
- If `globalKnowledge[word_grazie].learned === true`, the word is considered mastered.
- **Action:** The word is *Hidden* from the introductory vocabulary flashcard phase of the new scenario. It is *Not* presented as a new concept to learn.

## 3. Lesson Adaptation
- **Static Curriculum:** `mini_lessons.json` remains static and maps all extracted global IDs (so the factory guarantees 100% extraction coverage).
- **Dynamic Runtime:** The React `VocabularyTrainingScreen` dynamically filters the `exerciseIds` array against the user's global progress.
- **Auto-Completion:** If a mini-lesson section consists entirely of already-mastered global words, the section is automatically marked complete and skipped, creating a "magic" unlocking effect for the user.

## 4. Conversation Adaptation
- Conversations remain **static text**. 
- The user is still tested on the full conversation, reinforcing how their globally known vocabulary applies in a new, specific context.
- Distractor choices in conversations remain intact.

## 5. Spaced Repetition (SRS) Integration
- Spaced repetition operates exclusively on the **Global ID**.
- If a user learns `word_grazie` in Scenario A, its `dueAt` timer starts.
- If the user opens Scenario B and `word_grazie` is due for review, it will be injected into a **Global Review Queue** presented either before the scenario starts or in a dedicated "Daily Review" tab, rather than interrupting the flow of Scenario B's unique new vocabulary.

## 6. Mastery Calculation
Mastery transitions from a purely local calculation to a composite one.
- **Vocabulary Mastery:** `scenario_vocab_mastery` = 100% when all global IDs mapped to the scenario have `learned === true` in the global store.
- **Phrase/Sentence Mastery:** Remains local (`phraseScore >= 85`, `sentenceScore >= 80`).
- **Scenario Mastery:** Unlocked when the user achieves Phrase/Sentence mastery AND possesses the prerequisite Global Vocabulary mastery.

## 7. Factory & Certification Changes
- **Linguistic Extractor:** Must generate global deterministic IDs (e.g., `word_grazie` or `concept_floor_piano`) instead of `v1`.
- **Integrity Audit:** The bidirectional coverage audit (`scenario_integrity_audit.py`) will verify that `mini_lessons.json` maps 100% of the *Global IDs* extracted for that specific scenario.
- **Translation Audit:** The factory must ensure that the translation for a Global ID does not conflict across different scenarios (enforcing polysemy handling via `concept_` overrides).

## 8. Admin Panel Visualization
- **Global Knowledge Dashboard:** A new view in the Admin Panel showing the entire Italian dictionary extracted by the factory.
- **Metrics:** Displays global frequency (e.g., "grazie: 119 uses") and cross-references all scenarios utilizing a specific Global ID.
- **User Management:** Will display "Known Words: 1,452 / 3,845" instead of just "Completed Scenarios", providing a true CEFR-aligned proficiency score.
