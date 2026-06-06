import { db } from '../lib/db';

export type MasteryState = 'UNKNOWN' | 'LEARNING' | 'LEARNED' | 'ADVANCED' | 'MASTERED' | 'LAPSED' | 'RELEARNING';

export class GlobalProgressService {
  
  static async recordExposure(globalId: string, type: 'vocabulary' | 'phrase' | 'sentence' = 'vocabulary') {
    const existing = await db.global_progress.get(globalId);
    if (!existing) {
      await db.global_progress.put({
        item_id: globalId,
        item_type: type,
        mastery_level: 0,
        correct_streak: 0,
        total_attempts: 0,
        last_reviewed_at: new Date().toISOString(),
        next_review_at: new Date().toISOString(),
      });
    }
  }

  static async recordAnswer(globalId: string, isCorrect: boolean, scenarioId?: number, source: 'VOCABULARY' | 'CONVERSATION' = 'VOCABULARY') {
    await this.recordBatchResults([{ globalId, isCorrect }], scenarioId, source);
  }

  static async recordBatchResults(
    results: { globalId: string, isCorrect: boolean }[], 
    scenarioId?: number, 
    source: 'VOCABULARY' | 'CONVERSATION' = 'VOCABULARY'
  ) {
    const globalIds = results.map(r => r.globalId);
    const now = new Date().toISOString();

    await db.transaction('rw', [db.global_progress, db.global_review_history], async () => {
      const existingProgress = await db.global_progress.bulkGet(globalIds);
      const updates: any[] = [];
      const historyItems: any[] = [];

      for (let i = 0; i < results.length; i++) {
        const { globalId, isCorrect } = results[i];
        let progress = existingProgress[i];

        if (!progress) {
          // Default for new items
          progress = {
            item_id: globalId,
            item_type: 'vocabulary', // Defaulting to vocabulary for implicit reinforcement
            mastery_level: 0,
            correct_streak: 0,
            total_attempts: 0,
            last_reviewed_at: now,
            next_review_at: now,
          };
        }

        progress.total_attempts += 1;
        progress.last_reviewed_at = now;
        progress.last_result = isCorrect;

        if (isCorrect) {
          progress.correct_streak += 1;
          if (progress.correct_streak >= 3) {
            progress.mastery_level = Math.max(progress.mastery_level, 1);
          }
        } else {
          progress.correct_streak = 0;
          progress.mastery_level = Math.max(0, progress.mastery_level - 1);
        }

        updates.push(progress);
        historyItems.push({
          item_id: globalId,
          timestamp: now,
          result: isCorrect,
          scenario_id: scenarioId,
          source: source
        });
      }

      await Promise.all([
        db.global_progress.bulkPut(updates),
        db.global_review_history.bulkAdd(historyItems)
      ]);
    });
  }

  static async getMasteryState(globalId: string): Promise<MasteryState> {
    const progress = await db.global_progress.get(globalId);
    if (!progress) return 'UNKNOWN';
    if (progress.mastery_level >= 4) return 'MASTERED';
    if (progress.mastery_level === 3) return 'ADVANCED';
    if (progress.mastery_level >= 1) return 'LEARNED';
    if (progress.correct_streak === 0 && progress.total_attempts > 0) return 'LAPSED';
    return 'LEARNING';
  }
}
