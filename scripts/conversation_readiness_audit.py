import subprocess
import sys
import os

def run_test():
    print("Running Conversation Readiness Audit...")
    cmd = ["npm", "run", "test:unit", "--", "src/services/conversationReadiness.test.ts"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ PASS: Conversation Readiness gating is correctly enforced (80/80/80 Rule).")
        return True
    else:
        print("❌ FAIL: Conversation Readiness gating logic is incorrect.")
        print(result.stdout)
        return False

if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
