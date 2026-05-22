/**
 * Provides helpful hints and examples for incorrect answers across the app.
 */

export type ExplanationContext = {
  type: 'gender' | 'preposition' | 'translation' | 'vocabulary' | 'phrase' | 'sentence' | 'grammar' | 'idioms' | 'opposites' | 'numbers' | 'plural';
  italian?: string;
  correctAnswer?: string;
  userAnswer?: string;
  category?: string; // e.g. 'articles', 'verbs'
  extraData?: any;
};

export function getWrongAnswerExplanation(context: ExplanationContext): string {
  const { type, italian, correctAnswer, category } = context;

  switch (type) {
    case 'gender':
      return getGenderExplanation(italian || '', correctAnswer || '');
    case 'plural':
      return getPluralExplanation(italian || '', correctAnswer || '');
    case 'preposition':
      return getPrepositionExplanation(correctAnswer || '');
    case 'translation':
    case 'vocabulary':
    case 'phrase':
    case 'sentence':
      return getTranslationExplanation(type, italian || '', correctAnswer || '');
    case 'grammar':
      return getGrammarExplanation(category || '', correctAnswer || '');
    case 'idioms':
      return `Hint: Pay attention to the idiom's metaphor. For example, "In bocca al lupo" means "Good luck" not a literal wolf.`;
    case 'opposites':
      return `L'opposto di ${italian} è ${correctAnswer}. Hint: Think of common antonyms.`;
    case 'numbers':
      return `Hint: ${correctAnswer} is formed by combining the tens and units. Example: venti + due = ventidue.`;
    default:
      return "Keep trying! Pay attention to the word endings and common patterns.";
  }
}

function getGenderExplanation(word: string, correctGender: string): string {
  let hint = `Nouns ending in -o are usually masculine, and -a are usually feminine.`;
  
  if (word.toLowerCase() === 'mano') {
    hint = "Exceptions: 'mano' ends in -o but is feminine.";
  } else if (word.toLowerCase().endsWith('ma') && correctGender === 'm') {
    hint = "Nouns of Greek origin ending in -ma (like 'problema', 'clima') are often masculine.";
  } else if (word.toLowerCase().endsWith('e')) {
    hint = "Nouns ending in -e can be either masculine or feminine and must be memorized.";
  } else if (word.toLowerCase().endsWith('ione')) {
    hint = "Nouns ending in -ione are almost always feminine.";
  }

  const example = correctGender === 'm' ? "il libro (the book)" : "la casa (the house)";
  
  return `Hint: ${hint} Example of correct usage: ${example}.`;
}

function getPrepositionExplanation(preposition: string): string {
  const p = preposition.toLowerCase();
  let hint = "";
  let example = "";

  if (p === 'a') {
    hint = "Use 'a' for cities (a Roma) and specific places like 'a casa', 'a scuola'.";
    example = "Vado a Milano.";
  } else if (p === 'in') {
    hint = "Use 'in' for countries (in Italia), regions, and large islands.";
    example = "Vivo in Toscana.";
  } else if (p === 'da') {
    hint = "Use 'da' for origin or when going to a person's place.";
    example = "Vengo da Parigi.";
  } else if (p === 'di') {
    hint = "Use 'di' for possession or origin with the verb 'essere'.";
    example = "Il libro è di Marco.";
  } else if (p === 'sul' || p === 'sullo' || p === 'sulla') {
    hint = "Use 'su' (on) combined with an article for objects on surfaces.";
    example = "Il gatto è sul divano.";
  } else {
    hint = "Prepositions often depend on the verb they follow or the destination type.";
    example = "Vado al cinema (a + il).";
  }

  return `Hint: ${hint} Example: ${example}`;
}

function getTranslationExplanation(type: string, _italian: string, _correctAnswer: string): string {
  const hint = "Pay close attention to verb conjugations and the gender of nouns/adjectives.";
  const example = type === 'vocabulary' 
    ? "Il ragazzo (The boy) vs La ragazza (The girl)."
    : "Io parlo (I speak) vs Lui parla (He speaks).";
  
  return `Hint: ${hint} Example: ${example}`;
}

function getGrammarExplanation(category: string, _correctAnswer: string): string {
  let hint = "Check the grammar rules for this section.";
  let example = "";

  if (category === 'articles') {
    hint = "Articles must match the gender, number, and the starting letter of the noun.";
    example = "lo zaino (s+consonant), l'amico (vowel), il libro (consonant).";
  } else if (category.includes('verbs')) {
    hint = "Check the subject of the sentence to find the matching verb ending.";
    example = "io -o, tu -i, lui/lei -a/-e.";
  }

  return `Hint: ${hint} ${example ? 'Example: ' + example : ''}`;
}

function getPluralExplanation(word: string, plural: string): string {
  let hint = "Italian plurals usually follow patterns based on the ending.";
  
  if (word.endsWith('o')) {
    hint = "Nouns ending in -o (masculine) usually become -i in the plural.";
  } else if (word.endsWith('a')) {
    hint = "Nouns ending in -a (feminine) usually become -e in the plural.";
  } else if (word.endsWith('e')) {
    hint = "Nouns ending in -e (either gender) usually become -i in the plural.";
  } else if (plural === word) {
    hint = "Foreign loanwords or words with accents on the last vowel usually stay the same in plural.";
  }

  return `Hint: ${hint} Plural of ${word} is ${plural}.`;
}
