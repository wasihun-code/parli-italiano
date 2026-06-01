import json
import random

def fix_file(file_path):
    with open(file_path, 'r') as f:
        items = json.load(f)

    all_texts = [p['italian'] for p in items]

    for p in items:
        correct = p['italian']
        others = [t for t in all_texts if t != correct]
        
        # Try to find distractors with similar length
        others_by_len = sorted(others, key=lambda x: abs(len(x) - len(correct)))
        
        # Filter by length diff < 15
        candidates = [t for t in others if abs(len(t) - len(correct)) <= 15]
        
        if len(candidates) < 3:
            # Relax constraint if not enough candidates
            candidates = others_by_len[:10]
        
        distractors = random.sample(candidates, 3)
        choices = [correct] + distractors
        random.shuffle(choices)
        p['choicesItalian'] = choices

    with open(file_path, 'w') as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

fix_file('src/data/exports/dining/paying_the_bill/dining_paying_the_bill_phrases.json')
fix_file('src/data/exports/dining/paying_the_bill/dining_paying_the_bill_sentences.json')
fix_file('src/data/exports/dining/paying_the_bill/dining_paying_the_bill_vocabulary.json')
