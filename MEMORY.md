# PARLA ITALIANO MEMORY

## Current Phase

Phase 2

Validation Framework & Certification Pipeline

Status:

IN PROGRESS

---

# Gold Standard Scenario

Scenario:

Apartment Key Pickup

Status:

GOLD STANDARD V1

Certification Status:

Pending continuous refinement

Purpose:

Reference implementation for all future scenarios.

---

# Documentation Status

## Complete

* GOLD_STANDARD.md
* CURRICULUM_RULES.md
* CONVERSATION_RULES.md
* DISTRACTOR_RULES.md
* AUDIO_RULES.md
* DOMAIN_RULES.md
* VALIDATION_RULES.md
* RELEASE_CHECKLIST.md

---

# Audit Framework Status

## Implemented

* curriculum_audit.py
* audio_audit.py
* conversation_audit.py
* distractor_audit.py
* lesson_audit.py
* progression_audit.py
* translation_audit.py
* certify_scenario.py

## Pending Review

* keyboard_audit.py
* runtime_audio_audit.py
* domain_audit.py
* scenario_integrity_audit.py
* gold_standard_audit.py

---

# Audio System

Status:

Stable

Characteristics:

* deterministic hashing
* opus format
* normalized loudness
* asset reuse
* manifest-based lookup
* runtime resolver

---

# Curriculum Architecture

Conversation
→ Vocabulary Extraction
→ Phrase Extraction
→ Sentence Extraction
→ Mini Lessons
→ Certification

This architecture is mandatory.

---

# Scenario Progress

## Completed

1. Apartment Key Pickup
2. Extending Stay (accommodation/extending_stay)
3. Hostel Dorm (accommodation/hostel_dorm)
4. Ordering Pasta (dining/ordering_pasta)
5. Bakery (dining/bakery)
6. Cinema Tickets (culture/cinema_tickets)
7. Culture Festival (culture/festival)
8. Emergency Room (health/emergency_room)
9. Police Report (miscellaneous/police_report)
10. Talking About Money (miscellaneous/talking_about_money)
11. Explaining a Mistake (miscellaneous/explaining_a_mistake)
12. Shoe Store (shopping/shoe_store)
13. Outdoor Market (shopping/outdoor_market)
14. Verbs: -ire (verbs/ire_verbi_in_ire)

Status:

Gold Standard V1 & Certified

---

## Remaining Scenarios

102

Status:

In Progress

---

# Generation Workflow

For every scenario:

1. Domain Analysis
2. Conversation Generation
3. Linguistic Extraction
4. Curriculum Generation
5. Distractor Generation
6. Translation Generation
7. Audio Verification
8. Audit Execution
9. Certification
10. Update MEMORY.md
11. Proceed to next scenario

---

# Success Criteria

Project completion requires:

* 116 certified scenarios
* 100% curriculum coverage
* 100% audio coverage
* deterministic assets only
* no domain contamination
* all certification audits passing

---

# Known Lessons Learned

1. Conversation must be source of truth.
2. Lessons must derive from conversations.
3. Audio must be audited, not assumed.
4. Certification must be automated.
5. Apartment Key Pickup serves as benchmark.
6. Every future scenario must pass certification before acceptance.
