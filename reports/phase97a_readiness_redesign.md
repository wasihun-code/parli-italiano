# Phase 9.7a: Readiness Redesign

## 1. Problem
The footer readiness meter calculated global mastery across the entire scenario (100+ items). Since a 25-step session only provides fractional mastery increments to 25 items, the global average moved by less than 0.5% per session. This felt meaningless to the user.

## 2. Redesign
The footer has been redesigned to reflect metrics that change rapidly and meaningfully during a session:
1. **Session Progress:** Shows how far along the user is in the current 25-step chunk.
2. **Lesson Mastery:** Shows the average mastery of only the items contained within the *current* lesson scope.
3. **Scenario Readiness:** The global readiness score (slower moving, but necessary for the overarching goal).

## 3. Implementation
Calculated dynamically inside `LearningSystemV3PilotScreen.tsx` using the `lessonId` subset of items.
