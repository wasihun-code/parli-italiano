import os
import sys
import re

def extract_mapping():
    mapping_path = "src/data/scenarioMapping.ts"
    if not os.path.exists(mapping_path):
        print(f"FAIL: {mapping_path} not found")
        return {}
    
    with open(mapping_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    matches = re.findall(r"(\d+):\s+'([^']+)'", content)
    return {int(m[0]): m[1] for m in matches}

def check_scenario(s_id, rel_path, errors):
    base_dir = "src/data"
    full_path = os.path.join(base_dir, rel_path)
    
    if not os.path.exists(full_path):
        errors.append(f"ID {s_id}: Mapped directory not found: {full_path}")
        return

    # Check required files
    required_files = ["mini_lessons.json", "conversations.json", "domain.json"]
    for f in required_files:
        f_path = os.path.join(full_path, f)
        if not os.path.exists(f_path):
            errors.append(f"ID {s_id}: Missing required file: {f_path}")
            
    # Check for duplicates or near-duplicates
    folder_name = os.path.basename(rel_path)
    parent_dir = os.path.dirname(full_path)
    
    if os.path.exists(parent_dir):
        all_items = os.listdir(parent_dir)
        for item in all_items:
            item_path = os.path.join(parent_dir, item)
            if os.path.isdir(item_path):
                # Check for name collisions (e.g. hotel_check_in vs hotel_checkin)
                clean_item = item.replace("_", "").lower()
                clean_folder = folder_name.replace("_", "").lower()
                
                if clean_item == clean_folder and item != folder_name:
                    errors.append(f"ID {s_id}: Path Collision! Found '{item}' but mapping expects '{folder_name}'")

def main():
    target_slug = sys.argv[1] if len(sys.argv) > 1 else None
    
    if target_slug:
        print(f"\n--- PATH CONSISTENCY AUDIT: {target_slug} ---")
    else:
        print("\n--- PATH CONSISTENCY AUDIT: ALL ---")
        
    mapping = extract_mapping()
    if not mapping:
        return False
        
    errors = []
    
    if target_slug:
        # Check only the specific slug
        # Find ID for this slug
        matching_ids = [s_id for s_id, p in mapping.items() if p == target_slug or p == f"exports/{target_slug}"]
        if not matching_ids:
            # Maybe the slug passed is just the last part? 
            # Let's try to be flexible but accurate
            matching_ids = [s_id for s_id, p in mapping.items() if target_slug in p]
            
        if not matching_ids:
            errors.append(f"Slug '{target_slug}' not found in scenarioMapping.ts")
        else:
            for s_id in matching_ids:
                check_scenario(s_id, mapping[s_id], errors)
    else:
        # Check every scenario that HAS a directory
        # (This avoids failing for 100+ unmigrated placeholders)
        for s_id, rel_path in mapping.items():
            full_path = os.path.join("src/data", rel_path)
            if os.path.exists(full_path):
                check_scenario(s_id, rel_path, errors)

    if errors:
        for e in errors:
            print(f"  - {e}")
        print("PATH CONSISTENCY AUDIT: FAIL")
        return False
        
    print("PATH CONSISTENCY AUDIT: PASS")
    return True

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
