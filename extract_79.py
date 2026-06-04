import json
import os
import re
import random

scenario_path = 'src/data/exports/social/birthday_wishes'
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

common_phrases_list = [
    ("Tanti auguri", "Happy birthday"),
    ("Buon compleanno", "Happy birthday"),
    ("Grazie mille", "Thank you very much"),
    ("Per favore", "Please"),
    ("Va bene", "Alright / Okay"),
    ("A dopo", "See you later"),
    ("D'accordo", "Agreed"),
    ("Ottima idea", "Great idea"),
    ("Nessun problema", "No problem"),
    ("Ecco a te", "Here you go"),
    ("Figurati", "Don't mention it / You're welcome"),
    ("Di niente", "You're welcome"),
    ("A stasera", "See you tonight"),
    ("Non vedo l'ora", "I can't wait"),
    ("Che bella idea", "What a great idea"),
    ("Complimenti", "Congratulations / Well done")
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
                    # Note: choice might not have 'english' field in some cases, but here they do.
                    sentences.append({"italian": choice['text'], "english": choice.get('english', '')})
                    seen_sentences.add(choice['text'])
                    all_extracted_text += " " + choice['text']

# Extract vocabulary from all sentences
words = all_extracted_text.split()
for w in words:
    cw = clean_word(w)
    if cw and len(cw) > 1 and not cw.isdigit():
        vocab_set.add(cw)

sorted_vocab = sorted(list(vocab_set))

# Try to load existing translations to preserve them
existing_vocab_map = {}
vocab_file_path = os.path.join(scenario_path, 'social_birthday_wishes_vocabulary.json')
if os.path.exists(vocab_file_path):
    with open(vocab_file_path, 'r', encoding='utf-8') as f:
        existing_vocab = json.load(f)
        for item in existing_vocab:
            if item.get('english'):
                existing_vocab_map[item['italian']] = item['english']

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
        "english": existing_vocab_map.get(v, ""),
        "choicesItalian": choices
    })

# Create phrases.json
phrases_output = []
p_count = 1
for it, en in common_phrases_list:
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
with open(os.path.join(scenario_path, 'social_birthday_wishes_vocabulary.json'), 'w', encoding='utf-8') as f:
    json.dump(vocab_output, f, indent=2, ensure_ascii=False)

with open(os.path.join(scenario_path, 'social_birthday_wishes_phrases.json'), 'w', encoding='utf-8') as f:
    json.dump(phrases_output, f, indent=2, ensure_ascii=False)

with open(os.path.join(scenario_path, 'social_birthday_wishes_sentences.json'), 'w', encoding='utf-8') as f:
    json.dump(sentences_output, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(vocab_output)} words, {len(phrases_output)} phrases, {len(sentences_output)} sentences.")
