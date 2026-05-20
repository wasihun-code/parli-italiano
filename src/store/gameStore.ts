import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import { createPersistStorage } from './persistStorage';

export type GameProgress = {
  unlockedLevels: number;
  highScore: number;
};

export type StoryProgress = {
  currentPart: number;
  currentPage: number;
  completedPages: string[]; // partIndex_pageIndex
  completedParts: number[];
  translateUsesRemaining: number;
};

export type GameKey = 'genderGame' | 'translationGame' | 'prepositionGame' | 'idiomsGame' | 'oppositesGame' | 'numbersGame';

export type GameState = {
  genderGame: GameProgress;
  translationGame: GameProgress;
  prepositionGame: GameProgress;
  idiomsGame: GameProgress;
  oppositesGame: GameProgress;
  numbersGame: GameProgress;
  
  // Stories State
  unlockedStories: string[]; // story titles
  completedStories: string[];
  storyProgress: Record<string, StoryProgress>;
  storyScores: Record<string, number>;

  unlockLevel: (game: GameKey, level: number) => void;
  updateHighScore: (game: GameKey, score: number) => void;
  
  // Stories Actions
  unlockStory: (storyTitle: string) => void;
  completeStory: (storyTitle: string, score: number) => void;
  updateStoryProgress: (storyTitle: string, progress: Partial<StoryProgress>) => void;
  resetStoryTranslateUses: (storyTitle: string) => void;
};

const INITIAL_TRANSLATE_USES = 10;

export const useGameStore = create<GameState>()(
  persist(
    (set) => ({
      genderGame: { unlockedLevels: 1, highScore: 0 },
      translationGame: { unlockedLevels: 1, highScore: 0 },
      prepositionGame: { unlockedLevels: 1, highScore: 0 },
      idiomsGame: { unlockedLevels: 1, highScore: 0 },
      oppositesGame: { unlockedLevels: 1, highScore: 0 },
      numbersGame: { unlockedLevels: 1, highScore: 0 },
      
      unlockedStories: [], // Initialized in a component or effect if empty
      completedStories: [],
      storyProgress: {},
      storyScores: {},

      unlockLevel: (game, level) => set((state) => ({
        [game]: {
          ...state[game],
          unlockedLevels: Math.max(state[game].unlockedLevels, level)
        }
      })),
      updateHighScore: (game, score) => set((state) => ({
        [game]: {
          ...state[game],
          highScore: Math.max(state[game].highScore, score)
        }
      })),

      unlockStory: (storyTitle) => set((state) => ({
        unlockedStories: state.unlockedStories.includes(storyTitle) 
          ? state.unlockedStories 
          : [...state.unlockedStories, storyTitle]
      })),

      completeStory: (storyTitle, score) => set((state) => ({
        completedStories: state.completedStories.includes(storyTitle)
          ? state.completedStories
          : [...state.completedStories, storyTitle],
        storyScores: {
          ...state.storyScores,
          [storyTitle]: Math.max(state.storyScores[storyTitle] || 0, score)
        }
      })),

      updateStoryProgress: (storyTitle, progress) => set((state) => {
        const currentProgress = state.storyProgress[storyTitle] || {
          currentPart: 0,
          currentPage: 0,
          completedPages: [],
          completedParts: [],
          translateUsesRemaining: INITIAL_TRANSLATE_USES
        };
        return {
          storyProgress: {
            ...state.storyProgress,
            [storyTitle]: { ...currentProgress, ...progress }
          }
        };
      }),

      resetStoryTranslateUses: (storyTitle) => set((state) => {
        const currentProgress = state.storyProgress[storyTitle] || {
          currentPart: 0,
          currentPage: 0,
          completedPages: [],
          completedParts: [],
          translateUsesRemaining: INITIAL_TRANSLATE_USES
        };
        return {
          storyProgress: {
            ...state.storyProgress,
            [storyTitle]: { ...currentProgress, translateUsesRemaining: INITIAL_TRANSLATE_USES }
          }
        };
      }),
    }),
    {
      name: 'parla-italiano-games',
      storage: createJSONStorage(createPersistStorage),
    }
  )
);
