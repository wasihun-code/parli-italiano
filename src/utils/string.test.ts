import { levenshteinDistance, normalizeString } from './string';

describe('string utils', () => {
  describe('levenshteinDistance', () => {
    it('calculates the correct distance between identical strings', () => {
      expect(levenshteinDistance('hello', 'hello')).toBe(0);
    });

    it('calculates distance for insertions', () => {
      expect(levenshteinDistance('hello', 'helloo')).toBe(1);
    });

    it('calculates distance for deletions', () => {
      expect(levenshteinDistance('hello', 'hell')).toBe(1);
    });

    it('calculates distance for substitutions', () => {
      expect(levenshteinDistance('hello', 'hallo')).toBe(1);
    });

    it('handles empty strings', () => {
      expect(levenshteinDistance('', 'hello')).toBe(5);
      expect(levenshteinDistance('hello', '')).toBe(5);
      expect(levenshteinDistance('', '')).toBe(0);
    });
  });

  describe('normalizeString', () => {
    it('trims whitespace', () => {
      expect(normalizeString('  hello  ')).toBe('hello');
    });

    it('lowercases strings', () => {
      expect(normalizeString('HELLO')).toBe('hello');
    });

    it('removes accents', () => {
      expect(normalizeString('àèìòù')).toBe('aeiou');
      expect(normalizeString('città')).toBe('citta');
    });

    it('removes punctuation', () => {
      expect(normalizeString('hello, world!')).toBe('hello world');
      expect(normalizeString('what?')).toBe('what');
    });

    it('consolidates whitespace', () => {
      expect(normalizeString('hello   world')).toBe('hello world');
    });

    it('combines all normalizations', () => {
      expect(normalizeString('  CITTÀ, per favore!  ')).toBe('citta per favore');
    });
  });
});
