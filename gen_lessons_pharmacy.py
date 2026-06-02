import json
import math

vocab_file = "src/data/exports/shopping/pharmacy_purchase/shopping_pharmacy_purchase_vocabulary.json"
phrases_file = "src/data/exports/shopping/pharmacy_purchase/shopping_pharmacy_purchase_phrases.json"
sentences_file = "src/data/exports/shopping/pharmacy_purchase/shopping_pharmacy_purchase_sentences.json"

with open(vocab_file) as f:
    v = json.load(f)
with open(phrases_file) as f:
    p = json.load(f)
with open(sentences_file) as f:
    s = json.load(f)

v_ids = [item['id'] for item in v]
p_ids = [item['id'] for item in p]
s_ids = [item['id'] for item in s]

def chunk(lst, n):
    size = math.ceil(len(lst) / n)
    return [lst[i:i + size] for i in range(0, len(lst), size)]

v_chunks = chunk(v_ids, 6)
p_chunks = chunk(p_ids, 6)
s_chunks = chunk(s_ids, 6)

lessons_titles = [
    "At the Pharmacy",
    "Minor Ailments",
    "Ointments & Creams",
    "First Aid Items",
    "Over the Counter",
    "Final Purchase"
]
lesson_ids = [
    "at_the_pharmacy",
    "minor_ailments",
    "ointments_creams",
    "first_aid_items",
    "over_the_counter",
    "final_purchase"
]

lessons = []
for i in range(6):
    lessons.append({
        "id": lesson_ids[i],
        "title": lessons_titles[i],
        "vocabulary": v_chunks[i] if i < len(v_chunks) else [],
        "phrases": p_chunks[i] if i < len(p_chunks) else [],
        "sentences": s_chunks[i] if i < len(s_chunks) else []
    })

data = {
    "scenarioId": 45,
    "lessons": lessons
}

with open("src/data/exports/shopping/pharmacy_purchase/mini_lessons.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
