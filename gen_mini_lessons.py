import json

file_path = '/home/waseageru/parli-italiano/src/data/exports/culture/art_gallery/mini_lessons.json'

scenario_id = 86
prefix = f"s{scenario_id}"

num_vocab = 275
num_phrases = 40
num_sentences = 40

vocab_per_lesson = num_vocab // 6
phrases_per_lesson = num_phrases // 6
sentences_per_lesson = num_sentences // 6

goals = [
    "Buying a Ticket",
    "Learning about the Artist",
    "Discussing Art Styles",
    "Art Materials",
    "Gallery Rules",
    "Art Appreciation"
]

lessons = []

for i in range(6):
    lesson_id = f"l{i+1}"
    
    v_start = i * vocab_per_lesson + 1
    v_end = (i + 1) * vocab_per_lesson if i < 5 else num_vocab
    
    p_start = i * phrases_per_lesson + 1
    p_end = (i + 1) * phrases_per_lesson if i < 5 else num_phrases
    
    s_start = i * sentences_per_lesson + 1
    s_end = (i + 1) * sentences_per_lesson if i < 5 else num_sentences
    
    lesson = {
        "id": lesson_id,
        "title": f"Lesson {i+1}",
        "goal": goals[i],
        "estimatedDuration": "3 mins",
        "unlockCriteria": "none" if i == 0 else "complete_previous",
        "nextLesson": f"l{i+2}" if i < 5 else None,
        "sections": [
            {
                "type": "vocabulary",
                "title": "Learn the Words",
                "description": "Essential vocabulary.",
                "exerciseIds": [f"{prefix}-v{j}" for j in range(v_start, v_end + 1)]
            },
            {
                "type": "phrase",
                "title": "Build the Phrases",
                "description": "Useful phrases.",
                "exerciseIds": [f"{prefix}-p{j}" for j in range(p_start, p_end + 1)]
            },
            {
                "type": "sentence",
                "title": "Practice the Dialogue",
                "description": "Sentences from the host.",
                "exerciseIds": [f"{prefix}-s{j}" for j in range(s_start, s_end + 1)]
            },
            {
                "type": "mastery",
                "title": "Mastery Check",
                "description": "Prove your skills.",
                "exerciseIds": [f"{prefix}-s{s_end}"]
            }
        ]
    }
    lessons.append(lesson)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump({"lessons": lessons}, f, indent=2, ensure_ascii=False)
