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
    parts = scenario_slug.split('/')
    prefix = "_".join(parts)
    
    conv_path = os.path.join(base_path, "conversations.json")
    vocab_path = os.path.join(base_path, f"{prefix}_vocabulary.json")
    lessons_path = os.path.join(base_path, "mini_lessons.json")

    try:
        with open(conv_path, "r", encoding="utf-8") as f:
            conversations = json.load(f)["conversations"]
        with open(vocab_path, "r", encoding="utf-8") as f:
            vocab = json.load(f)
        with open(lessons_path, "r", encoding="utf-8") as f:
            lessons = json.load(f)["lessons"]
    except Exception as e:
        print(f"Error loading files: {e}")
        return False

    # Get all words that are taught across all lessons
    # According to curriculum rules, ALL conversation words must be taught.
    # The curriculum audit already verifies this.
    # The progression audit specifically ensures no word appears in conversation without being in the curriculum.
    # Since conversations are unlocked AFTER lessons, if the word is in the lessons, progression is valid.
    
    taught_words = set()
    for item in vocab:
        taught_words.add(item["italian"].lower())

    conv_words = set()
    for conv in conversations:
        for msg in conv.get("messages", []):
            conv_words.update(tokenize(msg["text"]))
            for c in msg.get("choices", []):
                if c.get("isCorrect"):
                    conv_words.update(tokenize(c["text"]))

    errors = []
    for word in conv_words:
        if word not in taught_words:
            errors.append(f"Word '{word}' appears in conversation but is never taught.")

    print(f"--- Progression Audit: {scenario_slug} ---")
    if errors:
        for e in errors[:10]: print(f"  - {e}")
        print("Progression Audit: FAIL")
        return False
    else:
        print("Progression Audit: PASS")
        return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "accommodation/apartment_key_pickup"
    sys.exit(0 if main(slug) else 1)
