import sys
import os
import subprocess
import json

def run_runtime_audit():
    print("Starting Runtime Contract Audit...")
    # Using vitest to handle Vite features (import.meta.glob)
    cmd = ["npm", "run", "test:unit", "--", "src/tests/runtimeIntegration.test.ts"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ PASS: Runtime Contract is fully integrated and handles production data.")
        return True
    else:
        print("❌ FAIL: Runtime Contract integration failed.")
        print(result.stdout)
        return False

if __name__ == "__main__":
    success = run_runtime_audit()
    sys.exit(0 if success else 1)
