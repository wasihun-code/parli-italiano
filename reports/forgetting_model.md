# Forgetting Model

When a user masters a word (e.g., `word_grazie` with a 45-day interval) but fails a review, the system must handle the "forgetting" event gracefully.

## The Problem with Full Resets
In naive SRS systems, failing a mature word resets its interval to 0 days, forcing the user to re-learn it from scratch. This is scientifically flawed: forgetting a word after 45 days does not mean the neural pathway is destroyed, it just needs a quick refresher. Full resets cause massive user frustration ("review hell").

## Proposed Forgetting Model: The Lapse Mechanism

Parla Italiano will use a **Partial Regression (Lapse)** model.

### 1. The Lapse Event
If a user fails a review for an item in the `LEARNED` or `MASTERED` state:
- The state transitions to **`LAPSED`**.
- The `lapses` counter increments by 1.
- The `ease_factor` decreases by `0.2` (minimum `1.3`). This ensures the word will grow its interval slightly slower in the future, as it has proven problematic.
- The new `interval` is slashed to **20%** of its previous value (minimum 1 day).
  - *Example:* A 30-day interval drops to a 6-day interval. It does NOT drop to 0.

### 2. The Relearning Phase
Once `LAPSED`, the item immediately enters the **`RELEARNING`** queue.
- It must be answered correctly **twice** consecutively within the current session (e.g., 1m, 10m steps).
- This ensures the memory is actually refreshed, not just guessed correctly once.

### 3. Re-Graduation
Upon passing the `RELEARNING` phase:
- The state returns to **`LEARNED`**.
- The `due_at` timer is set to `now + new_slashed_interval`.
- *Example:* The word "grazie" is refreshed, and will be seen again in 6 days (instead of 30), allowing the user to rebuild the long-term memory trace safely.

### 4. Loss of Mastery
If a `MASTERED` word (interval > 30 days) lapses, and its slashed interval falls below 30 days, it loses the `MASTERED` status and reverts to `LEARNED`. The user's "Mastered Words" metric will decrease by 1, accurately reflecting their current active recall.
