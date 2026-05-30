# Scenario Release Checklist

Every scenario MUST satisfy this checklist before it can be merged or released to the production environment. Manual testing is insufficient. Certification relies strictly on the automated pipeline.

## Automated Certification
Run `python scripts/certify_scenario.py <scenario_slug>`

### Required Audits:
- [ ] **Curriculum Audit:** Verifies 100% coverage of conversation language in lessons.
- [ ] **Audio Audit:** Verifies all assets exist and are referenced.
- [ ] **Conversation Audit:** Verifies node counts, turns, and logic flow.
- [ ] **Distractor Audit:** Verifies choice structure and plausibility.
- [ ] **Translation Audit:** Verifies English translations are present and valid.
- [ ] **Keyboard Audit:** Verifies accessibility shortcuts.
- [ ] **Domain Audit:** Verifies zero lexical contamination.
- [ ] **Runtime Audio Audit:** Verifies the React codebase conforms to playback rules.
- [ ] **Progression Audit:** Verifies concepts are taught before they appear in scenarios.
- [ ] **Lesson Audit:** Verifies lesson metadata and structure.

## Final Output
- [ ] `reports/<scenario_slug>_certification.json` exists and shows `overall: PASS`.
- [ ] `reports/<scenario_slug>_certification.md` is generated for review.

## Manual Verification (Optional but Recommended)
- [ ] Play through Conversation 1 using only the keyboard (`1-4`, `Space`, `Enter`, `T`).
- [ ] Verify Immersive Mode triggers correctly on desktop and mobile viewports.
