# Certification Report: --help

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
Error loading files: [Errno 2] No such file or directory: 'src/data/exports/--help/conversations.json'

--- Audio Audit: --help ---
Total Nodes Checked: 0
Audio Errors: 4
  - Failed to load src/data/exports/--help/conversations.json: [Errno 2] No such file or directory: 'src/data/exports/--help/conversations.json'
  - Failed to load src/data/exports/--help/--help_vocabulary.json: [Errno 2] No such file or directory: 'src/data/exports/--help/--help_vocabulary.json'
  - Failed to load src/data/exports/--help/--help_phrases.json: [Errno 2] No such file or directory: 'src/data/exports/--help/--help_phrases.json'
  - Failed to load src/data/exports/--help/--help_sentences.json: [Errno 2] No such file or directory: 'src/data/exports/--help/--help_sentences.json'
Audio Audit: FAIL

Failed to load src/data/exports/--help/conversations.json: [Errno 2] No such file or directory: 'src/data/exports/--help/conversations.json'

--- Distractor Quality Audit: --help ---
  - Failed to load src/data/exports/--help/conversations.json: [Errno 2] No such file or directory: 'src/data/exports/--help/conversations.json'
  - Failed to load src/data/exports/--help/--help_vocabulary.json: [Errno 2] No such file or directory: 'src/data/exports/--help/--help_vocabulary.json'
  - Failed to load src/data/exports/--help/--help_phrases.json: [Errno 2] No such file or directory: 'src/data/exports/--help/--help_phrases.json'
  - Failed to load src/data/exports/--help/--help_sentences.json: [Errno 2] No such file or directory: 'src/data/exports/--help/--help_sentences.json'
Distractor Audit: FAIL

Failed to load src/data/exports/--help/mini_lessons.json: [Errno 2] No such file or directory: 'src/data/exports/--help/mini_lessons.json'

Error loading files: [Errno 2] No such file or directory: 'src/data/exports/--help/conversations.json'

--- Translation Audit: --help ---
  - Failed to load src/data/exports/--help/conversations.json: [Errno 2] No such file or directory: 'src/data/exports/--help/conversations.json'
  - Failed to load src/data/exports/--help/--help_vocabulary.json: [Errno 2] No such file or directory: 'src/data/exports/--help/--help_vocabulary.json'
  - Failed to load src/data/exports/--help/--help_phrases.json: [Errno 2] No such file or directory: 'src/data/exports/--help/--help_phrases.json'
  - Failed to load src/data/exports/--help/--help_sentences.json: [Errno 2] No such file or directory: 'src/data/exports/--help/--help_sentences.json'
Translation Audit: FAIL


--- Keyboard Accessibility Audit (STATIC) ---
Keyboard Audit: PASS


--- DOMAIN CONTAMINATION AUDIT: --help ---
WARN: No domain.json found in src/data/exports/--help. Skipping strict lexical check.
FAIL: Could not load vocabulary json: [Errno 2] No such file or directory: 'src/data/exports/--help/--help_vocabulary.json'


--- PATH CONSISTENCY AUDIT: --help ---
  - Slug '--help' not found in scenarioMapping.ts
PATH CONSISTENCY AUDIT: FAIL


--- RUNTIME LEARNING FLOW AUDIT (STATIC) ---
Host autoplay implemented: YES
User autoplay present: NO
User manual speaker icon present: YES
CONVERSATION FLOW AUDIT: PASS


--- MINI LESSON AUDIO AUDIT: --help ---

Failed to load src/data/exports/--help/conversations.json: [Errno 2] No such file or directory: 'src/data/exports/--help/conversations.json'


```
