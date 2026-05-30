# PARLA ITALIANO — MASTER OPERATING SYSTEM

## Mission

Build the highest quality Italian immersion curriculum possible.

The project contains:

* 116 real-world scenarios
* Mini lessons
* Scripted conversations
* Deterministic audio
* Certification pipeline
* Gold Standard validation framework

The system must prioritize:

1. Pedagogical quality
2. Curriculum progression
3. Audio integrity
4. Conversation realism
5. Auditability
6. Deterministic generation

Speed is irrelevant.

Quality is mandatory.

---

# GOLD STANDARD AUTHORITY

Apartment Key Pickup is:

GOLD STANDARD SCENARIO V1

It is the reference implementation.

Every future scenario must be compared against it.

Before generating any scenario:

Study:

docs/GOLD_STANDARD.md
docs/CURRICULUM_RULES.md
docs/CONVERSATION_RULES.md
docs/DISTRACTOR_RULES.md
docs/AUDIO_RULES.md
docs/DOMAIN_RULES.md
docs/VALIDATION_RULES.md
docs/RELEASE_CHECKLIST.md

These documents are authoritative.

Never violate them.

---

# MANDATORY SUB-AGENT ARCHITECTURE

Never generate a scenario using a single agent.

Always create specialized agents.

Minimum required agents:

## Agent 1 — Domain Expert

Responsibility:

* Understand the real-world situation
* Identify required vocabulary
* Identify required interactions
* Identify common problems
* Identify realistic learner goals

Output:

domain_analysis.json

---

## Agent 2 — Conversation Architect

Responsibility:

Create:

conversations.json

Requirements:

* Follow CONVERSATION_RULES.md
* Minimum 4 conversations
* Minimum 10 turns each
* A1–A2 only
* Short sentences
* Realistic situations
* Multiple paths

Conversation is the source of truth.

---

## Agent 3 — Linguistic Extractor

Responsibility:

Extract:

* vocabulary
* phrases
* sentences

ONLY from conversations.

Create:

vocabulary.json
phrases.json
sentences.json

No manual additions.

---

## Agent 4 — Curriculum Designer

Responsibility:

Create mini lessons.

Requirements:

* Goal-oriented titles
* Progressive progression
* 2–3 minute duration
* Conversation vocabulary taught first

Output:

mini_lessons.json

---

## Agent 5 — Distractor Engineer

Responsibility:

Generate distractors.

Requirements:

* Follow DISTRACTOR_RULES.md
* Similar length
* Same domain
* Same grammatical category
* No placeholders

---

## Agent 6 — Translation Specialist

Responsibility:

Generate English translations.

Requirements:

* Natural English
* No placeholders
* No machine-style wording

---

## Agent 7 — Audio Specialist

Responsibility:

Verify:

* Existing audio assets
* Manifest reuse
* No duplicate generation

Generate audio only when necessary.

Never regenerate existing audio.

---

## Agent 8 — Curriculum Auditor

Run:

scripts/curriculum_audit.py

Must pass.

---

## Agent 9 — Audio Auditor

Run:

scripts/audio_audit.py

Must pass.

---

## Agent 10 — Conversation Auditor

Run:

scripts/conversation_audit.py

Must pass.

---

## Agent 11 — Distractor Auditor

Run:

scripts/distractor_audit.py

Must pass.

---

## Agent 12 — Progression Auditor

Run:

scripts/progression_audit.py

Must pass.

---

## Agent 13 — Translation Auditor

Run:

scripts/translation_audit.py

Must pass.

---

## Agent 14 — Domain Auditor

Run:

scripts/domain_audit.py

Must pass.

---

## Agent 15 — Certification Agent

Run:

scripts/certify_scenario.py

Scenario is not complete until certification passes.

---

# CERTIFICATION RULE

A scenario is complete ONLY IF:

scripts/certify_scenario.py

returns:

OVERALL PASS

Any failure means:

Scenario is NOT complete.

Repair it.

Re-audit it.

Re-certify it.

Repeat until PASS.

---

# AUDIO POLICY

Never generate duplicate audio.

Before generating audio:

1. Check manifest.
2. Check existing assets.
3. Check deterministic hash.
4. Reuse asset if present.

Generate only missing assets.

---

# CURRICULUM POLICY

Conversation drives curriculum.

Never:

Lessons → Conversation

Always:

Conversation
→ Extraction
→ Lessons
→ Audit
→ Certification

---

# QUALITY POLICY

Reject:

* placeholder distractors
* weak distractors
* long A2+ sentences
* domain contamination
* untranslated content
* missing audio
* broken progression

---

# SCENARIO COMPLETION POLICY

After certification:

Update MEMORY.md.

Then continue automatically to the next scenario.

Never stop after completing a scenario.

Continue until all scenarios are certified.

---

# FAILURE POLICY

If certification fails:

Do not claim success.

Identify:

* failing audit
* root cause
* repair strategy

Apply repair.

Run certification again.

Only report completion after PASS.

---

# OUTPUT REQUIREMENT

For every completed scenario provide:

1. Audit summary
2. Certification summary
3. Coverage report
4. Audio report
5. Curriculum report
6. Remaining issues

Never provide marketing-style success messages.

Provide measurable results only.
