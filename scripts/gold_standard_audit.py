import os
import sys
import subprocess

def run_script(script_name):
    print(f"\nRunning {script_name}...")
    result = subprocess.run([sys.executable, f"scripts/{script_name}"], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.returncode == 0

def run_gold_standard_audit():
    print("\n=============================================")
    print("GOLD STANDARD CERTIFICATION AUDIT")
    print("=============================================\n")
    
    audits = {
        "Curriculum Coverage": "curriculum_audit.py",
        "Audio Coverage": "conversation_audio_audit.py",
        "Domain Consistency": "domain_audit.py",
        "Lesson Integrity": "lesson_quality_audit.py",
        "Mini Lesson Audio": "mini_lesson_audio_audit.py",
        "Runtime Learning Flow": "runtime_learning_flow_audit.py"
    }
    
    results = {}
    overall_pass = True
    
    for name, script in audits.items():
        success = run_script(script)
        results[name] = "PASS" if success else "FAIL"
        if not success:
            overall_pass = False
            
    print("\n=============================================")
    print("CERTIFICATION RESULTS")
    print("=============================================\n")
    
    for name, res in results.items():
        print(f"{name:.<25} {res}")
        
    print(f"\nOVERALL ............... {'PASS' if overall_pass else 'FAIL'}")
    print("=============================================\n")
    
    return overall_pass

if __name__ == "__main__":
    success = run_gold_standard_audit()
    sys.exit(0 if success else 1)
