import json

with open('src/data/exports/health/pharmacy_symptoms/conversations.json', 'r') as f:
    data = json.load(f)

for conv in data['conversations']:
    for msg in conv['messages']:
        correct_text = next(c['text'] for c in msg['choices'] if c['isCorrect'])
        correct_len = len(correct_text)
        for choice in msg['choices']:
            if not choice['isCorrect']:
                distractor_len = len(choice['text'])
                ratio = distractor_len / correct_len
                if ratio < 0.6 or ratio > 1.4:
                    print(f"FAILED: Conv '{conv['id']}', Msg '{msg['id']}'")
                    print(f"  Correct: '{correct_text}' ({correct_len})")
                    print(f"  Distractor: '{choice['text']}' ({distractor_len}) - Ratio: {ratio:.2f}")
