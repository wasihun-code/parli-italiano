# Performance Analysis

Moving to a Global Knowledge Graph and a dynamic FSRS-Lite algorithm introduces new performance considerations for a client-side offline application.

## 1. Database Growth
- **Current:** 116 scenarios * ~250 items = ~29,000 isolated records in Dexie.
- **Future:** ~4,000 Global Dictionary records + ~29,000 mapping records.
- **Impact:** Minimal. The total row count is roughly the same, but the payload size of the global dictionary is smaller due to deduplication of English translations and audio paths.

## 2. Review Queue Size
- **Current:** 0.
- **Future:** Up to ~4,000 SRS items tracked in Zustand's local storage.
- **Impact:** Zustand handles `Record<string, SrsItem>` efficiently up to 10,000 keys. However, serializing and writing a massive JSON object to `localStorage` on every keystroke could cause UI stutter.
- **Mitigation:** Implement debounced persistence in the Zustand `persist` middleware, or move the `srsStore` entirely to Dexie if it exceeds 2MB.

## 3. Dictionary Size & Lookup Cost
- **Impact:** The `corpusLoader.ts` will need to parse a single ~1MB `global_dictionary.json` file on app boot.
- **Mitigation:** This is faster than parsing 116 separate vocabulary files. Lookup cost is `O(1)` since it will be loaded into a Javascript Map.

## 4. Mobile & Offline Performance
- **Impact:** The app remains 100% offline-capable. The FSRS-Lite algorithm is purely mathematical and runs entirely in the browser.
- **Mitigation:** The only risk is the "Implicit Review" dispatch at the end of a conversation, which might need to update 40+ SRS items simultaneously. This should be wrapped in a single batch transaction to prevent frame drops on low-end mobile devices.
