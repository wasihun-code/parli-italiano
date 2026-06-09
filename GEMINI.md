# PARLA ITALIANO — MASTER OPERATING SYSTEM

## 1. Project Overview

Parla Italiano is a comprehensive, offline-capable, gamified web application for learning Italian through real-world conversational scenarios.

The platform teaches learners through:

* Scenario-based conversations
* Structured curriculum progression
* Deterministic audio
* Knowledge dependency tracking
* Conversation mastery
* Review scheduling
* Verification-driven curriculum generation

The ultimate objective is conversation readiness and scenario mastery rather than isolated vocabulary memorization.

---

## 2. Current Project Status

### Scenario Factory

Status: COMPLETE

* 116/116 scenarios generated
* Gold Standard curriculum archived
* Factory V2 operational
* Translation pipeline operational
* Deterministic audio generation operational

### Curriculum Architecture

Status: APPROVED

Curriculum V4 is now the authoritative curriculum architecture.

Authoritative source:

docs/curriculum-v4/CURRICULUM_V4_SOURCE_OF_TRUTH.md

All curriculum work must follow the approved Curriculum V4 specifications.

---

## 3. Current Phase

Phase 4.1 — Verification Engine Implementation

Objective:

Implement deterministic verification scripts based on the approved Curriculum V4 architecture.

---

## 4. Mandatory Development Workflow

Every task must follow this sequence:

1. Analyze
2. Plan
3. Verify assumptions
4. Implement
5. Validate
6. Audit
7. Update MEMORY.md

No phase may skip verification.

---

## 5. Curriculum V4 Authority

The following documents are authoritative and approved:

docs/curriculum-v4/

* 01_knowledge_graph.md
* 02_dependency_graph.md
* 03_micro_lesson_structure.md
* 04_learning_flow.md
* 05_state_machine.md
* 06_verification_architecture.md
* 07_data_schema.md
* CURRICULUM_V4_SOURCE_OF_TRUTH.md

These documents define:

* Knowledge Graph
* Dependency Graph
* Micro Lessons
* Learning Flow
* State Machine
* Verification Architecture
* Canonical Data Schema

These documents are specifications.

Implementations must follow them.

Implementations must not redesign them.

---

## 6. Curriculum V4 Core Principles

### Conversation First

Conversations are the source of truth.

All curriculum content exists to prepare learners for successful conversation participation.

### Dependency Driven Learning

Learning progression follows:

Word
→ Phrase
→ Sentence
→ Conversation Turn

Forward references are prohibited.

### Single Introduction Rule

Every entity may be introduced exactly once.

After introduction:

* Practice is allowed
* Review is allowed

Re-introduction is prohibited.

### Conversation Readiness

A conversation turn may only be introduced when all required dependencies have been satisfied.

### Verification Before Generation

Curriculum generation is never trusted.

Verification is mandatory.

Generation without certification is prohibited.

---

## 7. Canonical Entity Types

Curriculum V4 defines:

* Word
* Phrase
* Sentence
* Conversation Turn
* Micro Lesson

All entities must conform to:

docs/curriculum-v4/07_data_schema.md

---

## 8. State Machine

Approved learner states:

* UNSEEN
* INTRODUCED
* PRACTICED
* MASTERED
* FORGOTTEN

Review scheduling operates independently.

State transitions must follow:

docs/curriculum-v4/05_state_machine.md

---

## 9. Verification Requirements

The following audits are mandatory:

A01 Dependency Audit

A02 Coverage Audit

A03 Duplicate Introduction Audit

A04 Lesson Flow Audit

A05 State Machine Audit

A06 Conversation Readiness Audit

A07 Exercise Eligibility Audit

No curriculum may pass certification if any audit fails.

---

## 10. Implementation Rules

When implementing curriculum systems:

* Read Curriculum V4 specifications first
* Implement exactly what is specified
* Do not redesign architecture
* Do not simplify architecture
* Do not bypass verification rules
* Do not invent alternative schemas

If implementation conflicts with existing code:

1. Report conflict
2. Explain impact
3. Propose options
4. Await approval

---

## 11. Forbidden Actions

DO NOT:

* Redesign Curriculum V4
* Introduce parallel curriculum architectures
* Bypass dependency validation
* Bypass certification
* Modify approved specifications without authorization
* Hardcode curriculum progress
* Circumvent verification audits
* Implement undocumented schema variants

---

## 12. Current Priorities

Priority 1

Phase 4.1
Verification Engine

Priority 2

Phase 5
Exercise Blueprint Architecture

Priority 3

Phase 6
Exercise Generation Framework

Priority 4

Phase 7
Runtime Integration

---

## 13. Memory Update Requirement

MEMORY.md is the live operational state.

After every completed phase:

* Update implementation status
* Update audit status
* Update verification status
* Update roadmap status

MEMORY.md must reflect actual project state.

Never future plans.

Never assumptions.
