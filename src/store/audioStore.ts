import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import { createPersistStorage } from './persistStorage';

interface AudioState {
  soundEnabled: boolean;
  volume: number;
  toggleSound: () => void;
  setVolume: (volume: number) => void;
}

export const useAudioStore = create<AudioState>()(
  persist(
    (set) => ({
      soundEnabled: true,
      volume: 0.5,
      toggleSound: () => set((state) => ({ soundEnabled: !state.soundEnabled })),
      setVolume: (volume) => set({ volume }),
    }),
    {
      name: 'parla-italiano-audio',
      storage: createJSONStorage(createPersistStorage),
    }
  )
);
