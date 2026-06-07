import { describe, it, expect } from 'vitest';
import { ConversationReadinessService } from './conversationReadinessService';
import { PathGenerationInput } from '../types/learningPath';

describe('ConversationReadinessService', () => {
  const mockScenarioData = {
    vocabulary: [{ id: 'v1' }, { id: 'v2' }, { id: 'v3' }, { id: 'v4' }, { id: 'v5' }],
    phrases: [{ id: 'p1' }, { id: 'p2' }, { id: 'p3' }, { id: 'p4' }, { id: 'p5' }],
    sentences: [{ id: 's1' }, { id: 's2' }, { id: 's3' }, { id: 's4' }, { id: 's5' }],
    scriptedConversations: []
  };

  it('fails when under 80% production level', () => {
    const input: PathGenerationInput = {
      scenarioId: 22,
      scenarioData: mockScenarioData as any,
      globalMastery: {
        'v1': 0.8, 'v2': 0.8, 'v3': 0.8, 'v4': 0.1, 'v5': 0.1, // 60% vocab
        'p1': 0.8, 'p2': 0.8, 'p3': 0.8, 'p4': 0.8, 'p5': 0.8, // 100% phrases
        's1': 0.8, 's2': 0.8, 's3': 0.8, 's4': 0.8, 's5': 0.8, // 100% sentences
      },
      reviewQueue: []
    };
    const result = ConversationReadinessService.checkReadiness(input);
    expect(result.isReady).toBe(false);
    expect(result.score.vocabulary).toBe(60);
  });

  it('fails at 79% production level', () => {
    // 4 out of 5 is 80%, so to get 79% we need more items
    const manyItems = Array.from({length: 100}, (_, i) => ({ id: `v${i}` }));
    const mastery: Record<string, number> = {};
    for (let i = 0; i < 79; i++) mastery[`v${i}`] = 0.8;
    for (let i = 79; i < 100; i++) mastery[`v${i}`] = 0.1;

    const input: PathGenerationInput = {
      scenarioId: 22,
      scenarioData: { ...mockScenarioData, vocabulary: manyItems } as any,
      globalMastery: {
        ...mastery,
        'p1': 0.8, 'p2': 0.8, 'p3': 0.8, 'p4': 0.8, 'p5': 0.8,
        's1': 0.8, 's2': 0.8, 's3': 0.8, 's4': 0.8, 's5': 0.8,
      },
      reviewQueue: []
    };
    const result = ConversationReadinessService.checkReadiness(input);
    expect(result.isReady).toBe(false);
    expect(result.score.vocabulary).toBe(79);
  });

  it('passes when at or above 80% production level for all categories', () => {
    const input: PathGenerationInput = {
      scenarioId: 22,
      scenarioData: mockScenarioData as any,
      globalMastery: {
        'v1': 0.8, 'v2': 0.8, 'v3': 0.8, 'v4': 0.8, 'v5': 0.1, // 80% vocab
        'p1': 0.8, 'p2': 0.8, 'p3': 0.8, 'p4': 0.8, 'p5': 0.1, // 80% phrases
        's1': 0.8, 's2': 0.8, 's3': 0.8, 's4': 0.8, 's5': 0.1, // 80% sentences
      },
      reviewQueue: []
    };
    const result = ConversationReadinessService.checkReadiness(input);
    expect(result.isReady).toBe(true);
    expect(result.score.vocabulary).toBe(80);
    expect(result.score.phrases).toBe(80);
    expect(result.score.sentences).toBe(80);
  });

  it('passes at 100% production level', () => {
    const input: PathGenerationInput = {
      scenarioId: 22,
      scenarioData: mockScenarioData as any,
      globalMastery: {
        'v1': 0.9, 'v2': 0.9, 'v3': 0.9, 'v4': 0.9, 'v5': 0.9,
        'p1': 0.9, 'p2': 0.9, 'p3': 0.9, 'p4': 0.9, 'p5': 0.9,
        's1': 0.9, 's2': 0.9, 's3': 0.9, 's4': 0.9, 's5': 0.9,
      },
      reviewQueue: []
    };
    const result = ConversationReadinessService.checkReadiness(input);
    expect(result.isReady).toBe(true);
    expect(result.score.vocabulary).toBe(100);
  });
});
