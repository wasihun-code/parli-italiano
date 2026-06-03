import json

with open('src/data/exports/travel/bus_ticket/travel_bus_ticket_phrases.json', 'r') as f:
    phrases = json.load(f)

for item in phrases:
    print(f"{item['id']}: {item['italian']}")
