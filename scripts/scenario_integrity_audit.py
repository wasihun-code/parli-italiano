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
    
    taught_ids = set()
    for l in data["lessons"].get("lessons", []):
        for s in l.get("sections", []):
            if isinstance(s, dict):
                for e_id in s.get("exerciseIds", []):
                    taught_ids.add(e_id)
            elif isinstance(s, str):
                taught_ids.add(s)
        for k in ["vocabulary", "phrase", "sentence", "phrases", "sentences", "mastery"]:
            if k in l:
                for e_id in l[k]:
                    taught_ids.add(e_id)
                    
    # 1. Check taught_ids <= valid_ids
    for e_id in taught_ids:
        if e_id not in valid_ids:
            errors.append(f"Lesson references missing item ID: {e_id}")

    # 2. Check valid_ids <= taught_ids
    untaught_ids = valid_ids - taught_ids
    if untaught_ids:
        errors.append(f"Coverage Failure: {len(untaught_ids)} extracted items are not taught in any lesson.")
        for e_id in sorted(list(untaught_ids))[:10]:
            errors.append(f"  - Untaught ID: {e_id}")

    print(f"--- Scenario Integrity Audit: {scenario_slug} ---")
    print(f"Total Extracted: {len(valid_ids)}")
    print(f"Total Taught: {len(taught_ids)}")
    if valid_ids:
        print(f"Coverage: {(len(taught_ids.intersection(valid_ids)) / len(valid_ids)) * 100:.1f}%")

    if errors:
        for e in errors[:15]: print(f"  - {e}")
        print("Scenario Integrity Audit: FAIL")
        return False
    else:
        print("Scenario Integrity Audit: PASS")
        return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "accommodation/apartment_key_pickup"
    sys.exit(0 if main(slug) else 1)
