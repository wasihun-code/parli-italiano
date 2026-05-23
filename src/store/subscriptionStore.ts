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
  forcePremiumForTesting: () => void;
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
          // Check for URL param or localStorage flag for testing
          const isDevPremium = localStorage.getItem('premium_test') === 'true' || window.location.search.includes('premium=true');
          if (isDevPremium) {
            set({ plan: 'premium', isValid: true, isLoading: false });
            return;
          }

          const status = await apiClient.getSubscriptionStatus();
          set({ plan: status.plan, isValid: status.is_valid, isLoading: false });
        } catch (err: any) {
          set({ error: err.message, isLoading: false });
        }
      },
      setPlan: (plan, isValid) => set({ plan, isValid }),
      forcePremiumForTesting: () => set({ plan: 'premium', isValid: true }),
    }),
    {
      name: 'parla-italiano-subscription',
      storage: createJSONStorage(createPersistStorage),
    }
  )
);
