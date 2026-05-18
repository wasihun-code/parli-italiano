export type GrammarExerciseType = 'multipleChoice' | 'fillBlank' | 'translation';

export type GrammarExercise = {
  id: string;
  kind: GrammarExerciseType;
  prompt: string;
  answer: string;
  options?: string[]; // for multipleChoice
};

export type GrammarLesson = {
  id: string;
  title: string;
  description: string;
  explanation: {
    text: string;
    examples: { it: string; en: string }[];
  }[];
  exercises: GrammarExercise[];
};

export const grammarLessons: GrammarLesson[] = [
  {
    id: 'g1',
    title: 'Present tense of regular verbs',
    description: 'Learn how to conjugate regular -are, -ere, and -ire verbs.',
    explanation: [
      {
        text: 'In Italian, verbs are grouped into three categories based on their infinitive endings: -are, -ere, -ire. To conjugate, drop the ending and add the pronouns\' specific suffixes.',
        examples: [
          { it: 'Io parlo (parlare)', en: 'I speak' },
          { it: 'Tu leggi (leggere)', en: 'You read' },
          { it: 'Lui dorme (dormire)', en: 'He sleeps' },
        ],
      },
      {
        text: 'The typical endings are:\n-ARE: -o, -i, -a, -iamo, -ate, -ano\n-ERE: -o, -i, -e, -iamo, -ete, -ono\n-IRE: -o, -i, -e, -iamo, -ite, -ono (some add -isc-).',
        examples: [
          { it: 'Noi mangiamo', en: 'We eat' },
          { it: 'Voi prendete', en: 'You all take' },
          { it: 'Loro aprono', en: 'They open' },
        ],
      }
    ],
    exercises: [
      { id: 'g1-1', kind: 'multipleChoice', prompt: "Translate: 'I work'", answer: 'Lavoro', options: ['Lavoro', 'Lavori', 'Lavora', 'Lavoriamo'] },
      { id: 'g1-2', kind: 'fillBlank', prompt: 'Noi ____ (scrivere) una lettera.', answer: 'scriviamo' },
      { id: 'g1-3', kind: 'multipleChoice', prompt: "Translate: 'They listen'", answer: 'Ascoltano', options: ['Ascoltano', 'Ascolta', 'Ascoltate', 'Ascoltiamo'] },
      { id: 'g1-4', kind: 'fillBlank', prompt: 'Tu ____ (partire) domani.', answer: 'parti' },
      { id: 'g1-5', kind: 'translation', prompt: 'He reads a book.', answer: 'Lui legge un libro.' },
    ]
  },
  {
    id: 'g2',
    title: 'Essere and Avere',
    description: 'The two most important irregular verbs in Italian: to be and to have.',
    explanation: [
      {
        text: 'Essere (to be) and Avere (to have) are highly irregular but essential for building sentences and forming past tenses.',
        examples: [
          { it: 'Io sono felice.', en: 'I am happy.' },
          { it: 'Io ho fame.', en: 'I am hungry (lit: I have hunger).' },
        ]
      },
      {
        text: 'Essere conjugation: sono, sei, è, siamo, siete, sono.\nAvere conjugation: ho, hai, ha, abbiamo, avete, hanno.',
        examples: [
          { it: 'Noi abbiamo una macchina.', en: 'We have a car.' },
          { it: 'Loro sono in Italia.', en: 'They are in Italy.' },
        ]
      }
    ],
    exercises: [
      { id: 'g2-1', kind: 'fillBlank', prompt: 'Tu ____ (essere) mio amico.', answer: 'sei' },
      { id: 'g2-2', kind: 'multipleChoice', prompt: "Translate: 'She has a dog'", answer: 'Lei ha un cane', options: ['Lei ha un cane', 'Lei è un cane', 'Lei ho un cane', 'Lei abbiamo un cane'] },
      { id: 'g2-3', kind: 'fillBlank', prompt: 'Voi ____ (avere) molto tempo.', answer: 'avete' },
      { id: 'g2-4', kind: 'multipleChoice', prompt: "Translate: 'We are ready'", answer: 'Noi siamo pronti', options: ['Noi siamo pronti', 'Noi abbiamo pronti', 'Loro sono pronti', 'Noi siete pronti'] },
      { id: 'g2-5', kind: 'translation', prompt: 'They have a house.', answer: 'Loro hanno una casa.' },
    ]
  },
  {
    id: 'g3',
    title: 'Definite and Indefinite Articles',
    description: 'Mastering il, la, i, le and un, una.',
    explanation: [
      {
        text: 'Articles must agree in gender (masculine/feminine) and number (singular/plural) with the noun.',
        examples: [
          { it: 'il ragazzo / i ragazzi', en: 'the boy / the boys' },
          { it: 'la ragazza / le ragazze', en: 'the girl / the girls' },
        ]
      },
      {
        text: 'Use "lo/gli" (def) and "uno" (indef) for masculine words starting with s+consonant or z. Use "l\'" and "un\'" before vowels.',
        examples: [
          { it: 'lo studente / gli studenti', en: 'the student / the students' },
          { it: 'un\'amica / l\'amica', en: 'a female friend / the female friend' },
        ]
      }
    ],
    exercises: [
      { id: 'g3-1', kind: 'multipleChoice', prompt: "Choose the article for 'zaino' (masc. sing.)", answer: 'lo', options: ['lo', 'il', 'la', 'gli'] },
      { id: 'g3-2', kind: 'fillBlank', prompt: '____ (A) mela', answer: 'una' },
      { id: 'g3-3', kind: 'multipleChoice', prompt: "Choose the article for 'amici' (masc. plur., vowel)", answer: 'gli', options: ['gli', 'i', 'le', 'lo'] },
      { id: 'g3-4', kind: 'fillBlank', prompt: '____ (The) pizza', answer: 'la' },
      { id: 'g3-5', kind: 'translation', prompt: 'The books', answer: 'I libri' },
    ]
  },
  {
    id: 'g4',
    title: 'Prepositions',
    description: 'Learn the essential prepositions: a, da, di, in, con, su, per, tra/fra.',
    explanation: [
      {
        text: 'Prepositions define relationships between words. "A" is for cities, "in" is for countries/regions, "di" shows possession or origin.',
        examples: [
          { it: 'Vado a Roma.', en: 'I go to Rome.' },
          { it: 'Vivo in Italia.', en: 'I live in Italy.' },
          { it: 'Il libro di Marco.', en: 'Marco\'s book.' },
        ]
      },
      {
        text: 'Prepositions combine with definite articles to form "articulated prepositions" (e.g., a + il = al).',
        examples: [
          { it: 'Vado al cinema.', en: 'I go to the cinema.' },
          { it: 'Il libro è sul tavolo.', en: 'The book is on the table (su + il).' },
        ]
      }
    ],
    exercises: [
      { id: 'g4-1', kind: 'fillBlank', prompt: 'Vado ____ (to) Parigi.', answer: 'a' },
      { id: 'g4-2', kind: 'multipleChoice', prompt: 'Translate: "To the restaurant" (a + il)', answer: 'al ristorante', options: ['al ristorante', 'a il ristorante', 'nel ristorante', 'dal ristorante'] },
      { id: 'g4-3', kind: 'fillBlank', prompt: 'Siamo ____ (in) Spagna.', answer: 'in' },
      { id: 'g4-4', kind: 'multipleChoice', prompt: 'Translate: "With me"', answer: 'con me', options: ['con me', 'di me', 'a me', 'per me'] },
      { id: 'g4-5', kind: 'translation', prompt: 'The keys are on the table.', answer: 'Le chiavi sono sul tavolo.' },
    ]
  },
  {
    id: 'g5',
    title: 'Negation and Word Order',
    description: 'How to form negative sentences and basic sentence structure.',
    explanation: [
      {
        text: 'To make a sentence negative in Italian, simply put "non" right before the verb.',
        examples: [
          { it: 'Io non capisco.', en: 'I don\'t understand.' },
          { it: 'Lui non lavora oggi.', en: 'He is not working today.' },
        ]
      },
      {
        text: 'The standard word order is Subject + Verb + Object. Adjectives usually come after the noun.',
        examples: [
          { it: 'La donna mangia una mela rossa.', en: 'The woman eats a red apple.' },
        ]
      }
    ],
    exercises: [
      { id: 'g5-1', kind: 'multipleChoice', prompt: "Translate: 'I am not ready'", answer: 'Non sono pronto', options: ['Non sono pronti', 'Non sono pronto', 'Sono non pronto', 'No sono pronto'] },
      { id: 'g5-2', kind: 'fillBlank', prompt: 'Noi ____ (don\'t) vogliamo uscire.', answer: 'non' },
      { id: 'g5-3', kind: 'translation', prompt: 'He does not speak Italian.', answer: 'Lui non parla italiano.' },
      { id: 'g5-4', kind: 'multipleChoice', prompt: 'Which sentence has correct word order?', answer: 'Io mangio una pizza calda.', options: ['Io mangio una calda pizza.', 'Io mangio una pizza calda.', 'Io una pizza calda mangio.', 'Mangio io pizza calda una.'] },
      { id: 'g5-5', kind: 'fillBlank', prompt: 'Lei ____ (doesn\'t) sa la risposta.', answer: 'non' },
    ]
  },
  {
    id: 'g6',
    title: 'Adjectives (Agreement & Position)',
    description: 'Matching adjectives to nouns and placing them correctly.',
    explanation: [
      {
        text: 'Adjectives must match the gender and number of the noun they modify.',
        examples: [
          { it: 'ragazzo alto / ragazza alta', en: 'tall boy / tall girl' },
          { it: 'ragazzi alti / ragazze alte', en: 'tall boys / tall girls' },
        ]
      },
      {
        text: 'Most adjectives go AFTER the noun. A few common ones (bello, bravo, buono, brutto, nuovo, vecchio, piccolo, grande) often go BEFORE.',
        examples: [
          { it: 'Un libro interessante', en: 'An interesting book' },
          { it: 'Un bel libro', en: 'A beautiful book' },
        ]
      }
    ],
    exercises: [
      { id: 'g6-1', kind: 'multipleChoice', prompt: "Choose the correct form: 'La casa ____'", answer: 'bianca', options: ['bianca', 'bianco', 'bianchi', 'bianche'] },
      { id: 'g6-2', kind: 'fillBlank', prompt: 'I cani ____ (piccolo - plural masc)', answer: 'piccoli' },
      { id: 'g6-3', kind: 'multipleChoice', prompt: 'Translate: "An elegant dress"', answer: 'Un vestito elegante', options: ['Un vestito elegante', 'Un elegante vestito', 'Una vestita elegante', 'Un vestito eleganti'] },
      { id: 'g6-4', kind: 'fillBlank', prompt: 'Le macchine ____ (nuovo - plural fem)', answer: 'nuove' },
      { id: 'g6-5', kind: 'translation', prompt: 'The red apple', answer: 'La mela rossa' },
    ]
  },
  {
    id: 'g7',
    title: 'Passato Prossimo',
    description: 'The most common past tense, using avere or essere.',
    explanation: [
      {
        text: 'Passato prossimo is formed with the present tense of avere or essere + the past participle of the main verb.',
        examples: [
          { it: 'Ho mangiato.', en: 'I ate / I have eaten.' },
          { it: 'Sono andato.', en: 'I went / I have gone.' },
        ]
      },
      {
        text: 'Most verbs use "avere". Verbs of movement, state, and reflexive verbs use "essere". When using "essere", the past participle must agree in gender and number with the subject.',
        examples: [
          { it: 'Noi abbiamo studiato.', en: 'We studied.' },
          { it: 'Lei è partita.', en: 'She left.' },
          { it: 'Loro sono arrivati.', en: 'They arrived.' },
        ]
      }
    ],
    exercises: [
      { id: 'g7-1', kind: 'multipleChoice', prompt: 'Translate: "I worked"', answer: 'Ho lavorato', options: ['Ho lavorato', 'Sono lavorato', 'Hai lavorato', 'Sei lavorato'] },
      { id: 'g7-2', kind: 'fillBlank', prompt: 'Lui ____ (went) a Roma.', answer: 'è andato' },
      { id: 'g7-3', kind: 'multipleChoice', prompt: 'Translate: "She has slept"', answer: 'Ha dormito', options: ['Ha dormito', 'È dormita', 'Ha dormita', 'È dormito'] },
      { id: 'g7-4', kind: 'fillBlank', prompt: 'Noi (fem) ____ (arrived).', answer: 'siamo arrivate' },
      { id: 'g7-5', kind: 'translation', prompt: 'We ate a pizza.', answer: 'Abbiamo mangiato una pizza.' },
    ]
  },
  {
    id: 'g8',
    title: 'Future Simple',
    description: 'Expressing actions that will happen.',
    explanation: [
      {
        text: 'The future simple (futuro semplice) is used to talk about events yet to come. It\'s formed by dropping the final "e" of the infinitive and adding specific endings. For -are verbs, the "a" changes to "e".',
        examples: [
          { it: 'Parlare -> io parlerò', en: 'I will speak' },
          { it: 'Leggere -> tu leggerai', en: 'You will read' },
          { it: 'Dormire -> lui dormirà', en: 'He will sleep' },
        ]
      },
      {
        text: 'The endings are: -ò, -ai, -à, -emo, -ete, -anno.',
        examples: [
          { it: 'Noi viaggeremo domani.', en: 'We will travel tomorrow.' },
          { it: 'Loro finiranno il lavoro.', en: 'They will finish the work.' },
        ]
      }
    ],
    exercises: [
      { id: 'g8-1', kind: 'multipleChoice', prompt: "Translate: 'I will eat'", answer: 'Mangerò', options: ['Mangerò', 'Mangerai', 'Mangio', 'Ho mangiato'] },
      { id: 'g8-2', kind: 'fillBlank', prompt: 'Lui ____ (will write) un libro.', answer: 'scriverà' },
      { id: 'g8-3', kind: 'translation', prompt: 'We will leave tomorrow.', answer: 'Partiremo domani.' },
      { id: 'g8-4', kind: 'multipleChoice', prompt: "Translate: 'They will take'", answer: 'Prenderanno', options: ['Prendono', 'Prenderanno', 'Prenderemo', 'Presero'] },
      { id: 'g8-5', kind: 'fillBlank', prompt: 'Tu ____ (will arrive) alle otto.', answer: 'arriverai' },
    ]
  },
  {
    id: 'g9',
    title: 'Direct Object Pronouns',
    description: 'Replacing direct objects to avoid repetition (lo, la, li, le).',
    explanation: [
      {
        text: 'Direct object pronouns replace a noun that directly receives the action. They go immediately BEFORE the conjugated verb.',
        examples: [
          { it: 'Mangi la mela? -> Sì, la mangio.', en: 'Do you eat the apple? -> Yes, I eat it.' },
          { it: 'Vedi il libro? -> No, non lo vedo.', en: 'Do you see the book? -> No, I don\'t see it.' },
        ]
      },
      {
        text: 'The pronouns are: mi (me), ti (you), lo (him/it masc), la (her/it fem), ci (us), vi (you plural), li (them masc), le (them fem).',
        examples: [
          { it: 'Conosci i miei amici? -> Sì, li conosco.', en: 'Do you know my friends? -> Yes, I know them.' },
        ]
      }
    ],
    exercises: [
      { id: 'g9-1', kind: 'multipleChoice', prompt: 'Replace "il caffè": "Bevi il caffè?" -> "Sì, ____ bevo."', answer: 'lo', options: ['lo', 'la', 'li', 'le'] },
      { id: 'g9-2', kind: 'fillBlank', prompt: 'Guardi la televisione? Sì, ____ (it fem) guardo.', answer: 'la' },
      { id: 'g9-3', kind: 'multipleChoice', prompt: 'Translate: "I see them (fem)"', answer: 'Le vedo', options: ['Li vedo', 'La vedo', 'Le vedo', 'Lo vedo'] },
      { id: 'g9-4', kind: 'translation', prompt: 'I buy it (masc).', answer: 'Lo compro.' },
      { id: 'g9-5', kind: 'fillBlank', prompt: 'Lui mi chiama? Sì, lui ____ (you) chiama.', answer: 'ti' },
    ]
  },
  {
    id: 'g10',
    title: 'Reflexive Verbs',
    description: 'Verbs where the subject performs the action on itself.',
    explanation: [
      {
        text: 'Reflexive verbs end in "-rsi" in the infinitive (e.g., lavarsi). The reflexive pronoun goes BEFORE the conjugated verb.',
        examples: [
          { it: 'Io mi alzo.', en: 'I get up.' },
          { it: 'Tu ti vesti.', en: 'You get dressed.' },
        ]
      },
      {
        text: 'The reflexive pronouns are: mi, ti, si, ci, vi, si.',
        examples: [
          { it: 'Lei si trucca.', en: 'She puts on makeup.' },
          { it: 'Noi ci divertiamo.', en: 'We have fun.' },
          { it: 'Loro si svegliano.', en: 'They wake up.' },
        ]
      }
    ],
    exercises: [
      { id: 'g10-1', kind: 'multipleChoice', prompt: "Translate: 'I wake up'", answer: 'Mi sveglio', options: ['Mi sveglio', 'Ti sveglio', 'Sveglio mi', 'Si sveglia'] },
      { id: 'g10-2', kind: 'fillBlank', prompt: 'Lui ____ (himself) lava.', answer: 'si' },
      { id: 'g10-3', kind: 'multipleChoice', prompt: "Translate: 'We have fun'", answer: 'Ci divertiamo', options: ['Ci divertiamo', 'Si divertiamo', 'Vi divertite', 'Mi diverto'] },
      { id: 'g10-4', kind: 'translation', prompt: 'You (plural) get dressed.', answer: 'Voi vi vestite.' },
      { id: 'g10-5', kind: 'fillBlank', prompt: 'Tu ____ (yourself) chiami Marco.', answer: 'ti' },
    ]
  }
];
