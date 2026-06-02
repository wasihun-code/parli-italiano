import json
import os

base_path = 'src/data/exports/culture/festival/'
prefix = 'culture_festival'

files = [
    f"{prefix}_vocabulary.json",
    f"{prefix}_phrases.json",
    f"{prefix}_sentences.json"
]

# Common word translations for vocabulary
word_translations = {
    "abbiamo": "we have",
    "accettiamo": "we accept",
    "aiuto": "help",
    "alla": "at the / to the",
    "alle": "at (time) / to the",
    "allora": "then",
    "altro": "other / else",
    "anche": "also",
    "ancora": "again / still",
    "andare": "to go",
    "angolo": "corner",
    "anno": "year",
    "antichi": "ancient (plural)",
    "antico": "ancient (singular)",
    "appetito": "appetite",
    "arrivederci": "goodbye",
    "artificio": "artifice / (fire)work",
    "artigianato": "crafts",
    "aspetti": "wait",
    "assaggiare": "to taste",
    "atmosfera": "atmosphere",
    "avete": "you have (plural)",
    "bancarelle": "stalls",
    "bella": "beautiful (feminine)",
    "belle": "beautiful (feminine plural)",
    "bellissima": "very beautiful (feminine)",
    "bellissime": "very beautiful (feminine plural)",
    "bellissimi": "very beautiful (masculine plural)",
    "bello": "beautiful (masculine)",
    "bene": "well",
    "benvenuti": "welcome",
    "bere": "to drink",
    "bicchiere": "glass",
    "biglietto": "ticket",
    "bisogna": "it is necessary",
    "borgo": "village / hamlet",
    "buon": "good",
    "buona": "good (feminine)",
    "buonasera": "good evening",
    "buongiorno": "good morning",
    "buono": "good",
    "carini": "cute",
    "carta": "card / paper",
    "carte": "cards",
    "cavalli": "horses",
    "cento": "hundred",
    "ceramiche": "ceramics",
    "cerca": "looks for",
    "cerco": "I am looking for",
    "certamente": "certainly",
    "certo": "sure",
    "che": "what / that",
    "chiesa": "church",
    "colline": "hills",
    "comprato": "bought",
    "con": "with",
    "confezione": "packaging / gift wrap",
    "consiglia": "recommends",
    "consiglio": "advice / I recommend",
    "corteo": "procession / parade",
    "cosa": "what / thing",
    "costa": "costs",
    "costume": "costume",
    "costumi": "costumes",
    "cultura": "culture",
    "cura": "care",
    "dall": "from the",
    "dalle": "from the",
    "dato": "given",
    "davvero": "really",
    "dei": "of the / some",
    "del": "of the",
    "deliziosa": "delicious (feminine)",
    "delizioso": "delicious (masculine)",
    "dell": "of the",
    "della": "of the",
    "delle": "of the",
    "dieci": "ten",
    "dietro": "behind",
    "dipinte": "painted (feminine plural)",
    "dipinti": "painted (masculine plural)",
    "diverso": "different",
    "divertimento": "fun",
    "donne": "women",
    "dopo": "after",
    "dove": "where",
    "dovrebbe": "should",
    "ecco": "here is / here are",
    "eccola": "here it is (feminine)",
    "esattamente": "exactly",
    "euro": "euro",
    "evento": "event",
    "faccia": "makes (subjunctive) / face",
    "fantastico": "fantastic",
    "fare": "to do / to make",
    "fatti": "made (masculine plural)",
    "fatto": "made (masculine singular)",
    "favore": "favor",
    "festa": "festival / party",
    "figuranti": "participants / extras",
    "fondo": "end / bottom",
    "foto": "photo / photos",
    "fotografica": "photographic",
    "fresco": "fresh",
    "fuochi": "fires / fireworks",
    "gente": "people",
    "gentile": "kind",
    "giornata": "day",
    "giro": "walk / turn",
    "già": "already",
    "gratuita": "free",
    "grazie": "thanks",
    "idea": "idea",
    "importante": "important",
    "incarto": "wrap",
    "include": "includes",
    "incredibile": "incredible",
    "informazioni": "information",
    "ingresso": "entrance",
    "inizia": "starts",
    "iniziano": "start (plural)",
    "interessa": "interests",
    "leggeri": "light (plural)",
    "lei": "you (formal) / her",
    "liberi": "free / vacant",
    "locale": "local",
    "lungo": "along / long",
    "macchina": "machine / car",
    "magnete": "magnet",
    "magneti": "magnets",
    "mano": "hand",
    "mappa": "map",
    "meravigliosa": "wonderful (feminine)",
    "meraviglioso": "wonderful (masculine)",
    "mezzanotte": "midnight",
    "mille": "thousand",
    "molta": "a lot of (feminine)",
    "molti": "many",
    "molto": "very / much",
    "mostra": "shows / exhibition",
    "musica": "music",
    "non": "not",
    "nostra": "our (feminine)",
    "nostre": "our (feminine plural)",
    "nostro": "our (masculine)",
    "notizia": "news",
    "nove": "nine",
    "ogni": "every",
    "ora": "hour / now",
    "ottima": "excellent (feminine)",
    "ottimo": "excellent (masculine)",
    "paese": "village / country",
    "pagare": "to pay",
    "palco": "stage",
    "pane": "bread",
    "parte": "starts / part",
    "passa": "passes",
    "passi": "spend / pass",
    "pasta": "pasta",
    "per": "for",
    "perfetto": "perfect",
    "persone": "people",
    "pezzo": "piece",
    "piaccia": "likes (subjunctive)",
    "piacciono": "like (plural)",
    "piace": "likes",
    "piatto": "plate / dish",
    "piazza": "square",
    "piccoli": "small (plural)",
    "piccolo": "small (singular)",
    "più": "more",
    "poco": "little",
    "portare": "to bring / to carry",
    "posso": "I can",
    "potete": "you can (plural)",
    "prego": "you're welcome / please",
    "prendo": "I take",
    "presto": "early / soon",
    "prezzo": "price",
    "prima": "before / first",
    "principale": "main",
    "proprio": "really / own",
    "punto": "point / o'clock sharp",
    "qual": "which",
    "qualcosa": "something",
    "quanto": "how much",
    "quest": "this",
    "queste": "these (feminine)",
    "questo": "this (masculine)",
    "quindici": "fifteen",
    "rappresenta": "represents",
    "regalo": "gift",
    "ricordo": "souvenir / memory",
    "rosso": "red",
    "rumorosa": "loud / noisy",
    "sagra": "local festival / fair",
    "sapere": "to know",
    "sarà": "it will be",
    "sbandieratori": "flag-wavers",
    "scoprire": "to discover",
    "scusi": "excuse me",
    "sedermi": "to sit down",
    "sembra": "seems",
    "serata": "evening",
    "serve": "needs",
    "sfilata": "parade",
    "sicuramente": "surely",
    "solo": "only",
    "sono": "they are / I am",
    "speciale": "special",
    "specialità": "specialty",
    "spero": "I hope",
    "spettacolo": "show",
    "splendide": "splendid",
    "stand": "stall / stand",
    "stasera": "tonight",
    "storica": "historical",
    "strada": "street",
    "sua": "your (formal) / his / her",
    "subito": "immediately",
    "tardi": "late",
    "tartufo": "truffle",
    "tavoli": "tables",
    "totalmente": "totally",
    "tovagliolo": "napkin",
    "tra": "between / among / in",
    "tradizione": "tradition",
    "tradizioni": "traditions",
    "tratta": "deals with",
    "tre": "three",
    "trova": "finds",
    "tutte": "all (feminine plural)",
    "tutti": "all (masculine plural)",
    "tutto": "everything / all",
    "una": "a / an",
    "unico": "unique",
    "uno": "one / a",
    "utile": "useful",
    "vado": "I go",
    "valigia": "suitcase",
    "vaso": "vase",
    "vedere": "to see",
    "vederli": "to see them",
    "vediamo": "we see",
    "vedo": "I see",
    "vero": "true",
    "vicino": "near",
    "vino": "wine",
    "visione": "vision / viewing",
    "visita": "visit"
}

# Phrases and Sentences translations will be pulled from conversations.json if possible
# but we already have them in the files since linguistic_extractor uses them.
# Let's check for remaining empty ones.

for filename in files:
    path = os.path.join(base_path, filename)
    if not os.path.exists(path):
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        items = json.load(f)
        
    updated = False
    for item in items:
        if not item.get("english"):
            if "vocabulary" in filename:
                if item["italian"] in word_translations:
                    item["english"] = word_translations[item["italian"]]
                    updated = True
            # For phrases and sentences, if they are still empty, they might be distractors
            # or from host lines that we missed.
            # But the user said "Fill ALL missing translations".
            
    if updated:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
        print(f"Updated translations in {filename}")

# One more pass for phrases and sentences using conversations.json directly
with open(os.path.join(base_path, 'conversations.json'), 'r', encoding='utf-8') as f:
    conv_data = json.load(f)

conv_translations = {}
for conv in conv_data['conversations']:
    for msg in conv['messages']:
        conv_translations[msg['text'].strip()] = msg['english'].strip()
        for choice in msg['choices']:
            conv_translations[choice['text'].strip()] = choice['english'].strip()

for filename in [f"{prefix}_phrases.json", f"{prefix}_sentences.json"]:
    path = os.path.join(base_path, filename)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        items = json.load(f)
    updated = False
    for item in items:
        if not item.get("english"):
            it = item["italian"].strip()
            if it in conv_translations:
                item["english"] = conv_translations[it]
                updated = True
    if updated:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
        print(f"Updated phrases/sentences in {filename}")
