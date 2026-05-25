import json

scenario = "asking_directions"
s_code = "s9"

vocab_data = [
    ("stazione", "station"), ("semaforo", "traffic light"), ("piazza", "square"), 
    ("incrocio", "intersection"), ("via", "street"), ("strada", "road"), 
    ("traversa", "side street"), ("campanile", "bell tower"), ("duomo", "cathedral"),
    ("ristorante", "restaurant"), ("aiuto", "help"), ("cammino", "walk/path"),
    ("minuto", "minute"), ("direzione", "direction"), ("sinistra", "left"),
    ("destra", "right"), ("dritto", "straight"), ("angolo", "corner"),
    ("fermata", "stop"), ("autobus", "bus"), ("metropolitana", "subway"),
    ("mappa", "map"), ("navigatore", "GPS"), ("ufficio postale", "post office"),
    ("banca", "bank"), ("farmacia", "pharmacy"), ("supermercato", "supermarket"),
    ("ospedale", "hospital"), ("centro", "center"), ("periferia", "outskirts"),
    ("ponte", "bridge"), ("fiume", "river"), ("castello", "castle"),
    ("museo", "museum"), ("chiesa", "church"), ("monumento", "monument"),
    ("parco", "park"), ("giardino", "garden"), ("fontana", "fountain"),
    ("statua", "statue"), ("marciapiede", "sidewalk"), ("strisce pedonali", "crosswalk"),
    ("sottopasso", "underpass"), ("cavalcavia", "overpass"), ("rotatoria", "roundabout"),
    ("cartello stradale", "road sign"), ("lontano", "far"), ("vicino", "near"),
    ("girare", "to turn"), ("seguire", "to follow"), ("andare", "to go"),
    ("arrivare", "to arrive"), ("cercare", "to look for"), ("perdersi", "to get lost")
]

def generate_distractors(item, all_items, lang):
    distractors = [i[0] if lang == 'it' else i[1] for i in all_items if i != item]
    import random
    return random.sample(distractors, 3)

items = []
for i, (it, en) in enumerate(vocab_data):
    dist_it = generate_distractors((it, en), vocab_data, 'it')
    dist_en = generate_distractors((it, en), vocab_data, 'en')
    
    choices_it = [it] + dist_it
    choices_en = [en] + dist_en
    # Shuffle alignment
    combined = list(zip(choices_it, choices_en))
    import random
    random.shuffle(combined)
    choices_it, choices_en = zip(*combined)
    
    item = {
        "id": f"{s_code}-v{i+1}",
        "italian": it,
        "english": en,
        "type": "vocabulary",
        "choicesItalian": list(choices_it),
        "choicesEnglish": list(choices_en),
        "correctAnswerItalian": it,
        "correctAnswerEnglish": en,
        "feedback": {
          "correctItalian": "Ottimo!",
          "incorrectItalian": f"Quasi! La risposta corretta è \"{it}\".",
          "correctEnglish": "Great!",
          "incorrectEnglish": f"Almost! The correct answer is \"{en}\"."
        }
    }
    items.append(item)

with open(f"/home/waseageru/parli-italiano/src/data/exports/travel/{scenario}/travel_{scenario}_vocabulary.json", "w") as f:
    json.dump(items, f, indent=2, ensure_ascii=False)
