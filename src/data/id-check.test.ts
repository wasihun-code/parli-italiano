import { describe, it } from 'vitest';
import { scenarios } from './scenarios';

describe('ID Format Investigation', () => {
  it('should print the actual IDs generated for Scenario 22', () => {
    const s22 = scenarios.find(s => s.id === 22);
    if (s22) {
      process.stdout.write('\n--- SCENARIO 22 VOCABULARY IDS ---\n');
      s22.vocabulary.slice(0, 10).forEach((v, i) => {
        process.stdout.write(`${i+1}. ID: "${v.id}" | Italian: "${v.italian}"\n`);
      });
      process.stdout.write('\n');
    }
  });
});
