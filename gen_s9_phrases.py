import json
import random

scenario = "asking_directions"
s_code = "s9"

phrases_data = [
    ("Mi scusi", "Excuse me"), ("Buongiorno", "Good morning"), ("Buonasera", "Good evening"),
    ("Per favore", "Please"), ("Grazie mille", "Thanks a lot"), ("Prego", "You're welcome"),
    ("Di nulla", "It's nothing"), ("Mi sono perso", "I'm lost"), ("Cerco il Duomo", "I'm looking for the Cathedral"),
    ("Dov'è la stazione?", "Where is the station?"), ("Come arrivo in centro?", "How do I get to the center?"),
    ("È lontano?", "Is it far?"), ("Quanto dista?", "How far is it?"), ("A piedi", "By foot"),
    ("In autobus", "By bus"), ("In metro", "By subway"), ("Giri a sinistra", "Turn left"),
    ("Giri a destra", "Turn right"), ("Vada dritto", "Go straight"), ("Fino al semaforo", "Until the traffic light"),
    ("Dopo l'incrocio", "After the intersection"), ("Accanto alla chiesa", "Next to the church"),
    ("Davanti al museo", "In front of the museum"), ("Dietro la banca", "Behind the bank"),
    ("All'angolo", "At the corner"), ("La prima a destra", "The first right"), ("La seconda a sinistra", "The second left"),
    ("Torni indietro", "Go back"), ("Attraversi la piazza", "Cross the square"), ("Segua la via", "Follow the street"),
    ("C'è una farmacia?", "Is there a pharmacy?"), ("Un buon ristorante?", "A good restaurant?"),
    ("Il bancomat più vicino?", "The nearest ATM?"), ("Può aiutarmi?", "Can you help me?"),
    ("Non capisco", "I don't understand"), ("Può ripetere?", "Can you repeat?"), ("Più piano, per favore", "Slower, please"),
    ("Scriva qui", "Write here"), ("Sulla mappa", "On the map"), ("Guardi lì", "Look there"),
    ("È proprio qui", "It's right here"), ("Circa dieci minuti", "About ten minutes"), ("Poco lontano", "Not far"),
    ("Molto vicino", "Very close"), ("In fondo alla strada", "At the end of the road"),
    ("Seconda traversa", "Second side street"), ("Dall'altra parte", "On the other side"),
    ("Attraversi il ponte", "Cross the bridge"), ("Prenda il bus", "Take the bus"), ("Fino alla fine", "Until the end"),
    ("Non ne sono sicuro", "I'm not sure"), ("Chieda a lui", "Ask him"), ("Buona giornata", "Good day"),
    ("Buona passeggiata", "Have a nice walk")
]

items = []
for i, (it, en) in enumerate(phrases_data):
    dist_it = [d[0] for d in random.sample(phrases_data, 4) if d[0] != it][:3]
    dist_en = [d[1] for d in phrases_data if d[0] in dist_it] # Keep alignment for distractors if possible or just sample
    # To ensure exact alignment of distractors:
    others = [d for d in phrases_data if d[0] != it]
    sampled_others = random.sample(others, 3)
    dist_it = [s[0] for s in sampled_others]
    dist_en = [s[1] for s in sampled_others]

    choices_it = [it] + dist_it
    choices_en = [en] + dist_en
    combined = list(zip(choices_it, choices_en))
    random.shuffle(combined)
    choices_it, choices_en = zip(*combined)
    
    item = {
        "id": f"{s_code}-p{i+1}",
        "italian": it,
        "english": en,
        "type": "phrase",
        "choicesItalian": list(choices_it),
        "choicesEnglish": list(choices_en),
        "correctAnswerItalian": it,
        "correctAnswerEnglish": en,
        "feedback": {
          "correctItalian": "Esatto!",
          "incorrectItalian": f"No, la frase corretta è \"{it}\".",
          "correctEnglish": "Exactly!",
          "incorrectEnglish": f"No, the correct phrase is \"{en}\"."
        }
    }
    items.append(item)

with open(f"/home/waseageru/parli-italiano/src/data/exports/travel/{scenario}/travel_{scenario}_phrases.json", "w") as f:
    json.dump(items, f, indent=2, ensure_ascii=False)
