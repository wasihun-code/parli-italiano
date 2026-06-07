# Parla Italiano: Hybrid Mastery Interaction Audit

## 1. Mastery Level Dynamics

The system utilizes an FSRS-lite model with 7 discrete states. The `CurriculumAdaptationService` determines what a learner sees based on their global progress.

| Global Mastery % | Effect on Local Lesson (Vocabulary) |
| :--- | :--- |
| **0 - 25%** | Standard experience. All new words are presented. |
| **50%** | Half of the vocabulary is skipped. "Safety Floor" ensures at least 2 words remain. |
| **75%** | Most words skipped. Review intervals for existing words may increase. |
| **100%** | The specialized Vocabulary Screen will show only 2 "Safety Floor" words for context refresh. |

## 2. Safety Floor & Empty Lessons

**Can lessons become empty?**
- **No.** The `CurriculumAdaptationService` enforces a minimum of **2 items** per lesson.
- If a learner has mastered all 50 words in a lesson via previous scenarios, the service will "pop" 2 of the most recently mastered words back into the "Visible" list to provide situational context.

## 3. Scope of Adaptation

| Element | Affected by Global Mastery? | Mechanism |
| :--- | :--- | :--- |
| **Vocabulary** | **YES** | `CurriculumAdaptationService` + `db.global_progress` |
| **Phrases** | **NO** | Fixed in `srsStore` per local ID. No global resolution. |
| **Sentences** | **NO** | Fixed in `srsStore` per local ID. No global resolution. |
| **Conversations** | **PARTIAL** | Content is static, but completion grants global credit to underlying words. |

## 4. Screen-Level Implementation

| Screen | Type | Status |
| :--- | :--- | :--- |
| **VocabularyTrainingScreen** | **DYNAMIC** | Fully integrated with Hybrid Mastery V2. Filters content globally. |
| **MiniLessonTrainingScreen** | **STATIC** | **CRITICAL FINDING**: This screen ignores Global Mastery. It loads the 100% fixed `mini_lessons.json` and presents every word, even if mastered globally. |
| **PhraseTrainingScreen** | **LOCAL** | Only filters based on local `srsStore` learned state. |
| **SentenceTrainingScreen** | **LOCAL** | Only filters based on local `srsStore` learned state. |
| **ScriptedConversationScreen** | **STATIC** | Content is fixed, but uses `ConversationReinforcementService` for output only. |

## 5. Architectural Risks

1.  **Mini-Lesson Disconnect:** A learner who has "Mastered" Italian will still be forced to sit through a "Lesson 1: Vocabulary" that shows basic words they already know, because the `MiniLessonTrainingScreen` does not yet implement the `CurriculumAdaptationService`.
2.  **ID Collision Risk:** The system currently relies on prefix-free IDs (`v1`, `v2`) in the JSON exports. While the database attempts to namespace these as `s22-v1` in fallback mode, the **Production Data paths** used by all 116 scenarios risk over-writing each other in the `srsStore` and specialized tables if namespaces are not rigorously enforced at the ingestion layer.
3.  **Phrase/Sentence Isolation:** There is no global registry for phrases. A learner who learns "Come stai?" in Scenario 1 must re-learn it in Scenario 5 because it lacks a global ID mapping.
