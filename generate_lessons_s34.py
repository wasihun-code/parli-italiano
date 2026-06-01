import json
import os

base_path = "src/data/exports/dining/vegetarian_meal/"
prefix = "dining_vegetarian_meal"

with open(os.path.join(base_path, f"{prefix}_vocabulary.json"), "r") as f:
    vocab = json.load(f)
with open(os.path.join(base_path, f"{prefix}_phrases.json"), "r") as f:
    phrases = json.load(f)
with open(os.path.join(base_path, f"{prefix}_sentences.json"), "r") as f:
    sentences = json.load(f)

def get_id(data, keyword):
    for item in data:
        if keyword.lower() in item["italian"].lower():
            return item["id"]
    return None

def get_ids(data, keywords):
    ids = []
    for kw in keywords:
        id_ = get_id(data, kw)
        if id_:
            ids.append(id_)
    return list(set(ids))

lessons = [
    {
        "id": "l1",
        "title": "Menu Basics",
        "goal": "Identify vegetarian and vegan options on the menu.",
        "estimatedDuration": "2 mins",
        "unlockCriteria": "none",
        "nextLesson": "l2",
        "sections": [
            {
                "type": "vocabulary",
                "title": "Core Words",
                "description": "Vegetarian and vegan vocabulary.",
                "exerciseIds": get_ids(vocab, ["vegetariani", "vegane", "menu", "piatti"])
            },
            {
                "type": "phrase",
                "title": "Asking",
                "description": "Ask about the menu.",
                "exerciseIds": get_ids(phrases, ["vegetariani", "vegane"])
            },
            {
                "type": "sentence",
                "title": "Ordering",
                "description": "Basic ordering.",
                "exerciseIds": get_ids(sentences, ["vegetariani", "vegane"])[:3]
            }
        ]
    },
    {
        "id": "l2",
        "title": "Substitutions",
        "goal": "Request changes and plant-based alternatives.",
        "estimatedDuration": "2 mins",
        "unlockCriteria": "complete_previous",
        "nextLesson": "l3",
        "sections": [
            {
                "type": "vocabulary",
                "title": "Alternatives",
                "description": "Milk and dairy alternatives.",
                "exerciseIds": get_ids(vocab, ["soia", "avena", "latte", "senza", "formaggio"])
            },
            {
                "type": "phrase",
                "title": "Modifying",
                "description": "How to ask for changes.",
                "exerciseIds": get_ids(phrases, ["senza", "soia"])
            },
            {
                "type": "sentence",
                "title": "Requests",
                "description": "Order with substitutions.",
                "exerciseIds": get_ids(sentences, ["senza", "latte"])[:3]
            }
        ]
    },
    {
        "id": "l3",
        "title": "Broth & Stocks",
        "goal": "Ask about hidden animal products in dishes.",
        "estimatedDuration": "2 mins",
        "unlockCriteria": "complete_previous",
        "nextLesson": "l4",
        "sections": [
            {
                "type": "vocabulary",
                "title": "Ingredients",
                "description": "Words for broths and meat.",
                "exerciseIds": get_ids(vocab, ["brodo", "carne", "pesce", "pollo"])
            },
            {
                "type": "phrase",
                "title": "Checking",
                "description": "Verify ingredients.",
                "exerciseIds": get_ids(phrases, ["brodo", "carne"])
            },
            {
                "type": "sentence",
                "title": "Verification",
                "description": "Ask the waiter for details.",
                "exerciseIds": get_ids(sentences, ["brodo", "carne", "pesce"])[:3]
            }
        ]
    },
    {
        "id": "l4",
        "title": "Dessert Choices",
        "goal": "Check for eggs and dairy in desserts.",
        "estimatedDuration": "2 mins",
        "unlockCriteria": "complete_previous",
        "nextLesson": "none",
        "sections": [
            {
                "type": "vocabulary",
                "title": "Sweets",
                "description": "Dessert-related terms.",
                "exerciseIds": get_ids(vocab, ["dolce", "uova", "sorbetto", "frutta"])
            },
            {
                "type": "phrase",
                "title": "Sweet Check",
                "description": "Ask about eggs in desserts.",
                "exerciseIds": get_ids(phrases, ["uova", "sorbetto"])
            },
            {
                "type": "sentence",
                "title": "Final Order",
                "description": "Finish your meal.",
                "exerciseIds": get_ids(sentences, ["uova", "sorbetto", "dolci"])[:3]
            }
        ]
    }
]

with open(os.path.join(base_path, "mini_lessons.json"), "w", encoding="utf-8") as f:
    json.dump({"lessons": lessons}, f, indent=2, ensure_ascii=False)
