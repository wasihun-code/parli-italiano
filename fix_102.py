import json
import os

path = "src/data/exports/tech/using_a_map_app"

# Fix mini_lessons.json
with open(f"{path}/mini_lessons.json", "r") as f:
    data = json.load(f)

for i, lesson in enumerate(data.get("lessons", [])):
    lesson["id"] = f"l{i+1}"
    if "goal" not in lesson:
        lesson["goal"] = f"Master {lesson.get('title', 'this topic')}"
    for section in lesson.get("sections", []):
        if "items" in section:
            section["exerciseIds"] = section.pop("items")

with open(f"{path}/mini_lessons.json", "w") as f:
    json.dump(data, f, indent=2)

# Fix translations
def fix_translations(filename):
    filepath = f"{path}/{filename}"
    if not os.path.exists(filepath):
        return
    with open(filepath, "r") as f:
        content = json.load(f)
    
    # Vocabulary, phrases, sentences usually have: "id", "italian", "english"
    # and maybe some missing english translations
    for item in content:
        if "english" not in item or not item["english"] or item["english"].strip() == "":
            # Basic translation logic or placeholder (but instruction says Fill ALL missing translations, 100% coverage, ensure high quality).
            # Actually, I should check what is missing first.
            pass

fix_translations("tech_using_a_map_app_vocabulary.json")
