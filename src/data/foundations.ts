export type FoundationExerciseKind = 'flashcard' | 'fillBlank' | 'listening' | 'multipleChoice';

export type FoundationTerm = {
  id: string;
  italian: string;
  english: string;
  note?: string;
};

export type FoundationExercise = {
  id: string;
  kind: FoundationExerciseKind;
  prompt: string;
  answer: string;
  options?: string[];
  lessonId?: number;
};

export type FoundationLesson = {
  id: number;
  title: string;
  description: string;
  terms: FoundationTerm[];
  exercises: FoundationExercise[];
};

export const foundationLessons: FoundationLesson[] = [
  {
    id: 1,
    title: 'People and Essere',
    description: 'Subject pronouns and the auxiliary verb essere (to be).',
    terms: [
      {id: 'f1-io', italian: 'io', english: 'I'},
      {id: 'f1-sono-io', italian: 'sono', english: 'I am'},
      {id: 'f1-tu', italian: 'tu', english: 'you'},
      {id: 'f1-sei', italian: 'sei', english: 'you are'},
      {id: 'f1-lui', italian: 'lui', english: 'he'},
      {id: 'f1-lei', italian: 'lei', english: 'she'},
      {id: 'f1-e', italian: 'è', english: 'is'},
      {id: 'f1-noi', italian: 'noi', english: 'we'},
      {id: 'f1-siamo', italian: 'siamo', english: 'we are'},
      {id: 'f1-voi', italian: 'voi', english: 'you all'},
      {id: 'f1-siete', italian: 'siete', english: 'you all are'},
      {id: 'f1-loro', italian: 'loro', english: 'they'},
      {id: 'f1-sono-loro', italian: 'sono', english: 'they are'},
    ],
    exercises: [
      {id: 'f1-e1', kind: 'multipleChoice', prompt: "Translate 'I am'", answer: 'io sono', options: ['io sono', 'tu sei', 'lui è', 'noi siamo']},
      {id: 'f1-e2', kind: 'fillBlank', prompt: "Tu ____ (are) italiano.", answer: 'sei'},
      {id: 'f1-e3', kind: 'multipleChoice', prompt: "Translate 'We are'", answer: 'noi siamo', options: ['noi siamo', 'voi siete', 'loro sono', 'io sono']},
      {id: 'f1-e4', kind: 'fillBlank', prompt: "Lui ____ (is) felice.", answer: 'è'},
      {id: 'f1-e5', kind: 'multipleChoice', prompt: "How do you say 'They are'?", answer: 'loro sono', options: ['loro sono', 'noi siamo', 'io sono', 'voi siete']},
      {id: 'f1-e6', kind: 'fillBlank', prompt: "Voi ____ (are) a Roma.", answer: 'siete'},
      {id: 'f1-e7', kind: 'multipleChoice', prompt: "Translate 'You (singular) are'", answer: 'tu sei', options: ['tu sei', 'io sono', 'lei è', 'noi siamo']},
      {id: 'f1-e8', kind: 'fillBlank', prompt: "Io ____ (am) uno studente.", answer: 'sono'},
      {id: 'f1-e9', kind: 'multipleChoice', prompt: "Translate 'She is'", answer: 'lei è', options: ['lei è', 'lui è', 'io sono', 'noi siamo']},
      {id: 'f1-e10', kind: 'fillBlank', prompt: "Noi ____ (are) amici.", answer: 'siamo'},
    ]
  },
  {
    id: 2,
    title: 'Core Prepositions',
    description: 'Small connector words: da, di, a, in, con, su, per, tra/fra.',
    terms: [
      {id: 'f2-da', italian: 'da', english: 'from / at'},
      {id: 'f2-di', italian: 'di', english: 'of / from'},
      {id: 'f2-a', italian: 'a', english: 'to / at'},
      {id: 'f2-in', italian: 'in', english: 'in / to'},
      {id: 'f2-con', italian: 'con', english: 'with'},
      {id: 'f2-su', italian: 'su', english: 'on'},
      {id: 'f2-per', italian: 'per', english: 'for / through'},
      {id: 'f2-tra', italian: 'tra', english: 'between / among'},
      {id: 'f2-fra', italian: 'fra', english: 'between / among'},
    ],
    exercises: [
      {id: 'f2-e1', kind: 'multipleChoice', prompt: "Translate 'with'", answer: 'con', options: ['con', 'di', 'a', 'in']},
      {id: 'f2-e2', kind: 'fillBlank', prompt: "Vado ____ (to) Roma.", answer: 'a'},
      {id: 'f2-e3', kind: 'multipleChoice', prompt: "Translate 'for'", answer: 'per', options: ['per', 'su', 'da', 'tra']},
      {id: 'f2-e4', kind: 'fillBlank', prompt: "Il libro è ____ (of) Marco.", answer: 'di'},
      {id: 'f2-e5', kind: 'multipleChoice', prompt: "Translate 'on'", answer: 'su', options: ['su', 'in', 'con', 'per']},
      {id: 'f2-e6', kind: 'fillBlank', prompt: "Vivo ____ (in) Italia.", answer: 'in'},
      {id: 'f2-e7', kind: 'multipleChoice', prompt: "Translate 'from'", answer: 'da', options: ['da', 'di', 'a', 'in']},
      {id: 'f2-e8', kind: 'fillBlank', prompt: "Caffè ____ (with) latte.", answer: 'con'},
      {id: 'f2-e9', kind: 'multipleChoice', prompt: "Translate 'between'", answer: 'tra', options: ['tra', 'per', 'su', 'di']},
      {id: 'f2-e10', kind: 'fillBlank', prompt: "Un regalo ____ (for) te.", answer: 'per'},
    ]
  },
  {
    id: 3,
    title: 'Articles',
    description: 'Definite and indefinite articles used in everyday speech.',
    terms: [
      {id: 'f3-il', italian: 'il', english: 'the, masculine singular'},
      {id: 'f3-la', italian: 'la', english: 'the, feminine singular'},
      {id: 'f3-i', italian: 'i', english: 'the, masculine plural'},
      {id: 'f3-le', italian: 'le', english: 'the, feminine plural'},
      {id: 'f3-un', italian: 'un', english: 'a / an, masculine'},
      {id: 'f3-una', italian: 'una', english: 'a / an, feminine'},
      {id: 'f3-uno', italian: 'uno', english: 'a / an, masculine before z/s+consonant'},
    ],
    exercises: [
      {id: 'f3-e1', kind: 'multipleChoice', prompt: "Choose the correct article: '____ libro' (masc.)", answer: 'il', options: ['il', 'la', 'lo', 'le']},
      {id: 'f3-e2', kind: 'fillBlank', prompt: "____ (The) ragazza è bella.", answer: 'la'},
      {id: 'f3-e3', kind: 'multipleChoice', prompt: "Choose the correct article: '____ studente' (z/s+cons.)", answer: 'lo', options: ['lo', 'il', 'la', 'i']},
      {id: 'f3-e4', kind: 'fillBlank', prompt: "____ (A) caffè, per favore.", answer: 'un'},
      {id: 'f3-e5', kind: 'multipleChoice', prompt: "Choose the correct plural article: '____ libri'", answer: 'i', options: ['i', 'le', 'gli', 'la']},
      {id: 'f3-e6', kind: 'fillBlank', prompt: "____ (The) pizze sono buone.", answer: 'le'},
      {id: 'f3-e7', kind: 'multipleChoice', prompt: "Indefinite article for '____ borsa'", answer: 'una', options: ['una', 'un', 'uno', 'la']},
      {id: 'f3-e8', kind: 'fillBlank', prompt: "____ (A) zaino (z/s+cons.)", answer: 'uno'},
      {id: 'f3-e9', kind: 'multipleChoice', prompt: "Translate 'the houses'", answer: 'le case', options: ['le case', 'i case', 'la case', 'gli case']},
      {id: 'f3-e10', kind: 'fillBlank', prompt: "____ (The) ragazzi sono qui.", answer: 'i'},
    ]
  },
  {
    id: 4,
    title: 'Question and Place Words',
    description: 'Pointing, place, time, manner, and reason words for simple questions.',
    terms: [
      {id: 'f4-questo', italian: 'questo', english: 'this'},
      {id: 'f4-quello', italian: 'quello', english: 'that'},
      {id: 'f4-qui', italian: 'qui', english: 'here'},
      {id: 'f4-la', italian: 'là', english: 'there'},
      {id: 'f4-dove', italian: 'dove', english: 'where'},
      {id: 'f4-quando', italian: 'quando', english: 'when'},
      {id: 'f4-come', italian: 'come', english: 'how / as'},
      {id: 'f4-perche', italian: 'perché', english: 'why / because'},
    ],
    exercises: [
      {id: 'f4-e1', kind: 'multipleChoice', prompt: "Translate 'Where'", answer: 'dove', options: ['dove', 'chi', 'cosa', 'quando']},
      {id: 'f4-e2', kind: 'fillBlank', prompt: "____ (What) fai?", answer: 'cosa'},
      {id: 'f4-e3', kind: 'multipleChoice', prompt: "Translate 'Who'", answer: 'chi', options: ['chi', 'come', 'perché', 'quando']},
      {id: 'f4-e4', kind: 'fillBlank', prompt: "____ (Where) è il bagno?", answer: 'dove'},
      {id: 'f4-e5', kind: 'multipleChoice', prompt: "Translate 'Why'", answer: 'perché', options: ['perché', 'quando', 'come', 'chi']},
      {id: 'f4-e6', kind: 'fillBlank', prompt: "____ (How) stai?", answer: 'come'},
      {id: 'f4-e7', kind: 'multipleChoice', prompt: "Translate 'This'", answer: 'questo', options: ['questo', 'quello', 'qui', 'là']},
      {id: 'f4-e8', kind: 'fillBlank', prompt: "____ (That) libro è mio.", answer: 'quello'},
      {id: 'f4-e9', kind: 'multipleChoice', prompt: "Translate 'When'", answer: 'quando', options: ['quando', 'cosa', 'dove', 'come']},
      {id: 'f4-e10', kind: 'fillBlank', prompt: "____ (Who) è lui?", answer: 'chi'},
    ]
  },
  {
    id: 5,
    title: 'Core Verbs and Negation',
    description: 'Full present-tense conjugations for essere, avere, fare, andare, volere, potere, dovere, plus non.',
    terms: [
      {id: 'f5-non', italian: 'non', english: 'not'},
      {id: 'f5-essere-io', italian: 'io sono', english: 'I am'},
      {id: 'f5-essere-tu', italian: 'tu sei', english: 'you are'},
      {id: 'f5-essere-lui', italian: 'lui/lei è', english: 'he/she is'},
      {id: 'f5-essere-noi', italian: 'noi siamo', english: 'we are'},
      {id: 'f5-essere-voi', italian: 'voi siete', english: 'you all are'},
      {id: 'f5-essere-loro', italian: 'loro sono', english: 'they are'},
      {id: 'f5-avere-io', italian: 'io ho', english: 'I have'},
      {id: 'f5-avere-tu', italian: 'tu hai', english: 'you have'},
      {id: 'f5-avere-lui', italian: 'lui/lei ha', english: 'he/she has'},
      {id: 'f5-avere-noi', italian: 'noi abbiamo', english: 'we have'},
      {id: 'f5-avere-voi', italian: 'voi avete', english: 'you all have'},
      {id: 'f5-avere-loro', italian: 'loro hanno', english: 'they have'},
      {id: 'f5-fare-io', italian: 'io faccio', english: 'I do / make'},
      {id: 'f5-fare-tu', italian: 'tu fai', english: 'you do / make'},
      {id: 'f5-fare-lui', italian: 'lui/lei fa', english: 'he/she does / makes'},
      {id: 'f5-fare-noi', italian: 'noi facciamo', english: 'we do / make'},
      {id: 'f5-fare-voi', italian: 'voi fate', english: 'you all do / make'},
      {id: 'f5-fare-loro', italian: 'loro fanno', english: 'they do / make'},
      {id: 'f5-andare-io', italian: 'io vado', english: 'I go'},
      {id: 'f5-andare-tu', italian: 'tu vai', english: 'you go'},
      {id: 'f5-andare-lui', italian: 'lui/lei va', english: 'he/she goes'},
      {id: 'f5-andare-noi', italian: 'noi andiamo', english: 'we go'},
      {id: 'f5-andare-voi', italian: 'voi andate', english: 'you all go'},
      {id: 'f5-andare-loro', italian: 'loro vanno', english: 'they go'},
      {id: 'f5-volere-io', italian: 'io voglio', english: 'I want'},
      {id: 'f5-volere-tu', italian: 'tu vuoi', english: 'you want'},
      {id: 'f5-volere-lui', italian: 'lui/lei vuole', english: 'he/she wants'},
      {id: 'f5-volere-noi', italian: 'noi vogliamo', english: 'we want'},
      {id: 'f5-volere-voi', italian: 'voi volete', english: 'you all want'},
      {id: 'f5-volere-loro', italian: 'loro vogliono', english: 'they want'},
      {id: 'f5-potere-io', italian: 'io posso', english: 'I can'},
      {id: 'f5-potere-tu', italian: 'tu puoi', english: 'you can'},
      {id: 'f5-potere-lui', italian: 'lui/lei può', english: 'he/she can'},
      {id: 'f5-potere-noi', italian: 'noi possiamo', english: 'we can'},
      {id: 'f5-potere-voi', italian: 'voi potete', english: 'you all can'},
      {id: 'f5-potere-loro', italian: 'loro possono', english: 'they can'},
      {id: 'f5-dovere-io', italian: 'io devo', english: 'I must / have to'},
      {id: 'f5-dovere-tu', italian: 'tu devi', english: 'you must / have to'},
      {id: 'f5-dovere-lui', italian: 'lui/lei deve', english: 'he/she must / has to'},
      {id: 'f5-dovere-noi', italian: 'noi dobbiamo', english: 'we must / have to'},
      {id: 'f5-dovere-voi', italian: 'voi dovete', english: 'you all must / have to'},
      {id: 'f5-dovere-loro', italian: 'loro devono', english: 'they must / have to'},
    ],
    exercises: [
      {id: 'f5-e1', kind: 'multipleChoice', prompt: "Translate 'I have'", answer: 'io ho', options: ['io ho', 'tu hai', 'lui ha', 'io sono']},
      {id: 'f5-e2', kind: 'fillBlank', prompt: "Io ____ (go) a casa.", answer: 'vado'},
      {id: 'f5-e3', kind: 'multipleChoice', prompt: "Translate 'I do not have'", answer: 'non ho', options: ['non ho', 'ho non', 'no ho', 'non sono']},
      {id: 'f5-e4', kind: 'fillBlank', prompt: "Lui ____ (has) fame.", answer: 'ha'},
      {id: 'f5-e5', kind: 'multipleChoice', prompt: "Translate 'He does'", answer: 'lui fa', options: ['lui fa', 'lui va', 'lui ha', 'lui è']},
      {id: 'f5-e6', kind: 'fillBlank', prompt: "Lei ____ (goes) al lavoro.", answer: 'va'},
      {id: 'f5-e7', kind: 'multipleChoice', prompt: "Translate 'What are you doing?'", answer: 'cosa fai?', options: ['cosa fai?', 'cosa vai?', 'cosa hai?', 'chi sei?']},
      {id: 'f5-e8', kind: 'fillBlank', prompt: "Io ____ (do) colazione.", answer: 'faccio'},
      {id: 'f5-e9', kind: 'multipleChoice', prompt: "Translate 'You (plural) have'", answer: 'voi avete', options: ['voi avete', 'noi abbiamo', 'loro hanno', 'tu hai']},
      {id: 'f5-e10', kind: 'fillBlank', prompt: "Noi ____ (go) al mare.", answer: 'andiamo'},
    ]
  },
];

export const placementTest: FoundationExercise[] = [
  // Pronouns and Essere
  { id: 'pt-1', kind: 'multipleChoice', prompt: "Choose the correct translation for 'I am American'", answer: "Io sono americano", options: ["Io sono americano", "Tu sei americano", "Lui è americano", "Noi siamo americani"], lessonId: 1 },
  { id: 'pt-2', kind: 'fillBlank', prompt: "Complete with 'essere': Noi ____ a casa.", answer: "siamo", lessonId: 1 },
  { id: 'pt-3', kind: 'multipleChoice', prompt: "Translate: 'They are students'", answer: "Loro sono studenti", options: ["Loro sono studenti", "Voi siete studenti", "Noi siamo studenti", "Lui è studente"], lessonId: 1 },
  
  // Articles
  { id: 'pt-4', kind: 'multipleChoice', prompt: "Choose the correct article: '____ ragazza' (girl)", answer: "La", options: ["Il", "La", "Lo", "Le"], lessonId: 3 },
  { id: 'pt-5', kind: 'multipleChoice', prompt: "Choose the correct article: '____ ragazzo' (boy)", answer: "Il", options: ["Il", "La", "Lo", "I"], lessonId: 3 },
  { id: 'pt-6', kind: 'fillBlank', prompt: "Complete with the correct definite article (plural): ____ gatti sono neri.", answer: "I", lessonId: 3 },
  { id: 'pt-7', kind: 'multipleChoice', prompt: "Choose the correct indefinite article: '____ caffè'", answer: "Un", options: ["Un", "Uno", "Una", "Un'"], lessonId: 3 },
  { id: 'pt-8', kind: 'multipleChoice', prompt: "Choose the correct article: '____ zaino' (backpack)", answer: "Uno", options: ["Un", "Uno", "Una", "Lo"], lessonId: 3 },

  // Prepositions
  { id: 'pt-9', kind: 'multipleChoice', prompt: "Translate: 'The book is on the table'", answer: "Il libro è sul tavolo", options: ["Il libro è sul tavolo", "Il libro è nel tavolo", "Il libro è con tavolo", "Il libro è per tavolo"], lessonId: 2 },
  { id: 'pt-10', kind: 'fillBlank', prompt: "Complete with 'to': Vado ____ Roma.", answer: "a", lessonId: 2 },
  { id: 'pt-11', kind: 'fillBlank', prompt: "Complete with 'in': Vivo ____ Italia.", answer: "in", lessonId: 2 },
  { id: 'pt-12', kind: 'multipleChoice', prompt: "Translate: 'With my friends'", answer: "Con i miei amici", options: ["Con i miei amici", "Di i miei amici", "A i miei amici", "Per i miei amici"], lessonId: 2 },

  // Core Verbs
  { id: 'pt-13', kind: 'multipleChoice', prompt: "Translate: 'I have a car'", answer: "Io ho una macchina", options: ["Io ho una macchina", "Io sono una macchina", "Io faccio una macchina", "Io vado una macchina"], lessonId: 5 },
  { id: 'pt-14', kind: 'fillBlank', prompt: "Complete with 'avere': Tu ____ un fratello?", answer: "hai", lessonId: 5 },
  { id: 'pt-15', kind: 'multipleChoice', prompt: "Translate: 'What are you doing?'", answer: "Cosa fai?", options: ["Cosa fai?", "Dove vai?", "Chi sei?", "Quanto costa?"], lessonId: 5 },
  { id: 'pt-16', kind: 'fillBlank', prompt: "Complete with 'andare': Domani noi ____ al cinema.", answer: "andiamo", lessonId: 5 },
  { id: 'pt-17', kind: 'multipleChoice', prompt: "Translate: 'He wants a pizza'", answer: "Lui vuole una pizza", options: ["Lui vuole una pizza", "Lui può una pizza", "Lui deve una pizza", "Lui fa una pizza"], lessonId: 5 },

  // Question and Place Words
  { id: 'pt-18', kind: 'multipleChoice', prompt: "Translate: 'Where is the bathroom?'", answer: "Dove è il bagno?", options: ["Dove è il bagno?", "Chi è il bagno?", "Quando è il bagno?", "Come è il bagno?"], lessonId: 4 },
  { id: 'pt-19', kind: 'fillBlank', prompt: "Translate 'Why': ____ studi l'italiano?", answer: "Perché", lessonId: 4 },
  { id: 'pt-20', kind: 'multipleChoice', prompt: "Translate: 'This book is interesting'", answer: "Questo libro è interessante", options: ["Questo libro è interessante", "Quello libro è interessante", "Qui libro è interessante", "Cosa libro è interessante"], lessonId: 4 },

  // Numbers and Colors
  { id: 'pt-21', kind: 'multipleChoice', prompt: "How many is 'Tre'?", answer: "3", options: ["2", "3", "4", "5"], lessonId: 0 },
  { id: 'pt-22', kind: 'multipleChoice', prompt: "Which color is 'Rosso'?", answer: "Red", options: ["Blue", "Red", "Green", "Yellow"], lessonId: 0 },
  { id: 'pt-23', kind: 'fillBlank', prompt: "The Italian word for '8' is: ____", answer: "otto", lessonId: 0 },

  // Negation and Mixed
  { id: 'pt-24', kind: 'multipleChoice', prompt: "Translate: 'I don't know'", answer: "Non so", options: ["Non so", "No so", "Non conosco", "So non"], lessonId: 5 },
  { id: 'pt-25', kind: 'multipleChoice', prompt: "Translate: 'How much does it cost?'", answer: "Quanto costa?", options: ["Quanto costa?", "Quando costa?", "Quale costa?", "Cosa costa?"], lessonId: 4 },
  { id: 'pt-26', kind: 'fillBlank', prompt: "Translate 'Please': Per ____", answer: "favore", lessonId: 0 },
];

export const foundationalVocabulary = foundationLessons.flatMap(lesson =>
  lesson.terms.map(term => term.italian),
);
