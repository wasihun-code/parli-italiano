import json

vocab_path = 'src/data/exports/accommodation/apartment_key_pickup/accommodation_apartment_key_pickup_vocabulary.json'
lessons_path = 'src/data/exports/accommodation/apartment_key_pickup/mini_lessons.json'

print("--- VOCABULARY JSON CONTENT ---")
try:
    with open(vocab_path, 'r', encoding='utf-8') as f:
        vocab_data = json.load(f)
        
    ids_to_check = ['s22-v2', 's22-v3', 's22-v15', 's22-v16', 's22-v21']
    found_ids = {}
    
    for item in vocab_data:
        item_id = item.get('id')
        if item_id in ids_to_check:
            found_ids[item_id] = item.get('italian') or item.get('correctAnswerItalian', 'N/A')
            
    for req_id in ids_to_check:
        print(f"1. Does '{req_id}' exist? {'YES' if req_id in found_ids else 'NO'}")
        if req_id in found_ids:
            print(f"   ID: {req_id}")
            print(f"   Italian text: {found_ids[req_id]}")
except Exception as e:
    print(f"Error reading vocabulary: {e}")

print("\n--- LESSON 1 REFERENCES ---")
try:
    with open(lessons_path, 'r', encoding='utf-8') as f:
        lessons_data = json.load(f)
        
    lesson_1 = next((l for l in lessons_data.get('lessons', []) if l.get('id') == 'l1'), None)
    if lesson_1:
        for section in lesson_1.get('sections', []):
            if section.get('type') == 'vocabulary':
                print(f"Exercise IDs: {json.dumps(section.get('exerciseIds', []), indent=2)}")
    else:
        print("Lesson 1 not found.")
except Exception as e:
    print(f"Error reading mini_lessons.json: {e}")

