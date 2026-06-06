# Final Mastery Recommendation

Based on the extensive forensic analysis, architectural investigations, and pedagogical design reviews conducted in Phase 6.1 through 6.5, here are the final recommendations for the Parla Italiano learning model.

### 1. Which SRS algorithm should Parla Italiano use?
**Recommendation: A Custom Hybrid (FSRS-Lite) Algorithm.**
A pure streak system (like Duolingo) is too punishing on memory lapses, and a pure SM-2 system (like Anki) relies heavily on user self-reporting ("Hard/Good/Easy"), which breaks the gamified, frictionless UX of Parla Italiano. 
The recommended algorithm deduces difficulty automatically from binary PASS/FAIL answers. It utilizes an "Ease Factor" to exponentially space out reviews for easy words, while employing a "Lapse Mechanism" (partial regression) rather than a full reset when a user forgets a word, ensuring a forgiving and highly adaptive learning curve.

### 2. What constitutes mastery?
Mastery is no longer a boolean switch flipped at the end of a scenario. It is a spectrum:
- **Known:** Answered correctly once (volatile).
- **Learning:** Passed micro-steps (e.g., 1m, 10m) within a single session.
- **Learned:** Survives a multi-day interval (e.g., 1d, 3d, 7d).
- **Mastered:** The spaced repetition interval surpasses **30 days**. The word is solidified in long-term memory.

### 3. What should happen when a mastered word appears in a new scenario?
**Recommendation: The "Skip-and-Contextualize" Model.**
When a globally `LEARNED` or `MASTERED` word (e.g., *grazie*) appears in a new scenario (e.g., *Hotel Check-In*):
- It is **dynamically hidden** from the introductory Vocabulary flashcard phase to completely eliminate review fatigue.
- However, it **remains visible** in the full text of the Conversation phase. This proves to the learner that they can actually read and understand their global vocabulary in new, diverse contexts.

### 4. How should Daily Review work?
**Recommendation: A Dedicated Global Queue.**
Reviews should be decoupled from scenarios. A user logs in and hits a central "Daily Review" button on the Home screen. The system prioritizes `RELEARNING` (recently lapsed) items first, followed by overdue `LEARNED` items, capped at a maximum of 100 reviews per day to prevent burnout. This ensures long-term retention without blocking a user from exploring new scenarios.

### 5. Is Hybrid Mastery worth implementing?
**ABSOLUTELY YES.**
The forensic data is overwhelming: the current Scenario Mastery architecture contains an **85.03% redundancy rate** in vocabulary. It forces a user to "re-learn" the word *grazie* 119 separate times. This level of repetition causes extreme pedagogical friction and user frustration. 

While the migration complexity is HIGH, the Hybrid Mastery architecture (Global Vocabulary + Scenario-Specific Phrases/Conversations) is the only path forward to make Parla Italiano a production-grade, CEFR-aligned language acquisition platform. It enables true proficiency tracking ("You know 1,200 words") while maintaining the situational immersion that makes the app unique.
