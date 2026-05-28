import type {ScenarioSentenceRow} from '@app/db/vocabularyRepository';
import type {useProgressStore} from '@app/store/progressStore';
import type {useSrsStore} from '@app/store/srsStore';
import {levenshteinDistance} from './string';

export type SentenceExerciseKind =
  | 'dictation'
  | 'translation'
  | 'completion';

export type SentenceExercise = {
  kind: SentenceExerciseKind;
  sentenceId: string;
  prompt: string;
  answer: string;
  english: string;
  grammarPoint: string;
  displayItalian?: string;
  missingText?: string;
};

export type SentenceAttemptStats = {
  attempts: number;
  correct: number;
};

export type SentenceTrainingStats = Record<string, SentenceAttemptStats>;

type SrsApi = Pick<ReturnType<typeof useSrsStore.getState>, 'registerItem'>;

type ProgressApi = Pick<
  ReturnType<typeof useProgressStore.getState>,
  'setScenarioSentenceScore'
>;

const lowValueWords = new Set([
  'a',
  'al',
  'alla',
  'alle',
  'con',
  'da',
  'dalla',
  'de',
  'del',
  'della',
  'di',
  'e',
  'è',
  'gli',
  'i',
  'il',
  'in',
  'la',
  'le',
  'lo',
  'per',
  'su',
  'un',
  'una',
  'uno',
]);

export function sortSentencesByDifficulty<T extends {italian: string}>(
  sentences: T[],
): T[] {
  return [...sentences].sort((a, b) => {
    // Primary: clause count (simple sentences with 1 verb vs compound)
    const clauseCount = (s: string) => {
      // Count conjugated verbs roughly (are/ere/ire endings + common irregulars)
      const verbs = s.match(
        /\b(?:sono|sei|è|siamo|siete|sono|ho|hai|ha|abbiamo|avete|hanno|vado|vai|va|andiamo|andate|vanno|faccio|fai|fa|facciamo|fate|fanno|posso|puoi|può|possiamo|potete|possono|devo|devi|deve|dobbiamo|dovete|devono|voglio|vuoi|vuole|vogliamo|volete|vogliono|\w+are|\w+ere|\w+ire)\b/gi,
      );
      return verbs ? verbs.length : 1;
    };
    const clausesA = clauseCount(a.italian);
    const clausesB = clauseCount(b.italian);
    if (clausesA !== clausesB) return clausesA - clausesB;

    // Secondary: total character length
    if (a.italian.length !== b.italian.length) {
      return a.italian.length - b.italian.length;
    }

    return a.italian.localeCompare(b.italian);
  });
}

export function registerSentenceItems(
  sentences: ScenarioSentenceRow[],
  srs: SrsApi,
): void {
  sentences.forEach(sentence =>
    srs.registerItem({
      id: sentence.id,
      type: 'sentence',
      italian: sentence.italian,
      english: sentence.english,
      audio: sentence.audio,
    }),
  );
}

export function getSentenceExerciseKind(
  exerciseIndex: number,
): SentenceExerciseKind {
  const kinds: SentenceExerciseKind[] = [
    'dictation',
    'translation',
    'completion',
  ];
  return kinds[exerciseIndex % kinds.length] ?? 'dictation';
}

function splitWords(sentence: string): string[] {
  return sentence
    .trim()
    .split(/\s+/)
    .filter(Boolean);
}

function stripEdgePunctuation(word: string): string {
  return word.replace(/^[^\p{L}\p{N}]+|[^\p{L}\p{N}]+$/gu, '');
}

function chooseCompletionSpan(sentence: string): {
  start: number;
  length: number;
  missingText: string;
} {
  const words = splitWords(sentence);
  const candidates = words
    .map((word, index) => ({
      index,
      clean: stripEdgePunctuation(word),
    }))
    .filter(candidate => {
      const lower = candidate.clean.toLocaleLowerCase('it-IT');
      return candidate.clean.length > 1 && !lowValueWords.has(lower);
    })
    .sort((left, right) => right.clean.length - left.clean.length);

  const first = candidates[0];
  if (!first) {
    return {
      start: 0,
      length: 1,
      missingText: stripEdgePunctuation(words[0] ?? ''),
    };
  }

  const nextWord = words[first.index + 1];
  const nextClean = nextWord ? stripEdgePunctuation(nextWord) : '';
  const canUseTwoWords =
    nextClean.length > 2 &&
    !lowValueWords.has(nextClean.toLocaleLowerCase('it-IT'));

  return {
    start: first.index,
    length: canUseTwoWords ? 2 : 1,
    missingText: words
      .slice(first.index, first.index + (canUseTwoWords ? 2 : 1))
      .map(stripEdgePunctuation)
      .join(' '),
  };
}

export function buildSentenceCompletion(sentence: string): {
  displayItalian: string;
  missingText: string;
} {
  const words = splitWords(sentence);
  const span = chooseCompletionSpan(sentence);
  const displayItalian = words
    .map((word, index) =>
      index === span.start
        ? '____'
        : index > span.start && index < span.start + span.length
          ? ''
          : word,
    )
    .filter(Boolean)
    .join(' ');

  return {
    displayItalian,
    missingText: span.missingText,
  };
}

export function buildSentenceExercise(
  sentence: ScenarioSentenceRow,
  exerciseIndex: number,
): SentenceExercise {
  const kind = getSentenceExerciseKind(exerciseIndex);

  if (kind === 'translation') {
    return {
      kind,
      sentenceId: sentence.id,
      prompt: sentence.english,
      answer: sentence.italian,
      english: sentence.english,
      grammarPoint: sentence.grammarPoint,
    };
  }

  if (kind === 'completion') {
    const completion = buildSentenceCompletion(sentence.italian);
    return {
      kind,
      sentenceId: sentence.id,
      prompt: sentence.english,
      answer: completion.missingText,
      english: sentence.english,
      grammarPoint: sentence.grammarPoint,
      displayItalian: completion.displayItalian,
      missingText: completion.missingText,
    };
  }

  return {
    kind,
    sentenceId: sentence.id,
    prompt: 'Listen and type the Italian sentence.',
    answer: sentence.italian,
    english: sentence.english,
    grammarPoint: sentence.grammarPoint,
  };
}

export function normalizeSentenceAnswer(value: string): string {
  return value
    .trim()
    .replace(/\s+/g, ' ')
    .replace(/[?.!,;:]+$/g, '')
    .toLocaleLowerCase('it-IT');
}

export function isSentenceAnswerCorrect(
  submittedAnswer: string,
  expectedAnswer: string,
): boolean {
  return checkSentenceAnswer(submittedAnswer, expectedAnswer) !== 'incorrect';
}

export type AnswerStatus = 'correct' | 'nearly_correct' | 'incorrect';

export function checkSentenceAnswer(
  submittedAnswer: string,
  expectedAnswer: string,
): AnswerStatus {
  const submitted = normalizeSentenceAnswer(submittedAnswer);
  const expected = normalizeSentenceAnswer(expectedAnswer);

  if (submitted === expected) {
    return 'correct';
  }

  const distance = levenshteinDistance(submitted, expected);
  if (expected.length >= 10 && distance <= 2) {
    return 'nearly_correct';
  }
  if (expected.length >= 3 && distance <= 1) {
    return 'nearly_correct';
  }

  return 'incorrect';
}

export function recordSentenceAttempt(
  stats: SentenceTrainingStats,
  sentenceId: string,
  correct: boolean,
): SentenceTrainingStats {
  const existing = stats[sentenceId] ?? {attempts: 0, correct: 0};
  return {
    ...stats,
    [sentenceId]: {
      attempts: existing.attempts + 1,
      correct: existing.correct + (correct ? 1 : 0),
    },
  };
}

export function calculateSentenceScore(stats: SentenceTrainingStats): number {
  const totals = Object.values(stats).reduce(
    (accumulator, item) => ({
      attempts: accumulator.attempts + item.attempts,
      correct: accumulator.correct + item.correct,
    }),
    {attempts: 0, correct: 0},
  );

  if (totals.attempts === 0) {
    return 0;
  }

  return Math.round((totals.correct / totals.attempts) * 100);
}

export function hasPracticedAllSentenceExercises(
  sentences: ScenarioSentenceRow[],
  completedExerciseCount: number,
): boolean {
  return sentences.length > 0 && completedExerciseCount >= sentences.length * 3;
}

export function completeSentencePhase(
  scenarioId: number,
  stats: SentenceTrainingStats,
  progress: ProgressApi,
): number {
  const score = calculateSentenceScore(stats);
  progress.setScenarioSentenceScore(scenarioId, score);
  return score;
}
