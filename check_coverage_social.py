import json

def check_coverage():
    with open('src/data/exports/social/phone_call/social_phone_call_vocabulary.json', 'r') as f:
        vocab = json.load(f)
    with open('src/data/exports/social/phone_call/social_phone_call_phrases.json', 'r') as f:
        phrases = json.load(f)
    with open('src/data/exports/social/phone_call/social_phone_call_sentences.json', 'r') as f:
        sentences = json.load(f)
    with open('src/data/exports/social/phone_call/mini_lessons.json', 'r') as f:
        lessons = json.load(f)

    vocab_ids = {v['id'] for v in vocab}
    phrase_ids = {p['id'] for p in phrases}
    sentence_ids = {s['id'] for s in sentences}

    covered_vocab = set()
    covered_phrases = set()
    covered_sentences = set()

    for lesson in lessons['lessons']:
        for section in lesson['sections']:
            if section['type'] == 'vocabulary':
                covered_vocab.update(section['exerciseIds'])
            elif section['type'] == 'phrase':
                covered_phrases.update(section['exerciseIds'])
            elif section['type'] == 'sentence':
                covered_sentences.update(section['exerciseIds'])
            elif section['type'] == 'mastery':
                # Mastery check usually includes sentences/phrases but let's see
                pass

    missing_vocab = vocab_ids - covered_vocab
    missing_phrases = phrase_ids - covered_phrases
    missing_sentences = sentence_ids - covered_sentences

    print(f"Missing Vocab: {missing_vocab}")
    print(f"Missing Phrases: {missing_phrases}")
    print(f"Missing Sentences: {missing_sentences}")

if __name__ == "__main__":
    check_coverage()
