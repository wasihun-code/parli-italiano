import { LearningPath, LearningStep } from '../types/learningPath';

/**
 * SessionGenerator
 * 
 * Responsible for chunking the master learning path into manageable 
 * daily sessions (20-30 exercises).
 */
export class SessionGenerator {
  public static readonly TARGET_SESSION_SIZE = 25;
  public static readonly MIN_SESSION_SIZE = 15;
  public static readonly MAX_SESSION_SIZE = 40;

  /**
   * Returns a subset of the master path for a single session.
   */
  static generateSession(masterPath: LearningPath): LearningStep[] {
    // Current implementation: Strict chunking of the first N steps.
    // Since the master path is already sorted by chronology and filtered by mastery,
    // the first N steps are always the most relevant next steps for the learner.
    return masterPath.steps.slice(0, this.TARGET_SESSION_SIZE);
  }
}
