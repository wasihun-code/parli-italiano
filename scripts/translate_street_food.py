import json

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def translate():
    # Vocabulary translations
    vocab_file = 'src/data/exports/dining/street_food/dining_street_food_vocabulary.json'
    vocab = load_json(vocab_file)
    
    # We will just write a simple translator function here or hardcode a big dict.
    # Since I'm an AI generating this script, I'll provide a dict for the words.
    
    # Phrases
    phrases_file = 'src/data/exports/dining/street_food/dining_street_food_phrases.json'
    phrases = load_json(phrases_file)
    
    # Sentences
    sentences_file = 'src/data/exports/dining/street_food/dining_street_food_sentences.json'
    sentences = load_json(sentences_file)
    
    # For phrases and sentences, I can parse conversations.json to get translations if they exist,
    # or just provide them. Let's dump all missing to a temp file to see what we need.
    missing_vocab = [v['italian'] for v in vocab if not v.get('english')]
    missing_phrases = [p['italian'] for p in phrases if not p.get('english')]
    missing_sentences = [s['italian'] for s in sentences if not s.get('english')]
    
    with open('missing_translations.json', 'w') as f:
        json.dump({"vocab": missing_vocab, "phrases": missing_phrases, "sentences": missing_sentences}, f, indent=2, ensure_ascii=False)

translate()
