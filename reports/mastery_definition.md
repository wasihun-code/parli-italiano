# Mastery Definition

In Parla Italiano, "knowing" a word is not binary. It is a spectrum of retention. This document defines the exact thresholds and definitions for each pedagogical state.

## 1. Known
A word is strictly **"Known"** the moment the user successfully identifies its meaning at least once. 

- **Threshold:** `correct_attempts >= 1`.
- **Significance:** The word is no longer completely foreign. However, it is highly volatile and likely to be forgotten within hours. 
- **UI Treatment:** Shown as "Encountered" or "Familiar".

## 2. Learning
A word is in the **"Learning"** state while the user is establishing short-term working memory.

- **Threshold:** `state == LEARNING`.
- **Streak Requirement:** Must achieve 3 consecutive correct recalls (e.g., 1m, 5m, 10m intervals within a single lesson session).
- **Accuracy Requirement:** 100% within the micro-session to graduate. A failure resets the micro-streak to 0.
- **Significance:** The word is in short-term memory and ready to be tested the next day.

## 3. Learned
A word is **"Learned"** when it has graduated from the initial micro-session and entered the multi-day spaced repetition schedule.

- **Threshold:** `state == LEARNED` (Graduated from `LEARNING` or `RELEARNING`).
- **Review Requirements:** The interval is measured in days (1d, 3d, 7d, 15d).
- **Retention Requirements:** The user must recall the word after at least 24 hours of sleeping/forgetting time.
- **Significance:** The word is in medium-term memory. 
- **UI Treatment:** The word counts towards the user's "Global Vocabulary Size" metric.

## 4. Mastered
A word is **"Mastered"** when it has proven highly resilient to forgetting over a long period.

- **Threshold:** `state == MASTERED`.
- **Requirement:** The current SRS interval reaches **>= 30 days**.
- **Significance:** The word is in long-term memory. The user can reliably recall this word without seeing it for a month. 
- **UI Treatment:** Unlocks the "Gold" status for the word. Counts towards the "Mastered Words" metric.

## Summary Table

| Term | Definition | SRS Interval | UI Metric |
| :--- | :--- | :--- | :--- |
| **Known** | Correct once. | Minutes | "Encountered" |
| **Learning** | Building short-term memory. | Minutes | - |
| **Learned** | Building medium-term memory. | 1 - 29 Days | "Vocabulary Size" |
| **Mastered**| Solidified long-term memory. | 30+ Days | "Mastered Words" |
