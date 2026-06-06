import { GlobalProgressService, MasteryState } from './globalProgressService';
import { GlobalDictionaryResolver } from './globalDictionaryResolver';

export interface AdaptationResult {
  visibleIds: string[];
  skippedIds: string[];
  stats: {
    total: number;
    new: number;
    learning: number;
    mastered: number;
    skipped: number;
  };
}

export class CurriculumAdaptationService {
  /**
   * Filters a list of local vocabulary IDs based on their global mastery state.
   * Ensures a 'Safety Floor' so lessons are never completely empty.
   */
  static async adaptVocabularyLesson(scenarioId: number, localVocabIds: string[]): Promise<AdaptationResult> {
    const visibleIds: string[] = [];
    const skippedIds: string[] = [];
    const stats = { total: localVocabIds.length, new: 0, learning: 0, mastered: 0, skipped: 0 };

    // Resolve and classify each ID
    const classifiedItems = await Promise.all(localVocabIds.map(async (localId) => {
      const globalId = await GlobalDictionaryResolver.resolveLocalToGlobal(scenarioId, localId);
      const state = globalId ? await GlobalProgressService.getMasteryState(globalId) : 'UNKNOWN';
      return { localId, globalId, state };
    }));

    for (const item of classifiedItems) {
      if (['LEARNED', 'ADVANCED', 'MASTERED'].includes(item.state)) {
        skippedIds.push(item.localId);
        stats.mastered++;
        stats.skipped++;
      } else {
        visibleIds.push(item.localId);
        if (item.state === 'UNKNOWN') stats.new++;
        else stats.learning++;
      }
    }

    // Safety Floor Enforcement (Min 2 items)
    while (visibleIds.length < 2 && skippedIds.length > 0) {
      // Pop an item from skipped back into visible to act as a contextual refresh
      const refreshId = skippedIds.pop();
      if (refreshId) {
        visibleIds.push(refreshId);
        stats.skipped--;
      }
    }

    return { visibleIds, skippedIds, stats };
  }
}
