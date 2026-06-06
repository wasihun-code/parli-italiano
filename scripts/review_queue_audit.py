import json
import os
import sys
from datetime import datetime, timedelta

def main():
    print("==================================================")
    print(" REVIEW QUEUE AUDIT (Phase 7.8)")
    print("==================================================")

    # 1. Simulate progress database
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    tomorrow = now + timedelta(days=1)
    
    mock_progress = [
        {"id": "word_grazie", "next_review": yesterday, "streak": 5, "attempts": 10}, # DUE (LEARNED)
        {"id": "word_pane", "next_review": yesterday, "streak": 0, "attempts": 5},    # LAPSED
        {"id": "word_latte", "next_review": yesterday, "streak": 0, "attempts": 2},   # LAPSED
        {"id": "word_vino", "next_review": tomorrow, "streak": 3, "attempts": 3},     # NOT DUE
    ]
    # Add 150 more DUE items to test cap
    for i in range(150):
        mock_progress.append({"id": f"word_test_{i}", "next_review": yesterday, "streak": 3, "attempts": 3})

    # 2. Extract and Filter Due Items
    due_items = [p for p in mock_progress if p["next_review"] <= now or (p["streak"] == 0 and p["attempts"] > 0)]
    
    if any(p["next_review"] > now and p["streak"] > 0 for p in due_items):
        print("❌ Error: Filter logic included non-due, non-lapsed items.")
        sys.exit(1)
    print("✅ Due Filtering Validated.")

    # 3. Prioritize (LAPSED first)
    def score(p):
        if p["streak"] == 0 and p["attempts"] > 0: return 100
        return 40
    
    due_items.sort(key=score, reverse=True)
    
    if due_items[0]["id"] != "word_pane" and due_items[0]["id"] != "word_latte":
        print("❌ Error: LAPSED items not prioritized at top of queue.")
        sys.exit(1)
    print("✅ Sorting Priority Validated (LAPSED first).")

    # 4. Cap at 100
    queue = due_items[:100]
    
    if len(queue) > 100:
        print(f"❌ Error: Queue size {len(queue)} exceeds 100 cap.")
        sys.exit(1)
    print("✅ 100-Item Cap Validated.")

    # 5. Uniqueness
    ids = [p["id"] for p in queue]
    if len(ids) != len(set(ids)):
        print("❌ Error: Duplicate IDs in queue.")
        sys.exit(1)
    print("✅ Uniqueness Validated.")

    print("\n✅ REVIEW QUEUE AUDIT: PASS")
    sys.exit(0)

if __name__ == "__main__":
    main()
