# Failure Report: daily_life/household_repair

**Timestamp:** 2026-06-04 15:45:07

## Audit Output
```text

=============================================
CERTIFICATION PIPELINE: daily_life/household_repair
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
Audio Integrity                FAIL
Conversation Logic             PASS
Distractor Quality             PASS
Lesson Integrity               PASS
Progression Validation         FAIL
Translation Completeness       FAIL
Keyboard & UI                  PASS
Domain Consistency             PASS
Path Consistency               PASS
Runtime Audio Flow             PASS
Mini Lesson Audio Flow         FAIL
Scenario Integrity             FAIL

OVERALL STATUS: FAIL
=============================================

Reports generated: reports/daily_life_household_repair_certification.json, reports/daily_life_household_repair_certification.md

```

## Analysis
- **Failure Type:** Structural / Logic Error
- **Suggested Fix:** Check the specific audit log above for details.
