
import json

file_path = 'src/data/exports/dining/wine_bar/conversations.json'

with open(file_path, 'r') as f:
    data = json.load(f)

for conversation in data['conversations']:
    for message in conversation['messages']:
        if 'choices' in message:
            for i, choice in enumerate(message['choices']):
                if i == 0:
                    choice['isCorrect'] = True
                else:
                    choice['isCorrect'] = False

with open(file_path, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
