# Database Review — Phase 7.3 (Hybrid Mastery)

## 1. Executive Summary
This report outlines the additive Dexie schema required to transition from Scenario Mastery to Hybrid Mastery (V2). The design ensures 100% backward compatibility with V1 tables while enabling global vocabulary tracking and longitudinal review history.

## 2. Proposed Dexie Schema V2
The following tables will be added to `ParlaItalianoDB` via `this.version(2)`.

### 2.1 `global_dictionary` (Static Corpus)
Stores canonical word definitions. Shared across all scenarios.
- **Key Path:** `id` (e.g., `word_grazie`, `concept_floor_piano`)
- **Indexes:** `italian` (for lookup)
- **Fields:**
    - `id`: string (PK)
    - `italian`: string (Index)
    - `english_primary`: string
    - `audio_json`: string (serialized JSON metadata)
    - `part_of_speech`: string
    - `last_updated`: string (ISO 8601)

### 2.2 `global_progress` (User State)
Globalized SRS tracking for words, phrases, and sentences.
- **Key Path:** `item_id`
- **Indexes:** `item_type`, `next_review_at`
- **Fields:**
    - `item_id`: string (PK)
    - `item_type`: 'vocabulary' | 'phrase' | 'sentence'
    - `mastery_level`: number (0-100)
    - `correct_streak`: number
    - `total_attempts`: number
    - `last_reviewed_at`: string
    - `next_review_at`: string (ISO 8601)
    - `last_result`: boolean

### 2.3 `global_review_history` (Audit/Forgetting Model)
Chronological log of all review attempts.
- **Key Path:** `id` (auto-incrementing)
- **Indexes:** `item_id`, `timestamp`
- **Fields:**
    - `id`: number (PK, auto-increment)
    - `item_id`: string (Index)
    - `timestamp`: string (Index, ISO 8601)
    - `result`: boolean
    - `response_time_ms`: number
    - `scenario_id`: number (context of review)

### 2.4 `scenario_vocab_mapping_cache` (Relational)
High-performance join table for resolving which global words belong to which scenario.
- **Key Path:** `id` (scenario_id + ':' + global_dict_id)
- **Indexes:** `scenario_id`, `global_dict_id`, `[scenario_id+global_dict_id]` (compound)
- **Fields:**
    - `id`: string (PK)
    - `scenario_id`: number (Index)
    - `global_dict_id`: string (Index)
    - `sort_order`: number

## 3. Technical Implementation Code (for `db.ts`)

### 3.1 Type Definitions
```typescript
export interface GlobalDictionaryEntry {
  id: string;
  italian: string;
  english_primary: string;
  audio_json?: string;
  part_of_speech?: string;
  last_updated: string;
}

export interface GlobalProgress {
  item_id: string;
  item_type: 'vocabulary' | 'phrase' | 'sentence';
  mastery_level: number;
  correct_streak: number;
  total_attempts: number;
  last_reviewed_at: string;
  next_review_at: string;
  last_result?: boolean;
}

export interface GlobalReviewHistory {
  id?: number;
  item_id: string;
  timestamp: string;
  result: boolean;
  response_time_ms?: number;
  scenario_id?: number;
}

export interface ScenarioVocabMappingCache {
  id: string;
  scenario_id: number;
  global_dict_id: string;
  sort_order: number;
}
```

### 3.2 Dexie Schema Upgrade
```typescript
// Inside ParlaItalianoDatabase class
class ParlaItalianoDatabase extends Dexie {
  // ... existing members ...
  global_dictionary!: EntityTable<GlobalDictionaryEntry, 'id'>;
  global_progress!: EntityTable<GlobalProgress, 'item_id'>;
  global_review_history!: EntityTable<GlobalReviewHistory, 'id'>;
  scenario_vocab_mapping_cache!: EntityTable<ScenarioVocabMappingCache, 'id'>;

  constructor() {
    super('ParlaItalianoDB');
    
    // Existing Version 1
    this.version(1).stores({
      app_metadata: 'key',
      foundation_lessons: 'id, sort_order',
      foundation_terms: 'id, lesson_id, sort_order',
      foundation_exercises: 'id, lesson_id, sort_order',
      scenarios: 'id, category, sort_order',
      scenario_vocabulary: 'id, scenario_id, sort_order',
      scenario_phrases: 'id, scenario_id, sort_order',
      scenario_sentences: 'id, scenario_id, sort_order',
      srs_items: 'item_id, item_type, scenario_id, foundation_lesson_id, due_at',
      tts_cache: 'text',
    });

    // New Version 2 (Additive)
    this.version(2).stores({
      global_dictionary: 'id, italian',
      global_progress: 'item_id, item_type, next_review_at',
      global_review_history: '++id, item_id, timestamp',
      scenario_vocab_mapping_cache: 'id, scenario_id, global_dict_id, [scenario_id+global_dict_id]',
    });
  }
}
```

## 4. Backward Compatibility & Risk Assessment
- **Zero-Destruction Policy:** No `clear()` or `delete` operations are performed on V1 tables during this upgrade.
- **Redundancy Phase:** For a transitional period, vocabulary will exist in both `scenario_vocabulary` (Legacy) and `global_dictionary` (Master). UI components should be updated to prioritize the Global Dictionary when available.
- **Indexing Strategy:** The compound index `[scenario_id+global_dict_id]` is included to ensure O(1) lookup during scenario curriculum resolution, preventing frame drops in the mobile-first UI.
