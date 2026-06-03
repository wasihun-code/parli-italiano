import json

with open('src/data/exports/travel/bus_ticket/travel_bus_ticket_vocabulary.json', 'r') as f:
    vocab = json.load(f)

for item in vocab:
    print(f"{item['id']}: {item['italian']}")
