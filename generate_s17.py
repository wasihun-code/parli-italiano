import json
import os

def generate_hotel_check_in():
    scenario = "hotel_check_in"
    prefix = "s17"
    base_path = f"src/data/exports/accommodation/{scenario}/"
    
    # Vocabulary
    vocab_list = [
        ("il check-in", "the check-in"), ("la prenotazione", "the reservation"), ("il nome", "the name"),
        ("il cognome", "the last name"), ("la camera", "the room"), ("doppia", "double"),
        ("singola", "single"), ("le notti", "the nights"), ("i documenti", "the documents"),
        ("il passaporto", "the passport"), ("le chiavi", "the keys"), ("il terzo piano", "the third floor"),
        ("l'ascensore", "the elevator"), ("il corridoio", "the corridor"), ("la colazione", "the breakfast"),
        ("la sala", "the hall/room"), ("il piano terra", "the ground floor"), ("il ritardo", "the delay"),
        ("la carta di credito", "the credit card"), ("la garanzia", "the guarantee"), ("l'identità", "the identity"),
        ("i contanti", "the cash"), ("il garage", "the garage"), ("sotterraneo", "underground"),
        ("il pass", "the pass"), ("il parcheggio", "the parking"), ("la disponibilità", "the availability"),
        ("la conferma", "the confirmation"), ("il modulo", "the form"), ("la firma", "the signature"),
        ("la ricevuta", "the receipt"), ("la tassa di soggiorno", "the city tax"), ("il wifi", "the wifi"),
        ("la password", "the password"), ("l'aria condizionata", "the air conditioning"), ("il riscaldamento", "the heating"),
        ("il ricevimento", "the front desk"), ("il receptionist", "the receptionist"), ("l'ospite", "the guest"),
        ("la valigia", "the suitcase"), ("il bagaglio", "the luggage"), ("il deposito", "the storage"),
        ("la mappa", "the map"), ("il centro", "the center"), ("la fermata", "the stop"),
        ("il taxi", "the taxi"), ("il ristorante", "the restaurant"), ("il bar", "the bar"),
        ("l'orario", "the schedule"), ("l'uscita", "the exit"), ("il bagno", "the bathroom"),
        ("il balcone", "the balcony"), ("la vista", "the view"), ("la cassaforte", "the safe")
    ]
    
    vocab_data = []
    for i, (it, en) in enumerate(vocab_list):
        choices_it = [it]
        choices_en = [en]
        # Simple distractors
        others = [v for v in vocab_list if v != (it, en)]
        import random
        random.seed(i)
        distractors = random.sample(others, 3)
        for d_it, d_en in distractors:
            choices_it.append(d_it)
            choices_en.append(d_en)
        
        # Shuffle aligned
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        
        vocab_data.append({
            "id": f"{prefix}-v{i+1:02d}",
            "type": "vocabulary",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Correct! '{it}' means '{en}'.",
                "incorrect": f"Not quite. '{it}' translates to '{en}'."
            }
        })

    # Phrases
    phrase_list = [
        ("A nome Rossi", "Under the name Rossi"), ("Una camera doppia", "A double room"),
        ("Per tre notti", "For three nights"), ("I vostri documenti", "Your documents"),
        ("Ecco le chiavi", "Here are the keys"), ("Al terzo piano", "On the third floor"),
        ("In fondo al corridoio", "At the end of the corridor"), ("Dalle sette alle dieci", "From seven to ten"),
        ("Al piano terra", "On the ground floor"), ("Scusi per il ritardo", "Sorry for the delay"),
        ("Per una singola", "For a single room"), ("Nessun problema", "No problem"),
        ("Il nome, prego?", "The name, please?"), ("Mi serve una carta", "I need a card"),
        ("Dati della carta", "Card details"), ("In contanti", "In cash"),
        ("Al check-out", "At check-out"), ("Garage sotterraneo", "Underground garage"),
        ("Ecco il pass", "Here is the pass"), ("Parcheggio incluso", "Parking included"),
        ("Prenotazione confermata", "Reservation confirmed"), ("Modulo da firmare", "Form to sign"),
        ("Tassa inclusa", "Tax included"), ("Wifi gratuito", "Free wifi"),
        ("Chiave magnetica", "Magnetic key"), ("Numero della camera", "Room number"),
        ("Deposito bagagli", "Luggage storage"), ("Mappa della città", "City map"),
        ("Centro storico", "Historic center"), ("Fermata dell'autobus", "Bus stop"),
        ("Prenotare un taxi", "To book a taxi"), ("Colazione servita", "Breakfast served"),
        ("Aria condizionata", "Air conditioning"), ("Riscaldamento centrale", "Central heating"),
        ("Codice d'accesso", "Access code"), ("Porta d'ingresso", "Entrance door"),
        ("Fino a mezzanotte", "Until midnight"), ("Domani mattina", "Tomorrow morning"),
        ("Questa sera", "This evening"), ("Buon soggiorno", "Enjoy your stay"),
        ("Buona permanenza", "Have a good stay"), ("Non si preoccupi", "Don't worry"),
        ("Tutto a posto", "All set / Everything ok"), ("In fondo a sinistra", "At the end on the left"),
        ("Sulla destra", "On the right"), ("Piano superiore", "Upper floor"),
        ("Camera non fumatori", "Non-smoking room"), ("Letto matrimoniale", "Double bed"),
        ("Letti separati", "Twin beds"), ("Vista mare", "Sea view"),
        ("Senza ascensore", "Without elevator"), ("Bagno privato", "Private bathroom")
    ]
    
    phrase_data = []
    for i, (it, en) in enumerate(phrase_list):
        choices_it = [it]
        choices_en = [en]
        others = [p for p in phrase_list if p != (it, en)]
        random.seed(i+100)
        distractors = random.sample(others, 3)
        for d_it, d_en in distractors:
            choices_it.append(d_it)
            choices_en.append(d_en)
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        
        phrase_data.append({
            "id": f"{prefix}-p{i+1:02d}",
            "type": "phrase",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Great! '{it}' is correctly translated as '{en}'.",
                "incorrect": f"Actually, '{it}' means '{en}'."
            }
        })

    # Sentences
    sentence_list = [
        ("Buongiorno, abbiamo una prenotazione a nome Rossi.", "Good morning, we have a reservation under the name Rossi."),
        ("Sì, una camera doppia per tre notti, corretto?", "Yes, a double room for three nights, correct?"),
        ("Posso avere i vostri documenti, per favore?", "Can I have your documents, please?"),
        ("Ecco qui i nostri passaporti.", "Here are our passports."),
        ("Siete al terzo piano, camera 305.", "You are on the third floor, room 305."),
        ("L'ascensore è in fondo al corridoio.", "The elevator is at the end of the corridor."),
        ("A che ora è la colazione?", "What time is breakfast?"),
        ("La colazione è servita dalle 7:00 alle 10:00.", "Breakfast is served from 7:00 to 10:00."),
        ("Buonasera, scusi per il ritardo.", "Good evening, sorry for the delay."),
        ("Abbiamo una prenotazione per una singola.", "We have a reservation for a single room."),
        ("Mi serve una carta di credito per la garanzia.", "I need a credit card for the guarantee."),
        ("Posso pagare in contanti al check-out?", "Can I pay in cash at check-out?"),
        ("Sì, certo. Al momento prendiamo solo i dati.", "Yes, of course. For now we only take the details."),
        ("C'è il parcheggio incluso nella prenotazione?", "Is parking included in the reservation?"),
        ("Può parcheggiare nel garage sotterraneo.", "You can park in the underground garage."),
        ("Ecco il pass per l'auto.", "Here is the car pass."),
        ("Vorrei fare il check-in, per favore.", "I would like to check in, please."),
        ("Il mio cognome è Bianchi.", "My last name is Bianchi."),
        ("Devo firmare questo modulo?", "Do I need to sign this form?"),
        ("La colazione è inclusa nel prezzo?", "Is breakfast included in the price?"),
        ("Dov'è la sala colazione?", "Where is the breakfast room?"),
        ("Si trova al piano terra.", "It is on the ground floor."),
        ("Qual è la password del wifi?", "What is the wifi password?"),
        ("C'è l'aria condizionata in camera?", "Is there air conditioning in the room?"),
        ("Sì, è telecomandata.", "Yes, it is remote-controlled."),
        ("Posso lasciare i bagagli qui?", "Can I leave the luggage here?"),
        ("Certamente, abbiamo un deposito.", "Certainly, we have a storage room."),
        ("A che ora apre la reception?", "What time does the front desk open?"),
        ("La reception è aperta ventiquattr'ore su ventiquattro.", "The front desk is open twenty-four hours a day."),
        ("Potrebbe darmi una mappa della città?", "Could you give me a map of the city?"),
        ("Il centro è raggiungibile a piedi?", "Can the center be reached on foot?"),
        ("Sì, dista solo dieci minuti.", "Yes, it's only ten minutes away."),
        ("Dov'è la fermata dell'autobus più vicina?", "Where is the nearest bus stop?"),
        ("Può chiamarmi un taxi per domani?", "Can you call me a taxi for tomorrow?"),
        ("A che ora deve essere qui?", "What time should it be here?"),
        ("Alle otto di mattina, grazie.", "At eight in the morning, thanks."),
        ("Ecco la chiave magnetica per la camera.", "Here is the magnetic key for the room."),
        ("La sua camera ha la vista mare.", "Your room has a sea view."),
        ("C'è una cassaforte in camera?", "Is there a safe in the room?"),
        ("Sì, si trova dentro l'armadio.", "Yes, it is inside the closet."),
        ("Mi scusi, il wifi non sembra funzionare.", "Excuse me, the wifi doesn't seem to work."),
        ("Provo a riavviare il router.", "I'll try to restart the router."),
        ("La camera è già pronta?", "Is the room ready yet?"),
        ("Sì, può salire subito.", "Yes, you can go up right away."),
        ("Dobbiamo compilare questi documenti.", "We need to fill out these documents."),
        ("La tassa di soggiorno si paga a parte.", "The city tax is paid separately."),
        ("Quanto costa la tassa di soggiorno?", "How much is the city tax?"),
        ("Sono due euro a persona al giorno.", "It's two euros per person per day."),
        ("Va bene, pagheremo tutto alla fine.", "Alright, we will pay everything at the end."),
        ("Avete bisogno di aiuto con le valigie?", "Do you need help with the suitcases?"),
        ("No grazie, facciamo da soli.", "No thanks, we'll do it ourselves."),
        ("Il codice per il portone è 1234.", "The code for the front door is 1234."),
        ("Buon soggiorno presso di noi!", "Enjoy your stay with us!"),
        ("Grazie, molto gentile.", "Thank you, very kind."),
        ("Spero che la camera sia di vostro gradimento.", "I hope the room is to your liking."),
        ("Il riscaldamento è automatico.", "The heating is automatic."),
        ("C'è un frigobar in camera?", "Is there a minibar in the room?"),
        ("Sì, i prezzi sono sul listino.", "Yes, the prices are on the list."),
        ("Posso avere un cuscino in più?", "Can I have an extra pillow?"),
        ("Certamente, glielo porto subito.", "Certainly, I'll bring it to you right away.")
    ]
    
    sentence_data = []
    for i, (it, en) in enumerate(sentence_list):
        choices_it = [it]
        choices_en = [en]
        others = [s for s in sentence_list if s != (it, en)]
        random.seed(i+200)
        distractors = random.sample(others, 3)
        for d_it, d_en in distractors:
            choices_it.append(d_it)
            choices_en.append(d_en)
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        
        sentence_data.append({
            "id": f"{prefix}-s{i+1:02d}",
            "type": "sentence",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Excellent! '{it}' means '{en}'.",
                "incorrect": f"Not quite. In Italian, '{en}' is '{it}'."
            }
        })

    with open(os.path.join(base_path, f"{scenario}_vocabulary.json"), "w") as f:
        json.dump(vocab_data, f, indent=2, ensure_ascii=False)
    with open(os.path.join(base_path, f"{scenario}_phrases.json"), "w") as f:
        json.dump(phrase_data, f, indent=2, ensure_ascii=False)
    with open(os.path.join(base_path, f"{scenario}_sentences.json"), "w") as f:
        json.dump(sentence_data, f, indent=2, ensure_ascii=False)

generate_hotel_check_in()
