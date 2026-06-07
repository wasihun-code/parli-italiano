import { ExercisePayload, ExerciseFactory } from './types';

/**
 * Builds a basic text/audio payload.
 */
export const basicPayloadBuilder: ExerciseFactory = (itemData: any, _stepId: string): ExercisePayload => {
  return {
    itemId: itemData.id,
    italian: itemData.italian,
    english: itemData.english,
    audio: itemData.audio,
    hint: itemData.hint
  };
};

/**
 * Builds a multiple choice payload.
 */
export const mcqPayloadBuilder: ExerciseFactory = (itemData: any, _stepId: string): ExercisePayload => {
  const base = basicPayloadBuilder(itemData, _stepId);
  return {
    ...base,
    options: itemData.choicesItalian || itemData.choicesEnglish || [itemData.italian, 'Option B', 'Option C', 'Option D']
  };
};

/**
 * Builds an assembly payload.
 */
export const assemblyPayloadBuilder: ExerciseFactory = (itemData: any, _stepId: string): ExercisePayload => {
  const base = basicPayloadBuilder(itemData, _stepId);
  const words = itemData.italian.split(/[\s,.'!?]+/).filter(Boolean);
  
  // Shuffled words for the UI to display
  const scrambledWords = [...words].sort(() => Math.random() - 0.5);
  
  return {
    ...base,
    scrambledWords
  };
};

/**
 * Builds a recall / fill-in-the-blank payload.
 */
export const recallPayloadBuilder: ExerciseFactory = (itemData: any, _stepId: string): ExercisePayload => {
  const base = basicPayloadBuilder(itemData, _stepId);
  const words = itemData.italian.split(' ');
  const blankIndex = Math.floor(Math.random() * words.length);
  
  return {
    ...base,
    blankIndex
  };
};
