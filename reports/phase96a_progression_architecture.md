# Phase 9.6a: Progression Architecture (Hardened)

## 1. Mathematical Definitions

### A. Session Complete
- **State:** `current_step_index == session_length`
- **Persistence:** Write `is_completed: true` to `db.learning_sessions`.
- **Outcome:** Trigger "Success Sound", show Summary, redirect to Scenario Screen.

### B. Lesson Complete
- **State:** `ScenarioProgress[id].miniLessonsCompleted.includes(lessonId)`
- **Persistence:** `useProgressStore.getState().completeMiniLesson(scenarioId, lessonId, 6)`
- **Rule:** This is triggered ONLY upon V3 Session completion for the specific lesson context.

### C. Scenario Complete
- **State:** `Avg(GlobalProgress[item].mastery) >= 0.75` for all items in scenario.
- **Rule:** Scenario is "Finished" when items are universally at "Advanced" level.

### D. Conversation Ready
- **State:** `∀ category: (count(category_items @ production_level) / category_total) >= 0.8`
- **Production Threshold:** `MasteryLevel >= 3` (Scale 0-4).

## 2. Unlock Flow
1. **Initial State:** Scenario 1 unlocked, Lesson 1 unlocked.
2. **Action:** User completes Session 1 (Lesson 1 items).
3. **Trigger:** `completeMiniLesson` adds `l1` to completion array.
4. **Result:** `ScenarioDetailScreen` computes `unlocked = completed.length + 1`, making Lesson 2 active.
5. **Persistence:** State saved in LocalStorage, persists across refresh.
