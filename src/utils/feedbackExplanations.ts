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
      return `Suggerimento: Fai attenzione alla metafora dell'idioma. Ad esempio, "In bocca al lupo" significa "Buona fortuna", non un lupo letterale.`;
    case 'opposites':
      return `L'opposto di ${italian} è ${correctAnswer}. Suggerimento: Pensa ai contrari comuni.`;
    case 'numbers':
      return `Suggerimento: ${correctAnswer} si forma combinando le decine e le unità. Esempio: venti + due = ventidue.`;
    default:
      return "Continua a provare! Fai attenzione alle desinenze delle parole e agli schemi comuni.";
  }
}

function getGenderExplanation(word: string, correctGender: string): string {
  let hint = `I nomi che finiscono in -o sono solitamente maschili, e quelli in -a sono solitamente femminili.`;
  
  if (word.toLowerCase() === 'mano') {
    hint = "Eccezioni: 'mano' finisce in -o ma è femminile.";
  } else if (word.toLowerCase().endsWith('ma') && correctGender === 'm') {
    hint = "I nomi di origine greca che terminano in -ma (come 'problema', 'clima') sono spesso maschili.";
  } else if (word.toLowerCase().endsWith('e')) {
    hint = "I nomi che terminano in -e possono essere sia maschili che femminili e devono essere memorizzati.";
  } else if (word.toLowerCase().endsWith('ione')) {
    hint = "I nomi che terminano in -ione sono quasi sempre femminili.";
  }

  const example = correctGender === 'm' ? "il libro" : "la casa";
  
  return `Suggerimento: ${hint} Esempio di utilizzo corretto: ${example}.`;
}

function getPrepositionExplanation(preposition: string): string {
  const p = preposition.toLowerCase();
  let hint = "";
  let example = "";

  if (p === 'a') {
    hint = "Usa 'a' per le città (a Roma) e luoghi specifici come 'a casa', 'a scuola'.";
    example = "Vado a Milano.";
  } else if (p === 'in') {
    hint = "Usa 'in' per i paesi (in Italia), le regioni e le grandi isole.";
    example = "Vivo in Toscana.";
  } else if (p === 'da') {
    hint = "Usa 'da' per l'origine o quando si va a casa di qualcuno.";
    example = "Vengo da Parigi.";
  } else if (p === 'di') {
    hint = "Usa 'di' per il possesso o l'origine con il verbo 'essere'.";
    example = "Il libro è di Marco.";
  } else if (p === 'sul' || p === 'sullo' || p === 'sulla') {
    hint = "Usa 'su' combinato con un articolo per oggetti su superfici.";
    example = "Il gatto è sul divano.";
  } else {
    hint = "Le preposizioni spesso dipendono dal verbo che seguono o dal tipo di destinazione.";
    example = "Vado al cinema (a + il).";
  }

  return `Suggerimento: ${hint} Esempio: ${example}`;
}

function getTranslationExplanation(type: string, _italian: string, _correctAnswer: string): string {
  const hint = "Presta molta attenzione alle coniugazioni verbali e al genere di nomi/aggettivi.";
  const example = type === 'vocabulary' 
    ? "Il ragazzo vs La ragazza."
    : "Io parlo vs Lui parla.";
  
  return `Suggerimento: ${hint} Esempio: ${example}`;
}

function getGrammarExplanation(category: string, _correctAnswer: string): string {
  let hint = "Controlla le regole grammaticali per questa sezione.";
  let example = "";

  if (category === 'articles') {
    hint = "Gli articoli devono corrispondere al genere, al numero e alla lettera iniziale del nome.";
    example = "lo zaino (s+consonante), l'amico (vocale), il libro (consonante).";
  } else if (category.includes('verbs')) {
    hint = "Controlla il soggetto della frase per trovare la desinenza verbale corrispondente.";
    example = "io -o, tu -i, lui/lei -a/-e.";
  }

  return `Suggerimento: ${hint} ${example ? 'Esempio: ' + example : ''}`;
}

function getPluralExplanation(word: string, plural: string): string {
  let hint = "I plurali italiani di solito seguono schemi basati sulla desinenza.";
  
  if (word.endsWith('o')) {
    hint = "I nomi che terminano in -o (maschili) di solito diventano -i al plurale.";
  } else if (word.endsWith('a')) {
    hint = "I nomi che terminano in -a (femminili) di solito diventano -e al plurale.";
  } else if (word.endsWith('e')) {
    hint = "I nomi che terminano in -e (di entrambi i generi) di solito diventano -i al plurale.";
  } else if (plural === word) {
    hint = "I prestiti stranieri o le parole con accenti sull'ultima vocale di solito rimangono invariati al plurale.";
  }

  return `Suggerimento: ${hint} Il plurale di ${word} è ${plural}.`;
}
