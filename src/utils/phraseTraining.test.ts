import {
  splitPhraseWords,
  buildFillBlankItalian,
  buildAssemblyWords,
  checkPhraseAnswer,
  calculatePhraseScore,
  recordPhraseAttempt,
} from './phraseTraining';

describe('phraseTraining utils', () => {
  describe('splitPhraseWords', () => {
    it('splits phrases into words without punctuation attached', () => {
      expect(splitPhraseWords('Ciao, come stai?')).toEqual(['Ciao,', 'come', 'stai?']);
    });
  });

  describe('buildFillBlankItalian', () => {
    it('replaces the longest word with blanks', () => {
      const result = buildFillBlankItalian('Vorrei una mela, per favore.');
      expect(result.missingWord).toBe('Vorrei');
      expect(result.displayItalian).toBe('____ una mela, per favore.');
    });
  });

  describe('buildAssemblyWords', () => {
    it('scrambles words by alternating evens and odds', () => {
      const result = buildAssemblyWords('Il gatto mangia il pesce');
      // indices: 0: Il, 1: gatto, 2: mangia, 3: il, 4: pesce
      // odds: gatto, il
      // evens: Il, mangia, pesce
      expect(result).toEqual(['gatto', 'il', 'Il', 'mangia', 'pesce']);
    });

    it('reverses very short phrases', () => {
      expect(buildAssemblyWords('Ciao bella')).toEqual(['bella', 'Ciao']);
    });
  });

  describe('checkPhraseAnswer', () => {
    it('returns correct for exact matches', () => {
      expect(checkPhraseAnswer('ciao', 'ciao')).toBe('correct');
    });

    it('returns nearly_correct for minor typos in long phrases', () => {
      // 10+ chars, 1-2 distance
      expect(checkPhraseAnswer('buongiorna', 'buongiorno')).toBe('nearly_correct');
    });

    it('returns incorrect for major mistakes', () => {
      expect(checkPhraseAnswer('arrivederci', 'buongiorno')).toBe('incorrect');
    });
  });

  describe('scoring', () => {
    it('calculates score correctly', () => {
      let stats = {};
      stats = recordPhraseAttempt(stats, 'p1', true);
      stats = recordPhraseAttempt(stats, 'p2', false);
      stats = recordPhraseAttempt(stats, 'p2', true);

      // Total attempts: 3, Total correct: 2
      expect(calculatePhraseScore(stats)).toBe(67);
    });

    it('returns 0 for no attempts', () => {
      expect(calculatePhraseScore({})).toBe(0);
    });
  });
});
