# Daily Review System Design

To handle the Spaced Repetition logic without polluting individual scenarios, Parla Italiano requires a dedicated "Daily Review" module.

## 1. Review Constraints & Guidelines

- **Maximum Reviews per Day:** Hard cap of 100 items to prevent review burnout.
- **Minimum Session:** 10 items per batch. (If a user has 45 items due, they can do them in batches of 10-15).
- **Overdue Handling:** If a user misses several days and accumulates 500 reviews, the system still enforces the 100/day cap. The algorithm prioritizes the most critical items first.

## 2. Queue Prioritization

When building a Daily Review batch, the system sorts items in the following priority order:

1. **`RELEARNING` (Lapses):** Items the user recently failed and is trying to refresh. These have the highest pedagogical urgency.
2. **`LEARNING` (Interday Steps):** Items introduced yesterday that require their first 24h reinforcement.
3. **`REVIEW_DUE` (Overdue):** Mature items whose timers have expired. Sorted by `due_at` ascending (oldest first).

## 3. The Review Screen UI

- **Location:** Accessible prominently from the Home Screen. "Start Daily Review".
- **Interface:** Fast, swipeable flashcard interface (similar to the current `VocabularyTrainingScreen`).
- **Data:**
  - Front: Audio plays + Italian text (or multiple choices).
  - Back: English translation + Example Context sentence (pulled from one of the scenarios the word belongs to).
- **Completion:** Upon finishing the batch, the user is awarded XP and a "Streak Freeze" token (if applicable).

## 4. Interaction with Scenarios

If the user has >20 pending Daily Reviews, attempting to start a *New Scenario* will trigger a soft warning:
> "You have vocabulary waiting to be reviewed! Refresh your memory before learning new words."
(They can bypass this, but it gently nudges them toward healthy SRS habits).
