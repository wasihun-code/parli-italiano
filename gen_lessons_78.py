import json

def generate_lessons():
    v_ids = [f"v{i}" for i in range(1, 323)]
    p_ids = [f"p{i}" for i in range(1, 41)]
    s_ids = [f"s{i}" for i in range(1, 41)]

    # Distribute sequentially but we will assign themes
    # 322/6 = 53.6 -> 54, 54, 54, 54, 54, 52
    v_chunks = [v_ids[i:i + 54] for i in range(0, 324, 54)]
    # 40/6 = 6.6 -> 7, 7, 7, 7, 6, 6
    p_chunks = [p_ids[0:7], p_ids[7:14], p_ids[14:21], p_ids[21:28], p_ids[28:34], p_ids[34:40]]
    s_chunks = [s_ids[0:7], s_ids[7:14], s_ids[14:21], s_ids[21:28], s_ids[28:34], s_ids[34:40]]

    lesson_data = [
        ("l1", "Style & Fashion", "Learn to compliment clothes and style."),
        ("l2", "Work & Achievement", "Praise a colleague's professional success."),
        ("l3", "Food & Cooking", "Express appreciation for a delicious meal."),
        ("l4", "Personality & Traits", "Compliment someone's character and smile."),
        ("l5", "Accepting Praise", "Respond graciously to a nice compliment."),
        ("l6", "Friendship & Support", "Recognize friendship and great teamwork.")
    ]

    lessons = []
    for i in range(6):
        lid, title, goal = lesson_data[i]
        lesson = {
            "id": lid,
            "title": title,
            "goal": goal,
            "sections": [
                {
                    "type": "vocabulary",
                    "exerciseIds": v_chunks[i]
                },
                {
                    "type": "phrase",
                    "exerciseIds": p_chunks[i]
                },
                {
                    "type": "sentence",
                    "exerciseIds": s_chunks[i]
                },
                {
                    "type": "mastery",
                    "exerciseIds": s_chunks[i]
                }
            ]
        }
        lessons.append(lesson)

    output = {
        "lessons": lessons
    }

    with open("src/data/exports/social/compliments/mini_lessons.json", "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    generate_lessons()
    print("mini_lessons.json generated successfully.")
