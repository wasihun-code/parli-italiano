import json
import os

def fill_translations(slug):
    base_path = f"src/data/exports/{slug}"
    parts = slug.split('/')
    prefix = "_".join(parts)
    
    conv_path = os.path.join(base_path, "conversations.json")
    with open(conv_path, "r", encoding="utf-8") as f:
        conversations = json.load(f)["conversations"]
        
    translations = {}
    for conv in conversations:
        for msg in conv.get("messages", []):
            it = msg["text"].strip()
            if msg.get("english"):
                translations[it] = msg["english"]
            for choice in msg.get("choices", []):
                it_c = choice["text"].strip()
                if choice.get("english"):
                    translations[it_c] = choice["english"]

    # Vocabulary is harder because it's single words. 
    # Let's try to find them in conversations if possible, but mostly I'll have to provide them.
    # Actually, for words, I'll use a predefined dictionary for common words and then AI for others.
    
    # Files to update
    files = [
        f"{prefix}_vocabulary.json",
        f"{prefix}_phrases.json",
        f"{prefix}_sentences.json"
    ]
    
    for fname in files:
        fpath = os.path.join(base_path, fname)
        if not os.path.exists(fpath): continue
        
        with open(fpath, "r", encoding="utf-8") as f:
            items = json.load(f)
            
        updated = False
        for item in items:
            if not item.get("english") or item["english"] == "":
                it = item["italian"].strip()
                if it in translations:
                    item["english"] = translations[it]
                    updated = True
                else:
                    # Manual/AI translation for remaining
                    # I'll fill them with a placeholder or actual translation if I can.
                    pass
        
        if updated:
            with open(fpath, "w", encoding="utf-8") as f:
                json.dump(items, f, indent=2, ensure_ascii=False)
            print(f"Updated {fname}")

if __name__ == "__main__":
    fill_translations("travel/buying_ferry_tickets")
