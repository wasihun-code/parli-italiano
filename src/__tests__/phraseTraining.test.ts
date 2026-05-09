/**
 * Unit tests for phraseTraining utilities (shared logic from src/utils/phraseTraining.ts)
 */
import { describe, it, expect } from 'vitest';
import {
  splitPhraseWords,
  buildFillBlankItalian,
  buildAssemblyWords,
  getPhraseExerciseKind,
  checkPhraseAnswer,
  isPhraseAnswerCorrect,
  calculatePhraseScore,
  recordPhraseAttempt,
} from '@shared/utils/phraseTraining';

describe('getPhraseExerciseKind', () => {
  it('cycles through listenRepeat, fillBlank, assembly', () => {
    expect(getPhraseExerciseKind(0)).toBe('listenRepeat');
    expect(getPhraseExerciseKind(1)).toBe('fillBlank');
    expect(getPhraseExerciseKind(2)).toBe('assembly');
    expect(getPhraseExerciseKind(3)).toBe('listenRepeat');
  });
});

describe('splitPhraseWords', () => {
  it('splits on whitespace', () => {
    expect(splitPhraseWords('Vorrei un caffè')).toEqual(['Vorrei', 'un', 'caffè']);
  });

  it('handles leading/trailing whitespace', () => {
    expect(splitPhraseWords('  ciao  ')).toEqual(['ciao']);
  });
});

describe('buildFillBlankItalian', () => {
  it('blanks out the longest word', () => {
    // 'appuntamento' (12 chars) is clearly the longest here
    const { displayItalian, missingWord } = buildFillBlankItalian('Ho un appuntamento con il dottore.');
    expect(missingWord).toBe('appuntamento');
    expect(displayItalian).toContain('____');
    expect(displayItalian).not.toContain('appuntamento');
  });

  it('works on short phrases', () => {
    const { displayItalian, missingWord } = buildFillBlankItalian('Ciao bella');
    expect(missingWord).toBeDefined();
    expect(displayItalian).toContain('____');
  });
});


describe('buildAssemblyWords', () => {
  it('reverses a two-word phrase', () => {
    expect(buildAssemblyWords('Ciao bella')).toEqual(['bella', 'Ciao']);
  });

  it('interleaves odds/evens for longer phrases', () => {
    // Words: 0=A 1=B 2=C → evens=[A,C] odds=[B] → result=[B,A,C]
    const result = buildAssemblyWords('A B C');
    expect(result).toEqual(['B', 'A', 'C']);
  });
});

describe('checkPhraseAnswer', () => {
  it('returns correct for exact match', () => {
    expect(checkPhraseAnswer('grazie', 'grazie')).toBe('correct');
  });

  it('returns correct when normalised match (accent stripped)', () => {
    expect(checkPhraseAnswer('citta', 'città')).toBe('correct');
  });

  it('returns nearly_correct for minor 1-char typo', () => {
    expect(checkPhraseAnswer('grazia', 'grazie')).toBe('nearly_correct');
  });

  it('returns nearly_correct for 2-char typo in long phrase', () => {
    expect(checkPhraseAnswer('buongiorni amico', 'buongiorno amico')).toBe('nearly_correct');
  });

  it('returns incorrect for large differences', () => {
    expect(checkPhraseAnswer('arrivederci', 'buongiorno')).toBe('incorrect');
  });
});

describe('isPhraseAnswerCorrect', () => {
  it('returns true for correct and nearly_correct', () => {
    expect(isPhraseAnswerCorrect('grazie', 'grazie')).toBe(true);
    expect(isPhraseAnswerCorrect('grazia', 'grazie')).toBe(true);
  });

  it('returns false for incorrect', () => {
    expect(isPhraseAnswerCorrect('arrivederci', 'buongiorno')).toBe(false);
  });
});

describe('calculatePhraseScore', () => {
  it('returns 0 for empty stats', () => {
    expect(calculatePhraseScore({})).toBe(0);
  });

  it('calculates percentage correctly', () => {
    let stats = {};
    stats = recordPhraseAttempt(stats, 'p1', true);
    stats = recordPhraseAttempt(stats, 'p2', true);
    stats = recordPhraseAttempt(stats, 'p3', false);
    // 2 correct / 3 attempts = 67%
    expect(calculatePhraseScore(stats)).toBe(67);
  });

  it('returns 100 for all correct', () => {
    let stats = {};
    stats = recordPhraseAttempt(stats, 'p1', true);
    stats = recordPhraseAttempt(stats, 'p2', true);
    expect(calculatePhraseScore(stats)).toBe(100);
  });
});

describe('recordPhraseAttempt', () => {
  it('initialises stats for new phrases', () => {
    const stats = recordPhraseAttempt({}, 'p1', true);
    expect(stats['p1']).toEqual({ attempts: 1, correct: 1 });
  });

  it('accumulates multiple attempts', () => {
    let stats = {};
    stats = recordPhraseAttempt(stats, 'p1', true);
    stats = recordPhraseAttempt(stats, 'p1', false);
    expect(stats['p1']).toEqual({ attempts: 2, correct: 1 });
  });
});
