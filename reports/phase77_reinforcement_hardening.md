# Phase 7.7 — Reinforcement Hardening

## 1. The Inflation Problem
Phase 7.6 allowed completing a conversation to reinforce *all* globally mapped vocabulary within that scenario. Audits proved this causes extreme inflation. An advanced user completing 5 conversations in 15 minutes could accrue 1,000+ SRS updates, artificially forcing hundreds of words into the `MASTERED` state and breaking the pedagogical curve.

## 2. Recommended Cap: 20 Words
We evaluated caps of 10, 20, and 30 words per conversation completion.
- **10 Words:** Too restrictive. Conversations often introduce 15-20 crucial new target words.
- **30 Words:** Too inflationary. 5 conversations = 150 implicit reviews, heavily skewing SRS models.
- **20 Words (Selected):** Perfect balance. It covers the core target vocabulary of a scenario while providing a small margin to reinforce crucial `LAPSED` or `LEARNING` words encountered in the dialogue.

## 3. Active Vocabulary Detection Rules
The `conversationReinforcementService` must strictly limit reinforcement to:
1. Words that exist in the `scenario_vocab_mapping`.
2. Words whose normalized Italian string appears in the **actual text of the conversation** (host messages + user choices).
3. Words that fit within the top 20 priority slots.
