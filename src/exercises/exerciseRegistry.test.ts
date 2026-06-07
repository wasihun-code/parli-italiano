import { describe, it, expect } from 'vitest';
import { ExerciseRegistry } from './registry';
import { resolveExercise } from './resolver';
import { LearningStep } from '../types/learningPath';

describe('ExerciseRegistry', () => {
  it('contains all 12 required exercise types', () => {
    const requiredTypes = [
      'Listen', 'ListenChoose', 'Match', 'BuildSentence', 'Recall',
      'Dictation', 'Speaking', 'Reading', 'Conversation', 'Review',
      'Assembly', 'Spelling'
    ];
    
    requiredTypes.forEach(type => {
      expect(ExerciseRegistry[type]).toBeDefined();
      expect(ExerciseRegistry[type].metadata.id).toBe(type);
    });
  });

  it('provides a valid definition for every registered type', () => {
    Object.values(ExerciseRegistry).forEach(def => {
      expect(def.metadata.name).toBeTruthy();
      expect(def.payloadBuilder).toBeTypeOf('function');
      expect(def.validator).toBeTypeOf('function');
      expect(def.completionHandler).toBeTypeOf('function');
    });
  });
});

describe('resolveExercise', () => {
  const mockScenarioData = {
    vocabulary: [{ id: 'v1', italian: 'ciao', english: 'hi' }],
    phrases: [],
    sentences: [],
    scriptedConversations: []
  };

  it('correctly resolves a vocabulary match step', () => {
    const step: LearningStep = {
      id: 'v1-match',
      itemId: 'v1',
      type: 'vocabulary',
      exerciseType: 'Match',
      masteryContribution: 0.2
    };
    
    const { definition, payload } = resolveExercise(step, mockScenarioData);
    
    expect(definition.metadata.id).toBe('Match');
    expect(payload.itemId).toBe('v1');
    expect(payload.italian).toBe('ciao');
  });

  it('throws error for unregistered exercise type', () => {
    const step: any = {
      id: 'v1-fake',
      itemId: 'v1',
      type: 'vocabulary',
      exerciseType: 'FakeType',
      masteryContribution: 0.2
    };
    
    expect(() => resolveExercise(step, mockScenarioData)).toThrow(/not found in registry/);
  });
});
