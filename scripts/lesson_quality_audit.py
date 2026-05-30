import json
import os
import sys

def run_lesson_audit(scenario_dir="src/data/exports/accommodation/apartment_key_pickup"):
    print("\n--- LESSON QUALITY AUDIT ---")
    
    try:
        with open(os.path.join(scenario_dir, "mini_lessons.json"), "r", encoding="utf-8") as f:
            lessons = json.load(f)["lessons"]
        with open(os.path.join(scenario_dir, "accommodation_apartment_key_pickup_vocabulary.json"), "r", encoding="utf-8") as f:
            vocab = json.load(f)
    except Exception as e:
        print(f"FAIL: Could not load json: {e}")
        return False

    errors = []
    
    for l in lessons:
        if not l.get("title"):
            errors.append(f"Lesson {l['id']} missing title.")
        if not l.get("goal"):
            errors.append(f"Lesson {l['id']} missing goal.")
            
        types = [s["type"] for s in l.get("sections", [])]
        if "vocabulary" not in types or "phrase" not in types or "sentence" not in types:
            errors.append(f"Lesson {l['id']} incomplete sections.")
            
    # Check vocab items
    for v in vocab:
        if not v.get("english"):
            errors.append(f"Vocab {v['id']} ({v['italian']}) has empty translation.")
        if "Translation of" in v.get("english", "") or "Placeholder" in v.get("english", ""):
            errors.append(f"Vocab {v['id']} ({v['italian']}) has placeholder translation.")
        if any(char.isdigit() for char in v["italian"]):
            errors.append(f"Vocab {v['id']} ({v['italian']}) contains numeric characters.")

    if errors:
        print(f"Errors found: {len(errors)}")
        for e in errors[:5]: print(f"  - {e}")
        print("LESSON AUDIT: FAIL")
        return False
        
    print("LESSON AUDIT: PASS")
    return True

if __name__ == "__main__":
    success = run_lesson_audit()
    sys.exit(0 if success else 1)
