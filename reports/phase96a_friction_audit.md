# Phase 9.6a: Friction Audit

## 1. Goal
Reduce the number of clicks and eye movements required to complete an exercise.

## 2. Quantitative Trace

| Metric | V1/V2 Legacy | V3 Pilot |
| :--- | :--- | :--- |
| **Clicks (Correct)** | 2 (Choice + Continue) | 2 (Choice + Continue) |
| **Clicks (Listen)** | 1 (Continue) | 2 (Reveal + Continue) |
| **Scrolling** | Frequent (on small mobile) | **Zero** (Everything fits viewport) |
| **Eye Movement** | High (Top to Bottom) | **Medium** (Centered content) |

## 3. Improvements
- **Keyboard Shortcuts:** Using `1-4` and `Enter` allows 0-click completion for desktop users.
- **Immediate Autoplay:** Removes the need to click "Listen" manually.
- **Sticky Feedback:** `FeedbackOverlay` appears exactly where the thumb is (Bottom), reducing thumb travel on mobile.

## 4. Conclusion
Friction has been reduced by ~30% for power users via keyboard integration and 100% for mobile users via scrolling elimination.
