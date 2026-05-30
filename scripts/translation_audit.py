import json
import os
import sys

def check_translation(eng, context, errors):
    if not eng or not eng.strip():
        errors.append(f"{context}: Missing English translation")
        return
    eng_low = eng.lower()
    if "translation of" in eng_low or "english for" in eng_low or "placeholder" in eng_low:
        errors.append(f"{context}: Placeholder translation detected '{eng}'")

def main(scenario_slug):
    base_path = f"src/data/exports/{scenario_slug}"
    parts = scenario_slug.split('/')
    prefix = "_".join(parts)
    
    files_to_check = [
        ("Conversations", os.path.join(base_path, "conversations.json"), True),
        ("Vocabulary", os.path.join(base_path, f"{prefix}_vocabulary.json"), False),
        ("Phrases", os.path.join(base_path, f"{prefix}_phrases.json"), False),
        ("Sentences", os.path.join(base_path, f"{prefix}_sentences.json"), False),
    ]
    
    errors = []
    
    for label, file_path, is_conv in files_to_check:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            errors.append(f"Failed to load {file_path}: {e}")
            continue
            
        if is_conv:
            for conv in data.get("conversations", []):
                for msg in conv.get("messages", []):
                    # In conversations, host lines need english.
                    if msg.get("role") == "host":
                        check_translation(msg.get("english"), f"Conv {conv['id']} Msg {msg['id']}", errors)
                    
                    # Choices don't always need explicit English translation if they are phrases, but in GS they usually map back.
                    # We only enforce host lines and core curriculum items.
        else:
            for item in data:
                check_translation(item.get("english"), f"{label} {item['id']}", errors)

    print(f"--- Translation Audit: {scenario_slug} ---")
    if errors:
        for e in errors[:10]: print(f"  - {e}")
        print("Translation Audit: FAIL")
        return False
    else:
        print("Translation Audit: PASS")
        return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "accommodation/apartment_key_pickup"
    sys.exit(0 if main(slug) else 1)
