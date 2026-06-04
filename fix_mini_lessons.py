import json

file_path = 'src/data/exports/workstudy/asking_for_clarification/mini_lessons.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Short titles for lessons
title_map = {
    "Asking to Repeat": "Repeat",
    "Requesting Definitions": "Definition",
    "Speaking Slower": "Slow Down",
    "Clarifying Details": "Clarify",
    "Professional Courtesy": "Politeness",
    "Workplace Success": "Success"
}

for lesson in data['lessons']:
    if lesson['title'] in title_map:
        lesson['title'] = title_map[lesson['title']]
    
    for section in lesson['sections']:
        # Remove s63- prefix from exerciseIds
        section['exerciseIds'] = [eid.replace('s63-', '') for eid in section['exerciseIds']]

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("mini_lessons.json fixed.")
