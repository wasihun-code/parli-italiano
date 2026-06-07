import { ExerciseType } from '../types/learningPath';

/**
 * High-level categories for grouping exercises.
 */
export type ExerciseCategory = 'Recognition' | 'Recall' | 'Production' | 'Application';

/**
 * Exercise difficulty levels.
 */
export type ExerciseDifficulty = 'Beginner' | 'Intermediate' | 'Advanced';

/**
 * Metadata for an exercise type.
 */
export interface ExerciseMetadata {
  id: ExerciseType;
  name: string;
  category: ExerciseCategory;
  difficulty: ExerciseDifficulty;
}

/**
 * The data required to render an exercise.
 * Polymorphic based on ExerciseType.
 */
export interface ExercisePayload {
  itemId: string;
  italian: string;
  english: string;
  audio?: any; // ScenarioAudio or hash string
  audioUrl?: string; // Resolved URL
  options?: string[]; // For MCQ types
  scrambledWords?: string[]; // For Assembly/BuildSentence
  blankIndex?: number; // For Fill-in-the-blank/Recall
  hint?: string;
  // Specific fields for specialized types can be added here
}

/**
 * Result of validating a user's answer.
 */
export interface ValidationResult {
  isValid: boolean;
  score: number; // 0.0 to 1.0
  feedback?: string;
  correctAnswer?: string;
}

/**
 * Logic to validate user input for a specific exercise type.
 */
export type ExerciseValidator = (payload: ExercisePayload, userInput: any) => ValidationResult;

/**
 * Contract for what happens when an exercise completes.
 */
export interface ExerciseCompletionResult {
  stepId: string;
  itemId: string;
  exerciseType: ExerciseType;
  success: boolean;
  score: number;
  attempts: number;
  responseTimeMs: number;
  masteryImpact: number;
  reviewRecommendation: 'RETRY' | 'MAINTAIN' | 'ACCELERATE';
}

/**
 * A factory that builds the payload for an exercise.
 */
export type ExerciseFactory = (itemData: any, stepId: string) => ExercisePayload;

/**
 * A completion handler that processes the result.
 */
export type CompletionHandler = (result: ExerciseCompletionResult) => void;

/**
 * The formal definition of an exercise type in the registry.
 */
export interface ExerciseDefinition {
  metadata: ExerciseMetadata;
  payloadBuilder: ExerciseFactory;
  validator: ExerciseValidator;
  completionHandler: CompletionHandler;
}
