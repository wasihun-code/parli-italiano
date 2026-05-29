import { describe, it } from 'vitest';
import { db, setupDatabase } from '../lib/db';

describe('Forensic DB Investigation', () => {
  it('should query the actual Dexie records', async () => {
    await setupDatabase();
    
    const ids = ['s22-v2', 's22-v3', 's22-v15'];
    process.stdout.write('\n--- INDIVIDUAL LOOKUPS ---\n');
    for (const id of ids) {
      const record = await db.scenario_vocabulary.get(id);
      process.stdout.write(`\nID: ${id}\n`);
      process.stdout.write(`Found: ${!!record}\n`);
      if (record) {
        process.stdout.write(`Object: ${JSON.stringify(record, null, 2)}\n`);
      }
    }

    process.stdout.write('\n--- SCENARIO 22 STATS ---\n');
    const count = await db.scenario_vocabulary
      .where("scenario_id")
      .equals(22)
      .count();
    process.stdout.write(`\nTotal Scenario 22 vocabulary records: ${count}\n`);

    process.stdout.write('\n--- FIRST 20 IDs FOR SCENARIO 22 ---\n');
    const first20 = await db.scenario_vocabulary
      .where("scenario_id")
      .equals(22)
      .limit(20)
      .toArray();
    
    first20.forEach((r, i) => {
      process.stdout.write(`${i+1}. ${r.id} (${r.italian})\n`);
    });
    process.stdout.write('\n');
  });
});
