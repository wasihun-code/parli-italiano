# Phase 8.0 — Dexie Performance Optimization Report

## 1. Bottleneck Analysis

### 1.1 `ConversationReinforcementService.reinforceConversation`
*   **Sequential Dictionary Reads:** Iterates over `globalIds` and calls `db.global_dictionary.get(gid)` for each. For a scenario with 30-50 vocabulary items, this results in 30-50 individual IndexedDB requests.
*   **Sequential Progress Reads:** After filtering, it again iterates and calls `GlobalProgressService.getMasteryState(gid)` and `db.global_dictionary.get(gid)`.
*   **Sequential Writes:** Calls `GlobalProgressService.recordAnswer` in a loop.
    *   Inside `recordAnswer`:
        *   `db.global_progress.get` (Read)
        *   `db.global_progress.put` (Write)
        *   `db.global_review_history.add` (Write)
*   **Impact:** A single conversation completion can trigger 100+ database operations, leading to UI stutter on low-end devices and slow response times.

### 1.2 `ReviewQueueService.getDailyQueue`
*   **Collection Filtering:** Uses `db.global_progress.filter(...).toArray()`. While `next_review_at` is indexed, the current implementation might not be utilizing the index effectively if it's mixed with other filters in a `.filter()` callback rather than using `.where()`.
*   **Sequential Metadata Resolution:** Iterates through capped items and calls `db.global_dictionary.get(p.item_id)` individually.

### 1.3 `GlobalProgressService.recordAnswer`
*   **Read-Before-Write:** Always performs a `get` before a `put`.
*   **Non-Atomic History Recording:** Progress update and history recording are not wrapped in a transaction, potentially leading to data inconsistency if one fails.

## 2. Optimization Plan

### 2.1 Implementation of Bulk Operations
*   Replace individual `.get()` calls with `db.table.bulkGet()`.
*   Replace individual `.put()`/`.add()` calls with `db.table.bulkPut()` and `db.table.bulkAdd()`.

### 2.2 Transactional Integrity
*   Wrap multi-table updates (Progress + History) in `db.transaction('rw', ...)`.
*   This ensures atomicity and improves performance by allowing the browser to optimize disk I/O.

### 2.3 Refactoring `GlobalProgressService`
*   Introduce `recordBatchResults` to handle multiple updates efficiently.
*   Optimize `recordAnswer` to be a wrapper around a single-item batch if needed, but prioritize batching at the service level.

### 2.4 Refactoring `ConversationReinforcementService`
*   Fetch all necessary dictionary entries and progress states upfront using `bulkGet`.
*   Process logic in-memory.
*   Commit all changes in a single transaction at the end.

## 3. Expected Outcomes
*   Reduction in DB round-trips by ~80-90% for conversation reinforcement.
*   Elimination of UI micro-stutters during "Conversation Complete" transitions.
*   Improved scalability as the Global Dictionary grows.
