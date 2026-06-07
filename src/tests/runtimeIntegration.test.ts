import { describe, it, expect } from 'vitest';
import { LearningPathGenerator } from '../services/learningPathGenerator';
import { resolveExercise } from '../exercises/resolver';
import { ConversationReadinessService } from '../services/conversationReadinessService';

describe('Runtime Integration Pilot', () => {
  const mockScenarioData = {
    vocabulary: [{ id: 'v1', italian: 'ciao', english: 'hi', audio: { italian: '/audio/test.opus' } }],
    phrases: [{ id: 'p1', italian: 'Come stai?', english: 'How are you?' }],
    sentences: [{ id: 's1', italian: 'Io vado.', english: 'I go.' }],
    scriptedConversations: []
  };

  it('verifies the full flow from Generator to Readiness', () => {
    // 1. Generator
    const input = {
      scenarioId: 22,
      scenarioData: mockScenarioData as any,
      globalMastery: {},
      reviewQueue: []
    };
    const genResult = LearningPathGenerator.generatePath(input);
    expect(genResult.path.steps.length).toBeGreaterThan(0);

    // 2. Resolver
    const step = genResult.path.steps[0];
    const { definition, payload } = resolveExercise(step, mockScenarioData);
    expect(definition).toBeDefined();
    expect(payload.itemId).toBe(step.itemId);

    // 3. Completion Simulation (Manual Mastery Update)
    const localMastery = { [step.itemId]: 0.8 }; // Production level

    // 4. Readiness
    const readinessResult = ConversationReadinessService.checkReadiness({
      scenarioId: 22,
      scenarioData: mockScenarioData as any,
      globalMastery: localMastery,
      reviewQueue: []
    });

    // Since we only mastered 1 item out of 3, it should be false
    expect(readinessResult.isReady).toBe(false);
    expect(readinessResult.score.vocabulary).toBe(100); // v1 is 100% of vocab category
    expect(readinessResult.score.phrases).toBe(0);
  });
});
