# Phase 9.6c: Audio Gating Audit

## 1. Goal
Determine if audio playback failures or deadlocks can trap the learner before choices appear in `ListenExercise`.

## 2. Investigation
In `ListenExercise.tsx`, audio is triggered via `useEffect` on mount.
```typescript
  const playAudio = async () => {
    setIsPlaying(true);
    await Tts.speak(payload.italian, payload.audio);
    setIsPlaying(false);
  };

  useEffect(() => {
    playAudio();
  }, [payload.itemId]);
```

The multiple-choice options (`options.map(...)`) are rendered independently of the `isPlaying` state.
The rendering of the UI is **not** gated by the successful completion of `Tts.speak()`.

## 3. Results
- **Audio Gating:** False. The UI choices appear immediately upon component mount, regardless of audio status.
- **Deadlock Risk:** None from audio. If `Tts.speak()` fails or hangs, the user can still see the choices (assuming payload is valid) and guess, or press the emergency skip button.

## 4. Conclusion
Audio playback architecture is safe and non-blocking. The deadlock observed in testing was entirely payload-driven, not audio-driven.
