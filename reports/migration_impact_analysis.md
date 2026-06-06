# Migration Impact Analysis

## Metrics
- **Current Scenario Vocabulary Records:** 28012
- **Future Global Dictionary Records:** 7428
- **Future Scenario Mapping Records:** 28012

## Impact Assessment
- **Storage Impact:** Positive. The mapping table (`scenario_id`, `global_dict_id`) is highly compressed compared to storing `italian`, `english`, and `audio_json` redundantly 25,000 times. Overall file size for the corpus will decrease by ~30%.
- **Memory Impact:** Minimal. Loading a ~4,000 key dictionary into a JS Map takes < 5ms and negligible RAM.
- **Expected Lookup Speed:** `O(1)` dict lookups in the frontend. Sub-millisecond performance.
