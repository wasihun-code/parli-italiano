import json
import os
import sys

path = "src/data/exports/tech/using_a_map_app"

def check_missing(filename):
    filepath = f"{path}/{filename}"
    if not os.path.exists(filepath):
        return
    with open(filepath, "r") as f:
        content = json.load(f)
    
    missing = []
    for item in content:
        if "english" not in item or not item["english"] or item["english"].strip() == "":
            missing.append(item)
    
    if missing:
        print(f"--- {filename} ---")
        for m in missing:
            print(json.dumps(m, ensure_ascii=False))

check_missing("tech_using_a_map_app_vocabulary.json")
check_missing("tech_using_a_map_app_phrases.json")
check_missing("tech_using_a_map_app_sentences.json")
