# Parla Italiano: Gold Standard V1

## Purpose
This document defines exactly what qualifies a scenario as production-ready in the Parla Italiano ecosystem. The `apartment_key_pickup` scenario serves as the V1 reference implementation. No scenario will be shipped to learners unless it meets or exceeds these standards, mathematically proven by the Certification Pipeline.

## 1. Mini Lesson Requirements
* **Goal-Oriented:** Every lesson must have a descriptive pedagogical `goal` (e.g., "Finding the Entrance", not just "Lesson 1").
* **Structure:** Lessons must contain exactly 4 sections: Vocabulary, Phrases, Sentences, and a Mastery Check.
* **Duration:** Content length must be calibrated for 2–3 minutes of active learning.
* **Audio Leak Prevention:** Answer audio MUST NOT autoplay before the learner commits to a choice. Manual playback (via 🔊 buttons) must be available for all choices.
* **Completion Flow:** The final lesson must unlock the Scenario Conversations.

## 2. Conversation Requirements
* **Authenticity:** Minimum 4 scripted, branching conversations per scenario.
* **Length:** 10–20 turns per conversation.
* **Level:** A1-A2 focused. Short sentences. One idea per sentence.
* **Flow:** Must begin with the host speaking. Must have a clear beginning, middle, and end (e.g., from arrival to entering the apartment).
* **Immersive Mode:** Host text is initially hidden. Audio autoplays. User must actively choose to "Show Text".
* **User Audio:** User replies do not autoplay. A manual replay button is provided in the chat history.

## 3. Curriculum Coverage Requirements
* **Source of Truth:** Conversations dictate the curriculum.
* **Extraction:** All vocabulary, phrases, and sentences used in conversations MUST be extracted and taught in the mini-lessons.
* **Audit:** Coverage must be 100%. The learner must never encounter conversation language that has not been previously taught.

## 4. Distractor Requirements
* **Count:** Every node/exercise must have 3-4 choices (1 correct, 2-3 distractors).
* **Quality:** Distractors must be of similar length (+/- 40% of the correct answer), same topic, and same grammatical category.
* **Integrity:** No placeholders ("Distractor 1"). No duplicate choices. Correct answers must be randomized at runtime.

## 5. Audio Requirements
* **Coverage:** 100% of hosts lines, user choices, vocabulary, phrases, and sentences must have valid, playable audio.
* **Deduplication:** Audio generation must be deterministic. Existing assets must be reused if the text matches exactly. No duplicate files.

## 6. Translation Requirements
* **Coverage:** 100% of host lines and vocabulary items must have accurate English translations.
* **Quality:** No placeholder translations ("Translation of...").
* **UI:** Translations are hidden by default in conversations to encourage listening comprehension.

## 7. UI & Keyboard Accessibility Requirements
* **Immersion:** All learning activities (Lessons, Conversations) must use the Fullscreen Immersive Mode (no global nav/sidebars, centered max-width 900px, consistent padding).
* **Keyboard Shortcuts:**
  * `1-4`: Select choice
  * `Enter`: Submit / Continue
  * `Space`: Replay target/host audio
  * `T`: Toggle translation
  * `Esc`: Exit activity

## 8. Certification Requirements
* Every scenario must pass the automated Certification Pipeline (`scripts/certify_scenario.py`).
* All audits must report `PASS` to generate a valid Certification Report.
