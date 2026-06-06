# Spaced Repetition Algorithm Recommendation

To manage the Global Knowledge Graph, Parla Italiano requires a robust Spaced Repetition System (SRS).

## Algorithm Comparison

### Option A: Simple Streak System (Duolingo style)
- **Mechanism:** Interval = `2^streak` days. Fail = streak resets to 0.
- **Pros:** Extremely easy to implement and explain to users.
- **Cons:** Pedagogically punishing. Forgetting a word you've known for a year resets it as if you've never seen it, causing review fatigue.

### Option B: Leitner System (Box System)
- **Mechanism:** Words move between boxes (e.g., Box 1 = daily, Box 2 = 3 days). Correct = move up, Incorrect = move down to Box 1.
- **Pros:** Simple, deterministic.
- **Cons:** Rigid intervals. Doesn't adapt to the difficulty of specific words.

### Option C: SM-2 (Anki style)
- **Mechanism:** Uses an "Ease Factor" (EF). `Next Interval = Previous Interval * EF`.
- **Pros:** Highly adaptive. Hard words are reviewed often; easy words are pushed far into the future.
- **Cons:** Complex. User must self-report difficulty ("Hard", "Good", "Easy"). Pure SM-2 punishes lapses harshly.

### Option D: Custom Hybrid (FSRS-Lite)
- **Mechanism:** A modified SM-2 that does not require user self-reporting. It assumes "Good" if correct, and "Again" if incorrect. It includes a softer "Lapse" penalty.
- **Pros:** Invisible to the user. Highly adaptive. Forgiving of temporary lapses.
- **Cons:** Requires careful tuning of initial parameters.

## Recommendation: Option D (Custom Hybrid)

Parla Italiano should implement a **Custom Hybrid (FSRS-Lite)** algorithm. Language learners using a gamified app do not want to rate their own memory (1-4 buttons). The system should deduce difficulty automatically based on binary PASS/FAIL inputs.

### The Parla Italiano SRS Algorithm Specification

**1. Initial Parameters**
- `ease_factor` (EF): Defaults to 2.5.
- `interval` (I): Measured in days.

**2. Learning Phase (Micro-steps)**
- Steps: 1 min, 5 min, 10 min.
- A word must pass all three steps to graduate to `LEARNED`.
- *Graduation:* `interval = 1`, `due_at = now + 1 day`.

**3. Review Phase (Macro-steps)**
When a user answers a `REVIEW_DUE` item:

**If CORRECT:**
- `interval = max(1, round(interval * ease_factor))`
- `ease_factor = min(3.0, ease_factor + 0.1)` (Reward for remembering)
- `due_at = now + interval days`

**If INCORRECT (Lapse):**
- `ease_factor = max(1.3, ease_factor - 0.2)` (Word is deemed harder)
- `interval = max(1, round(interval * 0.2))` (Lapse penalty: drops to 20% of previous interval, not zero)
- State changes to `RELEARNING`.

**4. Fuzzing**
To prevent massive clumps of reviews due on the exact same day, apply a +/- 5% random fuzz to the calculated `interval` before saving.
