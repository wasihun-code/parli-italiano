import os
import hashlib
import json
import sys
import subprocess

CORE_SCRIPTS = [
    "scripts/linguistic_extractor.py",
    "scripts/curriculum_designer.py",
    "scripts/distractor_generator.py",
    "scripts/build_and_certify_scenario.py",
    "scripts/certify_scenario.py",
    "scripts/curriculum_audit.py",
    "scripts/audio_audit.py",
    "scripts/conversation_audit.py",
    "scripts/distractor_audit.py",
    "scripts/lesson_audit.py",
    "scripts/progression_audit.py",
    "scripts/translation_audit.py",
    "scripts/keyboard_audit.py",
    "scripts/domain_audit.py",
    "scripts/path_consistency_audit.py",
    "scripts/runtime_learning_flow_audit.py",
    "scripts/mini_lesson_audio_audit.py",
    "scripts/scenario_integrity_audit.py"
]

def get_hash(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def main():
    hash_file = "benchmarks/core_scripts_hashes.json"
    curr_hashes = {f: get_hash(f) for f in CORE_SCRIPTS}
    
    regressions_detected = False
    changed_files = []
    
    if os.path.exists(hash_file):
        with open(hash_file, "r") as f:
            old_hashes = json.load(f)
            
        for f in CORE_SCRIPTS:
            if curr_hashes[f] != old_hashes.get(f):
                regressions_detected = True
                changed_files.append(f)
    else:
        # First run, just save hashes
        print("No previous hashes found. Initializing hash baseline.")
        with open(hash_file, "w") as f:
            json.dump(curr_hashes, f, indent=2)
        print("Hash baseline initialized.")
        sys.exit(0)

    report = {
        "status": "PASS",
        "changed_files": changed_files
    }

    if regressions_detected:
        print(f"Regression Detection: Changes detected in {len(changed_files)} core files:")
        for f in changed_files:
            print(f" - {f}")
        print("\nTriggering benchmark audit...")
        
        result = subprocess.run(
            [sys.executable, "scripts/benchmark_audit.py"],
            capture_output=False, text=True
        )
        
        # Update hashes after running benchmarks
        if result.returncode == 0:
            print("Benchmarks passed. Updating hash baseline.")
            with open(hash_file, "w") as f:
                json.dump(curr_hashes, f, indent=2)
            print("Hash baseline updated.")
        else:
            print("❌ Regression Detected: Benchmarks failed after code changes.")
            report["status"] = "FAIL"
            with open("reports/regression_audit.json", "w") as f:
                json.dump(report, f, indent=2)
            sys.exit(1)
    else:
        print("No changes detected in core scripts. Regression check passed.")

    with open("reports/regression_audit.json", "w") as f:
        json.dump(report, f, indent=2)
    sys.exit(0)

if __name__ == "__main__":
    main()
