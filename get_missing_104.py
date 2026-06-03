import json
import os

base = "./src/data/exports/tech/online_booking"
prefix = "tech_online_booking"

missing = []

for f_type in ["vocabulary", "phrases", "sentences"]:
    path = os.path.join(base, f"{prefix}_{f_type}.json")
    with open(path, "r", encoding="utf-8") as f:
        items = json.load(f)
    for item in items:
        if not item.get("english") or str(item["english"]).strip() == "":
            missing.append(item["italian"])

with open("missing_104.json", "w", encoding="utf-8") as f:
    json.dump(missing, f, indent=2, ensure_ascii=False)
