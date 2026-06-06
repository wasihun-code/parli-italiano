# Phase 7.8 — User Journey Test

## 1. Fresh User Journey
- **State:** User has never completed a scenario.
- **Home Screen:** The `DailyReviewBanner` does not render. 
- **Navigation:** The user clicks a static "Review" button on their profile.
- **Queue Generation:** `ReviewQueueService` returns an empty array.
- **UI:** The screen displays "Ripasso completato! Nessuna parola in scadenza." (Review complete! No words due). The user is directed back to explore new scenarios.

## 2. Intermediate User Journey
- **State:** User has 45 items due. 5 of them are `LAPSED`.
- **Home Screen:** A purple banner displays "🧠 45 Reviews Due".
- **Queue Generation:** The service fetches the 45 items. The 5 `LAPSED` words are assigned a priority score of 100 and sorted to indices 0-4.
- **UI:** The user starts the review. The first 5 flashcards force the user to rebuild their broken memory traces. Only after passing these do they move on to the 40 standard `DUE` items.
- **Result:** The user successfully recovers their lapsed vocabulary before learning anything new.

## 3. Advanced User Journey
- **State:** User has been away for a month. They have 300 items due.
- **Home Screen:** The banner displays "🧠 100 Reviews Due" (Capped).
- **Queue Generation:** The service fetches all 300. It sorts them by `LAPSED` > `RELEARNING` > `DUE`. It then slices the array at index 100.
- **UI:** The user completes a manageable 100-item session. 
- **Result:** The user is protected from burnout. They clear the most critical 100 items today, and the remaining 200 will be tackled over the next two days, ensuring long-term retention without immediate fatigue.
