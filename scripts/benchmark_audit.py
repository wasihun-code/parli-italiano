import json
import os
import sys
import subprocess
from datetime import datetime

BENCHMARKS = [
    "accommodation/apartment_key_pickup",
    "accommodation/hotel_check_in",
    "travel/airport_arrival",
    "social/phone_call",
    "tech/buying_a_sim_card",
    "workstudy/job_interview",
    "shopping/clothing_store",
    "daily_life/at_the_bank",
    "health/doctor_appointment",
    "culture/museum_tickets"
]

def get_stats(slug, base_path="src/data/exports"):
    base_dir = f"{base_path}/{slug}"
    if not os.path.exists(base_dir):
        return None
    
    try:
        # Conversations
        with open(f"{base_dir}/conversations.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            convs = data["conversations"] if isinstance(data, dict) and "conversations" in data else data
            conv_count = len(convs)
            total_turns = sum(len(c.get("messages", [])) for c in convs)

        # Lessons
        with open(f"{base_dir}/mini_lessons.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            lessons = data["lessons"] if isinstance(data, dict) and "lessons" in data else data
            lesson_count = len(lessons)

        # Linguistic
        prefix = slug.replace("/", "_")
        vocab_path = f"{base_dir}/{prefix}_vocabulary.json"
        if not os.path.exists(vocab_path):
             # Try without prefix if benchmarking against something else
             vocab_path = f"{base_dir}/vocabulary.json"

        with open(vocab_path, "r", encoding="utf-8") as f:
            vocab = json.load(f)
            vocab_count = len(vocab)
            untranslated_vocab = sum(1 for v in vocab if not v.get("english"))

        return {
            "conv_count": conv_count,
            "total_turns": total_turns,
            "lesson_count": lesson_count,
            "vocab_count": vocab_count,
            "untranslated_vocab": untranslated_vocab
        }
    except Exception as e:
        print(f"Error reading stats for {slug} in {base_path}: {e}")
        return None

def main():
    results = []
    overall_pass = True
    
    print(f"Benchmark Audit: Verifying 10 core scenarios...")
    
    for slug in BENCHMARKS:
        print(f"Auditing {slug}...", end=" ", flush=True)
        
        # 1. Run certification (The most important check)
        cert_result = subprocess.run(
            [sys.executable, "scripts/certify_scenario.py", slug],
            capture_output=True, text=True
        )
        cert_pass = cert_result.returncode == 0
        
        # 2. Check stats against deep benchmark storage
        curr_stats = get_stats(slug, "src/data/exports")
        base_stats = get_stats(slug, "benchmarks")
        
        if not curr_stats or not base_stats:
            print("❌ FAIL (Could not read stats)")
            results.append({"slug": slug, "status": "FAIL", "reason": "Missing files or unreadable"})
            overall_pass = False
            continue
            
        stats_match = True
        diffs = []
        for key in ["conv_count", "lesson_count", "vocab_count", "untranslated_vocab"]:
            if curr_stats[key] != base_stats[key]:
                stats_match = False
                diffs.append(f"{key}: {curr_stats[key]} (expected {base_stats[key]})")
        
        if cert_pass and stats_match:
            print("✅ PASS")
            results.append({"slug": slug, "status": "PASS"})
        else:
            print("❌ FAIL")
            reason = []
            if not cert_pass: reason.append("Certification failed")
            if not stats_match: reason.append("Stats mismatch: " + ", ".join(diffs))
            results.append({"slug": slug, "status": "FAIL", "reason": "; ".join(reason)})
            overall_pass = False

    # Human-readable report
    os.makedirs("reports", exist_ok=True)
    with open("reports/benchmark_audit.md", "w", encoding="utf-8") as f:
        f.write("# Benchmark Audit Report\n\n")
        f.write(f"**Overall Status:** {'✅ PASS' if overall_pass else '❌ FAIL'}\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("| Scenario | Status | Reason |\n")
        f.write("| :--- | :--- | :--- |\n")
        for r in results:
            f.write(f"| {r['slug']} | {'✅ PASS' if r['status'] == 'PASS' else '❌ FAIL'} | {r.get('reason', '-')} |\n")

    # Machine-readable report
    with open("reports/benchmark_audit.json", "w", encoding="utf-8") as f:
        json.dump({"overall": "PASS" if overall_pass else "FAIL", "results": results}, f, indent=2)

    print(f"\nBenchmark audit completed. Status: {'PASS' if overall_pass else 'FAIL'}")
    sys.exit(0 if overall_pass else 1)

if __name__ == "__main__":
    main()
