# Phase 7.5 — Safety Rules

## The "Empty Lesson" Problem
If a mini-lesson contains 5 vocabulary words and the user has globally `MASTERED` all 5, applying the strict Adaptation Design rules would result in an empty exercise array (length 0). This causes a UI crash or an immediate "All Learned!" screen, destroying the pacing.

## The Safety Floor
Every lesson section MUST present a minimum of **2** interactive elements to the user to maintain the rhythm of learning and provide a contextual warm-up.

### Algorithm
1. The `curriculumAdaptationService` processes the initial list of 5 words.
2. It identifies 0 `Visible` words and 5 `Hidden` words.
3. **Safety Check:** Is `Visible.length < 2`?
4. **Resolution:** If yes, the service backfills the `Visible` array by pulling items from the `Hidden` array until `Visible.length == 2`.
5. **Selection Criteria:** When backfilling, prioritize items with the lowest `mastery_level` or the longest time since `last_reviewed_at`.
6. **Flagging:** These backfilled items are flagged as `isContextualRefresh: true`.

### UI Handling of Contextual Refresh
When a word flagged as `isContextualRefresh` is presented in the `VocabularyTrainingScreen`, the UI should:
- Skip the initial "Presentation/Flashcard" phase (the user already knows the word).
- Jump straight to a low-friction multiple-choice or listening exercise.
- Display a subtle "Warm-up" badge instead of a "New" badge.
