import json
import os

path = 'src/data/exports/shopping/pharmacy_purchase/mini_lessons.json'
with open(path, 'r') as f:
    data = json.load(f)

new_lessons = []
for i, lesson in enumerate(data.get("lessons", [])):
    new_lesson = {
        "id": f"l{i+1}",
        "title": lesson.get("title", f"Lesson {i+1}"),
        "goal": f"Learn {lesson.get('title', '').lower()}",
        "sections": []
    }
    for sec_type in ["vocabulary", "phrases", "sentences"]:
        if sec_type in lesson and lesson[sec_type]:
            # remove any v, p, s prefixes if they exist to follow "No prefixes in IDs"?
            # Wait, the instruction says: "no prefixes in IDs" for the exercise IDs or lesson IDs?
            # the example has: "id": "l1" and "exerciseIds": ["v1", ...] 
            # So lesson id is "l1" (which has "l" prefix, wait).
            # Maybe the ids shouldn't be prefixed with scenario like "shopping_pharmacy_purchase_l1"?
            # Or the exerciseIds shouldn't have scenario prefix?
            
            # Let's just keep the existing exerciseIds as they are already v1, p1, etc.
            # I will create a python script that just maps exactly as the prompt example.
            
            exerciseIds = [x.split('_')[-1] if x.startswith('shopping_pharmacy_purchase_') else x for x in lesson[sec_type]]

            new_lesson["sections"].append({
                "type": sec_type,
                "exerciseIds": exerciseIds
            })
    new_lessons.append(new_lesson)

data["lessons"] = new_lessons
with open(path, 'w') as f:
    json.dump(data, f, indent=2)

print("Fixed mini_lessons.json")
