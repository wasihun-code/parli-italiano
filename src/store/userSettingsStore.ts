import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import { createPersistStorage } from './persistStorage';

type UserSettings = {
  feedbackLanguage: 'it' | 'en';
  soundEnabled: boolean;
  volume: number;
  flashcardDirection: 'it-en' | 'en-it';
  setFeedbackLanguage: (lang: 'it' | 'en') => void;
  setSoundEnabled: (enabled: boolean) => void;
  setVolume: (volume: number) => void;
  toggleSound: () => void;
  setFlashcardDirection: (dir: 'it-en' | 'en-it') => void;
  resetAllProgress: () => void;
};

export const useUserSettingsStore = create<UserSettings>()(
  persist(
    (set) => ({
      feedbackLanguage: 'it',
      soundEnabled: true,
      volume: 0.5,
      flashcardDirection: 'en-it',
      setFeedbackLanguage: (lang) => set({ feedbackLanguage: lang }),
      setSoundEnabled: (enabled) => set({ soundEnabled: enabled }),
      setVolume: (volume) => set({ volume }),
      toggleSound: () => set((state) => ({ soundEnabled: !state.soundEnabled })),
      setFlashcardDirection: (dir) => set({ flashcardDirection: dir }),
      resetAllProgress: () => {
        // This will be handled in the component by clearing localStorage
      },
    }),
    {
      name: 'parla-italiano-settings',
      storage: createJSONStorage(createPersistStorage),
    }
  )
);
