# Phase 7.7 — Priority Budget Design

To prevent inflation, implicit review credit is bounded to 20 words per conversation. When >20 eligible words exist, a scoring system decides which words receive the credit.

## 1. Mastery Priority Scoring
Lower mastery states represent a higher pedagogical urgency to reinforce.

| State | Score | Rationale |
| :--- | :--- | :--- |
| **LAPSED** | 100 | Highest urgency. Memory trace is broken and needs immediate repair. |
| **RELEARNING** | 90 | Actively repairing a lapse. |
| **UNKNOWN** | 80 | New target vocabulary for the scenario. |
| **LEARNING** | 70 | Building initial trace (`streak < 3`). |
| **LEARNED** | 40 | Standard maintenance. |
| **ADVANCED** | 20 | Mature memory trace. |
| **MASTERED** | 10 | Lowest urgency. Interval > 30 days. |

## 2. Tie-Breaking Mechanics
If there are 25 `LEARNED` words competing for the last 5 budget slots, the engine breaks ties based on:
1. **Due Date:** Words that are `REVIEW_DUE` win.
2. **Frequency:** Words appearing multiple times in the dialogue text win.
3. **Length:** Longer words win (lexical complexity heuristic).
