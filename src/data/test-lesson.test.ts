import { describe, it, expect } from 'vitest';
import { scenarios } from './scenarios';

describe('Seeding Evidence', () => {
  it('should show the production counts for Scenario 22', () => {
    const s22 = scenarios.find(s => s.id === 22);
    if (s22) {
      process.stdout.write(`\n[EVIDENCE] scenarioId: ${s22.id}\n`);
      process.stdout.write(`[EVIDENCE] vocabulary count: ${s22.vocabulary.length}\n`);
      process.stdout.write(`[EVIDENCE] First Vocab ID: ${s22.vocabulary[0]?.id}\n`);
      process.stdout.write(`[EVIDENCE] phrase count: ${s22.phrases.length}\n`);
      process.stdout.write(`[EVIDENCE] sentence count: ${s22.sentences.length}\n\n`);
    } else {
      process.stdout.write('[EVIDENCE] Scenario 22 not found in scenarios array\n');
    }
  });
});
