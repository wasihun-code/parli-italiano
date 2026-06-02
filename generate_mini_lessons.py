import json
import os

base_path = 'src/data/exports/miscellaneous/asking_for_help/'
prefix = 'miscellaneous_asking_for_help'

files = {
    'vocab': f"{prefix}_vocabulary.json",
    'phrase': f"{prefix}_phrases.json",
    'sentence': f"{prefix}_sentences.json"
}

data = {}
for key, filename in files.items():
    path = os.path.join(base_path, filename)
    with open(path, 'r', encoding='utf-8') as f:
        items = json.load(f)
        # remove prefix if present
        data[key] = [item['id'].replace(prefix + '_', '') for item in items]

num_lessons = 6
titles = [
    'Getting Attention', 
    'Asking for Directions', 
    'Using Machines', 
    'Understanding Directions', 
    'Thanking for Help', 
    'Final Review'
]

lessons = []
for i in range(num_lessons):
    # calculate slice
    v_chunk = len(data['vocab']) // num_lessons
    p_chunk = len(data['phrase']) // num_lessons
    s_chunk = len(data['sentence']) // num_lessons

    v_start = i * v_chunk
    p_start = i * p_chunk
    s_start = i * s_chunk

    v_end = (i + 1) * v_chunk if i < num_lessons - 1 else len(data['vocab'])
    p_end = (i + 1) * p_chunk if i < num_lessons - 1 else len(data['phrase'])
    s_end = (i + 1) * s_chunk if i < num_lessons - 1 else len(data['sentence'])

    lessons.append({
        "id": f"l{i+1}",
        "title": titles[i],
        "goal": f"Master {titles[i].lower()}.",
        "sections": [
            {
                "type": "vocabulary",
                "exerciseIds": data['vocab'][v_start:v_end]
            },
            {
                "type": "phrase",
                "exerciseIds": data['phrase'][p_start:p_end]
            },
            {
                "type": "sentence",
                "exerciseIds": data['sentence'][s_start:s_end]
            },
            {
                "type": "mastery",
                "exerciseIds": data['sentence'][s_start:s_end]
            }
        ]
    })

mini_lessons = {
    "lessons": lessons
}

with open(os.path.join(base_path, 'mini_lessons.json'), 'w', encoding='utf-8') as f:
    json.dump(mini_lessons, f, indent=2, ensure_ascii=False)

print("Generated mini_lessons.json")
