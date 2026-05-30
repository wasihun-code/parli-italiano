import json
import os
import sys

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
            
        def check_choices(choices, context, correct_text):
            if not choices: return
            
            if not (3 <= len(choices) <= 4):
                errors.append(f"{context}: has {len(choices)} choices (expected 3-4)")
                
            # No duplicates
            texts = [c.lower() for c in choices]
            if len(set(texts)) != len(texts):
                errors.append(f"{context}: contains duplicate choices")
                
            # Placeholders
            for c in choices:
                c_low = c.lower()
                if "distractor" in c_low or "placeholder" in c_low or c.strip() == "":
                    errors.append(f"{context}: contains placeholder '{c}'")
                    
                # Length check
                if correct_text:
                    correct_len = len(correct_text)
                    c_len = len(c)
                    if correct_len > 5:
                        diff = abs(correct_len - c_len)
                        allowed_diff = max(15, correct_len * 0.5)
                        if diff > allowed_diff:
                            errors.append(f"{context}: Distractor '{c}' length ({c_len}) is too different from correct ({correct_len}) (limit: {allowed_diff:.1f})")

        if is_conv:
            for conv in data.get("conversations", []):
                for msg in conv.get("messages", []):
                    choices = msg.get("choices", [])
                    if not choices: continue
                    
                    corrects = [c for c in choices if c.get("isCorrect")]
                    if len(corrects) != 1:
                        errors.append(f"Conv {conv['id']} Msg {msg['id']}: expected exactly 1 correct choice, got {len(corrects)}")
                    else:
                        texts = [c["text"] for c in choices]
                        check_choices(texts, f"Conv {conv['id']} Msg {msg['id']}", corrects[0]["text"])
        else:
            for item in data:
                # Vocab, Phrases, Sentences might have choicesItalian
                choices = item.get("choicesItalian")
                if choices:
                    check_choices(choices, f"{label} {item['id']}", item.get("italian"))

    print(f"--- Distractor Quality Audit: {scenario_slug} ---")
    if errors:
        for e in errors[:10]: print(f"  - {e}")
        print("Distractor Audit: FAIL")
        return False
    else:
        print("Distractor Audit: PASS")
        return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "accommodation/apartment_key_pickup"
    sys.exit(0 if main(slug) else 1)
