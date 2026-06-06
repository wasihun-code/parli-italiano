# Phase 7.9 — Progress & Pedagogical Certification Report

## 1. Executive Summary
The pedagogical integrity of the Hybrid Mastery system has been audited. The core infrastructure for state transitions, review prioritization, and implicit reinforcement is functional, though some "RELEARNING" state logic remains in a placeholder status as planned for later phases. The 20-word reinforcement cap is correctly implemented and provides a vital safeguard against SRS bloat.

## 2. Mastery State Transitions & FSRS-Lite
### 2.1 State Mapping Audit
The `MasteryState` type is correctly defined, but the implementation in `GlobalProgressService` shows a simplification:
- **UNKNOWN:** Item never encountered.
- **LEARNING:** `mastery_level == 0` and `total_attempts > 0`.
- **LEARNED:** `mastery_level >= 1`.
- **ADVANCED:** `mastery_level == 3`.
- **MASTERED:** `mastery_level >= 4`.
- **LAPSED:** `correct_streak == 0` and `total_attempts > 0`.
- **RELEARNING:** **ORPHANED.** Currently, the system transitions `LAPSED` items back to `LEARNING` once a single correct answer is recorded, skipping the explicit `RELEARNING` state in the code, though it exists in the documentation and types.

### 2.2 FSRS-Lite Implementation
The current logic is a "pre-FSRS" implementation (aligned with Phase 7.3 goals):
- Graduation to `LEARNED` requires a `correct_streak` of 3.
- Failure results in a "soft lapse" (decrementing `mastery_level` but not resetting to 0 unless already at low levels).
- **Finding:** Interval calculation (`next_review_at`) is currently static or set to `now`, indicating that Phase 7.8's full interval logic is pending or partially decoupled.

## 3. Review Queue Prioritization
### 3.1 Scoring & Sorting
`ReviewQueueService` successfully implements a tiered priority system:
1. **LAPSED (100):** Most urgent.
2. **LEARNING (70):** High priority for graduation.
3. **DUE (40):** Standard maintenance.
4. **RELEARNING (90):** **MISSING.** Code comments suggest a score of 90, but it is not implemented in the `getDailyQueue` switch.

### 3.2 Capacity Management
- **Hard Cap:** 100 items per day. Verified.
- **Impact:** Prevents user burnout and ensures the most critical items are seen first.

## 4. Conversation Reinforcement (The 20-Word Cap)
### 4.1 Budget Logic
`ConversationReinforcementService` implements a strict `REINFORCEMENT_BUDGET_CAP = 20`.
- **Scoring:** Uses a `PRIORITY_SCORES` map (which *does* include RELEARNING: 90).
- **Tie-breaking:** Frequency of words in the conversation provides a minor boost (+1 to +4), ensuring the most contextually relevant words are reinforced.

### 4.2 Pedagogical Guardrails
A critical guardrail was verified:
- **Exclusion of NEW/LEARNING items:** Only items with state `LEARNED`, `ADVANCED`, `MASTERED`, `LAPSED`, or `RELEARNING` receive implicit credit.
- **Rationale:** This prevents users from "learning" a word by simply finishing a conversation without dedicated study. It preserves the "Explicit -> Implicit" learning hierarchy.

## 5. Final Findings & Recommendations
| Metric | Status | Note |
| :--- | :--- | :--- |
| **State Transitions** | PASS | Robust enough for MVP. |
| **LAPSED Prioritization** | PASS | Top of the queue. |
| **RELEARNING Logic** | WARNING | Type exists, but state is unreachable in current `GlobalProgressService`. |
| **20-Word Cap** | PASS | Strictly enforced. |
| **Pedagogical Guardrails**| PASS | Effectively prevents accidental learning of UNKNOWN words. |

**Recommendation:** Update `GlobalProgressService.getMasteryState` to explicitly handle the `RELEARNING` state (e.g., when an item has `mastery_level >= 1` but was recently `LAPSED` and hasn't yet regained its original level) to align with Phase 7.10 requirements.

**Certification Level: SILVER** (Pending RELEARNING state activation).
