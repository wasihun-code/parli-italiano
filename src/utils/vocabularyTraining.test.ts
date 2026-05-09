import type {ScenarioVocabularyRow} from '@app/db/vocabularyRepository';
import {useProgressStore} from '@app/store/progressStore';
import {useSrsStore} from '@app/store/srsStore';
import {
  buildVocabularyExercise,
  countLearnedVocabulary,
  maybeCompleteVocabularyPhase,
  registerVocabularyTerms,
} from './vocabularyTraining';

const terms: ScenarioVocabularyRow[] = [
  {
    id: 's1-v1-biglietto',
    scenarioId: 1,
    italian: 'biglietto',
    english: 'ticket',
    sortOrder: 1,
  },
  {
    id: 's1-v2-treno',
    scenarioId: 1,
    italian: 'treno',
    english: 'train',
    sortOrder: 2,
  },
  {
    id: 's1-v3-stazione',
    scenarioId: 1,
    italian: 'stazione',
    english: 'station',
    sortOrder: 3,
  },
  {
    id: 's1-v4-binario',
    scenarioId: 1,
    italian: 'binario',
    english: 'platform',
    sortOrder: 4,
  },
];

describe('vocabulary training logic', () => {
  beforeEach(() => {
    useSrsStore.getState().reset();
    useProgressStore.setState({
      foundationScores: {},
      scenarioProgress: {},
    });
  });

  it('registers vocabulary words in the SRS store', () => {
    registerVocabularyTerms(terms, useSrsStore.getState());

    expect(useSrsStore.getState().items['s1-v1-biglietto']).toMatchObject({
      type: 'vocabulary',
      italian: 'biglietto',
      english: 'ticket',
      correctStreak: 0,
      learned: false,
    });
    expect(Object.keys(useSrsStore.getState().items)).toHaveLength(4);
  });

  it('updates learned progress as words reach three correct answers', () => {
    registerVocabularyTerms(terms, useSrsStore.getState());

    useSrsStore.getState().recordAnswer('s1-v1-biglietto', true);
    useSrsStore.getState().recordAnswer('s1-v1-biglietto', true);
    expect(
      countLearnedVocabulary(terms, useSrsStore.getState().isLearned),
    ).toBe(0);

    useSrsStore.getState().recordAnswer('s1-v1-biglietto', true);
    expect(
      countLearnedVocabulary(terms, useSrsStore.getState().isLearned),
    ).toBe(1);
  });

  it('sets the scenario vocabulary completion flag when all words are learned', () => {
    registerVocabularyTerms(terms, useSrsStore.getState());
    terms.forEach(term => {
      useSrsStore.getState().recordAnswer(term.id, true);
      useSrsStore.getState().recordAnswer(term.id, true);
      useSrsStore.getState().recordAnswer(term.id, true);
    });

    const completed = maybeCompleteVocabularyPhase(
      1,
      terms,
      useSrsStore.getState(),
      useProgressStore.getState(),
    );

    expect(completed).toBe(true);
    expect(
      useProgressStore.getState().scenarioProgress[1]?.vocabularyCompleted,
    ).toBe(true);
  });

  it('resets the correct streak after an incorrect answer', () => {
    registerVocabularyTerms(terms, useSrsStore.getState());

    useSrsStore.getState().recordAnswer('s1-v2-treno', true);
    useSrsStore.getState().recordAnswer('s1-v2-treno', true);
    useSrsStore.getState().recordAnswer('s1-v2-treno', false);

    expect(useSrsStore.getState().items['s1-v2-treno']?.correctStreak).toBe(0);
    expect(useSrsStore.getState().items['s1-v2-treno']?.learned).toBe(false);
  });

  it('rotates through the four required exercise types', () => {
    expect(buildVocabularyExercise(terms[0]!, terms, 0).kind).toBe('flashcard');
    expect(buildVocabularyExercise(terms[0]!, terms, 1).kind).toBe('listening');
    expect(buildVocabularyExercise(terms[0]!, terms, 2).kind).toBe('spelling');
    expect(buildVocabularyExercise(terms[0]!, terms, 3).kind).toBe(
      'multipleChoice',
    );
  });
});
