import {scenarios} from '../src/data/scenarios.ts';
import {courseWordList, wordsForCategory, type CourseWordCategory} from '../src/data/courseWordList.ts';

function normalize(value: string): string {
  return value
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLocaleLowerCase('it-IT');
}

function scenarioText(scenario: (typeof scenarios)[number]): string {
  return normalize([
    ...scenario.vocabulary.map(item => item.italian),
    ...scenario.phrases.map(item => item.italian),
    ...scenario.sentences.map(item => item.italian),
  ].join(' | '));
}

function findIssues(text: string): string[] {
  const issues: string[] = [];
  if (/\b(\p{L}+)\s+\1\b/iu.test(text)) {
    issues.push('repeated adjacent word');
  }
  if (/\s{2,}/.test(text)) {
    issues.push('double whitespace');
  }
  if (/Dov'è\s+(bagagli|documento|informazione|acqua|pane)\b/i.test(text)) {
    issues.push('possible missing article after Dov\'e');
  }
  if (/Mi devo \w+arsi\b/i.test(text)) {
    issues.push('reflexive infinitive should attach pronoun or use mi devo + infinitive stem');
  }
  if (!/[A-Za-zÀ-ÿ]/.test(text)) {
    issues.push('empty or non-text exercise');
  }
  return issues;
}

const allTargetWords = new Set<string>();
for (const category of Object.keys(courseWordList) as CourseWordCategory[]) {
  for (const word of wordsForCategory(category)) {
    allTargetWords.add(normalize(word));
  }
}

const coveredTargetWords = new Set<string>();
const coverageByScenario: Array<{id: number; title: string; covered: number; totalForCategory: number}> = [];

for (const scenario of scenarios) {
  const text = scenarioText(scenario);
  const category = scenario.category as CourseWordCategory;
  const categoryWords = category in courseWordList ? wordsForCategory(category) : [];
  const coveredForScenario = categoryWords.filter(word => text.includes(normalize(word)));

  for (const word of allTargetWords) {
    if (text.includes(word)) {
      coveredTargetWords.add(word);
    }
  }

  coverageByScenario.push({
    id: scenario.id,
    title: scenario.title,
    covered: coveredForScenario.length,
    totalForCategory: categoryWords.length,
  });

  console.log(`\n# ${scenario.id} ${scenario.title} [${scenario.category}]`);

  // Difficulty Warnings
  const checkDifficulty = () => {
    const warnings: string[] = [];

    // Vocabulary
    if (scenario.vocabulary.length >= 6) {
      const first3 = scenario.vocabulary.slice(0, 3).reduce((sum, v) => sum + v.italian.length, 0) / 3;
      const last3 = scenario.vocabulary.slice(-3).reduce((sum, v) => sum + v.italian.length, 0) / 3;
      if (first3 > last3) warnings.push(`Vocabulary difficulty warning: first 3 avg length ${first3.toFixed(1)} > last 3 avg length ${last3.toFixed(1)}`);
    }

    // Phrases
    if (scenario.phrases.length >= 6) {
      const wordCount = (s: string) => s.trim().split(/\s+/).length;
      const first3 = scenario.phrases.slice(0, 3).reduce((sum, p) => sum + wordCount(p.italian), 0) / 3;
      const last3 = scenario.phrases.slice(-3).reduce((sum, p) => sum + wordCount(p.italian), 0) / 3;
      if (first3 > last3) warnings.push(`Phrase difficulty warning: first 3 avg words ${first3.toFixed(1)} > last 3 avg words ${last3.toFixed(1)}`);
    }

    // Sentences
    if (scenario.sentences.length >= 6) {
      const clauseCount = (s: string) => {
        const verbs = s.match(/\b(?:sono|sei|è|siamo|siete|sono|ho|hai|ha|abbiamo|avete|hanno|vado|vai|va|andiamo|andate|vanno|faccio|fai|fa|facciamo|fate|fanno|posso|puoi|può|possiamo|potete|possono|devo|devi|deve|dobbiamo|dovete|devono|voglio|vuoi|vuole|vogliamo|volete|vogliono|\w+are|\w+ere|\w+ire)\b/gi);
        return verbs ? verbs.length : 1;
      };
      const first3 = scenario.sentences.slice(0, 3).reduce((sum, s) => sum + clauseCount(s.italian), 0) / 3;
      const last3 = scenario.sentences.slice(-3).reduce((sum, s) => sum + clauseCount(s.italian), 0) / 3;
      if (first3 > last3) warnings.push(`Sentence difficulty warning: first 3 avg clauses ${first3.toFixed(1)} > last 3 avg clauses ${last3.toFixed(1)}`);
    }
    return warnings;
  };

  const diffWarnings = checkDifficulty();
  if (diffWarnings.length > 0) {
    console.log(`DIFFICULTY WARNINGS:`);
    diffWarnings.forEach(w => console.log(`  - ${w}`));
  }

  for (const phrase of scenario.phrases) {
    const issues = findIssues(phrase.italian);
    console.log(`PHRASE ${phrase.id}: ${phrase.italian}${issues.length ? ` [FLAG: ${issues.join(', ')}]` : ''}`);
  }
  for (const sentence of scenario.sentences) {
    const issues = findIssues(sentence.italian);
    console.log(`SENTENCE ${sentence.id}: ${sentence.italian}${issues.length ? ` [FLAG: ${issues.join(', ')}]` : ''}`);
  }
}

const flagged = scenarios.flatMap(scenario => [
  ...scenario.phrases.map(item => ({scenario, kind: 'phrase', text: item.italian, issues: findIssues(item.italian)})),
  ...scenario.sentences.map(item => ({scenario, kind: 'sentence', text: item.italian, issues: findIssues(item.italian)})),
]).filter(item => item.issues.length > 0);

console.log('\n## Coverage By Scenario');
for (const item of coverageByScenario) {
  console.log(`${item.id}. ${item.title}: ${item.covered}/${item.totalForCategory} category words visible in this scenario`);
}

console.log('\n## Summary');
console.log(`Scenarios: ${scenarios.length}`);
console.log(`Target distinct Italian words: ${allTargetWords.size}`);
console.log(`Covered target distinct Italian words: ${coveredTargetWords.size}`);
console.log(`Flagged exercises: ${flagged.length}`);

if (flagged.length > 0) {
  for (const item of flagged) {
    console.log(`[${item.scenario.id}] ${item.kind}: ${item.text} -> ${item.issues.join(', ')}`);
  }
  process.exitCode = 1;
}
