import json
import os
import re

def tokenize(text):
    text = text.lower()
    text = text.replace("'", " ")
    text = re.sub(r'[^\w\sàèìòùé]', '', text)
    return [w for w in text.split() if len(w) > 2 and not w.isdigit()]

def update_scenario(slug):
    base_path = f"src/data/exports/{slug}"
    prefix = slug.replace("/", "_")
    
    with open(f"{base_path}/conversations.json", "r") as f:
        conversations = json.load(f)["conversations"]
        
    all_sentences = []
    all_phrases = []
    all_words = set()
    
    translations = {}

    for conv in conversations:
        for msg in conv["messages"]:
            it = msg["text"].strip()
            en = msg.get("english", "")
            all_sentences.append(it)
            if en: translations[it] = en
            all_words.update(tokenize(it))
            
            for choice in msg.get("choices", []):
                cit = choice["text"].strip()
                all_phrases.append(cit)
                all_words.update(tokenize(cit))

    def update_file(filename, items, id_prefix):
        path = f"{base_path}/{filename}"
        if os.path.exists(path):
            with open(path, "r") as f:
                existing = json.load(f)
        else:
            existing = []
            
        existing_it = {item["italian"] for item in existing}
        
        new_items = []
        for it in items:
            if it not in existing_it:
                new_items.append(it)
                existing_it.add(it)
        
        if not new_items:
            print(f"No new items for {filename}")
            return
            
        max_id = 0
        for item in existing:
            id_val = int(item["id"][1:])
            if id_val > max_id: max_id = id_val
            
        for i, it in enumerate(new_items):
            new_entry = {
                "id": f"{id_prefix}{max_id + i + 1}",
                "italian": it,
                "english": translations.get(it, ""),
                "audio": {"italian": f"/audio/TODO_{it[:10]}.opus"} # Placeholder
            }
            existing.append(new_entry)
            
        with open(path, "w") as f:
            json.dump(existing, f, indent=2, ensure_ascii=False)
        print(f"Added {len(new_items)} items to {filename}")

    update_file(f"{prefix}_vocabulary.json", sorted(list(all_words)), "v")
    update_file(f"{prefix}_phrases.json", all_phrases, "p")
    update_file(f"{prefix}_sentences.json", all_sentences, "s")

if __name__ == "__main__":
    update_scenario("culture/theater_evening")
