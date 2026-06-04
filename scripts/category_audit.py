import os
import json
import re

def get_categories():
    mapping_path = 'src/data/scenarioMapping.ts'
    if not os.path.exists(mapping_path):
        return {}
    
    with open(mapping_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Map from slug to category
    # Slugs are exports/CATEGORY/SCENARIO
    matches = re.findall(r"'exports/(.*?)/(.*?)'", content)
    categories = {}
    for cat, scenario in matches:
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(f"{cat}/{scenario}")
    return categories

def main():
    categories = get_categories()
    report_results = {}
    
    # Read existing reports from reports/ folder
    for cat, scenarios in categories.items():
        cat_stats = {"passed": 0, "failed": 0, "missing": 0, "total": len(scenarios)}
        for slug in scenarios:
            report_path = f"reports/{slug.replace('/', '_')}_certification.json"
            if os.path.exists(report_path):
                with open(report_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if data.get("overall") == "PASS":
                        cat_stats["passed"] += 1
                    else:
                        cat_stats["failed"] += 1
            else:
                cat_stats["missing"] += 1
        report_results[cat] = cat_stats

    # Human-readable report
    os.makedirs("reports", exist_ok=True)
    with open("reports/category_audit.md", "w", encoding="utf-8") as f:
        f.write("# Category Audit Report\n\n")
        f.write("| Category | Progress | Status |\n")
        f.write("| :--- | :--- | :--- |\n")
        for cat, stats in sorted(report_results.items()):
            progress = f"{stats['passed']}/{stats['total']}"
            status = "✅ PASS" if stats['passed'] == stats['total'] else "❌ FAIL"
            if stats['missing'] > 0:
                status = "⚠️ INCOMPLETE"
            f.write(f"| {cat.capitalize().replace('_', ' ')} | {progress} | {status} |\n")

    # Machine-readable report
    with open("reports/category_audit.json", "w", encoding="utf-8") as f:
        json.dump(report_results, f, indent=2)

    print("Category audit completed. Reports saved to reports/category_audit.md and .json")

if __name__ == "__main__":
    main()
