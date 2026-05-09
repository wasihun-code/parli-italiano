import type {ScenarioPhaseProgress} from '@app/store/progressStore';
import {
  calculateFoundationProgress,
  findResumeScenario,
  getNextScenarioRoute,
} from './home';

const baseProgress: ScenarioPhaseProgress = {
  vocabularyCompleted: false,
  phraseScore: 0,
  phraseCompleted: false,
  sentenceScore: 0,
  sentenceCompleted: false,
  conversationUnlocked: false,
};

describe('home resume logic', () => {
  it('identifies the next incomplete scenario phase', () => {
    expect(getNextScenarioRoute(3, baseProgress)).toEqual({
      name: 'VocabularyTraining',
      params: {scenarioId: 3},
    });

    expect(
      getNextScenarioRoute(3, {
        ...baseProgress,
        vocabularyCompleted: true,
        phraseCompleted: true,
      }),
    ).toEqual({name: 'SentenceTraining', params: {scenarioId: 3}});
  });

  it('finds a resume scenario from stored progress', () => {
    const resume = findResumeScenario({
      2: {
        ...baseProgress,
        vocabularyCompleted: true,
        phraseScore: 50,
      },
    });

    expect(resume).toMatchObject({
      scenarioId: 2,
      route: {name: 'PhraseTraining', params: {scenarioId: 2}},
      label: 'Continue Phrases',
    });
  });

  it('calculates foundation progress', () => {
    expect(calculateFoundationProgress({1: 90, 2: 80, 3: 95}, 5)).toBe(40);
  });
});
