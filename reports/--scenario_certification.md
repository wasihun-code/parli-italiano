# Certification Report: --scenario

**Overall Status:** FAIL

- ❌ **Curriculum Coverage**
- ❌ **Audio Integrity**
- ❌ **Conversation Logic**
- ❌ **Distractor Quality**
- ❌ **Lesson Integrity**
- ❌ **Progression Validation**
- ❌ **Translation Completeness**
- ✅ **Keyboard & UI**
- ❌ **Domain Consistency**
- ❌ **Path Consistency**
- ✅ **Runtime Audio Flow**
- ❌ **Mini Lesson Audio Flow**
- ❌ **Scenario Integrity**

## Audit Logs
```text
Error loading files: [Errno 2] No such file or directory: 'src/data/exports/--scenario/conversations.json'

--- Audio Audit: --scenario ---
Total Nodes Checked: 0
Audio Errors: 4
  - Failed to load src/data/exports/--scenario/conversations.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/conversations.json'
  - Failed to load src/data/exports/--scenario/--scenario_vocabulary.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/--scenario_vocabulary.json'
  - Failed to load src/data/exports/--scenario/--scenario_phrases.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/--scenario_phrases.json'
  - Failed to load src/data/exports/--scenario/--scenario_sentences.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/--scenario_sentences.json'
Audio Audit: FAIL

Failed to load src/data/exports/--scenario/conversations.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/conversations.json'

--- Distractor Quality Audit: --scenario ---
  - Failed to load src/data/exports/--scenario/conversations.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/conversations.json'
  - Failed to load src/data/exports/--scenario/--scenario_vocabulary.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/--scenario_vocabulary.json'
  - Failed to load src/data/exports/--scenario/--scenario_phrases.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/--scenario_phrases.json'
  - Failed to load src/data/exports/--scenario/--scenario_sentences.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/--scenario_sentences.json'
Distractor Audit: FAIL

Failed to load src/data/exports/--scenario/mini_lessons.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/mini_lessons.json'

Error loading files: [Errno 2] No such file or directory: 'src/data/exports/--scenario/conversations.json'

--- Translation Audit: --scenario ---
  - Failed to load src/data/exports/--scenario/conversations.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/conversations.json'
  - Failed to load src/data/exports/--scenario/--scenario_vocabulary.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/--scenario_vocabulary.json'
  - Failed to load src/data/exports/--scenario/--scenario_phrases.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/--scenario_phrases.json'
  - Failed to load src/data/exports/--scenario/--scenario_sentences.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/--scenario_sentences.json'
Translation Audit: FAIL


--- Keyboard Accessibility Audit (STATIC) ---
Keyboard Audit: PASS


--- DOMAIN CONTAMINATION AUDIT: --scenario ---
WARN: No domain.json found in src/data/exports/--scenario. Skipping strict lexical check.
FAIL: Could not load vocabulary json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/--scenario_vocabulary.json'


--- PATH CONSISTENCY AUDIT: --scenario ---
  - Slug '--scenario' not found in scenarioMapping.ts
PATH CONSISTENCY AUDIT: FAIL


--- RUNTIME LEARNING FLOW AUDIT (STATIC) ---
Host autoplay implemented: YES
User autoplay present: NO
User manual speaker icon present: YES
CONVERSATION FLOW AUDIT: PASS


--- MINI LESSON AUDIO AUDIT: --scenario ---

Failed to load src/data/exports/--scenario/conversations.json: [Errno 2] No such file or directory: 'src/data/exports/--scenario/conversations.json'


```
