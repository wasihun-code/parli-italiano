import json

def fix_lessons():
    path = "src/data/exports/travel/lost_in_a_city/mini_lessons.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    new_lessons = []
    goals = [
        "Learn how to admit you are lost and ask for help.",
        "Identify and use city landmarks to orient yourself.",
        "Master asking for directions to specific places like hotels.",
        "Understand and confirm basic direction instructions.",
        "Learn how to find useful services like the post office.",
        "Master getting maps and info from the tourist office."
    ]

    for i, lesson in enumerate(data["lessons"]):
        new_lesson = {
            "id": lesson["id"],
            "title": lesson["title"],
            "goal": goals[i],
            "sections": []
        }
        for section in lesson["sections"]:
            new_section = {
                "type": section["type"],
                "exerciseIds": section["exerciseIds"]
            }
            new_lesson["sections"].append(new_section)
        new_lessons.append(new_lesson)

    new_data = {"lessons": new_lessons}
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(new_data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    fix_lessons()
