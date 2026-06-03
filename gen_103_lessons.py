import json

d = 'src/data/exports/tech/video_call'
v = json.load(open(d+'/tech_video_call_vocabulary.json'))
p = json.load(open(d+'/tech_video_call_phrases.json'))
s = json.load(open(d+'/tech_video_call_sentences.json'))

v_ids = [x['id'] for x in v]
p_ids = [x['id'] for x in p]
s_ids = [x['id'] for x in s]

# Divide into 6 chunks
def chunk(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)]

v_chunks = chunk(v_ids, 6)
p_chunks = chunk(p_ids, 6)
s_chunks = chunk(s_ids, 6)

titles = [
    "Video Call Basics",
    "Screen Sharing",
    "Connection Issues",
    "Presentation Tools",
    "Documents and Files",
    "Finishing the Call"
]

goals = [
    "Learn basic vocabulary and phrases for starting a video call.",
    "Learn how to share your screen and present.",
    "Handle poor connections and audio issues.",
    "Learn to present and navigate slides.",
    "Discuss and review shared documents.",
    "Learn how to conclude a video call professionally."
]

lessons = []
for i in range(6):
    lesson = {
        "id": f"l{i+1}",
        "title": titles[i],
        "goal": goals[i],
        "sections": [
            {
                "type": "vocabulary",
                "exerciseIds": v_chunks[i]
            },
            {
                "type": "phrases",
                "exerciseIds": p_chunks[i]
            },
            {
                "type": "sentences",
                "exerciseIds": s_chunks[i]
            }
        ]
    }
    lessons.append(lesson)

with open(f'{d}/mini_lessons.json', 'w') as f:
    json.dump({"lessons": lessons}, f, indent=2)

print("Generated mini_lessons.json")
