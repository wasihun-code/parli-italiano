import {useMemo} from 'react';
import {create} from 'zustand';
import {persist, createJSONStorage} from 'zustand/middleware';

import {createPersistStorage} from './persistStorage';

type AuthUser = {
  id: string;
  name: string;
  email: string;
  // Demo-only local auth: passwords are stored in plaintext in browser storage.
  // Do not use this store as production authentication.
  password: string;
};

export type PublicUser = {
  id: string;
  name: string;
  email: string;
};

type AuthState = {
  users: AuthUser[];
  currentUserId?: string;
  login: (email: string, password: string) => {ok: true} | {ok: false; error: string};
  signup: (name: string, email: string, password: string) => {ok: true} | {ok: false; error: string};
  logout: () => void;
};

function normalizeEmail(email: string): string {
  return email.trim().toLocaleLowerCase();
}

export function publicUser(user: AuthUser): PublicUser {
  return {
    id: user.id,
    name: user.name,
    email: user.email,
  };
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set, get) => ({
      users: [],
      currentUserId: undefined,
      login: (email, password) => {
        const normalizedEmail = normalizeEmail(email);
        const user = get().users.find(item => item.email === normalizedEmail);
        if (!user || user.password !== password) {
          return {ok: false, error: 'Invalid email or password.'};
        }
        set({currentUserId: user.id});
        return {ok: true};
      },
      signup: (name, email, password) => {
        const normalizedEmail = normalizeEmail(email);
        if (!name.trim()) {
          return {ok: false, error: 'Enter your name.'};
        }
        if (!normalizedEmail.includes('@')) {
          return {ok: false, error: 'Enter a valid email.'};
        }
        if (password.length < 6) {
          return {ok: false, error: 'Use at least 6 characters for the password.'};
        }
        if (get().users.some(user => user.email === normalizedEmail)) {
          return {ok: false, error: 'An account already exists for this email.'};
        }
        const user: AuthUser = {
          id: `user-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
          name: name.trim(),
          email: normalizedEmail,
          password,
        };
        set(state => ({
          users: [...state.users, user],
          currentUserId: user.id,
        }));
        return {ok: true};
      },
      logout: () => set({currentUserId: undefined}),
    }),
    {
      name: 'parla-italiano-auth',
      storage: createJSONStorage(createPersistStorage),
      partialize: state => ({
        users: state.users,
        currentUserId: state.currentUserId,
      }),
    },
  ),
);

export const useCurrentUser = () => {
  const users = useAuthStore(state => state.users);
  const currentUserId = useAuthStore(state => state.currentUserId);
  const user = useMemo(() => users.find(u => u.id === currentUserId), [users, currentUserId]);
  return useMemo(() => (user ? publicUser(user) : undefined), [user]);
};
