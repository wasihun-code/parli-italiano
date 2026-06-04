import json

file_path = 'src/data/exports/social/phone_call/social_phone_call_vocabulary.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

missing = [item['italian'] for item in data if not item['english']]
print(json.dumps(missing, indent=2))
