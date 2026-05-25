
import fs from 'fs';
import path from 'path';
import { scenarios } from '../src/data/scenarios';

const EXPORT_DIR = path.join(process.cwd(), 'src/data/exports2');

if (!fs.existsSync(EXPORT_DIR)) {
  fs.mkdirSync(EXPORT_DIR, { recursive: true });
}

function slug(input: string): string {
  return input
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '_')
    .replace(/^_+|_+$/g, '');
}

function shuffle<T>(array: T[]): T[] {
  return [...array].sort(() => Math.random() - 0.5);
}

function getDistractors(correct: string, allPossible: string[], count: number = 3): string[] {
  const others = allPossible.filter(item => item !== correct);
  const shuffled = shuffle(others);
  return shuffled.slice(0, count);
}

function generateQuestions() {
  for (const scenario of scenarios) {
    const categorySlug = slug(scenario.category);
    const scenarioSlug = slug(scenario.title);

    const vocabList = scenario.vocabulary;
    const phraseList = scenario.phrases;
    const sentenceList = scenario.sentences;

    const allItalianVocab = vocabList.map(v => v.italian);
    const allItalianPhrases = phraseList.map(p => p.italian);
    const allItalianSentences = sentenceList.map(s => s.italian);

    // Vocabulary
    const vocabularyExport = vocabList.map(item => {
      const distractors = getDistractors(item.italian, allItalianVocab);
      const choices = shuffle([item.italian, ...distractors]);
      return {
        id: item.id,
        italian: item.italian,
        english: item.english,
        type: 'vocabulary',
        choices,
        correctAnswer: item.italian,
        feedback: {
          correct: 'Ottimo!',
          incorrect: `Quasi! La risposta corretta è "${item.italian}".`
        }
      };
    });

    // Phrases
    const phrasesExport = phraseList.map(item => {
      const distractors = getDistractors(item.italian, allItalianPhrases);
      const choices = shuffle([item.italian, ...distractors]);
      return {
        id: item.id,
        italian: item.italian,
        english: item.english,
        type: 'phrase',
        choices,
        correctAnswer: item.italian,
        feedback: {
          correct: 'Ottimo!',
          incorrect: `Quasi! La risposta corretta è "${item.italian}".`
        }
      };
    });

    // Sentences
    const sentencesExport = sentenceList.map(item => {
      const distractors = getDistractors(item.italian, allItalianSentences);
      const choices = shuffle([item.italian, ...distractors]);
      return {
        id: item.id,
        italian: item.italian,
        english: item.english,
        type: 'sentence',
        choices,
        correctAnswer: item.italian,
        feedback: {
          correct: 'Ottimo!',
          incorrect: `Quasi! La risposta corretta è "${item.italian}".`
        }
      };
    });

    fs.writeFileSync(
      path.join(EXPORT_DIR, `${categorySlug}_${scenarioSlug}_vocabulary.json`),
      JSON.stringify(vocabularyExport, null, 2)
    );
    fs.writeFileSync(
      path.join(EXPORT_DIR, `${categorySlug}_${scenarioSlug}_phrases.json`),
      JSON.stringify(phrasesExport, null, 2)
    );
    fs.writeFileSync(
      path.join(EXPORT_DIR, `${categorySlug}_${scenarioSlug}_sentences.json`),
      JSON.stringify(sentencesExport, null, 2)
    );
  }

  console.log(`Exported questions for ${scenarios.length} scenarios to ${EXPORT_DIR}`);
}

generateQuestions();
