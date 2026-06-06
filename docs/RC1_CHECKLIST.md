# RC1 Release Candidate Checklist

This document tracks the final production readiness gate for Parla Italiano.

## 1. Installation & Environment
- [ ] `npm install` clean on fresh machine.
- [ ] `.env.example` matches production requirements.
- [ ] No hardcoded local paths in `src/`.

## 2. Build & Deployment
- [ ] `npm run build` succeeds without warnings.
- [ ] Bundle size optimized (< 15MB total).
- [ ] Service worker (PWA) operational.

## 3. Database (IndexedDB V2)
- [ ] `SEED_VERSION` set to current production.
- [ ] Migration from V1 streaks to V2 mastery verified.
- [ ] No data loss on app refresh.

## 4. Audio Architecture
- [ ] `audio_manifest.json` matches on-disk assets.
- [ ] Deterministic hash fallback functional.
- [ ] No broken audio links in core scenarios.

## 5. Hybrid Mastery V2
- [ ] Global Dictionary generated (5,297 entities).
- [ ] Curriculum adaptation (Magic Skip) functional.
- [ ] Conversation reinforcement (20-word cap) operational.
- [ ] Daily Review Queue priority sorting verified.

## 6. Admin Panel
- [ ] All 9 operational routes load.
- [ ] Certification dashboard shows 100% pass rate.
- [ ] Mastered vocabulary metrics accurate.

## 7. QA & Certification
- [ ] All 116 scenarios pass `certify_all.py`.
- [ ] Playwright E2E suite green.
- [ ] Performance lookups < 10ms.

## 8. Monitoring
- [ ] Sentry (or equivalent) configured.
- [ ] Analytic events for "Scenario Complete" functional.
