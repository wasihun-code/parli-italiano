import {
  assistantMessageContainsCorrection,
  buildAlpacaPrompt,
  buildSystemMessage,
  buildConversationVocabulary,
  buildGrammarMiniLessonInstruction,
} from './prompt';

describe('Antonio Alpaca prompt builder', () => {
  it('builds system message correctly', () => {
    const vocabulary = buildConversationVocabulary(['biglietto']);
    const msg = buildSystemMessage('Airport', 'un impiegato', vocabulary);
    
    expect(msg).toContain('un impiegato');
    expect(msg).toContain('Airport');
    expect(msg).toContain('biglietto');
    expect(msg).toContain('Parla SOLO in italiano');
  });

  it('builds Alpaca prompt correctly', () => {
    const system = 'System message';
    const input = 'User input';
    const prompt = buildAlpacaPrompt(system, input);

    expect(prompt).toContain('### Instruction:\nSystem message');
    expect(prompt).toContain('### Input:\nUser input');
    expect(prompt).toContain('### Response:');
  });

  it('provides grammar mini-lesson instruction', () => {
    expect(buildGrammarMiniLessonInstruction()).toContain('consiglio grammaticale');
  });

  it('detects likely correction responses for error logging', () => {
    expect(assistantMessageContainsCorrection('Correzione: dire io sono.')).toBe(true);
    expect(assistantMessageContainsCorrection('Hai detto io essere.')).toBe(true);
    expect(assistantMessageContainsCorrection('Va bene.')).toBe(false);
  });
});
