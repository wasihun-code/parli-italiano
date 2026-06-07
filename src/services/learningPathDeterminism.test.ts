import { describe, it, expect } from 'vitest';
import { LearningPathGenerator } from './learningPathGenerator';
import { PathGenerationInput } from '../types/learningPath';

describe('LearningPathGenerator Determinism', () => {
  const mockInput: PathGenerationInput = {
    scenarioId: 22,
    scenarioData: {
      vocabulary: [{ id: 'v1', italian: 'ciao', english: 'hi' }, { id: 'v2', italian: 'casa', english: 'house' }],
      phrases: [{ id: 'p1', italian: 'Come stai?', english: 'How are you?' }],
      sentences: [{ id: 's1', italian: 'Io vado a casa.', english: 'I go home.' }],
      scriptedConversations: [
        {
          id: 'c1',
          messages: [
            { id: 'm1', role: 'host', text: 'Ciao! Io vado a casa.', choices: [{ text: 'Come stai?', isCorrect: true }] }
          ]
        }
      ]
    },
    globalMastery: { 'v1': 0.5, 'v2': 0.9 },
    reviewQueue: []
  };

  it('generates the exact same path 100 times', () => {
    const firstResult = LearningPathGenerator.generatePath(mockInput);
    const firstJson = JSON.stringify(firstResult);

    for (let i = 0; i < 100; i++) {
      const nextResult = LearningPathGenerator.generatePath(mockInput);
      expect(JSON.stringify(nextResult)).toBe(firstJson);
    }
  });
});
