import {italianToEnglish} from '../src/data/translations.ts';
import * as fs from 'fs';

const normalized: Record<string, string> = {};

for (const [it, en] of Object.entries(italianToEnglish)) {
  const key = it.toLowerCase();
  // Prefer the more detailed translation if we have duplicates
  if (!normalized[key] || en.length > normalized[key].length) {
    normalized[key] = en;
  }
}

const sortedKeys = Object.keys(normalized).sort();
const content = `export const italianToEnglish: Record<string, string> = {\n${sortedKeys.map(k => `  "${k}": ${JSON.stringify(normalized[k])}`).join(',\n')}\n};\n`;

fs.writeFileSync('src/data/translations.ts', content);
console.log(`Normalized ${sortedKeys.length} terms.`);
