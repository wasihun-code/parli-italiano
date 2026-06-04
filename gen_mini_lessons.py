import json
import math

vocab_count = 349
phrase_count = 40
sentence_count = 40

def chunk_ids(prefix, total, chunks=6):
    res = []
    base = total // chunks
    rem = total % chunks
    start = 1
    for i in range(chunks):
        count = base + (1 if i < rem else 0)
        res.append([f"{prefix}{x}" for x in range(start, start + count)])
        start += count
    return res

v_chunks = chunk_ids("v", vocab_count)
p_chunks = chunk_ids("p", phrase_count)
s_chunks = chunk_ids("s", sentence_count)

lessons = []
titles = ["Experience", "Skills", "Company", "Motivation", "Next Steps", "Conclusion"]

for i in range(6):
    lessons.append({
        "id": f"l{i+1}",
        "title": titles[i],
        "goal": f"Master part {i+1} of the interview.",
        "sections": [
            {"type": "vocabulary", "exerciseIds": v_chunks[i]},
            {"type": "phrase", "exerciseIds": p_chunks[i]},
            {"type": "sentence", "exerciseIds": s_chunks[i]},
            {"type": "mastery", "exerciseIds": s_chunks[i]}
        ]
    })

data = {"lessons": lessons}
with open("/home/waseageru/parli-italiano/src/data/exports/workstudy/job_interview/mini_lessons.json", "w") as f:
    json.dump(data, f, indent=2)

print("mini_lessons.json written.")
