import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import { createPersistStorage } from './persistStorage';

export type GameProgress = {
  unlockedLevels: number; // bitmask or just max level
  highScore: number;
};

export type GameState = {
  genderGame: GameProgress;
  translationGame: GameProgress;
  prepositionGame: GameProgress;
  unlockLevel: (game: 'genderGame' | 'translationGame' | 'prepositionGame', level: number) => void;
  updateHighScore: (game: 'genderGame' | 'translationGame' | 'prepositionGame', score: number) => void;
};

export const useGameStore = create<GameState>()(
  persist(
    (set) => ({
      genderGame: { unlockedLevels: 1, highScore: 0 },
      translationGame: { unlockedLevels: 1, highScore: 0 },
      prepositionGame: { unlockedLevels: 1, highScore: 0 },
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
    }),
    {
      name: 'parla-italiano-games',
      storage: createJSONStorage(createPersistStorage),
    }
  )
);
