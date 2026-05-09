import { foundationalVocabulary } from '@app/data/foundations';

export const highFrequencyConversationConnectors = [
  'sì',
  'no',
  'grazie',
  'prego',
  'scusi',
  'per favore',
  'va bene',
  'non capisco',
  'vorrei',
  'posso',
  'devo',
  'voglio',
] as const;

function splitIntoItalianWords(value: string): string[] {
  return value
    .trim()
    .split(/\s+/)
    .map(word => word.replace(/^[^\p{L}\p{N}]+|[^\p{L}\p{N}]+$/gu, ''))
    .filter(Boolean);
}

export function uniqueItalianVocabulary(values: string[]): string[] {
  const seen = new Set<string>();
  const unique: string[] = [];

  values.forEach(value => {
    splitIntoItalianWords(value).forEach(word => {
      const key = word.toLocaleLowerCase('it-IT');
      if (!seen.has(key)) {
        seen.add(key);
        unique.push(word);
      }
    });
  });

  return unique;
}

export function buildConversationVocabulary(
  scenarioVocabulary: string[],
): string[] {
  return uniqueItalianVocabulary([
    ...highFrequencyConversationConnectors,
    ...scenarioVocabulary,
  ]).slice(0, 50);
}

export function buildSystemMessage(scenarioTitle: string, role: string, vocabulary: string[]): string {
  const vocabList = vocabulary.join(', ');
  return `Tu sei ${role}. Stai parlando con un turista che sta imparando l'italiano. Scenario: ${scenarioTitle}. Parla SOLO in italiano semplice (livello A1). Usa frasi brevi. Non usare inglese, tranne per correggere errori. Rimani sempre nel tuo ruolo. Vocabolario consentito: ${vocabList}.`;
}

export function buildAlpacaPrompt(systemMessage: string, userInput: string): string {
  return `Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
${systemMessage}

### Input:
${userInput}

### Response:`;
}

export function buildGrammarMiniLessonInstruction(): string {
  return 'Offri un breve consiglio grammaticale in inglese su qualcosa che hai detto.';
}

export function assistantMessageContainsCorrection(text: string): boolean {
  return /\bCorrection:|\bYou said\b|Hai detto\b|Correzione\b/i.test(text);
}
