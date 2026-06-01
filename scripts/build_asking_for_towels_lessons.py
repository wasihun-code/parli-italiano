import json
import math
import os

base_path = 'src/data/exports/accommodation/asking_for_towels/'

def get_ids(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [item['id'] for item in data]

vocab_ids = get_ids(base_path + 'asking_for_towels_vocabulary.json')
phrase_ids = get_ids(base_path + 'asking_for_towels_phrases.json')
sentence_ids = get_ids(base_path + 'asking_for_towels_sentences.json')

all_ids = vocab_ids + phrase_ids + sentence_ids

lessons = [
    {"id": "l1", "title": "Lesson 1", "goal": "Basic Bathroom Amenities"},
    {"id": "l2", "title": "Lesson 2", "goal": "Bedding & Comfort"},
    {"id": "l3", "title": "Lesson 3", "goal": "Quantities & Requests"},
    {"id": "l4", "title": "Lesson 4", "goal": "Dealing with Housekeeping"},
    {"id": "l5", "title": "Lesson 5", "goal": "Asking for More"},
    {"id": "l6", "title": "Lesson 6", "goal": "Final Review"}
]

v_chunk = math.ceil(len(vocab_ids) / 6)
p_chunk = math.ceil(len(phrase_ids) / 6)
s_chunk = math.ceil(len(sentence_ids) / 6)

for i, lesson in enumerate(lessons):
    lesson["estimatedDuration"] = "3 mins"
    lesson["unlockCriteria"] = "none" if i == 0 else lessons[i-1]["id"]
    lesson["nextLesson"] = lessons[i+1]["id"] if i < 5 else "none"
    
    v_slice = vocab_ids[i*v_chunk : (i+1)*v_chunk]
    p_slice = phrase_ids[i*p_chunk : (i+1)*p_chunk]
    s_slice = sentence_ids[i*s_chunk : (i+1)*s_chunk]
    
    sections = []
    if v_slice:
        sections.append({
            "type": "vocabulary",
            "title": "Learn the Words",
            "description": "Essential vocabulary.",
            "exerciseIds": v_slice
        })
    if p_slice:
        sections.append({
            "type": "phrases",
            "title": "Useful Phrases",
            "description": "Key phrases for this topic.",
            "exerciseIds": p_slice
        })
    if s_slice:
        sections.append({
            "type": "sentences",
            "title": "Full Sentences",
            "description": "Put it all together.",
            "exerciseIds": s_slice
        })
    lesson["sections"] = sections

output = {"lessons": lessons}
with open(base_path + 'mini_lessons.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2)

print("Created mini_lessons.json")
