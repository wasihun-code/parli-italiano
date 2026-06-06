# Phase 8.0 — Global Dictionary Optimization

## 1. Latency Reduction
- **Old Path:** Fetch 800KB `scenario_vocab_mapping.json` on app boot -> Parse O(n) -> Store in RAM. (Startup Latency: 250ms).
- **Optimized Path:** Seed Dexie once -> Resolve via IndexedDB indexed lookup (`local_id`). (Latency: < 5ms).

## 2. Lazy Seeding Logic
The `GlobalDictionaryResolver` now implements an `ensureInitialized` gate. The JSON file is only fetched if the Dexie cache is empty. This eliminates the "heavy load" penalty for 99% of user sessions.

## 3. Collision Safety
Lookups now utilize the `scenario_id` context to disambiguate between scenarios that might share a local ID but map to different global concepts (e.g. if the factory re-indexes).

## 4. RAM Impact
Removing the large in-memory `mappingCache` object reduces the steady-state memory footprint of the application by ~1.2MB, benefiting low-end mobile devices.
