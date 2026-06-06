import { db } from '../lib/db';

export class GlobalDictionaryResolver {
  
  static async resolveLocalToGlobal(scenarioId: number, localVocabId: string): Promise<string | null> {
    // Attempt to find in the V2 mapping cache
    const mapping = await db.scenario_vocab_mapping_cache
      .where({ scenario_id: scenarioId })
      .toArray();
      
    // Because mapping doesn't natively store local_id in V2 cache yet, 
    // we use a static fallback resolving method or fetch it from the JSON.
    // In Phase 7.3, we rely on the `generated/scenario_vocab_mapping.json` for exact matches.
    try {
      const res = await fetch('/scenario_vocab_mapping.json');
      if (!res.ok) return null;
      const data = await res.json();
      
      // We need the slug from the scenarioId.
      const scenario = await db.scenarios.get(scenarioId);
      if (!scenario) return null;
      
      // Fallback rough path lookup since scenarios table stores id, title, category
      // In a real implementation we would map scenarioId -> slug correctly.
      // For now, we simulate resolution.
      return `word_${localVocabId}`; // Placeholder for strict resolution
    } catch (e) {
      console.warn("Global resolution failed", e);
      return null;
    }
  }

  static async loadDictionaryToDexie() {
    // Seeds the Dexie tables from the generated JSONs
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
