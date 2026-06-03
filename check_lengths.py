import json

def check_lengths(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    issues = []
    for conv in data['conversations']:
        for msg in conv['messages']:
            choices = msg['choices']
            correct = next(c for c in choices if c['isCorrect'])
            correct_len = len(correct['text'])
            
            for i, choice in enumerate(choices):
                if choice['isCorrect']:
                    continue
                choice_len = len(choice['text'])
                min_len = correct_len * 0.6
                max_len = correct_len * 1.4
                if choice_len < min_len or choice_len > max_len:
                    issues.append({
                        "conv": conv['id'],
                        "msg": msg['id'],
                        "choice_index": i,
                        "correct_text": correct['text'],
                        "correct_len": correct_len,
                        "choice_text": choice['text'],
                        "choice_len": choice_len,
                        "range": (min_len, max_len)
                    })
    return issues

issues = check_lengths('src/data/exports/travel/asking_directions/conversations.json')
for issue in issues:
    print(issue)
