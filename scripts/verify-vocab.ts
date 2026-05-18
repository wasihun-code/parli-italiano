import {scenarios} from '../src/data/scenarios.ts';

const untranslated = new Set<string>();

for (const scenario of scenarios) {
  for (const v of scenario.vocabulary) {
    if (v.italian === v.english && v.italian.length > 2) {
      untranslated.add(v.italian);
    }
  }
}

const list = Array.from(untranslated).sort();
console.log(`Found ${list.length} unique untranslated terms:`);
console.log(list.join(', '));
