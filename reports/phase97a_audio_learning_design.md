# Phase 9.7a: Audio Learning Design

## 1. Problem
Audio was a secondary, passive feature. The user read the word, and the audio happened to play in the background.

## 2. Fix Implemented
Re-architected the fundamental flow of the `Listen` exercise. The Italian text is completely hidden from the prompt. The user is forced to:
1. Tap the audio button (or trigger it automatically).
2. Listen to the raw spoken Italian.
3. Compare what they heard against 4 distinct written choices.
4. Select the matching choice to proceed.

## 3. Result
Audio is no longer an accessory; it is the primary vector for completing the recognition stage, directly training ear-to-brain comprehension.
