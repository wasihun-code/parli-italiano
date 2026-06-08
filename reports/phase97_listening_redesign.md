# Phase 9.7: Listening Redesign Defect Resolution

## 1. Root Cause
`ListenExercise.tsx` was structured as a flashcard: audio played, but the user only had to click "Reveal" to see the answer, bypassing any active recognition task.

## 2. Fix Implemented
Rebuilt `ListenExercise` into a "Choose what you hear" task:
- Removed the "Reveal" intermediate state.
- Extracted `payload.options` or `payload.choicesItalian`.
- Rendered multiple-choice buttons displaying Italian options.
- The user must now actively select the correct Italian text matching the audio.

## 3. Result
The flow is now: Audio -> Recognition Task (Multiple Choice) -> Answer/Feedback. This forces actual listening comprehension before proceeding.
