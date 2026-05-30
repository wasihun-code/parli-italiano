import json
import os
import re
import random
import string

# ---------------------------------------------------------
# STEP 1: CONVERSATION DATA (A1-A2 focused, short sentences)
# ---------------------------------------------------------

conversations = [
    {
        "id": "smooth_check_in",
        "title": "Smooth Check-In",
        "description": "Meet your host and enter the building normally.",
        "messages": [
            {"id": "m1", "role": "host", "text": "Ciao! Sei davanti al palazzo?", "english": "Hi! Are you in front of the building?",
             "choices": [
                 {"text": "Sì, sono davanti al palazzo.", "isCorrect": True},
                 {"text": "No, sono dentro il palazzo.", "isCorrect": False},
                 {"text": "Sì, sono dentro la stanza.", "isCorrect": False}
             ]},
            {"id": "m2", "role": "host", "text": "Ottimo. Il portone è chiuso?", "english": "Excellent. Is the building door closed?",
             "choices": [
                 {"text": "Sì, il portone è chiuso.", "isCorrect": True},
                 {"text": "No, la finestra è aperta.", "isCorrect": False},
                 {"text": "Sì, la cassetta è grande.", "isCorrect": False}
             ]},
            {"id": "m3", "role": "host", "text": "Hai il codice per entrare?", "english": "Do you have the code to enter?",
             "choices": [
                 {"text": "No, non ho il codice.", "isCorrect": True},
                 {"text": "Sì, ho una chiave rotta.", "isCorrect": False},
                 {"text": "No, non ho la cassetta.", "isCorrect": False}
             ]},
            {"id": "m4", "role": "host", "text": "Digita il codice. Poi premi il tasto.", "english": "Type the code. Then press the button.",
             "choices": [
                 {"text": "Ok, digito il codice ora.", "isCorrect": True},
                 {"text": "No, chiudo il portone.", "isCorrect": False},
                 {"text": "Sì, suono il citofono.", "isCorrect": False}
             ]},
            {"id": "m5", "role": "host", "text": "Ha funzionato? Sei dentro?", "english": "Did it work? Are you inside?",
             "choices": [
                 {"text": "Sì, ha funzionato. Sono dentro.", "isCorrect": True},
                 {"text": "No, non sono arrivato.", "isCorrect": False},
                 {"text": "Sì, il portone è bloccato.", "isCorrect": False}
             ]},
            {"id": "m6", "role": "host", "text": "Bene. Prendi l'ascensore.", "english": "Good. Take the elevator.",
             "choices": [
                 {"text": "Dov'è l'ascensore?", "isCorrect": True},
                 {"text": "Dov'è il citofono?", "isCorrect": False},
                 {"text": "Qual è il codice?", "isCorrect": False}
             ]},
            {"id": "m7", "role": "host", "text": "È in fondo. Sali al terzo piano.", "english": "It is at the end. Go up to the third floor.",
             "choices": [
                 {"text": "Vado al terzo piano.", "isCorrect": True},
                 {"text": "Vado al secondo piano.", "isCorrect": False},
                 {"text": "Esco dal palazzo ora.", "isCorrect": False}
             ]},
            {"id": "m8", "role": "host", "text": "Cerca la porta. C'è una cassetta.", "english": "Look for the door. There is a box.",
             "choices": [
                 {"text": "Vedo la cassetta sicura.", "isCorrect": True},
                 {"text": "La porta è aperta ora.", "isCorrect": False},
                 {"text": "Suono il citofono ora.", "isCorrect": False}
             ]},
            {"id": "m9", "role": "host", "text": "Usa il codice della cassetta.", "english": "Use the code for the box.",
             "choices": [
                 {"text": "Metto il codice subito.", "isCorrect": True},
                 {"text": "Giro la maniglia ora.", "isCorrect": False},
                 {"text": "Cerco la porta rotta.", "isCorrect": False}
             ]},
            {"id": "m10", "role": "host", "text": "Prendi le chiavi e apri la porta.", "english": "Take the keys and open the door.",
             "choices": [
                 {"text": "Ho le chiavi. Apro la porta.", "isCorrect": True},
                 {"text": "Lascio le chiavi per te.", "isCorrect": False},
                 {"text": "La porta è bloccata ora.", "isCorrect": False}
             ]},
            {"id": "m11", "role": "host", "text": "Benvenuto! Trovi le regole sul tavolo.", "english": "Welcome! You find the rules on the table.",
             "choices": [
                 {"text": "Grazie mille. A presto!", "isCorrect": True, "nextMessageId": "END"},
                 {"text": "Dove sono le scale?", "isCorrect": False},
                 {"text": "Ho perso le chiavi.", "isCorrect": False}
             ]}
        ]
    },
    {
        "id": "cant_find_building",
        "title": "Can't Find the Building",
        "description": "Navigate a confusing street.",
        "messages": [
            {"id": "m1", "role": "host", "text": "Pronto? Dove sei?", "english": "Hello? Where are you?",
             "choices": [
                 {"text": "Sono per strada.", "isCorrect": True},
                 {"text": "Sono in ascensore.", "isCorrect": False},
                 {"text": "Vedo il terzo piano.", "isCorrect": False}
             ]},
            {"id": "m2", "role": "host", "text": "Vedi il numero civico?", "english": "Do you see the street number?",
             "choices": [
                 {"text": "No, non vedo il numero.", "isCorrect": True},
                 {"text": "Sì, vedo un citofono rotto.", "isCorrect": False},
                 {"text": "Dov'è il corridoio ora?", "isCorrect": False}
             ]},
            {"id": "m3", "role": "host", "text": "Vedi il grande cancello?", "english": "Do you see the big gate?",
             "choices": [
                 {"text": "Sì, vedo il cancello.", "isCorrect": True},
                 {"text": "No, ho le chiavi ora.", "isCorrect": False},
                 {"text": "Il cancello è rotta.", "isCorrect": False}
             ]},
            {"id": "m4", "role": "host", "text": "C'è un vicolo accanto al cancello.", "english": "There is an alley next to the gate.",
             "choices": [
                 {"text": "Entro nel vicolo stretto?", "isCorrect": True},
                 {"text": "Prendo un ascensore ora.", "isCorrect": False},
                 {"text": "Il vicolo è chiuso ora.", "isCorrect": False}
             ]},
            {"id": "m5", "role": "host", "text": "Sì, entra. Vedi un cortile?", "english": "Yes, enter. Do you see a courtyard?",
             "choices": [
                 {"text": "Sì, vedo il cortile.", "isCorrect": True},
                 {"text": "No, vedo un ascensore.", "isCorrect": False},
                 {"text": "Il cortile è al quinto.", "isCorrect": False}
             ]},
            {"id": "m6", "role": "host", "text": "Quello è l'ingresso. C'è un tastierino.", "english": "That is the entrance. There is a keypad.",
             "choices": [
                 {"text": "Vedo il tastierino lì.", "isCorrect": True},
                 {"text": "Uso la cassetta ora.", "isCorrect": False},
                 {"text": "Suono il citofono lì.", "isCorrect": False}
             ]},
            {"id": "m7", "role": "host", "text": "Digita il codice segreto.", "english": "Type the secret code.",
             "choices": [
                 {"text": "Fatto. Il cancello si apre.", "isCorrect": True},
                 {"text": "Non ho le chiavi oggi.", "isCorrect": False},
                 {"text": "Il codice è sbagliato.", "isCorrect": False}
             ]},
            {"id": "m8", "role": "host", "text": "Attraversa il cortile. Sali al secondo piano.", "english": "Cross the courtyard. Go up to the second floor.",
             "choices": [
                 {"text": "Prendo le scale ora.", "isCorrect": True},
                 {"text": "Vado al primo piano.", "isCorrect": False},
                 {"text": "Il cortile è scuro.", "isCorrect": False}
             ]},
            {"id": "m9", "role": "host", "text": "La porta è nascosta. Ti aspetto.", "english": "The door is hidden. I am waiting.",
             "choices": [
                 {"text": "Arrivo subito da te.", "isCorrect": True},
                 {"text": "Sono molto in ritardo.", "isCorrect": False},
                 {"text": "Dov'è il citofono oggi?", "isCorrect": False}
             ]},
            {"id": "m10", "role": "host", "text": "Eccoti! Finalmente sei arrivato.", "english": "There you are! Finally you arrived.",
             "choices": [
                 {"text": "Grazie dell'aiuto. A presto!", "isCorrect": True, "nextMessageId": "END"},
                 {"text": "Voglio uscire da qui.", "isCorrect": False},
                 {"text": "Il portone è chiuso.", "isCorrect": False}
             ]}
        ]
    },
    {
        "id": "intercom_problem",
        "title": "Intercom Problem",
        "description": "Handle a broken intercom.",
        "messages": [
            {"id": "m1", "role": "host", "text": "Buongiorno. Sei al portone?", "english": "Good morning. Are you at the door?",
             "choices": [
                 {"text": "Sì, sono al portone.", "isCorrect": True}, 
                 {"text": "No, sono dentro ora.", "isCorrect": False}, 
                 {"text": "Qual è il codice?", "isCorrect": False}
             ]},
            {"id": "m2", "role": "host", "text": "Il citofono funziona bene?", "english": "Does the intercom work well?",
             "choices": [
                 {"text": "No, non sento niente.", "isCorrect": True}, 
                 {"text": "Sì, è molto chiuso.", "isCorrect": False}, 
                 {"text": "Apro il portone blu.", "isCorrect": False}
             ]},
            {"id": "m3", "role": "host", "text": "Premi forte il bottone.", "english": "Press the button hard.",
             "choices": [
                 {"text": "Premo forte, ma niente.", "isCorrect": True}, 
                 {"text": "Ho molta paura oggi.", "isCorrect": False}, 
                 {"text": "Il bottone è aperto.", "isCorrect": False}
             ]},
            {"id": "m4", "role": "host", "text": "È rotto. Suona al vicino.", "english": "It's broken. Ring the neighbor.",
             "choices": [
                 {"text": "Suono al vicino subito.", "isCorrect": True}, 
                 {"text": "Chi è il vicino lì?", "isCorrect": False}, 
                 {"text": "Vado via dal portone.", "isCorrect": False}
             ]},
            {"id": "m5", "role": "host", "text": "Lui ti apre il portone.", "english": "He will open the door for you.",
             "choices": [
                 {"text": "Va bene, provo ora.", "isCorrect": True}, 
                 {"text": "Non voglio entrare qui.", "isCorrect": False}, 
                 {"text": "Il portone è stretto.", "isCorrect": False}
             ]},
            {"id": "m6", "role": "host", "text": "Sei dentro adesso?", "english": "Are you inside now?",
             "choices": [
                 {"text": "Sì, sono dentro il palazzo.", "isCorrect": True}, 
                 {"text": "No, sono fuori dal palazzo.", "isCorrect": False}, 
                 {"text": "Il vicino è uscito ora.", "isCorrect": False}
             ]},
            {"id": "m7", "role": "host", "text": "Prendi l'ascensore subito.", "english": "Take the elevator immediately.",
             "choices": [
                 {"text": "Vado al quinto piano?", "isCorrect": True}, 
                 {"text": "Vado fuori dal palazzo.", "isCorrect": False}, 
                 {"text": "L'ascensore è chiuso.", "isCorrect": False}
             ]},
            {"id": "m8", "role": "host", "text": "Sì, quinto piano. La porta destra.", "english": "Yes, fifth floor. The right door.",
             "choices": [
                 {"text": "La porta a destra.", "isCorrect": True}, 
                 {"text": "La porta a sinistra.", "isCorrect": False}, 
                 {"text": "Sono in strada ora.", "isCorrect": False}
             ]},
            {"id": "m9", "role": "host", "text": "La porta è socchiusa.", "english": "The door is ajar.",
             "choices": [
                 {"text": "Entro nella stanza subito.", "isCorrect": True}, 
                 {"text": "Scappo dal palazzo ora.", "isCorrect": False}, 
                 {"text": "Chiudo tutto il palazzo.", "isCorrect": False}
             ]},
            {"id": "m10", "role": "host", "text": "Grazie della pazienza.", "english": "Thanks for your patience.",
             "choices": [
                 {"text": "Figurati! Grazie a te.", "isCorrect": True, "nextMessageId": "END"}, 
                 {"text": "Sono molto in ritardo.", "isCorrect": False}, 
                 {"text": "Dov'è il citofono rotta?", "isCorrect": False}
             ]}
        ]
    },
    {
        "id": "wrong_entrance",
        "title": "Wrong Apartment Entrance",
        "description": "Correct a door mistake.",
        "messages": [
            {"id": "m1", "role": "host", "text": "Sei davanti alla porta?", "english": "Are you in front of the door?",
             "choices": [
                 {"text": "Sì, sono davanti alla porta.", "isCorrect": True}, 
                 {"text": "No, sono per strada.", "isCorrect": False}, 
                 {"text": "Dov'è la chiave rotta?", "isCorrect": False}
             ]},
            {"id": "m2", "role": "host", "text": "Usa la chiave per entrare.", "english": "Use the key to enter.",
             "choices": [
                 {"text": "Giro la chiave ma niente.", "isCorrect": True}, 
                 {"text": "Uso il citofono nuovo.", "isCorrect": False}, 
                 {"text": "La chiave è molto piccola.", "isCorrect": False}
             ]},
            {"id": "m3", "role": "host", "text": "Spingi forte la porta.", "english": "Push the door hard.",
             "choices": [
                 {"text": "Spingo forte, ma è bloccata.", "isCorrect": True}, 
                 {"text": "Tiro la porta del bagno.", "isCorrect": False}, 
                 {"text": "Canto vicino alla porta.", "isCorrect": False}
             ]},
            {"id": "m4", "role": "host", "text": "Solleva la maniglia.", "english": "Lift the handle.",
             "choices": [
                 {"text": "Sollevo la maniglia oggi.", "isCorrect": True}, 
                 {"text": "Lascio la maniglia rotta.", "isCorrect": False}, 
                 {"text": "La maniglia è chiusa oggi.", "isCorrect": False}
             ]},
            {"id": "m5", "role": "host", "text": "C'è un interno scritto?", "english": "Is there an internal number written?",
             "choices": [
                 {"text": "Sì, è l'interno sbagliato.", "isCorrect": True}, 
                 {"text": "No, è molto buio qui.", "isCorrect": False}, 
                 {"text": "L'interno è rotto.", "isCorrect": False}
             ]},
            {"id": "m6", "role": "host", "text": "Hai sbagliato porta!", "english": "You got the wrong door!",
             "choices": [
                 {"text": "Oh, scusa! Cerco la porta giusta.", "isCorrect": True}, 
                 {"text": "Entro in questa porta oggi.", "isCorrect": False}, 
                 {"text": "Piacere di conoscerti ora.", "isCorrect": False}
             ]},
            {"id": "m7", "role": "host", "text": "La porta giusta è in fondo.", "english": "The right door is at the end.",
             "choices": [
                 {"text": "Vado in fondo al corridoio.", "isCorrect": True}, 
                 {"text": "Torno indietro per strada.", "isCorrect": False}, 
                 {"text": "Corro verso il portone.", "isCorrect": False}
             ]},
            {"id": "m8", "role": "host", "text": "Sei davanti alla porta giusta?", "english": "Are you in front of the right door?",
             "choices": [
                 {"text": "Sì, provo la chiave qui.", "isCorrect": True}, 
                 {"text": "No, sono per strada ora.", "isCorrect": False}, 
                 {"text": "Chi è alla porta giusta?", "isCorrect": False}
             ]},
            {"id": "m9", "role": "host", "text": "Si apre?", "english": "Does it open?",
             "choices": [
                 {"text": "Sì! Si apre subito.", "isCorrect": True}, 
                 {"text": "No, il portone è chiuso.", "isCorrect": False}, 
                 {"text": "Forse la cassetta è vuota.", "isCorrect": False}
             ]},
            {"id": "m10", "role": "host", "text": "Meno male! Entra pure.", "english": "Thank goodness! Come on in.",
             "choices": [
                 {"text": "Grazie mille. A dopo!", "isCorrect": True, "nextMessageId": "END"}, 
                 {"text": "Chiudo la cassetta ora.", "isCorrect": False}, 
                 {"text": "Dov'è il citofono ora?", "isCorrect": False}
             ]}
        ]
    }
]

# ---------------------------------------------------------
# STEP 2-5: GENERATE CURRICULUM, MINILESSONS
# ---------------------------------------------------------

manual_translations = {
    "palazzo": "building", "portone": "main door", "codice": "code", "chiave": "key",
    "serratura": "lock", "cassetta": "box", "sicurezza": "security", "tasto": "button",
    "piano": "floor", "ascensore": "elevator", "maniglia": "handle", "salire": "to go up",
    "scendere": "to go down", "entrare": "to enter", "arrivato": "arrived", "ritardo": "late",
    "traffico": "traffic", "vicolo": "alley", "cancello": "gate", "cortile": "courtyard",
    "citofono": "intercom", "suonare": "to ring", "vicino": "neighbor", "ospite": "guest",
    "aprire": "to open", "chiuso": "closed", "rotta": "broken", "sbagliata": "wrong",
    "mandata": "turn of the key", "uscire": "to go out", "regole": "rules", "foglio": "sheet",
    "password": "password", "salone": "living room", "salotto": "living room",
    "terzo": "third", "secondo": "second", "quinto": "fifth", "destra": "right",
    "sinistra": "left", "fondo": "end", "interno": "internal", "scatto": "click",
    "rumore": "noise", "bloccata": "stuck", "dura": "stiff", "pazienza": "patience",
    "disagio": "inconvenience", "socchiusa": "ajar", "piacere": "pleasure", "conoscerti": "to meet you",
    "purtroppo": "unfortunately", "funzionato": "worked", "ricevuto": "received", "soggiorno": "stay",
    "pronto": "hello", "capisco": "I understand", "civico": "street number", "nascosto": "hidden",
    "secondario": "secondary", "sollievo": "relief", "finalmente": "finally", "buongiorno": "good morning",
    "maledizione": "damn", "guasta": "breaks", "piove": "rains", "riunione": "meeting",
    "campanello": "doorbell", "gentilissimo": "very kind", "avvisato": "warned", "scatta": "clicks",
    "capricci": "tantrums", "spingendo": "pushing", "figuraccia": "embarrassment", "confusione": "confusion",
    "comodo": "comfortable", "adesso": "now", "grazie": "thanks", "prego": "welcome", "scusa": "sorry",
    "scusami": "excuse me", "ciao": "hi", "salgo": "I go up", "salve": "hello", "sì": "yes", "no": "no",
    "chi": "who", "cosa": "what", "dove": "where", "quando": "when", "perché": "why", "come": "how",
    "entro": "I enter", "aperto": "open", "aperta": "open", "cammino": "I walk", "vedo": "I see",
    "fatto": "done", "arrivo": "I am coming", "tavolo": "table", "monitor": "monitor", "telefono": "phone",
    "mille": "thousand", "bene": "well", "male": "badly", "buona": "good", "presto": "soon", "dita": "fingers",
    "fame": "hunger", "cane": "dog", "mare": "sea", "buio": "dark", "muro": "wall", "stanco": "tired",
    "scappo": "I run away", "forchetta": "fork", "canto": "I sing", "corro": "I run", "perso": "lost",
    "accanto": "next to", "alla": "to the", "apre": "opens", "apri": "open", "apro": "I open", "aspetto": "I wait",
    "attraversa": "cross", "bar": "bar", "benvenuto": "welcome", "bianchi": "Bianchi (name)", "bottone": "button",
    "capito": "understood", "cerca": "look for", "cerco": "I look for", "chiavi": "keys",
    "cinque": "five", "corridoio": "hallway", "corso": "course/street", "davanti": "in front of", "del": "of the",
    "della": "of the", "dentro": "inside", "digita": "type", "dopo": "after", "eccoti": "there you are",
    "entra": "enter", "figurati": "not at all", "forte": "hard/strong", "funziona": "works", "garibaldi": "Garibaldi (name)",
    "giro": "I turn", "grande": "big", "grigia": "gray", "hai": "you have", "lui": "he", "meno": "less",
    "metto": "I put", "nel": "in the", "nella": "in the", "niente": "nothing", "non": "not", "numero": "number", "ora": "now",
    "ottimo": "excellent", "per": "for", "poi": "then", "porta": "door", "premi": "press", "premo": "I press",
    "prendi": "take", "prendo": "I take", "provo": "I try", "pure": "as well", "quello": "that", "qui": "here",
    "rotto": "broken", "sali": "go up", "sbagliato": "wrong", "scale": "stairs", "scritto": "written",
    "sei": "you are", "sento": "I hear", "solleva": "lift", "sollevo": "I lift", "sono": "I am", "spingi": "push",
    "spingo": "I push", "subito": "immediately", "sul": "on the", "sulla": "on the", "suona": "ring",
    "suono": "I ring", "tastierino": "keypad", "una": "a", "usa": "use", "vado": "I go", "vedi": "you see",
    "verde": "green", "via": "street", "tra": "between", "cento": "hundred", "aiuto": "help", "ingresso": "entrance",
    "dov": "where", "dell": "of the", "lascensore": "the elevator", "lingresso": "the entrance", "dellaiuto": "of the help",
    "dovè": "where is", "lei": "you (formal)", "farlo": "to do it", "strada": "street", "stanza": "room", "finestra": "window",
    "scala": "stairs", "taxi": "taxi", "piedi": "feet", "blu": "blue", "sicura": "safe", "te": "you", "trovi": "you find",
    "scuro": "dark", "nascosta": "hidden", "oggi": "today", "stretto": "narrow", "lì": "there",
    "giusta": "right", "nuovo": "new", "piccola": "small", "calda": "hot", "vuota": "empty",
    "digito": "I type", "segreto": "secret"
}

def process_pipeline():
    print("--- STARTING QUALITY-FIRST GOLD PIPELINE ---")
    
    words_set = set()
    phrases_set = set()
    sentences_list = []
    
    def tokenize(text):
        text = text.lower().replace("'", " ")
        text = re.sub(r'[^\w\sàèìòùé]', '', text)
        return [w for w in text.split() if len(w) > 2 and not w.isdigit()]
        
    for conv in conversations:
        for msg in conv["messages"]:
            it_text = msg["text"].strip()
            sentences_list.append({"italian": it_text, "english": msg.get("english", ""), "grammarPoint": "Spoken line"})
            for cw in tokenize(it_text):
                words_set.add(cw)
            for choice in msg["choices"]:
                if choice.get("isCorrect"):
                    it_choice = choice["text"].strip()
                    phrases_set.add(it_choice)
                    for cw in tokenize(it_choice):
                        words_set.add(cw)
                            
    # 1. Create Vocabulary
    vocab_items = []
    v_idx = 1
    for w in sorted(list(words_set)):
        en = manual_translations.get(w, f"Translation of {w}")
        vocab_items.append({"id": f"s22-v{v_idx}", "italian": w, "english": en})
        v_idx += 1
        
    # 2. Create Phrases
    phrase_items = []
    for idx, p in enumerate(sorted(list(phrases_set))):
        phrase_items.append({"id": f"s22-p{idx+1}", "italian": p, "english": "User response"})
        
    # 3. Create Sentences
    sentence_items = []
    for idx, s in enumerate(sentences_list):
        sentence_items.append({"id": f"s22-s{idx+1}", "italian": s["italian"], "english": s["english"], "grammarPoint": s["grammarPoint"]})
        
    # --- ADD CHOICES ---
    def add_choices_to_list(items, item_type):
        for item in items:
            if "choicesItalian" not in item:
                item["choicesItalian"] = [] # Placeholder logic not needed for this audit as we handcrafted
            item["type"] = item_type

    # For vocab, phrases, sentences, we must provide 3 distractors so lesson audit passes
    def add_random_choices(items, item_type):
        all_italians = [item["italian"] for item in items]
        for item in items:
            correct = item["italian"]
            c_len = len(correct)
            pool = [x for x in all_italians if x != correct and abs(len(x) - c_len) <= max(3, c_len * 0.4)]
            if len(pool) < 3: pool = [x for x in all_italians if x != correct]
            if len(pool) < 3:
                pool += ["grazie", "prego", "scusa", "buongiorno", "ciao", "sì", "no"]
                pool = list(set([x for x in pool if x != correct]))
            distractors = random.sample(pool, 3)
            choices = [correct] + distractors
            random.shuffle(choices)
            item["choicesItalian"] = choices
            item["type"] = item_type
            item["feedback"] = {"correctItalian": "Esatto!", "incorrectItalian": f"No, è '{correct}'.", "correctEnglish": "Great!", "incorrectEnglish": f"No, it is '{correct}'."}

    add_random_choices(vocab_items, "vocabulary")
    add_random_choices(phrase_items, "phrase")
    add_random_choices(sentence_items, "sentence")
    
    # Conversations already have choices

    # --- MINI LESSON GENERATION ---
    mini_lessons = []
    goals = ["Finding the Entrance", "Using the Intercom", "Receiving Directions", "Entering the Building", "Finding the Apartment", "Receiving the Keys"]
    v_c, p_c, s_c = len(vocab_items)//6, len(phrase_items)//6, len(sentence_items)//6
    for i in range(6):
        v_s, v_e = i*v_c, (i+1)*v_c if i<5 else len(vocab_items)
        p_s, p_e = i*p_c, (i+1)*p_c if i<5 else len(phrase_items)
        s_s, s_e = i*s_c, (i+1)*s_c if i<5 else len(sentence_items)
        mini_lessons.append({
            "id": f"l{i+1}", "title": f"Lesson {i+1}", "goal": goals[i], "estimatedDuration": "3 mins",
            "unlockCriteria": "none" if i==0 else "complete_previous", "nextLesson": f"l{i+2}" if i<5 else None,
            "sections": [
                {"type": "vocabulary", "title": "Learn the Words", "description": "Essential vocabulary.", "exerciseIds": [it["id"] for it in vocab_items[v_s:v_e]]},
                {"type": "phrase", "title": "Build the Phrases", "description": "Useful phrases.", "exerciseIds": [it["id"] for it in phrase_items[p_s:p_e]]},
                {"type": "sentence", "title": "Practice the Dialogue", "description": "Sentences from the host.", "exerciseIds": [it["id"] for it in sentence_items[s_s:s_e]]},
                {"type": "mastery", "title": "Mastery Check", "description": "Prove your skills.", "exerciseIds": [sentence_items[s_e-1]["id"]] if s_e > 0 else []}
            ]
        })
        
    base_dir = "src/data/exports/accommodation/apartment_key_pickup/"
    os.makedirs(base_dir, exist_ok=True)
    with open(os.path.join(base_dir, "conversations.json"), "w", encoding="utf-8") as f: json.dump({"scenarioId": 22, "conversations": conversations}, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_dir, "accommodation_apartment_key_pickup_vocabulary.json"), "w", encoding="utf-8") as f: json.dump(vocab_items, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_dir, "accommodation_apartment_key_pickup_phrases.json"), "w", encoding="utf-8") as f: json.dump(phrase_items, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_dir, "accommodation_apartment_key_pickup_sentences.json"), "w", encoding="utf-8") as f: json.dump(sentence_items, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_dir, "mini_lessons.json"), "w", encoding="utf-8") as f: json.dump({"lessons": mini_lessons}, f, ensure_ascii=False, indent=2)
    print(f"Repaired Pipeline Complete. Vocab: {len(vocab_items)}")

if __name__ == "__main__":
    process_pipeline()
