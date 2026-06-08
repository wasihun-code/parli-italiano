# Phase 9.7a: Layout Repair

## 1. Problem
Previous iterations attempted to scale the layout, but the surrounding chrome was still too distracting, and the actual exercise cards didn't "own" the screen on mobile devices.

## 2. Fix Implemented
In `LearningSystemV3PilotScreen.tsx` and the individual exercise components:
- The main `<main>` container was converted to `flex: 1` with a `maxWidth: 1000px`, allowing the white surface to stretch across the entire functional area.
- Borders and shadows were refined to create a distinct, modern "card" that feels similar to a native mobile application.
- Padding inside the `Match` and `Spelling` components was increased to `spacing.xxl`, significantly increasing the tap targets for options.

## 3. Result
The layout is now highly optimized. The prompt and the interactive elements are the largest objects on the screen, improving readability and usability.
