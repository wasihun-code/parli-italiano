export type ScenarioFeedback = {
  correctItalian: string;
  incorrectItalian: string;
  correctEnglish: string;
  incorrectEnglish: string;
};

export type ScenarioAudio = {
  italian: string;
};

export type ScenarioVocabularyRow = {
  id: string;
  scenarioId: number;
  italian: string;
  english: string;
  correctStreakRequired: number;
  sortOrder: number;
  choicesItalian?: string[];
  choicesEnglish?: string[];
  feedback?: ScenarioFeedback;
  audio?: ScenarioAudio;
};

export type ScenarioPhraseRow = {
  id: string;
  scenarioId: number;
  italian: string;
  english: string;
  passScore: number;
  sortOrder: number;
  choicesItalian?: string[];
  choicesEnglish?: string[];
  feedback?: ScenarioFeedback;
  audio?: ScenarioAudio;
};

export type ScenarioSentenceRow = {
  id: string;
  scenarioId: number;
  italian: string;
  english: string;
  grammarPoint: string;
  passScore: number;
  sortOrder: number;
  choicesItalian?: string[];
  choicesEnglish?: string[];
  feedback?: ScenarioFeedback;
  audio?: ScenarioAudio;
};
