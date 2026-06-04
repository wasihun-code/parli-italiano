import json
import os
import re
import random

scenario_path = 'src/data/exports/daily_life/household_repair'
conv_file = os.path.join(scenario_path, 'conversations.json')

with open(conv_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

sentences = []
seen_sentences = set()
vocab_set = set()

def clean_word(w):
    w = w.lower()
    w = re.sub(r'[^\w\s]', '', w)
    return w.strip()

# Common phrases to look for in the text
common_phrases = [
    ("Buongiorno", "Good morning"),
    ("Pronto", "Hello (on the phone)"),
    ("Come posso aiutarla?", "How can I help you?"),
    ("Grazie mille", "Thank you very much"),
    ("Per favore", "Please"),
    ("Va bene", "Alright / Okay"),
    ("Arrivederci", "Goodbye"),
    ("A dopo", "See you later"),
    ("D'accordo", "Agreed"),
    ("A domani", "See you tomorrow"),
    ("Buona giornata", "Have a good day"),
    ("Ottimo lavoro", "Great job"),
    ("Nessun problema", "No problem"),
    ("Ecco a lei", "Here you go")
]

all_extracted_text = ""

for conv in data['conversations']:
    for msg in conv['messages']:
        # Host text
        if msg['text'] not in seen_sentences:
            sentences.append({"italian": msg['text'], "english": msg['english']})
            seen_sentences.add(msg['text'])
            all_extracted_text += " " + msg['text']
        
        # User choices (only correct ones)
        for choice in msg['choices']:
            if choice['isCorrect']:
                if choice['text'] not in seen_sentences:
                    sentences.append({"italian": choice['text'], "english": choice['english']})
                    seen_sentences.add(choice['text'])
                    all_extracted_text += " " + choice['text']

# Extract vocabulary from all sentences
words = all_extracted_text.split()
for w in words:
    cw = clean_word(w)
    if cw and len(cw) > 1 and not cw.isdigit():
        vocab_set.add(cw)

sorted_vocab = sorted(list(vocab_set))

# Basic vocabulary mapping for this domain
vocab_map = {
    "rubinetto": "faucet", "cucina": "kitchen", "problema": "problem", "perde": "leaks",
    "acqua": "water", "gocce": "drops", "urgente": "urgent", "terra": "floor",
    "chiudere": "to close", "valvola": "valve", "sicurezza": "safety", "indirizzo": "address",
    "roma": "Rome", "piano": "floor", "vecchio": "old", "dieci": "ten",
    "parcheggio": "parking", "furgone": "van", "palazzo": "building", "mezz'ora": "half an hour",
    "casa": "home", "novità": "news", "costo": "cost", "uscita": "call-out",
    "trenta": "thirty", "lavoro": "work", "interruttore": "switch", "funziona": "works",
    "luce": "light", "stanza": "room", "bagno": "bathroom", "specchio": "mirror",
    "tasto": "button", "lampadina": "light bulb", "tecnico": "technician", "domani": "tomorrow",
    "nove": "nine", "marco": "Marco", "cellulare": "cell phone", "urgenze": "emergencies",
    "fili": "wires", "elettrici": "electrical", "pericoloso": "dangerous", "quadro": "panel",
    "elettrico": "electrical", "generale": "general", "posto": "place", "scattato": "tripped",
    "salvavita": "circuit breaker", "altrove": "elsewhere", "cortocircuito": "short circuit",
    "paura": "fear", "apparecchi": "appliances", "soggiorno": "living room", "televisione": "television",
    "lampada": "lamp", "stufa": "heater", "stacco": "unplug", "presa": "outlet",
    "corrente": "current", "consiglio": "advice", "verdi": "Verdi", "confermo": "I confirm",
    "riparazione": "repair", "guasto": "fault", "tubo": "pipe", "rotto": "broken",
    "cambiarlo": "to change it", "tempo": "time", "pezzi": "pieces", "ricambio": "spare",
    "spostare": "to move", "venti": "twenty", "bicchiere": "glass", "apro": "I open",
    "cautela": "caution", "contento": "happy", "cinquanta": "fifty", "euro": "euro",
    "carta": "card", "ricevuta": "receipt", "email": "email", "finito": "finished",
    "pronto": "hello / ready", "idraulica": "plumbing", "elettricista": "electrician",
    "amministratore": "manager", "aiutarla": "to help you", "rossi": "Rossi", "bianchi": "Bianchi",
    "buongiorno": "good morning", "arrivederci": "goodbye"
}

# Create vocabulary.json
vocab_output = []
for i, v in enumerate(sorted_vocab):
    # For distractors, use other words from the vocab set
    others = [w for w in sorted_vocab if w != v]
    distractors = random.sample(others, min(len(others), 3))
    choices = distractors + [v]
    random.shuffle(choices)
    
    vocab_output.append({
        "id": f"v{i+1}",
        "italian": v,
        "english": vocab_map.get(v, ""),
        "choicesItalian": choices
    })

# Create phrases.json
phrases_output = []
p_count = 1
for it, en in common_phrases:
    if it.lower() in all_extracted_text.lower():
        phrases_output.append({
            "id": f"p{p_count}",
            "italian": it,
            "english": en
        })
        p_count += 1

# Create sentences.json
sentences_output = []
for i, s in enumerate(sentences):
    sentences_output.append({
        "id": f"s{i+1}",
        "italian": s['italian'],
        "english": s['english']
    })

# Save files
with open(os.path.join(scenario_path, 'daily_life_household_repair_vocabulary.json'), 'w', encoding='utf-8') as f:
    json.dump(vocab_output, f, indent=2, ensure_ascii=False)

with open(os.path.join(scenario_path, 'daily_life_household_repair_phrases.json'), 'w', encoding='utf-8') as f:
    json.dump(phrases_output, f, indent=2, ensure_ascii=False)

with open(os.path.join(scenario_path, 'daily_life_household_repair_sentences.json'), 'w', encoding='utf-8') as f:
    json.dump(sentences_output, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(vocab_output)} words, {len(phrases_output)} phrases, {len(sentences_output)} sentences.")
