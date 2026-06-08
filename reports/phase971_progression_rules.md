# Phase 9.7.1: Progression Rules

## 1. Definitions

*   **Session Complete:** All generated exercises in the `learningPath` array have been answered (i.e., `currentIndex >= learningPath.length - 1` when clicking Continue).
*   **Lesson Complete:** The unique `lessonId` string (e.g., `'l1'`) has been appended to the `miniLessonsCompleted` string array for a specific `scenarioId` in the `progressStore`.
*   **Scenario Complete:** All 6 mini-lessons are complete, satisfying the `withConversationGate` evaluation: `progress.miniLessonsCompleted.length >= totalLessons`.
*   **Unlock Condition:** A lesson at index `idx` is unlocked if `idx === 0` or if `completedLessons.includes(scenario.miniLessons[idx - 1].id)` is true.

## 2. Enforcement
These rules are enforced via rigorous structural typings in `src/store/progressStore.ts` and `src/screens/MiniLessonScenarioView.tsx`.
