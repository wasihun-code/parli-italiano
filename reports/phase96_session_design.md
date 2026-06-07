# Phase 9.6: Session Design Report

## 1. Overview
The Learning System V3 was producing Master Paths containing all 9 acquisitions phases for all items in a scenario, leading to sequences of 900+ steps. Phase 9.6 introduces the `SessionGenerator` to chunk these into manageable daily goals.

## 2. Session Metrics

| Metric | Master Path (Scenario 22) | Today's Session |
| :--- | :--- | :--- |
| **Total Steps** | ~920 | 25 |
| **Item Count** | 371 | ~8-12 |
| **Est. Completion Time** | 3+ hours | **5 - 8 minutes** |

## 3. Session Generation Algorithm
The `SessionGenerator` performs a strict chronological slice of the master path:
1. Master Path is generated (Chronology + Mastery aware).
2. The first **25 steps** are selected.
3. This ensures the user always works on the next most relevant items for the conversation without being overwhelmed.

## 4. Conclusion
Session chunking transforms the pilot from an exhaustive dictionary run into a focused, situational practice session.
