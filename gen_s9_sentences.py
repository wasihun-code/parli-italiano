import json
import random

scenario = "asking_directions"
s_code = "s9"

sentences_data = [
    ("Scusi, saprebbe dirmi come arrivare alla stazione?", "Excuse me, could you tell me how to get to the station?"),
    ("Deve andare dritto fino al semaforo.", "You must go straight until the traffic light."),
    ("Giri a sinistra dopo la piazza.", "Turn left after the square."),
    ("È lontano da qui a piedi?", "Is it far from here on foot?"),
    ("Sono circa dieci minuti di cammino.", "It's about a ten-minute walk."),
    ("Mi sono perso, cerco il Duomo.", "I'm lost, I'm looking for the Cathedral."),
    ("Vede quel campanile alto in fondo?", "Do you see 그 bell tower at the end?"),
    ("Segua quella direzione per cinque minuti.", "Follow that direction for five minutes."),
    ("Conosce un buon ristorante qui vicino?", "Do you know a good restaurant near here?"),
    ("È in una traversa di via Roma.", "It's in a side street off via Roma."),
    ("Torni indietro fino all'incrocio.", "Go back until the intersection."),
    ("Prenda la seconda strada a destra.", "Take the second street on the right."),
    ("Lo troverà subito sulla sinistra.", "You will find it immediately on the left."),
    ("Grazie mille per l'aiuto!", "Thanks a lot for the help!"),
    ("Non c'è di che, figurati!", "Don't mention it, no problem!"),
    ("Buongiorno, dov'è la fermata dell'autobus?", "Good morning, where is the bus stop?"),
    ("Attraversi la strada sulle strisce.", "Cross the road at the crosswalk."),
    ("L'ufficio postale è accanto alla banca.", "The post office is next to the bank."),
    ("Deve prendere la metropolitana, linea rossa.", "You need to take the subway, red line."),
    ("Scenda alla prossima fermata.", "Get off at the next stop."),
    ("Il museo è aperto oggi?", "Is the museum open today?"),
    ("Giri l'angolo e lo vedrà.", "Turn the corner and you'll see it."),
    ("C'è un bancomat in questa zona?", "Is there an ATM in this area?"),
    ("Sì, ce n'è uno davanti alla farmacia.", "Yes, there's one in front of the pharmacy."),
    ("Quanto tempo ci vuole per arrivare?", "How long does it take to get there?"),
    ("Ci vogliono circa venti minuti.", "It takes about twenty minutes."),
    ("È meglio andare in taxi o a piedi?", "Is it better to go by taxi or on foot?"),
    ("È molto vicino, meglio camminare.", "It's very close, better to walk."),
    ("Scusi, cerco l'hotel Michelangelo.", "Excuse me, I'm looking for the Michelangelo hotel."),
    ("È in fondo a questa via.", "It's at the end of this street."),
    ("Giri a destra al secondo semaforo.", "Turn right at the second traffic light."),
    ("Passerà davanti a un grande parco.", "You will pass in front of a large park."),
    ("Non può sbagliare, è un edificio rosso.", "You can't miss it, it's a red building."),
    ("Può mostrarmelo sulla mappa?", "Can you show it to me on the map?"),
    ("Certo, siamo esattamente qui.", "Sure, we are exactly here."),
    ("Devo andare a sinistra o a destra?", "Do I need to go left or right?"),
    ("Vada sempre dritto per un chilometro.", "Keep going straight for one kilometer."),
    ("C'è un parcheggio qui vicino?", "Is there a parking lot nearby?"),
    ("Sì, dietro quel supermercato.", "Yes, behind that supermarket."),
    ("Mi scusi, questa è via Mazzini?", "Excuse me, is this via Mazzini?"),
    ("No, via Mazzini è la prossima parallela.", "No, via Mazzini is the next parallel street."),
    ("Grazie, è stato molto gentile.", "Thank you, you've been very kind."),
    ("Prego, buona giornata!", "You're welcome, have a nice day!"),
    ("Scusi, come si chiama questa piazza?", "Excuse me, what is this square called?"),
    ("Questa è Piazza della Libertà.", "This is Freedom Square."),
    ("Il centro storico è lontano?", "Is the historical center far?"),
    ("No, attraversi il ponte e ci sei.", "No, cross the bridge and you're there."),
    ("Cerco l'ingresso del museo.", "I'm looking for the museum entrance."),
    ("L'ingresso è dall'altra parte del palazzo.", "The entrance is on the other side of the building."),
    ("Mi scusi, sa dove posso comprare i biglietti?", "Excuse me, do you know where I can buy tickets?"),
    ("In edicola o dal tabaccaio.", "At the newsstand or the tobacconist."),
    ("C'è una fontana famosa qui vicino?", "Is there a famous fountain near here?"),
    ("Sì, la Fontana di Trevi è a due passi.", "Yes, the Trevi Fountain is a stone's throw away."),
    ("È questa la direzione per il Vaticano?", "Is this the direction for the Vatican?"),
    ("Sì, continui così fino al fiume.", "Yes, keep going like this until the river."),
    ("C'è un punto panoramico?", "Is there a panoramic viewpoint?"),
    ("Sì, salga sulla collina a sinistra.", "Yes, go up the hill on the left."),
    ("La vista da lassù è bellissima.", "The view from up there is beautiful."),
    ("Grazie mille, gentilissimo!", "Thank you very much, so kind!"),
    ("Figurati, buona vacanza!", "No problem, have a nice holiday!"),
    ("Scusi, saprebbe indicarmi l'ospedale?", "Excuse me, could you point me to the hospital?"),
    ("Sì, segua i cartelli stradali blu.", "Yes, follow the blue road signs.")
]

items = []
for i, (it, en) in enumerate(sentences_data):
    others = [d for d in sentences_data if d[0] != it]
    sampled_others = random.sample(others, 3)
    dist_it = [s[0] for s in sampled_others]
    dist_en = [s[1] for s in sampled_others]

    choices_it = [it] + dist_it
    choices_en = [en] + dist_en
    combined = list(zip(choices_it, choices_en))
    random.shuffle(combined)
    choices_it, choices_en = zip(*combined)
    
    item = {
        "id": f"{s_code}-s{i+1}",
        "italian": it,
        "english": en,
        "type": "sentence",
        "choicesItalian": list(choices_it),
        "choicesEnglish": list(choices_en),
        "correctAnswerItalian": it,
        "correctAnswerEnglish": en,
        "feedback": {
          "correctItalian": "Perfetto!",
          "incorrectItalian": f"No, la risposta è \"{it}\".",
          "correctEnglish": "Perfect!",
          "incorrectEnglish": f"No, the answer is \"{en}\"."
        }
    }
    items.append(item)

with open(f"/home/waseageru/parli-italiano/src/data/exports/travel/{scenario}/travel_{scenario}_sentences.json", "w") as f:
    json.dump(items, f, indent=2, ensure_ascii=False)
