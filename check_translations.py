import json
import os

base_path = 'src/data/exports/shopping/souvenir_shop/'
files = [
    'shopping_souvenir_shop_vocabulary.json',
    'shopping_souvenir_shop_phrases.json',
    'shopping_souvenir_shop_sentences.json'
]

for file_name in files:
    file_path = os.path.join(base_path, file_name)
    print(f"Checking {file_name}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for i, item in enumerate(data):
        if 'english' not in item or not item['english']:
            print(f"Missing english in {file_name} at index {i}: {item.get('italian', 'NO ITALIAN')}")
