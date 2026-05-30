import json
import os
import sys
import hashlib

MANIFEST_PATH = "public/audio_manifest.json"

def get_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()[:8]

def main(scenario_slug):
    base_path = f"src/data/exports/{scenario_slug}"
    parts = scenario_slug.split('/')
    prefix = "_".join(parts)
    
    files = [
        os.path.join(base_path, f"{prefix}_vocabulary.json"),
        os.path.join(base_path, f"{prefix}_phrases.json"),
        os.path.join(base_path, f"{prefix}_sentences.json")
    ]
    
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    
    registry = manifest["registry"]
    
    # We use 'isabella' for general extraction
    voice_id = "isabella"
    
    new_items_count = 0
    
    for fpath in files:
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                items = json.load(f)
        except: continue
        
        for item in items:
            text = item["italian"]
            
            # Choice audio too
            choices = item.get("choicesItalian", [])
            all_text = [text] + choices
            
            for t in all_text:
                if t not in registry:
                    registry[t] = {}
                
                if voice_id not in registry[t]:
                    filename = f"it_{get_hash(t)}_{voice_id}.opus"
                    registry[t][voice_id] = {
                        "filename": filename,
                        "status": "pending",
                        "categories": [parts[0], scenario_slug]
                    }
                    new_items_count += 1
                
                # Update item path in JSON to match manifest filename
                # Actually, our JSON uses /audio/{text}.opus which is wrong for the manifest system.
                # Let's fix the JSON paths to use the hash-based filename.
                
    # Save manifest
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
        
    # Re-run extractor/path fixer to sync JSON files with manifest
    for fpath in files:
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                items = json.load(f)
        except: continue
        
        for item in items:
            text = item["italian"]
            filename = registry[text][voice_id]["filename"]
            item["audio"] = {"italian": f"/audio/{filename}"}
            
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)

    print(f"Updated manifest and curriculum paths for {scenario_slug}. Added {new_items_count} pending items.")
    return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else None
    if not slug: sys.exit(1)
    sys.exit(0 if main(slug) else 1)
