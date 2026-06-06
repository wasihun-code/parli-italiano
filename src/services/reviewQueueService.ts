import { db } from '../lib/db';
import { GlobalProgressService, MasteryState } from './globalProgressService';

export interface ReviewItem {
  globalId: string;
  italian: string;
  english: string;
  audio?: string;
  state: MasteryState;
  type: 'vocabulary' | 'phrase' | 'sentence';
}

export class ReviewQueueService {
  /**
   * Fetches and prioritizes the Daily Review Queue, capped at 100 items.
   */
  static async getDailyQueue(): Promise<ReviewItem[]> {
    const now = new Date().toISOString();
    
    // 1. Fetch Due and Lapsed Items efficiently
    // Due items: Use index on next_review_at
    const dueItems = await db.global_progress
      .where('next_review_at')
      .belowOrEqual(now)
      .toArray();

    // Lapsed items: Use index on correct_streak
    const lapsedItems = await db.global_progress
      .where('correct_streak')
      .equals(0)
      .and(p => p.total_attempts > 0)
      .toArray();

    // Merge and de-duplicate
    const seen = new Set<string>();
    const progressItems = [...dueItems, ...lapsedItems].filter(p => {
      if (seen.has(p.item_id)) return false;
      seen.add(p.item_id);
      return true;
    });

    // 2. Classify & Prioritize
    // Priority: LAPSED (100) > RELEARNING (90) > DUE (40) > LEARNING (70)
    const scoredItems = progressItems.map(p => {
      let score = 40; // Default DUE
      if (p.correct_streak === 0 && p.total_attempts > 0) score = 100; // LAPSED
      else if (p.mastery_level === 0 && p.total_attempts > 0) score = 70; // LEARNING
      return { progress: p, score };
    });

    // Sort descending by score
    scoredItems.sort((a, b) => b.score - a.score);

    // 3. Apply Hard Cap (100)
    const cappedItems = scoredItems.slice(0, 100).map(si => si.progress);

    // 4. Resolve Dictionary Metadata in Bulk
    const itemIds = cappedItems.map(p => p.item_id);
    const entries = await db.global_dictionary.bulkGet(itemIds);
    
    const reviewItems: ReviewItem[] = [];
    for (let i = 0; i < cappedItems.length; i++) {
      const p = cappedItems[i];
      const entry = entries[i];
      
      if (entry) {
        // Derive state for UI
        let state: MasteryState = 'UNKNOWN';
        if (p.mastery_level >= 4) state = 'MASTERED';
        else if (p.mastery_level === 3) state = 'ADVANCED';
        else if (p.mastery_level >= 1) state = 'LEARNED';
        else if (p.correct_streak === 0) state = 'LAPSED';
        else state = 'LEARNING';

        reviewItems.push({
          globalId: p.item_id,
          italian: entry.italian,
          english: entry.english_primary,
          audio: entry.audio_json,
          state,
          type: p.item_type
        });
      }
    }

    return reviewItems;
  }

  /**
   * Translates Anki-style feedback into Hybrid Mastery state updates.
   */
  static async recordReviewResult(globalId: string, outcome: 'AGAIN' | 'HARD' | 'GOOD' | 'EASY') {
    const isCorrect = outcome !== 'AGAIN';
    
    // In a full FSRS implementation, outcome maps to specific interval multipliers.
    // For Phase 7.8 MVP, we adapt to the binary recordAnswer service, 
    // but in a production environment, this would hit an explicit FSRS update function.
    
    // Phase 7.8 Bridge:
    await GlobalProgressService.recordAnswer(globalId, isCorrect, undefined, 'VOCABULARY');
  }
}
