import type {ScenarioVocabularyRow} from '@app/db/vocabularyRepository';
import type {useProgressStore} from '@app/store/progressStore';
import type {useSrsStore} from '@app/store/srsStore';
import { normalizeString, levenshteinDistance } from './string';

export type VocabularyExerciseKind =
  | 'flashcard'
  | 'listening'
  | 'spelling'
  | 'multipleChoice';

export type VocabularyExercise = {
  kind: VocabularyExerciseKind;
  prompt: string;
  answer: string;
  options: string[];
};

type SrsApi = Pick<
  ReturnType<typeof useSrsStore.getState>,
  'registerItem' | 'isLearned'
>;

type ProgressApi = Pick<
  ReturnType<typeof useProgressStore.getState>,
  'setScenarioVocabularyCompleted'
>;

export function registerVocabularyTerms(
  terms: ScenarioVocabularyRow[],
  srs: SrsApi,
): void {
  terms.forEach(term =>
    srs.registerItem({
      id: term.id,
      type: 'vocabulary',
      italian: term.italian,
      english: term.english,
    }),
  );
}

export function countLearnedVocabulary(
  terms: ScenarioVocabularyRow[],
  isLearned: (id: string) => boolean,
): number {
  return terms.filter(term => isLearned(term.id)).length;
}

export function maybeCompleteVocabularyPhase(
  scenarioId: number,
  terms: ScenarioVocabularyRow[],
  srs: Pick<ReturnType<typeof useSrsStore.getState>, 'isLearned'>,
  progress: ProgressApi,
): boolean {
  if (terms.length === 0) {
    return false;
  }

  const completed = countLearnedVocabulary(terms, srs.isLearned) === terms.length;
  if (completed) {
    progress.setScenarioVocabularyCompleted(scenarioId, true);
  }

  return completed;
}

export function getNextUnlearnedTerm(
  terms: ScenarioVocabularyRow[],
  currentIndex: number,
  isLearned: (id: string) => boolean,
): {term: ScenarioVocabularyRow; index: number} | null {
  if (terms.length === 0) {
    return null;
  }

  for (let offset = 0; offset < terms.length; offset += 1) {
    const index = (currentIndex + offset) % terms.length;
    const term = terms[index];
    if (term && !isLearned(term.id)) {
      return {term, index};
    }
  }

  return null;
}

export function getVocabularyExerciseKind(
  attemptCount: number,
): VocabularyExerciseKind {
  const kinds: VocabularyExerciseKind[] = [
    'flashcard',
    'listening',
    'spelling',
    'multipleChoice',
  ];
  return kinds[attemptCount % kinds.length] ?? 'flashcard';
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
  // Filter out the correct answer from distractors
  const otherOptions = allDistractors.filter(d => d.toLowerCase() !== correct.toLowerCase());
  
  // Shuffle distractors and pick some
  const shuffledDistractors = shuffle([...new Set(otherOptions)]);
  const selectedDistractors = shuffledDistractors.slice(0, maxOptions - 1);
  
  // Combine, shuffle again so correct answer isn't always first
  return shuffle([correct, ...selectedDistractors]);
}

export function buildVocabularyExercise(
  term: ScenarioVocabularyRow,
  allTerms: ScenarioVocabularyRow[],
  attemptCount: number,
): VocabularyExercise {
  const kind = getVocabularyExerciseKind(attemptCount);
  // No need to filter otherTerms if unused

  if (kind === 'listening') {
    return {
      kind,
      prompt: 'Listen and choose the English translation.',
      answer: term.english,
      options: buildOptions(
        term.english,
        allTerms.map(t => t.english),
      ),
    };
  }

  if (kind === 'spelling') {
    return {
      kind,
      prompt: term.english,
      answer: term.italian,
      options: [],
    };
  }

  if (kind === 'multipleChoice') {
    return {
      kind,
      prompt: term.italian,
      answer: term.english,
      options: buildOptions(
        term.english,
        allTerms.map(t => t.english),
      ),
    };
  }

  return {
    kind,
    prompt: term.english,
    answer: term.italian,
    options: buildOptions(
      term.italian,
      allTerms.map(t => t.italian),
    ),
  };
}

export type AnswerStatus = 'correct' | 'nearly_correct' | 'incorrect';

export function normalizeVocabularyAnswer(value: string): string {
  return normalizeString(value);
}

export function checkVocabularyAnswer(
  submitted: string,
  expected: string,
): AnswerStatus {
  const normSubmitted = normalizeVocabularyAnswer(submitted);
  const normExpected = normalizeVocabularyAnswer(expected);

  if (normSubmitted === normExpected) {
    return 'correct';
  }

  // Levenshtein distance of 1 is "nearly correct" for words >= 3 chars
  if (normExpected.length >= 3 && levenshteinDistance(normSubmitted, normExpected) === 1) {
    return 'nearly_correct';
  }

  return 'incorrect';
}
