# Phase 9.7.1: Progression Trace

## 1. Pipeline
The V3 Pilot progression pipeline follows this exact trace:

1. **Exercise Complete:** `LearningSystemV3PilotScreen.tsx` -> `handleComplete(result)`
2. **Session Complete:** `LearningSystemV3PilotScreen.tsx` -> `handleContinue()` -> Evaluates `if (isSessionEnd)`
3. **Lesson Complete:** `LearningSystemV3PilotScreen.tsx` -> `useProgressStore.getState().completeMiniLesson(currentScenarioId, lessonId, 6)`
4. **Scenario Progress Update:** `progressStore.ts` -> `completeMiniLesson` updates `scenarioProgress[scenarioId].miniLessonsCompleted`
5. **Persistence Layer:** `progressStore.ts` -> Zustand `persist` middleware synchronously writes to `localStorage` ('parla-italiano-progress').
6. **Unlock Next Lesson:** `MiniLessonScenarioView.tsx` -> `isUnlocked = completedLessons.includes(prevLessonId)`

## 2. Evaluation
All steps in this pipeline execute synchronously and reliably. The logic is mathematically robust.
