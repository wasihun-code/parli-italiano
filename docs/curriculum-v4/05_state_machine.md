## Learning State Machine Design

This document defines how the system tracks learner progress, manages state transitions, schedules reviews, and unlocks content. All entities (words, phrases, sentences, turns) follow the same state machine with minor parameter variations.

---

## 1. State Definitions

| State | Meaning | Entry Conditions | Exit Conditions |
|-------|---------|------------------|-----------------|
| **UNSEEN** | Learner has never encountered this item. | Initial state for all items. | Learner completes **first exposure** (Listen exercise for words/phrases/sentences; first Listen for turns). → INTRODUCED |
| **INTRODUCED** | Learner has seen the item once but has not yet practiced it. | After first exposure exercise (e.g., Listen). | Learner completes **practice phase** (e.g., for words: ListenChoose + Match + Recall + Spelling all correct). → PRACTICED |
| **PRACTICED** | Learner has successfully completed all required exercises for the item (recognition + recall + production) but has not yet proven long‑term retention. | After passing practice phase (mastery score ≥ threshold for PRACTICED). | Learner passes **first review** (scheduled after delay) → MASTERED. Or if review fails repeatedly, may stay PRACTICED. |
| **MASTERED** | Learner has demonstrated durable retention through spaced reviews. | After passing a review when in PRACTICED state, or after passing a scheduled review from MASTERED. | If a review is failed, state reverts to PRACTICED (not FORGOTTEN immediately). If multiple failures over long period, may become FORGOTTEN. |
| **FORGOTTEN** | Learner likely no longer remembers the item due to prolonged inactivity or repeated review failures. | No successful review for > 2× the normal review interval AND at least 30 days since last seen. Or after 3 consecutive review failures. | Learner re‑enters PRACTICED after completing a **re‑introduction** (shorter version of practice: e.g., Recall or Dictation once). |
| **REVIEW_DUE** | A scheduled review is pending for this item. This is not a permanent state but a flag that triggers review injection. | Calculated by review scheduler (see Section 5). When due, the item is flagged for review. After review is completed, REVIEW_DUE cleared; state becomes MASTERED (if passed) or PRACTICED (if failed). | Review is completed. |

**Note:** REVIEW_DUE is a **transient flag**; items in MASTERED or PRACTICED can become REVIEW_DUE without changing their base state until the review happens.

---

## 2. State Transition Diagram

```
UNSEEN
   │ (first exposure)
   ▼
INTRODUCED
   │ (practice exercises passed)
   ▼
PRACTICED ─────────────────────────────┐
   │ (first review passed)              │ (review failed)
   ▼                                    │
MASTERED                                │
   │ (review due)                        │
   ▼                                    │
REVIEW_DUE (flag)                        │
   │ (review passed)                     │
   └────────────────────────────────────► PRACTICED
   │ (review failed)
   └────────────────────────────────────► PRACTICED (already there)

After prolonged neglect or repeated failures:
MASTERED or PRACTICED ──(timeout/3 fails)──► FORGOTTEN
                                                      │
                                                      │ (re-introduction)
                                                      ▼
                                                  PRACTICED
```

**Valid transitions:**
- UNSEEN → INTRODUCED
- INTRODUCED → PRACTICED
- PRACTICED → MASTERED (on first review success)
- PRACTICED → REVIEW_DUE (when review scheduled)
- MASTERED → REVIEW_DUE (when review scheduled)
- MASTERED → PRACTICED (on review failure)
- PRACTICED → FORGOTTEN (after timeout or repeated failures)
- MASTERED → FORGOTTEN (after timeout or repeated failures)
- FORGOTTEN → PRACTICED (after successful re‑introduction)

No direct transition from FORGOTTEN to MASTERED; must pass through PRACTICED again.

---

## 3. Tracking Data Model

For each entity (word, phrase, sentence, turn), the system stores:

```json
{
  "entity_id": "w_000001",
  "state": "PRACTICED",
  "first_seen": 1700000000,
  "last_seen": 1700005000,
  "last_reviewed": 1700020000,
  "review_interval_days": 3,
  "consecutive_successes": 2,
  "consecutive_failures": 0,
  "total_attempts": 5,
  "correct_attempts": 4,
  "mastery_score": 0.82,
  "response_time_avg_ms": 1800,
  "next_review_due": 1700100000
}
```

**Field explanations:**
- `state` – current state (UNSEEN, INTRODUCED, PRACTICED, MASTERED, FORGOTTEN)
- `first_seen` – timestamp of first exposure (UNSEEN → INTRODUCED)
- `last_seen` – timestamp of any interaction (practice, review, production)
- `last_reviewed` – timestamp of last review attempt (for scheduling)
- `review_interval_days` – current interval before next review (varies with spaced repetition)
- `consecutive_successes` – number of successful reviews in a row (used to increase interval)
- `consecutive_failures` – number of failed reviews in a row (used to decrease interval or trigger FORGOTTEN)
- `total_attempts`, `correct_attempts` – for mastery score calculation
- `mastery_score` – composite score (0 to 1) based on accuracy, recency, response time
- `response_time_avg_ms` – average speed of recall/production responses
- `next_review_due` – timestamp when this item becomes REVIEW_DUE

---

## 4. Mastery Score Model

**Mastery score** is a continuous value in [0, 1] that influences transitions and review scheduling.

### 4.1 Calculation

Mastery = weighted combination of:
- **Accuracy** (60%): `correct_attempts / total_attempts` (capped at 1)
- **Recency** (20%): exponential decay since last seen: `exp(-days_since_last / 30)`
- **Response time** (20%): `1 - min(1, avg_response_ms / 5000)` (faster = higher)

### 4.2 Thresholds for State Transitions

| Transition | Required Mastery Score |
|------------|------------------------|
| INTRODUCED → PRACTICED | ≥ 0.70 (after completing all practice exercises) |
| PRACTICED → MASTERED (first review) | ≥ 0.80 on the review |
| MASTERED → REVIEW_DUE | automatically by schedule, regardless of score |
| PRACTICED → FORGOTTEN | < 0.30 for 30 consecutive days OR 3 review failures in a row |
| FORGOTTEN → PRACTICED | ≥ 0.70 on re‑introduction recall exercise |

### 4.3 Mastery Gain / Loss

- **Practice exercises (INTRODUCED → PRACTICED):** Score jumps to at least 0.70.
- **Successful review:** Score increases by `(1 - current) * 0.2`; caps at 0.99.
- **Failed review:** Score decreases by `current * 0.1`; minimum 0.30 (if falls below, may trigger FORGOTTEN after repeated failures).
- **Long inactivity:** Score decays by `0.01 * days_since_last` up to max 0.50 loss.

---

## 5. Review Scheduling Model

### 5.1 When does an item become REVIEW_DUE?

An item becomes REVIEW_DUE when `current_time >= next_review_due`.

**Initial review intervals (after entering PRACTICED or MASTERED):**

| Entity Type | First review (days) | Subsequent multiplier |
|-------------|---------------------|----------------------|
| Word        | 1                   | 2× (capped at 90 days) |
| Phrase      | 2                   | 2× (capped at 90) |
| Sentence    | 3                   | 2× (capped at 120) |
| Turn        | 4                   | 2× (capped at 150) |

**Algorithm:**
```
next_review_due = last_reviewed + (review_interval_days * 86400)
```

After each successful review:
```
review_interval_days = min(max_interval, review_interval_days * 2)
consecutive_successes += 1
consecutive_failures = 0
```

After each failed review:
```
review_interval_days = max(1, review_interval_days / 2)
consecutive_failures += 1
if consecutive_failures >= 3:
    state = FORGOTTEN
```

### 5.2 Review Injection

The system selects 2–4 REVIEW_DUE items per micro‑lesson (prioritising those with earliest due dates). Review exercises are quick (Match, ListenChoose, Recall). After review, update `last_reviewed`, `review_interval_days`, and recalc mastery.

---

## 6. Dependency Interaction Rules

**Rule 1:** A phrase **cannot** be introduced (UNSEEN → INTRODUCED) until **all** its dependent words are at least **PRACTICED** (mastery score ≥ 0.70).

**Rule 2:** A sentence **cannot** be introduced until **all** its dependent words and phrases are **PRACTICED** or **MASTERED** (≥ 0.70).

**Rule 3:** A conversation turn **cannot** be introduced until its **single corresponding sentence** is **PRACTICED** (≥ 0.70).

**Rule 4:** A conversation turn pair (host + user) can be **practiced** in Conversation exercise only when **both** turns have been introduced and are at least PRACTICED.

**Rule 5:** For unlocking review of an item, dependencies are **not** checked – reviews can happen even if dependencies are weaker, because the learner may still benefit. However, if a dependent word becomes FORGOTTEN, the system will flag the higher‑level item for earlier review.

**Rule 6:** When an item is FORGOTTEN, all items that depend on it (phrases, sentences, turns) are **not** automatically downgraded, but their **next review** is scheduled 50% sooner to prevent the learner from forgetting the dependent structure.

---

## 7. Unlocking Rules

### 7.1 Micro‑Lesson Unlocking

A micro‑lesson is a set of new words, phrases, sentences, and turns as defined in the curriculum.

**Prerequisite for unlocking micro‑lesson N+1:**  
All items (words, phrases, sentences, turns) from micro‑lesson N must be in state **PRACTICED** or **MASTERED** (no UNSEEN or INTRODUCED remaining). FORGOTTEN items are allowed as long as they are not part of the current micro‑lesson's dependencies; the system will trigger recovery reviews.

**Exception:** The learner may manually choose to unlock the next micro‑lesson even if some items are still INTRODUCED but not yet PRACTICED, after a warning. This is an “override” for advanced learners.

### 7.2 Conversation Practice Unlocking

The **Conversation** exercise for a pair of turns (e.g., host turn + user turn) unlocks when:
- Both turns have been **INTRODUCED** (not necessarily PRACTICED).
- All sentences underlying those turns are **PRACTICED** (mastery ≥ 0.70).

### 7.3 Scenario Completion

A scenario (e.g., “Smooth Check‑In”) is considered **complete** when:
- All 20 turns in that scenario have been **PRACTICED** at least once.
- The learner has completed the final Conversation exercise for that scenario with ≥80% accuracy on turn production.

---

## 8. Failure Recovery Rules

### 8.1 Repeated Failures During Practice

If a learner fails the same practice exercise (e.g., Recall for a word) **three times consecutively**:

- The system **does not** advance the state.
- A **hint** is shown (e.g., English translation or phonetic cue).
- After 3 failures, the item is automatically reviewed by presenting a simpler exercise (e.g., Match instead of Recall) and then retrying the original.
- No state change; learner may repeat as many times as needed.

### 8.2 Repeated Review Failures

If a learner fails a review for the same item **3 times in a row**:
- State becomes **FORGOTTEN**.
- The item is scheduled for **re‑introduction** after 1 day.
- Re‑introduction uses a shorter sequence: **Listen** (once) → **Recall** (with optional visual prompt). If passed, state returns to PRACTICED (mastery score reset to 0.70). If failed again, stays FORGOTTEN and repeats after 2 days.

### 8.3 Long Inactivity

If a learner has not interacted with the system for **> 14 days**:
- All items in PRACTICED or MASTERED have their `mastery_score` reduced by `0.05 * (inactivity_days / 7)` (max 0.40 reduction).
- Items whose mastery falls below 0.30 become FORGOTTEN.

Upon return, the learner is presented with a **“Review Catch‑Up”** session (5–10 review exercises) before resuming the current micro‑lesson.

### 8.4 Poor Review Performance

If a learner’s review accuracy for a session is < 60%:
- The system schedules **immediate re‑review** of the failed items (within the same session).
- The next micro‑lesson is **not unlocked** until the learner retakes the failed reviews and achieves ≥70% accuracy.

---

## 9. Example Lifecycle

### Example 1: Word `w_000012` (codice)

| Event | State | Mastery | Next Review Due |
|-------|-------|---------|-----------------|
| Initial | UNSEEN | 0.00 | – |
| Learner listens (Listen) | INTRODUCED | 0.20 | – |
| Completes ListenChoose + Match + Recall + Spelling all correct | PRACTICED | 0.72 | +1 day |
| 1 day later – review due; learner passes Recall | MASTERED | 0.82 | +2 days |
| 2 days later – review due; learner fails | PRACTICED | 0.74 | +1 day |
| 1 day later – review due; learner passes | MASTERED | 0.83 | +4 days |
| No interaction for 30 days – mastery decays to 0.31 | MASTERED | 0.31 | still MASTERED but next review due soon |
| Review due; learner fails 3 times in a row → FORGOTTEN | FORGOTTEN | 0.28 | re‑intro after 1 day |
| Re‑introduction: Listen + Recall (pass) | PRACTICED | 0.70 | +2 days |

### Example 2: Phrase `p_000004` (hai il codice)

| Event | State | Notes |
|-------|-------|-------|
| Before introduction: words `hai` and `codice` are PRACTICED | UNSEEN | Dependency satisfied |
| Listen phrase → INTRODUCED | INTRODUCED | – |
| Practice: ListenChoose, Match, Assembly, Recall all correct | PRACTICED | mastery ≥0.70 |
| First review (2 days later) passes | MASTERED | – |
| Review interval doubles each success. |

### Example 3: Sentence `s_000003` (Ottimo. Il portone è chiuso? Hai il codice per entrare?)

| Event | State | Dependency check |
|-------|-------|------------------|
| Dependencies: words (ottimo, portone, etc.) + phrase (hai il codice) all PRACTICED | UNSEEN → INTRODUCED | Allowed |
| Practice: Listen, Reading, ListenChoose (gap), BuildSentence, Dictation all correct | INTRODUCED → PRACTICED | – |
| First review (3 days later) passes | PRACTICED → MASTERED | – |

### Example 4: Conversation Turn `t_000003` (host: Ottimo. Il portone è chiuso? Hai il codice per entrare?)

| Event | State | Prerequisite |
|-------|-------|---------------|
| Sentence `s_000003` is PRACTICED | UNSEEN → INTRODUCED | Unlocked |
| Practice: Listen to turn, ListenChoose (choose correct user response), Speaking (host role), Recall (user role without text) | INTRODUCED → PRACTICED | – |
| Conversation exercise with paired user turn | PRACTICED (turn pair) | – |
| After first review (4 days later) passes | PRACTICED → MASTERED | – |

---

**End of Learning State Machine Design**
