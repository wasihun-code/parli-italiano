import { ExerciseValidator, ExercisePayload, ValidationResult } from './types';

/**
 * Standard exact string match validator.
 */
export const exactMatchValidator: ExerciseValidator = (payload: ExercisePayload, userInput: string): ValidationResult => {
  const normalizedUser = userInput.trim().toLowerCase();
  const normalizedTarget = payload.italian.trim().toLowerCase();
  
  const isValid = normalizedUser === normalizedTarget;
  return {
    isValid,
    score: isValid ? 1.0 : 0.0,
    correctAnswer: payload.italian
  };
};

/**
 * Multiple choice validator.
 */
export const mcqValidator: ExerciseValidator = (payload: ExercisePayload, userInput: string): ValidationResult => {
  const isValid = userInput === payload.italian || userInput === payload.english;
  return {
    isValid,
    score: isValid ? 1.0 : 0.0,
    correctAnswer: payload.options?.find(o => o === payload.italian || o === payload.english) || payload.italian
  };
};

/**
 * Assembly / Word order validator.
 */
export const assemblyValidator: ExerciseValidator = (payload: ExercisePayload, userInput: string[]): ValidationResult => {
  const targetWords = payload.italian.toLowerCase().split(/[\s,.'!?]+/).filter(Boolean);
  const userWords = userInput.map(w => w.toLowerCase());
  
  if (targetWords.length !== userWords.length) {
    return { isValid: false, score: 0.0, correctAnswer: payload.italian };
  }
  
  const isValid = targetWords.every((w, i) => w === userWords[i]);
  return {
    isValid,
    score: isValid ? 1.0 : 0.0,
    correctAnswer: payload.italian
  };
};

/**
 * Partial credit validator (e.g., for Speaking).
 */
export const fuzzyMatchValidator: ExerciseValidator = (payload: ExercisePayload, userInput: string): ValidationResult => {
  const normalizedUser = userInput.trim().toLowerCase();
  const normalizedTarget = payload.italian.trim().toLowerCase();
  
  if (normalizedUser === normalizedTarget) {
    return { isValid: true, score: 1.0 };
  }
  
  // Basic heuristic: if it contains the target or is very close
  const score = normalizedUser.includes(normalizedTarget) ? 0.8 : 0.0;
  
  return {
    isValid: score > 0.7,
    score,
    correctAnswer: payload.italian
  };
};
