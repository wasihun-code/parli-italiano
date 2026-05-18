import {create} from 'zustand';
import {persist, createJSONStorage} from 'zustand/middleware';

import {createPersistStorage} from './persistStorage';
import {useSrsStore} from './srsStore';
import {useProgressStore} from './progressStore';
import {useConversationStore} from './conversationStore';

export type ProfileState = {
  name: string;
  email: string;
  avatar: string;
  updateProfile: (updates: Partial<Pick<ProfileState, 'name' | 'email' | 'avatar'>>) => void;
  resetAllProgress: () => void;
};

export const useProfileStore = create<ProfileState>()(
  persist(
    (set) => ({
      name: 'Learner',
      email: '',
      avatar: '👤',
      updateProfile: (updates) => set((state) => ({ ...state, ...updates })),
      resetAllProgress: () => {
        useSrsStore.getState().reset();
        useProgressStore.setState({ foundationScores: {}, scenarioProgress: {} });
        useConversationStore.setState({ messages: [], userErrors: [], unknownWords: [] });
      }
    }),
    {
      name: 'parla-italiano-profile',
      storage: createJSONStorage(createPersistStorage),
    }
  )
);
