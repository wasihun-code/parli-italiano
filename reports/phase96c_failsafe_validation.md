# Phase 9.6c: Fail-Safe Rendering Resolution

## 1. Requirement
No exercise may render into a dead state. If a payload is invalid, the UI must show an "Exercise unavailable" error with a clear escape route.

## 2. Implementation
Modified `ExerciseRenderer.tsx` to include multiple layers of fail-safe checks:
1. **Null/Undefined Checks:** Rejects rendering if `definition` or `payload` is missing entirely.
2. **MCQ Pre-flight:** If the exercise is `Listen`, `Match`, or `ListenChoose`, it explicitly checks that the `options` array exists and has a length > 0.
3. **Runtime Catch:** The entire `switch` statement for rendering specific components is wrapped in a `try/catch` block.

If any of these fail, a standardized error boundary is shown:
```tsx
<div style={{ padding: 20, textAlign: 'center', color: colors.error }}>
  <h2>Errore di Caricamento / Errore Payload / Runtime Error</h2>
  <p>[Reason]</p>
  <PrimaryButton label="Salta Esercizio" onPress={handleEmergencySkip} />
</div>
```

## 3. Result
Learners will never stare at a blank screen or a screen missing actionable UI elements.
