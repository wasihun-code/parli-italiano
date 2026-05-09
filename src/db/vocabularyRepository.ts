export type ScenarioVocabularyRow = {
  id: string;
  scenarioId: number;
  italian: string;
  english: string;
  correctStreakRequired: number;
  sortOrder: number;
};

export type ScenarioPhraseRow = {
  id: string;
  scenarioId: number;
  italian: string;
  english: string;
  passScore: number;
  sortOrder: number;
};

export type ScenarioSentenceRow = {
  id: string;
  scenarioId: number;
  italian: string;
  english: string;
  grammarPoint: string;
  passScore: number;
  sortOrder: number;
};
