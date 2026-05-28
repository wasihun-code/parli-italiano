import { scenarioMapping } from './scenarioMapping';

// Eagerly import all vocabulary, phrases, and sentences from the exports directory
const vocabularyFiles = import.meta.glob('./exports/**/*_vocabulary.json', { eager: true });
const phrasesFiles = import.meta.glob('./exports/**/*_phrases.json', { eager: true });
const sentencesFiles = import.meta.glob('./exports/**/*_sentences.json', { eager: true });

export type RawScenarioData = {
  vocabulary: any[];
  phrases: any[];
  sentences: any[];
};

/**
 * Normalizes production corpus item to be backward compatible with legacy fields.
 */
function normalizeItem(item: any) {
  return {
    ...item,
    // Prefer correctAnswerItalian/English if they exist, fallback to italian/english
    italian: item.correctAnswerItalian || item.italian,
    english: item.correctAnswerEnglish || item.english,
  };
}

export function loadProductionScenarioData(scenarioId: number): RawScenarioData | null {
  const relPath = scenarioMapping[scenarioId];
  if (!relPath) return null;

  // Reconstruct the full path relative to this file
  // scenarioMapping stores paths like 'exports/travel/airport_arrival'
  const vocabPath = `./${relPath}/${relPath.split('/').pop()}_vocabulary.json`;
  const phrasesPath = `./${relPath}/${relPath.split('/').pop()}_phrases.json`;
  const sentencesPath = `./${relPath}/${relPath.split('/').pop()}_sentences.json`;

  // Find the imported modules
  // Note: import.meta.glob uses relative paths from the current file
  const vocabModule: any = vocabularyFiles[vocabPath];
  const phrasesModule: any = phrasesFiles[phrasesPath];
  const sentencesModule: any = sentencesFiles[sentencesPath];

  if (!vocabModule || !phrasesModule || !sentencesModule) {
    // console.warn(`Missing production data for scenario ${scenarioId} at ${relPath}`);
    return null;
  }

  return {
    vocabulary: (vocabModule.default || vocabModule).map(normalizeItem),
    phrases: (phrasesModule.default || phrasesModule).map(normalizeItem),
    sentences: (sentencesModule.default || sentencesModule).map(normalizeItem),
  };
}
