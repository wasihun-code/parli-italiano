import json

def check_parity(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    violations = []
    for conv in data['conversations']:
        for msg in conv['messages']:
            correct_choice = next(c for c in msg['choices'] if c['isCorrect'])
            correct_len = len(correct_choice['text'])
            min_len = correct_len * 0.6
            max_len = correct_len * 1.4
            
            for i, choice in enumerate(msg['choices']):
                if not choice['isCorrect']:
                    choice_len = len(choice['text'])
                    if choice_len < min_len or choice_len > max_len:
                        violations.append({
                            'conv': conv['title'],
                            'msg_id': msg['id'],
                            'choice_index': i,
                            'correct_text': correct_choice['text'],
                            'correct_len': correct_len,
                            'choice_text': choice['text'],
                            'choice_len': choice_len,
                            'min_len': min_len,
                            'max_len': max_len
                        })
    return violations

violations = check_parity('src/data/exports/workstudy/coworking_space/conversations.json')
for v in violations:
    print(f"Violation in {v['conv']} - {v['msg_id']}:")
    print(f"  Correct: ({v['correct_len']}) {v['correct_text']}")
    print(f"  Distractor {v['choice_index']}: ({v['choice_len']}) {v['choice_text']}")
    print(f"  Required range: {v['min_len']:.1f} - {v['max_len']:.1f}")
    print()
