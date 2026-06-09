## Curriculum V4 – Canonical Data Schema

This document defines the official data structures for the Curriculum V4 system. All components—curriculum generation, verification, exercise creation, progress tracking, and runtime delivery—must adhere to these schemas. No runtime logic is described; only the shape and meaning of the data.

---

### 1. Word

**Description**  
Represents a single Italian word that a learner will encounter. Words are the atomic building blocks of the language curriculum. Each word has a globally unique identifier, its canonical Italian form, an English gloss, and metadata describing its introduction point and linguistic properties.

**JSON Structure**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier, format `w_XXXXXX` (e.g., `w_000001`). |
| `italian` | string | yes | Canonical Italian word form (lemma or inflected form as listed in the Knowledge Graph). |
| `english` | string | yes | English translation/gloss. |
| `part_of_speech` | string | no | Optional tag (e.g., `noun`, `verb`, `adjective`). |
| `frequency` | integer | no | Number of sentences in the curriculum where this word appears (from the global inventory). |
| `introduced_in_lesson` | string | yes | ID of the micro‑lesson where this word is first introduced (e.g., `ML_001`). |
| `tags` | array of strings | no | Optional metadata labels (e.g., `["greeting", "A1"]`). |
| `metadata` | object | no | Extensible key‑value store for tooling (e.g., `{"source_scenario": "smooth_check_in"}`). |

**Example Object**
```json
{
  "id": "w_000001",
  "italian": "ciao",
  "english": "hi / hello",
  "part_of_speech": "interjection",
  "frequency": 4,
  "introduced_in_lesson": "ML_001",
  "tags": ["greeting", "A1"],
  "metadata": {
    "source_scenario": "smooth_check_in"
  }
}
```

---

### 2. Phrase

**Description**  
A multi‑word expression that forms a meaningful chunk. A phrase is defined only after all its constituent words have been introduced. It stores explicit dependencies on the words it requires.

**JSON Structure**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier, format `p_XXXXXX` (e.g., `p_000001`). |
| `italian` | string | yes | Full Italian phrase. |
| `english` | string | yes | English translation. |
| `depends_on_words` | array of strings | yes | Ordered list of word IDs that must be known before this phrase can be introduced. |
| `introduced_in_lesson` | string | yes | Micro‑lesson ID where the phrase is first taught. |
| `frequency` | integer | no | Number of sentences where the phrase appears. |
| `tags` | array of strings | no | Optional tags. |
| `metadata` | object | no | Extensible metadata. |

**Example Object**
```json
{
  "id": "p_000001",
  "italian": "piacere di conoscerti",
  "english": "nice to meet you",
  "depends_on_words": ["w_000002", "w_000003"],
  "introduced_in_lesson": "ML_002",
  "frequency": 3,
  "tags": ["greeting", "A1"],
  "metadata": {}
}
```

---

### 3. Sentence

**Description**  
A complete utterance from a conversation turn. It depends on a set of words and phrases. The sentence is the largest unit of instruction before full conversation turns.

**JSON Structure**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier, format `s_XXXXXX` (e.g., `s_000001`). |
| `italian` | string | yes | Full Italian sentence. |
| `english` | string | yes | English translation. |
| `depends_on_words` | array of strings | yes | Word IDs required for understanding. |
| `depends_on_phrases` | array of strings | yes | Phrase IDs required for understanding. |
| `introduced_in_lesson` | string | yes | Micro‑lesson ID. |
| `sentence_type` | string | no | e.g., `declarative`, `interrogative`, `imperative`. |
| `difficulty` | string | no | CEFR level or custom tag (e.g., `A1`). |
| `metadata` | object | no | Extensible data. |

**Example Object**
```json
{
  "id": "s_000001",
  "italian": "Ciao! Piacere di conoscerti. Sei arrivato davanti al palazzo?",
  "english": "Hi! Nice to meet you. Have you arrived in front of the building?",
  "depends_on_words": ["w_000001","w_000002","w_000003","w_000004","w_000005","w_000006","w_000007"],
  "depends_on_phrases": ["p_000001","p_000002"],
  "introduced_in_lesson": "ML_003",
  "sentence_type": "interrogative",
  "difficulty": "A1",
  "metadata": {}
}
```

---

### 4. Conversation Turn

**Description**  
A single utterance in a conversational exchange, spoken either by the host or the user. A turn references exactly one sentence. It also carries the scenario and turn order for practice sequencing.

**JSON Structure**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier, format `t_XXXXXX` (e.g., `t_000001`). |
| `scenario` | string | yes | Scenario name (e.g., `smooth_check_in`). |
| `speaker` | string | yes | Either `host` or `user`. |
| `sentence_id` | string | yes | ID of the sentence spoken in this turn. |
| `turn_index` | integer | yes | Position within the scenario’s conversation (1‑based). |
| `introduced_in_lesson` | string | yes | Micro‑lesson where this turn is first practiced. |
| `metadata` | object | no | Extensible metadata. |

**Example Object**
```json
{
  "id": "t_000001",
  "scenario": "smooth_check_in",
  "speaker": "host",
  "sentence_id": "s_000001",
  "turn_index": 1,
  "introduced_in_lesson": "ML_003",
  "metadata": {}
}
```

---

### 5. Micro Lesson

**Description**  
A micro‑lesson is the atomic unit of curriculum delivery. It bundles a small set of new words, phrases, sentences, and conversation turns, all introduced according to strict dependency ordering.

**JSON Structure**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `lesson_id` | string | yes | Unique identifier (e.g., `ML_001`). |
| `title` | string | yes | Human‑readable title (e.g., “Greeting & Arrival”). |
| `objective` | string | no | Short description of what the learner will achieve. |
| `new_words` | array of string | yes | Word IDs introduced in this lesson. |
| `new_phrases` | array of string | yes | Phrase IDs introduced. |
| `new_sentences` | array of string | yes | Sentence IDs introduced. |
| `new_turns` | array of string | yes | Turn IDs introduced. |
| `prerequisite_lesson_ids` | array of string | no | Lessons that must be completed before this one can start. |
| `estimated_duration_min` | integer | no | Approximate time in minutes to complete. |
| `metadata` | object | no | Extensible data. |

**Example Object**
```json
{
  "lesson_id": "ML_003",
  "title": "First conversation – Greeting & Arrival",
  "objective": "Understand and produce basic greeting and location exchange.",
  "new_words": [],
  "new_phrases": [],
  "new_sentences": ["s_000001","s_000002"],
  "new_turns": ["t_000001","t_000002"],
  "prerequisite_lesson_ids": ["ML_001","ML_002"],
  "estimated_duration_min": 12,
  "metadata": {}
}
```

---

### 6. Entity Progress

**Description**  
Tracks a learner’s state and performance for any single curriculum entity (word, phrase, sentence, turn). This is the runtime record that implements the Learning State Machine.

**JSON Structure**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `entity_id` | string | yes | Unique entity ID (e.g., `w_000001`). |
| `entity_type` | string | yes | One of `word`, `phrase`, `sentence`, `turn`. |
| `state` | string | yes | Current state: `UNSEEN`, `INTRODUCED`, `PRACTICED`, `MASTERED`, `FORGOTTEN`. |
| `mastery_score` | number | yes | Float between 0.0 and 1.0. |
| `times_seen` | integer | yes | Total number of times the entity has been presented (exposures + practice + reviews). |
| `correct_count` | integer | yes | Number of correct responses across all exercises/reviews. |
| `incorrect_count` | integer | yes | Number of incorrect responses. |
| `streak` | integer | yes | Consecutive correct answers in recent interactions. |
| `first_seen` | string (ISO 8601) | yes | Timestamp of first exposure (UNSEEN → INTRODUCED). |
| `last_seen` | string (ISO 8601) | yes | Timestamp of most recent interaction. |
| `last_reviewed` | string (ISO 8601) | no | Timestamp of last review attempt (if any). |
| `next_review` | string (ISO 8601) | no | Scheduled date for next review (null if no review due). |
| `review_interval_days` | number | no | Current spacing interval for the next review (only meaningful after PRACTICED). |
| `consecutive_successes` | integer | no | Number of successful reviews in a row (for spacing algorithm). |
| `consecutive_failures` | integer | no | Number of failed reviews in a row (to trigger FORGOTTEN). |
| `response_time_avg_ms` | number | no | Average response time in milliseconds (optional telemetry). |
| `metadata` | object | no | Extensible data (e.g., algorithm version). |

**Example Object**
```json
{
  "entity_id": "w_000012",
  "entity_type": "word",
  "state": "PRACTICED",
  "mastery_score": 0.72,
  "times_seen": 5,
  "correct_count": 4,
  "incorrect_count": 1,
  "streak": 2,
  "first_seen": "2024-01-15T10:23:00Z",
  "last_seen": "2024-01-15T10:35:00Z",
  "last_reviewed": "2024-01-16T09:10:00Z",
  "next_review": "2024-01-17T09:10:00Z",
  "review_interval_days": 1,
  "consecutive_successes": 1,
  "consecutive_failures": 0,
  "response_time_avg_ms": 1800,
  "metadata": {}
}
```

---

### 7. Review Queue Entry

**Description**  
An item that has been scheduled for review. The review scheduler uses this object to inject review exercises into micro‑lessons. It references an entity and indicates when and how it should be reviewed.

**JSON Structure**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `entity_id` | string | yes | ID of the entity to review. |
| `entity_type` | string | yes | `word`, `phrase`, `sentence`, or `turn`. |
| `due_date` | string (ISO 8601) | yes | Date and time when the review is due. |
| `scheduled_review_type` | string | yes | Preferred exercise type (e.g., `Match`, `Recall`, `Dictation`, `BuildSentence`). |
| `priority` | integer | yes | Scheduling priority (lower number = sooner). Based on `due_date` proximity and retention risk. |
| `state_before_review` | string | yes | Entity state at the time the review was scheduled (`PRACTICED` or `MASTERED`). |
| `created_at` | string (ISO 8601) | yes | Timestamp when this entry was created. |
| `metadata` | object | no | Extensible (e.g., review algorithm version). |

**Example Object**
```json
{
  "entity_id": "p_000004",
  "entity_type": "phrase",
  "due_date": "2024-01-18T08:00:00Z",
  "scheduled_review_type": "ListenChoose",
  "priority": 1,
  "state_before_review": "PRACTICED",
  "created_at": "2024-01-16T08:00:00Z",
  "metadata": {}
}
```

---

### 8. Lesson Completion Record

**Description**  
A snapshot written when a learner finishes a micro‑lesson (or a significant portion). It records which new entities were practiced and the overall outcome, enabling scenario progress and prerequisite checks.

**JSON Structure**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `lesson_id` | string | yes | Micro‑lesson identifier. |
| `learner_id` | string | yes | Unique identifier for the learner (outside scope, but required). |
| `started_at` | string (ISO 8601) | yes | Timestamp when the learner began the lesson. |
| `completed_at` | string (ISO 8601) | yes | Timestamp of completion. |
| `new_entities_practiced` | object | yes | Breakdown of entity types introduced and practiced: `{ "words": ["w_id",...], "phrases": [...], "sentences": [...], "turns": [...] }`. |
| `all_turns_practiced` | boolean | yes | True if every turn in the lesson reached at least PRACTICED state. |
| `mastery_challenge_passed` | boolean | no | Whether the optional end‑of‑lesson mastery challenge was passed (if enabled). |
| `metadata` | object | no | Additional data (e.g., time spent per stage). |

**Example Object**
```json
{
  "lesson_id": "ML_003",
  "learner_id": "user_abc123",
  "started_at": "2024-01-15T10:23:00Z",
  "completed_at": "2024-01-15T10:45:00Z",
  "new_entities_practiced": {
    "words": [],
    "phrases": [],
    "sentences": ["s_000001","s_000002"],
    "turns": ["t_000001","t_000002"]
  },
  "all_turns_practiced": true,
  "mastery_challenge_passed": false,
  "metadata": {}
}
```

---

### 9. Scenario Progress

**Description**  
Tracks a learner’s progress through a full conversational scenario (e.g., “Smooth Check‑In”). It aggregates turn practice, completion status, and readiness.

**JSON Structure**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `scenario_id` | string | yes | Scenario identifier (e.g., `smooth_check_in`). |
| `learner_id` | string | yes | Learner identifier. |
| `total_turns` | integer | yes | Total number of turns in the scenario (host + user). |
| `turns_practiced` | integer | yes | Count of turns that have reached at least PRACTICED. |
| `turns_mastered` | integer | yes | Count of turns in MASTERED state. |
| `completed` | boolean | yes | True if all turns are PRACTICED (or MASTERED) and the final conversation exercise has been completed. |
| `last_turn_practiced` | string | no | Turn ID of the last turn that was practiced. |
| `conversation_finalized` | boolean | yes | Whether the full scenario conversation practice (all turn pairs) has been successfully completed. |
| `metadata` | object | no | Extensible (e.g., scenario version). |

**Example Object**
```json
{
  "scenario_id": "smooth_check_in",
  "learner_id": "user_abc123",
  "total_turns": 20,
  "turns_practiced": 12,
  "turns_mastered": 4,
  "completed": false,
  "last_turn_practiced": "t_000012",
  "conversation_finalized": false,
  "metadata": {}
}
```

---

### 10. Audit Result

**Description**  
Standard output for every verification audit (A01–A07). Provides a deterministic pass/fail result along with detailed failure information to guide curriculum authors.

**JSON Structure**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `audit_id` | string | yes | Unique identifier for this audit run (e.g., UUID). |
| `audit_type` | string | yes | One of: `dependency`, `coverage`, `duplicate_introduction`, `lesson_flow`, `state_machine`, `conversation_readiness`, `exercise_eligibility`. |
| `target` | object | yes | Object describing what was audited (e.g., `{"lesson_id": "ML_005"}` or `{"entity_id": "w_000012", "exercise_type": "Recall"}`). |
| `passed` | boolean | yes | True only if all validation rules passed. |
| `timestamp` | string (ISO 8601) | yes | When the audit was executed. |
| `failures` | array of objects | yes | List of failure objects (empty if passed). Each failure contains: `rule` (string), `description` (string), `affected_entities` (array of IDs). |
| `summary` | string | no | Human‑readable summary of the audit outcome. |
| `metadata` | object | no | Additional data (e.g., duration, algorithm version). |

**Failure Object (inside `failures`)**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `rule` | string | yes | Identifier of the specific rule violated (e.g., `DEPENDENCY_FORWARD_REF`). |
| `description` | string | yes | Detailed explanation of what went wrong. |
| `affected_entities` | array of strings | yes | Entity IDs involved in the failure. |

**Example Object – Passed**
```json
{
  "audit_id": "aud_20240115_001",
  "audit_type": "dependency",
  "target": { "lesson_id": "ML_005" },
  "passed": true,
  "timestamp": "2024-01-15T12:00:00Z",
  "failures": [],
  "summary": "All dependencies satisfied. No forward references.",
  "metadata": {}
}
```

**Example Object – Failed**
```json
{
  "audit_id": "aud_20240115_002",
  "audit_type": "state_machine",
  "target": { "lesson_id": "ML_010" },
  "passed": false,
  "timestamp": "2024-01-15T12:05:00Z",
  "failures": [
    {
      "rule": "PREREQUISITE_NOT_PRACTICED",
      "description": "Phrase p_000007 depends on word w_000018 which is still INTRODUCED (not PRACTICED).",
      "affected_entities": ["p_000007", "w_000018"]
    }
  ],
  "summary": "1 failure: prerequisite not sufficiently practiced.",
  "metadata": {}
}
```

---

**All schemas are now formally defined. Implementations must serialize, validate, and exchange data according to these structures. No deviations are permitted without updating this canonical specification.**
