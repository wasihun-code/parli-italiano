import json
import os
import random

def generate_hotel_check_out():
    scenario = "hotel_check_out"
    prefix = "s18"
    base_path = f"src/data/exports/accommodation/{scenario}/"
    
    # Vocabulary
    vocab_list = [
        ("il check-out", "the check-out"), ("la partenza", "the departure"), ("il conto", "the bill"),
        ("il saldo", "the balance"), ("la ricevuta", "the receipt"), ("la fattura", "the invoice"),
        ("il minibar", "the minibar"), ("l'acqua minerale", "the mineral water"), ("la consumazione", "the consumption/drink"),
        ("il totale", "the total"), ("il pagamento", "the payment"), ("la carta di credito", "the credit card"),
        ("il PIN", "the PIN"), ("il deposito bagagli", "the luggage storage"), ("la valigia", "the suitcase"),
        ("il treno", "the train"), ("la stazione", "the station"), ("il taxi", "the taxi"),
        ("il soggiorno", "the stay"), ("piacevole", "pleasant"), ("la chiave", "the key"),
        ("la stanza", "the room"), ("gratuito", "free of charge"), ("la disponibilità", "the availability"),
        ("il servizio", "the service"), ("l'ospite", "the guest"), ("il supplemento", "the extra charge"),
        ("la colazione", "the breakfast"), ("il pranzo", "the lunch"), ("la cena", "the dinner"),
        ("il portiere", "the doorman/porter"), ("l'ascensore", "the elevator"), ("il piano", "the floor"),
        ("la camera", "the room"), ("il numero", "the number"), ("la firma", "the signature"),
        ("il documento", "the document"), ("il passaporto", "the passport"), ("la mancia", "the tip"),
        ("la prenotazione", "the reservation"), ("il viaggio", "the trip"), ("la destinazione", "the destination"),
        ("l'aeroporto", "the airport"), ("la navetta", "the shuttle"), ("l'orario", "the time/schedule"),
        ("il ritardo", "the delay"), ("la conferma", "the confirmation"), ("il modulo", "the form"),
        ("la cassa", "the cashier/desk"), ("il contante", "the cash"), ("il bancomat", "the debit card"),
        ("il vassoio", "the tray"), ("la pulizia", "the cleaning"), ("il cambio", "the change")
    ]
    
    vocab_data = []
    for i, (it, en) in enumerate(vocab_list):
        choices_it = [it]
        choices_en = [en]
        others = [v for v in vocab_list if v != (it, en)]
        random.seed(i)
        distractors = random.sample(others, 3)
        for d_it, d_en in distractors:
            choices_it.append(d_it)
            choices_en.append(d_en)
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
                "correct": f"Correct! '{it}' is '{en}'.",
                "incorrect": f"Wrong. '{it}' means '{en}'."
            }
        })

    # Phrases
    phrase_list = [
        ("Fare il check-out", "To check out"), ("Camera duecentododici", "Room two twelve"),
        ("Com'è stato il soggiorno?", "How was your stay?"), ("Molto piacevole", "Very pleasant"),
        ("Consumato qualcosa?", "Consumed anything?"), ("Dal minibar", "From the minibar"),
        ("Un'acqua minerale", "A mineral water"), ("Conto totale", "Total bill"),
        ("Tassa di soggiorno", "City tax"), ("Pagare con carta", "To pay by card"),
        ("Inserisca la carta", "Insert the card"), ("Digiti il PIN", "Type the PIN"),
        ("Lasciare la camera", "To leave the room"), ("Ricevuta del saldo", "Balance receipt"),
        ("Il nostro treno", "Our train"), ("Parte stasera", "Leaves tonight"),
        ("Alle sei", "At six"), ("Deposito valigie", "Luggage storage"),
        ("Stanza chiusa a chiave", "Locked room"), ("Venire a riprenderle", "To come pick them up"),
        ("Servizio gratuito", "Free service"), ("Grazie mille", "Many thanks"),
        ("Per i nostri ospiti", "For our guests"), ("Chiamare un taxi", "To call a taxi"),
        ("Andare in aeroporto", "To go to the airport"), ("C'è un supplemento?", "Is there a surcharge?"),
        ("Tutto compreso", "All included"), ("Posso avere la fattura?", "Can I have the invoice?"),
        ("A nome dell'azienda", "Under the company name"), ("Spero di tornare", "I hope to return"),
        ("Buon viaggio", "Have a good trip"), ("Ci vediamo presto", "See you soon"),
        ("Tutto a posto", "Everything is fine"), ("Check-out veloce", "Express check-out"),
        ("Chiave della camera", "Room key"), ("Sul bancone", "On the counter"),
        ("Pagamento effettuato", "Payment made"), ("Resto del conto", "Rest of the bill"),
        ("Orario di partenza", "Departure time"), ("Navetta per la stazione", "Shuttle to the station"),
        ("Bagagli pesanti", "Heavy luggage"), ("Aiuto con le borse", "Help with the bags"),
        ("Reception aperta", "Reception open"), ("Fino alle undici", "Until eleven"),
        ("Tardi per la colazione", "Late for breakfast"), ("Un momento solo", "Just a moment"),
        ("Controllo subito", "Checking right away"), ("Firma qui", "Sign here"),
        ("Ecco il resto", "Here is the change"), ("Scontrino fiscale", "Fiscal receipt"),
        ("Grazie per tutto", "Thanks for everything"), ("Alla prossima volta", "Until next time")
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
                "correct": f"Excellent! '{it}' translates to '{en}'.",
                "incorrect": f"No, '{it}' means '{en}'."
            }
        })

    # Sentences
    sentence_list = [
        ("Buongiorno, vorremmo fare il check-out.", "Good morning, we would like to check out."),
        ("Siamo nella camera duecentododici.", "We are in room two hundred twelve."),
        ("Com'è stato il vostro soggiorno qui?", "How was your stay here?"),
        ("È stato molto piacevole, grazie di tutto.", "It was very pleasant, thanks for everything."),
        ("Avete consumato qualcosa dal minibar?", "Did you consume anything from the minibar?"),
        ("Abbiamo preso solo un'acqua minerale.", "We only took a mineral water."),
        ("Ecco il conto totale del vostro soggiorno.", "Here is the total bill for your stay."),
        ("Il conto comprende anche la tassa di soggiorno.", "The bill also includes the city tax."),
        ("Posso pagare con la mia carta di credito?", "Can I pay with my credit card?"),
        ("Certamente. Inserisca pure la carta nel lettore.", "Certainly. Please insert the card into the reader."),
        ("Deve digitare il suo PIN per confermare.", "You need to type your PIN to confirm."),
        ("Salve, avremmo bisogno di lasciare la camera ora.", "Hello, we need to leave the room now."),
        ("Ecco a lei la ricevuta del saldo finale.", "Here is the receipt for the final balance."),
        ("Il nostro treno parte stasera alle sei.", "Our train leaves tonight at six."),
        ("È possibile lasciare le valigie qui in deposito?", "Is it possible to leave the suitcases here in storage?"),
        ("Abbiamo un'apposita stanza chiusa a chiave per i bagagli.", "We have a special locked room for luggage."),
        ("Potete venire a riprenderle quando volete oggi.", "You can come pick them up whenever you want today."),
        ("Questo servizio è gratuito per gli ospiti?", "Is this service free for guests?"),
        ("Sì, il deposito bagagli è gratuito.", "Yes, luggage storage is free."),
        ("Ottimo, grazie mille per la vostra disponibilità.", "Great, thanks a lot for your availability."),
        ("Vorrei la fattura a nome della mia azienda.", "I would like the invoice under my company name."),
        ("Mi servono i dati completi per la fatturazione.", "I need the full details for billing."),
        ("Può chiamarmi un taxi per la stazione?", "Can you call me a taxi for the station?"),
        ("Il taxi sarà qui tra cinque minuti.", "The taxi will be here in five minutes."),
        ("A che ora dobbiamo lasciare la camera?", "What time do we have to leave the room?"),
        ("Il check-out deve essere fatto entro le undici.", "Check-out must be done by eleven."),
        ("È possibile avere un check-out posticipato?", "Is it possible to have a late check-out?"),
        ("Dipende dalla disponibilità delle camere per oggi.", "It depends on the availability of rooms for today."),
        ("Dobbiamo pagare un supplemento per il ritardo?", "Do we have to pay a surcharge for the delay?"),
        ("Sì, dopo mezzogiorno c'è un piccolo costo extra.", "Yes, after noon there is a small extra cost."),
        ("Ecco le chiavi della camera, le lascio qui.", "Here are the room keys, I'll leave them here."),
        ("Tutto il minibar è stato incluso nel conto?", "Was the entire minibar included in the bill?"),
        ("No, abbiamo aggiunto solo le bevande di ieri.", "No, we only added yesterday's drinks."),
        ("Posso pagare una parte in contanti?", "Can I pay part in cash?"),
        ("Certamente, possiamo dividere il pagamento.", "Certainly, we can split the payment."),
        ("Mi dà una busta per la ricevuta, per favore?", "Can you give me an envelope for the receipt, please?"),
        ("Ecco a lei, spero che torniate presto a trovarci.", "Here you go, I hope you come back to visit us soon."),
        ("Il viaggio è stato lungo ma molto bello.", "The trip was long but very beautiful."),
        ("Avete bisogno di aiuto per portare giù le valigie?", "Do you need help bringing the suitcases down?"),
        ("Sì, se possibile vorrei un facchino.", "Yes, if possible I would like a porter."),
        ("Mando subito qualcuno al secondo piano.", "I'm sending someone to the second floor right away."),
        ("C'è una navetta gratuita per l'aeroporto?", "Is there a free shuttle to the airport?"),
        ("La prossima navetta parte tra venti minuti.", "The next shuttle leaves in twenty minutes."),
        ("Dove posso aspettare la navetta?", "Where can I wait for the shuttle?"),
        ("Può accomodarsi nella hall, la avviseremo noi.", "You can take a seat in the lobby, we'll notify you."),
        ("Grazie per la vostra cortesia durante il soggiorno.", "Thanks for your courtesy during the stay."),
        ("È stato un piacere avervi come nostri ospiti.", "It was a pleasure having you as our guests."),
        ("Vi auguro un buon proseguimento di viaggio.", "I wish you a good continuation of your trip."),
        ("Arrivederci e buona giornata!", "Goodbye and have a nice day!"),
        ("Grazie, anche a lei e a tutto lo staff.", "Thanks, to you too and to all the staff."),
        ("La colazione di stamattina era eccellente.", "This morning's breakfast was excellent."),
        ("Mi fa molto piacere, lo riferirò allo chef.", "I'm very pleased, I'll tell the chef."),
        ("Posso lasciare un commento positivo online?", "Can I leave a positive comment online?"),
        ("Sì, ci aiuterebbe molto, grazie!", "Yes, it would help us a lot, thanks!"),
        ("Ecco il mio biglietto da visita per il futuro.", "Here is my business card for the future."),
        ("Lo terrò senz'altro, a presto.", "I'll certainly keep it, see you soon."),
        ("Il telecomando è rimasto in camera.", "The remote control stayed in the room."),
        ("Non si preoccupi, lo recupereranno le pulizie.", "Don't worry, the cleaners will retrieve it."),
        ("Abbiamo dimenticato un caricabatterie.", "We forgot a charger."),
        ("Controlliamo subito se è ancora lì.", "We'll check right away if it's still there."),
        ("Sì, eccolo, lo avevamo appena trovato.", "Yes, here it is, we had just found it.")
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
                "correct": f"Well done! '{it}' means '{en}'.",
                "incorrect": f"Incorrect. '{en}' is '{it}' in Italian."
            }
        })

    with open(os.path.join(base_path, f"{scenario}_vocabulary.json"), "w") as f:
        json.dump(vocab_data, f, indent=2, ensure_ascii=False)
    with open(os.path.join(base_path, f"{scenario}_phrases.json"), "w") as f:
        json.dump(phrase_data, f, indent=2, ensure_ascii=False)
    with open(os.path.join(base_path, f"{scenario}_sentences.json"), "w") as f:
        json.dump(sentence_data, f, indent=2, ensure_ascii=False)

generate_hotel_check_out()
