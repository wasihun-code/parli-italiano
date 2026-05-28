import os
import json
import hashlib
import glob
import subprocess
import re
import concurrent.futures

# Configuration
BASE_DIR = "src/data/exports"
FOUNDATIONS_FILE = "src/data/foundations.ts"
MANIFEST_PATH = "public/audio_manifest.json"
AUDIO_DIR = "public/audio"
VOICE_ID = "elsa"

def get_audio_hash(text, voice_id=VOICE_ID):
    key = f"{text.strip()}|{voice_id}"
    return hashlib.sha1(key.encode('utf-8')).hexdigest()[:12]

def validate_media(file_path):
    """Programmatically validate browser-compatible decoding using ffprobe."""
    if not os.path.exists(file_path):
        return False, "File does not exist"
    
    try:
        # Run ffprobe to check if it's a valid Ogg/Opus container and has duration
        cmd = [
            "ffprobe", "-v", "error", 
            "-show_entries", "format=duration:stream=codec_name", 
            "-of", "json", file_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            return False, f"ffprobe error: {result.stderr.strip()}"
        
        info = json.loads(result.stdout)
        if not info.get("format") or not info["format"].get("duration"):
            return False, "Missing duration in media headers"
        
        duration = float(info["format"]["duration"])
        if duration <= 0:
            return False, f"Zero duration: {duration}"
            
        streams = info.get("streams", [])
        if not any(s.get("codec_name") == "opus" for s in streams):
            return False, "No Opus stream found in file"
            
        return True, "Valid"
    except Exception as e:
        return False, str(e)

def extract_from_foundations():
    texts = set()
    if os.path.exists(FOUNDATIONS_FILE):
        with open(FOUNDATIONS_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        matches = re.findall(r"italian: '(.*?)'", content)
        for m in matches:
            texts.add(m.strip())
    return texts

def run_audit():
    report = {
        "global_integrity": "Pending",
        "total_exercises_checked": 0,
        "total_unique_texts": 0,
        "missing_assets": [],
        "corrupted_assets": [],
        "orphaned_files": [],
        "orphaned_manifest_entries": [],
        "schema_inconsistencies": [],
        "coverage": {},
        "real_coverage_percentage": 0.0,
        "manifest_consistency": "Ok"
    }
    
    # 1. Load manifest
    if not os.path.exists(MANIFEST_PATH):
        report["manifest_consistency"] = "Manifest missing"
        return report
        
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    registry = manifest.get("registry", {})
    
    # 2. Extract all texts from corpus
    all_texts = set()
    exercise_to_asset = {} # id -> asset_path
    
    # JSON exports
    json_files = glob.glob(os.path.join(BASE_DIR, "**/*.json"), recursive=True)
    for file_path in json_files:
        if "instruction_for_gemini.json" in file_path: continue
        
        category = file_path.split(os.sep)[3] # exports/<category>/...
        if category not in report["coverage"]:
            report["coverage"][category] = {"total": 0, "playable": 0}
            
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            for item in data:
                report["total_exercises_checked"] += 1
                report["coverage"][category]["total"] += 1
                
                # Main text
                it = item.get("italian") or item.get("correctAnswerItalian")
                it_id = item.get("id", "unknown")
                
                if not it:
                    report["schema_inconsistencies"].append(f"Missing italian text in {file_path} id: {it_id}")
                    continue
                
                all_texts.add(it.strip())
                
                # Check choices/distractors
                choices = item.get("choicesItalian", [])
                for c in choices:
                    all_texts.add(c.strip())
                
                # Audio field check
                audio = item.get("audio")
                if not audio:
                    # report["schema_inconsistencies"].append(f"Missing audio field in {file_path} id: {it_id}")
                    pass # We have deterministic fallback, so not strictly an error if text exists
                elif isinstance(audio, str):
                    if not audio.startswith("/audio/"):
                        report["schema_inconsistencies"].append(f"Legacy audio string invalid format in {it_id}: {audio}")
                elif isinstance(audio, dict):
                    if "italian" not in audio:
                        report["schema_inconsistencies"].append(f"Production audio object missing 'italian' in {it_id}")
                else:
                    report["schema_inconsistencies"].append(f"Malformed audio field type in {it_id}: {type(audio)}")

        except Exception as e:
            report["global_integrity"] = f"Error reading {file_path}: {str(e)}"
            
    # Foundations
    found_texts = extract_from_foundations()
    if "foundations" not in report["coverage"]:
        report["coverage"]["foundations"] = {"total": 0, "playable": 0}
    for t in found_texts:
        all_texts.add(t)
        report["coverage"]["foundations"]["total"] += 1
        report["total_exercises_checked"] += 1
        
    report["total_unique_texts"] = len(all_texts)
    
    # 3. Validate Assets
    asset_status = {} # path -> (valid, message)
    
    def check_asset(text):
        h = get_audio_hash(text)
        filename = f"{h}.opus"
        path = os.path.join(AUDIO_DIR, filename)
        
        if not os.path.exists(path):
            return text, (False, "Missing")
        
        valid, msg = validate_media(path)
        return text, (valid, msg)

    print(f"Auditing {len(all_texts)} unique audio assets...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_text = {executor.submit(check_asset, t): t for t in all_texts}
        for future in concurrent.futures.as_completed(future_to_text):
            text, result = future.result()
            asset_status[text] = result

    # 4. Compile Asset Reports
    for text, (valid, msg) in asset_status.items():
        h = get_audio_hash(text)
        filename = f"{h}.opus"
        
        if msg == "Missing":
            report["missing_assets"].append({"text": text, "hash": h, "filename": filename})
        elif not valid:
            report["corrupted_assets"].append({"text": text, "hash": h, "filename": filename, "error": msg})
            
    # Update playable counts
    # We need to re-scan categories to map text to category
    for file_path in json_files:
        if "instruction_for_gemini.json" in file_path: continue
        category = file_path.split(os.sep)[3]
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for item in data:
                it = item.get("italian") or item.get("correctAnswerItalian")
                if it and asset_status.get(it.strip(), (False,))[0]:
                    report["coverage"][category]["playable"] += 1
        except: pass
        
    for t in found_texts:
        if asset_status.get(t, (False,))[0]:
            report["coverage"]["foundations"]["playable"] += 1

    # 5. Orphan Checks
    disk_files = set(os.listdir(AUDIO_DIR))
    referenced_files = set(f"{get_audio_hash(t)}.opus" for t in all_texts)
    
    orphans = disk_files - referenced_files
    report["orphaned_files"] = sorted(list(orphans))
    
    # Manifest orphans
    manifest_referenced = set()
    for text, voices in registry.items():
        for v, info in voices.items():
            manifest_referenced.add(info["filename"])
            if info["filename"] not in disk_files and info["status"] == "completed":
                report["orphaned_manifest_entries"].append({"text": text, "file": info["filename"]})

    # 6. Final Tally
    total_playable = sum(c["playable"] for c in report["coverage"].values())
    total_exercises = sum(c["total"] for c in report["coverage"].values())
    if total_exercises > 0:
        report["real_coverage_percentage"] = (total_playable / total_exercises) * 100
        
    if not report["missing_assets"] and not report["corrupted_assets"]:
        report["global_integrity"] = "Pass"
    else:
        report["global_integrity"] = "Fail"

    # Save artifact
    with open("scripts/audio_audit_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
        
    return report

if __name__ == "__main__":
    run_audit()
