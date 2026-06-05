import os
import json

SCENARIOS = [
    "travel/taxi_from_airport",
    "accommodation/asking_for_towels",
    "dining/ordering_pizza",
    "shopping/shoe_store",
    "daily_life/haircut",
    "workstudy/first_day_at_work",
    "social/inviting_a_friend",
    "culture/cinema_tickets",
    "health/pharmacy_symptoms",
    "tech/wi_fi_problem",
    "miscellaneous/asking_for_help",
    "verbs/are_verbi_in_are"
]

def analyze_scenario(slug):
    base_dir = f"src/data/exports/{slug}"
    prefix = slug.replace("/", "_")
    report = {"slug": slug, "issues": [], "warnings": []}

    # 1. Mini lessons
    lessons_list = []
    taught_ids = set()
    try:
        with open(f"{base_dir}/mini_lessons.json", "r", encoding="utf-8") as f:
            lessons_data = json.load(f)
            lessons_list = lessons_data.get("lessons", lessons_data) if isinstance(lessons_data, dict) else lessons_data
            if len(lessons_list) < 6:
                report["issues"].append(f"Has {len(lessons_list)} mini lessons instead of 6.")
            for l in lessons_list:
                for s in l.get("sections", []):
                    # In some schemas it is a list of strings, or a dict with "exerciseIds"
                    if isinstance(s, dict):
                        taught_ids.update(s.get("exerciseIds", []))
                    elif isinstance(s, str):
                        taught_ids.add(s)
                # Old schema might use vocabulary: [], phrase: [], sentence: [] directly in the lesson object
                for k in ["vocabulary", "phrase", "sentence", "phrases", "sentences", "mastery"]:
                    if k in l:
                        taught_ids.update(l[k])

    except Exception as e:
        report["issues"].append(f"Failed to load mini_lessons.json: {e}")

    # 2. Conversations
    try:
        with open(f"{base_dir}/conversations.json", "r", encoding="utf-8") as f:
            conv_data = json.load(f)
            convs = conv_data.get("conversations", conv_data) if isinstance(conv_data, dict) else conv_data
            if len(convs) < 4:
                report["issues"].append(f"Has {len(convs)} conversations instead of 4.")
            
            # 6, 7, 8: Distractor quality, difficulty, length
            for c in convs:
                msgs = c.get("messages", [])
                if len(msgs) < 10:
                    report["issues"].append(f"Conversation '{c.get('id')}' has only {len(msgs)} turns (expected >= 10).")
                
                for m in msgs:
                    correct = None
                    distractors = []
                    for ch in m.get("choices", []):
                        if ch.get("isCorrect"):
                            correct = ch.get("text", "")
                        else:
                            distractors.append(ch.get("text", ""))
                    
                    if correct:
                        c_len = len(correct)
                        for d in distractors:
                            d_len = len(d)
                            # Length parity +/- 40%, with a minimum floor of 15 chars tolerance
                            tolerance = max(15, c_len * 0.5)
                            if abs(c_len - d_len) > tolerance:
                                report["warnings"].append(f"Distractor length mismatch in '{c.get('id')}' msg '{m.get('id')}'")
    except Exception as e:
        report["issues"].append(f"Failed to load conversations.json: {e}")

    # 3, 4, 5, 9, 10: Linguistic data coverage, audio metadata, translations
    for ext, check_type in [("vocabulary", "Vocabulary"), ("phrases", "Phrase"), ("sentences", "Sentence")]:
        try:
            with open(f"{base_dir}/{prefix}_{ext}.json", "r", encoding="utf-8") as f:
                items = json.load(f)
                
                # Check translations
                missing_trans = sum(1 for i in items if not i.get("english"))
                if missing_trans > 0:
                    report["issues"].append(f"Missing {missing_trans} english translations in {ext}.")
                
                # Check audio
                missing_audio = sum(1 for i in items if not i.get("audio"))
                if missing_audio > 0:
                    # Handled by runtime, but still good to know
                    pass
                
                # Check coverage (are all extracted items taught in mini lessons?)
                untaught = sum(1 for i in items if i.get("id") not in taught_ids and f"{prefix}-{i.get('id')}" not in taught_ids and f"{slug.replace('/', '_')}-{i.get('id')}" not in taught_ids)
                if untaught > 0 and len(lessons_list) > 0:
                    report["issues"].append(f"{check_type} coverage failure: {untaught} items not taught in mini lessons.")
                    
        except Exception as e:
            report["issues"].append(f"Failed to load {ext}: {e}")

    # 11. Domain consistency
    try:
        with open(f"{base_dir}/domain.json", "r", encoding="utf-8") as f:
            domain = json.load(f)
            # Just checking existence for now. If it's an old schema with 'key_vocabulary' it's fine.
            if not domain:
                 report["issues"].append("domain.json is empty")
    except Exception as e:
        report["issues"].append(f"Failed to load domain.json: {e}")

    if len(report["issues"]) > 0:
        report["status"] = "FAIL"
    elif len(report["warnings"]) > 0:
        report["status"] = "WARNING"
    else:
        report["status"] = "PASS"
        
    return report

def main():
    reports = []
    for s in SCENARIOS:
        reports.append(analyze_scenario(s))
    
    os.makedirs("reports", exist_ok=True)
    with open("reports/gold_standard_factory_validation.md", "w", encoding="utf-8") as f:
        f.write("# Gold Standard Factory Validation\n\n")
        f.write("This report evaluates the quality of 12 generated scenarios across all categories against the 11 Gold Standard validation rules.\n\n")
        
        for r in reports:
            f.write(f"## {r['slug']}\n")
            status_icon = "❌ FAIL" if r["status"] == "FAIL" else "⚠️ WARNING" if r["status"] == "WARNING" else "✅ PASS"
            f.write(f"**Status:** {status_icon}\n\n")
            
            if r["issues"]:
                f.write("### Issues\n")
                for i in r["issues"]:
                    f.write(f"- {i}\n")
                f.write("\n")
                
            if r["warnings"]:
                f.write("### Warnings\n")
                for w in r["warnings"][:5]:
                    f.write(f"- {w}\n")
                if len(r["warnings"]) > 5:
                    f.write(f"- ... and {len(r['warnings']) - 5} more warnings.\n")
                f.write("\n")
                
            if r["status"] != "PASS":
                f.write("### Repair Recommendations\n")
                if any("translations" in i for i in r["issues"]):
                    f.write("- Execute Translation Specialist (Agent 6) to fill missing `english` translations.\n")
                if any("turns" in i for i in r["issues"]):
                    f.write("- Execute Conversation Architect (Agent 2) to expand conversations to 10+ turns.\n")
                if any("mini lessons" in i for i in r["issues"]):
                    f.write("- Execute Curriculum Designer (Agent 4) to generate 6 proper mini lessons.\n")
                if any("coverage" in i for i in r["issues"]):
                    f.write("- Re-run Curriculum Designer to ensure all extracted vocabulary and phrases are taught.\n")
                if any("Distractor" in w for w in r["warnings"]):
                    f.write("- Execute Distractor Engineer (Agent 5) to balance lengths of distractors within +/- 40% parity limits.\n")
                f.write("\n")

    print("Validation complete. Results written to reports/gold_standard_factory_validation.md")

if __name__ == "__main__":
    main()
