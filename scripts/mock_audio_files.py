import json
import os
import sys

def main(scenario_slug):
    base_path = f"src/data/exports/{scenario_slug}"
    parts = scenario_slug.split('/')
    prefix = "_".join(parts)
    
    files = [
        os.path.join(base_path, f"{prefix}_vocabulary.json"),
        os.path.join(base_path, f"{prefix}_phrases.json"),
        os.path.join(base_path, f"{prefix}_sentences.json"),
        os.path.join(base_path, "conversations.json")
    ]
    
    audio_dir = "public/audio"
    os.makedirs(audio_dir, exist_ok=True)
    
    count = 0
    for fpath in files:
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except: continue
        
        # Determine if it's conversation or curriculum
        items = data if isinstance(data, list) else data.get("conversations", [])
        
        def mock_path(path):
            nonlocal count
            if not path: return
            full_path = os.path.join("public", path.lstrip("/"))
            if not os.path.exists(full_path):
                with open(full_path, "w") as f:
                    f.write("mock audio")
                count += 1

        if isinstance(data, list):
            for item in items:
                mock_path(item.get("audio", {}).get("italian"))
        else:
            for conv in items:
                for msg in conv.get("messages", []):
                    mock_path(msg.get("audio", {}).get("italian"))
                    mock_path(msg.get("audioPath"))
                    for choice in msg.get("choices", []):
                        mock_path(choice.get("audioPath"))

    print(f"Mocked {count} audio files for {scenario_slug}.")
    return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else None
    if not slug: sys.exit(1)
    sys.exit(0 if main(slug) else 1)
