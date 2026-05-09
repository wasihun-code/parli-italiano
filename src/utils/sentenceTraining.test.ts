import type {ScenarioSentenceRow} from '@app/db/vocabularyRepository';
import {useProgressStore} from '@app/store/progressStore';
import {useSrsStore} from '@app/store/srsStore';
import {
  buildSentenceExercise,
  calculateSentenceScore,
  completeSentencePhase,
  hasPracticedAllSentenceExercises,
  isSentenceAnswerCorrect,
  recordSentenceAttempt,
  registerSentenceItems,
  type SentenceTrainingStats,
} from './sentenceTraining';

const sentences: ScenarioSentenceRow[] = [
  {
    id: 's1-s1',
    scenarioId: 1,
    italian: 'Vorrei uscita, per favore.',
    english: 'I would like exit, please.',
    grammarPoint: 'Vorrei + noun/phrase for polite requests.',
    passScore: 80,
    sortOrder: 1,
  },
  {
    id: 's1-s2',
    scenarioId: 1,
    italian: "Dov'è bagagli?",
    english: 'Where is luggage?',
    grammarPoint: "Dov'è combines dove + è for where is.",
    passScore: 80,
    sortOrder: 2,
  },
];

describe('sentence training logic', () => {
  beforeEach(() => {
    useSrsStore.getState().reset();
    useProgressStore.setState({
      foundationScores: {},
      scenarioProgress: {},
    });
  });

  it('generates a dictation prompt with grammar point', () => {
    const exercise = buildSentenceExercise(sentences[0]!, 0);

    expect(exercise.kind).toBe('dictation');
    expect(exercise.prompt).toBe('Listen and type the Italian sentence.');
    expect(exercise.answer).toBe('Vorrei uscita, per favore.');
    expect(exercise.grammarPoint).toContain('Vorrei');
  });

  it('generates a translation prompt from English to Italian', () => {
    const exercise = buildSentenceExercise(sentences[0]!, 1);

    expect(exercise.kind).toBe('translation');
    expect(exercise.prompt).toBe('I would like exit, please.');
    expect(exercise.answer).toBe('Vorrei uscita, per favore.');
  });

  it('generates sentence completion with one blank and grammar point', () => {
    const exercise = buildSentenceExercise(sentences[0]!, 2);

    expect(exercise.kind).toBe('completion');
    expect(exercise.displayItalian).toContain('____');
    expect(exercise.displayItalian?.match(/____/g)).toHaveLength(1);
    expect(exercise.answer.length).toBeGreaterThan(0);
    expect(exercise.grammarPoint).toContain('Vorrei');
  });

  it('normalizes sentence answers for scoring', () => {
    expect(
      isSentenceAnswerCorrect(' vorrei uscita, per favore ', 'Vorrei uscita, per favore.'),
    ).toBe(true);
    expect(isSentenceAnswerCorrect('vorrei bagagli', 'Vorrei uscita')).toBe(
      false,
    );
  });

  it('calculates cumulative sentence scores', () => {
    let stats: SentenceTrainingStats = {};
    stats = recordSentenceAttempt(stats, 's1-s1', true);
    stats = recordSentenceAttempt(stats, 's1-s1', true);
    stats = recordSentenceAttempt(stats, 's1-s2', false);

    expect(calculateSentenceScore(stats)).toBe(67);
  });

  it('registers sentence SRS items and records answers for review', () => {
    registerSentenceItems(sentences, useSrsStore.getState());
    useSrsStore.getState().recordAnswer('s1-s1', true);

    expect(useSrsStore.getState().items['s1-s1']).toMatchObject({
      type: 'sentence',
      italian: 'Vorrei uscita, per favore.',
      english: 'I would like exit, please.',
      attempts: 1,
      correctStreak: 1,
    });
  });

  it('sets scenario sentence progress with the final score', () => {
    let stats: SentenceTrainingStats = {};
    stats = recordSentenceAttempt(stats, 's1-s1', true);
    stats = recordSentenceAttempt(stats, 's1-s2', true);

    const score = completeSentencePhase(
      1,
      stats,
      useProgressStore.getState(),
    );

    expect(score).toBe(100);
    expect(useProgressStore.getState().scenarioProgress[1]).toMatchObject({
      sentenceScore: 100,
      sentenceCompleted: true,
    });
  });

  it('detects completion after every sentence has all three exercise types', () => {
    expect(hasPracticedAllSentenceExercises(sentences, 5)).toBe(false);
    expect(hasPracticedAllSentenceExercises(sentences, 6)).toBe(true);
  });
});
