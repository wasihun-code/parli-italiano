import json

words = [f"v{i}" for i in range(1, 128)]
phrases = [f"p{i}" for i in range(1, 21)]
sentences = [f"s{i}" for i in range(1, 41)]

def chunk(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)]

w_chunks = chunk(words, 6)
p_chunks = chunk(phrases, 6)
s_chunks = chunk(sentences, 6)

lessons = []
titles = ['At the Station', 'Reporting a Theft', 'Lost Items', 'Describing Items', 'Contact Info', 'Final Steps']

for i in range(6):
    l_id = f"l{i+1}"
    n_id = f"l{i+2}" if i < 5 else None
    crit = "none" if i == 0 else "complete_previous"
    
    sections = [
        {
            "type": "vocabulary",
            "title": "Learn the Words",
            "description": "Essential vocabulary.",
            "exerciseIds": w_chunks[i]
        },
        {
            "type": "phrase",
            "title": "Build the Phrases",
            "description": "Useful phrases.",
            "exerciseIds": p_chunks[i]
        },
        {
            "type": "sentence",
            "title": "Practice the Dialogue",
            "description": "Sentences from the host.",
            "exerciseIds": s_chunks[i]
        },
        {
            "type": "mastery",
            "title": "Mastery Check",
            "description": "Prove your skills.",
            "exerciseIds": [s_chunks[i][-1]] if s_chunks[i] else []
        }
    ]
    
    lessons.append({
        "id": l_id,
        "title": f"Lesson {i+1}",
        "goal": titles[i],
        "estimatedDuration": "3 mins",
        "unlockCriteria": crit,
        "nextLesson": n_id,
        "sections": sections
    })

with open("src/data/exports/miscellaneous/police_report/mini_lessons.json", "w") as f:
    json.dump({"lessons": lessons}, f, indent=2)
