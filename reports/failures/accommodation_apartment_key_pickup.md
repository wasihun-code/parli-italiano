# Failure Report: accommodation/apartment_key_pickup

**Timestamp:** 2026-06-04 14:56:51

## Audit Output
```text

=============================================
CERTIFICATION PIPELINE: accommodation/apartment_key_pickup
=============================================

Running Curriculum Coverage (curriculum_audit.py)...
Running Audio Integrity (audio_audit.py)...
Running Conversation Logic (conversation_audit.py)...
Running Distractor Quality (distractor_audit.py)...
Running Lesson Integrity (lesson_audit.py)...
Running Progression Validation (progression_audit.py)...
Running Translation Completeness (translation_audit.py)...
Running Keyboard & UI (keyboard_audit.py)...
Running Domain Consistency (domain_audit.py)...
Running Path Consistency (path_consistency_audit.py)...
Running Runtime Audio Flow (runtime_learning_flow_audit.py)...
Running Mini Lesson Audio Flow (mini_lesson_audio_audit.py)...
Running Scenario Integrity (scenario_integrity_audit.py)...

=============================================
CERTIFICATION RESULTS
=============================================

Curriculum Coverage            FAIL
Audio Integrity                PASS
Conversation Logic             FAIL
Distractor Quality             FAIL
Lesson Integrity               PASS
Progression Validation         FAIL
Translation Completeness       PASS
Keyboard & UI                  PASS
Domain Consistency             PASS
Path Consistency               PASS
Runtime Audio Flow             PASS
Mini Lesson Audio Flow         PASS
Scenario Integrity             PASS

OVERALL STATUS: FAIL
=============================================

Reports generated: reports/accommodation_apartment_key_pickup_certification.json, reports/accommodation_apartment_key_pickup_certification.md

```

## Analysis
- **Failure Type:** Structural / Logic Error
- **Suggested Fix:** Check the specific audit log above for details.
