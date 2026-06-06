# Vocabulary Mastery Lifecycle

This document defines the complete lifecycle of a vocabulary item (`global_dict_id`) within the Parla Italiano Hybrid Mastery system.

## State Definitions

A vocabulary item can exist in one of the following states:

1. **`NEW`**: The word exists in the global dictionary but has never been encountered by the user in any scenario.
2. **`LEARNING`**: The user has encountered the word in a scenario's vocabulary lesson but has not yet met the initial retention threshold.
3. **`LEARNED`**: The user has successfully completed the initial learning steps. The word is now subject to multi-day spaced repetition.
4. **`REVIEW_DUE`**: The word's spaced repetition interval has expired. It is actively waiting in the Daily Review Queue.
5. **`LAPSED`**: The user failed to recall a `LEARNED` or `MASTERED` word during a review.
6. **`RELEARNING`**: The user is rebuilding the memory trace for a `LAPSED` word.
7. **`MASTERED`**: The word has been successfully recalled multiple times over a long period. Its review interval is highly extended (e.g., > 30 days).

## State Transitions & Triggers

| Current State | Trigger Condition | Next State | Action / SRS Update |
| :--- | :--- | :--- | :--- |
| `NEW` | User starts a Scenario Vocabulary Lesson | `LEARNING` | Initialize SRS entity. Set `streak = 0`. |
| `LEARNING` | Correct Answer | `LEARNING` | `streak++`. If `streak == 3`, transition to `LEARNED`. |
| `LEARNING` | Incorrect Answer | `LEARNING` | `streak = 0`. |
| `LEARNING` | `streak == 3` reached | `LEARNED` | Set `interval = 1 day`. Set `due_at = now + 1 day`. |
| `LEARNED` | `now >= due_at` | `REVIEW_DUE` | Word enters Daily Review queue. |
| `REVIEW_DUE` | Correct Review | `LEARNED` | Multiply `interval` by `ease_factor`. Set new `due_at`. |
| `REVIEW_DUE` | Correct Review (Interval > 30d) | `MASTERED` | Multiply `interval` by `ease_factor`. Set new `due_at`. |
| `REVIEW_DUE` | Incorrect Review | `LAPSED` | Log lapse. Decrease `ease_factor`. |
| `LAPSED` | Immediate | `RELEARNING` | Reset `interval` to 10 mins. Require 2 correct answers to graduate. |
| `RELEARNING` | 2 Consecutive Correct Answers | `LEARNED` | Set `interval = 1 day`. Set `due_at = now + 1 day`. |
| `MASTERED` | `now >= due_at` | `REVIEW_DUE` | Word enters Daily Review queue. |
| `MASTERED` | Incorrect Review | `LAPSED` | Log lapse. Decrease `ease_factor` heavily. Drop to `RELEARNING`. |

## Diagram (Text Representation)

```text
       ┌─────────────────┐
       │       NEW       │
       └────────┬────────┘
                │ (Encounter in Scenario)
                ▼
       ┌─────────────────┐
  ┌───►│    LEARNING     ├──────┐ (Streak == 3)
  │    └────────┬────────┘      │
  │(Fail)       │ (Pass)        ▼
  └─────────────┘      ┌─────────────────┐
                       │     LEARNED     │◄──────────────┐
                       └────────┬────────┘               │
                                │ (Time passes)          │ (Pass Review)
                                ▼                        │
                       ┌─────────────────┐               │
                       │   REVIEW_DUE    ├───────────────┤
                       └────────┬────────┘               │
                                │ (Fail Review)          │ (Pass Review, Int > 30d)
                                ▼                        │
       ┌─────────────────┐     ┌─────────────────┐       │
  ┌───►│   RELEARNING    │◄────┤     LAPSED      │       ▼
  │    └────────┬────────┘     └─────────────────┘ ┌─────────────────┐
  │(Fail)       │ (Streak == 2)                    │    MASTERED     │
  └─────────────┘                                  └─────────────────┘
```
