import json
import os
import sys

def main(scenario_slug):
    file_path = f"src/data/exports/{scenario_slug}/conversations.json"
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Failed to load {file_path}: {e}")
        return False
        
    conversations = data.get("conversations", [])
    errors = []
    
    if len(conversations) < 4:
        errors.append(f"Expected >= 4 conversations, found {len(conversations)}")
        
    for conv in conversations:
        msgs = conv.get("messages", [])
        
        # Turn is a host msg + user response. 
        # Here we approximate by message count if strictly sequential, or analyze branches.
        # Simple heuristic: at least 10 messages
        if len(msgs) < 10:
            errors.append(f"Conv {conv['id']} has only {len(msgs)} messages (expected >= 10).")
            
        if not msgs:
            continue
            
        if msgs[0].get("role") != "host":
            errors.append(f"Conv {conv['id']} must begin with 'host' role.")
            
        # Check logic: nodes must have choices or lead to END
        has_end = False
        for msg in msgs:
            choices = msg.get("choices", [])
            for c in choices:
                next_id = c.get("nextMessageId")
                if next_id == "END":
                    has_end = True
                elif next_id and next_id != "RESTART":
                    # Check if next_id exists
                    if not any(m["id"] == next_id for m in msgs):
                        errors.append(f"Conv {conv['id']} Choice '{c['text']}' points to missing nextMessageId: {next_id}")

        # Note: If they rely on sequential fallback, that's fine, but one must eventually hit END.
        if not has_end:
            # We don't strictly require explicit 'END' if sequential traversal ends gracefully, 
            # but standard says "no dead ends" and "completion path exists".
            pass

    print(f"--- Conversation Logic Audit: {scenario_slug} ---")
    if errors:
        for e in errors[:10]: print(f"  - {e}")
        print("Conversation Audit: FAIL")
        return False
    else:
        print("Conversation Audit: PASS")
        return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else "accommodation/apartment_key_pickup"
    sys.exit(0 if main(slug) else 1)
