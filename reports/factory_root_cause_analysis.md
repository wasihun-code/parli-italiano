# Factory Root Cause Analysis

## Executive Summary
The Gold Standard factory successfully certified numerous scenarios that contained critical curriculum coverage gaps. A forensic investigation of the generation pipeline reveals that the root cause is a combination of a **unidirectional audit loophole** and a **broken dependency chain** during the conversation expansion phase.

## Pipeline Analysis

1. **Conversation Generation (Agent 2)**: Produces `conversations.json`. Often initially defaults to 5-6 turns due to context limits.
2. **Linguistic Extraction (Agent 3)**: `linguistic_extractor.py` parses `conversations.json` and outputs `vocabulary.json`, `phrases.json`, and `sentences.json`.
3. **Curriculum Generation (Agent 4)**: The LLM creates `mini_lessons.json` mapping the extracted IDs into 6 lessons.
4. **Distractor Generation (Agent 5)**: `distractor_generator.py` adds multiple-choice options.
5. **Translation Generation (Agent 6)**: The LLM fills missing English fields.
6. **Validation & Certification**: `build_and_certify_scenario.py` runs extraction, distractors, and then invokes all audits in `certify_scenario.py`.

### The Broken Dependency Chain
When a scenario fails the `Conversation Logic Audit` (e.g., has only 5 turns instead of 10), Agent 2 is invoked to expand the conversations. 
When `build_and_certify_scenario.py` is subsequently run, it automatically reruns `linguistic_extractor.py`, identifying new vocabulary and phrases.
However, **it does not automatically regenerate `mini_lessons.json`**. The old curriculum file remains statically mapped to the original 5-turn extraction.

### The Audit Loophole (Why it Certified)
The factory's audit scripts contain a massive blind spot:
- **`curriculum_audit.py`**: Verifies that the linguistic files are derived from the conversations (`extracted_words ⊆ conversation_words`).
- **`scenario_integrity_audit.py`**: Verifies that every ID listed in `mini_lessons.json` exists in the linguistic files (`taught_ids ⊆ valid_extracted_ids`).
- **CRITICAL MISSING CHECK**: **No script verifies that every extracted ID is taught in a lesson (`valid_extracted_ids ⊆ taught_ids`).**

Because the coverage check is unidirectional, a `mini_lessons.json` file that teaches only 10% of the extracted vocabulary will perfectly pass `scenario_integrity_audit.py` (since those 10% of IDs are valid). 

## Specific Scenario Investigations

* **Why `haircut` and `are_verbi_in_are` stop coverage at the midpoint:**
  These scenarios were initially generated with 5 turns. Agent 4 mapped items 1-20 to lessons. Later, Agent 2 expanded the conversations to 10 turns, and the extractor found items 21-40. Because `mini_lessons.json` was never regenerated, items 21-40 were completely orphaned. The audits passed because items 1-20 were still valid IDs.

* **Why `social/inviting_a_friend` teaches only 46 IDs out of >350:**
  During the Curriculum Generation phase (Agent 4), the LLM reached a token limit or simply hallucinated a truncated list of IDs, ignoring 80% of the extracted data. The unidirectional `scenario_integrity_audit.py` did not flag the omission.

* **Why `taxi_from_airport` is missing only one sentence:**
  A minor LLM omission/hallucination. When Agent 4 manually typed out `["s1", "s2", ... "s40"]`, it accidentally skipped `s12`.

## Required Architectural Fixes

1. **Close the Audit Loophole:** 
   Update `scripts/scenario_integrity_audit.py` (or `curriculum_audit.py`) to explicitly check for untaught IDs. If `len(extracted_ids - taught_ids) > 0`, the audit MUST fail.
2. **Automate Curriculum Generation:** 
   Relying on an LLM to accurately transcribe hundreds of IDs into a JSON array is inherently brittle. The project must introduce a deterministic Python script (`scripts/curriculum_designer.py`) that programmatically chunks the *latest* extracted IDs into the 6 lessons, entirely replacing Agent 4's manual JSON drafting.
3. **Pipeline Integration:**
   `build_and_certify_scenario.py` must be updated to automatically invoke the programmatic curriculum designer immediately after `linguistic_extractor.py`, ensuring the lessons always reflect 100% of the extracted state.

## Impact Assessment
- **Defective Stage:** Certification Audits & Curriculum Generation.
- **Responsible Scripts:** `scenario_integrity_audit.py` (lax rules) and `build_and_certify_scenario.py` (missing curriculum generation step).
- **Estimated Affected Scenarios:** High. Any scenario that underwent conversation expansion *after* initial lesson generation, or where Agent 4 truncated its response, will contain orphaned items. Based on forensic sampling, **40% to 60%** of the 116 "certified" scenarios likely suffer from coverage gaps.
- **Regeneration Required:** Yes. `mini_lessons.json` must be deterministically regenerated for all 116 scenarios once the architectural fixes are applied.
