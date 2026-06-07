# Phase 9.6a: Audio Root Cause Analysis

## 1. Problem Statement
User feedback indicates that audio does not play during the V3 Pilot session, despite 100% of assets being resolved by the audit script.

## 2. Root Cause Analysis

### A. Browser Autoplay Restrictions
The `ListenExercise` component attempts to play audio via `Tts.speak` immediately within a `useEffect` hook on mount. 
- **The Issue:** Modern browsers (Chrome, Safari, Firefox) block audio playback that is not initiated by a direct user gesture (e.g., click). 
- **The Impact:** The first exercise of a session is almost guaranteed to be silent if the user navigated directly to the route.

### B. Silent Promise Rejections
In `src/lib/tts.ts`, the `play().catch(reject)` handles errors, but in `speak` it is caught and only logged to `console.debug`.
- **The Issue:** If `audio.play()` fails due to autoplay policy, the app continues silently.
- **The Impact:** The user has no indication that audio *should* have played but was blocked.

### C. AudioContext State
The `audioService.ts` (which plays success/failure pings) attempts to resume the `AudioContext` only when `playTone` is called.
- **The Issue:** If the context is `suspended` (default behavior until gesture), the pings may also fail.

## 3. Recommended Fixes

1.  **Audio Unlock Step:** Add a "Start Lesson" or "Resume" button to the `LearningSystemV3PilotScreen` that must be clicked before the first exercise. This gesture will "unlock" the AudioContext and permission for the session.
2.  **Visible Audio Feedback:** Update the UI to show a "Playing..." state or a pulsing animation when `Tts.speak` is active.
3.  **Explicit Error UI:** If audio fails to load or play, show a small warning banner with a "Click to Enable Audio" button.
4.  **Audio Element Reuse:** Instead of creating a `new Audio()` every time, consider a singleton audio element to reduce browser overhead.
