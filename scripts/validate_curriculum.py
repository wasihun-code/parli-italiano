import json
import os
import re

# Load corpus
BASE_DIR = "src/data/exports/accommodation/apartment_key_pickup"
def load_json(filename):
    with open(os.path.join(BASE_DIR, filename), "r", encoding="utf-8") as f:
        return json.load(f)

vocab = load_json("accommodation_apartment_key_pickup_vocabulary.json")
phrases = load_json("accommodation_apartment_key_pickup_phrases.json")
sentences = load_json("accommodation_apartment_key_pickup_sentences.json")

corpus_map = {}
for item in vocab + phrases + sentences:
    corpus_map[item["id"]] = item.get("italian") or item.get("correctAnswerItalian")

# Define dependencies (what words a phrase/sentence relies on from this scenario)
# This acts as the validation ground truth.
dependencies = {
    "s22-p3": ["s22-v2"], # Il portone è chiuso -> portone
    "s22-p29": [], # A quale nome devo suonare? (Foundational)
    "s22-p31": ["s22-v16"], # Sono l'ospite di Marco -> ospite
    "s22-s1": ["s22-p3"], # Pronto? Sono davanti al palazzo ma il portone è chiuso -> Il portone è chiuso
    "s22-s16": ["s22-p29", "s22-v3"], # A quale nome devo suonare sul citofono? -> citofono, A quale nome devo suonare?
    "s22-s18": ["s22-p31"], # Dì pure che sei l'ospite di Marco e ti aprirà -> Sono l'ospite di Marco
}

# Define the new Generic Sections Schema for Lesson 1
lesson_1 = {
    "id": "l1",
    "title": "Finding the Entrance",
    "goal": "Communicate your arrival and navigate the intercom system.",
    "estimatedDuration": "3 minutes",
    "unlockCriteria": "none",
    "nextLesson": "l2",
    "sections": [
        {
            "type": "vocabulary",
            "title": "Learn the Words",
            "description": "Essential words for arriving at the building.",
            "exerciseIds": ["s22-v2", "s22-v3", "s22-v16", "s22-v21"]
        },
        {
            "type": "phrase",
            "title": "Build the Phrases",
            "description": "Common phrases to use upon arrival.",
            "exerciseIds": ["s22-p3", "s22-p29", "s22-p31"]
        },
        {
            "type": "dialogue",
            "title": "Practice the Dialogue",
            "description": "Real conversations you might have at the intercom.",
            "exerciseIds": ["s22-s1", "s22-s16", "s22-s18"]
        },
        {
            "type": "mastery",
            "title": "Mastery Check",
            "description": "Prove you are ready to open the door.",
            "exerciseIds": ["s22-v3", "s22-p3", "s22-s16"]
        }
    ]
}

# Curriculum Validator
print("--- RUNNING CURRICULUM VALIDATION ---")
introduced = set()
errors = []

for section in lesson_1["sections"]:
    for ex_id in section["exerciseIds"]:
        if ex_id not in corpus_map:
            errors.append(f"Invalid ID: {ex_id}")
            continue
            
        # Check dependencies
        deps = dependencies.get(ex_id, [])
        for dep in deps:
            if dep not in introduced and dep not in section["exerciseIds"]:
                errors.append(f"Dependency Violation: '{corpus_map[ex_id]}' requires '{corpus_map[dep]}' which has not been introduced.")
                
        # Mark as introduced
        introduced.add(ex_id)

if errors:
    print("VALIDATION FAILED:")
    for e in errors:
        print(" -", e)
else:
    print("VALIDATION PASSED: All pedagogical dependencies are satisfied.")

print("\n--- FINAL SCHEMA PREVIEW ---")
print(json.dumps(lesson_1, indent=2))
