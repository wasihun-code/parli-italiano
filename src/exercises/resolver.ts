import { LearningStep } from '../types/learningPath';
import { ExerciseRegistry } from './registry';

/**
 * Resolves a LearningStep into a formal ExerciseDefinition and its dynamic payload.
 * 
 * @param step The learning step from the generator path.
 * @param scenarioData The full scenario data corpus.
 * @returns { definition: ExerciseDefinition, payload: ExercisePayload }
 */
export const resolveExercise = (step: LearningStep, scenarioData: any) => {
  const definition = ExerciseRegistry[step.exerciseType];
  
  if (!definition) {
    throw new Error(`Exercise type '${step.exerciseType}' not found in registry.`);
  }
  
  // Find the item data from scenarioData
  let itemData = null;
  if (step.type === 'vocabulary') {
    itemData = scenarioData.vocabulary.find((v: any) => v.id === step.itemId);
  } else if (step.type === 'phrase') {
    itemData = scenarioData.phrases.find((p: any) => p.id === step.itemId);
  } else if (step.type === 'sentence') {
    itemData = scenarioData.sentences.find((s: any) => s.id === step.itemId);
  } else if (step.type === 'conversation') {
    itemData = scenarioData.scriptedConversations.find((c: any) => c.id === step.itemId);
  }
  
  if (!itemData) {
    throw new Error(`Item data for '${step.itemId}' (${step.type}) not found in scenario data.`);
  }
  
  const payload = definition.payloadBuilder(itemData, step.id);
  
  return {
    definition,
    payload
  };
};
