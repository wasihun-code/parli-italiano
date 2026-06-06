import { db } from './db';
import { useSrsStore } from '../store/srsStore';
import { GlobalProgressService } from '../services/globalProgressService';

export async function migrateToV2() {
  console.log('Starting migration to Hybrid Mastery V2...');
  
  try {
    const res = await fetch('/scenario_vocab_mapping.json');
    if (!res.ok) {
      console.warn('Mapping file not found. Migration aborted.');
      return;
    }
    const mappings = await res.json(); // { "travel/airport": [ {local_id, global_id} ] }
    
    // Reverse map to quickly lookup global_id by local key
    // In V1, items are stored as `s[scenarioId]-v[localId]`
    // E.g. "s22-v1". But we need to know the slug to lookup the mapping.
    // For now, we will do a best effort resolution or use a flat map.
    
    // This is a prototype migration function for Phase 7.3.
    // In a real environment, we'd have a legacy_to_global_map.json provided by the factory
    // mapping "s22-v1" directly to "word_grazie".
    
    const legacyToGlobalMapRes = await fetch('/legacy_to_global_map.json').catch(() => null);
    const legacyMap = legacyToGlobalMapRes && legacyToGlobalMapRes.ok ? await legacyToGlobalMapRes.json() : {};

    const store = useSrsStore.getState();
    const items = Object.values(store.items);
    
    const maxStreaks: Record<string, number> = {};
    const maxAttempts: Record<string, number> = {};
    
    for (const item of items) {
      if (item.type !== 'vocabulary') continue;
      
      // Determine global ID. Fallback for Phase 7.3 if map is missing
      const globalId = legacyMap[item.id] || `word_${item.italian.toLowerCase().replace(/[^a-z0-9àèìòùé']/g, '').replace(/ /g, '_')}`;
      
      if (!maxStreaks[globalId] || item.correctStreak > maxStreaks[globalId]) {
        maxStreaks[globalId] = item.correctStreak;
      }
      
      if (!maxAttempts[globalId]) maxAttempts[globalId] = 0;
      maxAttempts[globalId] += item.attempts;
    }
    
    for (const [globalId, maxStreak] of Object.entries(maxStreaks)) {
      const existing = await db.global_progress.get(globalId);
      if (!existing) {
        await db.global_progress.put({
          item_id: globalId,
          item_type: 'vocabulary',
          mastery_level: maxStreak >= 3 ? 1 : 0,
          correct_streak: maxStreak,
          total_attempts: maxAttempts[globalId],
          last_reviewed_at: new Date().toISOString(),
          next_review_at: new Date(Date.now() + 86400000).toISOString(),
          last_result: maxStreak > 0
        });
      }
    }
    
    console.log('Migration to V2 successful.');
  } catch (err) {
    console.error('Migration failed:', err);
  }
}
