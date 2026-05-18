import type {ScenarioPhraseRow} from '@app/db/vocabularyRepository';
import type {useProgressStore} from '@app/store/progressStore';
import type {useSrsStore} from '@app/store/srsStore';
import { normalizeString, levenshteinDistance } from './string';

export type PhraseExerciseKind = 'speaking' | 'fillBlank' | 'assembly' | 'multipleChoice' | 'dictation';

export type PhraseExercise = {
  kind: PhraseExerciseKind;
  phraseId: string;
  prompt: string;
  answer: string;
  displayItalian?: string;
  missingWord?: string;
  assemblyWords: string[];
  options: string[];
};

export type PhraseAttemptStats = {
  attempts: number;
  correct: number;
};

export type PhraseTrainingStats = Record<string, PhraseAttemptStats>;

type SrsApi = Pick<ReturnType<typeof useSrsStore.getState>, 'registerItem' | 'isLearned'>;

type ProgressApi = Pick<
  ReturnType<typeof useProgressStore.getState>,
  'setScenarioPhraseScore'
>;

export function sortPhrasesByDifficulty<T extends {italian: string}>(
  phrases: T[],
): T[] {
  return [...phrases].sort((a, b) => {
    // Primary: number of words in Italian phrase (split by spaces)
    const wordsA = a.italian.trim().split(/\s+/).length;
    const wordsB = b.italian.trim().split(/\s+/).length;
    if (wordsA !== wordsB) return wordsA - wordsB;

    // Secondary: total character length
    if (a.italian.length !== b.italian.length) {
      return a.italian.length - b.italian.length;
    }

    return a.italian.localeCompare(b.italian);
  });
}

export function registerPhraseItems(
  phrases: ScenarioPhraseRow[],
  srs: SrsApi,
): void {
  phrases.forEach(phrase =>
    srs.registerItem({
      id: phrase.id,
      type: 'phrase',
      italian: phrase.italian,
      english: phrase.english,
    }),
  );
}

export function getPhraseExerciseKind(
  attemptCount: number,
): PhraseExerciseKind {
  const kinds: PhraseExerciseKind[] = ['multipleChoice', 'assembly', 'fillBlank', 'dictation', 'speaking'];
  return kinds[attemptCount % kinds.length] ?? 'multipleChoice';
}

function shuffle<T>(array: T[]): T[] {
  const result = [...array];
  for (let i = result.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [result[i], result[j]] = [result[j] as T, result[i] as T];
  }
  return result;
}

function buildOptions(
  correct: string,
  allDistractors: string[],
  maxOptions = 4,
): string[] {
  const otherOptions = allDistractors.filter(d => d.toLowerCase() !== correct.toLowerCase());
  const shuffledDistractors = shuffle([...new Set(otherOptions)]);
  const selectedDistractors = shuffledDistractors.slice(0, maxOptions - 1);
  return shuffle([correct, ...selectedDistractors]);
}

export function getNextUnlearnedPhrase(
  phrases: ScenarioPhraseRow[],
  currentIndex: number,
  isLearned: (id: string) => boolean,
): {phrase: ScenarioPhraseRow; index: number} | null {
  if (phrases.length === 0) return null;

  for (let offset = 0; offset < phrases.length; offset += 1) {
    const index = (currentIndex + offset) % phrases.length;
    const phrase = phrases[index];
    if (phrase && !isLearned(phrase.id)) {
      return {phrase, index};
    }
  }

  return null;
}

export function splitPhraseWords(phrase: string): string[] {
  return phrase.trim().split(/\s+/).filter(Boolean);
}

function stripPunctuation(word: string): string {
  return word.replace(/^[^\p{L}\p{N}]+|[^\p{L}\p{N}]+$/gu, '');
}

function chooseMissingWord(words: string[]): {index: number; word: string} {
  const ranked = words
    .map((word, index) => ({index, word: stripPunctuation(word)}))
    .filter(candidate => candidate.word.length > 1)
    .sort((left, right) => right.word.length - left.word.length);

  return ranked[0] ?? {index: 0, word: stripPunctuation(words[0] ?? '')};
}

export function buildFillBlankItalian(phrase: string): {
  displayItalian: string;
  missingWord: string;
} {
  const words = splitPhraseWords(phrase);
  const missing = chooseMissingWord(words);
  const displayItalian = words
    .map((word, index) => (index === missing.index ? '____' : word))
    .join(' ');

  return {
    displayItalian,
    missingWord: missing.word,
  };
}

export function buildAssemblyWords(phrase: string): string[] {
  const words = splitPhraseWords(phrase);
  if (words.length <= 2) return [...words].reverse();
  const evens = words.filter((_word, index) => index % 2 === 0);
  const odds = words.filter((_word, index) => index % 2 === 1);
  return [...odds, ...evens];
}

export function buildPhraseExercise(
  phrase: ScenarioPhraseRow,
  allPhrases: ScenarioPhraseRow[],
  attemptCount: number,
): PhraseExercise {
  const kind = getPhraseExerciseKind(attemptCount);

  if (kind === 'multipleChoice') {
    return {
      kind,
      phraseId: phrase.id,
      prompt: phrase.english,
      answer: phrase.italian,
      assemblyWords: [],
      options: buildOptions(phrase.italian, allPhrases.map(p => p.italian)),
    };
  }

  if (kind === 'fillBlank') {
    const blank = buildFillBlankItalian(phrase.italian);
    return {
      kind,
      phraseId: phrase.id,
      prompt: phrase.english,
      answer: blank.missingWord,
      displayItalian: blank.displayItalian,
      missingWord: blank.missingWord,
      assemblyWords: [],
      options: [],
    };
  }

  if (kind === 'assembly') {
    return {
      kind,
      phraseId: phrase.id,
      prompt: phrase.english,
      answer: phrase.italian,
      assemblyWords: buildAssemblyWords(phrase.italian),
      options: [],
    };
  }

  if (kind === 'dictation') {
    return {
      kind,
      phraseId: phrase.id,
      prompt: 'Listen and write the Italian phrase.',
      answer: phrase.italian,
      assemblyWords: [],
      options: [],
    };
  }

  // speaking
  return {
    kind: 'speaking',
    phraseId: phrase.id,
    prompt: phrase.english,
    answer: phrase.italian,
    displayItalian: phrase.italian,
    assemblyWords: [],
    options: [],
  };
}

export function normalizePhraseAnswer(value: string): string {
  return normalizeString(value);
}

export type AnswerStatus = 'correct' | 'nearly_correct' | 'incorrect';

export function checkPhraseAnswer(
  submitted: string,
  expected: string,
): AnswerStatus {
  const normSubmitted = normalizePhraseAnswer(submitted);
  const normExpected = normalizePhraseAnswer(expected);

  if (normSubmitted === normExpected) return 'correct';

  const dist = levenshteinDistance(normSubmitted, normExpected);
  if (normExpected.length >= 10 && dist <= 2) return 'nearly_correct';
  if (normExpected.length >= 3 && dist === 1) return 'nearly_correct';

  return 'incorrect';
}

export function isPhraseAnswerCorrect(
  submittedAnswer: string,
  expectedAnswer: string,
): boolean {
  return checkPhraseAnswer(submittedAnswer, expectedAnswer) !== 'incorrect';
}

export function recordPhraseAttempt(
  stats: PhraseTrainingStats,
  phraseId: string,
  correct: boolean,
): PhraseTrainingStats {
  const existing = stats[phraseId] ?? {attempts: 0, correct: 0};
  return {
    ...stats,
    [phraseId]: {
      attempts: existing.attempts + 1,
      correct: existing.correct + (correct ? 1 : 0),
    },
  };
}

export function calculatePhraseScore(stats: PhraseTrainingStats): number {
  const totals = Object.values(stats).reduce(
    (accumulator, item) => ({
      attempts: accumulator.attempts + item.attempts,
      correct: accumulator.correct + item.correct,
    }),
    {attempts: 0, correct: 0},
  );

  if (totals.attempts === 0) return 0;
  return Math.round((totals.correct / totals.attempts) * 100);
}

export function hasPracticedAllPhraseExercises(
  phrases: ScenarioPhraseRow[],
  completedExerciseCount: number,
): boolean {
  return phrases.length > 0 && completedExerciseCount >= phrases.length * 3;
}

export function completePhrasePhase(
  scenarioId: number,
  stats: PhraseTrainingStats,
  progress: ProgressApi,
): number {
  const score = calculatePhraseScore(stats);
  progress.setScenarioPhraseScore(scenarioId, score);
  return score;
}
