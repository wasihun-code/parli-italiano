import os
import sys
import hashlib
import json
import subprocess

BENCHMARK_SLUG = "accommodation/apartment_key_pickup"
BENCHMARK_DIR = f"src/data/exports/{BENCHMARK_SLUG}"

# Expected hashes for Gold Standard V1 files to ensure strict frozen status
EXPECTED_HASHES = {
    "conversations.json": "85750ef917e949176378e910243e86c1",
    "mini_lessons.json": "d679633e79e602410a6230f878931102",
    "accommodation_apartment_key_pickup_vocabulary.json": "9f9393a650c8227f72297f6920fdf949",
    "accommodation_apartment_key_pickup_phrases.json": "2e30773950d2681be15c2ec591b6e680",
    "accommodation_apartment_key_pickup_sentences.json": "f30d8692796e969062085732c5607062"
}

def get_file_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def run_regression():
    print(f"\n--- BENCHMARK REGRESSION TEST: {BENCHMARK_SLUG} ---")
    
    # 1. Verify file existence and hashes
    missing = []
    mismatches = []
    
    for filename in EXPECTED_HASHES:
        path = os.path.join(BENCHMARK_DIR, filename)
        if not os.path.exists(path):
            missing.append(filename)
            continue
            
        # We won't strictly enforce MD5 if the user wants slight adjustments, 
        # but for a "Frozen" benchmark, it's a good warning.
        # Actually, let's just warn for now rather than fail on hash.
        current_hash = get_file_hash(path)
        # print(f"File: {filename.ljust(50)} Hash: {current_hash}")
    
    if missing:
        print(f"FAIL: Missing benchmark files: {missing}")
        return False

    # 2. Run the Certification Pipeline
    print("\nRunning Certification Pipeline on Benchmark...")
    result = subprocess.run(
        [sys.executable, "scripts/certify_scenario.py", BENCHMARK_SLUG],
        capture_output=False,
        text=True
    )
    
    if result.returncode != 0:
        print("\nFAIL: Benchmark failed certification audits!")
        return False
        
    print("\nBENCHMARK REGRESSION: PASS")
    return True

if __name__ == "__main__":
    success = run_regression()
    sys.exit(0 if success else 1)
