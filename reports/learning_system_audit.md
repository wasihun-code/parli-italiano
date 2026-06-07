# Parla Italiano: Pedagogical Audit

## 1. Executive Summary

The Parla Italiano learning experience is a highly structured, recognition-focused journey designed to prepare learners for branching conversations. While the system effectively bridges vocabulary acquisition to situational context, the current "Apartment Key Pickup" implementation reveals significant pedagogical bottlenecks: extreme vocabulary density, alphabetical (non-pedagogical) ordering, and a heavy reliance on passive recognition over active production.

## 2. Learner Interaction Trace (Apartment Key Pickup)

### Lesson 1 - Finding the Entrance
- **Vocabulary (v1-v49):** Learner is hit with 49 words. Interactions: Flashcard -> Multiple Choice (EN->IT) -> Listening (Audio->EN).
- **Phrases (p1-p7):** Recognition of complex strings like "4832... tasto chiave. Ah sì, ha funzionato! Sto entrando."
- **Sentences (s1-s7):** Identifying host lines from a list of options.
- **Mastery:** Repeat the sentences.

### Lessons 2-6
- **Pattern repeats:** Each lesson introduces ~50 new words alphabetically and ~7 phrases/sentences.
- **Total Load:** By the end of Lesson 6, the learner has encountered **~300 unique tokens** alphabetically (from "abbassa" to "zerbino").

### The Conversation
- **Final Step:** The learner enters the "Smooth Check-In" or other branching paths.
- **Action:** Listen to host -> Choose 1 of 3 replies.

## 3. Skills Analysis

| Skill | Training Level | Mechanism |
| :--- | :--- | :--- |
| **Listening** | High | Every item has audio; specific "Listening" exercises in Vocab/Phrase/Sentence screens. |
| **Reading** | High | Primary interaction mode. Constant reading of Italian and English translations. |
| **Recall** | Low | Limited "Dictation" and "Fill-in-the-blank" exercises. Most activities are recognition-based. |
| **Writing** | Low | "Spelling" (Vocab) and "Dictation" (Sentence) require typing, but represent <15% of total volume. |
| **Speaking** | Minimal | A "Speaking" mode exists in `PhraseTrainingScreen` using Web Speech API, but frequently falls back to recognition. |

## 4. Exercise Typology

- **Recognition (~85%):** Multiple Choice (IT->EN, EN->IT), identifying audio, matching host lines.
- **Recall (~10%):** Fill-in-the-blank, Assembly (ordering words).
- **Production (~5%):** Spelling (typing words), Dictation, Speaking (if enabled).

## 5. Item Ordering Analysis

- **Vocabulary:** **Alphabetical**. (e.g., Lesson 1 starts with "abbassa", "abbassata", "accanto"). This is a major pedagogical weakness as it groups words by spelling rather than meaning or utility.
- **Phrases/Sentences:** **Complexity-based**. Sorted by word count and character length. This ensures a "shallow to deep" progression in terms of reading load.

## 6. Pedagogical Meaning vs. Chunking

The current lesson progression is **Mechanical Chunking**.
- The `curriculum_designer.py` script simply takes the total extracted lists and divides them by 6.
- There is no semantic relationship between the words in "Lesson 1" and the theme "Finding the Entrance" other than proximity in the alphabet. A learner might learn "abbassa" (lower) before "porta" (door) simply because of the letter 'A'.

## 7. Conversation Readiness

**Could a learner realistically complete the conversation?**
- **Technically: Yes.** The "Bidirectional Coverage" rule ensures every word in the conversation was "taught" in a lesson.
- **Practically: Difficult.** The cognitive load of 300 words taught alphabetically is overwhelming. However, because the conversation itself is multiple-choice (recognition), the learner can often "recognize" the correct reply based on keywords they just saw in Lesson 6.

## 8. Pedagogical Value Mapping

### High Value Activities
- **Scripted Conversations:** Provide the only "real" application of knowledge. Branching feedback explains *why* a choice was culturally or contextually wrong.
- **Dictation (Sentences):** Forces the learner to map sounds to spelling and syntax.

### Low Value Activities
- **Mass Vocabulary Flashcards:** Learning 50 words alphabetically in one sitting leads to high interference and low retention.
- **Alphabetical Recognition:** Matching "abbassa" to "lower" among other "A" words doesn't teach the situational use of the word.

## 9. Learner Journey Diagram

```text
START: Scenario "Apartment Key Pickup"
  |
  +-- Lesson 1 (Theme: Entrance)
  |     [49 Words (A-B)] -> [7 Phrases] -> [7 Sentences] -> [Mastery]
  |
  +-- Lessons 2-5 (Repeat Pattern)
  |     [Vocab C-Z] -> [Contextual Phrases] -> [Host Sentences]
  |
  +-- Lesson 6 (Theme: Keys)
  |     [Final Vocab] -> [Lockbox Phrases] -> [Final host lines]
  |
  +-- CONVERSATION SIMULATOR (The Goal)
  |     (A) "Smooth Check-In" (Success)
  |     (B) "Code Problem" (Troubleshooting)
  |     (C) "Wrong Building" (Edge Case)
  |
  +-- REINFORCEMENT
        [Global Dictionary Updates] -> [Mastery Badge]
```

## 10. Audit Findings Summary

1.  **Recognition Bias:** The system is an "Input Machine". It is excellent at training a learner to *understand* what is said, but provides almost no training on how to *construct* an original sentence.
2.  **Vocabulary Overload:** 50 words per mini-lesson is 5-10x the recommended cognitive load for a single learning session.
3.  **The "Alphabetical Trap":** Ordering vocabulary alphabetically destroys the "Theme" of the mini-lesson. Lesson 1 is titled "Finding the Entrance", but the vocabulary is simply the first 50 words of the scenario sorted A-Z.
4.  **Implicit Success:** The "Conversation Reinforcement" is a strong feature, as it rewards the learner for naturally encountering words in context, bridging the gap between flashcards and real use.
