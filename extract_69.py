import json
import os
import re
import random

scenario_id = 69
scenario_path = 'src/workstudy/printing_documents'
conv_file = os.path.join(scenario_path, 'conversations.json')

with open(conv_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

sentences_list = []
seen_sentences = set()
vocab_set = set()

def clean_word(w):
    w = w.lower()
    w = re.sub(r'[^\w\s]', '', w)
    return w.strip()

# Dictionary for translations
vocab_map = {
    "stampante": "printer", "stampare": "to print", "fotocopia": "photocopy",
    "colore": "color", "bianco": "white", "nero": "black", "fronte": "front",
    "retro": "back", "carta": "paper", "foglio": "sheet", "formato": "format",
    "prezzo": "price", "documento": "document", "file": "file", "chiavetta": "USB stick",
    "usb": "USB", "stampa": "print", "pagine": "pages", "numero": "number",
    "copie": "copies", "quante": "how many", "a4": "A4", "a3": "A3",
    "costo": "cost", "pagare": "to pay", "euro": "euro", "centesimi": "cents",
    "pronto": "ready", "attesa": "waiting", "momento": "moment", "favore": "favor",
    "grazie": "thanks", "buongiorno": "good morning", "salve": "hello",
    "aiuto": "help", "bisogno": "need", "posso": "I can", "vuole": "wants",
    "desidera": "desires", "scelta": "choice", "opzione": "option",
    "singolo": "single", "doppio": "double", "poster": "poster", "pesante": "heavy",
    "vivaci": "vivid", "cartella": "folder", "finire": "to finish",
    "bellissimi": "very beautiful", "totale": "total", "dieci": "ten",
    "risparmiamo": "we save", "riciclata": "recycled", "pinzare": "to staple",
    "pinzate": "stapled", "immagini": "images", "scritte": "writings",
    "tabelle": "tables", "siedo": "I sit", "ricevuta": "receipt",
    "contratto": "contract", "pdf": "PDF", "alto": "high", "venti": "twenty",
    "sessanta": "sixty", "accetta": "accepts", "bancomat": "ATM card",
    "riuscito": "successful", "solo": "only", "questo": "this", "fogli": "sheets",
    "cinque": "five", "dieci": "ten", "tre": "three", "due": "two", "pago": "I pay"
}

common_phrases = [
    ("Buongiorno", "Good morning"),
    ("Per favore", "Please"),
    ("Grazie mille", "Thank you very much"),
    ("Va bene", "Alright"),
    ("Arrivederci", "Goodbye"),
    ("Buona giornata", "Have a good day"),
    ("Fronte retro", "Double-sided"),
    ("Bianco e nero", "Black and white"),
    ("A colori", "In color"),
    ("Ecco a lei", "Here you go")
]

all_extracted_text = ""

for conv in data['conversations']:
    for msg in conv['messages']:
        # Host text
        if msg['text'] not in seen_sentences:
            sentences_list.append({"italian": msg['text'], "english": msg['english']})
            seen_sentences.add(msg['text'])
            all_extracted_text += " " + msg['text']
        
        # User choices (only correct ones)
        for choice in msg['choices']:
            if choice['isCorrect']:
                if choice['text'] not in seen_sentences:
                    sentences_list.append({"italian": choice['text'], "english": choice['english']})
                    seen_sentences.add(choice['text'])
                    all_extracted_text += " " + choice['text']

# Extract vocabulary
words = all_extracted_text.split()
for w in words:
    cw = clean_word(w)
    if cw and len(cw) > 1 and not cw.isdigit() and cw in vocab_map:
        vocab_set.add(cw)

sorted_vocab = sorted(list(vocab_set))

# Create vocabulary.json
vocab_output = []
for i, v in enumerate(sorted_vocab):
    others = [w for w in sorted_vocab if w != v]
    distractors = random.sample(others, min(len(others), 3))
    choices = distractors + [v]
    random.shuffle(choices)
    
    vocab_output.append({
        "id": f"s{scenario_id}-v{i+1}",
        "italian": v,
        "english": vocab_map.get(v, v),
        "choicesItalian": choices,
        "type": "vocabulary",
        "feedback": {
            "correctItalian": "Esatto!",
            "incorrectItalian": f"No, è '{v}'.",
            "correctEnglish": "Great!",
            "incorrectEnglish": f"No, it is '{v}'."
        }
    })

# Create phrases.json
phrases_output = []
p_count = 1
for it, en in common_phrases:
    if it.lower() in all_extracted_text.lower():
        phrases_output.append({
            "id": f"s{scenario_id}-p{p_count}",
            "italian": it,
            "english": en,
            "type": "phrase"
        })
        p_count += 1

# Create sentences.json
sentences_output = []
for i, s in enumerate(sentences_list):
    sentences_output.append({
        "id": f"s{scenario_id}-s{i+1}",
        "italian": s['italian'],
        "english": s['english'],
        "type": "sentence"
    })

# Save files
with open(os.path.join(scenario_path, 'vocabulary.json'), 'w', encoding='utf-8') as f:
    json.dump(vocab_output, f, indent=2, ensure_ascii=False)

with open(os.path.join(scenario_path, 'phrases.json'), 'w', encoding='utf-8') as f:
    json.dump(phrases_output, f, indent=2, ensure_ascii=False)

with open(os.path.join(scenario_path, 'sentences.json'), 'w', encoding='utf-8') as f:
    json.dump(sentences_output, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(vocab_output)} words, {len(phrases_output)} phrases, {len(sentences_output)} sentences.")
