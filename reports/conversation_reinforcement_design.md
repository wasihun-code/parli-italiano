# Conversation Reinforcement Design

Conversations are the ultimate assessment in Parla Italiano. They also serve as the most powerful engine for Implicit Learning.

## Mechanisms of Reinforcement

1. **Can conversation success reinforce vocabulary?**
   **YES.** This is the cornerstone of Hybrid Mastery V2. When a user completes a conversation, the system should parse the host lines and chosen user responses. Any `global_dict_id` present in that conversation receives "Implicit Review Credit." If `word_chiave` was due for an SRS review, encountering and understanding it in the conversation counts as a successful "Easy" review, pushing its SRS interval forward without requiring a flashcard.

2. **Can conversation success reinforce phrases?**
   **YES.** Successfully choosing a phrase within the branching dialogue is the final proof of phrase mastery. It locks in the `phraseCompleted` flag for the scenario.

3. **Can conversation success replace explicit review?**
   **YES.** As a learner progresses to higher scenarios, they will naturally encounter common words (`grazie`, `avere`, `essere`) in conversations constantly. This implicit contextual review entirely replaces the need for explicit flashcards for those words, preventing the Daily Review queue from overflowing.

4. **Can conversations generate mastery credit?**
   **YES.** A conversation completion acts as an event trigger for the `srsStore`, dispatching a batch update to all known vocabulary utilized within that specific dialogue path.
