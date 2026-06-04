import json
import os

lessons_data = {
  "scenarioId": 65,
  "lessons": [
    {
      "id": "l1",
      "title": "Welcome and Syllabus",
      "description": "Learn the basics of asking about a course and reading the syllabus.",
      "objectives": [
        "Ask about the syllabus",
        "Understand course requirements"
      ],
      "exercises": [
        {
          "type": "vocabulary",
          "items": ["v1", "v2", "v3", "v4"]
        },
        {
          "type": "phrase",
          "items": ["p1", "p2"]
        }
      ]
    },
    {
      "id": "l2",
      "title": "Asking Questions in Class",
      "description": "Learn how to ask a professor for clarification.",
      "objectives": [
        "Ask questions to the professor",
        "Understand classroom terms"
      ],
      "exercises": [
        {
          "type": "vocabulary",
          "items": ["v5", "v6", "v7", "v8"]
        },
        {
          "type": "phrase",
          "items": ["p3", "p4"]
        }
      ]
    },
    {
      "id": "l3",
      "title": "The University Library",
      "description": "Learn terms related to studying and library use.",
      "objectives": [
        "Talk about library and studying",
        "Make study plans"
      ],
      "exercises": [
        {
          "type": "vocabulary",
          "items": ["v9", "v10", "v11", "v12"]
        },
        {
          "type": "sentence",
          "items": ["s1", "s2"]
        }
      ]
    },
    {
      "id": "l4",
      "title": "Borrowing Notes",
      "description": "Learn how to borrow notes from a classmate.",
      "objectives": [
        "Borrow notes",
        "Explain an absence"
      ],
      "exercises": [
        {
          "type": "vocabulary",
          "items": ["v13", "v14", "v15", "v16"]
        },
        {
          "type": "sentence",
          "items": ["s3", "s4"]
        }
      ]
    },
    {
      "id": "l5",
      "title": "Exam Dates",
      "description": "Learn how to ask the secretariat about exam schedules.",
      "objectives": [
        "Ask for exam dates",
        "Talk to secretariat"
      ],
      "exercises": [
        {
          "type": "vocabulary",
          "items": ["v17", "v18", "v19", "v20"]
        },
        {
          "type": "sentence",
          "items": ["s5", "s6"]
        }
      ]
    },
    {
      "id": "l6",
      "title": "Scholarship Info",
      "description": "Learn how to ask about financial aid and registration.",
      "objectives": [
        "Ask about scholarship",
        "Understand registration deadlines"
      ],
      "exercises": [
        {
          "type": "vocabulary",
          "items": ["v21", "v22", "v23", "v24"]
        },
        {
          "type": "phrase",
          "items": ["p5", "p6"]
        }
      ]
    }
  ]
}

os.makedirs('src/data/exports/workstudy/university_class', exist_ok=True)
with open('src/data/exports/workstudy/university_class/mini_lessons.json', 'w') as f:
    json.dump(lessons_data, f, indent=2)

print("Created mini_lessons.json")
