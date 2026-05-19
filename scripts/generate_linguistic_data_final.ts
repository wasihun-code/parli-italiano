
import * as fs from 'fs';

const translationSentences = [
  // Difficulty 1
  { italian: "Io mangio.", english: "I eat.", difficulty: 1 },
  { italian: "Tu bevi.", english: "You drink.", difficulty: 1 },
  { italian: "Lei legge.", english: "She reads.", difficulty: 1 },
  { italian: "Noi andiamo.", english: "We go.", difficulty: 1 },
  { italian: "Voi parlate.", english: "You all speak.", difficulty: 1 },
  { italian: "Loro ridono.", english: "They laugh.", difficulty: 1 },
  { italian: "Il gatto dorme.", english: "The cat sleeps.", difficulty: 1 },
  { italian: "La mela è rossa.", english: "The apple is red.", difficulty: 1 },
  { italian: "Il cane corre.", english: "The dog runs.", difficulty: 1 },
  { italian: "Fa caldo.", english: "It is hot.", difficulty: 1 },
  { italian: "Ho fame.", english: "I am hungry.", difficulty: 1 },
  { italian: "Mi piace la pizza.", english: "I like pizza.", difficulty: 1 },
  { italian: "Dove sei?", english: "Where are you?", difficulty: 1 },
  { italian: "Come stai?", english: "How are you?", difficulty: 1 },
  { italian: "Buongiorno signore.", english: "Good morning sir.", difficulty: 1 },
  { italian: "Arrivederci.", english: "Goodbye.", difficulty: 1 },
  { italian: "Grazie mille.", english: "Thanks a lot.", difficulty: 1 },
  { italian: "Mi chiamo Paolo.", english: "My name is Paolo.", difficulty: 1 },
  { italian: "Piacere di conoscerti.", english: "Nice to meet you.", difficulty: 1 },
  { italian: "Scusi, dov'è il bagno?", english: "Excuse me, where is the bathroom?", difficulty: 1 },
  { italian: "Quanto costa?", english: "How much does it cost?", difficulty: 1 },
  { italian: "È molto caro.", english: "It is very expensive.", difficulty: 1 },
  { italian: "Voglio un caffè.", english: "I want a coffee.", difficulty: 1 },
  { italian: "Prendo un gelato.", english: "I'll have an ice cream.", difficulty: 1 },
  { italian: "Il libro è sul tavolo.", english: "The book is on the table.", difficulty: 1 },
  { italian: "La chiave è qui.", english: "The key is here.", difficulty: 1 },
  { italian: "Siamo pronti.", english: "We are ready.", difficulty: 1 },
  { italian: "Sono le tre.", english: "It is three o'clock.", difficulty: 1 },
  { italian: "Che tempo fa?", english: "How is the weather?", difficulty: 1 },
  { italian: "Piove oggi.", english: "It is raining today.", difficulty: 1 },
  { italian: "Ho un cane.", english: "I have a dog.", difficulty: 1 },
  { italian: "Sei stanco?", english: "Are you tired?", difficulty: 1 },
  { italian: "Lei è bella.", english: "She is beautiful.", difficulty: 1 },
  { italian: "Loro sono felici.", english: "They are happy.", difficulty: 1 },

  // Difficulty 2
  { italian: "Ieri ho mangiato una pizza molto buona.", english: "Yesterday I ate a very good pizza.", difficulty: 2 },
  { italian: "Mia sorella vive in una casa grande.", english: "My sister lives in a big house.", difficulty: 2 },
  { italian: "Domani andremo al mare con gli amici.", english: "Tomorrow we will go to the sea with friends.", difficulty: 2 },
  { italian: "Non posso venire perché devo studiare molto.", english: "I cannot come because I have to study a lot.", difficulty: 2 },
  { italian: "Abbiamo comprato un nuovo computer per l'ufficio.", english: "We bought a new computer for the office.", difficulty: 2 },
  { italian: "Il treno parte alle otto e mezza.", english: "The train leaves at eight thirty.", difficulty: 2 },
  { italian: "Mi piace ascoltare la musica mentre cucino.", english: "I like listening to music while I cook.", difficulty: 2 },
  { italian: "Hai visto il film di cui ti parlavo?", english: "Have you seen the movie I was telling you about?", difficulty: 2 },
  { italian: "La macchina di Marco è sempre molto pulita.", english: "Marco's car is always very clean.", difficulty: 2 },
  { italian: "Quando ero piccolo giocavo sempre a calcio.", english: "When I was little I always played soccer.", difficulty: 2 },
  { italian: "Spero che tu possa venire alla festa.", english: "I hope you can come to the party.", difficulty: 2 },
  { italian: "Vorrei un bicchiere di vino rosso, grazie.", english: "I would like a glass of red wine, thank you.", difficulty: 2 },
  { italian: "Gli studenti leggono i libri in biblioteca.", english: "The students read books in the library.", difficulty: 2 },
  { italian: "Ho dimenticato le chiavi della macchina a casa.", english: "I forgot the car keys at home.", difficulty: 2 },
  { italian: "Fa troppo freddo per uscire senza cappotto.", english: "It is too cold to go out without a coat.", difficulty: 2 },
  { italian: "Mi sono svegliato presto per andare a correre.", english: "I woke up early to go for a run.", difficulty: 2 },
  { italian: "Lei parla italiano meglio di suo fratello.", english: "She speaks Italian better than her brother.", difficulty: 2 },
  { italian: "Dove hai comprato quelle scarpe così belle?", english: "Where did you buy those beautiful shoes?", difficulty: 2 },
  { italian: "C'è molta gente in centro stasera.", english: "There are many people downtown tonight.", difficulty: 2 },
  { italian: "Mi dispiace, ma non capisco cosa dici.", english: "I'm sorry, but I don't understand what you're saying.", difficulty: 2 },
  { italian: "Il ristorante apre alle sette per la cena.", english: "The restaurant opens at seven for dinner.", difficulty: 2 },
  { italian: "Dobbiamo finire questo lavoro entro domani sera.", english: "We must finish this work by tomorrow evening.", difficulty: 2 },
  { italian: "Hai fame o vuoi solo bere qualcosa?", english: "Are you hungry or do you just want to drink something?", difficulty: 2 },
  { italian: "Mi piace passeggiare nel parco la domenica.", english: "I like walking in the park on Sundays.", difficulty: 2 },
  { italian: "Mio padre lavora in banca da vent'anni.", english: "My father has worked in a bank for twenty years.", difficulty: 2 },
  { italian: "Ti va di andare al cinema stasera?", english: "Do you feel like going to the cinema tonight?", difficulty: 2 },
  { italian: "Non ho mai visitato la città di Roma.", english: "I have never visited the city of Rome.", difficulty: 2 },
  { italian: "La torta che ha fatto mia madre è deliziosa.", english: "The cake my mother made is delicious.", difficulty: 2 },
  { italian: "Cerco un regalo per il compleanno di Giulia.", english: "I'm looking for a gift for Giulia's birthday.", difficulty: 2 },
  { italian: "Fa bel tempo, andiamo a fare una passeggiata?", english: "The weather is nice, shall we go for a walk?", difficulty: 2 },
  { italian: "Ho incontrato il tuo amico al supermercato ieri.", english: "I met your friend at the supermarket yesterday.", difficulty: 2 },
  { italian: "Non so se ho abbastanza soldi per questo.", english: "I don't know if I have enough money for this.", difficulty: 2 },
  { italian: "Lei si veste sempre in modo molto elegante.", english: "She always dresses in a very elegant way.", difficulty: 2 },

  // Difficulty 3
  { italian: "Se avessi più tempo libero, imparerei a suonare il pianoforte.", english: "If I had more free time, I would learn to play the piano.", difficulty: 3 },
  { italian: "Sebbene piovesse a dirotto, siamo usciti comunque a fare una passeggiata.", english: "Even though it was raining cats and dogs, we went out for a walk anyway.", difficulty: 3 },
  { italian: "Credo che sia importante studiare le lingue straniere fin da piccoli.", english: "I believe it is important to study foreign languages from a young age.", difficulty: 3 },
  { italian: "Quando sarai arrivato a destinazione, chiamami subito per farmi sapere come stai.", english: "When you have arrived at your destination, call me immediately to let me know how you are.", difficulty: 3 },
  { italian: "Mi piacerebbe molto visitare il Giappone, ma i voli sono troppo costosi per me.", english: "I would very much like to visit Japan, but the flights are too expensive for me.", difficulty: 3 },
  { italian: "Nonostante le difficoltà iniziali, è riuscito a completare il progetto con successo.", english: "Despite the initial difficulties, he managed to complete the project successfully.", difficulty: 3 },
  { italian: "Se fossi in te, non accetterei quell'offerta di lavoro senza prima rifletterci bene.", english: "If I were you, I wouldn't accept that job offer without thinking about it carefully first.", difficulty: 3 },
  { italian: "Penso che tu debba chiedere scusa per quello che hai detto ieri sera.", english: "I think you should apologize for what you said last night.", difficulty: 3 },
  { italian: "Spero che il tempo migliori presto, altrimenti non potremo andare in montagna.", english: "I hope the weather improves soon, otherwise we won't be able to go to the mountains.", difficulty: 3 },
  { italian: "Mi ha detto che non sarebbe venuto alla riunione perché si sentiva poco bene.", english: "He told me he wouldn't come to the meeting because he was feeling unwell.", difficulty: 3 },
  { italian: "Se avessimo saputo della tua festa, ti avremmo sicuramente portato un regalo.", english: "If we had known about your party, we would have definitely brought you a gift.", difficulty: 3 },
  { italian: "È necessario che tutti i partecipanti si presentino puntuali all'inizio della conferenza.", english: "It is necessary that all participants show up on time at the start of the conference.", difficulty: 3 },
  { italian: "Non sapevo che lei vivesse a Milano da così tanto tempo prima di trasferirsi.", english: "I didn't know she had lived in Milan for so long before moving.", difficulty: 3 },
  { italian: "Sebbene non avessi molta fame, ho mangiato tutto quello che mi hanno offerto.", english: "Although I wasn't very hungry, I ate everything they offered me.", difficulty: 3 },
  { italian: "Mi domando se lui si ricordi ancora di noi dopo tutti questi anni.", english: "I wonder if he still remembers us after all these years.", difficulty: 3 },
  { italian: "Prima di uscire di casa, assicurati di aver spento tutte le luci e chiuso il gas.", english: "Before leaving the house, make sure you have turned off all the lights and closed the gas.", difficulty: 3 },
  { italian: "Qualunque cosa accada, sarò sempre al tuo fianco per sostenerti e aiutarti.", english: "Whatever happens, I will always be by your side to support you and help you.", difficulty: 3 },
  { italian: "Si dice che quel vecchio castello sia abitato da fantasmi che appaiono di notte.", english: "It is said that that old castle is inhabited by ghosts that appear at night.", difficulty: 3 },
  { italian: "Avrei voluto dirti la verità fin dall'inizio, ma avevo paura della tua reazione.", english: "I wanted to tell you the truth from the beginning, but I was afraid of your reaction.", difficulty: 3 },
  { italian: "Se potessi cambiare qualcosa del mio passato, forse studierei medicina invece di legge.", english: "If I could change something about my past, maybe I would study medicine instead of law.", difficulty: 3 },
  { italian: "Benché fosse stanco morto, continuò a lavorare fino a tarda notte per finire il rapporto.", english: "Even though he was dead tired, he continued to work until late at night to finish the report.", difficulty: 3 },
  { italian: "Non credo che ci siano molte soluzioni possibili a questo complicato problema burocratico.", english: "I don't think there are many possible solutions to this complicated bureaucratic problem.", difficulty: 3 },
  { italian: "Sebbene il film fosse un po' lungo, mi è piaciuto molto per la sua fotografia.", english: "Although the movie was a bit long, I liked it a lot for its cinematography.", difficulty: 3 },
  { italian: "Mi chiedo perché non mi abbia ancora risposto al messaggio che gli ho mandato stamattina.", english: "I wonder why he hasn't replied yet to the message I sent him this morning.", difficulty: 3 },
  { italian: "È probabile che il volo subisca un ritardo a causa delle avverse condizioni meteorologiche.", english: "It is likely that the flight will experience a delay due to adverse weather conditions.", difficulty: 3 },
  { italian: "Se avessi vinto la lotteria, avrei comprato una villa enorme sulla costa toscana.", english: "If I had won the lottery, I would have bought a huge villa on the Tuscan coast.", difficulty: 3 },
  { italian: "Nonostante avesse studiato duramente, non è riuscito a superare l'esame di ammissione.", english: "Despite having studied hard, he did not manage to pass the entrance exam.", difficulty: 3 },
  { italian: "Spero che tutto vada per il meglio e che tu possa finalmente realizzare i tuoi sogni.", english: "I hope everything goes for the best and that you can finally realize your dreams.", difficulty: 3 },
  { italian: "Mi piacerebbe che tu mi spiegassi come funziona questo nuovo software che abbiamo installato.", english: "I would like you to explain to me how this new software we installed works.", difficulty: 3 },
  { italian: "Sebbene la situazione fosse critica, il capitano mantenne la calma e guidò l'equipaggio in salvo.", english: "Although the situation was critical, the captain stayed calm and led the crew to safety.", difficulty: 3 },
  { italian: "Non credo che lui sappia la verità su quello che è successo realmente durante la festa.", english: "I don't think he knows the truth about what actually happened during the party.", difficulty: 3 },
  { italian: "Se avessi saputo che saresti venuto, avrei preparato qualcosa di speciale per cena.", english: "If I had known you were coming, I would have prepared something special for dinner.", difficulty: 3 },
  { italian: "Bisogna che tutti si impegnino al massimo per raggiungere gli obiettivi che ci siamo prefissati.", english: "Everyone must do their best to reach the goals we have set for ourselves.", difficulty: 3 },
];

const grammarLessons = [
  {
    id: "l1",
    title: "Articles (Definite, Indefinite, Partitive)",
    description: "Master the use of articles in Italian, including the tricky partitive.",
    explanation: [
      {
        text: "Definite articles (il, lo, la, i, gli, le) specify a particular noun. Indefinite articles (un, uno, una, un') refer to any member of a class. Partitive articles (del, dello, della, dei, degli, delle) indicate 'some' or 'any' of an uncountable or plural noun.",
        examples: [
          { it: "Il libro è sul tavolo.", en: "The book is on the table." },
          { it: "Voglio una mela.", en: "I want an apple." },
          { it: "Vorrei del pane.", en: "I would like some bread." }
        ]
      }
    ],
    exercises: [
      { id: "l1-e1", kind: "multipleChoice", prompt: "Choose the correct article for 'zaino' (masc. sing, starts with z):", answer: "lo", options: ["il", "lo", "la", "un"] },
      { id: "l1-e2", kind: "fillBlank", prompt: "Vorrei ____ (some) acqua.", answer: "dell'" },
      { id: "l1-e3", kind: "multipleChoice", prompt: "Which is the definite article for 'amici'?", answer: "gli", options: ["i", "gli", "le", "degli"] }
    ]
  },
  {
    id: "l2",
    title: "Nouns (Gender, Number, Irregular Plurals)",
    description: "Learn how nouns change based on gender and number, and watch out for irregulars.",
    explanation: [
      {
        text: "In Italian, nouns are either masculine or feminine. Generally, -o ends in masculine singular, -a in feminine singular. In plural, -o becomes -i, and -a becomes -e. However, many nouns ending in -e can be either gender and become -i in plural.",
        examples: [
          { it: "Il ragazzo / I ragazzi", en: "The boy / The boys" },
          { it: "La casa / Le case", en: "The house / The houses" },
          { it: "Il braccio / Le braccia", en: "The arm / The arms (irregular)" }
        ]
      }
    ],
    exercises: [
      { id: "l2-e1", kind: "fillBlank", prompt: "Plural of 'fiore' (masc):", answer: "fiori" },
      { id: "l2-e2", kind: "multipleChoice", prompt: "What is the plural of 'uovo' (masc. sing)?", answer: "uova (fem. plur)", options: ["uovi", "uove", "uova", "uovo"] },
      { id: "l2-e3", kind: "fillBlank", prompt: "Gender of 'mano':", answer: "feminine" }
    ]
  },
  {
    id: "l3",
    title: "Adjectives (Agreement, Position, Irregulars)",
    description: "How to describe things correctly in Italian.",
    explanation: [
      {
        text: "Adjectives must agree in gender and number with the noun they modify. Most adjectives follow the noun, but some common ones (like bello, buono, grande) can precede it and may have irregular forms when they do.",
        examples: [
          { it: "Un libro interessante.", en: "An interesting book." },
          { it: "Un bel giorno.", en: "A beautiful day." },
          { it: "Delle persone gentili.", en: "Kind people." }
        ]
      }
    ],
    exercises: [
      { id: "l3-e1", kind: "multipleChoice", prompt: "Correct form: 'Le ragazze ____'", answer: "alte", options: ["alto", "alta", "alti", "alte"] },
      { id: "l3-e2", kind: "fillBlank", prompt: "Un ____ (good) amico.", answer: "buon" },
      { id: "l3-e3", kind: "translation", prompt: "A red car", answer: "Una macchina rossa" }
    ]
  },
  {
    id: "l4",
    title: "Pronouns (Subject, Direct, Indirect, Reflexive, Possessive)",
    description: "Master the various types of pronouns used in daily conversation.",
    explanation: [
      {
        text: "Subject pronouns (io, tu...) are often omitted. Direct object pronouns (mi, ti, lo, la...) replace the direct object. Indirect pronouns (mi, ti, gli, le...) indicate 'to whom'. Reflexive pronouns (mi, ti, si...) are used with reflexive verbs. Possessive pronouns (mio, tuo...) show ownership.",
        examples: [
          { it: "Lo vedo.", en: "I see him/it." },
          { it: "Gli parlo.", en: "I speak to him." },
          { it: "È il mio.", en: "It is mine." }
        ]
      }
    ],
    exercises: [
      { id: "l4-e1", kind: "multipleChoice", prompt: "Replace 'a Marco': 'Dico a Marco' -> '____ dico'", answer: "Gli", options: ["Lo", "Gli", "Le", "Ci"] },
      { id: "l4-e2", kind: "fillBlank", prompt: "Io ____ (myself) lavo le mani.", answer: "mi" },
      { id: "l4-e3", kind: "multipleChoice", prompt: "Which is 'ours'?", answer: "il nostro", options: ["mio", "tuo", "suo", "nostro"] }
    ]
  },
  {
    id: "l5",
    title: "Verbs (Present & Passato Prossimo)",
    description: "Learn how to talk about the present and the recent past.",
    explanation: [
      {
        text: "The present tense is used for current actions. Passato prossimo uses 'avere' or 'essere' + past participle for completed past actions. Remember that with 'essere', the participle agrees with the subject.",
        examples: [
          { it: "Mangio una mela.", en: "I eat an apple." },
          { it: "Ho mangiato una mela.", en: "I ate an apple." },
          { it: "Sono andato a Roma.", en: "I went to Rome." }
        ]
      }
    ],
    exercises: [
      { id: "l5-e1", kind: "fillBlank", prompt: "Io ____ (parlare) italiano.", answer: "parlo" },
      { id: "l5-e2", kind: "multipleChoice", prompt: "Past of 'lei parte':", answer: "lei è partita", options: ["lei ha partito", "lei è partito", "lei è partita", "lei ha partita"] },
      { id: "l5-e3", kind: "fillBlank", prompt: "Noi ____ (avere) finito.", answer: "abbiamo" }
    ]
  },
  {
    id: "l6",
    title: "Verbs (Imperfetto & Futuro)",
    description: "Describing ongoing past actions and future events.",
    explanation: [
      {
        text: "Imperfetto is for habitual or ongoing past actions ('I used to', 'I was doing'). Futuro is for future events ('I will do').",
        examples: [
          { it: "Da bambino giocavo sempre.", en: "As a child I always played." },
          { it: "Domani studierò.", en: "Tomorrow I will study." },
          { it: "Mentre leggevo, lui dormiva.", en: "While I was reading, he was sleeping." }
        ]
      }
    ],
    exercises: [
      { id: "l6-e1", kind: "fillBlank", prompt: "Loro ____ (essere - imperfetto) felici.", answer: "erano" },
      { id: "l6-e2", kind: "multipleChoice", prompt: "Future of 'noi andiamo':", answer: "andremo", options: ["andiamo", "andavamo", "andremo", "andremmo"] },
      { id: "l6-e3", kind: "fillBlank", prompt: "Tu ____ (parlare - futuro).", answer: "parlerai" }
    ]
  },
  {
    id: "l7",
    title: "Verbs (Condizionale & Imperativo)",
    description: "Expressing desires, possibilities, and giving commands.",
    explanation: [
      {
        text: "The conditional is used for 'would' (desires, polite requests). The imperative is for orders or suggestions.",
        examples: [
          { it: "Vorrei un caffè.", en: "I would like a coffee." },
          { it: "Vieni qui!", en: "Come here!" },
          { it: "Mangiate tutto!", en: "Eat everything!" }
        ]
      }
    ],
    exercises: [
      { id: "l7-e1", kind: "multipleChoice", prompt: "Conditional of 'io faccio':", answer: "farei", options: ["faccio", "farò", "farei", "facessi"] },
      { id: "l7-e2", kind: "fillBlank", prompt: "____ (Imperative 'Tu' - parlare)!", answer: "Parla" },
      { id: "l7-e3", kind: "translation", prompt: "I would go.", answer: "Andrei." }
    ]
  },
  {
    id: "l8",
    title: "Introduction to Congiuntivo",
    description: "Expressing doubts, hopes, and opinions.",
    explanation: [
      {
        text: "The subjunctive (congiuntivo) is used after verbs of emotion, doubt, or opinion, usually introduced by 'che'. It expresses subjectivity rather than fact.",
        examples: [
          { it: "Spero che tu stia bene.", en: "I hope you are well." },
          { it: "Credo che sia tardi.", en: "I believe it's late." },
          { it: "È necessario che lui venga.", en: "It's necessary that he comes." }
        ]
      }
    ],
    exercises: [
      { id: "l8-e1", kind: "fillBlank", prompt: "Penso che lei ____ (essere) stanca.", answer: "sia" },
      { id: "l8-e2", kind: "multipleChoice", prompt: "Which is subjunctive?", answer: "vada", options: ["va", "andrà", "vada", "andava"] },
      { id: "l8-e3", kind: "translation", prompt: "I hope he wins.", answer: "Spero che vinca." }
    ]
  },
  {
    id: "l9",
    title: "Prepositions (Simple & Articulated)",
    description: "Connecting words to show relationships in space and time.",
    explanation: [
      {
        text: "Simple prepositions (di, a, da, in, con, su, per, tra, fra) combine with definite articles to form articulated prepositions (e.g., in + il = nel).",
        examples: [
          { it: "Vado a casa.", en: "I go home." },
          { it: "Vado al cinema.", en: "I go to the cinema." },
          { it: "Il libro è sul tavolo.", en: "The book is on the table." }
        ]
      }
    ],
    exercises: [
      { id: "l9-e1", kind: "fillBlank", prompt: "Siamo ____ (in + la) cucina.", answer: "nella" },
      { id: "l9-e2", kind: "multipleChoice", prompt: "Combine 'di + gli':", answer: "degli", options: ["dei", "degli", "dagli", "sugli"] },
      { id: "l9-e3", kind: "fillBlank", prompt: "Vado ____ (to) Roma.", answer: "a" }
    ]
  },
  {
    id: "l10",
    title: "Negation and Word Order",
    description: "How to say 'no' and how to structure your sentences.",
    explanation: [
      {
        text: "To negate, put 'non' before the verb. Standard word order is Subject-Verb-Object, but Italian is flexible. Adjectives usually follow nouns.",
        examples: [
          { it: "Non capisco.", en: "I don't understand." },
          { it: "Io mangio la mela.", en: "I eat the apple." },
          { it: "Una macchina rossa.", en: "A red car." }
        ]
      }
    ],
    exercises: [
      { id: "l10-e1", kind: "translation", prompt: "I do not work.", answer: "Non lavoro." },
      { id: "l10-e2", kind: "multipleChoice", prompt: "Correct order:", answer: "Un gatto nero", options: ["Un nero gatto", "Un gatto nero", "Gatto un nero", "Nero un gatto"] },
      { id: "l10-e3", kind: "fillBlank", prompt: "Lui ____ (not) parla.", answer: "non" }
    ]
  },
  {
    id: "l11",
    title: "Comparatives and Superlatives",
    description: "Comparing things and expressing the highest degree.",
    explanation: [
      {
        text: "Comparatives use 'più... di' (more than) or 'meno... di' (less than). Relative superlatives use 'il più/meno...', and absolute superlatives use the suffix '-issimo'.",
        examples: [
          { it: "Marco è più alto di me.", en: "Marco is taller than me." },
          { it: "La pizza è buonissima!", en: "The pizza is very good!" },
          { it: "È il film più bello.", en: "It's the most beautiful movie." }
        ]
      }
    ],
    exercises: [
      { id: "l11-e1", kind: "fillBlank", prompt: "Lei è ____ (more) intelligente di lui.", answer: "più" },
      { id: "l11-e2", kind: "multipleChoice", prompt: "Translate 'very fast':", answer: "velocissimo", options: ["veloce", "più veloce", "velocissimo", "il più veloce"] },
      { id: "l11-e3", kind: "translation", prompt: "He is less tall than you.", answer: "Lui è meno alto di te." }
    ]
  },
  {
    id: "l12",
    title: "Conjunctions (e, ma, perché, quando, se)",
    description: "Words that connect sentences and ideas.",
    explanation: [
      {
        text: "Conjunctions connect words or clauses. 'E' (and), 'ma' (but), 'perché' (because/why), 'quando' (when), 'se' (if) are the most common.",
        examples: [
          { it: "Pane e burro.", en: "Bread and butter." },
          { it: "Vengo se posso.", en: "I'll come if I can." },
          { it: "Sono felice perché è sabato.", en: "I'm happy because it's Saturday." }
        ]
      }
    ],
    exercises: [
      { id: "l12-e1", kind: "fillBlank", prompt: "Non so ____ (if) lui viene.", answer: "se" },
      { id: "l12-e2", kind: "multipleChoice", prompt: "Which means 'but'?", answer: "ma", options: ["e", "ma", "perché", "quando"] },
      { id: "l12-e3", kind: "fillBlank", prompt: "Chiamami ____ (when) arrivi.", answer: "quando" }
    ]
  }
];

const result = {
  translationSentences,
  grammarLessons
};

console.log(JSON.stringify(result, null, 2));
