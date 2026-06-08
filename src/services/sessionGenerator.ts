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
    const vocabSteps = masterPath.steps.filter(s => s.type === 'vocabulary');
    const phraseSteps = masterPath.steps.filter(s => s.type === 'phrase');
    const sentenceSteps = masterPath.steps.filter(s => s.type === 'sentence');
    
    // Enforce a balanced pedagogical diet:
    // Minimum 30% Sentences, 20% Phrases, 50% Vocabulary
    const targetVocab = Math.floor(this.TARGET_SESSION_SIZE * 0.5);
    const targetPhrases = Math.floor(this.TARGET_SESSION_SIZE * 0.2);
    const targetSentences = Math.floor(this.TARGET_SESSION_SIZE * 0.3);
    
    const selected: LearningStep[] = [
      ...vocabSteps.slice(0, targetVocab),
      ...phraseSteps.slice(0, targetPhrases),
      ...sentenceSteps.slice(0, targetSentences)
    ];
    
    // Fill remaining if there are shortages in any category
    if (selected.length < this.TARGET_SESSION_SIZE) {
      const remaining = masterPath.steps.filter(s => !selected.includes(s));
      selected.push(...remaining.slice(0, this.TARGET_SESSION_SIZE - selected.length));
    }
    
    // Shuffle the final selection to interleave the difficulty
    return selected.sort(() => Math.random() - 0.5);
  }
}
