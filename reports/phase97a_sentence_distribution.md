# Phase 9.7a: Sentence Training Rebalance

## 1. Distribution Audit
Before this fix, the `SessionGenerator.ts` sliced the first 25 items from the master path. Because the master path fell back to a default chronological sort when items tied, all vocabulary items (49 items in Lesson 1) were pushed to the top of the queue. As a result, the learner experienced a session comprised of **100% vocabulary** and 0% sentences.

## 2. Fix Implemented
Updated `SessionGenerator.ts` to explicitly enforce a categorical distribution for every session:
- **50% Vocabulary** (approx. 12 items)
- **20% Phrases** (approx. 5 items)
- **30% Sentences** (approx. 8 items)

If there is a shortage in any category, it dynamically fills the gap with the remaining items. Finally, the selected items are interleaved (shuffled) to ensure the learner constantly switches context between recognizing words and building sentences.

## 3. Result
Sentences are now guaranteed to be actively trained in every session, perfectly aligning the user experience with the ultimate goal of conversational readiness.
