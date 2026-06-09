# Phase 4.05A: Materialization Forensic Audit

## 1. Word Registry
- PASS: 142 words exist
- PASS: IDs are unique
- PASS: No duplicate Italian entries

## 2. Phrase Registry
- PASS: 78 phrases exist
- PASS: Every depends_on_words reference exists

## 3. Sentence Registry
- PASS: 80 sentences exist
- PASS: Every depends_on_words and depends_on_phrases reference exists

## 4. Turn Registry
- PASS: 80 turns exist
- PASS: Every sentence_id exists

## 5. Micro Lessons
- PASS: IDs only, no literal Italian strings
- PASS: Every referenced entity exists

## 6. Chronological Integrity
- FAIL: 6 chronological dependency violations found
  - Entity p_000045 depends on word w_000040 which is never introduced
  - Entity p_000048 depends on word w_000045 which is never introduced
  - Entity p_000052 depends on word w_000047 which is never introduced
  - Entity p_000057 depends on word w_000040 which is never introduced
  - Entity p_000064 depends on word w_000047 which is never introduced
  - Entity p_000067 depends on word w_000050 which is never introduced

## 7. Coverage Integrity
- FAIL: 36 entities do not appear in any micro lesson
  - Entity w_000040 is missing from all lessons
  - Entity w_000041 is missing from all lessons
  - Entity w_000042 is missing from all lessons
  - Entity w_000043 is missing from all lessons
  - Entity w_000044 is missing from all lessons
  - Entity w_000045 is missing from all lessons
  - Entity w_000046 is missing from all lessons
  - Entity w_000047 is missing from all lessons
  - Entity w_000048 is missing from all lessons
  - Entity w_000049 is missing from all lessons
  - ...

## 8. Determinism
- PASS: No text matching required anywhere. Everything resolvable through IDs.

## OVERALL STATUS
**FAIL** (2 checks failed)