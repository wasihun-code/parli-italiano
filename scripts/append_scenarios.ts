import * as fs from 'fs';

const existingScenariosFile = 'src/data/scenarios.ts';
let content = fs.readFileSync(existingScenariosFile, 'utf8');

// Fix the two flagged items:
content = content.replace(
  "['Mescolare l\\'olio con la farina piano piano.', 'Mix the oil with the flour slowly.', {\"grammarPoint\":\"Describing a process con \\\"piano piano\\\".\"}]",
  "['Mescolare l\\'olio con la farina lentamente.', 'Mix the oil with the flour slowly.', {\"grammarPoint\":\"Adverb ending in -mente (lentamente).\"}]"
);

content = content.replace(
  "['Cin cin e tanti auguri a te!', 'Cheers and best wishes to you!', {\"grammarPoint\":\"Typical Italian toast \\\"cin cin\\\".\"}]",
  "['Facciamo un brindisi e tanti auguri a te!', 'Let\\'s make a toast and best wishes to you!', {\"grammarPoint\":\"Expression \\\"fare un brindisi\\\".\"}]"
);

// Append scenarios 111 to 116
const additionalBlueprints = [
  {
    id: 111,
    category: 'Daily Life',
    title: 'Animali',
    description: 'Talk about common animals.',
    focus: [['cane', 'dog'], ['gatto', 'cat'], ['cavallo', 'horse'], ['uccello', 'bird'], ['pesce', 'fish'], ['coniglio', 'rabbit'], ['gallina', 'hen'], ['farfalla', 'butterfly']],
    phrases: [
      ['Ho un cane.', 'I have a dog.'],
      ['Il gatto dorme.', 'The cat is sleeping.'],
      ['Ecco un cavallo.', 'Here is a horse.'],
      ['Sento un uccello.', 'I hear a bird.'],
      ['Guardo il pesce.', 'I am looking at the fish.'],
      ['C\'è una bella farfalla.', 'There is a beautiful butterfly.']
    ],
    sentences: [
      ['Il mio cane ama correre nel parco ogni mattina.', 'My dog loves to run in the park every morning.', {grammarPoint: 'Possessive adjective "mio" with article.'}],
      ['Abbiamo visto un bellissimo cavallo bianco nella fattoria.', 'We saw a beautiful white horse at the farm.', {grammarPoint: 'Absolute superlative "bellissimo".'}],
      ['Sento sempre un piccolo uccello cantare sul balcone.', 'I always hear a small bird singing on the balcony.', {grammarPoint: 'Infinitive "cantare" after perception verb.'}],
      ['Il coniglio mangia una carota fresca dal giardino.', 'The rabbit eats a fresh carrot from the garden.', {grammarPoint: 'Present tense of -ARE verb (mangiare).'}],
      ['La bambina guarda una grande farfalla colorata sui fiori.', 'The little girl looks at a large colorful butterfly on the flowers.', {grammarPoint: 'Adjective agreement.'}]
    ]
  },
  {
    id: 112,
    category: 'WorkStudy',
    title: 'Verbi in -ARE',
    description: 'Practice common verbs ending in -ARE.',
    focus: [['parlare', 'to speak'], ['ascoltare', 'to listen'], ['imparare', 'to learn'], ['visitare', 'to visit'], ['lavorare', 'to work'], ['studiare', 'to study'], ['mangiare', 'to eat'], ['cercare', 'to look for']],
    phrases: [
      ['Voglio parlare italiano.', 'I want to speak Italian.'],
      ['Devi ascoltare la musica.', 'You must listen to the music.'],
      ['Mi piace visitare i musei.', 'I like to visit museums.'],
      ['Lavoro in banca.', 'I work in a bank.'],
      ['Studio ogni giorno.', 'I study every day.'],
      ['Cerco i miei occhiali.', 'I am looking for my glasses.']
    ],
    sentences: [
      ['Sto provando a parlare italiano con i miei amici.', 'I am trying to speak Italian with my friends.', {grammarPoint: 'Verb "provare a" + infinitive.'}],
      ['Ascoltare la radio aiuta molto a imparare la lingua.', 'Listening to the radio helps a lot to learn the language.', {grammarPoint: 'Infinitive used as subject.'}],
      ['Domani andiamo a visitare il museo d\'arte moderna in centro.', 'Tomorrow we are going to visit the modern art museum downtown.', {grammarPoint: 'Verb "andare a".'}],
      ['Mia sorella lavora in un ristorante e mangia sempre lì.', 'My sister works in a restaurant and always eats there.', {grammarPoint: 'Present tense of -ARE verbs (lavora, mangia).'}],
      ['Stiamo cercando un buon posto per mangiare la pizza stasera.', 'We are looking for a good place to eat pizza tonight.', {grammarPoint: 'Present progressive "stiamo cercando".'}]
    ]
  },
  {
    id: 113,
    category: 'WorkStudy',
    title: 'Verbi in -ERE',
    description: 'Practice common verbs ending in -ERE.',
    focus: [['vedere', 'to see'], ['prendere', 'to take'], ['scrivere', 'to write'], ['leggere', 'to read'], ['chiedere', 'to ask'], ['conoscere', 'to know'], ['vivere', 'to live'], ['rispondere', 'to answer']],
    phrases: [
      ['Non riesco a vedere.', 'I cannot see.'],
      ['Prendo un caffè.', 'I am taking a coffee.'],
      ['Devo scrivere una email.', 'I must write an email.'],
      ['Mi piace leggere libri.', 'I like to read books.'],
      ['Posso chiedere una cosa?', 'Can I ask something?'],
      ['Voglio conoscere Roma.', 'I want to know Rome.']
    ],
    sentences: [
      ['Preferisco prendere il treno invece di guidare la macchina.', 'I prefer to take the train instead of driving the car.', {grammarPoint: 'Verb "preferire" + infinitive.'}],
      ['La mia amica mi ha chiesto di scrivere una lunga lettera.', 'My friend asked me to write a long letter.', {grammarPoint: 'Verb "chiedere di" + infinitive.'}],
      ['In Italia puoi leggere il giornale bevendo un buon caffè.', 'In Italy you can read the newspaper while drinking a good coffee.', {grammarPoint: 'Gerund "bevendo".'}],
      ['Ho deciso di vivere in questa bellissima città per sempre.', 'I have decided to live in this beautiful city forever.', {grammarPoint: 'Verb "decidere di" + infinitive.'}],
      ['Devi rispondere al telefono quando tua madre ti chiama!', 'You must answer the phone when your mother calls you!', {grammarPoint: 'Verb "rispondere a" (to answer to).'}]
    ]
  },
  {
    id: 114,
    category: 'WorkStudy',
    title: 'Verbi in -IRE',
    description: 'Practice common verbs ending in -IRE.',
    focus: [['sentire', 'to hear / feel'], ['aprire', 'to open'], ['dormire', 'to sleep'], ['partire', 'to leave'], ['capire', 'to understand'], ['finire', 'to finish'], ['pulire', 'to clean'], ['preferire', 'to prefer']],
    phrases: [
      ['Non riesco a sentire.', 'I cannot hear.'],
      ['Puoi aprire la finestra?', 'Can you open the window?'],
      ['Ho bisogno di dormire.', 'I need to sleep.'],
      ['A che ora devi partire?', 'What time do you have to leave?'],
      ['Ora posso capire.', 'Now I can understand.'],
      ['Devo finire il lavoro.', 'I must finish the work.']
    ],
    sentences: [
      ['Non riesco a sentire bene la tua voce al telefono.', 'I cannot hear your voice well on the phone.', {grammarPoint: 'Verb "riuscire a" + infinitive.'}],
      ['Domani mattina devo partire presto per il mio lungo viaggio.', 'Tomorrow morning I have to leave early for my long trip.', {grammarPoint: 'Present used for future plans.'}],
      ['Con un po\' di pazienza, puoi capire tutto facilmente.', 'With a bit of patience, you can understand everything easily.', {grammarPoint: 'Adverb ending in -mente (facilmente).'}],
      ['Spero di finire di pulire tutta la casa entro stasera.', 'I hope to finish cleaning the whole house by tonight.', {grammarPoint: 'Verb "finire di" + infinitive.'}],
      ['Anche se fa freddo, preferisco uscire e camminare.', 'Even if it is cold, I prefer to go out and walk.', {grammarPoint: 'Conjunction "anche se" (even if).'}]
    ]
  },
  {
    id: 115,
    category: 'Daily Life',
    title: 'Verbi Riflessivi',
    description: 'Practice common reflexive verbs.',
    focus: [['svegliarsi', 'to wake up'], ['alzarsi', 'to get up'], ['lavarsi', 'to wash oneself'], ['vestirsi', 'to get dressed'], ['divertirsi', 'to have fun'], ['sentirsi', 'to feel'], ['chiamarsi', 'to be named'], ['riposarsi', 'to rest']],
    phrases: [
      ['Mi sveglio presto.', 'I wake up early.'],
      ['Mi alzo dal letto.', 'I get up from bed.'],
      ['Vado a lavarmi.', 'I am going to wash myself.'],
      ['Devo vestirmi per uscire.', 'I must get dressed to go out.'],
      ['Spero di divertirmi.', 'I hope to have fun.'],
      ['Come ti chiami?', 'What is your name?']
    ],
    sentences: [
      ['Di solito mi sveglio alle sette e mi alzo subito.', 'Usually I wake up at seven and get up immediately.', {grammarPoint: 'Reflexive pronouns "mi" in the present tense.'}],
      ['La mattina mi lavo i denti prima di fare colazione.', 'In the morning I brush my teeth before having breakfast.', {grammarPoint: 'Reflexive used for body parts.'}],
      ['Mi vesto elegante perché stasera ho una cena importante.', 'I dress elegantly because tonight I have an important dinner.', {grammarPoint: 'Reflexive verb "vestirsi".'}],
      ['Alla festa di ieri sera ci siamo divertiti davvero molto.', 'At the party last night we really had a lot of fun.', {grammarPoint: 'Passato prossimo of reflexive verbs with "essere".'}],
      ['Non mi sento bene oggi, quindi voglio solo riposarmi.', 'I don\'t feel well today, so I just want to rest.', {grammarPoint: 'Reflexive pronoun attached to infinitive (riposarmi).'}]
    ]
  },
  {
    id: 116,
    category: 'Daily Life',
    title: 'Parole per Descrivere',
    description: 'Practice common adjectives.',
    focus: [['buono', 'good'], ['bello', 'beautiful'], ['grande', 'big'], ['piccolo', 'small'], ['nuovo', 'new'], ['vecchio', 'old'], ['facile', 'easy'], ['difficile', 'difficult']],
    phrases: [
      ['È un piatto molto buono.', 'It is a very good dish.'],
      ['Che bel paesaggio!', 'What a beautiful landscape!'],
      ['Ho una casa grande.', 'I have a big house.'],
      ['Il mio cane è piccolo.', 'My dog is small.'],
      ['Ho comprato un telefono nuovo.', 'I bought a new phone.'],
      ['È una lezione facile.', 'It is an easy lesson.']
    ],
    sentences: [
      ['Questo gelato al pistacchio è davvero molto buono e fresco.', 'This pistachio ice cream is really very good and fresh.', {grammarPoint: 'Adjective placement after noun.'}],
      ['Abbiamo visitato un bel castello grande e antico vicino qui.', 'We visited a beautiful big and old castle near here.', {grammarPoint: 'Multiple adjectives.'}],
      ['Mi piace il tuo nuovo vestito rosso, è molto bello.', 'I like your new red dress, it is very beautiful.', {grammarPoint: 'Adjectives preceding and following the noun.'}],
      ['Per me, questo libro è piccolo ma molto difficile da leggere.', 'For me, this book is small but very difficult to read.', {grammarPoint: 'Adjective + "da" + infinitive (difficile da leggere).'}],
      ['Il mio vecchio computer era molto lento e difficile da usare.', 'My old computer was very slow and difficult to use.', {grammarPoint: 'Imperfect tense "era".'}]
    ]
  }
];

const blueprintsStartMatch = content.match(/const blueprints: ScenarioBlueprint\[\] = \[/);
if (!blueprintsStartMatch) {
  console.error('Could not find blueprints start');
  process.exit(1);
}
const startIndex = blueprintsStartMatch.index + blueprintsStartMatch[0].length;
let depth = 1;
let endIndex = -1;
for (let i = startIndex; i < content.length; i++) {
  if (content[i] === '[') depth++;
  else if (content[i] === ']') depth--;
  if (depth === 0) {
    endIndex = i;
    break;
  }
}
if (endIndex === -1) {
  console.error('Could not find blueprints end');
  process.exit(1);
}

const appendString = ',\n' + additionalBlueprints.map(b => {
  return `  {id: ${b.id}, category: '${b.category}', title: '${b.title.replace(/'/g, "\\'")}', description: '${b.description.replace(/'/g, "\\'")}', ${b.difficulty ? `difficulty: ${b.difficulty}, ` : ''}focus: ${JSON.stringify(b.focus)}, phrases: ${JSON.stringify(b.phrases)}, sentences: ${JSON.stringify(b.sentences)}}`;
}).join(',\n');

// Append just before the closing bracket of blueprints array
const newContent = content.slice(0, endIndex) + appendString + content.slice(endIndex);

fs.writeFileSync(existingScenariosFile, newContent);
console.log('Appended 111-116 and fixed flagged sentences.');
