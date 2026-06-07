import subprocess
import sys
import hashlib
import json

def run_determinism_audit():
    print("Starting Learning Path Determinism Audit (Hardened)...")
    
    hashes = set()
    outputs = []

    # Run 100 times
    for i in range(100):
        # We use the existing unit test but capture its output if possible, 
        # or we run a specialized node script that prints the JSON.
        # Since I can't easily change the existing test to print JSON without side effects,
        # I will create a temporary node script for this audit.
        pass

    # Actually, let's create a dedicated node script to ensure pure logic audit.
    node_script = """
import { LearningPathGenerator } from './src/services/learningPathGenerator';
const mockInput = {
    scenarioId: 22,
    scenarioData: {
      vocabulary: [{ id: 'v1', italian: 'ciao', english: 'hi' }],
      phrases: [],
      sentences: [],
      scriptedConversations: []
    },
    globalMastery: {},
    reviewQueue: []
};
const result = LearningPathGenerator.generatePath(mockInput);
console.log(JSON.stringify(result));
"""
    with open('temp_audit.ts', 'w') as f:
        f.write(node_script)

    for i in range(100):
        result = subprocess.run(["npx", "tsx", "temp_audit.ts"], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Execution {i} failed")
            return False
        
        h = hashlib.sha256(result.stdout.strip().encode()).hexdigest()
        hashes.add(h)
        if i == 0:
            outputs.append(result.stdout.strip())

    if len(hashes) == 1:
        print(f"✅ PASS: 100 runs produced identical hash: {list(hashes)[0]}")
        # Cleanup
        subprocess.run(["rm", "temp_audit.ts"])
        return True
    else:
        print(f"❌ FAIL: Variance detected! {len(hashes)} different outputs found.")
        return False

if __name__ == "__main__":
    success = run_determinism_audit()
    sys.exit(0 if success else 1)
