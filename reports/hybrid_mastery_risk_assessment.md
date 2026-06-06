# Hybrid Mastery Risk Assessment

## 1. Technical Risks

**Risk:** UI Freezes during Implicit Reviews (Probability: Medium, Impact: High)
- *Description:* Dispatching 40+ Zustand state updates when a user finishes a conversation could block the main thread and freeze the victory screen animation.
- *Mitigation:* Implement batched updates or Web Workers to handle bulk SRS calculations in the background.

**Risk:** LocalStorage Quota Exceeded (Probability: Low, Impact: Critical)
- *Description:* The `srsStore` currently persists to `localStorage`, which has a 5MB hard limit. Storing 4,000 FSRS items might exceed this.
- *Mitigation:* Migrate the `srsStore` persistence layer to Dexie (IndexedDB) before launching Hybrid Mastery.

## 2. Pedagogical Risks

**Risk:** "Swiss Cheese" Scenarios (Probability: High, Impact: Medium)
- *Description:* If a user skips 90% of the vocabulary in a scenario because they know the global words, they might struggle with the Conversation phase because they haven't refreshed those words in context recently.
- *Mitigation:* Ensure that if a word is `REVIEW_DUE`, the user MUST complete the Daily Review queue before unlocking the Conversation phase of the scenario.

## 3. Migration Risks

**Risk:** Loss of User Progress (Probability: High, Impact: Critical)
- *Description:* The `migrate_to_v2.ts` script fails to map a legacy ID to a new Global ID, permanently wiping the user's hard-earned streak.
- *Mitigation:* Create a `srs_items_v1_backup` table during migration. Implement rigorous test coverage on the migration script using edge cases before deployment.

## 4. Data Integrity Risks

**Risk:** Factory Extract Errors (Probability: Medium, Impact: High)
- *Description:* The normalization logic in the new `linguistic_extractor.py` strips out crucial accents or punctuation, causing two different words to merge into the same global ID (e.g., `pero` vs `però`).
- *Mitigation:* The normalizer must explicitly preserve Italian accents. All Factory extraction changes must pass the `certification_pipeline` before merging.
