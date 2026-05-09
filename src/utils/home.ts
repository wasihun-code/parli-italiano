import {scenarioCatalog} from '@app/data/scenarios';
import type {RootStackParamList} from '@app/navigation/AppNavigator';
import type {ScenarioPhaseProgress} from '@app/store/progressStore';

export type ResumeRoute =
  | {name: 'VocabularyTraining'; params: RootStackParamList['VocabularyTraining']}
  | {name: 'PhraseTraining'; params: RootStackParamList['PhraseTraining']}
  | {name: 'SentenceTraining'; params: RootStackParamList['SentenceTraining']}
  | {name: 'Conversation'; params: RootStackParamList['Conversation']};

export type ResumeScenario = {
  scenarioId: number;
  title: string;
  route: ResumeRoute;
  label: string;
};

function isInProgress(progress: ScenarioPhaseProgress): boolean {
  return (
    progress.vocabularyCompleted ||
    progress.phraseScore > 0 ||
    progress.phraseCompleted ||
    progress.sentenceScore > 0 ||
    progress.sentenceCompleted ||
    progress.conversationUnlocked
  );
}

export function getNextScenarioRoute(
  scenarioId: number,
  progress: ScenarioPhaseProgress,
): ResumeRoute {
  if (!progress.vocabularyCompleted) {
    return {name: 'VocabularyTraining', params: {scenarioId}};
  }

  if (!progress.phraseCompleted) {
    return {name: 'PhraseTraining', params: {scenarioId}};
  }

  if (!progress.sentenceCompleted) {
    return {name: 'SentenceTraining', params: {scenarioId}};
  }

  return {name: 'Conversation', params: {scenarioId}};
}

export function findResumeScenario(
  scenarioProgress: Record<number, ScenarioPhaseProgress>,
): ResumeScenario | null {
  const entries = Object.entries(scenarioProgress)
    .map(([scenarioId, progress]) => ({
      scenarioId: Number(scenarioId),
      progress,
    }))
    .filter(entry => isInProgress(entry.progress))
    .sort((left, right) => left.scenarioId - right.scenarioId);

  const entry = entries[0];
  if (!entry) {
    return null;
  }

  const scenario = scenarioCatalog.find(item => item.id === entry.scenarioId);
  const route = getNextScenarioRoute(entry.scenarioId, entry.progress);

  return {
    scenarioId: entry.scenarioId,
    title: scenario?.title ?? `Scenario ${entry.scenarioId}`,
    route,
    label:
      route.name === 'VocabularyTraining'
        ? 'Continue Vocabulary'
        : route.name === 'PhraseTraining'
          ? 'Continue Phrases'
          : route.name === 'SentenceTraining'
            ? 'Continue Sentences'
            : 'Continue Conversation',
  };
}

export function calculateFoundationProgress(
  foundationScores: Record<number, number>,
  totalLessons: number,
): number {
  if (totalLessons <= 0) {
    return 0;
  }

  const passed = Object.values(foundationScores).filter(score => score >= 90).length;
  return Math.round((passed / totalLessons) * 100);
}
