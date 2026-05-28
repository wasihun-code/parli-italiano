import os
import json
import glob

BASE_DIR = "src/data/exports"
MANIFEST_PATH = "public/audio_manifest.json"
AUDIO_DIR = "public/audio"

def get_italian_text(item):
    """Extract the primary Italian text from a corpus item."""
    if "italian" in item:
        return item["italian"].strip()
    if "correctAnswerItalian" in item:
        return item["correctAnswerItalian"].strip()
    return None

def validate():
    print("--- Audio Infrastructure Validation ---")
    errors = []
    
    # 1. Load manifest
    if not os.path.exists(MANIFEST_PATH):
        print("FAIL: Manifest not found.")
        return
        
    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        manifest = json.load(f)
    
    registry = manifest.get("registry", {})
    default_voice = manifest.get("metadata", {}).get("default_voice", "elsa")
    
    # 2. Check manifest vs disk
    for text, voices in registry.items():
        for voice_id, info in voices.items():
            if info["status"] == "completed":
                filename = info["filename"]
                if not os.path.exists(os.path.join(AUDIO_DIR, filename)):
                    errors.append(f"Missing file for completed manifest item: {filename} ({text[:20]}...)")
            
    # 3. Check corpus vs manifest
    json_files = glob.glob(os.path.join(BASE_DIR, "**/*.json"), recursive=True)
    unique_corpus_text = set()
    total_exercises = 0
    
    for file_path in json_files:
        if "instruction_for_gemini.json" in file_path:
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        text = get_italian_text(item)
                        if text:
                            unique_corpus_text.add(text)
                            total_exercises += 1
                            
                            # Check if audio field exists
                            if "audio" not in item:
                                errors.append(f"Missing audio field in {file_path}: {text[:20]}...")
                            elif "italian" not in item["audio"]:
                                errors.append(f"Missing audio.italian field in {file_path}: {text[:20]}...")
                            else:
                                audio_path = item["audio"]["italian"]
                                
                                # Verify against manifest
                                if text not in registry:
                                    errors.append(f"Text in corpus missing from manifest: {text[:20]}...")
                                elif default_voice not in registry[text]:
                                    errors.append(f"Default voice '{default_voice}' missing for text: {text[:20]}...")
                                else:
                                    info = registry[text][default_voice]
                                    expected_path = info["path"]
                                    if audio_path != expected_path:
                                        errors.append(f"Incorrect audio path in {file_path}: found {audio_path}, expected {expected_path}")
        except Exception as e:
            errors.append(f"Error reading {file_path}: {e}")
            
    # Summary
    print(f"Total exercises processed: {total_exercises}")
    print(f"Total unique texts in corpus: {len(unique_corpus_text)}")
    print(f"Total manifest registry entries: {len(registry)}")
    print(f"Total audio files on disk: {len(os.listdir(AUDIO_DIR)) if os.path.exists(AUDIO_DIR) else 0}")
    
    if errors:
        print(f"\nFound {len(errors)} errors:")
        for error in errors[:20]: # Show first 20 errors
            print(f"- {error}")
        if len(errors) > 20:
            print(f"... and {len(errors) - 20} more.")
    else:
        print("\nSUCCESS: All validations passed!")

if __name__ == "__main__":
    validate()
