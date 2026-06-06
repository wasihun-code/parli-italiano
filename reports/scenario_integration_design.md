# Scenario Integration Design

A critical challenge in Hybrid Mastery is handling scenarios that contain a mix of completely new vocabulary and globally mastered vocabulary.

## 1. The Pedagogical Dilemma
*Scenario Example:* Ordering Pizza.
*Vocab:* `pizza`, `pomodoro`, `grazie`, `conto`.
*User State:* Knows `grazie` and `conto`. Does not know `pizza` or `pomodoro`.

### Options Evaluated:
A. **Hide them completely:** The scenario acts as if `grazie` doesn't exist. (Fails to reinforce context).
B. **Mark them:** Show them in the lesson, but with a "Known" badge. (Causes flashcard fatigue).
C. **Make them optional:** Add a "Skip known words" button. (Adds UI clutter).
D. **Review them:** Force the user to review them before starting. (Derails the scenario flow).

## 2. Recommended Behavior: The "Skip-and-Contextualize" Model

The optimal integration seamlessly blends Global Knowledge into Scenario mastery:

### Step 1: Lesson Adaptation (Hiding the Flashcards)
- When the user enters the **Vocabulary Mini-Lesson** for "Ordering Pizza", the system fetches the global `srsStore`.
- `word_grazie` and `word_conto` have `learned == true`.
- These words are **silently filtered out** of the active flashcard queue for that specific lesson.
- The user only drills `pizza` and `pomodoro`.
- If *all* words in the lesson are known globally, the lesson instantly displays a "Completed" animation and grants XP.

### Step 2: Conversation Adaptation (Contextual Review)
- When the user reaches the **Conversation Phase**, the full, unedited dialogue is presented.
- The user must read, hear, and interact with sentences containing `grazie` and `conto` alongside the new words.
- *Why?* This provides powerful, implicit "contextual review." The user proves they still know the word by succeeding in the conversation, without suffering through an explicit flashcard drill.

### Step 3: Progression Logic
A scenario's Conversation Phase is unlocked when:
1. All scenario-specific Phrases are `Completed` (Score >= 85).
2. All scenario-specific Sentences are `Completed` (Score >= 80).
3. **All** global vocabulary mapped to this scenario is marked as `LEARNED` or `MASTERED` in the global `srsStore`.
