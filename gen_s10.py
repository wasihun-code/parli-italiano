import json
import random

scenario = "renting_a_car"
s_code = "s10"
path = f"/home/waseageru/parli-italiano/src/data/exports/travel/{scenario}/"

def save_json(items, filename):
    with open(path + filename, "w") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

def create_items(data, item_type, s_code):
    items = []
    prefix = item_type[0]
    for i, (it, en) in enumerate(data):
        others = [d for d in data if d[0] != it]
        sampled_others = random.sample(others, 3)
        choices_it = [it] + [s[0] for s in sampled_others]
        choices_en = [en] + [s[1] for s in sampled_others]
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        
        item = {
            "id": f"{s_code}-{prefix}{i+1}",
            "italian": it,
            "english": en,
            "type": item_type,
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
              "correctItalian": "Ottimo!" if item_type == "vocabulary" else "Esatto!" if item_type == "phrase" else "Perfetto!",
              "incorrectItalian": f"No, la risposta è \"{it}\".",
              "correctEnglish": "Great!" if item_type == "vocabulary" else "Exactly!" if item_type == "phrase" else "Perfect!",
              "incorrectEnglish": f"No, the answer is \"{en}\"."
            }
        }
        items.append(item)
    return items

# Vocabulary (50+)
vocab_data = [
    ("auto", "car"), ("prenotazione", "reservation"), ("patente", "driver's license"),
    ("carta di credito", "credit card"), ("chiavi", "keys"), ("parcheggio", "parking lot"),
    ("pieno", "full tank"), ("assicurazione", "insurance"), ("franchigia", "deductible"),
    ("danno", "damage"), ("ricevuta", "receipt"), ("noleggio", "rental"),
    ("carburante", "fuel"), ("benzina", "gasoline"), ("diesel", "diesel"),
    ("manuale", "manual"), ("automatico", "automatic"), ("categoria", "category"),
    ("economica", "economy"), ("media", "mid-size"), ("lusso", "luxury"),
    ("baule", "trunk"), ("sedile", "seat"), ("volante", "steering wheel"),
    ("freno", "brake"), ("acceleratore", "accelerator"), ("frizione", "clutch"),
    ("cambio", "gearbox"), ("motore", "engine"), ("gomma", "tire"),
    ("ruota di scorta", "spare tire"), ("fari", "headlights"), ("climatizzatore", "air conditioning"),
    ("navigatore", "GPS"), ("seggiolino", "child seat"), ("specchietto", "mirror"),
    ("parabrezza", "windshield"), ("tergicristalli", "wipers"), ("carrozzeria", "bodywork"),
    ("cristalli", "glass/windows"), ("ritiro", "pick-up"), ("consegna", "return"),
    ("restituzione", "return"), ("contratto", "contract"), ("firma", "signature"),
    ("multa", "fine"), ("autostrada", "highway"), ("pedaggio", "toll"),
    ("limite di velocità", "speed limit"), ("incidente", "accident"), ("soccorso stradale", "roadside assistance"),
    ("km illimitati", "unlimited mileage")
]

# Phrases (50+)
phrases_data = [
    ("Ho una prenotazione", "I have a reservation"), ("A nome Smith", "Under the name Smith"),
    ("Ecco la mia patente", "Here is my license"), ("È valida in Italia?", "Is it valid in Italy?"),
    ("Quanto costa al giorno?", "How much does it cost per day?"), ("È inclusa l'assicurazione?", "Is insurance included?"),
    ("Vorrei aggiungere la kasko", "I'd like to add full insurance"), ("Senza franchigia", "Without deductible"),
    ("Dov'è l'auto?", "Where is the car?"), ("Posto numero venti", "Spot number twenty"),
    ("Faccia il pieno", "Fill it up"), ("Pieno-pieno", "Full-to-full"),
    ("Devo riconsegnarla qui?", "Do I have to return it here?"), ("Dove lascio le chiavi?", "Where do I leave the keys?"),
    ("L'auto è graffiata", "The car is scratched"), ("C'è un piccolo danno", "There is a small damage"),
    ("Controllo l'auto", "I'm checking the car"), ("Tutto a posto", "Everything's fine"),
    ("Firmi qui", "Sign here"), ("La ricevuta, per favore", "The receipt, please"),
    ("Il serbatoio è pieno", "The tank is full"), ("Posso avere un seggiolino?", "Can I have a child seat?"),
    ("L'auto è diesel o benzina?", "Is the car diesel or gas?"), ("Cambio manuale", "Manual transmission"),
    ("Cambio automatico", "Automatic transmission"), ("Quanto dista l'aeroporto?", "How far is the airport?"),
    ("Posso guidare all'estero?", "Can I drive abroad?"), ("Serve un secondo conducente", "A second driver is needed"),
    ("A che ora chiudete?", "What time do you close?"), ("Il parcheggio è gratuito?", "Is parking free?"),
    ("Ho forato una gomma", "I have a flat tire"), ("L'auto non parte", "The car won't start"),
    ("Chiami il soccorso", "Call assistance"), ("Mi serve un navigatore", "I need a GPS"),
    ("L'auto è troppo piccola", "The car is too small"), ("Vorrei una categoria superiore", "I'd like a higher category"),
    ("Quanto è il deposito?", "How much is the deposit?"), ("Sulla carta di credito", "On the credit card"),
    ("Torni tra un'ora", "Come back in an hour"), ("Ecco le chiavi", "Here are the keys"),
    ("Buon viaggio!", "Have a good trip!"), ("Guidi con prudenza", "Drive carefully"),
    ("Controlli il livello dell'olio", "Check the oil level"), ("Pressione delle gomme", "Tire pressure"),
    ("Non trovo il tappo della benzina", "I can't find the gas cap"), ("Si apre da qui", "It opens from here"),
    ("È un'auto ibrida", "It's a hybrid car"), ("Dov'è la stazione di servizio?", "Where is the gas station?"),
    ("Grazie per l'aiuto", "Thanks for the help"), ("A presto", "See you soon"),
    ("Buona giornata", "Have a good day"), ("Arrivederci", "Goodbye")
]

# Sentences (60+)
sentences_data = [
    ("Buongiorno, ho prenotato un'auto per tre giorni.", "Good morning, I've booked a car for three days."),
    ("Mi servono la sua patente e una carta di credito.", "I need your license and a credit card."),
    ("La mia patente è internazionale, va bene?", "My license is international, is that okay?"),
    ("Sì, è perfettamente valida per guidare in Italia.", "Yes, it is perfectly valid for driving in Italy."),
    ("L'auto è parcheggiata al posto numero ventidue.", "The car is parked in spot number twenty-two."),
    ("Devo riconsegnare l'auto con il serbatoio pieno?", "Do I have to return the car with a full tank?"),
    ("Sì, se non fa il pieno addebiteremo il costo del carburante.", "Yes, if you don't fill it up we will charge for the fuel."),
    ("Vorrebbe aggiungere un'assicurazione completa?", "Would you like to add full insurance?"),
    ("L'assicurazione copre anche i danni ai cristalli?", "Does the insurance also cover damage to the windows?"),
    ("Sì, la kasko completa elimina ogni franchigia.", "Yes, full insurance eliminates any deductible."),
    ("Firmi il contratto di noleggio qui in basso.", "Sign the rental contract here at the bottom."),
    ("Ecco le chiavi e la copia del contratto.", "Here are the keys and the copy of the contract."),
    ("Dove posso trovare l'auto nel parcheggio?", "Where can I find the car in the parking lot?"),
    ("Esca dall'ufficio e segua le indicazioni per il settore B.", "Exit the office and follow the signs for sector B."),
    ("C'è già un graffio sulla portiera sinistra.", "There is already a scratch on the left door."),
    ("Lo segno subito sulla scheda dei danni.", "I'll mark it immediately on the damage report."),
    ("Vorrei noleggiare un'auto con il cambio automatico.", "I'd like to rent a car with automatic transmission."),
    ("Mi dispiace, al momento abbiamo solo auto manuali.", "I'm sorry, at the moment we only have manual cars."),
    ("Quanto costa aggiungere un secondo conducente?", "How much does it cost to add a second driver?"),
    ("Costa dieci euro in più al giorno.", "It costs ten euros more per day."),
    ("L'auto ha il navigatore satellitare incluso?", "Does the car have a satellite navigator included?"),
    ("Sì, il GPS è già integrato nel cruscotto.", "Yes, the GPS is already integrated into the dashboard."),
    ("C'è un limite di chilometri giornaliero?", "Is there a daily mileage limit?"),
    ("No, il noleggio include chilometri illimitati.", "No, the rental includes unlimited mileage."),
    ("Cosa devo fare in caso di incidente?", "What should I do in case of an accident?"),
    ("Chiami subito il nostro numero di assistenza stradale.", "Call our roadside assistance number immediately."),
    ("Il numero è scritto sul retro del contratto.", "The number is written on the back of the contract."),
    ("Buongiorno, devo riconsegnare quest'auto.", "Good morning, I have to return this car."),
    ("Ha fatto il pieno di benzina prima di arrivare?", "Did you fill up with gas before arriving?"),
    ("Sì, ho la ricevuta dell'ultimo rifornimento.", "Yes, I have the receipt from the last fill-up."),
    ("Controllo se ci sono nuovi danni alla carrozzeria.", "I'm checking if there are new damages to the bodywork."),
    ("L'auto è in perfette condizioni, grazie.", "The car is in perfect condition, thank you."),
    ("Le invieremo la fattura finale via email.", "We will send you the final invoice by email."),
    ("Posso lasciare l'auto in un'altra città?", "Can I leave the car in another city?"),
    ("Sì, ma c'è un supplemento per il viaggio di sola andata.", "Yes, but there's a supplement for the one-way trip."),
    ("A che ora apre l'ufficio domani mattina?", "What time does the office open tomorrow morning?"),
    ("Apriamo alle sette per le riconsegne anticipate.", "We open at seven for early returns."),
    ("Posso avere un seggiolino per un bambino di tre anni?", "Can I have a child seat for a three-year-old?"),
    ("Certamente, glielo porto subito all'auto.", "Certainly, I'll bring it to the car right away."),
    ("L'auto usa benzina senza piombo o diesel?", "Does the car use unleaded gas or diesel?"),
    ("Questa macchina va a gasolio, mi raccomando.", "This car runs on diesel, please take note."),
    ("Dove si trova il distributore più vicino?", "Where is the nearest gas station?"),
    ("Giri a destra all'uscita del parcheggio.", "Turn right at the parking lot exit."),
    ("Ho perso le chiavi della macchina, cosa faccio?", "I lost the car keys, what do I do?"),
    ("Dobbiamo mandare un carro attrezzi con il duplicato.", "We have to send a tow truck with the duplicate."),
    ("Il costo della chiave smarrita è a suo carico.", "The cost of the lost key is your responsibility."),
    ("Quanto è il deposito cauzionale?", "How much is the security deposit?"),
    ("Bloccheremo ottocento euro sulla sua carta.", "We will block eight hundred euros on your card."),
    ("La somma verrà sbloccata alla riconsegna.", "The amount will be unblocked upon return."),
    ("C'è il triangolo di emergenza nel baule?", "Is there an emergency triangle in the trunk?"),
    ("Sì, e c'è anche il giubbotto catarifrangente.", "Yes, and there's also the reflective vest."),
    ("Come si accendono i fari antinebbia?", "How do you turn on the fog lights?"),
    ("Usi la manopola a sinistra del volante.", "Use the knob to the left of the steering wheel."),
    ("Grazie, è stato molto chiaro e gentile.", "Thank you, you've been very clear and kind."),
    ("Spero che l'auto le piaccia, buon viaggio!", "I hope you like the car, have a good trip!"),
    ("Mi scusi, il climatizzatore non sembra funzionare.", "Excuse me, the air conditioning doesn't seem to work."),
    ("Provo a controllare io, forse è solo un'impostazione.", "Let me check, maybe it's just a setting."),
    ("Ah ecco, adesso esce l'aria fredda.", "Ah here, now cold air is coming out."),
    ("Grazie ancora, arrivederci.", "Thanks again, goodbye."),
    ("Si ricordi di allacciare sempre le cinture.", "Remember to always fasten your seat belts."),
    ("In Italia i fari devono essere accesi anche di giorno.", "In Italy, headlights must be on even during the day.")
]

save_json(create_items(vocab_data, "vocabulary", s_code), f"travel_{scenario}_vocabulary.json")
save_json(create_items(phrases_data, "phrase", s_code), f"travel_{scenario}_phrases.json")
save_json(create_items(sentences_data, "sentence", s_code), f"travel_{scenario}_sentences.json")
