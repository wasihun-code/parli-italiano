import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import { createPersistStorage } from './persistStorage';

type UserSettings = {
  feedbackLanguage: 'it' | 'en';
  soundEnabled: boolean;
  flashcardDirection: 'it-en' | 'en-it';
  ttsProvider: 'browser' | 'api';
  setFeedbackLanguage: (lang: 'it' | 'en') => void;
  setSoundEnabled: (enabled: boolean) => void;
  setFlashcardDirection: (dir: 'it-en' | 'en-it') => void;
  setTtsProvider: (provider: 'browser' | 'api') => void;
  resetAllProgress: () => void;
};

export const useUserSettingsStore = create<UserSettings>()(
  persist(
    (set) => ({
      feedbackLanguage: 'it',
      soundEnabled: true,
      flashcardDirection: 'en-it',
      ttsProvider: 'api',
      setFeedbackLanguage: (lang) => set({ feedbackLanguage: lang }),
      setSoundEnabled: (enabled) => set({ soundEnabled: enabled }),
      setFlashcardDirection: (dir) => set({ flashcardDirection: dir }),
      setTtsProvider: (provider) => set({ ttsProvider: provider }),
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
