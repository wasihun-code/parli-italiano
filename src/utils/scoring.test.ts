import {
  hasPassedFoundation,
  hasPassedPhraseTraining,
  hasPassedSentenceTraining,
  percentageScore,
} from './scoring';

describe('scoring utilities', () => {
  it('calculates whole-number percentage scores', () => {
    expect(percentageScore(9, 10)).toBe(90);
    expect(percentageScore(2, 3)).toBe(67);
    expect(percentageScore(0, 0)).toBe(0);
  });

  it('applies phase pass thresholds', () => {
    expect(hasPassedFoundation(90)).toBe(true);
    expect(hasPassedFoundation(89)).toBe(false);
    expect(hasPassedPhraseTraining(85)).toBe(true);
    expect(hasPassedPhraseTraining(84)).toBe(false);
    expect(hasPassedSentenceTraining(80)).toBe(true);
    expect(hasPassedSentenceTraining(79)).toBe(false);
  });
});
