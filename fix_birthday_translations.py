import json
import os

def main():
    path = "src/data/exports/social/birthday_wishes/social_birthday_wishes_vocabulary.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    translations = {
        "v259": "I will use",
        "v261": "goes",
        "v263": "you see",
        "v268": "comes"
    }

    for item in data:
        if item["id"] in translations:
            item["english"] = translations[item["id"]]
        elif item["id"] == "v3" and not item.get("english"):
            item["english"] = "to admire" # guessing based on previous run

    # Check for any other empty ones
    for item in data:
        if not item.get("english"):
            if item["italian"] == "adoro": item["english"] = "I love / I adore"
            if item["italian"] == "alla": item["english"] = "at the"
            if item["italian"] == "anni": item["english"] = "years"
            if item["italian"] == "appunto": item["english"] = "indeed / exactly"
            if item["italian"] == "auguri": item["english"] = "wishes"
            if item["italian"] == "bel": item["english"] = "beautiful / nice"
            if item["italian"] == "brindisi": item["english"] = "toast"
            if item["italian"] == "cheeseee": item["english"] = "cheese (for photo)"
            if item["italian"] == "chi": item["english"] = "who"
            if item["italian"] == "compleanno": item["english"] = "birthday"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
