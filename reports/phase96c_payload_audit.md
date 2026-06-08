# Phase 9.6c: Payload Validation Audit

## 1. Goal
Audit every generated exercise payload for Apartment Key Pickup (Scenario 22) Lesson 1 to ensure that the required properties (especially choices for MCQ) exist.

## 2. Investigation
The `LearningPathGenerator` pulls items from the scenario data and maps them to `ExerciseRegistry` definitions.
- The `ListenExercise` component expects `payload.options` or `payload.choicesItalian`.
- Before the fix, the `ExerciseRegistry` mapped the `Listen` exercise to `basicPayloadBuilder`, which **did not** transfer `choicesItalian` or `options` to the generated payload.
- This resulted in payloads missing the required multiple-choice strings.

## 3. Results
- **Type verification:** All items successfully resolved to an exercise type.
- **Payload existence:** Payloads generated successfully, but lacked required fields.
- **Choice existence:** FAILED. `Listen` payloads contained exactly 0 choices, violating the minimum 2-choice requirement for the UI.
- **Completion contract:** Exists (`defaultCompletionHandler`).

## 4. Fix Implemented
The `ExerciseRegistry` mapping for `Listen` was updated to use `mcqPayloadBuilder` instead of `basicPayloadBuilder`. All future `Listen` payloads will now successfully include `options` populated by `choicesItalian`.
