import os
import subprocess
import json
import sys
from datetime import datetime

def get_scenario_slugs():
    mapping_path = 'src/data/scenarioMapping.ts'
    if not os.path.exists(mapping_path):
        return []
    import re
    with open(mapping_path, 'r', encoding='utf-8') as f:
        content = f.read()
    slugs = re.findall(r"'exports/(.*?)'", content)
    return slugs

def main():
    slugs = get_scenario_slugs()
    total = len(slugs)
    passed = []
    failed = []
    
    print(f"Global Certification: Processing {total} scenarios...")
    
    os.makedirs("reports", exist_ok=True)
    os.makedirs("reports/failures", exist_ok=True)

    for i, slug in enumerate(slugs):
        print(f"[{i+1}/{total}] Certifying: {slug}...", end=" ", flush=True)
        
        # We run certify_scenario.py directly since build_and_certify_scenario.py 
        # is more for fresh generation (extraction/distractors).
        # Global certification should check if the CURRENT state is valid.
        result = subprocess.run(
            [sys.executable, "scripts/certify_scenario.py", slug],
            capture_output=True, text=True
        )
        
        if result.returncode == 0:
            print("✅ PASS")
            passed.append(slug)
        else:
            print("❌ FAIL")
            failed.append(slug)
            
            # Phase 6: Self-Healing Factory Failure Reports
            failure_report_path = f"reports/failures/{slug.replace('/', '_')}.md"
            with open(failure_report_path, "w", encoding="utf-8") as f:
                f.write(f"# Failure Report: {slug}\n\n")
                f.write(f"**Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("## Audit Output\n")
                f.write("```text\n")
                f.write(result.stdout)
                f.write("\n```\n")
                f.write("\n## Analysis\n")
                # Simple logic to suggest fix based on output
                if "Missing English translation" in result.stdout:
                    f.write("- **Failure Type:** Translation Gap\n")
                    f.write("- **Suggested Fix:** Run Agent 6 (Translation Specialist) to fill missing fields.\n")
                elif "expected >= 10" in result.stdout:
                    f.write("- **Failure Type:** Conversation Length Regression\n")
                    f.write("- **Suggested Fix:** Expand conversations in conversations.json to meet turn requirements.\n")
                elif "DOMAIN AUDIT: FAIL" in result.stdout:
                    f.write("- **Failure Type:** Domain Contamination\n")
                    f.write("- **Suggested Fix:** Update domain.json to allow/forbid specific terms.\n")
                else:
                    f.write("- **Failure Type:** Structural / Logic Error\n")
                    f.write("- **Suggested Fix:** Check the specific audit log above for details.\n")

    pass_rate = (len(passed) / total * 100) if total > 0 else 0
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "total": total,
        "passed_count": len(passed),
        "failed_count": len(failed),
        "pass_rate": f"{pass_rate:.2f}%",
        "passed_scenarios": passed,
        "failed_scenarios": failed
    }

    # Human-readable report
    md_path = "reports/global_certification.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Global Certification Report\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"- **Total Scenarios:** {total}\n")
        f.write(f"- **Passed:** {len(passed)}\n")
        f.write(f"- **Failed:** {len(failed)}\n")
        f.write(f"- **Pass Rate:** {pass_rate:.2f}%\n\n")
        
        if failed:
            f.write("## Failed Scenarios\n\n")
            for s in failed:
                f.write(f"- {s}\n")
        else:
            f.write("## ✅ All scenarios passed certification!\n")

    # Machine-readable report
    with open("reports/global_certification.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    # Dictionary Audit (Phase 7.2)
    print("\n[Phase 7.2] Running Global Dictionary Integrity Audit...")
    subprocess.run([sys.executable, "scripts/dictionary_integrity_audit.py"])

    print(f"\nGlobal certification completed.")
    print(f"Pass Rate: {pass_rate:.2f}%")
    print(f"Results saved to reports/global_certification.md and .json")
    
    if failed:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
