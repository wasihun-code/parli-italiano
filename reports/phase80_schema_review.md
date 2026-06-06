# Phase 8.0 — IndexedDB Schema Review Report

## 1. Index Audit

### 1.1 `global_progress`
*   **Current Stores:** `item_id, item_type, next_review_at`
*   **Analysis:** 
    *   `item_id` is the primary key.
    *   `next_review_at` is correctly indexed for the Review Queue.
    *   **Missing Index:** `mastery_level` and `correct_streak`. `ReviewQueueService.getDailyQueue` uses these to identify LAPSED items (`correct_streak === 0 && total_attempts > 0`). 
*   **Recommendation:** Update store to `item_id, item_type, next_review_at, mastery_level, correct_streak`.

### 1.2 `global_review_history`
*   **Current Stores:** `++id, item_id, timestamp`
*   **Analysis:**
    *   `item_id` is indexed, which is good for fetching history for a specific item.
    *   `timestamp` is indexed, good for time-based reports.
*   **Recommendation:** Add `scenario_id` to indexes if we plan to show scenario-specific progress reports in the future.

### 1.3 `scenario_vocab_mapping_cache`
*   **Current Stores:** `id, scenario_id, global_dict_id, [scenario_id+global_dict_id]`
*   **Analysis:** Compound index `[scenario_id+global_dict_id]` is excellent for looking up specific mappings.

## 2. Query Pattern Review

### 2.1 Review Queue Retrieval
*   **Current:** `db.global_progress.filter(...).toArray()`
*   **Proposed:** 
    ```typescript
    const due = await db.global_progress.where('next_review_at').belowOrEqual(now).toArray();
    const lapsed = await db.global_progress.where('correct_streak').equals(0).and(p => p.total_attempts > 0).toArray();
    ```
    Actually, IndexedDB doesn't handle multiple `where` clauses easily without compound indexes.
    A better approach for LAPSED might be a compound index `[correct_streak+total_attempts]`.

### 2.2 Global Dictionary Lookups
*   Frequently queried by `italian` for token matching.
*   **Current Stores:** `id, italian`
*   **Analysis:** `italian` is already indexed. This is correct.

## 3. Scalability & Future-Proofing

*   **Compound Indexing:** For Phase 8.5 (Advanced Analytics), we should consider compound indexes on `global_review_history` like `[item_id+timestamp]` to speed up SRS interval calculations.
*   **Storage Limits:** As `global_review_history` grows, it could exceed 50MB. We should consider a retention policy or a more compressed storage format for history (e.g., storing results as a bitstring for each item) in Phase 9.

## 4. Immediate Schema Actions
1. Add `mastery_level` and `correct_streak` to `global_progress` indexes.
2. Verify that `global_review_history` is handling auto-increment correctly (it is).
