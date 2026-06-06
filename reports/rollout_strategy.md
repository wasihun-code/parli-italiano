# Rollout Strategy

Migrating to Hybrid Mastery V2 involves deep structural changes to both the curriculum data and the client-side progress tracking.

## Option A: Big Bang Migration
- **Description:** Deploy the new factory data and the new React frontend simultaneously. All users are forced through the `migrate_to_v2.ts` script on their next login.
- **Pros:** Cleanest codebase. No need to maintain two separate curriculum loaders.
- **Cons:** Highest risk. If the migration script fails, all users lose progress simultaneously with no way back.

## Option B: Feature Flag (Recommended)
- **Description:** The new `global_dictionary` and `srsStore_v2` are deployed alongside the old systems. A feature flag enables the new UI components and SRS math for a small subset of beta users.
- **Pros:** Safest approach. Allows monitoring of the FSRS-Lite algorithm parameters on real data without risking the entire user base.
- **Cons:** Technical debt. The app must ship with both the V1 and V2 stores and UI logic for several weeks.

## Option C: Parallel Systems (Beta App)
- **Description:** Launch a separate "Parla Italiano V2" web app pointing to the new data.
- **Pros:** Zero risk to current users.
- **Cons:** Fractures the user base. Requires users to actively choose to migrate.

## Recommendation & Rollback Strategy
**Recommendation: Option B (Feature Flag)** is the most professional approach for an application with active users.

**Rollback Strategy:**
If the feature flag is enabled and critical bugs are detected (e.g., users stuck on a broken review screen):
1. The feature flag is flipped to `false` remotely.
2. The UI falls back to reading the `srsStore_v1` (which was preserved during the migration).
3. The user continues learning using Scenario Mastery while the engineering team diagnoses the issue.
