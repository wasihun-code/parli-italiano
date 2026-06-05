import os
import json

SCENARIOS = [
    "travel/taxi_from_airport",
    "daily_life/haircut",
    "social/inviting_a_friend",
    "culture/cinema_tickets",
    "tech/wi_fi_problem",
    "verbs/are_verbi_in_are"
]

def analyze_forensics(slug):
    base_dir = f"src/data/exports/{slug}"
    prefix = slug.replace("/", "_")
    report_path = f"reports/coverage_forensics_{prefix}.md"
    
    # 1-3. Total items
    vocab_items = []
    phrase_items = []
    sentence_items = []
    
    def load_json(filename):
        path = os.path.join(base_dir, filename)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    vocab_data = load_json(f"{prefix}_vocabulary.json")
    phrase_data = load_json(f"{prefix}_phrases.json")
    sentence_data = load_json(f"{prefix}_sentences.json")
    
    vocab_items = {item["id"]: item for item in vocab_data if "id" in item}
    phrase_items = {item["id"]: item for item in phrase_data if "id" in item}
    sentence_items = {item["id"]: item for item in sentence_data if "id" in item}
    
    # 4. Total lesson-taught IDs
    taught_ids_info = {} # mapping ID to location string
    lessons_data = load_json("mini_lessons.json")
    lessons_list = lessons_data.get("lessons", lessons_data) if isinstance(lessons_data, dict) else lessons_data
    
    for l_idx, l in enumerate(lessons_list):
        l_id = l.get("id", f"lesson_{l_idx}")
        # Check sections array
        for s_idx, s in enumerate(l.get("sections", [])):
            if isinstance(s, dict):
                for eid in s.get("exerciseIds", []):
                    taught_ids_info[eid] = f"Lesson {l_id}, Section {s_idx} ({s.get('type', 'unknown')})"
            elif isinstance(s, str):
                taught_ids_info[s] = f"Lesson {l_id}, Section {s_idx} (string)"
        # Check direct keys
        for k in ["vocabulary", "phrase", "sentence", "phrases", "sentences", "mastery"]:
            if k in l:
                for eid in l[k]:
                    taught_ids_info[eid] = f"Lesson {l_id}, Key {k}"

    taught_ids_set = set(taught_ids_info.keys())
    
    # Analyze missing
    def get_missing(item_dict):
        missing = []
        for eid in item_dict.keys():
            # Check direct ID, ID with scenario prefix, and ID with slug prefix
            if eid not in taught_ids_set and f"{prefix}-{eid}" not in taught_ids_set and f"{slug.replace('/', '_')}-{eid}" not in taught_ids_set:
                missing.append(eid)
        return missing

    missing_vocab = get_missing(vocab_items)
    missing_phrases = get_missing(phrase_items)
    missing_sentences = get_missing(sentence_items)
    
    # 8. Forensic breakdown
    def generate_forensic_breakdown(missing_list, name, item_dict):
        lines = []
        if not missing_list:
            lines.append(f"No missing {name} IDs.")
            return lines
            
        lines.append(f"First {min(20, len(missing_list))} missing {name} IDs:")
        for eid in missing_list[:20]:
            item_text = item_dict[eid].get("italian", "UNKNOWN TEXT")
            lines.append(f"  - `{eid}` (\"{item_text}\")")
            # Is it in mini_lessons.json at all? Maybe under a weird key or as a substring?
            found_raw = False
            raw_lessons_str = json.dumps(lessons_data)
            if f'"{eid}"' in raw_lessons_str:
                lines.append(f"    - Exists in mini_lessons.json? YES (as a raw string match, but not parsed in valid schema sections).")
            else:
                lines.append(f"    - Exists in mini_lessons.json? NO. Why? Likely because the curriculum was generated for an older, shorter version of conversations.json and was not updated after conversation expansion.")
        return lines

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# Coverage Forensics: {slug}\n\n")
        f.write(f"1. **Total vocabulary items:** {len(vocab_items)}\n")
        f.write(f"2. **Total phrase items:** {len(phrase_items)}\n")
        f.write(f"3. **Total sentence items:** {len(sentence_items)}\n")
        f.write(f"4. **Total lesson-taught IDs:** {len(taught_ids_set)}\n\n")
        
        f.write("## Missing Vocabulary Analysis\n")
        f.write("\n".join(generate_forensic_breakdown(missing_vocab, "Vocabulary", vocab_items)) + "\n\n")
        
        f.write("## Missing Phrase Analysis\n")
        f.write("\n".join(generate_forensic_breakdown(missing_phrases, "Phrase", phrase_items)) + "\n\n")
        
        f.write("## Missing Sentence Analysis\n")
        f.write("\n".join(generate_forensic_breakdown(missing_sentences, "Sentence", sentence_items)) + "\n\n")

    print(f"Generated {report_path}")

def main():
    os.makedirs("reports", exist_ok=True)
    for s in SCENARIOS:
        analyze_forensics(s)

if __name__ == "__main__":
    main()
