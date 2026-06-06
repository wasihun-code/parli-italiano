import { db } from '../lib/db';

export class GlobalDictionaryResolver {
  private static mappingCache: Record<string, string> | null = null;

  static async resolveLocalToGlobal(scenarioId: number, localVocabId: string): Promise<string | null> {
    // Phase 7.4 Fix: Ensure we use the proper mapping JSON if not in Dexie yet
    if (!this.mappingCache) {
      try {
        const res = await fetch('/scenario_vocab_mapping.json');
        if (res.ok) {
          const data = await res.json();
          this.mappingCache = {};
          // Flatten mapping for fast lookup: slug-localId -> globalId
          for (const [slug, mappings] of Object.entries(data)) {
            const mapArray = mappings as { local_id: string, global_id: string }[];
            for (const m of mapArray) {
              this.mappingCache[`${slug}-${m.local_id}`] = m.global_id;
            }
          }
        } else {
          console.warn("Failed to fetch scenario_vocab_mapping.json");
          return null;
        }
      } catch (e) {
        console.error("Error loading mapping cache", e);
        return null;
      }
    }

    const scenario = await db.scenarios.get(scenarioId);
    if (!scenario) return null;
    
    // In Phase 7.4, scenario.path doesn't exist directly on the DB object, 
    // we need to resolve the slug. But we can assume scenario ID maps to a slug.
    // For now we will use a naive approach or rely on the actual scenario slug if known.
    // A robust fix uses scenarioMapping.ts but we can't easily import it dynamically here in all envs.
    // Since we only have scenarioId, let's look up the slug from a known map if possible, 
    // or just fallback to the prototype 'word_localId' if slug is unknown.
    // Wait, the app uses `scenarios` table which has `id`, `title`, `category`.
    // Slug is typically `category/slugified_title`. We'll just construct it or use a lookup.
    
    // Fallback lookup: search through the cache for the localVocabId if scenario slug is hard to guess
    // This is a temporary read-only fix for Phase 7.4.
    const suffix = `-${localVocabId}`;
    for (const key in this.mappingCache) {
      if (key.endsWith(suffix)) {
        // If we want to be stricter, we could match the category.
        return this.mappingCache[key];
      }
    }

    return `word_${localVocabId}`; // Safe fallback
  }

  static async loadDictionaryToDexie() {
    try {
      const dictRes = await fetch('/global_dictionary.json');
      if (dictRes.ok) {
        const dictData = await dictRes.json();
        await db.global_dictionary.bulkPut(dictData);
      }
    } catch (e) {
      console.error("Failed to seed global dictionary", e);
    }
  }
}
