# Phase 9.7: Sentence Training Rebalance Defect Resolution

## 1. Root Cause
In `LearningPathGenerator.ts`, the `getSentenceSteps` method utilized exercise types (`Reading`, `Assembly`, `Recall`, `Dictation`, `Speaking`) that were **not supported** by the current `ExerciseRenderer` in the V3 Pilot. Because the pilot explicitly filtered its session to only include `['Listen', 'Match', 'Spelling']`, almost all sentence-stage training was dropped, resulting in vocabulary over-indexing.

## 2. Fix Implemented
Mapped the pedagogical steps for phrases and sentences to use the active V3 Pilot exercise types, fulfilling the requirement to avoid adding new components while increasing sentence importance:
- `Listen` (Recognition/Exposure) -> Weight 0.2
- `Match` (Understanding) -> Weight 0.4
- `Spelling` (Production) -> Weight 1.0

## 3. Result
Sentences and phrases now actively participate in the pilot learning flow. Learners must explicitly recognize, understand, and produce the conversational sentences, drastically improving spoken conversation readiness.
