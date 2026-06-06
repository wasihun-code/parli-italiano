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
    let progress = await db.global_progress.get(globalId);

    if (!progress) {
      await this.recordExposure(globalId);
      progress = await db.global_progress.get(globalId);
      if (!progress) return;
    }

    const now = new Date().toISOString();

    // FSRS-Lite inspired state transitions for Phase 7.3
    progress.total_attempts += 1;
    progress.last_reviewed_at = now;
    progress.last_result = isCorrect;

    if (isCorrect) {
      progress.correct_streak += 1;
      // Basic mock mastery level update (Full SRS scheduled for Phase 7.5/7.8)
      if (progress.correct_streak >= 3) progress.mastery_level = Math.max(progress.mastery_level, 1);
    } else {
      progress.correct_streak = 0;
      // Soft lapse
      progress.mastery_level = Math.max(0, progress.mastery_level - 1);
    }

    await db.global_progress.put(progress);

    // Record History
    await db.global_review_history.add({
      item_id: globalId,
      timestamp: now,
      result: isCorrect,
      scenario_id: scenarioId,
      source: source
    } as any); // Type cast until db.ts interface is updated
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
