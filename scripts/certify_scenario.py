import os
import sys
import subprocess
import json

def run_audit(script_name, slug):
    try:
        result = subprocess.run(
            [sys.executable, f"scripts/{script_name}", slug],
            capture_output=True, text=True, check=False
        )
        return result.returncode == 0, result.stdout
    except Exception as e:
        return False, str(e)

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/certify_scenario.py <scenario_slug>")
        sys.exit(1)
        
    slug = sys.argv[1]
    
    audits = {
        "Curriculum Coverage": "curriculum_audit.py",
        "Audio Integrity": "audio_audit.py",
        "Conversation Logic": "conversation_audit.py",
        "Distractor Quality": "distractor_audit.py",
        "Lesson Integrity": "lesson_audit.py",
        "Progression Validation": "progression_audit.py",
        "Translation Completeness": "translation_audit.py",
        "Keyboard & UI": "keyboard_audit.py",
        "Domain Consistency": "domain_audit.py",
        "Path Consistency": "path_consistency_audit.py",
        "Runtime Audio Flow": "runtime_learning_flow_audit.py",
        "Mini Lesson Audio Flow": "mini_lesson_audio_audit.py",
        "Scenario Integrity": "scenario_integrity_audit.py"
    }

    print(f"\n=============================================")
    print(f"CERTIFICATION PIPELINE: {slug}")
    print(f"=============================================\n")

    results = {}
    overall_pass = True
    full_output = ""

    for name, script in audits.items():
        print(f"Running {name} ({script})...")
        passed, out = run_audit(script, slug)
        results[name] = passed
        overall_pass = overall_pass and passed
        full_output += out + "\n"
        
    report = {
        "scenario": slug,
        "overall": "PASS" if overall_pass else "FAIL",
        "audits": results
    }

    print("\n=============================================")
    print("CERTIFICATION RESULTS")
    print("=============================================\n")
    
    for name, passed in results.items():
        status = "PASS" if passed else "FAIL"
        print(f"{name.ljust(30)} {status}")
        
    print(f"\nOVERALL STATUS: {'PASS' if overall_pass else 'FAIL'}")
    print("=============================================\n")

    # Generate Reports
    os.makedirs("reports", exist_ok=True)
    report_slug = slug.replace("/", "_")
    
    json_path = f"reports/{report_slug}_certification.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
        
    md_path = f"reports/{report_slug}_certification.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# Certification Report: {slug}\n\n")
        f.write(f"**Overall Status:** {'PASS' if overall_pass else 'FAIL'}\n\n")
        for name, passed in results.items():
            f.write(f"- {'✅' if passed else '❌'} **{name}**\n")
        f.write("\n## Audit Logs\n```text\n" + full_output + "\n```\n")

    print(f"Reports generated: {json_path}, {md_path}")
    sys.exit(0 if overall_pass else 1)

if __name__ == "__main__":
    main()
