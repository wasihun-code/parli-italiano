import json

file_path = 'src/data/exports/daily_life/at_the_post_office/conversations.json'
with open(file_path, 'r') as f:
    data = json.load(f)

for conv in data['conversations']:
    for msg in conv['messages']:
        if 'speaker' in msg:
            msg['role'] = msg.pop('speaker')
        if 'translation' in msg:
            msg['english'] = msg.pop('translation')
        
        if 'choices' in msg:
            for i, choice in enumerate(msg['choices']):
                if 'translation' in choice:
                    choice['english'] = choice.pop('translation')
                if i == 0:
                    choice['isCorrect'] = True
                else:
                    choice['isCorrect'] = False

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
