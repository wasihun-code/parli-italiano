import json
import os
import re
import sys
from collections import defaultdict

# Add current scripts directory to path to import linguistic_extractor
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from linguistic_extractor import tokenize

def get_scenario_slugs():
    mapping_path = 'src/data/scenarioMapping.ts'
    if not os.path.exists(mapping_path):
        return []
    with open(mapping_path, 'r', encoding='utf-8') as f:
        content = f.read()
    slugs = re.findall(r"'exports/(.*?)'", content)
    return slugs

def generate_global_id(italian, english, overrides):
    normalized = italian.lower().replace(" ", "_")
    # Handle overrides for homonyms
    if italian in overrides:
        for keyword, concept_id in overrides[italian].items():
            if keyword.lower() in english.lower():
                return concept_id
    
    # Default ID
    safe_text = re.sub(r"[^a-z0-9àèìòùé']", "", normalized)
    return f"word_{safe_text}"

def main():
    os.makedirs("generated", exist_ok=True)
    slugs = get_scenario_slugs()
    
    overrides_path = "src/data/dictionary_overrides.json"
    overrides = {}
    if os.path.exists(overrides_path):
        with open(overrides_path, "r", encoding="utf-8") as f:
            overrides = json.load(f)

    global_dictionary = {}
    scenario_vocab_mapping = defaultdict(list)
    
    print(f"Processing {len(slugs)} scenarios for global dictionary...")

    for slug in slugs:
        parts = slug.split('/')
        prefix = "_".join(parts)
        base_path = f"src/data/exports/{slug}"
        vocab_path = os.path.join(base_path, f"{prefix}_vocabulary.json")
        
        if not os.path.exists(vocab_path):
            print(f"  Skipping {slug} (no vocabulary file)")
            continue

        try:
            with open(vocab_path, "r", encoding="utf-8") as f:
                scenario_vocab = json.load(f)
            
            for item in scenario_vocab:
                it = item["italian"]
                en = item.get("english", "")
                local_id = item["id"]
                
                global_id = generate_global_id(it, en, overrides)
                
                # Add to global dict if not exists or if more complete
                if global_id not in global_dictionary:
                    global_dictionary[global_id] = {
                        "id": global_id,
                        "italian": it,
                        "english_primary": en,
                        "audio_json": item.get("audio")
                    }
                
                # Create mapping
                scenario_vocab_mapping[slug].append({
                    "local_id": local_id,
                    "global_id": global_id
                })
        except Exception as e:
            print(f"  Error processing {slug}: {e}")

    # Save outputs
    with open("generated/global_dictionary.json", "w", encoding="utf-8") as f:
        json.dump(list(global_dictionary.values()), f, indent=2, ensure_ascii=False)
        
    with open("generated/scenario_vocab_mapping.json", "w", encoding="utf-8") as f:
        json.dump(scenario_vocab_mapping, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated global dictionary with {len(global_dictionary)} entities.")
    print(f"Mapped vocabulary for {len(scenario_vocab_mapping)} scenarios.")

if __name__ == "__main__":
    main()
