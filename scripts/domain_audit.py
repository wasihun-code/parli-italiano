import json
import os
import sys

def main(scenario_slug):
    print(f"\n--- DOMAIN CONTAMINATION AUDIT: {scenario_slug} ---")
    base_path = f"src/data/exports/{scenario_slug}"
    parts = scenario_slug.split('/')
    prefix = "_".join(parts)
    
    vocab_path = os.path.join(base_path, f"{prefix}_vocabulary.json")
    domain_path = os.path.join(base_path, "domain.json")
    
    # 1. Load domain rules if they exist
    forbidden_words = set()
    if os.path.exists(domain_path):
        try:
            with open(domain_path, "r", encoding="utf-8") as f:
                domain_rules = json.load(f)
                forbidden_words = set(w.lower() for w in domain_rules.get("forbidden", []))
        except Exception as e:
            print(f"WARN: Could not parse domain.json: {e}")
    else:
        # Fallback to a basic check or just pass if no rules defined yet
        # For the benchmark, we will define a domain.json file
        print(f"WARN: No domain.json found in {base_path}. Skipping strict lexical check.")

    try:
        with open(vocab_path, "r", encoding="utf-8") as f:
            vocab = json.load(f)
    except Exception as e:
        print(f"FAIL: Could not load vocabulary json: {e}")
        return False

    violations = []
    for v in vocab:
        word = v.get("italian", "").lower()
        if word in forbidden_words:
            violations.append(word)

    if violations:
        print(f"Violations found: {len(violations)}")
        for v in violations[:10]:
            print(f"  - {v}")
        print("DOMAIN AUDIT: FAIL")
        return False
        
    print("DOMAIN AUDIT: PASS")
    return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "accommodation/apartment_key_pickup"
    sys.exit(0 if main(slug) else 1)
