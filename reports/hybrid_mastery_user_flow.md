# Hybrid Mastery User Flow

## 1. The Learner Perspective

The primary goal of the Hybrid Mastery migration is to eliminate "flashcard fatigue."

### Scenario 1: The First Encounter (e.g., "Airport Arrival")
- The user starts learning Italian.
- They encounter the word "grazie" (`word_grazie`) for the very first time.
- They see the flashcard, hear the audio, and answer it correctly 3 times.
- **State Change:** `word_grazie.learned = true`.

### Scenario 2: The Next Day (e.g., "Hotel Check-In")
- The user opens "Hotel Check-In," which also heavily features the word "grazie".
- **The Magic Moment:** The UI displays a brief notification: *"5 words already known from previous lessons!"*
- The vocabulary training screen completely skips "grazie". The user focuses only on truly new words like "prenotazione" (reservation).
- The user still reads and hears "grazie" during the full *Conversation* exercise, reinforcing the word in context without the tedium of re-learning its basic definition.

## 2. Marking, Hiding, and Reviewing

### Marking vs. Hiding
- **In Vocabulary Lessons:** Known words are **Hidden**. They do not appear in the learning carousel unless they are specifically due for an SRS review.
- **In UI/Progress Screens:** Known words are **Marked** with a checkmark or gold color in the Scenario Detail view, showing the user they are accumulating permanent knowledge.

### The Review Flow
- Words due for SRS review are pooled into a global **"Daily Review"** module. 
- If a user has unreviewed words, the app prompts them to complete a global review session before starting a new scenario, rather than injecting old reviews awkwardly into a new topic.

## 3. Changes to Progress Screens

- **Home Screen:** Replaces the generic "XP" or "Scenarios Completed" primary metric with a concrete proficiency score: **"Vocabulary Size: 450 Words"**.
- **Scenario Detail Screen:** 
  - Instead of "0/40 Words Mastered," it will display: 
    - "New Words to Learn: 15"
    - "Already Known: 25"
  - This gamifies the experience. As the user completes more of the curriculum, new scenarios become visually "easier" to start because the user has built a massive global vocabulary foundation.
