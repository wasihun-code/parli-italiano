import json
import os

file_path = 'src/data/exports/shopping/souvenir_shop/conversations.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for conv in data['conversations']:
    for i, msg in enumerate(conv['messages']):
        msg['id'] = f'm{i+1}'

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
