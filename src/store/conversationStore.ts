import {create} from 'zustand';
import {persist, createJSONStorage} from 'zustand/middleware';

import {createPersistStorage} from './persistStorage';

export type ConversationSpeed = 'lento' | 'normale';
export type ConversationRole = 'assistant' | 'user' | 'system';

export type ConversationMessage = {
  id: string;
  scenarioId: number;
  role: ConversationRole;
  text: string;
  translation?: string;
  createdAt: string;
};

export type LoggedUserError = {
  id: string;
  scenarioId: number;
  sourceText: string;
  correction: string;
  explanation: string;
  createdAt: string;
};

export type UnknownWord = {
  id: string;
  scenarioId: number;
  word: string;
  context: string;
  createdAt: string;
};

type ConversationState = {
  messages: ConversationMessage[];
  speed: ConversationSpeed;
  activeScenarioId?: number;
  userErrors: LoggedUserError[];
  unknownWords: UnknownWord[];
  startScenario: (scenarioId: number) => void;
  addMessage: (message: Omit<ConversationMessage, 'id' | 'createdAt'>) => string;
  setSpeed: (speed: ConversationSpeed) => void;
  logUserError: (
    error: Omit<LoggedUserError, 'id' | 'createdAt'>,
  ) => void;
  logUnknownWord: (word: Omit<UnknownWord, 'id' | 'createdAt'>) => void;
  clearScenario: (scenarioId: number) => void;
};

function makeId(prefix: string): string {
  return `${prefix}-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;
}

export const useConversationStore = create<ConversationState>()(
  persist(
    set => ({
      messages: [],
      speed: 'lento',
      userErrors: [],
      unknownWords: [],
      startScenario: scenarioId => set({activeScenarioId: scenarioId}),
      addMessage: message => {
        const id = makeId('message');
        set(state => ({
          messages: [
            ...state.messages,
            {
              ...message,
              id,
              createdAt: new Date().toISOString(),
            },
          ],
        }));
        return id;
      },
      setSpeed: speed => set({speed}),
      logUserError: error =>
        set(state => ({
          userErrors: [
            ...state.userErrors,
            {...error, id: makeId('error'), createdAt: new Date().toISOString()},
          ],
        })),
      logUnknownWord: word =>
        set(state => ({
          unknownWords: [
            ...state.unknownWords,
            {...word, id: makeId('unknown'), createdAt: new Date().toISOString()},
          ],
        })),
      clearScenario: scenarioId =>
        set(state => ({
          messages: state.messages.filter(message => message.scenarioId !== scenarioId),
          userErrors: state.userErrors.filter(error => error.scenarioId !== scenarioId),
          unknownWords: state.unknownWords.filter(word => word.scenarioId !== scenarioId),
        })),
    }),
    {
      name: 'parla-italiano-conversation-history',
      storage: createJSONStorage(createPersistStorage),
    },
  ),
);
