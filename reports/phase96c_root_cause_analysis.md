# Phase 9.6c: Root Cause Analysis

## 1. Problem Statement
Real user testing showed that learners became trapped on the very first exercise of the V3 Pilot ("ASCOLTA E SELEZIONA"). The screen showed a speaker icon but absolutely no multiple-choice buttons, no feedback overlay, and no way to continue or skip. The lesson was deadlocked.

## 2. Investigation
The `ListenExercise` component was redesigned in Phase 9.7 to be an active multiple-choice task, replacing a passive flashcard flow. 
Inside `ListenExercise.tsx`:
```typescript
const options = payload.options || payload.choicesItalian || [];
```
If `options` is an empty array, no buttons render.

We traced the payload generation back to `src/exercises/resolver.ts` and `src/exercises/registry.ts`.
In `registry.ts`, the `Listen` exercise is defined to use `basicPayloadBuilder`:
```typescript
  Listen: {
    metadata: { id: 'Listen', name: 'Listening', category: 'Recognition', difficulty: 'Beginner' },
    payloadBuilder: basicPayloadBuilder,
    // ...
```
In `src/exercises/factories.ts`, `basicPayloadBuilder` explicitly strips out the distractors/choices:
```typescript
export const basicPayloadBuilder: ExerciseFactory = (itemData: any, _stepId: string): ExercisePayload => {
  return {
    itemId: itemData.id,
    italian: itemData.italian,
    english: itemData.english,
    audio: itemData.audio,
    hint: itemData.hint
  }; // NO 'choicesItalian' or 'options' passed!
};
```

## 3. The Root Cause
1. **Component Mismatch:** In Phase 9.7, `ListenExercise` was upgraded to require MCQ options, but its definition in `ExerciseRegistry` was not updated. It still used `basicPayloadBuilder` instead of `mcqPayloadBuilder`.
2. **Missing Fail-safes:** The UI component assumed `options` would be present. When it wasn't, the component rendered an empty grid without providing any fallback "Skip" or "Continue" button, hard-locking the application.
3. **Missing Pre-flight Validation:** The `LearningPathGenerator` generated the session, but nothing validated whether the resulting payloads were actually renderable by their target components before serving them to the user.

## 4. Required Fixes
- `Listen` must use `mcqPayloadBuilder` in the registry.
- `ExerciseRenderer` must implement strict payload validation before mounting a component.
- The UI must have an emergency "Skip" or fallback state if rendering fails.
