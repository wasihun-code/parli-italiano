import { describe, it, expect } from 'vitest';
import { LearningPathGenerator } from './learningPathGenerator';
import { PathGenerationInput } from '../types/learningPath';

describe('LearningPathGenerator', () => {
  const mockScenarioData = {
    vocabulary: [
      { id: 'v1', italian: 'ciao', english: 'hi' }, 
      { id: 'v2', italian: 'grazie', english: 'thanks' }
    ],
    phrases: [
      { id: 'p1', italian: 'Per favore', english: 'Please' }
    ],
    sentences: [
      { id: 's1', italian: 'Come va?', english: 'How goes it?' }
    ],
    scriptedConversations: [
      {
        id: 'c1',
        messages: [
          { id: 'm1', role: 'host', text: 'Come va?', choices: [{ text: 'Per favore', isCorrect: true }] },
          { id: 'm2', role: 'host', text: 'Grazie', choices: [] }
        ]
      }
    ]
  };

  it('sorts items based on conversation chronology', () => {
    // In our mock, 's1' (Come va?) is Turn 1, 'p1' (Per favore) is Turn 2, 'v2' (grazie) is Turn 3.
    // 'v1' (ciao) is NOT in the conversation, so it should be at the end.
    
    const input: PathGenerationInput = {
      scenarioId: 22,
      scenarioData: mockScenarioData as any,
      globalMastery: {},
      reviewQueue: []
    };
    
    const result = LearningPathGenerator.generatePath(input);
    const itemOrder = [...new Set(result.path.steps.map(s => s.itemId))];
    
    // Check if 's1' appears before 'p1'
    const s1Index = itemOrder.indexOf('s1');
    const p1Index = itemOrder.indexOf('p1');
    const v2Index = itemOrder.indexOf('v2');
    const v1Index = itemOrder.indexOf('v1');
    
    expect(s1Index).toBeLessThan(p1Index);
    expect(p1Index).toBeLessThan(v2Index);
    expect(v1Index).toBeGreaterThan(v2Index);
  });

  it('adapts exercise sequence for mastered items', () => {
    const input: PathGenerationInput = {
      scenarioId: 22,
      scenarioData: mockScenarioData as any,
      globalMastery: { 'v1': 0.9 }, // Mastered
      reviewQueue: []
    };
    
    const result = LearningPathGenerator.generatePath(input);
    const v1Steps = result.path.steps.filter(s => s.itemId === 'v1');
    
    // For mastered items, it should only have Spelling and Speaking
    const types = v1Steps.map(s => s.exerciseType);
    expect(types).toContain('Spelling');
    expect(types).toContain('Speaking');
    expect(types).not.toContain('Listen');
    expect(types).not.toContain('Match');
  });

  it('implements 25% mastery accelerated recall', () => {
    const input: PathGenerationInput = {
      scenarioId: 22,
      scenarioData: mockScenarioData as any,
      globalMastery: { 
        'v1': 0.5, 
        'v2': 0.8, // Mastered -> 25% of 4 items
        'p1': 0.5, 
        's1': 0.5 
      },
      reviewQueue: []
    };
    
    const result = LearningPathGenerator.generatePath(input);
    const v1Steps = result.path.steps.filter(s => s.itemId === 'v1');
    
    // Should skip 'ListenChoose' if global mastery > 25% and item mastery > 0.4
    const types = v1Steps.map(s => s.exerciseType);
    expect(types).not.toContain('ListenChoose');
  });

  it('prioritizes Review Queue items at the start of the path', () => {
    const input: PathGenerationInput = {
      scenarioId: 22,
      scenarioData: mockScenarioData as any,
      globalMastery: {},
      reviewQueue: ['v2'] // 'v2' is normally last in chronology but in review queue
    };

    const result = LearningPathGenerator.generatePath(input);
    
    // v2 steps should come BEFORE s1 steps (s1 is first in chronology)
    const v2Index = result.path.steps.findIndex(s => s.itemId === 'v2');
    const s1Index = result.path.steps.findIndex(s => s.itemId === 's1');
    
    expect(v2Index).toBeLessThan(s1Index);
  });
});
