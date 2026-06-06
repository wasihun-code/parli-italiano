import { db } from '../lib/db';

export class GlobalDictionaryResolver {
  private static isInitialized = false;

  /**
   * Initializes the resolver by seeding the mapping cache from JSON if needed.
   */
  private static async ensureInitialized() {
    if (this.isInitialized) return;

    try {
      const count = await db.scenario_vocab_mapping_cache.count();
      if (count === 0) {
        console.log("Seeding scenario vocab mapping cache...");
        const res = await fetch('/scenario_vocab_mapping.json');
        if (res.ok) {
          const data = await res.json();
          const bulkData: any[] = [];
          
          for (const [slug, mappings] of Object.entries(data)) {
            const mapArray = mappings as { local_id: string, global_id: string }[];
            for (const m of mapArray) {
              bulkData.push({
                id: `${slug}-${m.local_id}`, // Stable PK
                scenario_slug: slug,
                local_id: m.local_id,
                global_id: m.global_id
              });
            }
          }
          
          if (bulkData.length > 0) {
            await db.scenario_vocab_mapping_cache.bulkPut(bulkData);
          }
        }
      }
      this.isInitialized = true;
    } catch (e) {
      console.error("Failed to initialize GlobalDictionaryResolver", e);
    }
  }

  static async resolveLocalToGlobal(scenarioId: number, localVocabId: string): Promise<string | null> {
    await this.ensureInitialized();

    try {
      // Find mapping. Since we don't have scenario_slug easily here without another lookup,
      // we search by local_id and verify if multiple exist.
      // Optimization: In Phase 8.1 we should pass the slug directly.
      const mappings = await db.scenario_vocab_mapping_cache
        .where('local_id').equals(localVocabId)
        .toArray();
        
      if (mappings.length === 1) return mappings[0].global_id;
      
      // If multiple scenarios use the same local ID (e.g. v1), we need the scenario context.
      const scenario = await db.scenarios.get(scenarioId);
      if (scenario) {
        // Attempt to match by category/title pattern in scenario_slug
        const slugPart = scenario.title.toLowerCase().replace(/ /g, '_');
        const match = mappings.find(m => m.scenario_slug.includes(slugPart));
        if (match) return match.global_id;
      }
      
      return mappings[0]?.global_id || `word_${localVocabId}`;
    } catch (e) {
      console.error("Resolution failed", e);
      return `word_${localVocabId}`;
    }
  }

  static async loadDictionaryToDexie() {
    try {
      const dictRes = await fetch('/global_dictionary.json');
      if (dictRes.ok) {
        const dictData = await dictRes.json();
        // Ensure every entry has a last_updated field for version tracking
        const timestampedData = dictData.map((d: any) => ({
          ...d,
          last_updated: d.last_updated || new Date().toISOString()
        }));
        await db.global_dictionary.bulkPut(timestampedData);
      }
    } catch (e) {
      console.error("Failed to seed global dictionary", e);
    }
  }
}
