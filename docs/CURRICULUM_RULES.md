# Curriculum Generation Rules

## Core Philosophy
**The Conversation is the Source of Truth.**
We do not build lessons and hope they apply to real life. We build real-life conversations first, and extract the lessons from them.

## The Generation Pipeline

Future scenario generation MUST follow this exact, unyielding pipeline:

1.  **Conversation Generation**
    *   Write the branching dialogues (`conversations.json`) first.
    *   Ensure they meet A1-A2 complexity and length requirements.

2.  **Linguistic Extraction**
    *   Parse the conversations to extract the complete language inventory.
    *   Host lines → Sentences
    *   User correct choices → Phrases
    *   All unique words (cleaned, >2 chars, non-numeric) → Vocabulary

3.  **Distractor Generation**
    *   Generate plausible distractors for all items.
    *   Distractors must be sourced from the extracted inventory of the same scenario.

4.  **Lesson Assembly**
    *   Divide the inventory into progressive chunks.
    *   Create 5-6 mini-lessons.
    *   Each lesson must have a Title, a pedagogical Goal, and sections for Vocab, Phrases, Sentences, and a Mastery Check.

5.  **Coverage Validation**
    *   Run `scripts/curriculum_audit.py`.
    *   **Rule:** Every word, phrase, and sentence in the conversations MUST exist in the mini-lessons.
    *   Lessons and conversations are never allowed to diverge. If conversation text changes, the curriculum must be re-extracted.
