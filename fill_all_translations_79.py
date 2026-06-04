import json
import os

scenario_path = 'src/data/exports/social/birthday_wishes'

def fill_vocabulary():
    file_path = os.path.join(scenario_path, 'social_birthday_wishes_vocabulary.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    mapping = {
        "abbiamo": "we have", "accomodati": "make yourself comfortable", "aiutatemi": "help me (plural)",
        "aiuto": "help", "al": "at the / to the", "alla": "at the / to the", "alle": "at",
        "allegro": "cheerful / happy", "allora": "then / so", "almeno": "at least",
        "altri": "others", "altro": "other / else", "amici": "friends", "anche": "also / too",
        "ancora": "still / again", "anni": "years", "aprilo": "open it", "arriva": "arrives / is coming",
        "arrivato": "arrived", "attenzione": "attention", "auguri": "wishes / congratulations",
        "avveri": "comes true", "ballare": "to dance", "bel": "beautiful / nice",
        "bella": "beautiful / nice", "bellissimo": "very beautiful", "bene": "well / good",
        "benissimo": "very well", "bere": "to drink", "bibite": "drinks / beverages",
        "bicchiere": "glass", "biglietto": "card / ticket", "bisogno": "need",
        "bravissima": "very good / very talented", "bravo": "good / talented", "brindisi": "toast",
        "buon": "good", "calma": "calmly", "candeline": "candles", "cantare": "to sing",
        "carta": "paper / card", "casa": "home / house", "ce": "there is / there",
        "certamente": "certainly", "certo": "sure / certain", "cestino": "basket / bin",
        "che": "that / what", "cheeseee": "cheese (for photos)", "chi": "who", "ci": "there / us",
        "ciao": "hi / hello / bye", "cinquanta": "fifty", "cioccolato": "chocolate",
        "città": "city", "colorati": "colored", "come": "how / like", "compi": "you turn (age)",
        "compiere": "to turn (age) / to complete", "compleanno": "birthday",
        "complimenti": "compliments / well done", "comprarli": "to buy them", "comè": "how is it",
        "con": "with", "cosè": "what is it", "cucina": "kitchen / cooking",
        "cucinare": "to cook", "cuore": "heart", "cè": "there is", "da": "from / to",
        "dacqua": "of water", "dare": "to give", "dei": "of the / some", "del": "of the",
        "deliziosa": "delicious", "della": "of the", "delle": "of the / some",
        "dentro": "inside", "desideravo": "I wanted / I desired", "desiderio": "wish / desire",
        "devo": "I must / I have to", "di": "of", "dimenticare": "to forget", "dirà": "will say",
        "disturbarti": "to bother you", "dite": "say (plural)", "ditegli": "tell him",
        "divano": "sofa / couch", "divertendo": "having fun", "divertente": "fun / funny",
        "divertiti": "have fun", "dobbiamo": "we must / we have to", "domani": "tomorrow",
        "dopo": "after / later", "dove": "where", "dovevi": "you had to", "due": "two",
        "ecco": "here is / here", "entra": "come in / enters", "esprimere": "to express",
        "facciamo": "we do / we make", "faccio": "I do / I make", "fare": "to do / to make",
        "fatta": "made / done", "fatto": "made / done", "favore": "favor / please",
        "felice": "happy", "festa": "party", "festeggiare": "to celebrate",
        "figurati": "don't mention it", "finora": "so far", "forse": "maybe / perhaps",
        "forte": "hard / strong / loud", "forza": "come on / strength", "foto": "photo",
        "fuori": "outside / out", "gassosa": "soda / fizzy drink", "generosi": "generous",
        "gentile": "kind", "giorno": "day", "giovanissimo": "very young", "giulia": "Giulia",
        "già": "already", "gli": "the / to him", "grande": "big / great", "grazie": "thanks / thank you",
        "gruppo": "group", "ha": "has", "hai": "you have", "ho": "I have", "idea": "idea",
        "il": "the", "in": "in", "indimenticabile": "unforgettable", "inizia": "starts / begins",
        "iniziata": "started", "insieme": "together", "intanto": "meanwhile",
        "invitare": "to invite", "io": "I", "italiana": "Italian", "la": "the",
        "laiuto": "the help", "lavoro": "work / job", "le": "the", "leggerò": "I will read",
        "lha": "has it", "libero": "free", "libro": "book", "lo": "the / it",
        "lora": "the hour / time", "lui": "he", "ma": "but", "madre": "mother",
        "mangiare": "to eat", "mano": "hand", "marco": "Marco", "mattina": "morning",
        "me": "me", "meriti": "you deserve", "messaggio": "message", "mettere": "to put",
        "metterla": "to put it", "mettiamo": "we put / let's put", "mi": "me / to me",
        "mia": "my / mine", "miei": "my / mine", "mille": "thousand", "molti": "many",
        "molto": "very / much", "momento": "moment", "musica": "music", "ne": "of it / some",
        "nel": "in the", "nervoso": "nervous", "niente": "nothing", "no": "no",
        "noi": "we / us", "non": "not", "nulla": "nothing", "occupa": "takes care / occupies",
        "oggi": "today", "oh": "oh", "ora": "now / hour", "organizzare": "to organize",
        "ottanta": "eighty", "ottima": "excellent / great", "ottimo": "excellent / great",
        "otto": "eight", "pacco": "package / parcel", "palloncini": "balloons",
        "panna": "cream", "paolo": "Paolo", "parla": "speaks / talk", "parlare": "to talk",
        "partie": "party (from English or typo)", "passato": "past / passed",
        "patatine": "chips / fries", "pensa": "thinks / think", "pensato": "thought",
        "pensavo": "I was thinking", "per": "for / to", "perché": "why / because",
        "perfetto": "perfect", "però": "however / but", "pezzo": "piece", "piace": "likes / like",
        "piccola": "small / little", "piccolo": "small / little", "pista": "track / dance floor",
        "più": "more", "po": "bit / little", "pomeriggio": "afternoon", "pompieri": "firefighters",
        "pongo": "put (rare) / Pongo", "porta": "door / brings", "portare": "to bring",
        "portato": "brought", "porti": "you bring / ports", "porto": "I bring / port",
        "posso": "I can", "potevo": "I could", "prego": "you're welcome / please",
        "prendine": "take some", "presto": "soon / early", "prima": "first / before",
        "programmi": "plans / programs", "promesso": "promised", "proprio": "really / just",
        "puoi": "you can", "pure": "also / just / feel free", "quando": "when",
        "quante": "how many", "quanti": "how many", "quanti ne": "how many of them",
        "quanti anni": "how many years / how old", "quanti anni compi": "how old are you turning",
        "quanti ne servono": "how many are needed", "quanti ne vuoi": "how many do you want",
        "quanti ne porti": "how many do you bring", "quello": "that", "quello che": "what / that which",
        "quanti ne abbiamo": "how many do we have", "questo": "this", "quanti ne sono": "how many are there",
        "quanti ne hai": "how many do you have", "quanti ne ha": "how many does he/she have",
        "qui": "here", "quanti ne ho": "how many do I have", "regali": "gifts / presents",
        "regalo": "gift / present", "ricordate": "remember (plural)", "ricordato": "remembered",
        "sabato": "Saturday", "sai": "you know", "salutare": "to greet / to say goodbye",
        "sapevo": "I knew", "sarà": "will be", "scoppiano": "they burst / pop",
        "scrivo": "I write", "se": "if", "secondo": "according to / second",
        "sei": "you are / six", "sembra": "seems / looks like", "sempre": "always",
        "sera": "evening", "serata": "evening", "servono": "are needed", "settemila": "seven thousand",
        "sette": "seven", "si": "yes / self", "sia": "is / be", "sicuramente": "surely",
        "silenzio": "silence", "smesso": "stopped", "soffia": "blows / blow",
        "soffiare": "to blow", "solo": "only / alone", "sono": "I am / they are",
        "sopra": "on top / above", "sorpresa": "surprise", "sospetta": "suspects / suspect",
        "spero": "I hope", "squisita": "exquisite / delicious", "ssh": "shh",
        "stai": "you are / stay", "stasera": "tonight", "stata": "been", "stati": "been / states",
        "sua": "his / her / its", "subito": "immediately", "supporto": "support",
        "sì": "yes", "tagliamo": "we cut / let's cut", "tanta": "so much / a lot of",
        "tante": "so many", "tanti": "many / so many", "tanti auguri": "happy birthday",
        "tardi": "late", "te": "you", "tema": "theme", "ti": "you / to you",
        "torta": "cake", "tra": "between / among / in", "tranquillo": "calm / quiet / don't worry",
        "tre": "three", "trentanni": "thirty years", "trenta": "thirty", "tu": "you",
        "tua": "your", "tuo": "your", "tutti": "all / everyone", "tutto": "all / everything",
        "un": "a / an", "una": "a / an", "uno": "one", "urgente": "urgent",
        "usarò": "I will use", "uscita": "exit", "utile": "useful", "va": "goes / is going",
        "vado": "I go", "ve": "you / there", "vediamo": "we see / let's see",
        "vedo": "I see", "vengono": "they come", "verrà": "will come", "vicini": "near / close",
        "vogliamo": "we want", "voglio": "I want", "vuoi": "you want"
    }
    
    for item in data:
        it = item['italian']
        if not item.get('english'):
            item['english'] = mapping.get(it, "")
            
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Filled translations for {len(data)} vocabulary items.")

def fill_sentences():
    file_path = os.path.join(scenario_path, 'social_birthday_wishes_sentences.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    mapping = {
        "Certamente! Oggi è il tuo compleanno. Tanti auguri!": "Certainly! Today is your birthday. Happy birthday!",
        "Figurati, non potevo dimenticare! Quanti anni compi oggi?": "Don't mention it, I couldn't forget! How old are you turning today?",
        "Trent'anni! Sei ancora giovanissimo, complimenti!": "Thirty years old! You're still very young, congratulations!",
        "Spero di festeggiare con te! Facciamo un brindisi?": "I hope to celebrate with you! Shall we make a toast?",
        "Ottimo! A che ora inizia la festa?": "Great! What time does the party start?",
        "Sì, perfetto. Chi altro viene alla festa?": "Yes, perfect. Who else is coming to the party?",
        "Sarà divertente! Vuoi che porti qualcosa da mangiare?": "It will be fun! Do you want me to bring something to eat?",
        "Va bene, porto io le bibite allora. Ti piace la gassosa?": "Alright, I'll bring the drinks then. Do you like soda?",
        "Di niente! Allora ci vediamo stasera alle otto.": "You're welcome! See you tonight at eight then.",
        "A dopo! Buon compleanno ancora!": "See you later! Happy birthday again!",
        "Grazie! Ho portato un piccolo regalo per te. Auguri!": "Thanks! I brought a small gift for you. Happy birthday!",
        "È una sorpresa! Aprilo e vedi se ti piace.": "It's a surprise! Open it and see if you like it.",
        "Sapevo che ti piace cucinare. Spero ti sia utile!": "I knew you like cooking. I hope it's useful to you!",
        "Prego! C'è anche un biglietto dentro il pacco.": "You're welcome! There's also a card inside the package.",
        "Puoi metterla nel cestino della carta. Vuoi una mano?": "You can put it in the paper bin. Do you want a hand?",
        "Grazie. Ci sono molti altri regali qui, vedo!": "Thanks. I see there are many other gifts here!",
        "Ti meriti tutto questo! Ti piace la festa finora?": "You deserve all this! Are you enjoying the party so far?",
        "Un bicchiere d'acqua va benissimo, grazie.": "A glass of water is just fine, thanks.",
        "Certo, vado a salutare Giulia e Marco.": "Sure, I'm going to say hello to Giulia and Marco.",
        "Certamente! A dopo e grazie ancora.": "Certainly! See you later and thanks again.",
        "Che bella torta! Quante candeline ci sono sopra?": "What a beautiful cake! How many candles are on it?",
        "Certamente! Tanti auguri a te, tanti auguri a te...": "Certainly! Happy birthday to you, happy birthday to you...",
        "Soffia forte! Spero che il tuo desiderio si avveri.": "Blow hard! I hope your wish comes true.",
        "Sembra deliziosa. È al cioccolato o alla panna?": "It looks delicious. Is it chocolate or cream?",
        "Sì, grazie! Un bel pezzo grande, per favore.": "Yes, please! A nice big piece, please.",
        "È squisita! Complimenti a chi l'ha fatta.": "It's exquisite! Compliments to whoever made it.",
        "Tua madre è bravissima in cucina! Vuoi ancora un po' di musica?": "Your mother is very good in the kitchen! Do you want some more music?",
        "Ottima idea! Tutti in pista allora!": "Great idea! Everyone on the dance floor then!",
        "Certo! Tutti vicini alla torta, forza!": "Sure! Everyone close to the cake, come on!",
        "Cheeseee! Che bella serata, grazie di tutto.": "Cheeseee! What a beautiful evening, thanks for everything.",
        "Che bella idea! Quando vogliamo fare la festa?": "What a great idea! When do we want to have the party?",
        "Sì, sabato sera sono libero. Dove facciamo la festa?": "Yes, I'm free Saturday night. Where are we having the party?",
        "Ottimo! Io posso portare la torta e i regali.": "Great! I can bring the cake and the gifts.",
        "Certo, scrivo subito un messaggio a tutti quanti.": "Sure, I'll write a message to everyone right away.",
        "Facciamo un tema 'anni ottanta'! È molto divertente.": "Let's do an 'eighties' theme! It's very fun.",
        "Vado io a comprarli domani mattina. Quanti ne servono?": "I'll go buy them tomorrow morning. How many are needed?",
        "No, lui pensa che sabato io sia fuori città.": "No, he thinks I'm out of town on Saturday.",
        "Se ne occupa Giulia. Gli dirà che ha bisogno di un aiuto.": "Giulia is taking care of it. She'll tell him she needs some help.",
        "Stai tranquillo, abbiamo pensato a tutto noi.": "Don't worry, we've thought of everything.",
        "Promesso! Sarà una sorpresa indimenticabile.": "Promised! It will be an unforgettable surprise."
    }
    
    for item in data:
        it = item['italian']
        if not item.get('english'):
            item['english'] = mapping.get(it, "")
            
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Filled translations for {len(data)} sentences.")

fill_vocabulary()
fill_sentences()
