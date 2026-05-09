import type {StateStorage} from 'zustand/middleware';

const memoryStore = new Map<string, string>();

const memoryStorage: StateStorage = {
  getItem: name => memoryStore.get(name) ?? null,
  setItem: (name, value) => {
    memoryStore.set(name, value);
  },
  removeItem: name => {
    memoryStore.delete(name);
  },
};

function getBrowserStorage(): StateStorage | undefined {
  if (typeof globalThis === 'undefined' || !('localStorage' in globalThis)) {
    return undefined;
  }

  return (globalThis as typeof globalThis & {localStorage: StateStorage})
    .localStorage;
}

export function createPersistStorage(): StateStorage {
  return getBrowserStorage() ?? memoryStorage;
}
