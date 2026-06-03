import json
import os

path = "src/data/exports/tech/using_a_map_app"

with open("translated_102.json", "r", encoding="utf-8") as f:
    translations = json.load(f)

# Also load conversations to get phrase/sentence translations
conv_path = os.path.join(path, "conversations.json")
if os.path.exists(conv_path):
    with open(conv_path, "r", encoding="utf-8") as f:
        conversations = json.load(f)["conversations"]
    for conv in conversations:
        for msg in conv.get("messages", []):
            it = msg["text"].strip()
            if msg.get("english"):
                translations[it] = msg["english"]
            for choice in msg.get("choices", []):
                it_c = choice["text"].strip()
                if choice.get("english"):
                    translations[it_c] = choice["english"]

files = [
    "tech_using_a_map_app_vocabulary.json",
    "tech_using_a_map_app_phrases.json",
    "tech_using_a_map_app_sentences.json"
]

for fname in files:
    fpath = os.path.join(path, fname)
    if not os.path.exists(fpath): continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        items = json.load(f)
        
    updated = False
    for item in items:
        if not item.get("english") or str(item.get("english")).strip() == "":
            it = item["italian"].strip()
            if it in translations and translations[it]:
                item["english"] = translations[it]
                updated = True
            else:
                print(f"Still missing: {it} in {fname}")
                
    if updated:
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
        print(f"Updated {fname}")

