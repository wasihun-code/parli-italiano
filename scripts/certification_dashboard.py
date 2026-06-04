import os
import json
from datetime import datetime

def main():
    dashboard_path = "reports/dashboard.md"
    os.makedirs("reports", exist_ok=True)
    
    # 1. Load Global Certification
    global_cert = {}
    if os.path.exists("reports/global_certification.json"):
        with open("reports/global_certification.json", "r") as f:
            global_cert = json.load(f)
            
    # 2. Load Category Audit
    category_audit = {}
    if os.path.exists("reports/category_audit.json"):
        with open("reports/category_audit.json", "r") as f:
            category_audit = json.load(f)
            
    # 3. Load Benchmark Audit
    benchmark_audit = {}
    if os.path.exists("reports/benchmark_audit.json"):
        with open("reports/benchmark_audit.json", "r") as f:
            benchmark_audit = json.load(f)
            
    # 3.5 Load Regression Audit
    regression_audit = {}
    if os.path.exists("reports/regression_audit.json"):
        with open("reports/regression_audit.json", "r") as f:
            regression_audit = json.load(f)
            
    # 4. Generate Dashboard
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write("# PARLA ITALIANO — CERTIFICATION DASHBOARD\n\n")
        f.write(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Overview
        f.write("## Overview\n\n")
        f.write(f"- **Total Scenarios:** {global_cert.get('total', '-')}\n")
        f.write(f"- **Certified Scenarios:** {global_cert.get('passed_count', '-')}\n")
        f.write(f"- **Failed Scenarios:** {global_cert.get('failed_count', '-')}\n")
        f.write(f"- **Pass Rate:** {global_cert.get('pass_rate', '-')}\n")
        f.write(f"- **Benchmark Status:** {'✅ PASS' if benchmark_audit.get('overall') == 'PASS' else '❌ FAIL'}\n")
        f.write(f"- **Regression Status:** {'✅ PASS' if regression_audit.get('status') == 'PASS' else '❌ FAIL'}\n\n")
        
        # Category Breakdown
        f.write("## Category Breakdown\n\n")
        f.write("| Category | Progress | Status |\n")
        f.write("| :--- | :--- | :--- |\n")
        for cat, stats in sorted(category_audit.items()):
            progress = f"{stats['passed']}/{stats['total']}"
            status = "✅ PASS" if stats['passed'] == stats['total'] else "❌ FAIL"
            f.write(f"| {cat.capitalize().replace('_', ' ')} | {progress} | {status} |\n")
        f.write("\n")
        
        # Benchmarks
        f.write("## Benchmark Status\n\n")
        f.write("| Benchmark Scenario | Status |\n")
        f.write("| :--- | :--- |\n")
        for res in benchmark_audit.get("results", []):
            f.write(f"| {res['slug']} | {'✅ PASS' if res['status'] == 'PASS' else '❌ FAIL'} |\n")
        f.write("\n")
        
        # Recent Failures
        if global_cert.get("failed_scenarios"):
            f.write("## Recent Failures\n\n")
            for s in global_cert["failed_scenarios"]:
                report_link = f"reports/failures/{s.replace('/', '_')}.md"
                f.write(f"- [{s}]({report_link})\n")
            f.write("\n")
            
        f.write("---")
        
    print(f"Certification dashboard generated at {dashboard_path}")

if __name__ == "__main__":
    main()
