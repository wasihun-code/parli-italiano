import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import { createPersistStorage } from './persistStorage';
import { apiClient } from '../lib/apiClient';

export type PlanType = 'free' | 'premium' | 'premium_plus';

interface SubscriptionState {
  plan: PlanType;
  isValid: boolean;
  isLoading: boolean;
  error: string | null;
  fetchStatus: () => Promise<void>;
  setPlan: (plan: PlanType, isValid: boolean) => void;
}

export const useSubscriptionStore = create<SubscriptionState>()(
  persist(
    (set) => ({
      plan: 'free',
      isValid: false,
      isLoading: false,
      error: null,
      fetchStatus: async () => {
        set({ isLoading: true, error: null });
        try {
          const status = await apiClient.getSubscriptionStatus();
          set({ plan: status.plan, isValid: status.is_valid, isLoading: false });
        } catch (err: any) {
          set({ error: err.message, isLoading: false });
        }
      },
      setPlan: (plan, isValid) => set({ plan, isValid }),
    }),
    {
      name: 'parla-italiano-subscription',
      storage: createJSONStorage(createPersistStorage),
    }
  )
);
