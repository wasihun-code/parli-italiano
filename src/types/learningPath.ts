
/**
 * Supported exercise types in Learning System V3.
 */
export type ExerciseType =
  | 'Listen'
  | 'ListenChoose'
  | 'Match'
  | 'BuildSentence'
  | 'Recall'
  | 'Dictation'
  | 'Speaking'
  | 'Reading'
  | 'Conversation'
  | 'Review'
  | 'Assembly'
  | 'Spelling';

/**
 * A single step in a learning path.
 */
export interface LearningStep {
  id: string; // Unique ID for this step (e.g., v1-match)
  itemId: string; // The ID of the item being taught (e.g., v1)
  type: 'vocabulary' | 'phrase' | 'sentence' | 'conversation';
  exerciseType: ExerciseType;
  masteryContribution: number;
}

/**
 * The complete sequence for a learning session.
 */
export interface LearningPath {
  scenarioId: number;
  steps: LearningStep[];
}

/**
 * Input required to generate a deterministic learning path.
 */
export interface PathGenerationInput {
  scenarioId: number;
  scenarioData: {
    vocabulary: any[];
    phrases: any[];
    sentences: any[];
    scriptedConversations?: any[];
  };
  globalMastery: Record<string, number>; // itemId -> masteryLevel (0.0 to 1.0)
  reviewQueue: string[]; // List of item IDs due for review
}

/**
 * Result of the path generation process.
 */
export interface PathGenerationResult {
  path: LearningPath;
  stats: {
    totalSteps: number;
    recognitionCount: number;
    recallCount: number;
    productionCount: number;
  };
}

/**
 * Represents the cognitive phase of a learning item.
 */
export type CognitivePhase = 'Recognition' | 'Recall' | 'Production' | 'Conversation';
