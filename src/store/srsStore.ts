import {create} from 'zustand';
import {persist, createJSONStorage} from 'zustand/middleware';

import {createPersistStorage} from './persistStorage';

export type SrsItemType = 'foundation' | 'vocabulary' | 'phrase' | 'sentence';

export type SrsItem = {
  id: string;
  type: SrsItemType;
  italian: string;
  english: string;
  correctStreak: number;
  attempts: number;
  correctAttempts: number;
  learned: boolean;
  dueAt: string;
  lastReviewedAt?: string;
  audio?: any;
};

type RegisterSrsItemInput = {
  id: string;
  type: SrsItemType;
  italian: string;
  english: string;
  audio?: any;
};

type SrsState = {
  items: Record<string, SrsItem>;
  registerItem: (item: RegisterSrsItemInput) => void;
  recordAnswer: (id: string, correct: boolean) => void;
  getDueItems: (now?: Date) => SrsItem[];
  isLearned: (id: string) => boolean;
  markAsLearned: (ids: string[]) => void;
  unlearnItem: (id: string) => void;
  reset: () => void;
};

function nextDueDate(correct: boolean, correctStreak: number, now: Date): string {
  const minutes = correct ? Math.max(10, correctStreak * 60) : 5;
  return new Date(now.getTime() + minutes * 60 * 1000).toISOString();
}

export const useSrsStore = create<SrsState>()(
  persist(
    (set, get) => ({
      items: {},
      registerItem: item =>
        set(state => {
          if (state.items[item.id]) {
            return state;
          }

          return {
            items: {
              ...state.items,
              [item.id]: {
                ...item,
                attempts: 0,
                correctAttempts: 0,
                correctStreak: 0,
                dueAt: new Date(0).toISOString(),
                learned: false,
              },
            },
          };
        }),
      recordAnswer: (id, correct) =>
        set(state => {
          const existing = state.items[id];
          if (!existing) {
            return state;
          }

          const now = new Date();
          const correctStreak = correct ? existing.correctStreak + 1 : 0;
          return {
            items: {
              ...state.items,
              [id]: {
                ...existing,
                attempts: existing.attempts + 1,
                correctAttempts: existing.correctAttempts + (correct ? 1 : 0),
                correctStreak,
                dueAt: nextDueDate(correct, correctStreak, now),
                lastReviewedAt: now.toISOString(),
                learned: correctStreak >= 3,
              },
            },
          };
        }),
      getDueItems: (now = new Date()) =>
        Object.values(get().items).filter(item => new Date(item.dueAt) <= now),
      isLearned: id => get().items[id]?.learned ?? false,
      markAsLearned: ids =>
        set(state => {
          const newItems = {...state.items};
          ids.forEach(id => {
            if (newItems[id]) {
              newItems[id] = {
                ...newItems[id],
                learned: true,
                correctStreak: Math.max(newItems[id].correctStreak, 3),
              };
            }
          });
          return {items: newItems};
        }),
      unlearnItem: id =>
        set(state => {
          const existing = state.items[id];
          if (!existing) return state;
          return {
            items: {
              ...state.items,
              [id]: {
                ...existing,
                learned: false,
                correctStreak: 0,
                dueAt: new Date().toISOString(),
              },
            },
          };
        }),
      reset: () => set({items: {}}),
    }),
    {
      name: 'parla-italiano-srs',
      storage: createJSONStorage(createPersistStorage),
    },
  ),
);
