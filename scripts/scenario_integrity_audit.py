import json
import os
import sys

def main(scenario_slug):
    base_path = f"src/data/exports/{scenario_slug}"
    parts = scenario_slug.split('/')
    prefix = "_".join(parts)
    
    files = {
        "conversations": os.path.join(base_path, "conversations.json"),
        "vocab": os.path.join(base_path, f"{prefix}_vocabulary.json"),
        "phrases": os.path.join(base_path, f"{prefix}_phrases.json"),
        "sentences": os.path.join(base_path, f"{prefix}_sentences.json"),
        "lessons": os.path.join(base_path, "mini_lessons.json")
    }
    
    data = {}
    for k, p in files.items():
        try:
            with open(p, "r", encoding="utf-8") as f:
                data[k] = json.load(f)
        except Exception as e:
            print(f"Failed to load {p}: {e}")
            return False

    errors = []
    
    # Check that all lesson exerciseIds exist in the language inventory
    valid_ids = set()
    for item in data["vocab"]: valid_ids.add(item["id"])
    for item in data["phrases"]: valid_ids.add(item["id"])
    for item in data["sentences"]: valid_ids.add(item["id"])
    
    for l in data["lessons"].get("lessons", []):
        for s in l.get("sections", []):
            for e_id in s.get("exerciseIds", []):
                if e_id not in valid_ids:
                    errors.append(f"Lesson {l.get('id')} references missing item ID: {e_id}")

    print(f"--- Scenario Integrity Audit: {scenario_slug} ---")
    if errors:
        for e in errors[:10]: print(f"  - {e}")
        print("Scenario Integrity Audit: FAIL")
        return False
    else:
        print("Scenario Integrity Audit: PASS")
        return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "accommodation/apartment_key_pickup"
    sys.exit(0 if main(slug) else 1)
