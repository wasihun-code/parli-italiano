import json
import math

vocab_file = "src/data/exports/dining/cooking_class/dining_cooking_class_vocabulary.json"
phrases_file = "src/data/exports/dining/cooking_class/dining_cooking_class_phrases.json"
sentences_file = "src/data/exports/dining/cooking_class/dining_cooking_class_sentences.json"
conversations_file = "src/data/exports/dining/cooking_class/conversations.json"

with open(vocab_file, "r") as f:
    vocab = json.load(f)
with open(phrases_file, "r") as f:
    phrases = json.load(f)
with open(sentences_file, "r") as f:
    sentences = json.load(f)

vocab_ids = [item["id"] for item in vocab]
phrase_ids = [item["id"] for item in phrases]
sentence_ids = [item["id"] for item in sentences]

def chunk_list(lst, n):
    size = math.ceil(len(lst) / n)
    return [lst[i:i + size] for i in range(0, len(lst), size)]

vocab_chunks = chunk_list(vocab_ids, 6)
phrase_chunks = chunk_list(phrase_ids, 6)
sentence_chunks = chunk_list(sentence_ids, 6)

lessons_data = [
    {
        "id": "kitchen_basics",
        "title": "Kitchen Basics",
        "goal": "Learn the basics of the kitchen.",
        "convo": []
    },
    {
        "id": "ingredients",
        "title": "Ingredients",
        "goal": "Learn about ingredients.",
        "convo": ["starting_the_class"]
    },
    {
        "id": "making_dough",
        "title": "Making Dough",
        "goal": "Learn how to make dough.",
        "convo": ["making_pasta_dough"]
    },
    {
        "id": "cooking_steps",
        "title": "Cooking Steps",
        "goal": "Learn the cooking steps.",
        "convo": ["preparing_the_sauce"]
    },
    {
        "id": "asking_help",
        "title": "Asking Help",
        "goal": "Learn how to ask for help.",
        "convo": []
    },
    {
        "id": "final_tasting",
        "title": "Final Tasting",
        "goal": "Taste the food.",
        "convo": ["tasting_the_food"]
    }
]

lessons = []
for i, l in enumerate(lessons_data):
    sections = []
    
    if i < len(vocab_chunks) and vocab_chunks[i]:
        sections.append({
            "type": "vocabulary",
            "exerciseIds": vocab_chunks[i]
        })
    if i < len(phrase_chunks) and phrase_chunks[i]:
        sections.append({
            "type": "phrases",
            "exerciseIds": phrase_chunks[i]
        })
    if i < len(sentence_chunks) and sentence_chunks[i]:
        sections.append({
            "type": "sentences",
            "exerciseIds": sentence_chunks[i]
        })
    
    for c in l["convo"]:
        sections.append({
            "type": "conversation",
            "exerciseIds": [c]
        })
        
    lessons.append({
        "id": l["id"],
        "title": l["title"],
        "goal": l["goal"],
        "sections": sections
    })

with open("src/data/exports/dining/cooking_class/mini_lessons.json", "w") as f:
    json.dump({"lessons": lessons}, f, indent=2, ensure_ascii=False)
