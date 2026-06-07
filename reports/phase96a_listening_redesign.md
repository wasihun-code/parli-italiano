# Phase 9.6a: Listening Exercise Redesign

## 1. Current State
The "Listen" exercise is effectively a flashcard. It shows the Italian word and English translation immediately, then plays audio. 
- **Pedagogical Failure:** The learner doesn't have to "listen" to understand; they can just read.

## 2. Redesigned Flow

### Phase 1: Passive Listening
- **Action:** Audio plays automatically.
- **UI:** Shows a large pulsing speaker icon.
- **Text:** Italian and English strings are **hidden**.
- **Button:** "I heard it" or "Reveal Answer".

### Phase 2: Verification
- **Action:** User clicks "Reveal Answer".
- **UI:** Italian and English text appear.
- **Goal:** Confirms if what the user *thought* they heard matches the target item.

### Phase 3: Completion
- **Button:** "Continue".

## 3. Implementation Details
Modify `src/components/learning/exercises/ListenExercise.tsx` to include an `isRevealed` boolean state.

```typescript
const [isRevealed, setIsRevealed] = useState(false);
```

**Target Experience:**
1. Hear "Ciao".
2. See "🔊" icon.
3. Think "I think that means Hello".
4. Click "Reveal".
5. See "Ciao / Hi".
6. Click "Continue".
