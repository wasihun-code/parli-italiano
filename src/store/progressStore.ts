import {create} from 'zustand';
import {persist, createJSONStorage} from 'zustand/middleware';

import {foundationLessons} from '@app/data/foundations';
import {
  trackFoundationLessonCompleted,
  trackScenarioPhraseCompleted,
  trackScenarioSentenceCompleted,
  trackScenarioVocabularyCompleted,
} from '@app/utils/analytics';
import {createPersistStorage} from './persistStorage';
import {apiClient} from '../lib/apiClient';

export type ScenarioPhaseProgress = {
  vocabularyCompleted: boolean;
  phraseScore: number;
  phraseCompleted: boolean;
  sentenceScore: number;
  sentenceCompleted: boolean;
  conversationUnlocked: boolean;
};

type ProgressState = {
  xp: number;
  streak: number;
  lastActivityDate: string;
  streakFreezesUsed: number;
  streakFreezeLimit: number;
  awardedStreakMilestones: number[];
  foundationScores: Record<number, number>;
  scenarioProgress: Record<number, ScenarioPhaseProgress>;
  recordFoundationScore: (lessonId: number, score: number) => void;
  resetFoundationLesson: (lessonId: number) => void;
  areFoundationsPassed: () => boolean;
  getFoundationScore: (lessonId: number) => number;
  setScenarioVocabularyCompleted: (scenarioId: number, completed: boolean) => void;
  setScenarioPhraseScore: (scenarioId: number, score: number) => void;
  setScenarioSentenceScore: (scenarioId: number, score: number) => void;
  addXP: (amount: number) => void;
  updateStreak: () => Promise<void>;
  syncWithBackend: () => Promise<void>;
};

export const emptyScenarioProgress: ScenarioPhaseProgress = {
  vocabularyCompleted: false,
  phraseScore: 0,
  phraseCompleted: false,
  sentenceScore: 0,
  sentenceCompleted: false,
  conversationUnlocked: false,
};

function resolveScenarioProgress(
  progress: Record<number, ScenarioPhaseProgress>,
  scenarioId: number,
): ScenarioPhaseProgress {
  return progress[scenarioId] ?? emptyScenarioProgress;
}

function withConversationGate(
  progress: ScenarioPhaseProgress,
): ScenarioPhaseProgress {
  return {
    ...progress,
    conversationUnlocked:
      progress.vocabularyCompleted &&
      progress.phraseCompleted &&
      progress.sentenceCompleted,
  };
}

export const useProgressStore = create<ProgressState>()(
  persist(
    (set, get) => ({
      xp: 0,
      streak: 0,
      lastActivityDate: '',
      streakFreezesUsed: 0,
      streakFreezeLimit: 0,
      awardedStreakMilestones: [],
      foundationScores: {},
      scenarioProgress: {},
      addXP: (amount) => set((state) => ({ xp: state.xp + amount })),
      updateStreak: async () => {
        const today = new Date().toISOString().split('T')[0];
        const { lastActivityDate, streak, awardedStreakMilestones, xp } = get();
        
        if (lastActivityDate === today) return;

        const yesterday = new Date(Date.now() - 86400000).toISOString().split('T')[0];
        const newStreak = lastActivityDate === yesterday ? streak + 1 : 1;
        
        const milestones = awardedStreakMilestones || [];
        let bonusXP = 0;
        const newMilestones = [...milestones];

        if (newStreak >= 30 && !milestones.includes(30)) {
          bonusXP = 50;
          newMilestones.push(30);
        } else if (newStreak >= 7 && !milestones.includes(7)) {
          bonusXP = 10;
          newMilestones.push(7);
        }

        set({ 
          streak: newStreak, 
          lastActivityDate: today,
          xp: xp + bonusXP,
          awardedStreakMilestones: newMilestones,
        });

        try {
          await apiClient.recordActivity();
        } catch (err) {
          console.error('Failed to sync streak with backend:', err);
        }
      },
      syncWithBackend: async () => {
        const state = get();
        const data = {
          xp: state.xp,
          streak: state.streak,
          lastActivityDate: state.lastActivityDate,
          foundationScores: state.foundationScores,
          scenarioProgress: state.scenarioProgress,
        };
        // Assuming 'it' for Italian as the default language
        await apiClient.batchSync(data, 'it');
      },
      recordFoundationScore: (lessonId, score) => {
        const previousScore = get().foundationScores[lessonId] ?? 0;
        const nextScore = Math.max(previousScore, score);
        set(state => ({
          foundationScores: {
            ...state.foundationScores,
            [lessonId]: nextScore,
          },
        }));

        if (nextScore >= 90 && previousScore < 90) {
          trackFoundationLessonCompleted(lessonId, nextScore).catch(() => undefined);
        }
      },
      resetFoundationLesson: lessonId =>
        set(state => {
          const nextScores = {...state.foundationScores};
          delete nextScores[lessonId];
          return {foundationScores: nextScores};
        }),
      areFoundationsPassed: () =>
        foundationLessons.every(
          lesson => (get().foundationScores[lesson.id] ?? 0) >= 90,
        ),
      getFoundationScore: lessonId => get().foundationScores[lessonId] ?? 0,
      setScenarioVocabularyCompleted: (scenarioId, completed) => {
        const previous = get().scenarioProgress[scenarioId];
        set(state => {
          const existing = resolveScenarioProgress(
            state.scenarioProgress,
            scenarioId,
          );
          return {
            scenarioProgress: {
              ...state.scenarioProgress,
              [scenarioId]: withConversationGate({
                ...existing,
                vocabularyCompleted: completed,
              }),
            },
          };
        });

        if (completed && !previous?.vocabularyCompleted) {
          trackScenarioVocabularyCompleted(scenarioId).catch(() => undefined);
          get().updateStreak().catch(() => undefined);
        }
      },
      setScenarioPhraseScore: (scenarioId, score) => {
        const previous = get().scenarioProgress[scenarioId];
        set(state => {
          const existing = resolveScenarioProgress(
            state.scenarioProgress,
            scenarioId,
          );
          return {
            scenarioProgress: {
              ...state.scenarioProgress,
              [scenarioId]: withConversationGate({
                ...existing,
                phraseScore: Math.max(existing.phraseScore, score),
                phraseCompleted: Math.max(existing.phraseScore, score) >= 85,
              }),
            },
          };
        });

        if (score >= 85 && !previous?.phraseCompleted) {
          trackScenarioPhraseCompleted(scenarioId, score).catch(() => undefined);
        }
      },
      setScenarioSentenceScore: (scenarioId, score) => {
        const previous = get().scenarioProgress[scenarioId];
        set(state => {
          const existing = resolveScenarioProgress(
            state.scenarioProgress,
            scenarioId,
          );
          return {
            scenarioProgress: {
              ...state.scenarioProgress,
              [scenarioId]: withConversationGate({
                ...existing,
                sentenceScore: Math.max(existing.sentenceScore, score),
                sentenceCompleted: Math.max(existing.sentenceScore, score) >= 80,
              }),
            },
          };
        });

        if (score >= 80 && !previous?.sentenceCompleted) {
          trackScenarioSentenceCompleted(scenarioId, score).catch(() => undefined);
        }
      },
    }),
    {
      name: 'parla-italiano-progress',
      storage: createJSONStorage(createPersistStorage),
    },
  ),
);
