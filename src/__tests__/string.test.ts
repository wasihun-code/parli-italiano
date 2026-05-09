/**
 * Unit tests for string utilities (shared logic from src/utils/string.ts)
 */
import { describe, it, expect } from 'vitest';
import { levenshteinDistance, normalizeString } from '@shared/utils/string';

describe('levenshteinDistance', () => {
  it('returns 0 for identical strings', () => {
    expect(levenshteinDistance('ciao', 'ciao')).toBe(0);
  });

  it('counts insertions', () => {
    expect(levenshteinDistance('cio', 'ciao')).toBe(1);
  });

  it('counts deletions', () => {
    expect(levenshteinDistance('ciaoo', 'ciao')).toBe(1);
  });

  it('counts substitutions', () => {
    expect(levenshteinDistance('chao', 'ciao')).toBe(1);
  });

  it('handles empty strings', () => {
    expect(levenshteinDistance('', 'ciao')).toBe(4);
    expect(levenshteinDistance('ciao', '')).toBe(4);
    expect(levenshteinDistance('', '')).toBe(0);
  });

  it('handles multi-character differences', () => {
    expect(levenshteinDistance('arrivederci', 'buongiorno')).toBeGreaterThan(5);
  });
});

describe('normalizeString', () => {
  it('trims whitespace', () => {
    expect(normalizeString('  ciao  ')).toBe('ciao');
  });

  it('converts to lowercase', () => {
    expect(normalizeString('CIAO')).toBe('ciao');
  });

  it('strips accents', () => {
    expect(normalizeString('città')).toBe('citta');
    expect(normalizeString('perché')).toBe('perche');
  });

  it('removes punctuation', () => {
    expect(normalizeString('ciao!')).toBe('ciao');
    expect(normalizeString('va bene?')).toBe('va bene');
  });

  it('collapses multiple spaces', () => {
    expect(normalizeString('per  favore')).toBe('per favore');
  });

  it('handles combined transformations', () => {
    expect(normalizeString('  Città, per favore!  ')).toBe('citta per favore');
  });
});
