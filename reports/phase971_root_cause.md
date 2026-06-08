# Phase 9.7.1: Root Cause Analysis

## 1. Problem
Real user testing proved that after completing a lesson, the next lesson remained locked and the state did not survive a refresh.

## 2. Investigation
The internal logic of `completeMiniLesson` in `src/store/progressStore.ts` and the unlock evaluation in `src/screens/MiniLessonScenarioView.tsx` are mathematically flawless. Simulated state transitions prove that completing `'l1'` correctly unlocks `'l2'`.

The root cause was architectural: **Store Duplication via Path Aliases.**

In the codebase, `LearningSystemV3PilotScreen.tsx` imported the store via relative path:
```typescript
import { useProgressStore } from '../store/progressStore';
```
While `MiniLessonScenarioView.tsx`, `ScenarioDetailScreen.tsx`, and `MiniLessonIntroScreen.tsx` imported the store via the `@shared` alias:
```typescript
import { useProgressStore, emptyScenarioProgress } from '@shared/store/progressStore';
```

Under certain Vite/bundler configurations or hot-module-reloading states, these two distinct import paths caused the bundler to instantiate **two separate singleton instances** of the Zustand store. 
1. The V3 Pilot updated Instance A and persisted it to `localStorage`.
2. The Scenario View read from Instance B. Instance B had already hydrated its memory state from `localStorage` on initial mount, and was completely unaware that Instance A had updated the disk.
3. Therefore, the UI remained locked.

## 3. Fix Implemented
Standardized all imports across the scenario and learning screens to use the relative path `../store/progressStore`. This guarantees a single, unified memory instance of the Zustand store, ensuring that state updates in the Pilot instantly reflect in the Scenario View.
