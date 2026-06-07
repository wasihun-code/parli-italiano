# Phase 9.1: Learning Path Specification Report

This report defines the architectural blue-print for the Learning System V3 runtime engine.

## LEARNING FLOW

The V3 engine orchestrates four distinct object flows, each tailored to the linguistic granularity of the content.

### Vocabulary Flow
Vocabulary moves through a 9-step acquisition ladder. Unknown words prioritize **Recognition** (Listen, Match) before entering the **Recall** (Build, Recall) and **Production** (Dictation, Speaking) phases. This prevents cognitive overload by ensuring the user can identify a word before they are asked to spell or speak it.

### Phrase Flow
Phrases prioritize syntax over single-word meaning. The flow starts with **Reading** and **Listening** to establish the "sound" of the phrase, followed by **Build Sentence** to reinforce structural relationships between words.

### Sentence Flow
Sentences focus on complex syntactic patterns. V3 utilizes **Assembly** (scrambled construction) and **Recall** (Gap fill) to ensure users understand how verbs and nouns interact within a situation.

### Conversation Flow
The ultimate convergence point. A conversation is not just a lesson; it is the **Validation Phase**. Mastery of 80% of vocabulary is a hard gate for entry, ensuring the learner is prepared for situational branching.

## PROGRESSION FLOW

V3 enforces a non-linear but strictly phased progression:
`Recognition → Recall → Production → Conversation`

1.  **Recognition:** Receptive skills (Input).
2.  **Recall:** Stimulus-response connection (Bridge).
3.  **Production:** Generative skills (Output).
4.  **Conversation:** Integrated performance (Outcome).

## ADAPTATION FLOW

User paths dynamically shorten or deepen based on their Global Progress.

-   **New User:** Lengthy paths focusing on building a foundation.
-   **Intermediate User:** Accelerated paths that bypass low-level recognition for previously seen stems.
-   **Advanced User:** Rapid production checks and deep conversation branching.

## DETERMINISM FLOW

To ensure stability and testability, the Path Generator must be a pure mathematical function.

**Input State:**
- `ScenarioID` (Integer)
- `GlobalMastery` (Map<ID, Score>)
- `ReviewQueue` (List<ID>)

**Generator Logic:**
1. Filter out mastered items below the "Safety Floor".
2. Sort remaining items by `Conversation Chronology`.
3. Map items to `Phased Exercises` based on `Mastery Score`.
4. Output `OrderedExerciseSequence`.

**Mathematical Proof of Determinism:**
Since the `Conversation Chronology` is derived from an immutable JSON source of truth, and the `Mastery Score` is a fixed snapshot at the moment of request, the generator's sorting and mapping operations will always yield the same array index for every exercise. This eliminates "randomized noise" and allows for 100% reproducible learning sessions.
