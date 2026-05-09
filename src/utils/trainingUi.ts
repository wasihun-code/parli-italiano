import type {SrsItemType, useSrsStore} from '@shared/store/srsStore';
import type {CSSProperties} from 'react';
import {colors} from '@shared/theme/colors';
import {normalizeString} from './string';

export function shuffle<T>(items: T[]): T[] {
  const result = [...items];
  for (let index = result.length - 1; index > 0; index -= 1) {
    const swapIndex = Math.floor(Math.random() * (index + 1));
    [result[index], result[swapIndex]] = [result[swapIndex] as T, result[index] as T];
  }
  return result;
}

export function pickRandomDistractors(
  correct: string,
  candidates: string[],
  count = 3,
): string[] {
  const normalizedCorrect = correct.trim().toLocaleLowerCase('it-IT');
  const unique = Array.from(
    new Set(
      candidates
        .map(candidate => candidate.trim())
        .filter(
          candidate =>
            candidate.length > 0 &&
            candidate.toLocaleLowerCase('it-IT') !== normalizedCorrect,
        ),
    ),
  );
  return shuffle(unique).slice(0, count);
}

export function buildShuffledOptions(
  correct: string,
  candidates: string[],
  maxOptions = 4,
): string[] {
  return shuffle([
    correct,
    ...pickRandomDistractors(correct, candidates, maxOptions - 1),
  ]);
}

export function masterSrsItems(
  items: Array<{id: string; type: SrsItemType; italian: string; english: string}>,
  srs: ReturnType<typeof useSrsStore.getState>,
): void {
  items.forEach(item => {
    srs.registerItem(item);
    for (let count = 0; count < 3; count += 1) {
      srs.recordAnswer(item.id, true);
    }
  });
}

export function isLearnedByIdOrItalian(
  item: {id: string; italian: string},
  srs: ReturnType<typeof useSrsStore.getState>,
): boolean {
  if (srs.isLearned(item.id)) {
    return true;
  }

  const normalizedItalian = normalizeString(item.italian);
  return Object.values(srs.items).some(
    existing =>
      existing.learned &&
      normalizeString(existing.italian) === normalizedItalian,
  );
}

export function progressBar(): CSSProperties {
  return {
    height: 12,
    width: '100%',
    backgroundColor: 'rgba(78, 52, 46, 0.1)',
    borderRadius: 999,
    overflow: 'hidden',
    border: '1px solid rgba(78, 52, 46, 0.05)',
    margin: '8px 0'
  };
}

export function progressFill(progress: number): CSSProperties {
  const clamped = Math.max(0, Math.min(1, progress));
  return {
    height: '100%',
    width: `${clamped * 100}%`,
    backgroundColor: colors.accent,
    transition: 'width 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)',
    borderRadius: 999
  };
}

export function trainingFooterStyle(): CSSProperties {
  return {
    flexShrink: 0,
    paddingTop: 24,
    paddingBottom: 8,
    backgroundColor: 'transparent',
  };
}

export function feedbackCardStyle(status: 'correct' | 'nearly_correct' | 'incorrect'): CSSProperties {
  const isCorrect = status === 'correct';
  const isNearlyCorrect = status === 'nearly_correct';
  
  let bg: string = 'rgba(212, 163, 115, 0.15)'; // Caramel tint for correct
  let color: string = colors.primary; // Espresso text
  let border: string = colors.accent;

  if (isNearlyCorrect) {
    bg = 'rgba(227, 155, 20, 0.1)';
    color = colors.warning;
    border = colors.warning;
  } else if (!isCorrect) {
    bg = 'rgba(141, 110, 99, 0.1)'; // Cappuccino tint for incorrect
    color = colors.primary;
    border = colors.secondary;
  }

  return {
    padding: 24,
    borderRadius: 20,
    backgroundColor: bg,
    color: color,
    fontWeight: 900,
    border: `2px solid ${border}`,
    textAlign: 'center',
    fontSize: 20,
    boxShadow: '0 4px 12px rgba(0,0,0,0.05)',
  };
}
