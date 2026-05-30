import json
import os
import sys

def main(scenario_slug):
    file_path = f"src/data/exports/{scenario_slug}/mini_lessons.json"
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Failed to load {file_path}: {e}")
        return False
        
    lessons = data.get("lessons", [])
    errors = []
    
    for l in lessons:
        if not l.get("title"):
            errors.append(f"Lesson {l.get('id')} missing title")
        if not l.get("goal"):
            errors.append(f"Lesson {l.get('id')} missing goal")
            
        sections = l.get("sections", [])
        if not sections:
            errors.append(f"Lesson {l.get('id')} has no sections")
            
        for s in sections:
            # We expect sections for vocabulary, phrases, sentences, mastery
            exercises = s.get("exerciseIds", [])
            seen_exercises = set()
            for e_id in exercises:
                if e_id in seen_exercises:
                    errors.append(f"Lesson {l.get('id')} Section '{s.get('type')}' has duplicate exercise {e_id}")
                seen_exercises.add(e_id)

    print(f"--- Lesson Integrity Audit: {scenario_slug} ---")
    if errors:
        for e in errors[:10]: print(f"  - {e}")
        print("Lesson Audit: FAIL")
        return False
    else:
        print("Lesson Audit: PASS")
        return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "accommodation/apartment_key_pickup"
    sys.exit(0 if main(slug) else 1)
