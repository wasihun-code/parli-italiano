import fs from 'fs';
import path from 'path';
import { loadProductionScenarioData } from './corpusLoader';
import { scenarios } from './scenarios';
import { describe, it } from 'vitest';

describe('Forensic Trace of s22-v2 and s22-v3', () => {
  it('should trace IDs through the pipeline', async () => {
    const vocabJsonPath = 'src/data/exports/accommodation/apartment_key_pickup/accommodation_apartment_key_pickup_vocabulary.json';
    const rawJson = JSON.parse(fs.readFileSync(vocabJsonPath, 'utf-8'));
    
    process.stdout.write('\n--- 1. RAW JSON (fs.readFileSync) ---\n');
    process.stdout.write(`JSON loaded count: ${rawJson.length}\n`);
    const v2Json = rawJson.find(i => i.id === 's22-v2');
    const v3Json = rawJson.find(i => i.id === 's22-v3');
    process.stdout.write(`s22-v2 in JSON? ${!!v2Json} (${v2Json?.italian})\n`);
    process.stdout.write(`s22-v3 in JSON? ${!!v3Json} (${v3Json?.italian})\n`);

    process.stdout.write('\n--- 2. LOADER (loadProductionScenarioData) ---\n');
    const loadedData = loadProductionScenarioData(22);
    if (loadedData) {
      process.stdout.write(`Loader count: ${loadedData.vocabulary.length}\n`);
      const v2Loaded = loadedData.vocabulary.find(i => i.id === 's22-v2');
      const v3Loaded = loadedData.vocabulary.find(i => i.id === 's22-v3');
      process.stdout.write(`s22-v2 in Loader? ${!!v2Loaded}\n`);
      process.stdout.write(`s22-v3 in Loader? ${!!v3Loaded}\n`);
    } else {
      process.stdout.write('Loader returned null\n');
    }

    process.stdout.write('\n--- 3. REGISTRY (scenarios array) ---\n');
    const s22 = scenarios.find(s => s.id === 22);
    if (s22) {
      process.stdout.write(`Registry count: ${s22.vocabulary.length}\n`);
      const v2Reg = s22.vocabulary.find(i => i.id === 's22-v2');
      const v3Reg = s22.vocabulary.find(i => i.id === 's22-v3');
      process.stdout.write(`s22-v2 in Registry? ${!!v2Reg}\n`);
      process.stdout.write(`s22-v3 in Registry? ${!!v3Reg}\n`);
      
      if (!v2Reg) {
         // Check for duplicate Italian text
         const portoneItems = s22.vocabulary.filter(i => i.italian === 'portone');
         process.stdout.write(`Count of items with text 'portone': ${portoneItems.length}\n`);
         if (portoneItems.length > 0) {
            process.stdout.write(`Winning item ID: ${portoneItems[0].id}\n`);
         }
      }
    }
  });
});
