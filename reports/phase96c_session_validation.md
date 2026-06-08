# Phase 9.6c: Session Validation Audit

## 1. Goal
Ensure that a generated session never starts if it contains a fundamentally broken exercise (e.g., missing payload data, undefined choices) that would trap the learner.

## 2. Implementation
Created `src/services/sessionValidator.ts`. This service acts as a pre-flight check before a session is handed over to the React UI.
It iterates through the proposed `LearningStep` array:
1. Attempts to `resolveExercise`.
2. Verifies `definition` and `payload` are non-null.
3. For MCQ types (`Listen`, `Match`, `ListenChoose`), strictly verifies that an `options` or `choicesItalian` array exists, has at least 2 items, and explicitly includes the correct answer (`payload.italian`).
4. Catches any resolution exceptions.

## 3. Usage
The UI component (`LearningSystemV3PilotScreen.tsx`) must invoke this validator after calling `SessionGenerator`. If it returns false, the session must be discarded and either regenerated or aborted with a clean error screen.

## 4. Result
Learners will no longer enter sessions that are destined to deadlock.
