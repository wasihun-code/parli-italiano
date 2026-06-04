import json

base_path = "src/data/exports/workstudy/team_meeting/"
vocab = json.load(open(base_path + "workstudy_team_meeting_vocabulary.json"))
phrases = json.load(open(base_path + "workstudy_team_meeting_phrases.json"))
sentences = json.load(open(base_path + "workstudy_team_meeting_sentences.json"))

v_ids = [item['id'] for item in vocab]
p_ids = [item['id'] for item in phrases]
s_ids = [item['id'] for item in sentences]

lessons = [
    {
        "id": "l1",
        "title": "Starting the Meeting",
        "goal": "Learn how to greet and introduce the agenda.",
        "sections": [
            {"type": "vocabulary", "exerciseIds": v_ids[:45]},
            {"type": "phrase", "exerciseIds": p_ids[:7]},
            {"type": "sentence", "exerciseIds": s_ids[:7]},
            {"type": "conversation", "conversationId": "starting_the_meeting"}
        ]
    },
    {
        "id": "l2",
        "title": "Status Update",
        "goal": "Discuss project progress.",
        "sections": [
            {"type": "vocabulary", "exerciseIds": v_ids[45:90]},
            {"type": "phrase", "exerciseIds": p_ids[7:14]},
            {"type": "sentence", "exerciseIds": s_ids[7:14]},
            {"type": "conversation", "conversationId": "project_status_update"}
        ]
    },
    {
        "id": "l3",
        "title": "Brainstorming",
        "goal": "Share and discuss ideas.",
        "sections": [
            {"type": "vocabulary", "exerciseIds": v_ids[90:135]},
            {"type": "phrase", "exerciseIds": p_ids[14:21]},
            {"type": "sentence", "exerciseIds": s_ids[14:21]},
            {"type": "conversation", "conversationId": "brainstorming_ideas"}
        ]
    },
    {
        "id": "l4",
        "title": "Setting Steps",
        "goal": "Agree on next steps.",
        "sections": [
            {"type": "vocabulary", "exerciseIds": v_ids[135:180]},
            {"type": "phrase", "exerciseIds": p_ids[21:28]},
            {"type": "sentence", "exerciseIds": s_ids[21:28]},
            {"type": "conversation", "conversationId": "setting_next_steps"}
        ]
    },
    {
        "id": "l5",
        "title": "Project Review",
        "goal": "Review key project vocabulary.",
        "sections": [
            {"type": "vocabulary", "exerciseIds": v_ids[180:220]},
            {"type": "phrase", "exerciseIds": p_ids[28:34]},
            {"type": "sentence", "exerciseIds": s_ids[28:34]}
        ]
    },
    {
        "id": "l6",
        "title": "Meeting Summary",
        "goal": "Summarize everything learned.",
        "sections": [
            {"type": "vocabulary", "exerciseIds": v_ids[220:]},
            {"type": "phrase", "exerciseIds": p_ids[34:]},
            {"type": "sentence", "exerciseIds": s_ids[34:]}
        ]
    }
]

with open(base_path + "mini_lessons.json", "w") as f:
    json.dump({"lessons": lessons}, f, indent=2)
