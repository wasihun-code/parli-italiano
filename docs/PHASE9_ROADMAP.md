# Phase 9: Learning System V3 Roadmap

This document outlines the phased implementation strategy for Learning System V3.

## Phase 9.0A - Governance & Verification Framework
Establish the rules, documentation, and audit stubs. (COMPLETE)

## Phase 9.0B - Learning Path Specification Hardening
Mathematically define the pure-function generator and the cognitive progression curve. (COMPLETE)

## Phase 9.1 - Architecture & Data Structures
Design the runtime interfaces, the Learning Path Generator classes, and the Zustand store updates required to support dynamic sequences without modifying IndexedDB schemas.

## Phase 9.2 - Learning Path Specification
Canonicalize the exercise-to-mastery mapping and transition state machine.

## Phase 9.3 - Learning Path Generator
Implement the core V3 Engine: the algorithm that reads the legacy `mini_lessons.json` and dynamically re-sorts and injects exercises based on Global Progress and the `Recognition -> Recall -> Production` rules.

## Phase 9.4 - Exercise Registry
Implement the distinct React components for each of the 11 identified exercise types (Listen, Match, Dictation, etc.), ensuring they adhere strictly to the Input/Output definitions defined by the Generator.

## Phase 9.5 - Audit Layer Implementation
Flesh out the Python audit stubs created in 9.0A into fully functional verification scripts that can simulate the V3 runtime and mathematically prove compliance.

## Phase 9.6 - Pilot Scenario (Apartment Key Pickup)
Enable V3 exclusively for Scenario 22 (`apartment_key_pickup`). Run extensive manual QA and automated audits to verify the new progression curve and semantic grouping.

## Phase 9.7 - Multi-Scenario Rollout
Expand V3 to 10 diverse scenarios spanning different complexities and categories. Monitor for edge cases and ID collisions.

## Phase 9.8 - Full Global Rollout
Enable Learning System V3 for all 116 scenarios. Finalize RC2.

---

### Justification for Roadmap Correction
The **Learning Path Generator** (9.3) is now scheduled before the **Exercise Registry** (9.4). This ensures that the logical data contract is established first. UI components (Registry) will be built to consume the specific data structures emitted by the Generator, preventing "UI-driven architecture" where logical constraints are compromised for visual convenience.
