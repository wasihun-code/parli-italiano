# Phase 9.7a: Scenario Immersion

## 1. Problem
The initial landing screen for the V3 pilot felt disconnected from the scenario. It displayed a generic "Situazione: Arrivo al Palazzo" for all lessons, which failed to prime the learner.

## 2. Fix Implemented
The context banner in `LearningSystemV3PilotScreen.tsx` was made fully dynamic, tying directly into the data from `mini_lessons.json`. It now displays the specific goal of the current lesson (e.g., "Finding the Entrance", "Using the Intercom") prominently in the header.

## 3. Result
The learner is constantly reminded of *why* they are practicing these specific words and sentences.
