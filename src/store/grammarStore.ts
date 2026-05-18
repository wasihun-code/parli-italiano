import {create} from 'zustand';
import {persist, createJSONStorage} from 'zustand/middleware';
import {createPersistStorage} from './persistStorage';

export type GrammarState = {
  completedLessons: Record<string, boolean>;
  markCompleted: (lessonId: string) => void;
  resetProgress: () => void;
};

export const useGrammarStore = create<GrammarState>()(
  persist(
    (set) => ({
      completedLessons: {},
      markCompleted: (lessonId) => set((state) => ({
        completedLessons: { ...state.completedLessons, [lessonId]: true }
      })),
      resetProgress: () => set({ completedLessons: {} })
    }),
    {
      name: 'parla-italiano-grammar',
      storage: createJSONStorage(createPersistStorage),
    }
  )
);
