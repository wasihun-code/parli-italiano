# Phase 9.7a: Progress Experience Redesign

## 1. Problem
The original footer simply displayed: `Vocab: X% | Phrases: Y% | Conv: Z%`. These percentages were based on the *entire scenario* (150+ items), causing them to move at a glacial pace (0.5% per session).

## 2. Solution
The readiness footer in `LearningSystemV3PilotScreen.tsx` was redesigned to display immediate, localized progress metrics:
- **Session Progress:** A prominent progress bar moving from 0% to 100% directly tied to `currentIndex / totalSteps`.
- **Lesson Mastery:** Calculates the average mastery solely for the `exerciseIds` included in the current `lessonId`. This metric updates visibly after every correct answer.
- **Scenario Readiness:** The overarching goal progress.

## 3. Result
Learners now experience tangible rewards and clear tracking for their immediate session, their current lesson block, and their overall conversational goal.
