import os
import json
import glob
import sys

def main():
    print("==================================================")
    print(" RELEASE READINESS AUDIT (Phase 8.1 Repair)")
    print("==================================================")

    # 1. Verification of Global Certification JSON (Authoritative)
    cert_json_path = 'reports/global_certification.json'
    if not os.path.exists(cert_json_path):
        print(f"❌ Error: Global certification report missing at {cert_json_path}")
        sys.exit(1)
    
    try:
        with open(cert_json_path, 'r', encoding='utf-8') as f:
            cert_data = json.load(f)
            passed_count = cert_data.get('passed_count', 0)
            total_count = cert_data.get('total', 0)
            
            if passed_count < 116 or total_count < 116:
                print(f"❌ Error: Incomplete certification. Found {passed_count}/{total_count} passed (Need 116/116).")
                sys.exit(1)
            
            print(f"✅ Authoritative Certification Verified: {passed_count}/{total_count} PASS.")
    except Exception as e:
        print(f"❌ Error: Failed to parse {cert_json_path}: {e}")
        sys.exit(1)

    # 2. Hybrid Mastery Operational Verification
    paths = [
        'src/services/globalProgressService.ts',
        'src/services/curriculumAdaptationService.ts',
        'src/services/reviewQueueService.ts',
        'generated/global_dictionary.json',
        'generated/scenario_vocab_mapping.json'
    ]
    for p in paths:
        if not os.path.exists(p):
            print(f"❌ Error: Missing core V2 component: {p}")
            sys.exit(1)
    print("✅ Hybrid Mastery V2 Infrastructure Present.")

    # 3. Audio Manifest Validation
    if not os.path.exists('public/audio_manifest.json'):
        print("❌ Error: Audio manifest missing.")
        sys.exit(1)
    print("✅ Audio Manifest Present.")

    # 4. Cleanup Check (Adversarial)
    dead_files = ['src/lib/voiceAgent.ts', 'src/lib/migrate_to_v2.ts']
    found_dead = False
    for df in dead_files:
        if os.path.exists(df):
            print(f"❌ Error: Dead code '{df}' still exists.")
            found_dead = True
    if not found_dead:
        print("✅ Cleanup Verified.")
    else:
        sys.exit(1)

    print("\n✅ RELEASE READINESS: PASS")
    print("STATUS: RC1 Candidate Validated Successfully.")
    sys.exit(0)

if __name__ == "__main__":
    main()
