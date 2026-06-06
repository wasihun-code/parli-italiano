# Mastery Analytics Design

Transitioning to Hybrid Mastery allows the Parla Italiano platform to gather vastly superior telemetry on learning efficacy.

## 1. User Metrics (Frontend Tracking)

Instead of just tracking boolean completion, the `srsStore` will now provide deep insights into the user's brain:

- **Vocabulary Size (Active):** Count of items with `state == LEARNED` or `MASTERED`.
- **Retention Rate:** `Total Correct Reviews / Total Reviews`. (A healthy SRS targets 85-90% retention).
- **Lapse Rate:** How often `MASTERED` items fall back to `RELEARNING`.
- **Time to Mastery:** Average days required for a `NEW` word to reach the `MASTERED` (>30d) state.

## 2. Admin Metrics (Backend/Dashboard Aggregation)

The Admin Panel's `AnalyticsDashboard` will be upgraded to aggregate anonymized global SRS data to identify curriculum flaws.

### A. The "Most Difficult Words" Report
Identifies words with the lowest average `ease_factor` across all users.
- *Actionable Insight:* If `word_allora` has an average ease factor of 1.4 (meaning everyone fails it constantly), the curriculum designers can investigate if the English translation is ambiguous, if the audio is poor, or if the distractors are too tricky.

### B. The "Most Forgotten Words" (High Lapse Rate)
Identifies words that users reach `LEARNED` status on, but consistently fail when the interval stretches to 7 or 15 days.
- *Actionable Insight:* These words might lack sufficient contextual reinforcement. The factory can be instructed to inject these specific words into future scenario conversations to provide more reading practice.

### C. Global Dictionary Coverage
- Tracks the size of the extracted Global Dictionary (e.g., 3,845 words) against a standard CEFR A1/A2 frequency list (e.g., the top 2,000 Italian words).
- *Actionable Insight:* The admin panel can flag: "You have 116 scenarios, but the top 100 most common Italian words are missing 4 entries (e.g., 'nessuno')." This directly informs what Domain the next scenario should cover.

### D. "Free Ride" Analytics
- Tracks how many scenarios users complete purely by relying on Global Knowledge (i.e., scenario vocabulary lessons auto-completing because all words are known).
- *Actionable Insight:* If scenarios 80-116 have a 95% "Free Ride" rate, the curriculum is stagnating and needs more advanced B1 vocabulary injected.
