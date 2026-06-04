import json
import re
import os
import random

scenario_path = '/home/waseageru/parli-italiano/src/data/exports/workstudy/asking_for_clarification'
conv_file = os.path.join(scenario_path, 'conversations.json')

with open(conv_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

vocab_set = set()
phrases_map = {
    "Scusa": "Sorry",
    "Scusi": "Excuse me (formal)",
    "Per favore": "Please",
    "Non ho capito": "I didn't understand",
    "Può ripetere?": "Can you repeat? (formal)",
    "Puoi ripetere?": "Can you repeat? (informal)",
    "Che cosa significa?": "What does it mean?",
    "Grazie mille": "Thank you very much",
    "Adesso è chiaro": "Now it's clear",
    "Nessun problema": "No problem",
    "Prego": "You're welcome",
    "Va bene": "Alright / Okay",
    "Capito!": "Understood!",
    "Grazie per la spiegazione": "Thank you for the explanation",
    "Più lentamente": "More slowly",
    "Più piano": "More slowly / More quietly",
    "Cosa intendi per": "What do you mean by",
    "Puoi spiegare la parola?": "Can you explain the word?",
    "Può parlare più piano?": "Can you speak more slowly? (formal)",
    "Può ripetere?": "Can you repeat? (formal)",
    "Può spiegare meglio": "Can you explain better (formal)",
    "Grazie per la pazienza": "Thank you for the patience",
    "A più tardi": "See you later",
    "A domani": "See you tomorrow",
    "Entro le diciassette": "By 5 PM",
    "Tutto chiaro": "All clear",
    "Grazie ancora": "Thanks again"
}

vocab_map = {
    "chiarimento": "clarification", "ripetere": "to repeat", "capire": "to understand",
    "spiegare": "to explain", "lento": "slow", "piano": "slowly / quietly",
    "parola": "word", "significato": "meaning", "dubbio": "doubt",
    "domanda": "question", "cortesia": "courtesy / kindness",
    "scadenza": "deadline", "ricerca": "research", "budget": "budget",
    "stampati": "printed", "documenti": "documents", "ufficio": "office",
    "riunione": "meeting", "domani": "tomorrow", "ora": "time",
    "dieci": "ten", "nove": "nine", "mattina": "morning",
    "file": "file", "preparare": "to prepare", "finito": "finished",
    "inviare": "to send", "lunedì": "Monday", "martedì": "Tuesday",
    "veloce": "fast", "lentamente": "slowly", "spiegazione": "explanation",
    "chiaro": "clear", "precisamente": "precisely", "esempio": "example",
    "aiuto": "help", "pazienza": "patience", "lavoro": "work",
    "progetto": "project", "nuovo": "new", "parlare": "to speak",
    "dire": "to say", "ascoltare": "to listen", "scrivere": "to write",
    "nomi": "names", "clienti": "clients", "prezzi": "prices",
    "internet": "internet", "informazioni": "information", "cercare": "to look for",
    "iniziare": "to start", "pronto": "ready", "sicuramente": "certainly",
    "programma": "program", "software": "software", "chiamate": "calls",
    "video": "video", "link": "link", "email": "email", "indirizzo": "address",
    "azienda": "company", "colleghi": "colleagues", "capo": "boss",
    "direttore": "director", "pomeridiana": "afternoon (adj)", "urgente": "urgent",
    "diciassette": "seventeen / 5 PM", "presentazione": "presentation",
    "immagini": "images", "testo": "text", "mostrare": "to show",
    "sala": "room / hall", "conferenze": "conferences", "stanza": "room",
    "rallentare": "to slow down", "pomeriggio": "afternoon"
}

sentences = []
seen_sentences = set()

def clean_word(w):
    return re.sub(r'[^\w\s]', '', w).lower().strip()

# Extract from conversations
for conv in data['conversations']:
    for msg in conv['messages']:
        # Host sentence
        if msg['text'] not in seen_sentences:
            sentences.append({
                "italian": msg['text'],
                "english": msg['english']
            })
            seen_sentences.add(msg['text'])
        
        # Correct choice sentence
        correct_choice = next(c for c in msg['choices'] if c['isCorrect'])
        if correct_choice['text'] not in seen_sentences:
            sentences.append({
                "italian": correct_choice['text'],
                "english": "" 
            })
            seen_sentences.add(correct_choice['text'])

        # Words
        for word in msg['text'].split():
            cw = clean_word(word)
            if cw and len(cw) > 1 and not cw.isdigit():
                vocab_set.add(cw)
        
        for word in correct_choice['text'].split():
            cw = clean_word(word)
            if cw and len(cw) > 1 and not cw.isdigit():
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
        "id": f"v{i+1}",
        "italian": v,
        "english": vocab_map.get(v, ""),
        "choicesItalian": choices
    })

# Create phrases.json
found_phrases = []
all_text = " ".join(seen_sentences)
for it, en in phrases_map.items():
    if it.lower() in all_text.lower():
        found_phrases.append({"italian": it, "english": en})

phrases_output = []
for i, p in enumerate(found_phrases):
    phrases_output.append({
        "id": f"p{i+1}",
        "italian": p['italian'],
        "english": p['english']
    })

# Create sentences.json
sentences_output = []
for i, s in enumerate(sentences):
    sentences_output.append({
        "id": f"s{i+1}",
        "italian": s['italian'],
        "english": s['english']
    })

base_name = "workstudy_asking_for_clarification"

with open(os.path.join(scenario_path, f'{base_name}_vocabulary.json'), 'w', encoding='utf-8') as f:
    json.dump(vocab_output, f, indent=2, ensure_ascii=False)

with open(os.path.join(scenario_path, f'{base_name}_phrases.json'), 'w', encoding='utf-8') as f:
    json.dump(phrases_output, f, indent=2, ensure_ascii=False)

with open(os.path.join(scenario_path, f'{base_name}_sentences.json'), 'w', encoding='utf-8') as f:
    json.dump(sentences_output, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(vocab_output)} words, {len(phrases_output)} phrases, {len(sentences_output)} sentences.")
