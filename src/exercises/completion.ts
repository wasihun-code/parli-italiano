import { ExerciseCompletionResult } from './types';
import { GlobalProgressService } from '../services/globalProgressService';

/**
 * Standard completion handler that logs the result and updates global progress.
 */
export const defaultCompletionHandler = async (result: ExerciseCompletionResult): Promise<void> => {
  console.log(`[Exercise Completion] item:${result.itemId} type:${result.exerciseType} success:${result.success} score:${result.score}`);
  
  // Update the global progress in Dexie
  await GlobalProgressService.recordAnswer(result.itemId, result.success);
};

/**
 * Creates a completion result based on performance.
 */
export const createCompletionResult = (
  stepId: string, 
  itemId: string, 
  exerciseType: any,
  success: boolean,
  score: number,
  attempts: number,
  responseTimeMs: number
): ExerciseCompletionResult => {
  return {
    stepId,
    itemId,
    exerciseType,
    success,
    score,
    attempts,
    responseTimeMs,
    masteryImpact: success ? 0.1 : -0.2, // Base FSRS-lite impact
    reviewRecommendation: success ? 'MAINTAIN' : 'RETRY'
  };
};
