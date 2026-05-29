import { scenarioMapping } from './scenarioMapping';

// Eagerly import all vocabulary, phrases, and sentences from the exports directory
const vocabularyFiles = import.meta.glob('./exports/**/*_vocabulary.json', { eager: true });
const phrasesFiles = import.meta.glob('./exports/**/*_phrases.json', { eager: true });
const sentencesFiles = import.meta.glob('./exports/**/*_sentences.json', { eager: true });
const miniLessonsFiles = import.meta.glob('./exports/**/mini_lessons.json', { eager: true });

export type RawScenarioData = {
  vocabulary: any[];
  phrases: any[];
  sentences: any[];
  miniLessons?: any[];
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

  // Extract the folder name (e.g., 'apartment_key_pickup')
  const folderName = relPath.split('/').pop();
  if (!folderName) return null;

  // Ultra-resilient match: find any key that contains the folder name and ends with the correct suffix
  const vocabPath = Object.keys(vocabularyFiles).find(k => k.includes(folderName) && k.endsWith('_vocabulary.json'));
  const phrasesPath = Object.keys(phrasesFiles).find(k => k.includes(folderName) && k.endsWith('_phrases.json'));
  const sentencesPath = Object.keys(sentencesFiles).find(k => k.includes(folderName) && k.endsWith('_sentences.json'));

  const vocabModule: any = vocabPath ? vocabularyFiles[vocabPath] : undefined;
  const phrasesModule: any = phrasesPath ? phrasesFiles[phrasesPath] : undefined;
  const sentencesModule: any = sentencesPath ? sentencesFiles[sentencesPath] : undefined;
  
  const miniLessonsPath = Object.keys(miniLessonsFiles).find(k => k.includes(folderName) && k.endsWith('mini_lessons.json'));
  const miniLessonsModule: any = miniLessonsPath ? miniLessonsFiles[miniLessonsPath] : undefined;
  const miniLessons = miniLessonsModule ? (miniLessonsModule.default || miniLessonsModule).lessons : undefined;

  // Global debug hook
  if (typeof window !== 'undefined') {
    (window as any).__PARLA_CORPUS__ = (window as any).__PARLA_CORPUS__ || {};
    (window as any).__PARLA_CORPUS__[scenarioId] = { folderName, vocabPath, phrasesPath, sentencesPath, miniLessonsPath, miniLessonsFound: !!miniLessons };
  }

  if (!vocabModule || !phrasesModule || !sentencesModule) {
    if (scenarioId === 22) console.log("[LOADER EVIDENCE] Production modules NOT found for ID 22");
    return null;
  }

  const vData = (vocabModule.default || vocabModule);
  if (scenarioId === 22) {
    console.log("[LOADER EVIDENCE] First Production Vocab ID found:", vData[0]?.id);
  }

  return {
    vocabulary: vData.map(normalizeItem),
    phrases: (phrasesModule.default || phrasesModule).map(normalizeItem),
    sentences: (sentencesModule.default || sentencesModule).map(normalizeItem),
    miniLessons,
  };
}
