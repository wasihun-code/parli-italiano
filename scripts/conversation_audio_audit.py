import json
import os
import sys

def run_audio_audit(scenario_dir="src/data/exports/accommodation/apartment_key_pickup"):
    print("\n--- CONVERSATION AUDIO AUDIT ---")
    conv_file = os.path.join(scenario_dir, "conversations.json")
    
    try:
        with open(conv_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"FAIL: Could not load conversations.json: {e}")
        return False

    conversations = data.get("conversations", [])
    
    total_nodes = 0
    missing_assets = []
    broken_references = []
    
    for conv in conversations:
        for msg in conv.get("messages", []):
            total_nodes += 1
            
            # Check host message audio
            if "audio" not in msg or "italian" not in msg["audio"]:
                missing_assets.append(f"Conv '{conv['id']}' Msg '{msg['id']}': Missing host audio metadata")
            else:
                audio_path = msg["audio"]["italian"]
                full_path = os.path.join("public", audio_path.lstrip("/"))
                if not os.path.exists(full_path):
                    broken_references.append(f"Conv '{conv['id']}' Msg '{msg['id']}': File not found '{full_path}'")
                    
            # Check choices
            for choice in msg.get("choices", []):
                total_nodes += 1
                if "audio" not in choice or "italian" not in choice["audio"]:
                    missing_assets.append(f"Conv '{conv['id']}' Msg '{msg['id']}' Choice '{choice['text']}': Missing choice audio metadata")
                else:
                    audio_path = choice["audio"]["italian"]
                    full_path = os.path.join("public", audio_path.lstrip("/"))
                    if not os.path.exists(full_path):
                        broken_references.append(f"Conv '{conv['id']}' Msg '{msg['id']}' Choice '{choice['text']}': File not found '{full_path}'")

    audio_coverage_pct = 100.0
    if total_nodes > 0:
        failures = len(missing_assets) + len(broken_references)
        audio_coverage_pct = ((total_nodes - failures) / total_nodes) * 100

    print(f"Conversation Nodes (incl. choices): {total_nodes}")
    print(f"Audio Coverage: {audio_coverage_pct:.1f}%")
    
    if missing_assets:
        print(f"Missing Assets ({len(missing_assets)}):")
        for m in missing_assets[:5]: print(f"  - {m}")
        if len(missing_assets) > 5: print(f"  ... and {len(missing_assets)-5} more")
        
    if broken_references:
        print(f"Broken References ({len(broken_references)}):")
        for b in broken_references[:5]: print(f"  - {b}")
        if len(broken_references) > 5: print(f"  ... and {len(broken_references)-5} more")

    if audio_coverage_pct == 100.0:
        print("AUDIO AUDIT: PASS")
        return True
    else:
        print("AUDIO AUDIT: FAIL")
        return False

if __name__ == "__main__":
    success = run_audio_audit()
    sys.exit(0 if success else 1)
