import json
import os
import re
import sys
import string

def tokenize(text):
    text = text.lower()
    text = text.replace("'", " ")
    text = re.sub(r'[^\w\sàèìòùé]', '', text)
    return [w for w in text.split() if len(w) > 2 and not w.isdigit()]

def main(scenario_slug):
    base_path = f"src/data/exports/{scenario_slug}"
    conv_path = os.path.join(base_path, "conversations.json")
    
    parts = scenario_slug.split('/')
    prefix = "_".join(parts)
    
    try:
        with open(conv_path, "r", encoding="utf-8") as f:
            conversations = json.load(f)["conversations"]
    except Exception as e:
        print(f"Error loading conversations: {e}")
        return False

    all_sentences = set()
    all_phrases = set()
    all_words = set()
    
    # Map for translations
    translations = {}

    for conv in conversations:
        for msg in conv.get("messages", []):
            it_text = msg["text"].strip()
            all_sentences.add(it_text)
            if msg.get("english"):
                translations[it_text] = msg["english"]
            
            all_words.update(tokenize(it_text))
            
            for choice in msg.get("choices", []):
                if choice.get("isCorrect"):
                    it_choice = choice["text"].strip()
                    all_phrases.add(it_choice)
                    all_words.update(tokenize(it_choice))
                    if choice.get("english"):
                        translations[it_choice] = choice["english"]

    # Load existing translations if file exists to avoid data loss
    existing_translations = {}
    for fname in [f"{prefix}_vocabulary.json", f"{prefix}_phrases.json", f"{prefix}_sentences.json"]:
        p = os.path.join(base_path, fname)
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    old_items = json.load(f)
                    for item in old_items:
                        if item.get("english"):
                            existing_translations[item["italian"]] = item["english"]
            except: pass

    # Combine with new translations from conversations
    # (New ones in conversations take precedence if they changed)
    merged_translations = {**existing_translations, **translations}

    # Build JSON objects
    vocab_list = []
    for i, word in enumerate(sorted(list(all_words))):
        vocab_list.append({
            "id": f"v{i+1}",
            "italian": word,
            "english": merged_translations.get(word, ""),
            "audio": {"italian": f"/audio/{word}.opus"}
        })
        
    phrases_list = []
    for i, phrase in enumerate(sorted(list(all_phrases))):
        phrases_list.append({
            "id": f"p{i+1}",
            "italian": phrase,
            "english": translations.get(phrase, ""),
            "audio": {"italian": f"/audio/{phrase.replace(' ', '_')}.opus"}
        })
        
    sentences_list = []
    for i, sentence in enumerate(sorted(list(all_sentences))):
        sentences_list.append({
            "id": f"s{i+1}",
            "italian": sentence,
            "english": translations.get(sentence, ""),
            "audio": {"italian": f"/audio/{sentence.replace(' ', '_')}.opus"}
        })

    # Save files
    with open(os.path.join(base_path, f"{prefix}_vocabulary.json"), "w", encoding="utf-8") as f:
        json.dump(vocab_list, f, indent=2, ensure_ascii=False)
    with open(os.path.join(base_path, f"{prefix}_phrases.json"), "w", encoding="utf-8") as f:
        json.dump(phrases_list, f, indent=2, ensure_ascii=False)
    with open(os.path.join(base_path, f"{prefix}_sentences.json"), "w", encoding="utf-8") as f:
        json.dump(sentences_list, f, indent=2, ensure_ascii=False)

    print(f"Extracted {len(vocab_list)} words, {len(phrases_list)} phrases, {len(sentences_list)} sentences.")
    return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else None
    if not slug:
        print("Usage: python scripts/linguistic_extractor.py <scenario_slug>")
        sys.exit(1)
    sys.exit(0 if main(slug) else 1)
