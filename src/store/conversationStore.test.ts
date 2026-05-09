import {useConversationStore} from './conversationStore';

describe('conversation store', () => {
  beforeEach(() => {
    useConversationStore.setState({
      activeScenarioId: undefined,
      messages: [],
      speed: 'lento',
      unknownWords: [],
      userErrors: [],
    });
  });

  it('tracks scenario messages, speed, errors, and unknown words', () => {
    useConversationStore.getState().startScenario(12);
    useConversationStore.getState().setSpeed('normale');
    useConversationStore.getState().addMessage({
      scenarioId: 12,
      role: 'assistant',
      text: 'Buongiorno.',
    });
    useConversationStore.getState().logUserError({
      scenarioId: 12,
      sourceText: 'io essere',
      correction: 'io sono',
      explanation: 'Use sono with io.',
    });
    useConversationStore.getState().logUnknownWord({
      scenarioId: 12,
      word: 'binario',
      context: 'Dov è il binario?',
    });

    const state = useConversationStore.getState();
    expect(state.activeScenarioId).toBe(12);
    expect(state.speed).toBe('normale');
    expect(state.messages).toHaveLength(1);
    expect(state.userErrors).toHaveLength(1);
    expect(state.unknownWords).toHaveLength(1);
  });
});
