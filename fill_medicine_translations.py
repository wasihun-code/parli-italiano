import json
import os
import re

def tokenize(text):
    text = text.lower()
    text = text.replace("'", " ")
    text = re.sub(r'[^\w\sàèìòùé]', '', text)
    # Filter out short words and numbers
    return [w for w in text.split() if len(w) > 2 and not w.isdigit()]

def main():
    scenario_slug = "health/buying_medicine"
    base_path = f"src/data/exports/{scenario_slug}"
    conv_path = os.path.join(base_path, "conversations.json")
    prefix = "health_buying_medicine"
    
    with open(conv_path, "r", encoding="utf-8") as f:
        conversations = json.load(f)["conversations"]

    all_sentences = set()
    all_phrases = set()
    all_words = set()
    
    # Map for translations from conversations
    conv_translations = {}

    for conv in conversations:
        for msg in conv.get("messages", []):
            it_text = msg["text"].strip()
            all_sentences.add(it_text)
            if msg.get("english"):
                conv_translations[it_text] = msg["english"]
            
            all_words.update(tokenize(it_text))
            
            for choice in msg.get("choices", []):
                it_choice = choice["text"].strip()
                if choice.get("isCorrect"):
                    all_phrases.add(it_choice)
                    if choice.get("english"):
                        conv_translations[it_choice] = choice["english"]
                all_words.update(tokenize(it_choice))

    # Master translation map for vocabulary
    vocab_translations = {
        "abbiamo": "we have",
        "adulti": "adults",
        "aiutarla": "to help you",
        "allora": "then",
        "altre": "other (feminine plural)",
        "altri": "others / other (masculine plural)",
        "altro": "other / else",
        "anche": "also / too",
        "ancora": "again / still",
        "antibiotici": "antibiotics",
        "antibiotico": "antibiotic",
        "antinfiammatori": "anti-inflammatories",
        "arrivederci": "goodbye",
        "assumerlo": "to take it",
        "avete": "you have (plural)",
        "bambini": "children",
        "bambino": "child",
        "barre": "bars (as in barcode)",
        "bene": "well / fine",
        "buona": "good (feminine)",
        "buongiorno": "good morning",
        "capisco": "I understand",
        "capito": "understood",
        "carta": "card / paper",
        "causare": "to cause",
        "cena": "dinner",
        "centesimi": "cents",
        "certamente": "certainly",
        "che": "that / which",
        "chiaro": "clear",
        "chiesto": "asked",
        "cinquanta": "fifty",
        "cinque": "five",
        "codice": "code",
        "colazione": "breakfast",
        "collaterali": "side (as in side effects)",
        "come": "how",
        "comprare": "to buy",
        "compresse": "tablets / pills",
        "comunque": "anyway / however",
        "con": "with",
        "consiglio": "advice / tip",
        "consultare": "to consult",
        "contanti": "cash",
        "continuare": "to continue",
        "controindicazioni": "contraindications",
        "cosa": "what / thing",
        "costa": "it costs",
        "cura": "treatment / care",
        "darlo": "to give it",
        "dell": "of the",
        "desidera": "you desire / would you like",
        "deve": "he/she/you must",
        "devo": "I must",
        "dieci": "ten",
        "dimentico": "I forget",
        "dodici": "twelve",
        "dopo": "after",
        "dose": "dose",
        "dubbi": "doubts",
        "due": "two",
        "ecco": "here is / here are",
        "effetti": "effects",
        "elettronica": "electronic",
        "esatto": "exact / exactly",
        "euro": "euro",
        "evitare": "to avoid",
        "fare": "to do / to make",
        "farmaci": "drugs / medicines",
        "farmaco": "drug / medication",
        "farò": "I will do",
        "fatto": "done",
        "finire": "to finish",
        "foglietto": "leaflet",
        "giornata": "day / daytime",
        "giorni": "days",
        "giorno": "day",
        "gli": "the / to him",
        "grazie": "thank you",
        "guidare": "to drive",
        "ibuprofene": "ibuprofen",
        "illustrativo": "illustrative / package (leaflet)",
        "importanti": "important",
        "informazione": "information",
        "inserire": "to insert",
        "insieme": "together",
        "legga": "read (imperative/subjunctive)",
        "lei": "she / you (formal)",
        "mal": "ache / bad",
        "male": "bad / poorly",
        "medica": "medical",
        "medico": "doctor",
        "meglio": "better",
        "meno": "less",
        "mille": "thousand",
        "mio": "my",
        "molto": "very / much",
        "mostri": "show (imperative/subjunctive)",
        "non": "not",
        "numero": "number",
        "obbligatoria": "mandatory",
        "ogni": "every / each",
        "ora": "now / hour",
        "ore": "hours",
        "otto": "eight",
        "paga": "pays / pay",
        "pago": "I pay",
        "pasti": "meals",
        "per": "for / by",
        "perfetto": "perfect",
        "posso": "I can",
        "pranzo": "lunch",
        "preferibilmente": "preferably",
        "prego": "you're welcome / please",
        "prenda": "take (imperative/subjunctive)",
        "prendere": "to take",
        "prenderle": "to take them",
        "prenderlo": "to take it",
        "prenderne": "to take some",
        "prescritto": "prescribed",
        "proprio": "really / own",
        "prossima": "next",
        "pure": "also / too",
        "può": "can / he/she/it can",
        "qualcosa": "something",
        "quante": "how many (feminine)",
        "quanti": "how many (masculine)",
        "quanto": "how much",
        "quaranta": "forty",
        "queste": "these (feminine)",
        "questo": "this",
        "qui": "here",
        "quindi": "so / therefore",
        "regolarmente": "regularly",
        "ricetta": "prescription / recipe",
        "salve": "hello",
        "sapevo": "I knew",
        "scatola": "box",
        "scatole": "boxes",
        "sciroppo": "syrup",
        "seguirò": "I will follow",
        "sente": "feels",
        "serve": "it serves / it is needed",
        "sicuramente": "surely / definitely",
        "sicuro": "sure / safe",
        "soldi": "money",
        "solo": "only / alone",
        "sonnolenza": "drowsiness",
        "sono": "I am / they are",
        "specifica": "specific (feminine)",
        "specifico": "specific (masculine)",
        "stanco": "tired",
        "stomaco": "stomach",
        "sul": "on the",
        "telefono": "phone",
        "testa": "head",
        "tipo": "type",
        "totale": "total",
        "tre": "three",
        "tutta": "all / whole (feminine)",
        "tutto": "all / whole (masculine) / everything",
        "una": "a / an / one",
        "usare": "to use",
        "venti": "twenty",
        "versione": "version",
        "volte": "times",
        "vorrei": "I would like",
        "vuoto": "empty",
        # New words from extension
        "alcolici": "alcoholic drinks",
        "asciutto": "dry",
        "aereo": "plane / airplane",
        "bagaglio": "luggage",
        "conservare": "to keep / to store",
        "confezione": "package / box",
        "cibi": "foods",
        "dosi": "doses",
        "farmacia": "pharmacy",
        "fondo": "bottom",
        "frigorifero": "refrigerator",
        "luce": "light",
        "lontan": "far", # lontano was already there, check tokenizer
        "lontano": "far",
        "necessario": "necessary",
        "pazienza": "patience",
        "problemi": "problems",
        "scade": "it expires",
        "scadenza": "expiration",
        "spiegazioni": "explanations",
        "trasporto": "transport / transportation",
        "viaggio": "trip / travel",
        "guarigione": "recovery / healing",
        "figurati": "don't mention it / you're welcome",
        "appena": "as soon as",
        "ricorda": "remembers / remember",
        "salto": "jump / miss (as in skip a dose)",
        "succede": "happens",
        "dettagli": "details",
        "tornare": "to return / to come back",
        "fondo": "bottom",
        "accordo": "agreement / ok",
        "all": "to the / at the",
        "anni": "years",
        "anno": "year",
        "aumentare": "to increase",
        "avere": "to have",
        "basta": "enough / is enough",
        "bella": "beautiful",
        "bere": "to drink",
        "bicchiere": "glass",
        "biglietto": "ticket",
        "borsa": "bag / purse",
        "buon": "good",
        "caffè": "coffee",
        "calma": "calm",
        "camera": "room",
        "cane": "dog",
        "cappello": "hat",
        "chiave": "key",
        "chilo": "kilogram",
        "chiude": "closes",
        "cinema": "cinema",
        "città": "city",
        "colore": "color",
        "colori": "colors",
        "comprarla": "to buy it",
        "compro": "I buy",
        "consigliate": "recommended",
        "controlli": "check (imperative/subjunctive)",
        "correre": "to run",
        "credito": "credit",
        "cucinare": "to cook",
        "cuore": "heart",
        "dalla": "from the",
        "data": "date",
        "della": "of the",
        "delle": "of the / some",
        "domande": "questions",
        "domani": "tomorrow",
        "dormire": "to sleep",
        "dormito": "slept",
        "dove": "where",
        "eviti": "avoid (imperative/subjunctive)",
        "fame": "hunger",
        "fiori": "flowers",
        "forchetta": "fork",
        "fumetti": "comics",
        "gatto": "cat",
        "gelato": "ice cream",
        "giornale": "newspaper",
        "grande": "big / large",
        "gusto": "taste",
        "hotel": "hotel",
        "idea": "idea",
        "latte": "milk",
        "leggere": "to read",
        "libri": "books",
        "limone": "lemon",
        "luogo": "place",
        "macchina": "car",
        "mangiare": "to eat",
        "margherita": "daisy / margherita (pizza)",
        "mattine": "mornings",
        "mele": "apples",
        "mese": "month",
        "metto": "I put",
        "minuti": "minutes",
        "molti": "many",
        "museo": "museum",
        "musica": "music",
        "negozio": "shop",
        "nel": "in the",
        "nera": "black",
        "nome": "name",
        "nuotare": "to run", # wait, nuotare is to swim
        "nuotata": "swim",
        "nuovo": "new",
        "ombrello": "umbrella",
        "ordinare": "to order",
        "ottima": "excellent",
        "pagato": "paid",
        "pane": "bread",
        "parcheggiare": "to park",
        "passa": "passes",
        "pasta": "pasta",
        "penna": "pen",
        "perché": "because / why",
        "persone": "people",
        "piace": "like / pleases",
        "pizza": "pizza",
        "portarle": "to bring them",
        "possono": "they can",
        "postino": "postman",
        "preferito": "favorite",
        "prendo": "I take",
        "preoccupi": "worry (subjunctive/imperative)",
        "presto": "soon / early",
        "prima": "before / first",
        "problema": "problem",
        "qual": "which / what",
        "quando": "when",
        "questa": "this",
        "questi": "these",
        "restare": "to stay",
        "ritardo": "delay",
        "roma": "Rome",
        "scarpe": "shoes",
        "sconto": "discount",
        "scritta": "written",
        "scuro": "dark",
        "semplice": "simple",
        "sempre": "always",
        "senta": "feel (imperative/subjunctive)",
        "siamo": "we are",
        "spero": "I hope",
        "stazione": "station",
        "strada": "road / street",
        "subito": "immediately",
        "sulla": "on the",
        "suo": "his / her / its / your (formal)",
        "superi": "exceed (imperative/subjunctive)",
        "tavolo": "table",
        "torta": "cake",
        "tra": "between / among",
        "trova": "finds / is located",
        "trovare": "to find",
        "tutte": "all",
        "tutti": "all / everyone",
        "uno": "one / a",
        "uso": "use",
        "vado": "I go",
        "verdura": "vegetables",
        "vero": "true / right",
        "vestiti": "clothes",
        "visitare": "to visit",
        "visto": "seen",
        "voglio": "I want",
        "zaino": "backpack",
        "nuotare": "to swim"
    }

    def process_file(filename, items_set, translations, id_prefix):
        p = os.path.join(base_path, filename)
        existing_items = {}
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                for item in json.load(f):
                    existing_items[item["italian"]] = item
        
        new_list = []
        # Sort to keep IDs deterministic if we create new ones
        sorted_items = sorted(list(items_set))
        
        for i, it in enumerate(sorted_items):
            if it in existing_items:
                item = existing_items[it]
                # Update English if missing
                if not item.get("english") or item["english"] == "":
                    item["english"] = translations.get(it, "")
                new_list.append(item)
            else:
                # Create new item
                new_item = {
                    "id": f"{id_prefix}{len(existing_items) + i + 1}", # This is not great for stable IDs but okay for now
                    "italian": it,
                    "english": translations.get(it, ""),
                    "audio": {"italian": f"/audio/{it.replace(' ', '_')}.opus"} # Placeholder, will be fixed by audio specialist/audit
                }
                new_list.append(new_item)
        
        # Ensure 100% coverage - fill any remaining empty english
        for item in new_list:
            if not item.get("english"):
                item["english"] = translations.get(item["italian"], "MISSING")
                if item["english"] == "MISSING":
                    print(f"Warning: Still missing translation for '{item['italian']}'")
        
        with open(p, "w", encoding="utf-8") as f:
            json.dump(new_list, f, indent=2, ensure_ascii=False)
        return len(new_list)

    v_count = process_file(f"{prefix}_vocabulary.json", all_words, vocab_translations, "v")
    p_count = process_file(f"{prefix}_phrases.json", all_phrases, conv_translations, "p")
    s_count = process_file(f"{prefix}_sentences.json", all_sentences, conv_translations, "s")
    
    print(f"Updated {v_count} words, {p_count} phrases, {s_count} sentences.")

if __name__ == "__main__":
    main()
