import { PathGenerationInput } from '../types/learningPath';

export interface ReadinessResult {
  isReady: boolean;
  score: {
    vocabulary: number;
    phrases: number;
    sentences: number;
  };
  missingIds: string[];
}

/**
 * ConversationReadinessService
 * 
 * Logic to determine if a learner is prepared to enter a branching conversation.
 */
export class ConversationReadinessService {

  private static readonly PRODUCTION_THRESHOLD = 0.8;
  private static readonly REQUIRED_PERCENT = 80;

  /**
   * Checks if the user has reached the production threshold for enough items.
   */
  static checkReadiness(input: PathGenerationInput): ReadinessResult {
    const { scenarioData, globalMastery } = input;

    const checkCategory = (items: any[]) => {
      if (items.length === 0) return 100;
      const productionCount = items.filter(item => (globalMastery[item.id] ?? 0) >= this.PRODUCTION_THRESHOLD).length;
      return (productionCount / items.length) * 100;
    };

    const vocabScore = checkCategory(scenarioData.vocabulary);
    const phraseScore = checkCategory(scenarioData.phrases);
    const sentenceScore = checkCategory(scenarioData.sentences);

    const isReady = vocabScore >= this.REQUIRED_PERCENT && 
                    phraseScore >= this.REQUIRED_PERCENT && 
                    sentenceScore >= this.REQUIRED_PERCENT;

    const missingIds: string[] = [];
    [...scenarioData.vocabulary, ...scenarioData.phrases, ...scenarioData.sentences].forEach(item => {
      if ((globalMastery[item.id] ?? 0) < this.PRODUCTION_THRESHOLD) {
        missingIds.push(item.id);
      }
    });

    return {
      isReady,
      score: {
        vocabulary: Math.round(vocabScore),
        phrases: Math.round(phraseScore),
        sentences: Math.round(sentenceScore)
      },
      missingIds
    };
  }
}
