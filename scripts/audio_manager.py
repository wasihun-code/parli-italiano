import os
import json
import hashlib
import glob
from datetime import datetime

DEFAULT_VOICE_ID = "elsa"
DEFAULT_VOICE_NAME = "it-IT-ElsaNeural"

def get_audio_hash(text, voice_id=DEFAULT_VOICE_ID):
    """Generate a deterministic 12-char SHA-1 hash for text + voice."""
    # Use a separator to ensure "text" + "elsa" is different from "texte" + "lsa"
    key = f"{text.strip()}|{voice_id}"
    return hashlib.sha1(key.encode('utf-8')).hexdigest()[:12]

def get_italian_text(item):
    """Extract the primary Italian text from a corpus item."""
    if "italian" in item:
        return item["italian"].strip()
    if "correctAnswerItalian" in item:
        return item["correctAnswerItalian"].strip()
    return None

def extract_corpus_data(base_dir):
    """Scan all JSON files and extract text mapped to their categories."""
    # text -> set of categories
    text_to_categories = {}
    
    # 1. JSON Exports
    json_files = glob.glob(os.path.join(base_dir, "**/*.json"), recursive=True)
    for file_path in json_files:
        if "instruction_for_gemini.json" in file_path:
            continue
            
        parts = file_path.split(os.sep)
        try:
            exports_idx = parts.index("exports")
            category = parts[exports_idx + 1]
        except (ValueError, IndexError):
            category = "unknown"
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        # Extract main text
                        text = get_italian_text(item)
                        if text:
                            if text not in text_to_categories:
                                text_to_categories[text] = set()
                            text_to_categories[text].add(category)
                        
                        # Extract choices
                        choices = item.get("choicesItalian", [])
                        for choice in choices:
                            c_text = choice.strip()
                            if c_text:
                                if c_text not in text_to_categories:
                                    text_to_categories[c_text] = set()
                                text_to_categories[c_text].add(category)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
    # 2. Foundations (TS file)
    foundations_file = "src/data/foundations.ts"
    if os.path.exists(foundations_file):
        try:
            import re
            with open(foundations_file, "r", encoding="utf-8") as f:
                content = f.read()
            matches = re.findall(r"italian: '(.*?)'", content)
            for m in matches:
                text = m.strip()
                if text:
                    if text not in text_to_categories:
                        text_to_categories[text] = set()
                    text_to_categories[text].add("foundations")
        except Exception as e:
            print(f"Error reading foundations: {e}")

    return text_to_categories

def generate_manifest(text_to_categories, output_path):
    """Create a scalable manifest mapping text+voice to hash and tracking status."""
    manifest = {
        "metadata": {
            "last_updated": datetime.now().isoformat(),
            "default_voice": DEFAULT_VOICE_ID,
            "voice_map": {
                DEFAULT_VOICE_ID: DEFAULT_VOICE_NAME
            }
        },
        "registry": {}
    }
    
    # Load existing manifest if it exists to preserve status
    if os.path.exists(output_path):
        try:
            with open(output_path, 'r', encoding='utf-8') as f:
                old_data = json.load(f)
                # Handle migration from old flat format to new nested format
                if "registry" in old_data:
                    manifest["registry"] = old_data["registry"]
                else:
                    # Old flat structure
                    print("Migrating old flat manifest to new scalable architecture...")
                    for text, info in old_data.items():
                        # Note: Old hashes didn't include voice_id, so they will be regenerated
                        # But we preserve text as key
                        manifest["registry"][text] = {}
        except Exception as e:
            print(f"Error reading existing manifest: {e}")
            
    for text, categories in text_to_categories.items():
        if text not in manifest["registry"]:
            manifest["registry"][text] = {}
            
        # Ensure default voice entry exists
        if DEFAULT_VOICE_ID not in manifest["registry"][text]:
            h = get_audio_hash(text, DEFAULT_VOICE_ID)
            manifest["registry"][text][DEFAULT_VOICE_ID] = {
                "hash": h,
                "filename": f"{h}.opus",
                "path": f"/audio/{h}.opus",
                "status": "pending",
                "categories": sorted(list(categories))
            }
        else:
            # Update categories even if voice entry exists
            manifest["registry"][text][DEFAULT_VOICE_ID]["categories"] = sorted(list(categories))
            
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    print(f"Manifest updated with {len(manifest['registry'])} unique texts at {output_path}")
    return manifest

def inject_audio_paths(base_dir, manifest):
    """Inject audio paths into all JSON exercises based on the default voice in manifest."""
    registry = manifest["registry"]
    
    json_files = glob.glob(os.path.join(base_dir, "**/*.json"), recursive=True)
    
    for file_path in json_files:
        if "instruction_for_gemini.json" in file_path:
            continue
            
        modified = False
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if isinstance(data, list):
                for item in data:
                    text = get_italian_text(item)
                    if text and text in registry and DEFAULT_VOICE_ID in registry[text]:
                        info = registry[text][DEFAULT_VOICE_ID]
                        item["audio"] = {
                            "italian": info["path"]
                        }
                        modified = True
            
            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    BASE_DIR = "src/data/exports"
    MANIFEST_PATH = "public/audio_manifest.json"
    
    print("Step 1: Extracting corpus data and categories...")
    text_to_categories = extract_corpus_data(BASE_DIR)
    
    print("Step 2: Generating scalable manifest...")
    manifest = generate_manifest(text_to_categories, MANIFEST_PATH)
    
    print("Step 3: Injecting audio paths into corpus...")
    inject_audio_paths(BASE_DIR, manifest)
    
    print("Done!")
