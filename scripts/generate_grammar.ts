import fs from 'fs';

const topics = [
  {
    id: "articles",
    title: "Definite and Indefinite Articles",
    level: "A1",
    explanation: "In Italian, nouns have a gender (masculine or feminine) and a number (singular or plural). The article must agree with the noun in both gender and number.\n\n### Definite Articles (The)\nThey refer to specific nouns.\n- Masculine singular: **il** (before consonants), **lo** (before s+consonant, z, ps, gn), **l'** (before vowels).\n- Masculine plural: **i** (plural of il), **gli** (plural of lo and l').\n- Feminine singular: **la** (before consonants), **l'** (before vowels).\n- Feminine plural: **le** (for all plural feminine nouns).\n\n### Indefinite Articles (A/An)\nThey refer to unspecific nouns.\n- Masculine: **un** (most cases), **uno** (before s+consonant, z, ps, gn).\n- Feminine: **una** (before consonants), **un'** (before vowels).",
    examples: [
      { italian: "il gatto", english: "the cat (m)" },
      { italian: "lo zaino", english: "the backpack" },
      { italian: "l'amico", english: "the friend (m)" },
      { italian: "i gatti", english: "the cats" },
      { italian: "gli zaini", english: "the backpacks" },
      { italian: "la donna", english: "the woman" },
      { italian: "l'amica", english: "the friend (f)" },
      { italian: "le donne", english: "the women" },
      { italian: "un cane", english: "a dog" },
      { italian: "uno studente", english: "a student (m)" },
      { italian: "una casa", english: "a house" },
      { italian: "un'idea", english: "an idea" }
    ],
    exercises: [
      { id: "art1", type: "multiple-choice", question: "Choose the correct article: ___ sole (m)", options: ["il", "lo", "la", "l'"], answer: "il" },
      { id: "art2", type: "multiple-choice", question: "Choose the correct article: ___ zio (m)", options: ["il", "lo", "la", "gli"], answer: "lo" },
      { id: "art3", type: "multiple-choice", question: "Choose the correct article: ___ alberi (m. pl.)", options: ["i", "gli", "le", "lo"], answer: "gli" },
      { id: "art4", type: "multiple-choice", question: "Choose the correct article: ___ amica (f)", options: ["la", "l'", "le", "un'"], answer: "l'" },
      { id: "art5", type: "multiple-choice", question: "Choose the correct article: ___ mela (f)", options: ["il", "lo", "la", "le"], answer: "la" },
      { id: "art6", type: "multiple-choice", question: "Choose the indefinite article: ___ ragazzo (m)", options: ["un", "uno", "una", "un'"], answer: "un" },
      { id: "art7", type: "multiple-choice", question: "Choose the indefinite article: ___ specchio (m)", options: ["un", "uno", "una", "un'"], answer: "uno" },
      { id: "art8", type: "multiple-choice", question: "Choose the indefinite article: ___ automobile (f)", options: ["un", "uno", "una", "un'"], answer: "un'" },
      { id: "art9", type: "multiple-choice", question: "Choose the correct article: ___ case (f. pl.)", options: ["i", "gli", "la", "le"], answer: "le" },
      { id: "art10", type: "multiple-choice", question: "Choose the correct article: ___ psicologo (m)", options: ["il", "lo", "la", "i"], answer: "lo" }
    ]
  },
  {
    id: "nouns",
    title: "Nouns and Gender",
    level: "A1",
    explanation: "In Italian, every noun is either masculine or feminine. Unlike English, even inanimate objects have a gender.\n\n### General Rules\n- Nouns ending in **-o** are usually masculine (e.g., *il libro*).\n- Nouns ending in **-a** are usually feminine (e.g., *la casa*).\n- Nouns ending in **-e** can be either masculine or feminine (e.g., *il padre*, *la madre*).\n\n### Plural Formation\n- **-o** changes to **-i** (*libro* -> *libri*)\n- **-a** changes to **-e** (*casa* -> *case*)\n- **-e** changes to **-i** (*padre* -> *padri*, *madre* -> *madri*)",
    examples: [
      { italian: "il libro", english: "the book (m)" },
      { italian: "i libri", english: "the books (m)" },
      { italian: "la casa", english: "the house (f)" },
      { italian: "le case", english: "the houses (f)" },
      { italian: "il fiore", english: "the flower (m)" },
      { italian: "i fiori", english: "the flowers (m)" },
      { italian: "la notte", english: "the night (f)" },
      { italian: "le notti", english: "the nights (f)" },
      { italian: "il problema", english: "the problem (m - exception)" },
      { italian: "la mano", english: "the hand (f - exception)" }
    ],
    exercises: [
      { id: "n1", type: "multiple-choice", question: "What is the plural of 'il ragazzo'?", options: ["i ragazzi", "le ragazze", "i ragazze", "gli ragazzi"], answer: "i ragazzi" },
      { id: "n2", type: "multiple-choice", question: "What is the plural of 'la mela'?", options: ["le mele", "i meli", "le mela", "i mela"], answer: "le mele" },
      { id: "n3", type: "multiple-choice", question: "What is the plural of 'il cane'?", options: ["i cani", "le cane", "i cane", "le cani"], answer: "i cani" },
      { id: "n4", type: "multiple-choice", question: "What gender is 'problema'?", options: ["Masculine", "Feminine"], answer: "Masculine" },
      { id: "n5", type: "multiple-choice", question: "What gender is 'mano'?", options: ["Masculine", "Feminine"], answer: "Feminine" },
      { id: "n6", type: "multiple-choice", question: "What is the plural of 'la stazione'?", options: ["le stazioni", "le stazione", "i stazioni", "i stazione"], answer: "le stazioni" },
      { id: "n7", type: "multiple-choice", question: "Is 'padre' masculine or feminine?", options: ["Masculine", "Feminine"], answer: "Masculine" },
      { id: "n8", type: "multiple-choice", question: "What is the singular of 'le penne'?", options: ["la penna", "il penno", "la penne", "il penne"], answer: "la penna" },
      { id: "n9", type: "multiple-choice", question: "Is 'giorno' masculine or feminine?", options: ["Masculine", "Feminine"], answer: "Masculine" },
      { id: "n10", type: "multiple-choice", question: "What is the plural of 'l'amico'?", options: ["gli amici", "i amici", "le amice", "l'amici"], answer: "gli amici" }
    ]
  },
  {
    id: "adjectives",
    title: "Adjectives",
    level: "A1",
    explanation: "Adjectives must agree in gender and number with the noun they modify.\n\n### Types of Adjectives\n1. **Ending in -o**: Have four forms (e.g., *bello* (m.sg.), *bella* (f.sg.), *belli* (m.pl.), *belle* (f.pl.)).\n2. **Ending in -e**: Have two forms, singular for both genders and plural for both genders (e.g., *intelligente* (sg.), *intelligenti* (pl.)).\n\n### Position\nMost descriptive adjectives come **after** the noun (e.g., *una casa grande*). Some common adjectives (like bello, bravo, buono, nuovo, vecchio, giovane) often come **before** the noun (e.g., *un bel libro*).",
    examples: [
      { italian: "un gatto nero", english: "a black cat" },
      { italian: "una gatta nera", english: "a black cat (f)" },
      { italian: "i gatti neri", english: "the black cats" },
      { italian: "le gatte nere", english: "the black cats (f)" },
      { italian: "un ragazzo intelligente", english: "an intelligent boy" },
      { italian: "una ragazza intelligente", english: "an intelligent girl" },
      { italian: "i ragazzi intelligenti", english: "the intelligent boys" },
      { italian: "le ragazze intelligenti", english: "the intelligent girls" },
      { italian: "una bella casa", english: "a beautiful house" },
      { italian: "un bravo studente", english: "a good student" }
    ],
    exercises: [
      { id: "adj1", type: "multiple-choice", question: "il libro ___", options: ["rosso", "rossa", "rossi", "rosse"], answer: "rosso" },
      { id: "adj2", type: "multiple-choice", question: "la porta ___", options: ["aperto", "aperta", "aperti", "aperte"], answer: "aperta" },
      { id: "adj3", type: "multiple-choice", question: "i ragazzi ___", options: ["alto", "alta", "alti", "alte"], answer: "alti" },
      { id: "adj4", type: "multiple-choice", question: "le ragazze ___", options: ["simpatico", "simpatica", "simpatici", "simpatiche"], answer: "simpatiche" },
      { id: "adj5", type: "multiple-choice", question: "il treno ___", options: ["veloce", "veloci", "veloco", "veloca"], answer: "veloce" },
      { id: "adj6", type: "multiple-choice", question: "le macchine ___", options: ["veloce", "veloci", "veloco", "veloca"], answer: "veloci" },
      { id: "adj7", type: "multiple-choice", question: "un ___ libro", options: ["bello", "bel", "bella", "belli"], answer: "bel" },
      { id: "adj8", type: "multiple-choice", question: "la mia amica è ___", options: ["gentile", "gentili", "gentila", "gentilo"], answer: "gentile" },
      { id: "adj9", type: "multiple-choice", question: "i cani sono ___", options: ["piccolo", "piccola", "piccoli", "piccole"], answer: "piccoli" },
      { id: "adj10", type: "multiple-choice", question: "le case sono ___", options: ["grande", "grandi", "granda", "grando"], answer: "grandi" }
    ]
  },
  {
    id: "pronouns",
    title: "Personal Pronouns",
    level: "A1",
    explanation: "Subject pronouns replace the noun acting as the subject of the sentence.\n\n### Subject Pronouns\n- **io** (I)\n- **tu** (you, informal singular)\n- **lui / lei / Lei** (he / she / You, formal singular)\n- **noi** (we)\n- **voi** (you all, plural)\n- **loro** (they)\n\nIn Italian, subject pronouns are often omitted because the verb ending already indicates who is performing the action. They are used for emphasis or clarification.",
    examples: [
      { italian: "Io sono italiano.", english: "I am Italian." },
      { italian: "Tu parli bene.", english: "You speak well." },
      { italian: "Lui studia molto.", english: "He studies a lot." },
      { italian: "Lei mangia la mela.", english: "She eats the apple." },
      { italian: "Lei, di dov'è?", english: "Where are You from? (formal)" },
      { italian: "Noi andiamo a Roma.", english: "We are going to Rome." },
      { italian: "Voi capite?", english: "Do you all understand?" },
      { italian: "Loro dormono.", english: "They are sleeping." },
      { italian: "Sono stanco.", english: "I am tired. (pronoun omitted)" },
      { italian: "Andiamo!", english: "Let's go! (pronoun omitted)" }
    ],
    exercises: [
      { id: "pro1", type: "multiple-choice", question: "___ sono felice. (I)", options: ["Io", "Tu", "Lui", "Noi"], answer: "Io" },
      { id: "pro2", type: "multiple-choice", question: "___ sei mio amico. (You, informal)", options: ["Io", "Tu", "Lui", "Voi"], answer: "Tu" },
      { id: "pro3", type: "multiple-choice", question: "___ legge un libro. (He)", options: ["Lui", "Lei", "Loro", "Noi"], answer: "Lui" },
      { id: "pro4", type: "multiple-choice", question: "___ lavora in banca. (She)", options: ["Lui", "Lei", "Tu", "Io"], answer: "Lei" },
      { id: "pro5", type: "multiple-choice", question: "___ cantiamo bene. (We)", options: ["Io", "Voi", "Noi", "Loro"], answer: "Noi" },
      { id: "pro6", type: "multiple-choice", question: "___ mangiate la pizza. (You all)", options: ["Noi", "Voi", "Loro", "Tu"], answer: "Voi" },
      { id: "pro7", type: "multiple-choice", question: "___ guardano la TV. (They)", options: ["Lui", "Lei", "Noi", "Loro"], answer: "Loro" },
      { id: "pro8", type: "multiple-choice", question: "Which pronoun is formal 'You'?", options: ["tu", "voi", "Lei", "loro"], answer: "Lei" },
      { id: "pro9", type: "multiple-choice", question: "Is the subject pronoun always required in Italian?", options: ["Yes", "No"], answer: "No" },
      { id: "pro10", type: "multiple-choice", question: "___ siamo pronti! (We)", options: ["Loro", "Voi", "Noi", "Io"], answer: "Noi" }
    ]
  },
  {
    id: "verbs-present",
    title: "Present Tense (Indicativo Presente)",
    level: "A1",
    explanation: "Italian verbs are divided into three conjugations based on their infinitive endings: **-are**, **-ere**, and **-ire**.\n\n### Regular Endings\n- **-are** (e.g., parlare): parlo, parli, parla, parliamo, parlate, parlano.\n- **-ere** (e.g., leggere): leggo, leggi, legge, leggiamo, leggete, leggono.\n- **-ire** (e.g., dormire): dormo, dormi, dorme, dormiamo, dormite, dormono.\n\nSome -ire verbs insert '-isc-' (e.g., capire: capisco, capisci, capisce, capiamo, capite, capiscono).\n\n### Important Irregular Verbs\n- **Essere** (to be): sono, sei, è, siamo, siete, sono.\n- **Avere** (to have): ho, hai, ha, abbiamo, avete, hanno.",
    examples: [
      { italian: "Io parlo italiano.", english: "I speak Italian." },
      { italian: "Lui legge il giornale.", english: "He reads the newspaper." },
      { italian: "Noi dormiamo otto ore.", english: "We sleep eight hours." },
      { italian: "Io capisco tutto.", english: "I understand everything." },
      { italian: "Tu sei molto gentile.", english: "You are very kind." },
      { italian: "Loro hanno un cane.", english: "They have a dog." },
      { italian: "Voi mangiate la pasta.", english: "You all eat pasta." },
      { italian: "Lei scrive una lettera.", english: "She writes a letter." },
      { italian: "Io non so.", english: "I don't know." },
      { italian: "Noi andiamo al cinema.", english: "We go to the cinema." }
    ],
    exercises: [
      { id: "vp1", type: "multiple-choice", question: "Io ___ (parlare) italiano.", options: ["parlo", "parli", "parla", "parlano"], answer: "parlo" },
      { id: "vp2", type: "multiple-choice", question: "Tu ___ (leggere) molto.", options: ["leggo", "leggi", "legge", "leggete"], answer: "leggi" },
      { id: "vp3", type: "multiple-choice", question: "Lui ___ (dormire) fino a tardi.", options: ["dormo", "dormi", "dorme", "dormiamo"], answer: "dorme" },
      { id: "vp4", type: "multiple-choice", question: "Noi ___ (capire) la lezione.", options: ["capisco", "capiamo", "capite", "capiscono"], answer: "capiamo" },
      { id: "vp5", type: "multiple-choice", question: "Voi ___ (mangiare) la pizza.", options: ["mangio", "mangi", "mangiate", "mangiano"], answer: "mangiate" },
      { id: "vp6", type: "multiple-choice", question: "Loro ___ (scrivere) una mail.", options: ["scrivo", "scrive", "scriviamo", "scrivono"], answer: "scrivono" },
      { id: "vp7", type: "multiple-choice", question: "Io ___ (essere) stanco.", options: ["sono", "sei", "è", "siamo"], answer: "sono" },
      { id: "vp8", type: "multiple-choice", question: "Noi ___ (avere) fame.", options: ["ho", "hai", "ha", "abbiamo"], answer: "abbiamo" },
      { id: "vp9", type: "multiple-choice", question: "Tu ___ (capire) l'inglese?", options: ["capisco", "capisci", "capisce", "capite"], answer: "capisci" },
      { id: "vp10", type: "multiple-choice", question: "Lei ___ (essere) felice.", options: ["sono", "sei", "è", "siete"], answer: "è" }
    ]
  },
  {
    id: "verbs-passato-prossimo",
    title: "Present Perfect (Passato Prossimo)",
    level: "A2",
    explanation: "The *passato prossimo* is used to express actions completed in the recent past.\n\nIt is a compound tense formed with an auxiliary verb (**essere** or **avere**) + the **past participle** of the main verb.\n\n### Past Participle Regular Endings\n- **-are** -> **-ato** (parlato)\n- **-ere** -> **-uto** (creduto)\n- **-ire** -> **-ito** (dormito)\n\n### Auxiliary Verbs\n- **Avere**: Used with most transitive verbs (verbs that take a direct object). E.g., *Ho mangiato una mela*.\n- **Essere**: Used with verbs of movement, state, and reflexive verbs. When using *essere*, the past participle must agree in gender and number with the subject. E.g., *Sono andato/a*, *Siamo andati/e*.",
    examples: [
      { italian: "Ho mangiato la pizza.", english: "I ate / have eaten the pizza." },
      { italian: "Hai capito?", english: "Did you understand?" },
      { italian: "Abbiamo visto un bel film.", english: "We saw a good movie." },
      { italian: "Loro hanno dormito bene.", english: "They slept well." },
      { italian: "Sono andato al cinema.", english: "I (m) went to the cinema." },
      { italian: "Maria è andata a casa.", english: "Maria went home." },
      { italian: "Siamo partiti presto.", english: "We (m/mixed) left early." },
      { italian: "Le ragazze sono arrivate.", english: "The girls arrived." },
      { italian: "Cosa hai fatto ieri?", english: "What did you do yesterday?" },
      { italian: "Non ho studiato.", english: "I didn't study." }
    ],
    exercises: [
      { id: "pp1", type: "multiple-choice", question: "Io ___ (mangiare) una mela.", options: ["ho mangiato", "ha mangiato", "sono mangiato", "è mangiato"], answer: "ho mangiato" },
      { id: "pp2", type: "multiple-choice", question: "Tu ___ (capire) il problema?", options: ["hai capito", "ha capito", "sei capito", "sono capito"], answer: "hai capito" },
      { id: "pp3", type: "multiple-choice", question: "Maria ___ (andare) a scuola.", options: ["ha andato", "ha andata", "è andato", "è andata"], answer: "è andata" },
      { id: "pp4", type: "multiple-choice", question: "Noi ___ (vedere) un film.", options: ["abbiamo visto", "siamo visti", "avete visto", "hanno visto"], answer: "abbiamo visto" },
      { id: "pp5", type: "multiple-choice", question: "Loro (m) ___ (partire) alle otto.", options: ["hanno partito", "sono partito", "sono partiti", "sono partite"], answer: "sono partiti" },
      { id: "pp6", type: "multiple-choice", question: "Voi ___ (dormire) bene?", options: ["avete dormito", "siete dormiti", "hanno dormito", "sono dormiti"], answer: "avete dormito" },
      { id: "pp7", type: "multiple-choice", question: "Io (f) ___ (uscire) con gli amici.", options: ["ho uscito", "ho uscita", "sono uscito", "sono uscita"], answer: "sono uscita" },
      { id: "pp8", type: "multiple-choice", question: "Luigi e Marco ___ (arrivare).", options: ["hanno arrivato", "sono arrivato", "sono arrivati", "sono arrivate"], answer: "sono arrivati" },
      { id: "pp9", type: "multiple-choice", question: "La lezione ___ (finire).", options: ["ha finito", "è finito", "ha finita", "è finita"], answer: "è finita" },
      { id: "pp10", type: "multiple-choice", question: "Io ___ (fare) i compiti.", options: ["ho fatto", "ho feci", "sono fatto", "ho facito"], answer: "ho fatto" }
    ]
  },
  {
    id: "verbs-imperfetto",
    title: "Imperfect Tense (Imperfetto)",
    level: "A2",
    explanation: "The *imperfetto* is used to describe continuous, habitual, or background actions in the past.\n\n### Regular Conjugation\nDrop the -re from the infinitive and add:\n- **-vo, -vi, -va, -vamo, -vate, -vano**\nE.g., Parlare -> parlavo, parlavi, parlava, parlavamo, parlavate, parlavano.\n\n### Usage\n- Descriptions in the past (weather, age, feelings, appearance).\n- Habitual actions in the past (\"I used to...\").\n- Actions in progress that were interrupted.",
    examples: [
      { italian: "Da bambino giocavo molto.", english: "As a child I used to play a lot." },
      { italian: "Mentre mangiavo, ha squillato il telefono.", english: "While I was eating, the phone rang." },
      { italian: "Faceva caldo.", english: "It was hot." },
      { italian: "La casa era grande.", english: "The house was big." },
      { italian: "Io leggevo un libro.", english: "I was reading a book." },
      { italian: "Noi andavamo spesso al mare.", english: "We used to go to the sea often." },
      { italian: "Lei aveva capelli lunghi.", english: "She had long hair." },
      { italian: "Loro dormivano quando sono arrivato.", english: "They were sleeping when I arrived." },
      { italian: "Ero stanco ieri.", english: "I was tired yesterday." },
      { italian: "Voi guardavate la TV.", english: "You were watching TV." }
    ],
    exercises: [
      { id: "imp1", type: "multiple-choice", question: "Io ___ (parlare) con Maria.", options: ["parlavo", "parlavi", "parlava", "parlavamo"], answer: "parlavo" },
      { id: "imp2", type: "multiple-choice", question: "Mentre tu ___ (leggere)...", options: ["leggevo", "leggevi", "leggeva", "leggevamo"], answer: "leggevi" },
      { id: "imp3", type: "multiple-choice", question: "Lui ___ (dormire) sul divano.", options: ["dormivo", "dormivi", "dormiva", "dormivano"], answer: "dormiva" },
      { id: "imp4", type: "multiple-choice", question: "Noi ___ (andare) al cinema ogni sabato.", options: ["andavo", "andavamo", "andavate", "andavano"], answer: "andavamo" },
      { id: "imp5", type: "multiple-choice", question: "Voi ___ (essere) felici.", options: ["eravate", "erano", "eravamo", "eri"], answer: "eravate" },
      { id: "imp6", type: "multiple-choice", question: "Loro ___ (avere) fame.", options: ["avevo", "avevi", "avevano", "avevamo"], answer: "avevano" },
      { id: "imp7", type: "multiple-choice", question: "Il cielo ___ (essere) blu.", options: ["era", "ero", "erano", "eravamo"], answer: "era" },
      { id: "imp8", type: "multiple-choice", question: "Io ___ (fare) sport.", options: ["facevo", "facevi", "faceva", "favo"], answer: "facevo" },
      { id: "imp9", type: "multiple-choice", question: "Da piccola, Maria ___ (bere) molto latte.", options: ["beveva", "bevevo", "bevevi", " bevevamo"], answer: "beveva" },
      { id: "imp10", type: "multiple-choice", question: "Noi ___ (mangiare) quando...", options: ["mangiavo", "mangiavamo", "mangiavate", "mangiavano"], answer: "mangiavamo" }
    ]
  },
  {
    id: "prepositions",
    title: "Prepositions (Preposizioni)",
    level: "A1",
    explanation: "Italian has simple prepositions (di, a, da, in, con, su, per, tra, fra) and articulated prepositions (preposition + definite article).\n\n### Common Uses\n- **A**: to, at (cities, specific places like 'a casa', 'a scuola').\n- **In**: to, in (countries, regions, large islands, rooms, transport).\n- **Di**: of, from (possession, origin with 'essere').\n- **Da**: from, since, to a person's place (e.g., 'vado dal medico').\n- **Per**: for, in order to, through.\n\n### Articulated Prepositions\nWhen a preposition is followed by a definite article, they combine (e.g., a + il = al, di + la = della, in + lo = nello).",
    examples: [
      { italian: "Vado a Roma.", english: "I am going to Rome." },
      { italian: "Vivo in Italia.", english: "I live in Italy." },
      { italian: "Il libro è di Marco.", english: "The book is Marco's." },
      { italian: "Vengo da Parigi.", english: "I come from Paris." },
      { italian: "Vado dal medico.", english: "I am going to the doctor." },
      { italian: "Il gatto è sul tavolo.", english: "The cat is on the table." },
      { italian: "Questo regalo è per te.", english: "This gift is for you." },
      { italian: "Parlo con lei.", english: "I talk with her." },
      { italian: "Il bar è tra la banca e il cinema.", english: "The bar is between the bank and the cinema." },
      { italian: "Andiamo al mare.", english: "We are going to the sea (a + il = al)." }
    ],
    exercises: [
      { id: "prep1", type: "multiple-choice", question: "Vado ___ Roma.", options: ["a", "in", "di", "da"], answer: "a" },
      { id: "prep2", type: "multiple-choice", question: "Vivo ___ Italia.", options: ["a", "in", "di", "da"], answer: "in" },
      { id: "prep3", type: "multiple-choice", question: "Il libro è ___ Maria.", options: ["a", "in", "di", "da"], answer: "di" },
      { id: "prep4", type: "multiple-choice", question: "Vengo ___ Napoli.", options: ["a", "in", "di", "da"], answer: "da" },
      { id: "prep5", type: "multiple-choice", question: "Vado ___ cinema.", options: ["al", "a il", "nel", "sul"], answer: "al" },
      { id: "prep6", type: "multiple-choice", question: "Il cane è ___ tavolo.", options: ["su", "sul", "in", "nel"], answer: "sul" },
      { id: "prep7", type: "multiple-choice", question: "Passeggio ___ il parco.", options: ["per", "con", "a", "di"], answer: "per" },
      { id: "prep8", type: "multiple-choice", question: "Esco ___ i miei amici.", options: ["con", "per", "di", "a"], answer: "con" },
      { id: "prep9", type: "multiple-choice", question: "Siamo ___ treno.", options: ["a", "in", "su", "con"], answer: "in" },
      { id: "prep10", type: "multiple-choice", question: "La penna è ___ borsa (nella).", options: ["in la", "nella", "alla", "sulla"], answer: "nella" }
    ]
  },
  {
    id: "negation",
    title: "Negation",
    level: "A1",
    explanation: "To make a sentence negative in Italian, place **non** directly before the verb.\n\n- E.g., *Io parlo* -> *Io non parlo*.\n\n### Double Negatives\nItalian often uses double negatives, which is perfectly correct. You use **non** before the verb and another negative word after it.\n- **Niente / Nulla** (nothing)\n- **Nessuno** (nobody / no one)\n- **Mai** (never)\n- **Neanche / Nemmeno** (not even / neither)\n- **Più** (anymore / no longer)\n\nE.g., *Non mangio niente* (I don't eat anything / I eat nothing).",
    examples: [
      { italian: "Non capisco.", english: "I don't understand." },
      { italian: "Non ho tempo.", english: "I don't have time." },
      { italian: "Non vedo niente.", english: "I don't see anything." },
      { italian: "Non c'è nessuno.", english: "There is nobody." },
      { italian: "Non fumo mai.", english: "I never smoke." },
      { italian: "Non voglio più mangiare.", english: "I don't want to eat anymore." },
      { italian: "Lui non viene neanche oggi.", english: "He isn't coming today either." },
      { italian: "Non ho detto nulla.", english: "I didn't say anything." },
      { italian: "Non so niente.", english: "I know nothing." },
      { italian: "Maria non è italiana.", english: "Maria is not Italian." }
    ],
    exercises: [
      { id: "neg1", type: "multiple-choice", question: "Io ___ capisco.", options: ["non", "no", "niente", "mai"], answer: "non" },
      { id: "neg2", type: "multiple-choice", question: "Non vedo ___.", options: ["niente", "tutto", "qualcosa", "sempre"], answer: "niente" },
      { id: "neg3", type: "multiple-choice", question: "Non c'è ___ in casa.", options: ["nessuno", "tutti", "niente", "mai"], answer: "nessuno" },
      { id: "neg4", type: "multiple-choice", question: "Io non bevo ___ caffè (never).", options: ["mai", "niente", "più", "nessuno"], answer: "mai" },
      { id: "neg5", type: "multiple-choice", question: "Non voglio ___ studiare (anymore).", options: ["più", "mai", "niente", "nessuno"], answer: "più" },
      { id: "neg6", type: "multiple-choice", question: "Lui ___ è stanco.", options: ["non", "no", "mai", "nessuno"], answer: "non" },
      { id: "neg7", type: "multiple-choice", question: "Non mangio ___ io (neither).", options: ["neanche", "niente", "mai", "nessuno"], answer: "neanche" },
      { id: "neg8", type: "multiple-choice", question: "Non ho detto ___ (nothing).", options: ["nulla", "nessuno", "mai", "non"], answer: "nulla" },
      { id: "neg9", type: "multiple-choice", question: "Dove sei? ___ lo so.", options: ["Non", "No", "Mai", "Niente"], answer: "Non" },
      { id: "neg10", type: "multiple-choice", question: "Oggi ___ piove.", options: ["non", "no", "mai", "nessuno"], answer: "non" }
    ]
  },
  {
    id: "comparatives",
    title: "Comparatives",
    level: "A2",
    explanation: "Comparatives are used to compare two things or people.\n\n### Majority (More ... than)\n**più + adjective/adverb + di/che**\n- Use **di** before a noun, pronoun, or numeral.\n- Use **che** before an adjective, verb, or when comparing two things about the same subject.\n\n### Minority (Less ... than)\n**meno + adjective/adverb + di/che** (same rules for di/che as above).\n\n### Equality (As ... as)\n**(così) ... come** or **(tanto) ... quanto**\n- E.g., *Marco è (così) alto come Luigi*.",
    examples: [
      { italian: "Roma è più grande di Firenze.", english: "Rome is bigger than Florence." },
      { italian: "Io sono più alto di te.", english: "I am taller than you." },
      { italian: "È più divertente giocare che studiare.", english: "It's more fun to play than to study." },
      { italian: "Questo libro è meno caro di quello.", english: "This book is less expensive than that one." },
      { italian: "Leggere è meno stancante che correre.", english: "Reading is less tiring than running." },
      { italian: "Marco è alto come Luigi.", english: "Marco is as tall as Luigi." },
      { italian: "Lavoriamo tanto quanto voi.", english: "We work as much as you." },
      { italian: "Il cane è più affettuoso del gatto.", english: "The dog is more affectionate than the cat." },
      { italian: "C'è più vino che acqua.", english: "There is more wine than water." },
      { italian: "Oggi fa meno freddo di ieri.", english: "Today is less cold than yesterday." }
    ],
    exercises: [
      { id: "comp1", type: "multiple-choice", question: "Maria è più alta ___ Lucia.", options: ["di", "che", "come", "quanto"], answer: "di" },
      { id: "comp2", type: "multiple-choice", question: "È più facile parlare ___ scrivere.", options: ["che", "di", "come", "quanto"], answer: "che" },
      { id: "comp3", type: "multiple-choice", question: "Il sole è ___ luminoso della luna.", options: ["più", "molto", "che", "di"], answer: "più" },
      { id: "comp4", type: "multiple-choice", question: "Questa macchina è meno veloce ___ tua.", options: ["della", "di", "che", "come"], answer: "della" },
      { id: "comp5", type: "multiple-choice", question: "Lui è (così) simpatico ___ te.", options: ["come", "di", "che", "quanto"], answer: "come" },
      { id: "comp6", type: "multiple-choice", question: "Mangio tanto ___ te.", options: ["quanto", "come", "di", "che"], answer: "quanto" },
      { id: "comp7", type: "multiple-choice", question: "Ho letto più libri ___ riviste.", options: ["che", "di", "come", "quanto"], answer: "che" },
      { id: "comp8", type: "multiple-choice", question: "La pizza è più buona ___ pasta.", options: ["della", "di", "che", "come"], answer: "della" },
      { id: "comp9", type: "multiple-choice", question: "Viaggiare in treno è meno caro ___ volare.", options: ["che", "di", "come", "quanto"], answer: "che" },
      { id: "comp10", type: "multiple-choice", question: "Pietro è più grande ___ me.", options: ["di", "che", "come", "quanto"], answer: "di" }
    ]
  },
  {
    id: "conjunctions",
    title: "Conjunctions (Congiunzioni)",
    level: "A2",
    explanation: "Conjunctions connect words, phrases, or clauses.\n\n### Coordinating Conjunctions\n- **e** (and): Connects similar ideas.\n- **o / oppure** (or): Offers an alternative.\n- **ma / però** (but): Introduces a contrast.\n- **quindi / perciò** (therefore, so): Indicates a consequence.\n\n### Subordinating Conjunctions\n- **perché** (because, why): Gives a reason.\n- **quando** (when): Indicates time.\n- **se** (if): Introduces a condition.\n- **che** (that): Introduces a subordinate clause (e.g., 'Penso che...').",
    examples: [
      { italian: "Io leggo e lui scrive.", english: "I read and he writes." },
      { italian: "Vuoi acqua o vino?", english: "Do you want water or wine?" },
      { italian: "È piccolo ma forte.", english: "He is small but strong." },
      { italian: "Piove, quindi resto a casa.", english: "It's raining, so I'm staying home." },
      { italian: "Non esco perché sono stanco.", english: "I'm not going out because I'm tired." },
      { italian: "Ti chiamo quando arrivo.", english: "I'll call you when I arrive." },
      { italian: "Se piove, non usciamo.", english: "If it rains, we won't go out." },
      { italian: "So che sei occupato.", english: "I know that you are busy." },
      { italian: "Vengo però faccio tardi.", english: "I'm coming but I'll be late." },
      { italian: "Caffè oppure tè?", english: "Coffee or tea?" }
    ],
    exercises: [
      { id: "conj1", type: "multiple-choice", question: "Mangio una mela ___ una pera.", options: ["e", "o", "ma", "se"], answer: "e" },
      { id: "conj2", type: "multiple-choice", question: "Vuoi andare al mare ___ in montagna?", options: ["o", "e", "ma", "perché"], answer: "o" },
      { id: "conj3", type: "multiple-choice", question: "Volevo uscire, ___ pioveva.", options: ["ma", "e", "o", "perché"], answer: "ma" },
      { id: "conj4", type: "multiple-choice", question: "Studio molto, ___ prendo bei voti.", options: ["quindi", "ma", "se", "o"], answer: "quindi" },
      { id: "conj5", type: "multiple-choice", question: "Non vado a scuola ___ sono malato.", options: ["perché", "quando", "se", "che"], answer: "perché" },
      { id: "conj6", type: "multiple-choice", question: "Ti telefono ___ finisco di lavorare.", options: ["quando", "perché", "che", "ma"], answer: "quando" },
      { id: "conj7", type: "multiple-choice", question: "___ fa bel tempo, andiamo al parco.", options: ["Se", "Quando", "Perché", "Che"], answer: "Se" },
      { id: "conj8", type: "multiple-choice", question: "Penso ___ sia una buona idea.", options: ["che", "se", "quando", "perché"], answer: "che" },
      { id: "conj9", type: "multiple-choice", question: "È intelligente, ___ non studia.", options: ["però", "e", "o", "perché"], answer: "però" },
      { id: "conj10", type: "multiple-choice", question: "Andiamo al ristorante ___ al pub?", options: ["oppure", "e", "ma", "se"], answer: "oppure" }
    ]
  },
  {
    id: "verbs-futuro",
    title: "Future Tense (Futuro Semplice)",
    level: "A2",
    explanation: "The *futuro semplice* expresses actions that will happen in the future. In spoken Italian, the present tense is often used for the near future, but the future tense is needed for distant future or uncertainty.\n\n### Regular Conjugation\nDrop the final -e of the infinitive. For -are verbs, change the 'a' to 'e' (e.g., parlare -> parler-).\nThen add: **-ò, -ai, -à, -emo, -ete, -anno**.\n- Parlare: parlerò, parlerai, parlerà, parleremo, parlerete, parleranno.\n- Leggere: leggerò, leggerai, leggerà, leggeremo, leggerete, leggeranno.\n- Dormire: dormirò, dormirai, dormirà, dormiremo, dormirete, dormiranno.\n\n### Irregular Verbs\n- **Essere**: sarò, sarai, sarà, saremo, sarete, saranno.\n- **Avere**: avrò, avrai, avrà, avremo, avrete, avranno.\n- **Andare**: andrò... **Vedere**: vedrò... **Fare**: farò...",
    examples: [
      { italian: "Domani partirò per Roma.", english: "Tomorrow I will leave for Rome." },
      { italian: "L'anno prossimo studierò lo spagnolo.", english: "Next year I will study Spanish." },
      { italian: "Che cosa farai stasera?", english: "What will you do tonight?" },
      { italian: "Non ci sarò alla festa.", english: "I won't be at the party." },
      { italian: "Quando avrò tempo, leggerò questo libro.", english: "When I have time, I will read this book." },
      { italian: "Andremo al mare quest'estate.", english: "We will go to the sea this summer." },
      { italian: "Vedrete che andrà tutto bene.", english: "You'll see that everything will be fine." },
      { italian: "Sarà vero?", english: "Will it be true? (I wonder if it's true)" },
      { italian: "Loro arriveranno domani.", english: "They will arrive tomorrow." },
      { italian: "Ti scriverò una lettera.", english: "I will write you a letter." }
    ],
    exercises: [
      { id: "fut1", type: "multiple-choice", question: "Domani io ___ (parlare) con il capo.", options: ["parlerò", "parlerai", "parlerà", "parleremo"], answer: "parlerò" },
      { id: "fut2", type: "multiple-choice", question: "Tu ___ (leggere) questo libro?", options: ["leggerai", "leggerò", "leggerà", "leggeremo"], answer: "leggerai" },
      { id: "fut3", type: "multiple-choice", question: "Lui ___ (dormire) in albergo.", options: ["dormirà", "dormirò", "dormirai", "dormiranno"], answer: "dormirà" },
      { id: "fut4", type: "multiple-choice", question: "Noi ___ (andare) in vacanza.", options: ["andremo", "andrò", "andrai", "andranno"], answer: "andremo" },
      { id: "fut5", type: "multiple-choice", question: "Voi ___ (essere) felici.", options: ["sarete", "sarò", "sarai", "saranno"], answer: "sarete" },
      { id: "fut6", type: "multiple-choice", question: "Loro ___ (avere) molto tempo.", options: ["avranno", "avrò", "avrai", "avremo"], answer: "avranno" },
      { id: "fut7", type: "multiple-choice", question: "Io ___ (fare) una torta.", options: ["farò", "farai", "farà", "faremo"], answer: "farò" },
      { id: "fut8", type: "multiple-choice", question: "Maria ___ (vedere) il film.", options: ["vedrà", "vedrò", "vedrai", "vedranno"], answer: "vedrà" },
      { id: "fut9", type: "multiple-choice", question: "Noi ___ (mangiare) al ristorante.", options: ["mangeremo", "mangerò", "mangerai", "mangeranno"], answer: "mangeremo" },
      { id: "fut10", type: "multiple-choice", question: "Tu ___ (capire) quando sarai grande.", options: ["capirai", "capirò", "capirà", "capiranno"], answer: "capirai" }
    ]
  }
];

fs.writeFileSync('/home/waseageru/parli-italiano/src/data/grammarExpanded.json', JSON.stringify(topics, null, 2));
console.log('Successfully generated grammarExpanded.json with 12 topics.');
