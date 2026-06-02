import json

files = [
    "src/data/exports/dining/market_lunch/dining_market_lunch_vocabulary.json",
    "src/data/exports/dining/market_lunch/dining_market_lunch_phrases.json",
    "src/data/exports/dining/market_lunch/dining_market_lunch_sentences.json"
]

for f in files:
    with open(f, 'r') as fp:
        data = json.load(fp)
    c = 0
    for item in data:
        if item.get("english") == "":
            c += 1
    print(f"{f}: {c} missing")
