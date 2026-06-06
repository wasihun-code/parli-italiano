# Hybrid Mastery UX Design

The shift to Hybrid Mastery fundamentally changes how progress is visualized to the learner. Instead of focusing purely on "completed folders," the UX shifts to emphasize actual language acquisition.

## 1. Home Screen (Dashboard)

The current dashboard focuses on Scenario paths. The new dashboard will introduce a **Global Knowledge Panel** at the very top:

- **Primary Metric:** `Vocabulary Size: 1,245 Words` (A count of all words in the `LEARNED` and `MASTERED` states).
- **Secondary Metrics:**
  - `Mastered Words: 300` (Gold icon, words with > 30d interval).
  - `Daily Reviews Due: 42` (Red/Orange notification badge).
- **Call to Action:** A prominent "Review Now" button that enters the Daily Review module.

## 2. Scenario Detail Screen

When a user clicks into a specific scenario (e.g., "At the Bank"):

- **Vocabulary Tab:**
  - `Total Words: 40`
  - `Already Known: 25` (Visualized as a solid green progress bar).
  - `New Words to Learn: 15` (Visualized as an empty bar).
  - The UI clearly communicates that exploring new scenarios is "cheaper" because the user brings their existing knowledge with them.

- **Item Lists:** 
  - Words that are already known will have a small gold spark or checkmark next to them in the curriculum lists.

## 3. Global Dictionary / Word Detail Screen

A new feature accessible from the profile or a bottom nav tab.

- **Searchable List:** The user can scroll through their entire known vocabulary.
- **Word Detail Modal:** Clicking a word (e.g., `word_prenotazione`) shows:
  - **Mastery Level:** Level 4 (Learned) / Level MAX (Mastered).
  - **Next Review:** "Due in 14 Days".
  - **Contexts:** "You encountered this word in: *Hotel Check-In*, *Ordering Pizza*, *Booking a Dentist*."
  - **Example Sentence:** Pulls one random sentence from the scenarios using this word.

## 4. End of Scenario Screen

When a scenario is completed, the victory screen summarizes:
- "+15 New Words Added to Vocabulary!"
- "+5 Phrases Mastered!"
- "+250 XP"
