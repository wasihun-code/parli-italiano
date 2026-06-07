# Learning System V3

## Goals
- Address the pedagogical weaknesses identified in the Phase 9.0 audits.
- Introduce dynamic, mastery-aware exercise selection.
- Enforce a strict "Recognition → Recall → Production → Conversation" progression flow.
- Maintain the integrity of the immutable Gold Standard curriculum and Factory V2 artifacts.
- Provide a robust runtime layer that orchestrates existing JSON assets into an adaptive learner journey.

## Architecture
Learning System V3 is strictly a **runtime layer**. It does not generate new static JSON files. It consumes the existing `vocabulary.json`, `phrases.json`, `sentences.json`, and `conversations.json` to generate dynamic learning paths. The system sits between the IndexedDB local store and the React Training Screens, orchestrating what exercises appear and in what order based on Global Progress.

## Data Flow
1. **Corpus Loader** loads standard scenario JSONs.
2. **Global Progress Service** queries user mastery states.
3. **Learning Path Generator (V3)** dynamically constructs a sequence of exercises.
4. **React Training Screens** render the exercises.
5. **Feedback Loop** writes success/failure back to Global Progress.

## Progression Philosophy
Exercises are no longer randomly or alphabetically presented. They follow a strict cognitive acquisition curve:
1. **Recognition:** Identifying the meaning (e.g., Flashcard, Multiple Choice, Listening).
2. **Recall:** Retrieving the word given context (e.g., Assembly, Fill-in-the-blank).
3. **Production:** Active generation of the target language (e.g., Dictation, Spelling, Speaking).
4. **Conversation:** Final situational application in scripted, branching dialogue.

## Interaction with Hybrid Mastery
V3 fully integrates with Hybrid Mastery. Known words (Globally Mastered) will skip Recognition and Recall phases, and may only briefly appear in Production or as contextual "Safety Floor" items in Mini Lessons.

## Interaction with Review Queue
FSRS-lite decay dictates when an item re-enters the active learning path. The Review Queue feeds items into the V3 Path Generator for daily reinforcement.

## Interaction with Conversations
Conversations remain the ultimate goal. The vocabulary presented in early lessons is dynamically re-sorted by V3 to prioritize words needed for the first turns of the conversation, breaking the "Alphabetical Trap."
