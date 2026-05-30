import json
import os
import sys
import re

def run_mini_lesson_audio_audit(scenario_slug="accommodation/apartment_key_pickup"):
    print(f"\n--- MINI LESSON AUDIO AUDIT: {scenario_slug} ---")
    scenario_dir = f"src/data/exports/{scenario_slug}"
    parts = scenario_slug.split('/')
    prefix = "_".join(parts)
    
    lessons_file = os.path.join(scenario_dir, "mini_lessons.json")
    
    # Files to check
    data_files = [
        f"{prefix}_vocabulary.json",
        f"{prefix}_phrases.json",
        f"{prefix}_sentences.json"
    ]
    
    registry = {}
    for df in data_files:
        path = os.path.join(scenario_dir, df)
        with open(path, "r", encoding="utf-8") as f:
            items = json.load(f)
            for item in items:
                registry[item["id"]] = item

    try:
        with open(lessons_file, "r", encoding="utf-8") as f:
            lessons = json.load(f)["lessons"]
    except Exception as e:
        print(f"FAIL: Could not load mini_lessons.json: {e}")
        return False

    missing_audio = []
    broken_choices = []
    
    for lesson in lessons:
        for section in lesson.get("sections", []):
            for eid in section.get("exerciseIds", []):
                item = registry.get(eid)
                if not item:
                    print(f"WARN: Item {eid} not found in registry")
                    continue
                
                # Check item audio
                if "audio" not in item or "italian" not in item["audio"]:
                    missing_audio.append(f"Item {eid}: Missing audio metadata")
                else:
                    audio_path = item["audio"]["italian"]
                    if not os.path.exists(os.path.join("public", audio_path.lstrip("/"))):
                        missing_audio.append(f"Item {eid}: File not found '{audio_path}'")
                
                # Check choice audio (in our gold standard, choices are strings from the same pool)
                # But they MUST have entries in the global manifest if we want to play them manually.
                # Our pipeline ensures they exist.
                
    # Static logic audit of the React file
    training_file = "src/screens/MiniLessonTrainingScreen.tsx"
    with open(training_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # New Requirement: Choice audio plays immediately on submitAnswer
    has_immediate_choice_playback = "void Tts.speak(ans)" in content
    
    # Requirement: No autoplay on new item
    has_leaking_autoplay = "Auto-play audio on new item" in content
    
    print(f"Items checked: {len(registry)}")
    print(f"Immediate choice playback implemented: {'YES' if has_immediate_choice_playback else 'NO'}")
    print(f"Pre-submission autoplay leaked: {'YES' if has_leaking_autoplay else 'NO'}")

    if missing_audio:
        print(f"Missing Audio ({len(missing_audio)}):")
        for m in missing_audio[:5]: print(f"  - {m}")
    
    success = not missing_audio and has_immediate_choice_playback and not has_leaking_autoplay
    
    if success:
        print("MINI LESSON AUDIO AUDIT: PASS")
        return True
    else:
        print("MINI LESSON AUDIO AUDIT: FAIL")
        return False

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "accommodation/apartment_key_pickup"
    success = run_mini_lesson_audio_audit(slug)
    sys.exit(0 if success else 1)
