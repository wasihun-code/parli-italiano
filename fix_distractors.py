import json
import random

file_path = 'src/data/exports/dining/paying_the_bill/dining_paying_the_bill_phrases.json'
with open(file_path, 'r') as f:
    phrases = json.load(f)

all_texts = [p['italian'] for p in phrases]

for p in phrases:
    correct = p['italian']
    others = [t for t in all_texts if t != correct]
    distractors = random.sample(others, 3)
    choices = [correct] + distractors
    random.shuffle(choices)
    p['choicesItalian'] = choices

with open(file_path, 'w') as f:
    json.dump(phrases, f, indent=2, ensure_ascii=False)
