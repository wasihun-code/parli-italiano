import json

def get_missing(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    for item in data:
        if not item.get("english"):
            print(f'{item["id"]}: {item["italian"]}')

get_missing("src/data/exports/tech/online_booking/tech_online_booking_vocabulary.json")
get_missing("src/data/exports/tech/online_booking/tech_online_booking_phrases.json")
get_missing("src/data/exports/tech/online_booking/tech_online_booking_sentences.json")
