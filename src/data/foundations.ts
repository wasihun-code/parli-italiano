export type FoundationExerciseKind = 'flashcard' | 'fillBlank' | 'listening';

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
};

export type FoundationLesson = {
  id: number;
  title: string;
  description: string;
  terms: FoundationTerm[];
  exercises: FoundationExercise[];
};

const lessonOneTerms: FoundationTerm[] = [
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
];

const lessonTwoTerms: FoundationTerm[] = [
  {id: 'f2-da', italian: 'da', english: 'from / at'},
  {id: 'f2-di', italian: 'di', english: 'of / from'},
  {id: 'f2-a', italian: 'a', english: 'to / at'},
  {id: 'f2-in', italian: 'in', english: 'in / to'},
  {id: 'f2-con', italian: 'con', english: 'with'},
  {id: 'f2-su', italian: 'su', english: 'on'},
  {id: 'f2-per', italian: 'per', english: 'for / through'},
  {id: 'f2-tra', italian: 'tra', english: 'between / among'},
  {id: 'f2-fra', italian: 'fra', english: 'between / among'},
];

const lessonThreeTerms: FoundationTerm[] = [
  {id: 'f3-il', italian: 'il', english: 'the, masculine singular'},
  {id: 'f3-la', italian: 'la', english: 'the, feminine singular'},
  {id: 'f3-i', italian: 'i', english: 'the, masculine plural'},
  {id: 'f3-le', italian: 'le', english: 'the, feminine plural'},
  {id: 'f3-un', italian: 'un', english: 'a / an, masculine'},
  {id: 'f3-una', italian: 'una', english: 'a / an, feminine'},
  {id: 'f3-uno', italian: 'uno', english: 'a / an, masculine before z/s+consonant'},
];

const lessonFourTerms: FoundationTerm[] = [
  {id: 'f4-questo', italian: 'questo', english: 'this'},
  {id: 'f4-quello', italian: 'quello', english: 'that'},
  {id: 'f4-qui', italian: 'qui', english: 'here'},
  {id: 'f4-la', italian: 'là', english: 'there'},
  {id: 'f4-dove', italian: 'dove', english: 'where'},
  {id: 'f4-quando', italian: 'quando', english: 'when'},
  {id: 'f4-come', italian: 'come', english: 'how / as'},
  {id: 'f4-perche', italian: 'perché', english: 'why / because'},
];

const lessonFiveTerms: FoundationTerm[] = [
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
];

function buildExercises(
  lessonId: number,
  terms: FoundationTerm[],
): FoundationExercise[] {
  return terms.slice(0, 10).flatMap((term, index) => {
    const options = [
      term.italian,
      ...terms
        .filter(option => option.id !== term.id)
        .slice(index % Math.max(terms.length - 1, 1), terms.length)
        .concat(terms)
        .map(option => option.italian)
        .filter((option, optionIndex, allOptions) => allOptions.indexOf(option) === optionIndex)
        .slice(0, 3),
    ];

    return [
      {
        id: `f${lessonId}-flashcard-${index + 1}`,
        kind: 'flashcard' as const,
        prompt: term.english,
        answer: term.italian,
        options,
      },
      {
        id: `f${lessonId}-fill-${index + 1}`,
        kind: 'fillBlank' as const,
        prompt: `${term.english}: ____`,
        answer: term.italian,
      },
      {
        id: `f${lessonId}-listening-${index + 1}`,
        kind: 'listening' as const,
        prompt: `Listen and choose: ${term.english}`,
        answer: term.italian,
        options,
      },
    ];
  });
}

export const foundationLessons: FoundationLesson[] = [
  {
    id: 1,
    title: 'People and Essere',
    description: 'Subject pronouns and the most common present-tense forms of essere.',
    terms: lessonOneTerms,
    exercises: buildExercises(1, lessonOneTerms),
  },
  {
    id: 2,
    title: 'Core Prepositions',
    description: 'Small connector words that make A1 phrases understandable.',
    terms: lessonTwoTerms,
    exercises: buildExercises(2, lessonTwoTerms),
  },
  {
    id: 3,
    title: 'Articles',
    description: 'Definite and indefinite articles used in everyday speech.',
    terms: lessonThreeTerms,
    exercises: buildExercises(3, lessonThreeTerms),
  },
  {
    id: 4,
    title: 'Question and Place Words',
    description: 'Pointing, place, time, manner, and reason words for simple questions.',
    terms: lessonFourTerms,
    exercises: buildExercises(4, lessonFourTerms),
  },
  {
    id: 5,
    title: 'Core Verbs and Negation',
    description: 'Full present-tense conjugations for essere, avere, fare, andare, volere, potere, dovere, plus non.',
    terms: lessonFiveTerms,
    exercises: buildExercises(5, lessonFiveTerms),
  },
];

export const foundationalVocabulary = foundationLessons.flatMap(lesson =>
  lesson.terms.map(term => term.italian),
);
