import json
import os

base_path = 'src/data/exports/miscellaneous/asking_for_help/'
prefix = 'miscellaneous_asking_for_help'

files = [
    f"{prefix}_vocabulary.json",
    f"{prefix}_phrases.json",
    f"{prefix}_sentences.json"
]

missing = {}

for filename in files:
    path = os.path.join(base_path, filename)
    with open(path, 'r', encoding='utf-8') as f:
        items = json.load(f)
    for item in items:
        if not item.get("english"):
            missing[item["italian"]] = ""

print(json.dumps(missing, indent=2, ensure_ascii=False))
