import json
import os
import sys
import random

def get_similar_length_items(pool, target, limit=3):
    target_len = len(target)
    # Filter pool to items with similar length (+/- 50% or at least 10 chars)
    # And not equal to target
    candidates = [p for p in pool if p.lower() != target.lower()]
    
    def length_diff(item):
        return abs(len(item) - target_len)
    
    candidates.sort(key=length_diff)
    return candidates[:limit]

def main(scenario_slug):
    base_path = f"src/data/exports/{scenario_slug}"
    parts = scenario_slug.split('/')
    prefix = "_".join(parts)
    
    files = [
        os.path.join(base_path, f"{prefix}_vocabulary.json"),
        os.path.join(base_path, f"{prefix}_phrases.json"),
        os.path.join(base_path, f"{prefix}_sentences.json")
    ]
    
    # Load all strings from the scenario for distractor pool
    all_italian = []
    for fpath in files:
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
                all_italian.extend([item["italian"] for item in data])
        except: pass

    for fpath in files:
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except: continue
        
        for item in data:
            if "choicesItalian" not in item:
                # Generate 3 distractors
                distractors = get_similar_length_items(all_italian, item["italian"], 3)
                choices = [item["italian"]] + distractors
                random.shuffle(choices)
                item["choicesItalian"] = choices
                
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Generated distractors for all curriculum files in {scenario_slug}.")
    return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else None
    if not slug: sys.exit(1)
    sys.exit(0 if main(slug) else 1)
