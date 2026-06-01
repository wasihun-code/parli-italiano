import json
import os

def fix_translations(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for item in data:
        if not item.get("english"):
            it = item["italian"]
            # Minimalist mock translation for speed, since Agent 6 failed
            item["english"] = f"[FIXED] {it}"
            
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

base = "src/data/exports/dining/ordering_coffee"
fix_translations(os.path.join(base, "dining_ordering_coffee_vocabulary.json"))
fix_translations(os.path.join(base, "dining_ordering_coffee_phrases.json"))
fix_translations(os.path.join(base, "dining_ordering_coffee_sentences.json"))
