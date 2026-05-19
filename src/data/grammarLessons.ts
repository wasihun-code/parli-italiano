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
      "id": "l1",
      "title": "Articles (Definite, Indefinite, Partitive)",
      "description": "Master the use of articles in Italian, including the tricky partitive.",
      "explanation": [
        {
          "text": "Definite articles (il, lo, la, i, gli, le) specify a particular noun. Indefinite articles (un, uno, una, un') refer to any member of a class. Partitive articles (del, dello, della, dei, degli, delle) indicate 'some' or 'any' of an uncountable or plural noun.",
          "examples": [
            { "it": "Il libro è sul tavolo.", "en": "The book is on the table." },
            { "it": "Voglio una mela.", "en": "I want an apple." },
            { "it": "Vorrei del pane.", "en": "I would like some bread." }
          ]
        }
      ],
      "exercises": [
        { "id": "l1-e1", "kind": "multipleChoice", "prompt": "Choose the correct article for 'zaino' (masc. sing, starts with z):", "answer": "lo", "options": ["il", "lo", "la", "un"] },
        { "id": "l1-e2", "kind": "fillBlank", "prompt": "Vorrei ____ (some) acqua.", "answer": "dell'" },
        { "id": "l1-e3", "kind": "multipleChoice", "prompt": "Which is the definite article for 'amici'?", "answer": "gli", "options": ["i", "gli", "le", "degli"] }
      ]
    },
    {
      "id": "l2",
      "title": "Nouns (Gender, Number, Irregular Plurals)",
      "description": "Learn how nouns change based on gender and number, and watch out for irregulars.",
      "explanation": [
        {
          "text": "In Italian, nouns are either masculine or feminine. Generally, -o ends in masculine singular, -a in feminine singular. In plural, -o becomes -i, and -a becomes -e. However, many nouns ending in -e can be either gender and become -i in plural.",
          "examples": [
            { "it": "Il ragazzo / I ragazzi", "en": "The boy / The boys" },
            { "it": "La casa / Le case", "en": "The house / The houses" },
            { "it": "Il braccio / Le braccia", "en": "The arm / The arms (irregular)" }
          ]
        }
      ],
      "exercises": [
        { "id": "l2-e1", "kind": "fillBlank", "prompt": "Plural of 'fiore' (masc):", "answer": "fiori" },
        { "id": "l2-e2", "kind": "multipleChoice", "prompt": "What is the plural of 'uovo' (masc. sing)?", "answer": "uova (fem. plur)", "options": ["uovi", "uove", "uova", "uovo"] },
        { "id": "l2-e3", "kind": "fillBlank", "prompt": "Gender of 'mano':", "answer": "feminine" }
      ]
    },
    {
      "id": "l3",
      "title": "Adjectives (Agreement, Position, Irregulars)",
      "description": "How to describe things correctly in Italian.",
      "explanation": [
        {
          "text": "Adjectives must agree in gender and number with the noun they modify. Most adjectives follow the noun, but some common ones (like bello, bravo, buono, brutto, nuovo, vecchio, piccolo, grande) can precede it and may have irregular forms when they do.",
          "examples": [
            { "it": "Un libro interessante.", "en": "An interesting book." },
            { "it": "Un bel giorno.", "en": "A beautiful day." },
            { "it": "Delle persone gentili.", "en": "Kind people." }
          ]
        }
      ],
      "exercises": [
        { "id": "l3-e1", "kind": "multipleChoice", "prompt": "Correct form: 'Le ragazze ____'", "answer": "alte", "options": ["alto", "alta", "alti", "alte"] },
        { "id": "l3-e2", "kind": "fillBlank", "prompt": "Un ____ (good) amico.", "answer": "buon" },
        { "id": "l3-e3", "kind": "translation", "prompt": "A red car", "answer": "Una macchina rossa" }
      ]
    },
    {
      "id": "l4",
      "title": "Pronouns (Subject, Direct, Indirect, Reflexive, Possessive)",
      "description": "Master the various types of pronouns used in daily conversation.",
      "explanation": [
        {
          "text": "Subject pronouns (io, tu...) are often omitted. Direct object pronouns (mi, ti, lo, la...) replace the direct object. Indirect pronouns (mi, ti, gli, le...) indicate 'to whom'. Reflexive pronouns (mi, ti, si...) are used with reflexive verbs. Possessive pronouns (mio, tuo...) show ownership.",
          "examples": [
            { "it": "Lo vedo.", "en": "I see him/it." },
            { "it": "Gli parlo.", "en": "I speak to him." },
            { "it": "È il mio.", "en": "It is mine." }
          ]
        }
      ],
      "exercises": [
        { "id": "l4-e1", "kind": "multipleChoice", "prompt": "Replace 'a Marco': 'Dico a Marco' -> '____ dico'", "answer": "Gli", "options": ["Lo", "Gli", "Le", "Ci"] },
        { "id": "l4-e2", "kind": "fillBlank", "prompt": "Io ____ (myself) lavo le mani.", "answer": "mi" },
        { "id": "l4-e3", "kind": "multipleChoice", "prompt": "Which is 'ours'?", "answer": "il nostro", "options": ["mio", "tuo", "suo", "nostro"] }
      ]
    },
    {
      "id": "l5",
      "title": "Verbs (Present & Passato Prossimo)",
      "description": "Learn how to talk about the present and the recent past.",
      "explanation": [
        {
          "text": "The present tense is used for current actions. Passato prossimo uses 'avere' or 'essere' + past participle for completed past actions. Remember that with 'essere', the participle agrees with the subject.",
          "examples": [
            { "it": "Mangio una mela.", "en": "I eat an apple." },
            { "it": "Ho mangiato una mela.", "en": "I ate an apple." },
            { "it": "Sono andato a Roma.", "en": "I went to Rome." }
          ]
        }
      ],
      "exercises": [
        { "id": "l5-e1", "kind": "fillBlank", "prompt": "Io ____ (parlare) italiano.", "answer": "parlo" },
        { "id": "l5-e2", "kind": "multipleChoice", "prompt": "Past of 'lei parte':", "answer": "lei è partita", "options": ["lei ha partito", "lei è partito", "lei è partita", "lei ha partita"] },
        { "id": "l5-e3", "kind": "fillBlank", "prompt": "Noi ____ (avere) finito.", "answer": "abbiamo" }
      ]
    },
    {
      "id": "l6",
      "title": "Verbs (Imperfetto & Futuro)",
      "description": "Describing ongoing past actions and future events.",
      "explanation": [
        {
          "text": "Imperfetto is for habitual or ongoing past actions ('I used to', 'I was doing'). Futuro is for future events ('I will do').",
          "examples": [
            { "it": "Da bambino giocavo sempre.", "en": "As a child I always played." },
            { "it": "Domani studierò.", "en": "Tomorrow I will study." },
            { "it": "Mentre leggevo, lui dormiva.", "en": "While I was reading, he was sleeping." }
          ]
        }
      ],
      "exercises": [
        { "id": "l6-e1", "kind": "fillBlank", "prompt": "Loro ____ (erano - imperfetto) felici.", "answer": "erano" },
        { "id": "l6-e2", "kind": "multipleChoice", "prompt": "Future of 'noi andiamo':", "answer": "andremo", "options": ["andiamo", "andavamo", "andremo", "andremmo"] },
        { "id": "l6-e3", "kind": "fillBlank", "prompt": "Tu ____ (parlerai - futuro).", "answer": "parlerai" }
      ]
    },
    {
      "id": "l7",
      "title": "Verbs (Condizionale & Imperativo)",
      "description": "Expressing desires, possibilities, and giving commands.",
      "explanation": [
        {
          "text": "The conditional is used for 'would' (desires, polite requests). The imperative is for orders or suggestions.",
          "examples": [
            { "it": "Vorrei un caffè.", "en": "I would like a coffee." },
            { "it": "Vieni qui!", "en": "Come here!" },
            { "it": "Mangiate tutto!", "en": "Eat everything!" }
          ]
        }
      ],
      "exercises": [
        { "id": "l7-e1", "kind": "multipleChoice", "prompt": "Conditional of 'io faccio':", "answer": "farei", "options": ["faccio", "farò", "farei", "facessi"] },
        { "id": "l7-e2", "kind": "fillBlank", "prompt": "____ (Imperative 'Tu' - parlare)!", "answer": "Parla" },
        { "id": "l7-e3", "kind": "translation", "prompt": "I would go.", "answer": "Andrei." }
      ]
    },
    {
      "id": "l8",
      "title": "Introduction to Congiuntivo",
      "description": "Expressing doubts, hopes, and opinions.",
      "explanation": [
        {
          "text": "The subjunctive (congiuntivo) is used after verbs of emotion, doubt, or opinion, usually introduced by 'che'. It expresses subjectivity rather than fact.",
          "examples": [
            { "it": "Spero che tu stia bene.", "en": "I hope you are well." },
            { "it": "Credo che sia tardi.", "en": "I believe it's late." },
            { "it": "È necessario che lui venga.", "en": "It's necessary that he comes." }
          ]
        }
      ],
      "exercises": [
        { "id": "l8-e1", "kind": "fillBlank", "prompt": "Penso che lei ____ (sia) stanca.", "answer": "sia" },
        { "id": "l8-e2", "kind": "multipleChoice", "prompt": "Which is subjunctive?", "answer": "vada", "options": ["va", "andrà", "vada", "andava"] },
        { "id": "l8-e3", "kind": "translation", "prompt": "I hope he wins.", "answer": "Spero che vinca." }
      ]
    },
    {
      "id": "l9",
      "title": "Prepositions (Simple & Articulated)",
      "description": "Connecting words to show relationships in space and time.",
      "explanation": [
        {
          "text": "Simple prepositions (di, a, da, in, con, su, per, tra, fra) combine with definite articles to form articulated prepositions (e.g., in + il = nel).",
          "examples": [
            { "it": "Vado a casa.", "en": "I go home." },
            { "it": "Vado al cinema.", "en": "I go to the cinema." },
            { "it": "Il libro è sul tavolo.", "en": "The book is on the table." }
          ]
        }
      ],
      "exercises": [
        { "id": "l9-e1", "kind": "fillBlank", "prompt": "Siamo ____ (nella) cucina.", "answer": "nella" },
        { "id": "l9-e2", "kind": "multipleChoice", "prompt": "Combine 'di + gli':", "answer": "degli", "options": ["dei", "degli", "dagli", "sugli"] },
        { "id": "l9-e3", "kind": "fillBlank", "prompt": "Vado ____ (a) Roma.", "answer": "a" }
      ]
    },
    {
      "id": "l10",
      "title": "Negation and Word Order",
      "description": "How to say 'no' and how to structure your sentences.",
      "explanation": [
        {
          "text": "To negate, put 'non' before the verb. Standard word order is Subject-Verb-Object, but Italian is flexible. Adjectives usually follow nouns.",
          "examples": [
            { "it": "Non capisco.", "en": "I don't understand." },
            { "it": "Io mangio la mela.", "en": "I eat the apple." },
            { "it": "Una macchina rossa.", "en": "A red car." }
          ]
        }
      ],
      "exercises": [
        { "id": "l10-e1", "kind": "translation", "prompt": "I do not work.", "answer": "Non lavoro." },
        { "id": "l10-e2", "kind": "multipleChoice", "prompt": "Correct order:", "answer": "Un gatto nero", "options": ["Un nero gatto", "Un gatto nero", "Gatto un nero", "Nero un gatto"] },
        { "id": "l10-e3", "kind": "fillBlank", "prompt": "Lui ____ (non) parla.", "answer": "non" }
      ]
    },
    {
      "id": "l11",
      "title": "Comparatives and Superlatives",
      "description": "Comparing things and expressing the highest degree.",
      "explanation": [
        {
          "text": "Comparatives use 'più... di' (more than) or 'meno... di' (less than). Relative superlatives use 'il più/meno...', and absolute superlatives use the suffix '-issimo'.",
          "examples": [
            { "it": "Marco è più alto di me.", "en": "Marco is taller than me." },
            { "it": "La pizza è buonissima!", "en": "The pizza is very good!" },
            { "it": "È il film più bello.", "en": "It's the most beautiful movie." }
          ]
        }
      ],
      "exercises": [
        { "id": "l11-e1", "kind": "fillBlank", "prompt": "Lei è ____ (più) intelligente di lui.", "answer": "più" },
        { "id": "l11-e2", "kind": "multipleChoice", "prompt": "Translate 'very fast':", "answer": "velocissimo", "options": ["veloce", "più veloce", "velocissimo", "il più veloce"] },
        { "id": "l11-e3", "kind": "translation", "prompt": "He is less tall than you.", "answer": "Lui è meno alto di te." }
      ]
    },
    {
      "id": "l12",
      "title": "Conjunctions (e, ma, perché, quando, se)",
      "description": "Words that connect sentences and ideas.",
      "explanation": [
        {
          "text": "Conjunctions connect words or clauses. 'E' (and), 'ma' (but), 'perché' (because/why), 'quando' (when), 'se' (if) are the most common.",
          "examples": [
            { "it": "Pane e burro.", "en": "Bread and butter." },
            { "it": "Vengo se posso.", "en": "I'll come if I can." },
            { "it": "Sono felice perché è sabato.", "en": "I'm happy because it's Saturday." }
          ]
        }
      ],
      "exercises": [
        { "id": "l12-e1", "kind": "fillBlank", "prompt": "Non so ____ (se) lui viene.", "answer": "se" },
        { "id": "l12-e2", "kind": "multipleChoice", "prompt": "Which means 'but'?", "answer": "ma", "options": ["e", "ma", "perché", "quando"] },
        { "id": "l12-e3", "kind": "fillBlank", "prompt": "Chiamami ____ (quando) arrivi.", "answer": "quando" }
      ]
    }
];
