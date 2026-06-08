# Phase 9.7a: Feedback Consistency

## 1. Investigation
The instruction was that *every* exercise must end with a feedback screen.
In Phase 9.7, we centralized the `FeedbackOverlay` in `LearningSystemV3PilotScreen.tsx`. It triggers when `lastResult` is set by `handleComplete`. Since all `ExerciseRenderer` components invoke `onComplete` with a `ValidationResult`, this constraint is structurally enforced.

## 2. Validation
- `ListenExercise`: Calls `onComplete(result)`. Feedback overlay blocks.
- `MatchExercise`: Calls `onComplete(result)`. Feedback overlay blocks.
- `SpellingExercise`: Calls `onComplete(result)`. Feedback overlay blocks.

There are no paths that bypass the feedback overlay in the pilot.
