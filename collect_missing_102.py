import json
import os

path = "src/data/exports/tech/using_a_map_app"
files = [
    "tech_using_a_map_app_vocabulary.json",
    "tech_using_a_map_app_phrases.json",
    "tech_using_a_map_app_sentences.json"
]

missing = {}

for fname in files:
    fpath = os.path.join(path, fname)
    if not os.path.exists(fpath): continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        items = json.load(f)
        
    for item in items:
        if not item.get("english") or str(item.get("english")).strip() == "":
            missing[item["italian"]] = ""

with open("to_translate_102.json", "w", encoding="utf-8") as f:
    json.dump(missing, f, indent=2, ensure_ascii=False)
