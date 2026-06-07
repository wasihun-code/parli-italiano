# Phase 9.6a: Progress Design

## 1. Overview
V3 communicates three nested levels of progress to the user simultaneously.

## 2. Progress Levels

### A. Session Progress (The "Now")
- **UI:** Horizontal progress bar at the top of the header.
- **Value:** `(currentIndex + 1) / learningPath.length`.
- **Feedback:** "STEP 9 / 25".

### B. Scenario Progress (The "Goal")
- **UI:** "Scenario Title" and "Current Goal" (e.g., Finding the Entrance).
- **Goal Connection:** Items are sorted chronologically, so the bar represents the user's progress through the scenario's narrative arc.

### C. Conversation Readiness (The "Outcome")
- **UI:** Mini readiness meters in the footer.
- **Goal Connection:** Clear visualization of the 80/80/80 requirement.

## 3. Conclusion
The combination of these three indicators ensures the user knows exactly where they are, why they are doing it, and what they need to achieve next.
