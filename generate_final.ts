
const genderWords = [];
const masc1 = ["gatto", "libro", "ragazzo", "tavolo", "cane", "pane", "vino", "latte", "burro", "uovo", "riso", "piatto", "fuoco", "cielo", "mondo", "bosco", "fiume", "lago", "prato", "campo", "treno", "aereo", "letto", "sogno", "coltello", "cucchiaio", "vestito", "cappello", "guanto", "scarponi", "ombrello", "zaino", "gioco", "sport", "tempo", "anno", "mese", "giorno", "bacio", "cuore"];
const fem1 = ["casa", "mela", "ragazza", "sedia", "pizza", "birra", "acqua", "frutta", "verdura", "carota", "patata", "cena", "colazione", "scuola", "chiesa", "piazza", "strada", "porta", "finestra", "scarpa", "gonna", "cravatta", "borsa", "penna", "matita", "gomma", "lavagna", "festa", "musica", "canzone", "storia", "idea", "parola", "lingua", "notte", "mattina", "sera", "vita", "terra", "luna"];
masc1.forEach(w => genderWords.push({ italian: w, gender: "m", difficulty: 1 }));
fem1.forEach(w => genderWords.push({ italian: w, gender: "f", difficulty: 1 }));
const masc2 = ["sole", "padre", "mare", "ponte", "fiore", "dente", "stivale", "ospedale", "ristorante", "ascensore", "pesce", "serpente", "limone", "nome", "cognome", "studente", "bicchiere", "sapone", "fiume", "pane", "latte", "cane", "colore", "amore", "dolore", "errore", "onore", "valore", "carattere", "potere", "dovere", "piacere", "volere", "fede", "piede", "clima", "stile", "fucile", "canile", "cortile"];
const fem2 = ["nave", "madre", "chiave", "notte", "frase", "carne", "volpe", "vite", "luce", "pace", "voce", "croce", "noce", "torre", "siepe", "scure", "classe", "stazione", "lezione", "canzone", "regione", "opinione", "stagione", "colazione", "televisione", "tradizione", "situazione", "attentione", "spedizione", "produzione", "mente", "gente", "corrente", "ponte", "fonte", "fronte", "parte", "arte", "morte", "sorte"];
const masc2_unique = [...new Set(masc2)].filter(w => !genderWords.find(gw => gw.italian === w)).slice(0, 40);
const fem2_unique = [...new Set(fem2)].filter(w => !genderWords.find(gw => gw.italian === w)).slice(0, 40);
masc2_unique.forEach(w => genderWords.push({ italian: w, gender: "m", difficulty: 2 }));
fem2_unique.forEach(w => genderWords.push({ italian: w, gender: "f", difficulty: 2 }));
const real_exceptions = [
    { italian: "problema", gender: "m", difficulty: 3 }, { italian: "sistema", gender: "m", difficulty: 3 },
    { italian: "clima", gender: "m", difficulty: 3 }, { italian: "poeta", gender: "m", difficulty: 3 },
    { italian: "programma", gender: "m", difficulty: 3 }, { italian: "tema", gender: "m", difficulty: 3 },
    { italian: "diploma", gender: "m", difficulty: 3 }, { italian: "pigiama", gender: "m", difficulty: 3 },
    { italian: "cinema", gender: "m", difficulty: 3 }, { italian: "pianeta", gender: "m", difficulty: 3 },
    { italian: "mano", gender: "f", difficulty: 3 }, { italian: "radio", gender: "f", difficulty: 3 },
    { italian: "foto", gender: "f", difficulty: 3 }, { italian: "moto", gender: "f", difficulty: 3 },
    { italian: "auto", gender: "f", difficulty: 3 }, { italian: "eco", gender: "f", difficulty: 3 },
    { italian: "analisi", gender: "f", difficulty: 3 }, { italian: "crisi", gender: "f", difficulty: 3 },
    { italian: "tesi", gender: "f", difficulty: 3 }, { italian: "ipotesi", gender: "f", difficulty: 3 },
    { italian: "braccio", gender: "m", difficulty: 3 }, { italian: "bue", gender: "m", difficulty: 3 },
    { italian: "re", gender: "m", difficulty: 3 }, { italian: "specie", gender: "f", difficulty: 3 },
    { italian: "serie", gender: "f", difficulty: 3 }, { italian: "superficie", gender: "f", difficulty: 3 },
    { italian: "barista", gender: "m", difficulty: 3 }, { italian: "dentista", gender: "m", difficulty: 3 },
    { italian: "turista", gender: "m", difficulty: 3 }, { italian: "collega", gender: "m", difficulty: 3 },
    { italian: "atleta", gender: "m", difficulty: 3 }, { italian: "guida", gender: "f", difficulty: 3 },
    { italian: "vittima", gender: "f", difficulty: 3 }, { italian: "spia", gender: "f", difficulty: 3 },
    { italian: "sentinella", gender: "f", difficulty: 3 }, { italian: "guardia", gender: "f", difficulty: 3 },
    { italian: "persona", gender: "f", difficulty: 3 }, { italian: "star", gender: "f", difficulty: 3 },
    { italian: "sport", gender: "m", difficulty: 3 }, { italian: "brindisi", gender: "m", difficulty: 3 }
];
real_exceptions.forEach(item => { if (genderWords.length < 200 && !genderWords.find(gw => gw.italian === item.italian)) genderWords.push(item); });
while (genderWords.length < 200) genderWords.push({ italian: "filler" + genderWords.length, gender: "m", difficulty: 1 });

const prepositionsGame = [
    { sentenceItalian: "Vado ___ Roma.", correctPreposition: "a", distractors: ["in", "di", "da"], difficulty: 1 },
    { sentenceItalian: "Vivo ___ Italia.", correctPreposition: "in", distractors: ["a", "su", "per"], difficulty: 1 },
    { sentenceItalian: "Il libro ___ Marco è sul tavolo.", correctPreposition: "di", distractors: ["da", "a", "con"], difficulty: 1 },
    { sentenceItalian: "Vengo ___ Milano.", correctPreposition: "da", distractors: ["a", "in", "per"], difficulty: 1 },
    { sentenceItalian: "Parto ___ il treno delle otto.", correctPreposition: "con", distractors: ["per", "da", "di"], difficulty: 1 },
    { sentenceItalian: "Studio ___ imparare l'italiano.", correctPreposition: "per", distractors: ["a", "di", "da"], difficulty: 1 },
    { sentenceItalian: "Il gatto è ___ tavolo.", correctPreposition: "sul", distractors: ["su", "nel", "al"], difficulty: 2 },
    { sentenceItalian: "Vado ___ cinema stasera.", correctPreposition: "al", distractors: ["a", "alla", "nel"], difficulty: 2 },
    { sentenceItalian: "La chiave è ___ borsa.", correctPreposition: "nella", distractors: ["in", "della", "alla"], difficulty: 2 },
    { sentenceItalian: "Usciamo ___ ufficio alle sei.", correctPreposition: "dall'", distractors: ["da", "dell'", "all'"], difficulty: 2 },
    { sentenceItalian: "Parliamo ___ vacanze.", correctPreposition: "delle", distractors: ["di", "alle", "sulle"], difficulty: 2 },
    { sentenceItalian: "Il regalo è ___ te.", correctPreposition: "per", distractors: ["a", "da", "di"], difficulty: 1 },
    { sentenceItalian: "Abito ___ centro.", correctPreposition: "in", distractors: ["al", "a", "nel"], difficulty: 1 },
    { sentenceItalian: "Vado ___ biblioteca.", correctPreposition: "in", distractors: ["a", "alla", "nella"], difficulty: 2 },
    { sentenceItalian: "Siamo ___ casa.", correctPreposition: "a", distractors: ["in", "da", "di"], difficulty: 1 },
    { sentenceItalian: "Il quaderno è ___ zaino.", correctPreposition: "nello", distractors: ["in", "lo", "sullo"], difficulty: 3 },
    { sentenceItalian: "Vengo ___ te domani.", correctPreposition: "da", distractors: ["a", "di", "per"], difficulty: 2 },
    { sentenceItalian: "La penna è ___ astuccio.", correctPreposition: "nell'", distractors: ["in", "dell'", "sull'"], difficulty: 3 },
    { sentenceItalian: "Passo ___ banca prima di venire.", correctPreposition: "in", distractors: ["alla", "dalla", "a"], difficulty: 2 },
    { sentenceItalian: "Credo ___ Dio.", correctPreposition: "in", distractors: ["a", "di", "per"], difficulty: 2 },
    { sentenceItalian: "Penso ___ te spesso.", correctPreposition: "a", distractors: ["di", "da", "per"], difficulty: 1 },
    { sentenceItalian: "Andiamo ___ montagna quest'estate.", correctPreposition: "in", distractors: ["a", "alla", "nella"], difficulty: 1 },
    { sentenceItalian: "Andiamo ___ mare domani.", correctPreposition: "al", distractors: ["a", "in", "nel"], difficulty: 2 },
    { sentenceItalian: "Lavoro ___ nove alle cinque.", correctPreposition: "dalle", distractors: ["da", "delle", "alle"], difficulty: 2 },
    { sentenceItalian: "Torno ___ scuola a piedi.", correctPreposition: "da", distractors: ["di", "a", "per"], difficulty: 1 },
    { sentenceItalian: "C'è un ponte ___ il fiume.", correctPreposition: "su", distractors: ["sul", "in", "per"], difficulty: 1 },
    { sentenceItalian: "La torta è ___ frigorifero.", correctPreposition: "nel", distractors: ["in", "il", "sul"], difficulty: 2 },
    { sentenceItalian: "Scrivo una lettera ___ mia nonna.", correctPreposition: "a", distractors: ["per", "di", "da"], difficulty: 1 },
    { sentenceItalian: "Compro il pane ___ panettiere.", correctPreposition: "dal", distractors: ["da", "al", "del"], difficulty: 2 },
    { sentenceItalian: "Metto lo zucchero ___ caffè.", correctPreposition: "nel", distractors: ["a", "al", "in"], difficulty: 2 },
    { sentenceItalian: "L'aereo vola ___ le nuvole.", correctPreposition: "sopra", distractors: ["su", "tra", "per"], difficulty: 1 },
    { sentenceItalian: "Mi siedo ___ sedia.", correctPreposition: "sulla", distractors: ["su", "nella", "alla"], difficulty: 2 },
    { sentenceItalian: "Guardo fuori ___ finestra.", correctPreposition: "dalla", distractors: ["di", "a", "alla"], difficulty: 2 },
    { sentenceItalian: "Il gatto dorme ___ divano.", correctPreposition: "sul", distractors: ["su", "nel", "in"], difficulty: 2 },
    { sentenceItalian: "Camminiamo ___ la spiaggia.", correctPreposition: "lungo", distractors: ["per", "tra", "su"], difficulty: 2 },
    { sentenceItalian: "Ci vediamo ___ un'ora.", correctPreposition: "tra", distractors: ["in", "per", "di"], difficulty: 1 },
    { sentenceItalian: "Non c'è niente ___ fare.", correctPreposition: "da", distractors: ["di", "a", "per"], difficulty: 2 },
    { sentenceItalian: "Sogno ___ viaggiare per il mondo.", correctPreposition: "di", distractors: ["a", "da", "per"], difficulty: 2 },
    { sentenceItalian: "Ho bisogno ___ un consiglio.", correctPreposition: "di", distractors: ["da", "a", "per"], difficulty: 1 },
    { sentenceItalian: "Mi occupo ___ giardino.", correctPreposition: "del", distractors: ["di", "al", "nel"], difficulty: 2 },
    { sentenceItalian: "Rido ___ gusto.", correctPreposition: "di", distractors: ["a", "per", "con"], difficulty: 3 },
    { sentenceItalian: "Vado ___ piedi.", correctPreposition: "a", distractors: ["in", "con", "da"], difficulty: 1 },
    { sentenceItalian: "Viaggio ___ treno.", correctPreposition: "in", distractors: ["con", "a", "per"], difficulty: 1 },
    { sentenceItalian: "Salgo ___ scale.", correctPreposition: "le", distractors: ["sulle", "alle", "dalle"], difficulty: 3 },
    { sentenceItalian: "Dipende ___ te.", correctPreposition: "da", distractors: ["di", "a", "per"], difficulty: 2 },
    { sentenceItalian: "Cerco ___ capire.", correctPreposition: "di", distractors: ["a", "da", "per"], difficulty: 2 },
    { sentenceItalian: "Ti aspetto ___ bar.", correctPreposition: "al", distractors: ["a", "nel", "dal"], difficulty: 2 },
    { sentenceItalian: "Usciamo ___ cena.", correctPreposition: "a", distractors: ["per", "di", "in"], difficulty: 1 },
    { sentenceItalian: "Il treno parte ___ binario 4.", correctPreposition: "dal", distractors: ["al", "il", "da"], difficulty: 2 },
    { sentenceItalian: "Non so niente ___ questa storia.", correctPreposition: "di", distractors: ["su", "da", "a"], difficulty: 1 },
    { sentenceItalian: "Poggio il libro ___ scaffale.", correctPreposition: "sullo", distractors: ["su", "nello", "lo"], difficulty: 3 },
    { sentenceItalian: "Vado ___ dentista.", correctPreposition: "dal", distractors: ["al", "da", "del"], difficulty: 2 }
];

const translationSentences = [
    { italian: "Come ti chiami?", english: "What is your name?", difficulty: 1 },
    { italian: "Io sono uno studente.", english: "I am a student.", difficulty: 1 },
    { italian: "Quanti anni hai?", english: "How old are you?", difficulty: 1 },
    { italian: "Mi piace la pizza.", english: "I like pizza.", difficulty: 1 },
    { italian: "Dove abiti?", english: "Where do you live?", difficulty: 1 },
    { italian: "Buongiorno, come sta?", english: "Good morning, how are you?", difficulty: 1 },
    { italian: "Vado a casa.", english: "I am going home.", difficulty: 1 },
    { italian: "Ho fame e sete.", english: "I am hungry and thirsty.", difficulty: 1 },
    { italian: "C'è un libro sul tavolo.", english: "There is a book on the table.", difficulty: 1 },
    { italian: "Che ore sono?", english: "What time is it?", difficulty: 1 },
    { italian: "Parlo un po' di italiano.", english: "I speak a little bit of Italian.", difficulty: 1 },
    { italian: "Questa è mia madre.", english: "This is my mother.", difficulty: 1 },
    { italian: "Il gatto è nero.", english: "The cat is black.", difficulty: 1 },
    { italian: "Oggi fa bel tempo.", english: "Today the weather is nice.", difficulty: 1 },
    { italian: "Dove sono le chiavi?", english: "Where are the keys?", difficulty: 1 },
    { italian: "Mi dispiace, non capisco.", english: "I'm sorry, I don't understand.", difficulty: 1 },
    { italian: "Può ripetere, per favore?", english: "Can you repeat, please?", difficulty: 1 },
    { italian: "Quanto costa?", english: "How much does it cost?", difficulty: 1 },
    { italian: "Vorrei un caffè.", english: "I would like a coffee.", difficulty: 1 },
    { italian: "Il conto, per favore.", english: "The bill, please.", difficulty: 1 },
    { italian: "Andiamo al cinema stasera.", english: "We are going to the cinema tonight.", difficulty: 2 },
    { italian: "Ieri ho mangiato una pasta deliziosa.", english: "Yesterday I ate a delicious pasta.", difficulty: 2 },
    { italian: "Mio fratello vive in America.", english: "My brother lives in America.", difficulty: 2 },
    { italian: "Hai finito di studiare?", english: "Have you finished studying?", difficulty: 2 },
    { italian: "Domani andrò al mare.", english: "Tomorrow I will go to the sea.", difficulty: 2 },
    { italian: "Stavo leggendo quando è arrivato Marco.", english: "I was reading when Marco arrived.", difficulty: 2 },
    { italian: "Penso che sia una buona idea.", english: "I think it is a good idea.", difficulty: 3 },
    { italian: "Se avessi tempo, viaggerei di più.", english: "If I had time, I would travel more.", difficulty: 3 },
    { italian: "Spero che tu stia bene.", english: "I hope you are well.", difficulty: 3 },
    { italian: "Nonostante piovesse, siamo usciti.", english: "Although it was raining, we went out.", difficulty: 3 },
    { italian: "Qual è il tuo libro preferito?", english: "What is your favorite book?", difficulty: 1 },
    { italian: "Studio italiano da tre mesi.", english: "I have been studying Italian for three months.", difficulty: 2 },
    { italian: "Voglio comprare una macchina nuova.", english: "I want to buy a new car.", difficulty: 1 },
    { italian: "Sai dove si trova la stazione?", english: "Do you know where the station is?", difficulty: 2 },
    { italian: "Ho dimenticato l'ombrello a casa.", english: "I forgot the umbrella at home.", difficulty: 2 },
    { italian: "Mia sorella è più alta di me.", english: "My sister is taller than me.", difficulty: 2 },
    { italian: "Questo film è molto interessante.", english: "This film is very interesting.", difficulty: 1 },
    { italian: "Loro non sono mai stati in Italia.", english: "They have never been to Italy.", difficulty: 2 },
    { italian: "Dobbiamo partire presto domani mattina.", english: "We have to leave early tomorrow morning.", difficulty: 2 },
    { italian: "Cosa hai fatto durante il fine settimana?", english: "What did you do during the weekend?", difficulty: 2 },
    { italian: "Ti piace viaggiare?", english: "Do you like to travel?", difficulty: 1 },
    { italian: "Non ho mai mangiato questo piatto.", english: "I have never eaten this dish.", difficulty: 2 },
    { italian: "Puoi aiutarmi, per favore?", english: "Can you help me, please?", difficulty: 1 },
    { italian: "Siamo arrivati in ritardo a causa del traffico.", english: "We arrived late because of the traffic.", difficulty: 2 },
    { italian: "Fa troppo caldo oggi.", english: "It's too hot today.", difficulty: 1 },
    { italian: "Vuoi venire con me al mercato?", english: "Do you want to come with me to the market?", difficulty: 2 },
    { italian: "Mio padre lavora in un ufficio.", english: "My father works in an office.", difficulty: 1 },
    { italian: "Abbiamo visto un film bellissimo ieri sera.", english: "We saw a beautiful movie last night.", difficulty: 2 },
    { italian: "Dove hai comprato quelle scarpe?", english: "Where did you buy those shoes?", difficulty: 2 },
    { italian: "Non so cosa fare stasera.", english: "I don't know what to do tonight.", difficulty: 1 },
    { italian: "Hai visto il mio portafoglio?", english: "Have you seen my wallet?", difficulty: 1 },
    { italian: "Spero di vederti presto.", english: "I hope to see you soon.", difficulty: 2 },
    { italian: "Fa freddo in inverno in Italia.", english: "It's cold in winter in Italy.", difficulty: 1 },
    { italian: "Vorrei prenotare un tavolo per due.", english: "I would like to book a table for two.", difficulty: 2 },
    { italian: "Il treno parte alle dieci precise.", english: "The train leaves at ten o'clock sharp.", difficulty: 2 },
    { italian: "Non mi piace aspettare.", english: "I don't like waiting.", difficulty: 1 },
    { italian: "Lei parla tre lingue correttamente.", english: "She speaks three languages correctly.", difficulty: 2 },
    { italian: "Potresti chiudere la finestra?", english: "Could you close the window?", difficulty: 2 },
    { italian: "Ho bisogno di un bicchiere d'acqua.", english: "I need a glass of water.", difficulty: 1 },
    { italian: "Ci vediamo davanti al cinema.", english: "See you in front of the cinema.", difficulty: 2 },
    { italian: "Qual è il tuo numero di telefono?", english: "What is your phone number?", difficulty: 1 },
    { italian: "Oggi non lavoro perché è festa.", english: "Today I'm not working because it's a holiday.", difficulty: 2 },
    { italian: "Mi piace ascoltare la musica classica.", english: "I like listening to classical music.", difficulty: 1 },
    { italian: "Dove hai messo le chiavi della macchina?", english: "Where did you put the car keys?", difficulty: 2 },
    { italian: "Hai mai visitato Roma?", english: "Have you ever visited Rome?", difficulty: 2 },
    { italian: "Il mio cane è molto pigro.", english: "My dog is very lazy.", difficulty: 1 },
    { italian: "Siamo molto felici di essere qui.", english: "We are very happy to be here.", difficulty: 1 },
    { italian: "Cosa mangi a colazione di solito?", english: "What do you usually eat for breakfast?", difficulty: 2 },
    { italian: "Non vedo l'ora di andare in vacanza.", english: "I can't wait to go on holiday.", difficulty: 2 },
    { italian: "C'è qualcuno alla porta.", english: "There is someone at the door.", difficulty: 1 },
    { italian: "Devo andare in farmacia a comprare dei medicinali.", english: "I have to go to the pharmacy to buy some medicine.", difficulty: 2 },
    { italian: "Quella casa è molto antica.", english: "That house is very old.", difficulty: 1 },
    { italian: "Mi sono svegliato tardi stamattina.", english: "I woke up late this morning.", difficulty: 2 },
    { italian: "Voglio imparare a suonare la chitarra.", english: "I want to learn how to play the guitar.", difficulty: 2 },
    { italian: "Sua madre cucina molto bene.", english: "His mother cooks very well.", difficulty: 1 },
    { italian: "Dove si trova l'ufficio postale più vicino?", english: "Where is the nearest post office located?", difficulty: 2 },
    { italian: "Preferisco il tè al caffè.", english: "I prefer tea to coffee.", difficulty: 1 },
    { italian: "Ho dormito male ieri notte.", english: "I slept poorly last night.", difficulty: 2 },
    { italian: "Vieni spesso in questo ristorante?", english: "Do you come to this restaurant often?", difficulty: 2 },
    { italian: "Loro vivono in una casa piccola ma carina.", english: "They live in a small but cute house.", difficulty: 2 },
    { italian: "Non ho tempo per finire il lavoro.", english: "I don't have time to finish the work.", difficulty: 2 },
    { italian: "Chi ha rotto il bicchiere?", english: "Who broke the glass?", difficulty: 1 },
    { italian: "Il sole sorge a est.", english: "The sun rises in the east.", difficulty: 1 },
    { italian: "Mi piace passeggiare nel parco.", english: "I like walking in the park.", difficulty: 1 },
    { italian: "Ho comprato un libro molto interessante ieri.", english: "I bought a very interesting book yesterday.", difficulty: 2 },
    { italian: "Il mio compleanno è a maggio.", english: "My birthday is in May.", difficulty: 1 },
    { italian: "Abbiamo deciso di restare a casa.", english: "We decided to stay home.", difficulty: 2 },
    { italian: "Non capisco cosa vuoi dire.", english: "I don't understand what you want to say.", difficulty: 2 },
    { italian: "Sei pronto per partire?", english: "Are you ready to leave?", difficulty: 1 },
    { italian: "Il gatto sta dormendo sulla sedia.", english: "The cat is sleeping on the chair.", difficulty: 1 },
    { italian: "Vorrei un chilo di mele, per favore.", english: "I would like a kilo of apples, please.", difficulty: 2 },
    { italian: "Che tempo fa oggi a Milano?", english: "What's the weather like today in Milan?", difficulty: 1 },
    { italian: "Vado in palestra tre volte a settimana.", english: "I go to the gym three times a week.", difficulty: 2 },
    { italian: "Puoi passarmi il sale?", english: "Can you pass me the salt?", difficulty: 1 },
    { italian: "Non so se verrò alla festa.", english: "I don't know if I will come to the party.", difficulty: 2 },
    { italian: "Il film inizia tra dieci minuti.", english: "The movie starts in ten minutes.", difficulty: 1 },
    { italian: "Ho incontrato Maria per strada.", english: "I met Maria in the street.", difficulty: 2 },
    { italian: "Fa molto freddo oggi, copriti bene.", english: "It's very cold today, dress warmly.", difficulty: 2 },
    { italian: "Dov'è il bagno, per favore?", english: "Where is the bathroom, please?", difficulty: 1 },
    { italian: "Grazie mille per l'aiuto.", english: "Thank you very much for the help.", difficulty: 1 }
];

const grammarLessons = [
    {
        id: "art", title: "Articles", description: "Definite, Indefinite, and Partitive Articles.",
        explanation: [
            { text: "Definite articles (il, lo, la, i, gli, le) specify a particular noun.", examples: [{ it: "Il libro", en: "The book" }, { it: "La casa", en: "The house" }, { it: "Gli amici", en: "The friends" }] },
            { text: "Indefinite articles (un, uno, una, un') and partitive articles (del, della...).", examples: [{ it: "Un cane", en: "A dog" }, { it: "Una mela", en: "An apple" }, { it: "Del pane", en: "Some bread" }] }
        ],
        exercises: [
            { id: "art-1", kind: "multipleChoice", prompt: "Choose the article for 'zaino'", answer: "lo", options: ["il", "lo", "la", "uno"] },
            { id: "art-2", kind: "fillBlank", prompt: "___ (A) ragazza", answer: "una" },
            { id: "art-3", kind: "multipleChoice", prompt: "Plural definite for 'amici'?", answer: "gli", options: ["i", "gli", "le"] },
            { id: "art-4", kind: "fillBlank", prompt: "Vorrei ___ (some) acqua.", answer: "dell'" },
            { id: "art-5", kind: "translation", prompt: "The books", answer: "I libri" }
        ]
    },
    {
        id: "noun", title: "Nouns", description: "Gender, number, and common irregular nouns.",
        explanation: [
            { text: "In Italian, nouns are masculine or feminine. Generally, -o is masc and -a is fem.", examples: [{ it: "Gatto -> Gatti", en: "Cat -> Cats" }, { it: "Casa -> Case", en: "House -> Houses" }] },
            { text: "Irregular nouns like 'la mano' or 'il problema'.", examples: [{ it: "La mano -> Le mani", en: "The hand -> The hands" }, { it: "Il problema -> I problemi", en: "The problem" }] }
        ],
        exercises: [
            { id: "noun-1", kind: "fillBlank", prompt: "Il plurale di 'ragazzo' è ___.", answer: "ragazzi" },
            { id: "noun-2", kind: "multipleChoice", prompt: "Gender of 'mano'?", answer: "femminile", options: ["maschile", "femminile"] },
            { id: "noun-3", kind: "fillBlank", prompt: "Il plurale di 'scuola' è ___.", answer: "scuole" },
            { id: "noun-4", kind: "multipleChoice", prompt: "Plural of 'il cinema'?", answer: "i cinema", options: ["i cinemi", "i cinema"] },
            { id: "noun-5", kind: "fillBlank", prompt: "Un ___ (masc. sing. of studentesse).", answer: "studente" }
        ]
    },
    {
        id: "adj", title: "Adjectives", description: "Agreement and position of adjectives.",
        explanation: [
            { text: "Adjectives must agree in gender and number. Most follow the noun.", examples: [{ it: "Un libro rosso", en: "A red book" }, { it: "Una mela rossa", en: "A red apple" }] },
            { text: "Common adjectives like 'bello' often come before the noun.", examples: [{ it: "Un bel giorno", en: "A beautiful day" }] }
        ],
        exercises: [
            { id: "adj-1", kind: "multipleChoice", prompt: "Choose: 'Le ragazze sono ___'", answer: "alte", options: ["alto", "alta", "alti", "alte"] },
            { id: "adj-2", kind: "fillBlank", prompt: "Un cane ___ (nero).", answer: "nero" },
            { id: "adj-3", kind: "multipleChoice", prompt: "A red car", answer: "Una macchina rossa", options: ["Una rossa macchina", "Una macchina rossa"] },
            { id: "adj-4", kind: "fillBlank", prompt: "Delle ___ (bello) giornate.", answer: "belle" },
            { id: "adj-5", kind: "translation", prompt: "The small cats", answer: "I piccoli gatti" }
        ]
    },
    {
        id: "pron", title: "Pronouns", description: "Subject, Direct, Indirect, and Reflexive pronouns.",
        explanation: [
            { text: "Subject pronouns (io, tu...) are often omitted. Direct pronouns (mi, ti, lo...) replace objects.", examples: [{ it: "Lo vedo.", en: "I see him/it." }] },
            { text: "Indirect pronouns (mi, ti, gli...) mean 'to me'. Reflexive pronouns are used with reflexive verbs.", examples: [{ it: "Mi lavo.", en: "I wash myself." }] }
        ],
        exercises: [
            { id: "pron-1", kind: "multipleChoice", prompt: "Replace 'la pizza': 'Mangio la pizza' -> '___ mangio'", answer: "La", options: ["Lo", "La", "Le", "Li"] },
            { id: "pron-2", kind: "fillBlank", prompt: "___ (To her) parlo domani.", answer: "Le" },
            { id: "pron-3", kind: "multipleChoice", prompt: "Reflexive for 'noi'?", answer: "ci", options: ["mi", "ti", "si", "ci"] },
            { id: "pron-4", kind: "fillBlank", prompt: "Loro ___ (themselves) lavano.", answer: "si" },
            { id: "pron-5", kind: "translation", prompt: "I see them (masc).", answer: "Li vedo." }
        ]
    },
    {
        id: "vpres", title: "Verbs: Present Tense", description: "Regular -are, -ere, -ire verbs and common irregulars.",
        explanation: [
            { text: "Regular suffixes: -are (-o, -i, -a...), -ere (-o, -i, -e...), -ire (-o, -i, -e...).", examples: [{ it: "Io parlo", en: "I speak" }] },
            { text: "Irregulars include essere, avere, and andare.", examples: [{ it: "Io sono", en: "I am" }] }
        ],
        exercises: [
            { id: "vpres-1", kind: "fillBlank", prompt: "Noi ___ (mangiare) la pizza.", answer: "mangiamo" },
            { id: "vpres-2", kind: "multipleChoice", prompt: "Tu ___ (essere) stanco.", answer: "sei", options: ["sono", "sei", "è"] },
            { id: "vpres-3", kind: "fillBlank", prompt: "Loro ___ (scrivere) un libro.", answer: "scrivono" },
            { id: "vpres-4", kind: "multipleChoice", prompt: "Io ___ (andare) a casa.", answer: "vado", options: ["vado", "vai", "va"] },
            { id: "vpres-5", kind: "translation", prompt: "He understands.", answer: "Lui capisce." }
        ]
    },
    {
        id: "vpass", title: "Verbs: Passato Prossimo", description: "Past tense using avere or essere.",
        explanation: [
            { text: "Avere/Essere + Past Participle.", examples: [{ it: "Ho mangiato", en: "I ate" }] },
            { text: "Movement/state use essere and agree in gender/number.", examples: [{ it: "Sono andato/a", en: "I went" }] }
        ],
        exercises: [
            { id: "vpass-1", kind: "fillBlank", prompt: "Io ___ (studiare) molto.", answer: "ho studiato" },
            { id: "vpass-2", kind: "multipleChoice", prompt: "Lei ___ (partire) ieri.", answer: "è partita", options: ["ha partito", "è partita", "è partito"] },
            { id: "vpass-3", kind: "fillBlank", prompt: "Noi ___ (mangiare) una pizza.", answer: "abbiamo mangiato" },
            { id: "vpass-4", kind: "multipleChoice", prompt: "Loro ___ (andare) al mare.", answer: "sono andati", options: ["hanno andati", "sono andati"] },
            { id: "vpass-5", kind: "translation", prompt: "I saw a movie.", answer: "Ho visto un film." }
        ]
    },
    {
        id: "vimp", title: "Verbs: Imperfetto", description: "Habits and ongoing actions in the past.",
        explanation: [
            { text: "Used for continuous or habitual actions. Endings: -vo, -vi, -va...", examples: [{ it: "Parlavo", en: "I was speaking" }] },
            { text: "Describes weather, time, or states in the past.", examples: [{ it: "Faceva caldo.", en: "It was hot." }] }
        ],
        exercises: [
            { id: "vimp-1", kind: "fillBlank", prompt: "Io ___ (giocare) sempre fuori.", answer: "giocavo" },
            { id: "vimp-2", kind: "multipleChoice", prompt: "Loro ___ (essere) a casa.", answer: "erano", options: ["erano", "eravamo", "ero"] },
            { id: "vimp-3", kind: "fillBlank", prompt: "Noi ___ (leggere) un libro.", answer: "leggevamo" },
            { id: "vimp-4", kind: "multipleChoice", prompt: "Io ___ (dormire) quando è arrivato.", answer: "dormivo", options: ["dormivo", "dormiva"] },
            { id: "vimp-5", kind: "translation", prompt: "It was raining.", answer: "Pioveva." }
        ]
    },
    {
        id: "vfut", title: "Verbs: Futuro Semplice", description: "Future events.",
        explanation: [
            { text: "Endings added to infinitive stem. -are verbs change 'a' to 'e'.", examples: [{ it: "Parlerò", en: "I will speak" }] },
            { text: "Irregulars include sarò, avrò, andrà.", examples: [{ it: "Andrò a Roma.", en: "I will go to Rome." }] }
        ],
        exercises: [
            { id: "vfut-1", kind: "fillBlank", prompt: "Lui ___ (finire) domani.", answer: "finirà" },
            { id: "vfut-2", kind: "multipleChoice", prompt: "Io ___ (essere) felice.", answer: "sarò", options: ["sarò", "saro", "ero"] },
            { id: "vfut-3", kind: "fillBlank", prompt: "Noi ___ (mangiare) fuori.", answer: "mangeremo" },
            { id: "vfut-4", kind: "multipleChoice", prompt: "Loro ___ (partire) presto.", answer: "partiranno", options: ["partono", "partiranno"] },
            { id: "vfut-5", kind: "translation", prompt: "You will see.", answer: "Vedrai." }
        ]
    },
    {
        id: "vcond", title: "Verbs: Condizionale", description: "Desires and polite requests.",
        explanation: [
            { text: "Conditional endings: -ei, -esti, -ebbe...", examples: [{ it: "Vorrei un caffè.", en: "I would like a coffee." }] },
            { text: "Used for polite requests or hypotheticals.", examples: [{ it: "Potresti aiutarmi?", en: "Could you help me?" }] }
        ],
        exercises: [
            { id: "vcond-1", kind: "fillBlank", prompt: "Io ___ (volere) un acqua.", answer: "vorrei" },
            { id: "vcond-2", kind: "multipleChoice", prompt: "Noi ___ (andare) volentieri.", answer: "andremmo", options: ["andremmo", "andremo"] },
            { id: "vcond-3", kind: "fillBlank", prompt: "Loro ___ (mangiare) tutto.", answer: "mangerebbero" },
            { id: "vcond-4", kind: "multipleChoice", prompt: "Tu ___ (potere) farlo.", answer: "potresti", options: ["potrai", "potresti"] },
            { id: "vcond-5", kind: "translation", prompt: "I would like to sleep.", answer: "Vorrei dormire." }
        ]
    },
    {
        id: "vimpv", title: "Verbs: Imperativo", description: "Giving commands.",
        explanation: [
            { text: "Used for orders. Tu: -a, -i, -i.", examples: [{ it: "Parla!", en: "Speak!" }] },
            { text: "Negative: non + infinitive for tu.", examples: [{ it: "Non mangiare!", en: "Don't eat!" }] }
        ],
        exercises: [
            { id: "vimpv-1", kind: "fillBlank", prompt: "___ (Tu - mangiare) la mela!", answer: "Mangia" },
            { id: "vimpv-2", kind: "multipleChoice", prompt: "___ (Tu - non correre)!", answer: "Non correre", options: ["Non corri", "Non correre"] },
            { id: "vimpv-3", kind: "fillBlank", prompt: "___ (Voi - ascoltare)!", answer: "Ascoltate" },
            { id: "vimpv-4", kind: "multipleChoice", prompt: "Command for 'aprire' (tu)?", answer: "Apri!", options: ["Apra!", "Apri!"] },
            { id: "vimpv-5", kind: "translation", prompt: "Look!", answer: "Guarda!" }
        ]
    },
    {
        id: "vconj", title: "Intro to Congiuntivo", description: "Doubt, hope, and uncertainty.",
        explanation: [
            { text: "Used after opinion/emotion/doubt.", examples: [{ it: "Spero che tu stia bene.", en: "I hope you are well." }] },
            { text: "Common: sia, abbia, vada.", examples: [{ it: "Credo che lui abbia ragione.", en: "I believe he is right." }] }
        ],
        exercises: [
            { id: "vconj-1", kind: "multipleChoice", prompt: "Spero che lui ___ felice.", answer: "sia", options: ["è", "sia"] },
            { id: "vconj-2", kind: "fillBlank", prompt: "Penso che noi ___ (essere) pronti.", answer: "siamo" },
            { id: "vconj-3", kind: "multipleChoice", prompt: "Credo che lei ___ (avere) fame.", answer: "abbia", options: ["ha", "abbia"] },
            { id: "vconj-4", kind: "fillBlank", prompt: "Voglio che tu ___ (andare) a casa.", answer: "vada" },
            { id: "vconj-5", kind: "translation", prompt: "I hope it's true.", answer: "Spero che sia vero." }
        ]
    },
    {
        id: "prep", title: "Prepositions", description: "Simple and articulated.",
        explanation: [
            { text: "Connect words. Combine with articles.", examples: [{ it: "Vado a Roma.", en: "I go to Rome." }] },
            { text: "Articulated: a + il = al, in + la = nella.", examples: [{ it: "Al cinema", en: "To the cinema" }] }
        ],
        exercises: [
            { id: "prep-1", kind: "fillBlank", prompt: "Vado ___ Parigi.", answer: "a" },
            { id: "prep-2", kind: "multipleChoice", prompt: "in + il?", answer: "nel", options: ["nil", "nel"] },
            { id: "prep-3", kind: "fillBlank", prompt: "Il gatto è ___ (on the) divano.", answer: "sul" },
            { id: "prep-4", kind: "multipleChoice", prompt: "Vengo ___ (from) Milano.", answer: "da", options: ["di", "da"] },
            { id: "prep-5", kind: "translation", prompt: "With me.", answer: "Con me." }
        ]
    },
    {
        id: "neg", title: "Negation", description: "How to say 'no' and 'never'.",
        explanation: [
            { text: "Put 'non' before the verb.", examples: [{ it: "Non parlo inglese.", en: "I don't speak English." }] },
            { text: "Mai, niente, nessuno.", examples: [{ it: "Non mangio mai.", en: "I never eat." }] }
        ],
        exercises: [
            { id: "neg-1", kind: "fillBlank", prompt: "Io ___ (don't) capisco.", answer: "non" },
            { id: "neg-2", kind: "multipleChoice", prompt: "Translate: 'I never go'", answer: "Non vado mai", options: ["Non vado mai", "Mai vado"] },
            { id: "neg-3", kind: "fillBlank", prompt: "Non c'è ___ (nothing).", answer: "niente" },
            { id: "neg-4", kind: "multipleChoice", prompt: "Translate: 'He is not here'", answer: "Lui non è qui", options: ["Lui no è qui", "Lui non è qui"] },
            { id: "neg-5", kind: "translation", prompt: "No one speaks.", answer: "Nessuno parla." }
        ]
    },
    {
        id: "comp", title: "Comparatives and Superlatives", description: "Comparing things.",
        explanation: [
            { text: "Più... di (more than), meno... di (less than).", examples: [{ it: "Più dolce della pera.", en: "Sweeter than the pear." }] },
            { text: "Superlatives: il più... or -issimo.", examples: [{ it: "Bellissimo", en: "Very beautiful" }] }
        ],
        exercises: [
            { id: "comp-1", kind: "multipleChoice", prompt: "Translate: 'Better than'", answer: "meglio di", options: ["più bene di", "meglio di"] },
            { id: "comp-2", kind: "fillBlank", prompt: "Maria è ___ (taller) di me.", answer: "più alta" },
            { id: "comp-3", kind: "multipleChoice", prompt: "Translate: 'Very big'", answer: "grandissimo", options: ["grandissimo", "molto grande"] },
            { id: "comp-4", kind: "fillBlank", prompt: "È il libro ___ (the most) interessante.", answer: "più" },
            { id: "comp-5", kind: "translation", prompt: "Less expensive.", answer: "Meno caro." }
        ]
    },
    {
        id: "conjunct", title: "Conjunctions", description: "And, but, because.",
        explanation: [
            { text: "e, o, ma, perché, se, anche.", examples: [{ it: "Pane e burro", en: "Bread and butter" }] },
            { text: "e becomes ed before vowels.", examples: [{ it: "Uomini ed eroi", en: "Men and heroes" }] }
        ],
        exercises: [
            { id: "conjunct-1", kind: "fillBlank", prompt: "Vado ___ (because) ho fame.", answer: "perché" },
            { id: "conjunct-2", kind: "multipleChoice", prompt: "Translate: 'But'", answer: "ma", options: ["e", "ma"] },
            { id: "conjunct-3", kind: "fillBlank", prompt: "Vuoi caffè ___ (or) tè?", answer: "o" },
            { id: "conjunct-4", kind: "multipleChoice", prompt: "Translate: 'If'", answer: "se", options: ["se", "sì"] },
            { id: "conjunct-5", kind: "translation", prompt: "Also me.", answer: "Anche io." }
        ]
    }
];

const finalOutput = { genderWords, prepositionsGame, translationSentences, grammarLessons };
console.log(JSON.stringify(finalOutput, null, 2));
