import json
import re

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text.lower())

with open('src/data/exports/shopping/electronics_store/conversations.json', 'r', encoding='utf-8') as f:
    conv_data = json.load(f)

sentences = []
for conv in conv_data['conversations']:
    for msg in conv['messages']:
        # Host sentence
        sentences.append({
            'italian': msg['text'],
            'english': msg['english']
        })
        # Correct choice sentence
        for choice in msg['choices']:
            if choice['isCorrect']:
                sentences.append({
                    'italian': choice['text'],
                    'english': choice['english']
                })

# Unique sentences
unique_sentences = []
seen_it = set()
for s in sentences:
    if s['italian'] not in seen_it:
        unique_sentences.append(s)
        seen_it.add(s['italian'])

# Vocabulary extraction
words_it_en = {}
# Common words to exclude from vocabulary if we have enough
stop_words = {'il', 'lo', 'la', 'i', 'gli', 'le', 'un', 'una', 'uno', 'e', 'è', 'di', 'a', 'in', 'con', 'su', 'per', 'tra', 'fra', 'che', 'non', 'mi', 'ti', 'si', 'ci', 'vi', 'lo', 'la', 'li', 'le', 'ne', 'si', 'ho', 'hai', 'ha', 'abbiamo', 'avete', 'hanno', 'sono', 'sei', 'è', 'siamo', 'siete', 'sono'}

# We'll use a manual dictionary for common words found in this scenario
vocab_dict = {
    "cellulare": "cell phone",
    "computer": "computer",
    "schermo": "screen",
    "memoria": "memory",
    "gigabyte": "gigabyte",
    "prezzo": "price",
    "caricabatterie": "charger",
    "custodia": "case",
    "protettiva": "protective",
    "trasparente": "transparent",
    "contanti": "cash",
    "carta": "card",
    "credito": "credit",
    "scontrino": "receipt",
    "busta": "bag",
    "cuffie": "headphones",
    "batteria": "battery",
    "comode": "comfortable",
    "suono": "sound",
    "chiaro": "clear",
    "fantastico": "fantastic",
    "promozione": "promotion",
    "bianco": "white",
    "nero": "black",
    "riduzione": "reduction",
    "rumore": "noise",
    "cavo": "cable",
    "filo": "wire",
    "adattatore": "adapter",
    "assicurazione": "insurance",
    "danni": "damage",
    "portatile": "laptop",
    "sedici": "sixteen",
    "dieci": "ten",
    "leggero": "light",
    "sottile": "thin",
    "ufficio": "office",
    "sistema": "system",
    "operativo": "operating",
    "installato": "installed",
    "porte": "ports",
    "collegare": "connect",
    "mouse": "mouse",
    "tastiera": "keyboard",
    "retroilluminata": "backlit",
    "scrivere": "write",
    "pacchetto": "package",
    "negozio": "store",
    "garanzia": "warranty",
    "standard": "standard",
    "obbligatori": "mandatory",
    "legge": "law",
    "coperta": "covered",
    "protezione": "protection",
    "rassicura": "reassures",
    "sicuro": "safe",
    "difetti": "defects",
    "fabbrica": "factory",
    "accidentali": "accidental",
    "estendere": "extend",
    "estensione": "extension",
    "valida": "valid",
    "guasto": "breakdown"
}

# Distractor generation helpers
semantic_categories = {
    "objects": ["cellulare", "computer", "mouse", "tastiera", "cuffie", "cavo", "busta", "scontrino", "caricabatterie", "custodia", "adattatore"],
    "specs": ["memoria", "batteria", "schermo", "suono", "gigabyte", "sistema", "porte"],
    "adjectives": ["grande", "piccolo", "leggero", "sottile", "comodo", "chiaro", "fantastico", "veloce", "lento", "caro", "economico"],
    "colors": ["nero", "bianco", "blu", "rosso", "verde", "giallo"],
    "business": ["prezzo", "contanti", "carta", "garanzia", "promozione", "sconto", "assicurazione", "estensione", "scontrino", "iva"]
}

def get_distractors(word, lang='it'):
    # Simple distractor generator based on semantic categories
    cat = None
    for c, words in semantic_categories.items():
        if word in words:
            cat = c
            break
    
    if cat:
        options = [w for w in semantic_categories[cat] if w != word]
        import random
        random.shuffle(options)
        return options[:3]
    else:
        # Fallback to random words from vocab_dict
        import random
        options = [w for w in vocab_dict.keys() if w != word]
        random.shuffle(options)
        return options[:3]

# Generate Vocabulary JSON
vocab_json = []
for i, (it, en) in enumerate(vocab_dict.items()):
    dist_it = get_distractors(it)
    choices_it = [it] + dist_it
    import random
    random.shuffle(choices_it)
    
    # Map choices to English for choicesEnglish
    choices_en = []
    for c in choices_it:
        if c == it:
            choices_en.append(en)
        else:
            choices_en.append(vocab_dict.get(c, "???"))

    vocab_json.append({
        "id": f"v{i+1}",
        "italian": it,
        "english": en,
        "audio": {"italian": ""}, # Will be filled by audio specialist or hash
        "choicesItalian": choices_it,
        "choicesEnglish": choices_en,
        "feedback": {
            "correctItalian": "Esatto!",
            "incorrectItalian": f"No, significa '{en}'.",
            "correctEnglish": "Correct!",
            "incorrectEnglish": f"No, it means '{it}'."
        }
    })

# Generate Sentences JSON
sentences_json = []
for i, s in enumerate(unique_sentences):
    # For sentences, distractors should be other sentences
    import random
    other_sentences = [os['italian'] for os in unique_sentences if os['italian'] != s['italian']]
    random.shuffle(other_sentences)
    choices_it = [s['italian']] + other_sentences[:3]
    random.shuffle(choices_it)
    
    choices_en = []
    for c in choices_it:
        found = False
        for os in unique_sentences:
            if os['italian'] == c:
                choices_en.append(os['english'])
                found = True
                break
        if not found:
            choices_en.append("???")

    sentences_json.append({
        "id": f"s{i+1}",
        "italian": s['italian'],
        "english": s['english'],
        "audio": {"italian": ""},
        "choicesItalian": choices_it,
        "choicesEnglish": choices_en,
        "feedback": {
            "correctItalian": "Perfetto!",
            "incorrectItalian": "Non è corretto.",
            "correctEnglish": "Perfect!",
            "incorrectEnglish": "That is not correct."
        }
    })

# Generate Phrases JSON
# For phrases, we'll use shorter sentences or parts
phrases_json = []
phrase_count = 0
for s in unique_sentences:
    if len(s['italian'].split()) <= 4:
        # Use as phrase
        phrase_count += 1
        import random
        other_phrases = [os['italian'] for os in unique_sentences if os['italian'] != s['italian'] and len(os['italian'].split()) <= 5]
        random.shuffle(other_phrases)
        choices_it = [s['italian']] + other_phrases[:3]
        random.shuffle(choices_it)
        
        choices_en = []
        for c in choices_it:
            found = False
            for os in unique_sentences:
                if os['italian'] == c:
                    choices_en.append(os['english'])
                    found = True
                    break
            if not found:
                choices_en.append("???")

        phrases_json.append({
            "id": f"p{phrase_count}",
            "italian": s['italian'],
            "english": s['english'],
            "audio": {"italian": ""},
            "choicesItalian": choices_it,
            "choicesEnglish": choices_en,
            "feedback": {
                "correctItalian": "Ottimo!",
                "incorrectItalian": "Riprova.",
                "correctEnglish": "Great!",
                "incorrectEnglish": "Try again."
            }
        })
    if phrase_count >= 50:
        break

# If we don't have enough phrases, add some common ones from the scenario
if phrase_count < 45:
    extra_phrases = [
        ("Quanto costa?", "How much does it cost?"),
        ("Lo prendo.", "I'll take it."),
        ("No grazie.", "No thanks."),
        ("Sì, per favore.", "Yes, please."),
        ("Vorrei questo.", "I would like this."),
        ("È troppo caro.", "It's too expensive."),
        ("Va bene.", "Alright."),
        ("Mi serve un caricabatterie.", "I need a charger."),
        ("Ecco lo scontrino.", "Here is the receipt."),
        ("Pago con carta.", "I pay by card."),
        ("In contanti?", "In cash?"),
        ("Due anni.", "Two years."),
        ("Un anno.", "One year."),
        ("Molto comode.", "Very comfortable."),
        ("Il suono è chiaro.", "The sound is clear."),
        ("È pronto?", "Is it ready?"),
        ("Dieci minuti.", "Ten minutes."),
        ("Ottima scelta!", "Great choice!"),
        ("Posso aiutarla?", "Can I help you?"),
        ("Buongiorno.", "Good morning.")
    ]
    for it, en in extra_phrases:
        if any(p['italian'] == it for p in phrases_json): continue
        phrase_count += 1
        import random
        choices_it = [it] + [ep[0] for ep in extra_phrases if ep[0] != it]
        random.shuffle(choices_it)
        choices_it = choices_it[:4]
        if it not in choices_it: choices_it[0] = it
        random.shuffle(choices_it)
        
        choices_en = []
        for c in choices_it:
            found = False
            if c == it:
                choices_en.append(en)
                found = True
            else:
                for ep in extra_phrases:
                    if ep[0] == c:
                        choices_en.append(ep[1])
                        found = True
                        break
            if not found: choices_en.append("???")

        phrases_json.append({
            "id": f"p{phrase_count}",
            "italian": it,
            "english": en,
            "audio": {"italian": ""},
            "choicesItalian": choices_it,
            "choicesEnglish": choices_en,
            "feedback": {
                "correctItalian": "Esatto!",
                "incorrectItalian": "Sbagliato.",
                "correctEnglish": "Exact!",
                "incorrectEnglish": "Wrong."
            }
        })

# Save files
with open('src/data/exports/shopping/electronics_store/shopping_electronics_store_vocabulary.json', 'w', encoding='utf-8') as f:
    json.dump(vocab_json, f, indent=2, ensure_ascii=False)
with open('src/data/exports/shopping/electronics_store/shopping_electronics_store_phrases.json', 'w', encoding='utf-8') as f:
    json.dump(phrases_json, f, indent=2, ensure_ascii=False)
with open('src/data/exports/shopping/electronics_store/shopping_electronics_store_sentences.json', 'w', encoding='utf-8') as f:
    json.dump(sentences_json, f, indent=2, ensure_ascii=False)

# Update Mini Lessons
# We'll create 6 lessons, each covering one aspect and using a subset of the new IDs.
lessons = []
# Lesson 1: General Help & Shop
v_l1 = [f"v{i}" for i in range(1, 11)]
p_l1 = [f"p{i}" for i in range(1, 6)]
s_l1 = [f"s{i}" for i in range(1, 6)]
lessons.append({
    "id": "l1", "title": "At the Tech Store", "goal": "Learn basic store interaction.",
    "sections": [
        {"type": "vocabulary", "title": "Store Words", "exerciseIds": v_l1},
        {"type": "phrase", "title": "Basic Phrases", "exerciseIds": p_l1},
        {"type": "sentence", "title": "Greetings", "exerciseIds": s_l1}
    ]
})
# Lesson 2: Smartphones
v_l2 = [f"v{i}" for i in range(11, 21)]
p_l2 = [f"p{i}" for i in range(6, 11)]
s_l2 = [f"s{i}" for i in range(6, 11)]
lessons.append({
    "id": "l2", "title": "Smartphones", "goal": "Buying a phone.",
    "sections": [
        {"type": "vocabulary", "title": "Phone Words", "exerciseIds": v_l2},
        {"type": "phrase", "title": "Phone Phrases", "exerciseIds": p_l2},
        {"type": "sentence", "title": "Buying a Phone", "exerciseIds": s_l2}
    ]
})
# Lesson 3: Audio
v_l3 = [f"v{i}" for i in range(21, 31)]
p_l3 = [f"p{i}" for i in range(11, 16)]
s_l3 = [f"s{i}" for i in range(11, 16)]
lessons.append({
    "id": "l3", "title": "Audio Gear", "goal": "Choosing headphones.",
    "sections": [
        {"type": "vocabulary", "title": "Audio Words", "exerciseIds": v_l3},
        {"type": "phrase", "title": "Audio Phrases", "exerciseIds": p_l3},
        {"type": "sentence", "title": "Headphones", "exerciseIds": s_l3}
    ]
})
# Lesson 4: Computers
v_l4 = [f"v{i}" for i in range(31, 41)]
p_l4 = [f"p{i}" for i in range(16, 21)]
s_l4 = [f"s{i}" for i in range(16, 21)]
lessons.append({
    "id": "l4", "title": "Computers", "goal": "Discussing laptops.",
    "sections": [
        {"type": "vocabulary", "title": "Computer Words", "exerciseIds": v_l4},
        {"type": "phrase", "title": "Laptop Phrases", "exerciseIds": p_l4},
        {"type": "sentence", "title": "Laptop Specs", "exerciseIds": s_l4}
    ]
})
# Lesson 5: Warranty
v_l5 = [f"v{i}" for i in range(41, 51)]
p_l5 = [f"p{i}" for i in range(21, 26)]
s_l5 = [f"s{i}" for i in range(21, 26)]
lessons.append({
    "id": "l5", "title": "Warranty & Protection", "goal": "Ask about warranty.",
    "sections": [
        {"type": "vocabulary", "title": "Warranty Words", "exerciseIds": v_l5},
        {"type": "phrase", "title": "Protection Phrases", "exerciseIds": p_l5},
        {"type": "sentence", "title": "Warranty Info", "exerciseIds": s_l5}
    ]
})
# Lesson 6: Finalizing
v_l6 = [f"v{i}" for i in range(51, len(vocab_json)+1)]
p_l6 = [f"p{i}" for i in range(26, min(len(phrases_json)+1, 35))]
s_l6 = [f"s{i}" for i in range(26, min(len(sentences_json)+1, 35))]
lessons.append({
    "id": "l6", "title": "Final Purchase", "goal": "Completing the transaction.",
    "sections": [
        {"type": "vocabulary", "title": "Final Words", "exerciseIds": v_l6},
        {"type": "phrase", "title": "Payment Phrases", "exerciseIds": p_l6},
        {"type": "sentence", "title": "Receipt & Bag", "exerciseIds": s_l6}
    ]
})

# Add boilerplate to lessons
for i, l in enumerate(lessons):
    l["estimatedDuration"] = "3 mins"
    l["unlockCriteria"] = "none" if i == 0 else "complete_previous"
    l["nextLesson"] = f"l{i+2}" if i < len(lessons)-1 else "none"
    for sec in l["sections"]:
        sec["description"] = f"Practice {sec['type']}."
    l["sections"].append({
        "type": "mastery", "title": "Mastery Check", "description": "Prove your skills.", "exerciseIds": [l["sections"][1]["exerciseIds"][0]]
    })

with open('src/data/exports/shopping/electronics_store/mini_lessons.json', 'w', encoding='utf-8') as f:
    json.dump({"lessons": lessons}, f, indent=2, ensure_ascii=False)
