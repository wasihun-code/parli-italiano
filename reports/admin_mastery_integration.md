# Admin Mastery Integration Plan

The Admin Panel will serve as the diagnostic tool for the new FSRS-Lite algorithm.

## New Metrics Required

### 1. Global Dictionary Coverage
- **Description:** Size of the `global_dictionary.json` vs CEFR A1/A2 targets.
- **Value:** Guides content creators on what Domain to tackle next (e.g., "We are missing 50 essential A2 verbs").

### 2. Known vs. Mastered Vocabulary
- **Description:** Aggregates user progress to show the average vocabulary size.
- **Value:** Tracks the overall efficacy of the platform.

### 3. Review Accuracy & Retention Rate
- **Description:** The percentage of `REVIEW_DUE` items answered correctly.
- **Value:** If retention drops below 80%, the `ease_factor` math in the FSRS-Lite algorithm must be adjusted to schedule reviews sooner.

### 4. Most Forgotten Words
- **Description:** Words with the highest number of `LAPSED` state transitions.
- **Value:** Identifies vocabulary that lacks contextual reinforcement. Admin can command the factory to inject these words into future conversation designs.

### 5. Most Difficult Words
- **Description:** Words with the lowest average `ease_factor`.
- **Value:** Identifies problematic flashcards (e.g., ambiguous English translations or confusing audio) requiring manual correction in the overrides file.

### 6. Review Queue Health
- **Description:** Average number of overdue reviews per user.
- **Value:** Identifies if the 100/day cap is sufficient or if users are experiencing review bankruptcy.
