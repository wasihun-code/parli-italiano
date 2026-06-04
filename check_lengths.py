import json
import os

file_path = 'src/data/exports/daily_life/making_an_appointment/conversations.json'

with open(file_path, 'r') as f:
    data = json.load(f)

for conv in data['conversations']:
    print(f"Conversation: {conv['id']}")
    for msg in conv['messages']:
        correct_text = next(c['text'] for c in msg['choices'] if c['isCorrect'])
        target_len = len(correct_text)
        min_len = target_len * 0.6
        max_len = target_len * 1.4
        
        for i, choice in enumerate(msg['choices']):
            if choice['isCorrect']:
                continue
            choice_len = len(choice['text'])
            if choice_len < min_len or choice_len > max_len:
                print(f"  Message {msg['id']} Choice {i} ('{choice['text']}'): Length {choice_len} is out of bounds [{min_len:.1f}, {max_len:.1f}] (Correct: {target_len})")
