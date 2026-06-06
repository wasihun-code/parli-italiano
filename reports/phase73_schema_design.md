# Phase 7.3 — Database Schema V2 Design

The Dexie schema has been additively upgraded to support Hybrid Mastery.

## 1. Target Schema Changes (`src/lib/db.ts`)

- **Retained Tables:** `scenarios`, `scenario_vocabulary`, `scenario_phrases`, `scenario_sentences`, `srs_items`, `foundation_lessons`.
- **New Version:** Dexie `SEED_VERSION` bumped to 2.

## 2. New Tables

### `global_dictionary`
- **Fields:** `id` (PK), `italian` (indexed), `english_primary`, `audio_json`, `part_of_speech`, `last_updated`.
- **Purpose:** Source of truth for 5,297 unique vocabulary items.

### `global_progress`
- **Fields:** `item_id` (PK), `item_type`, `mastery_level`, `correct_streak`, `total_attempts`, `last_reviewed_at`, `next_review_at` (indexed), `last_result`.
- **Purpose:** Tracks user mastery states (`UNKNOWN`, `LEARNING`, `LEARNED`, `ADVANCED`, `MASTERED`, `LAPSED`).

### `global_review_history`
- **Fields:** `id` (PK, auto-increment), `item_id` (indexed), `timestamp` (indexed), `result`, `response_time_ms`, `scenario_id`.
- **Purpose:** Append-only log for retention analytics.

### `scenario_vocab_mapping_cache`
- **Fields:** `id` (PK), `scenario_id` (indexed), `global_dict_id` (indexed), `sort_order`. Compound index on `[scenario_id+global_dict_id]`.
- **Purpose:** Fast lookup table tying scenarios to global vocabulary.
