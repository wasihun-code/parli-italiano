import json
import os
import re
import sys

def tokenize(text):
    text = text.lower()
    text = text.replace("'", " ")
    text = re.sub(r'[^\w\sàèìòùé]', '', text)
    return {w for w in text.split() if len(w) > 2 and not w.isdigit()}

def main(scenario_slug):
    base_path = f"src/data/exports/{scenario_slug}"
    # e.g., if scenario_slug is accommodation/apartment_key_pickup, the files are accommodation_apartment_key_pickup_...
    parts = scenario_slug.split('/')
    prefix = "_".join(parts)
    
    conv_path = os.path.join(base_path, "conversations.json")
    vocab_path = os.path.join(base_path, f"{prefix}_vocabulary.json")
    phrases_path = os.path.join(base_path, f"{prefix}_phrases.json")
    sentences_path = os.path.join(base_path, f"{prefix}_sentences.json")

    try:
        with open(conv_path, "r", encoding="utf-8") as f:
            conversations = json.load(f)["conversations"]
        with open(vocab_path, "r", encoding="utf-8") as f:
            vocab = json.load(f)
        with open(phrases_path, "r", encoding="utf-8") as f:
            phrases = json.load(f)
        with open(sentences_path, "r", encoding="utf-8") as f:
            sentences = json.load(f)
    except Exception as e:
        print(f"Error loading files: {e}")
        return False

    conv_words = set()
    conv_phrases = set()
    conv_sentences = set()

    for conv in conversations:
        for msg in conv.get("messages", []):
            it_text = msg["text"].strip()
            conv_sentences.add(it_text)
            conv_words.update(tokenize(it_text))
            
            for choice in msg.get("choices", []):
                if choice.get("isCorrect"):
                    it_choice = choice["text"].strip()
                    conv_phrases.add(it_choice)
                    conv_words.update(tokenize(it_choice))

    lesson_v_it = {v["italian"].lower() for v in vocab}
    lesson_p_it = {p["italian"].lower() for p in phrases}
    lesson_s_it = {s["italian"].lower() for s in sentences}

    def check_coverage(target_set, source_set, label):
        missing = [item for item in target_set if item.lower() not in source_set]
        if missing:
            print(f"Missing {label}: {list(missing)[:5]}")
        percentage = (1 - len(missing)/max(len(target_set), 1)) * 100
        print(f"{label} Coverage: {percentage:.1f}%")
        return len(missing) == 0

    print(f"--- Curriculum Audit: {scenario_slug} ---")
    words_ok = check_coverage(conv_words, lesson_v_it, "Words")
    phrases_ok = check_coverage(conv_phrases, lesson_p_it, "Phrases")
    sentences_ok = check_coverage(conv_sentences, lesson_s_it, "Sentences")

    if words_ok and phrases_ok and sentences_ok:
        print("Curriculum Audit: PASS")
        return True
    else:
        print("Curriculum Audit: FAIL")
        return False

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "accommodation/apartment_key_pickup"
    sys.exit(0 if main(slug) else 1)
