import {foundationLessons} from '@app/data/foundations';
import {useProgressStore} from './progressStore';

describe('progress store', () => {
  beforeEach(() => {
    useProgressStore.setState({
      foundationScores: {},
      scenarioProgress: {},
    });
  });

  it('blocks scenario access until every foundation lesson is at least 90%', () => {
    expect(useProgressStore.getState().areFoundationsPassed()).toBe(false);

    foundationLessons.forEach(lesson => {
      useProgressStore.getState().recordFoundationScore(lesson.id, 90);
    });

    expect(useProgressStore.getState().areFoundationsPassed()).toBe(true);
  });

  it('keeps the best foundation score', () => {
    useProgressStore.getState().recordFoundationScore(1, 95);
    useProgressStore.getState().recordFoundationScore(1, 70);

    expect(useProgressStore.getState().getFoundationScore(1)).toBe(95);
  });

  it('unlocks conversation only after phases 2 through 4 are complete', () => {
    useProgressStore.getState().setScenarioVocabularyCompleted(1, true);
    useProgressStore.getState().setScenarioPhraseScore(1, 85);
    expect(
      useProgressStore.getState().scenarioProgress[1]?.conversationUnlocked,
    ).toBe(false);

    useProgressStore.getState().setScenarioSentenceScore(1, 80);
    expect(
      useProgressStore.getState().scenarioProgress[1]?.conversationUnlocked,
    ).toBe(true);
  });
});
