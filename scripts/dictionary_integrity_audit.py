import json
import os
import sys

def main():
    dict_path = "generated/global_dictionary.json"
    mapping_path = "generated/scenario_vocab_mapping.json"
    
    if not os.path.exists(dict_path) or not os.path.exists(mapping_path):
        print("❌ Error: Dictionary or mapping file missing. Run generation first.")
        sys.exit(1)

    with open(dict_path, "r", encoding="utf-8") as f:
        global_dict_list = json.load(f)
        global_dict = {item["id"]: item for item in global_dict_list}
        
    with open(mapping_path, "r", encoding="utf-8") as f:
        scenario_mappings = json.load(f)

    errors = []

    # 1. Uniqueness check
    if len(global_dict_list) != len(global_dict):
        errors.append("Duplicate IDs found in global_dictionary.json")

    # 2. Mapping Integrity & Empty Translations
    for slug, mappings in scenario_mappings.items():
        for m in mappings:
            gid = m["global_id"]
            if gid not in global_dict:
                errors.append(f"Broken mapping in {slug}: global_id {gid} not found in dictionary.")
            else:
                if not global_dict[gid].get("english_primary"):
                    errors.append(f"Empty translation for {gid} (referenced by {slug})")

    # 3. Round Trip Validation
    print("Executing Round-Trip Validation...")
    round_trip_passed = True
    for slug, mappings in scenario_mappings.items():
        parts = slug.split('/')
        prefix = "_".join(parts)
        original_vocab_path = f"src/data/exports/{slug}/{prefix}_vocabulary.json"
        
        if not os.path.exists(original_vocab_path):
            continue

        with open(original_vocab_path, "r", encoding="utf-8") as f:
            original_vocab = {item["id"]: item["italian"] for item in json.load(f)}
            
        for m in mappings:
            local_id = m["local_id"]
            global_id = m["global_id"]
            
            reconstructed_italian = global_dict[global_id]["italian"]
            original_italian = original_vocab.get(local_id)
            
            if original_italian and reconstructed_italian.lower() != original_italian.lower():
                errors.append(f"Round-trip failure in {slug}: {local_id} ({original_italian}) != reconstructed ({reconstructed_italian})")
                round_trip_passed = False

    # 4. Result
    if errors:
        print("\n❌ DICTIONARY AUDIT: FAIL")
        for err in errors[:20]: # Show first 20
            print(f"  - {err}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more errors.")
        sys.exit(1)
    else:
        print("\n✅ DICTIONARY AUDIT: PASS")
        print(f"  - Entities: {len(global_dict)}")
        print(f"  - Scenarios: {len(scenario_mappings)}")
        print("  - Round-trip: 100% Correct")
        sys.exit(0)

if __name__ == "__main__":
    main()
