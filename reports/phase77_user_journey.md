# Phase 7.7 — User Journey Test

## 1. Fresh User Journey
**Path:** Apartment Key Pickup -> Hotel Check-In
- **Initial State:** User knows 0 words.
- **Experience:** During "Hotel Check-In", the user completes a conversation containing 80 unique words. 
- **Reinforcement Logic:** Because all words are `UNKNOWN` or `LEARNING` (High Priority score: 70-80), the service ranks them above `MASTERED` words. The top 20 words receive implicit credit, safely establishing the baseline memory trace without overwhelming the daily review queue the next day.

## 2. Intermediate User Journey
**Path:** Dining -> Grocery Store
- **Initial State:** User knows 200 words. They have lapsed on "pane" (bread) and "latte" (milk).
- **Experience:** User completes a Grocery conversation containing "pane", "latte", and 60 other words.
- **Reinforcement Logic:** `LAPSED` items have a priority score of 100. "pane" and "latte" jump to the very top of the reinforcement queue, consuming 2 of the 20 budget slots. The remaining 18 slots are given to new target vocabulary. The user seamlessly refreshes forgotten words without needing a flashcard.

## 3. Advanced User Journey
**Path:** Work/Study -> Job Interview
- **Initial State:** User knows 1,200 words. `grazie` and `buongiorno` are `MASTERED`.
- **Experience:** User completes a 10-turn interview containing 150 unique words.
- **Reinforcement Logic:** The new target words take the first 15 slots. The 5 remaining slots are distributed to the lowest-mastery known words. `grazie` (score: 10) misses the cutoff, avoiding useless SRS updates. The memory model is successfully stabilized.
