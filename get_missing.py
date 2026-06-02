import json

files = [
    'src/data/exports/miscellaneous/talking_about_money/miscellaneous_talking_about_money_vocabulary.json',
    'src/data/exports/miscellaneous/talking_about_money/miscellaneous_talking_about_money_phrases.json',
    'src/data/exports/miscellaneous/talking_about_money/miscellaneous_talking_about_money_sentences.json'
]

missing = {}
for f in files:
    with open(f, 'r') as file:
        data = json.load(file)
        for item in data:
            if not item.get('english'):
                missing[item['italian']] = ""

with open('missing_it.json', 'w') as out:
    json.dump(missing, out, indent=2, ensure_ascii=False)
