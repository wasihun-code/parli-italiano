# Phase 9.6c: Renderer Validation Audit

## 1. Goal
Audit `ExerciseRenderer.tsx` to verify that `Listen`, `Match`, `Spelling`, and `ListenChoose` render correctly and are resilient to invalid or missing payloads.

## 2. Investigation
The `ExerciseRenderer` component previously assumed all payloads were valid and perfectly formed. 
- It did not verify if `payload` existed before switching on the exercise type.
- It passed potentially malformed payloads directly to children (`ListenExercise`, `MatchExercise`).
- The child components expected valid arrays (e.g., `options.map()`), which caused React crashes or silent deadlocks when rendering empty lists.

## 3. Results
- **Null Payloads:** Not handled.
- **Empty Arrays:** Not handled. Components like `ListenExercise` silently rendered nothing when `options` was empty.
- **Invalid Types:** Caught by the `default` switch case which displayed "Unsupported Exercise Type", but offered no way out.

## 4. Required Action
Implement a "Fail-Safe Rendering" pattern in `ExerciseRenderer.tsx`. It must validate payload integrity (especially for MCQs) and provide an emergency "Skip" recovery UI if the payload is corrupted, preventing hard-locks.
