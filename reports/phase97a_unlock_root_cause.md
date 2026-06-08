# Phase 9.7a: Unlock Root Cause Analysis

## 1. Problem
Learners completed Lesson 1, but Lesson 2 remained locked.

## 2. Investigation
The unlock logic in `MiniLessonScenarioView.tsx` relies on `completedLessons` from the global `progressStore`. 
In `LearningSystemV3PilotScreen.tsx`, the completion call was:
```typescript
useProgressStore.getState().completeMiniLesson(22, lessonId, 6);
```
While this successfully wrote to the DB, it hardcoded `scenarioId` to `22`. If the user accessed the app via a string parameter or a different scenario, progress was misaligned. Furthermore, the `MiniLessonScenarioView` requires the `id` from the JSON to exactly match the stored string.

## 3. Fix
Updated `LearningSystemV3PilotScreen.tsx` to dynamically resolve `scenarioId` from the URL parameters instead of hardcoding `22`, ensuring that the completion signal always matches the viewing context. Verified `isUnlocked` correctly cascades.
