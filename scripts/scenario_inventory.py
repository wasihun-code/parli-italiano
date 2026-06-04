import os
import re
import sys
import json

def get_scenario_slugs():
    mapping_path = 'src/data/scenarioMapping.ts'
    if not os.path.exists(mapping_path):
        print(f"Error: {mapping_path} not found.")
        return []
    
    with open(mapping_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract slugs like 'exports/travel/airport_arrival'
    slugs = re.findall(r"'exports/(.*?)'", content)
    return slugs

def main():
    slugs = get_scenario_slugs()
    inventory = []
    
    print(f"Scenario Inventory: Found {len(slugs)} scenarios in mapping.")
    
    for slug in slugs:
        base_dir = os.path.join('src/data/exports', slug)
        exists = os.path.isdir(base_dir)
        
        files = ["conversations.json", "mini_lessons.json", "domain.json"]
        missing_files = []
        if exists:
            for f in files:
                if not os.path.exists(os.path.join(base_dir, f)):
                    missing_files.append(f)
        
        item = {
            "slug": slug,
            "directory_exists": exists,
            "missing_files": missing_files,
            "is_complete": exists and len(missing_files) == 0
        }
        inventory.append(item)

    # Human-readable report
    os.makedirs("reports", exist_ok=True)
    report_path = "reports/scenario_inventory.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Scenario Inventory Report\n\n")
        f.write(f"Total defined in mapping: {len(slugs)}\n")
        f.write(f"Valid directories: {sum(1 for i in inventory if i['directory_exists'])}\n")
        f.write(f"Fully populated: {sum(1 for i in inventory if i['is_complete'])}\n\n")
        
        f.write("| Slug | Exists | Missing Files | Status |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for i in inventory:
            status = "✅ OK" if i['is_complete'] else "❌ INCOMPLETE"
            missing = ", ".join(i['missing_files']) if i['missing_files'] else "-"
            f.write(f"| {i['slug']} | {'Yes' if i['directory_exists'] else 'No'} | {missing} | {status} |\n")

    # Machine-readable report
    with open("reports/scenario_inventory.json", "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=2)

    print(f"Inventory completed. Reports saved to reports/scenario_inventory.md and .json")

if __name__ == "__main__":
    main()
