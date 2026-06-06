# Target Architecture Blueprint

## Current Architecture: Scenario Mastery
The system is heavily siloed. The database, progress stores, and UI all operate within the boundaries of a specific scenario.

```text
[Database]
Scenario A Vocab (s22-v1) --> [srsStore] (s22-v1: streak 3) --> [UI] "Vocab Done"
Scenario B Vocab (s17-v4) --> [srsStore] (s17-v4: streak 0) --> [UI] "Vocab Pending"
```

## Target Architecture: Hybrid Mastery V2
Vocabulary is lifted into a Global Knowledge Graph. Scenarios merely reference this graph. Phrases and Sentences remain local.

```text
[Database]
Global Dictionary (word_grazie) <----[Mapping]----> Scenario A
                                <----[Mapping]----> Scenario B

[srsStore]
(word_grazie: interval 14d)

[UI: Scenario A]
- Checks Mapping -> Requires 'word_grazie'
- Checks srsStore -> 'word_grazie' is LEARNED
- Result: Hides 'word_grazie' from flashcards.
```

## Component Roles in Target State
1. **Global Dictionary (`db.ts`)**: The source of truth for all vocabulary.
2. **Scenario Vocab Mapping (`db.ts`)**: Defines which global words are required to survive a specific scenario.
3. **Global Progress (`srsStore.ts`)**: Tracks FSRS-Lite mastery on global IDs.
4. **Review Queue (UI)**: A new daily interface to handle reviews decoupled from scenario progression.
5. **Conversation Reinforcement**: Completing a conversation reads the text, matches it to the Global Dictionary, and updates the `srsStore`.
