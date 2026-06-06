# UI Migration Plan

## 1. Home Screen
- **Current State:** Lists scenarios. Shows "XP" and a daily streak.
- **Future State:** A new "Global Knowledge" banner at the top displaying "Vocabulary Size" and "Mastered Words". A prominent "Daily Review" button if items are pending.
- **Migration Risk:** LOW. Mostly additive UI.

## 2. Scenario Screen
- **Current State:** Lists 6 mini-lessons, showing completion stars.
- **Future State:** Vocabulary lessons will show a split progress bar: "Known (Green)" vs "New (Blue)". If a lesson is 100% known globally, it renders as a "Free Pass" completed state.
- **Migration Risk:** MEDIUM. Requires complex conditional rendering based on global store getters.

## 3. Mini Lessons (VocabularyTrainingScreen)
- **Current State:** Cycles through a static array of flashcards.
- **Future State:** Dynamically filters the `exerciseIds` array passed via router state. If empty, immediately redirects to the success screen.
- **Migration Risk:** HIGH. Interfering with the flashcard carousel logic can cause index-out-of-bounds crashes.

## 4. Conversations
- **Current State:** Standard text tree.
- **Future State:** No visual changes. Silent dispatch on completion to update the `srsStore`.
- **Migration Risk:** LOW.

## 5. Profile
- **Current State:** Shows generic XP.
- **Future State:** Shows detailed SRS metrics (Retention Rate, Current Lapses).
- **Migration Risk:** LOW.

## 6. Review Queue (NEW)
- **Current State:** N/A.
- **Future State:** A new `/review` route. Uses the existing flashcard component but feeds it from the `getDueItems()` selector instead of a scenario payload.
- **Migration Risk:** LOW.

## 7. Admin Panel
- **Current State:** Displays scenario counts and mock metrics.
- **Future State:** Integrates a Global Dictionary viewer and real retention analytics.
- **Migration Risk:** LOW.
