# Phrase Mastery Model

## Lifecycle
- **NEW**: User starts the Phrase lesson.
- **LEARNING**: User completes flashcard exercises within the lesson.
- **LEARNED**: Phrase lesson completed with >= 85% accuracy.
- **MASTERED**: The scenario's Conversation Phase is successfully completed using this phrase.
- **LAPSED**: (N/A for local phrases. See below).

## SRS Decision
**Recommendation: C. No long-term SRS for Scenario Phrases.**

*Why?* Phrases (like "Vorrei un tavolo per due") are structural chunks used to scaffold the learner toward the conversation. Their purpose is immediate situational fluency, not isolated long-term memorization. 

The underlying *Vocabulary* ("tavolo", "due") is already tracked in the Global SRS. Memorizing thousands of highly specific phrases via flashcards violates the "Minimum Information Principle" of spaced repetition and leads to catastrophic user burnout.

Phrase mastery is achieved and proven contextually within the scenario's Conversation. Once the scenario is passed, the phrase does not need to return as an isolated flashcard.
