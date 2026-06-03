import json

file_path = '/home/waseageru/parli-italiano/src/data/exports/travel/parking/travel_parking_vocabulary.json'

with open(file_path, 'r') as f:
    data = json.load(f)

translations = {
    "sua": "your",
    "subito": "immediately",
    "succede": "happens",
    "sul": "on the",
    "sull": "on the",
    "tornare": "to return",
    "tra": "between",
    "trovano": "they find",
    "tutti": "all",
    "vedere": "to see",
    "visto": "seen",
    "vorrei": "I would like"
}

for entry in data:
    if entry['italian'] in translations and entry['english'] == "":
        entry['english'] = translations[entry['italian']]

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
