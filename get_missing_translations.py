import json

files = [
    "src/data/exports/dining/market_lunch/dining_market_lunch_vocabulary.json",
    "src/data/exports/dining/market_lunch/dining_market_lunch_phrases.json",
    "src/data/exports/dining/market_lunch/dining_market_lunch_sentences.json"
]

missing = {}

for f in files:
    with open(f, 'r') as fp:
        data = json.load(fp)
    for item in data:
        if item.get("english") == "":
            missing[item["italian"]] = ""

print(f"Total missing: {len(missing)}")
with open("missing_it.json", "w") as fp:
    json.dump(missing, fp, indent=2)
