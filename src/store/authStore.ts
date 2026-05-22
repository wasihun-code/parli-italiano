import {create} from 'zustand';
import {persist, createJSONStorage} from 'zustand/middleware';

import {createPersistStorage} from './persistStorage';
import {apiClient} from '../lib/apiClient';

type AuthUser = {
  id: string;
  name: string;
  email: string;
};

export type PublicUser = AuthUser;

type AuthState = {
  currentUser?: AuthUser;
  login: (email: string, password: string) => Promise<{ok: boolean, error?: string}>;
  signup: (name: string, email: string, password: string) => Promise<{ok: boolean, error?: string}>;
  googleLogin: (token: string) => Promise<{ok: boolean, error?: string}>;
  logout: () => void;
};

export const useAuthStore = create<AuthState>()(
  persist(
    (set, get) => ({
      currentUser: undefined,
      login: async (email, password) => {
        try {
          const response = await apiClient.login(email, password);
          set({ currentUser: { 
            id: response.user.id, 
            email: response.user.email, 
            name: response.user.username 
          } });
          return {ok: true};
        } catch (err: any) {
          return {ok: false, error: err.message};
        }
      },
      signup: async (name, email, password) => {
        try {
          await apiClient.register({ username: name, email, password });
          return await get().login(email, password);
        } catch (err: any) {
          return {ok: false, error: err.message};
        }
      },
      googleLogin: async (token) => {
        try {
          const response = await apiClient.googleLogin(token);
          set({ currentUser: { 
            id: response.user.id, 
            email: response.user.email, 
            name: response.user.username 
          } });
          return {ok: true};
        } catch (err: any) {
          return {ok: false, error: err.message};
        }
      },
      logout: () => {
        localStorage.removeItem('auth_token');
        set({currentUser: undefined});
      },
    }),
    {
      name: 'parla-italiano-auth',
      storage: createJSONStorage(createPersistStorage),
    },
  ),
);

export const useCurrentUser = () => {
  return useAuthStore(state => state.currentUser);
};
