import json
import random

def gen_feedback(correct_it, correct_en):
    return {
        "correct": "Ottimo! / Great!",
        "incorrect": f"La risposta corretta è / The correct answer is: {correct_it} ({correct_en})"
    }

def get_choices(item_it, item_en, all_it, all_en):
    # Ensure alignment: choices_it[i] == translation of choices_en[i]
    choices_it = [item_it]
    choices_en = [item_en]
    
    others = list(zip(all_it, all_en))
    others = [o for o in others if o[0] != item_it]
    random.shuffle(others)
    
    for i in range(3):
        if i < len(others):
            choices_it.append(others[i][0])
            choices_en.append(others[i][1])
            
    # Shuffle aligned
    combined = list(zip(choices_it, choices_en))
    random.shuffle(combined)
    
    return [c[0] for c in combined], [c[1] for c in combined]

def save_scenario(scenario_id, name, vocab, phrases, sentences):
    path = f"src/data/exports/travel/{name}/"
    
    # Vocab
    v_data = []
    v_it = [v[0] for v in vocab]
    v_en = [v[1] for v in vocab]
    for i, (it, en) in enumerate(vocab):
        c_it, c_en = get_choices(it, en, v_it, v_en)
        v_data.append({
            "id": f"{scenario_id}-v{i+1}",
            "italian": it,
            "english": en,
            "type": "vocabulary",
            "choicesItalian": c_it,
            "choicesEnglish": c_en,
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": gen_feedback(it, en)
        })
    
    # Phrases
    p_data = []
    p_it = [p[0] for p in phrases]
    p_en = [p[1] for p in phrases]
    for i, (it, en) in enumerate(phrases):
        c_it, c_en = get_choices(it, en, p_it, p_en)
        p_data.append({
            "id": f"{scenario_id}-p{i+1}",
            "italian": it,
            "english": en,
            "type": "phrase",
            "choicesItalian": c_it,
            "choicesEnglish": c_en,
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": gen_feedback(it, en)
        })
        
    # Sentences
    s_data = []
    s_it = [s[0] for s in sentences]
    s_en = [s[1] for s in sentences]
    for i, (it, en) in enumerate(sentences):
        c_it, c_en = get_choices(it, en, s_it, s_en)
        s_data.append({
            "id": f"{scenario_id}-s{i+1}",
            "italian": it,
            "english": en,
            "type": "sentence",
            "choicesItalian": c_it,
            "choicesEnglish": c_en,
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": gen_feedback(it, en)
        })
    
    with open(f"{path}travel_{name}_vocabulary.json", "w") as f:
        json.dump(v_data, f, indent=2, ensure_ascii=False)
    with open(f"{path}travel_{name}_phrases.json", "w") as f:
        json.dump(p_data, f, indent=2, ensure_ascii=False)
    with open(f"{path}travel_{name}_sentences.json", "w") as f:
        json.dump(s_data, f, indent=2, ensure_ascii=False)

# Data for s5 train_ticket
s5_vocab = [
    ("biglietto", "ticket"), ("treno", "train"), ("stazione", "station"), ("binario", "platform"), ("partenza", "departure"),
    ("arrivo", "arrival"), ("ritardo", "delay"), ("posto", "seat"), ("classe", "class"), ("prenotazione", "reservation"),
    ("macchinetta", "machine"), ("tastiera", "keyboard"), ("schermo", "screen"), ("pagamento", "payment"), ("regionale", "regional"),
    ("frecciarossa", "high-speed train"), ("venezia", "Venice"), ("pomeriggio", "afternoon"), ("oggi", "today"), ("domani", "tomorrow"),
    ("orario", "schedule"), ("disponibile", "available"), ("scelta", "choice"), ("convalidare", "validate"), ("scadenza", "expiration"),
    ("tratta", "route"), ("aiuto", "help"), ("città", "city"), ("nome", "name"), ("destinazione", "destination"),
    ("elenco", "list"), ("tasto", "button"), ("contanti", "cash"), ("carta", "card"), ("euro", "euro"),
    ("totale", "total"), ("prima", "first"), ("seconda", "second"), ("sedersi", "to sit"), ("assegnato", "assigned"),
    ("valigia", "suitcase"), ("borsa", "bag"), ("passeggero", "passenger"), ("controllore", "conductor"), ("viaggio", "trip"),
    ("fermata", "stop"), ("cambio", "change"), ("coincidenza", "connection"), ("sottopassaggio", "underpass"), ("ufficio", "office")
]
s5_phrases = [
    ("Vorrei un biglietto", "I would like a ticket"), ("Due biglietti", "Two tickets"), ("Per favore", "Please"), ("Grazie mille", "Thank you very much"), ("Quanto costa?", "How much does it cost?"),
    ("Quanto viene?", "How much is it?"), ("In totale", "In total"), ("Prima classe", "First class"), ("Seconda classe", "Second class"), ("Posti disponibili", "Available seats"),
    ("Oggi pomeriggio", "This afternoon"), ("Domani mattina", "Tomorrow morning"), ("Per Venezia", "To Venice"), ("Per Firenze", "To Florence"), ("Treno regionale", "Regional train"),
    ("Treno veloce", "Fast train"), ("Binario dieci", "Platform ten"), ("Solo andata", "One way only"), ("Andata e ritorno", "Round trip"), ("Prenotazione obbligatoria", "Mandatory reservation"),
    ("Posto assegnato", "Assigned seat"), ("Dove vuole", "Wherever you want"), ("Può aiutarmi?", "Can you help me?"), ("Non riesco", "I can't"), ("Selezionare la stazione", "Select the station"),
    ("Scrivere il nome", "Write the name"), ("Sulla tastiera", "On the keyboard"), ("Sullo schermo", "On the screen"), ("Dall'elenco", "From the list"), ("Non la trovavo", "I couldn't find it"),
    ("Scelga l'orario", "Choose the time"), ("Proceda al pagamento", "Proceed to payment"), ("Ecco fatto", "There we go"), ("Necessaria la prenotazione?", "Is reservation needed?"), ("Non c'è", "There isn't"),
    ("Una volta convalidato", "Once validated"), ("Vale quattro ore", "Valid for four hours"), ("Sulla tratta scelta", "On the chosen route"), ("Mi scusi", "Excuse me"), ("Buongiorno", "Good morning"),
    ("Salve", "Hello"), ("Va benissimo", "It's perfect"), ("Quale preferisce?", "Which one do you prefer?"), ("Alle tre", "At three"), ("Alle quattro", "At four"),
    ("In contanti", "In cash"), ("Con carta", "By card"), ("Dov'è la stazione?", "Where is the station?"), ("A che ora parte?", "What time does it leave?"), ("Buon viaggio!", "Have a good trip!")
]
s5_sentences = [
    ("Vorrei due biglietti per il Frecciarossa.", "I would like two tickets for the Frecciarossa."),
    ("Vorrei andare a Venezia oggi pomeriggio.", "I would like to go to Venice this afternoon."),
    ("Ci sono posti disponibili alle quindici e trenta?", "Are there seats available at 15:30?"),
    ("Quello delle sedici e trenta va benissimo.", "The one at 16:30 is perfect."),
    ("Preferisce viaggiare in prima o in seconda classe?", "Do you prefer to travel in first or second class?"),
    ("Sono ottanta euro in totale per i biglietti.", "It is eighty euros in total for the tickets."),
    ("Scusi, può aiutarmi con questa macchinetta?", "Excuse me, can you help me with this machine?"),
    ("Non riesco a selezionare la mia destinazione.", "I can't select my destination."),
    ("Deve scrivere il nome della città sulla tastiera.", "You must write the city name on the keyboard."),
    ("Cercavo di selezionarla dall'elenco ma non c'è.", "I was trying to select it from the list but it's not there."),
    ("Ora scelga l'orario e proceda al pagamento.", "Now choose the time and proceed to payment."),
    ("Grazie mille per l'aiuto, è stato molto gentile.", "Thank you very much for the help, you were very kind."),
    ("È necessaria la prenotazione del posto sul regionale?", "Is seat reservation necessary on the regional train?"),
    ("Sui treni regionali non c'è il posto assegnato.", "On regional trains there is no assigned seat."),
    ("Può sedersi dove vuole se il posto è libero.", "You can sit wherever you want if the seat is free."),
    ("Il biglietto ha una scadenza dopo la convalida?", "Does the ticket have an expiration after validation?"),
    ("Il biglietto vale per quattro ore sulla tratta.", "The ticket is valid for four hours on the route."),
    ("Una volta convalidato, deve salire sul treno.", "Once validated, you must get on the train."),
    ("Il treno per Roma parte dal binario dodici.", "The train to Rome leaves from platform twelve."),
    ("Devo cambiare treno a Bologna per andare a Venezia?", "Do I have to change trains in Bologna to go to Venice?"),
    ("Quanto tempo ho per la coincidenza a Milano?", "How much time do I have for the connection in Milan?"),
    ("Il treno ha venti minuti di ritardo oggi.", "The train is twenty minutes late today."),
    ("Posso pagare con la carta di credito qui?", "Can I pay with a credit card here?"),
    ("Accettate pagamenti in contanti alla biglietteria?", "Do you accept cash payments at the ticket office?"),
    ("Dov'è l'ufficio informazioni della stazione?", "Where is the information office of the station?"),
    ("Il binario sette si trova nel sottopassaggio.", "Platform seven is located in the underpass."),
    ("Deve obliterare il biglietto prima di partire.", "You must validate the ticket before leaving."),
    ("Il controllore passerà tra poco a controllare i biglietti.", "The conductor will come soon to check the tickets."),
    ("Vorrei un posto vicino al finestrino, per favore.", "I would like a seat near the window, please."),
    ("C'è una carrozza ristorante su questo treno?", "Is there a dining car on this train?"),
    ("Posso portare la mia valigia grande a bordo?", "Can I bring my large suitcase on board?"),
    ("Il treno è molto affollato in questo orario.", "The train is very crowded at this time."),
    ("Qual è l'ultima fermata di questa linea?", "What is the last stop of this line?"),
    ("Devo fare il biglietto anche per il cane?", "Do I have to buy a ticket for the dog too?"),
    ("C'è lo sconto per gli studenti o i giovani?", "Is there a discount for students or young people?"),
    ("Vorrei un biglietto di andata e ritorno per Firenze.", "I would like a round trip ticket for Florence."),
    ("A che ora arriva il treno a destinazione?", "What time does the train arrive at the destination?"),
    ("Il binario è stato cambiato all'ultimo momento.", "The platform was changed at the last moment."),
    ("Non trovo il mio posto sulla carrozza cinque.", "I can't find my seat in coach five."),
    ("Scusi, questo posto è libero o occupato?", "Excuse me, is this seat free or occupied?"),
    ("Posso caricare il telefono sul treno?", "Can I charge my phone on the train?"),
    ("C'è il Wi-Fi gratuito a bordo del Frecciarossa?", "Is there free Wi-Fi on board the Frecciarossa?"),
    ("La macchinetta non accetta le mie banconote.", "The machine does not accept my banknotes."),
    ("Ho perso il treno, posso usare lo stesso biglietto?", "I missed the train, can I use the same ticket?"),
    ("Quanto costa il supplemento per la prima classe?", "How much is the supplement for first class?"),
    ("Il treno regionale si ferma in tutte le stazioni.", "The regional train stops at all stations."),
    ("Mi serve una ricevuta per il pagamento del biglietto.", "I need a receipt for the ticket payment."),
    ("Dove posso guardare il tabellone degli arrivi?", "Where can I look at the arrivals board?"),
    ("Il sottopassaggio è l'unico modo per raggiungere il binario.", "The underpass is the only way to reach the platform."),
    ("Attenzione al divario tra il treno e la banchina.", "Mind the gap between the train and the platform."),
    ("Il mio posto è nella carrozza numero tre.", "My seat is in coach number three."),
    ("Posso prenotare il biglietto tramite l'applicazione?", "Can I book the ticket through the app?"),
    ("C'è un'area per i bagagli pesanti a bordo.", "There is an area for heavy luggage on board."),
    ("Il viaggio dura circa tre ore e mezza.", "The trip lasts about three and a half hours."),
    ("Scusi, sa se questo treno va a Venezia?", "Excuse me, do you know if this train goes to Venice?"),
    ("La stazione è chiusa durante la notte.", "The station is closed during the night."),
    ("Devo stampare il biglietto elettronico?", "Do I have to print the electronic ticket?"),
    ("Mi può indicare dov'è il binario quattro?", "Can you show me where platform four is?"),
    ("Il treno per Napoli è al binario nove.", "The train to Naples is at platform nine."),
    ("Buon viaggio a tutti i passeggeri!", "Have a good trip to all passengers!")
]

save_scenario("s5", "train_ticket", s5_vocab, s5_phrases, s5_sentences)

# Data for s6 train_platform
s6_vocab = [
    ("binario", "platform"), ("sottopassaggio", "underpass"), ("cambio", "change"), ("coincidenza", "connection"), ("carrozza", "coach"),
    ("finestrino", "window"), ("annuncio", "announcement"), ("ritardo", "delay"), ("ferroviere", "railway worker"), ("firenze", "Florence"),
    ("milano", "Milan"), ("pisa", "Pisa"), ("tabellone", "board"), ("luminoso", "luminous"), ("tecnico", "technical"),
    ("linea", "line"), ("anziché", "instead of"), ("pesanti", "heavy"), ("tempo", "time"), ("minuti", "minutes"),
    ("valigie", "suitcases"), ("sbrigarsi", "to hurry"), ("capito", "understood"), ("partenza", "departure"), ("arrivato", "arrived"),
    ("convalidare", "validate"), ("salire", "to board"), ("scendere", "to get off"), ("informazione", "information"), ("personale", "staff"),
    ("sicurezza", "safety"), ("gialla", "yellow"), ("limite", "limit"), ("attentione", "attention"), ("prossimo", "next"),
    ("direzione", "direction"), ("fermata", "stop"), ("transito", "transit"), ("viaggiatori", "travelers"), ("bagaglio", "luggage"),
    ("marrone", "brown"), ("perso", "lost"), ("trovato", "found"), ("ufficio", "office"), ("scala", "staircase"),
    ("mobile", "escalator"), ("ascensore", "elevator"), ("uscita", "exit"), ("ingresso", "entrance"), ("biglietteria", "ticket office")
]
s6_phrases = [
    ("Da quale binario?", "From which platform?"), ("Parte dal binario dodici", "Leaves from platform twelve"), ("È già al binario?", "Is it already at the platform?"), ("Arrivato proprio ora", "Just arrived now"), ("Corro subito!", "I'm running right now!"),
    ("Ha molto ritardo?", "Is it very late?"), ("Venti minuti di ritardo", "Twenty minutes late"), ("Problema tecnico", "Technical problem"), ("Sulla linea", "On the line"), ("Rimane il sette", "Remains number seven"),
    ("Tabellone luminoso", "Luminous board"), ("Tra poco", "In a little while"), ("D'accordo", "Agreed"), ("Ho capito bene?", "Did I understand correctly?"), ("Cambiato binario", "Changed platform"),
    ("Appena detto", "Just said"), ("Dal binario quattro", "From platform four"), ("Anziché dal nove", "Instead of nine"), ("Fare il sottopassaggio", "Take the underpass"), ("Valigie pesanti", "Heavy suitcases"),
    ("Fare in tempo", "To be on time"), ("Si sbrighi!", "Hurry up!"), ("Mancano tre minuti", "Three minutes left"), ("Attenzione!", "Attention!"), ("Treno regionale", "Regional train"),
    ("In fondo", "At the end"), ("Vicino alla testa", "Near the front"), ("Posto finestrino", "Window seat"), ("Ascolta l'annuncio", "Listen to the announcement"), ("Il nostro treno", "Our train"),
    ("Perdere la coincidenza", "To miss the connection"), ("Fare un cambio", "To make a change"), ("In ritardo", "Late / delayed"), ("Dov'è il sottopassaggio?", "Where is the underpass?"), ("Seconda classe", "Second class"),
    ("Sulla banchina", "On the platform"), ("Oltre la linea", "Beyond the line"), ("In arrivo", "Arriving"), ("In partenza", "Departing"), ("Sola andata", "One way"),
    ("Prossima fermata", "Next stop"), ("Treno in transito", "Train in transit"), ("Non sostare", "Do not stand"), ("Oltre la linea gialla", "Beyond the yellow line"), ("Sottopassaggio pedonale", "Pedestrian underpass"),
    ("Binario tronco", "Dead-end platform"), ("Carrozza ristorante", "Dining car"), ("Ufficio oggetti smarriti", "Lost and found office"), ("Scala mobile", "Escalator"), ("Uscita di sicurezza", "Emergency exit")
]
s6_sentences = [
    ("Scusi, sa da quale binario parte il treno per Firenze?", "Excuse me, do you know from which platform the train to Florence leaves?"),
    ("Il treno per Firenze parte dal binario dodici oggi.", "The train to Florence leaves from platform twelve today."),
    ("Il treno è già al binario o deve ancora arrivare?", "Is the train already at the platform or is it yet to arrive?"),
    ("Sì, è arrivato proprio ora al binario sette.", "Yes, it just arrived now at platform seven."),
    ("Deve solo convalidare il biglietto prima di salire a bordo.", "You just need to validate the ticket before boarding."),
    ("Grazie mille, corro subito al binario per non perderlo!", "Thank you very much, I'm running to the platform now so I don't miss it!"),
    ("Mi scusi, il treno per Milano ha molto ritardo?", "Excuse me, is the train to Milan very late?"),
    ("Al momento segnalano venti minuti di ritardo per un problema.", "At the moment they are reporting twenty minutes of delay due to a problem."),
    ("C'è un problema tecnico sulla linea tra Roma e Firenze.", "There is a technical problem on the line between Rome and Florence."),
    ("Cambierà il binario di partenza per il treno delle dieci?", "Will the departure platform change for the ten o'clock train?"),
    ("No, il binario di partenza rimane il numero sette.", "No, the departure platform remains number seven."),
    ("Controlli comunque il tabellone luminoso tra poco per sicurezza.", "Check the luminous board in a little while anyway for safety."),
    ("D'accordo, grazie per l'informazione e buona giornata.", "Agreed, thanks for the information and have a good day."),
    ("Attenzione, il treno per Pisa partirà dal binario quattro.", "Attention, the train to Pisa will leave from platform four."),
    ("Il treno partirà dal binario quattro anziché dal binario nove.", "The train will leave from platform four instead of platform nine."),
    ("Scusi, ho capito bene? Il treno ha cambiato binario?", "Excuse me, did I understand correctly? Has the train changed platforms?"),
    ("Sì, hanno appena detto che parte dal binario quattro.", "Yes, they just said it leaves from platform four."),
    ("Dobbiamo fare il sottopassaggio per raggiungere l'altra banchina.", "We have to take the underpass to reach the other platform."),
    ("Le valigie sono molto pesanti, spero di fare in tempo.", "The suitcases are very heavy, I hope to make it on time."),
    ("Si sbrighi, mancano solo tre minuti alla partenza del treno!", "Hurry up, there are only three minutes left until the train departs!"),
    ("Ascolta l'annuncio, il nostro treno è in forte ritardo.", "Listen to the announcement, our train is seriously delayed."),
    ("Per raggiungere il binario due, devi prendere il sottopassaggio.", "To reach platform two, you have to take the underpass."),
    ("Se il treno è in ritardo, perderemo sicuramente la coincidenza.", "If the train is delayed, we will surely miss the connection."),
    ("La carrozza numero cinque è vicino alla testa del treno.", "Coach number five is near the front of the train."),
    ("Scusate, questo è il posto vicino al finestrino?", "Excuse me, is this the window seat?"),
    ("Hanno appena fatto un annuncio per il cambio di binario.", "They just made an announcement for the platform change."),
    ("Non sostare oltre la linea gialla sulla banchina.", "Do not stand beyond the yellow line on the platform."),
    ("Il treno regionale in arrivo al binario tre si ferma in tutte le stazioni.", "The regional train arriving at platform three stops at all stations."),
    ("Il treno Alta Velocità per Milano è in transito al binario uno.", "The high-speed train to Milan is transiting through platform one."),
    ("Dov'è l'ufficio degli oggetti smarriti in questa stazione?", "Where is the lost and found office in this station?"),
    ("Prenda l'ascensore se ha bagagli molto pesanti con sé.", "Take the elevator if you have very heavy luggage with you."),
    ("La scala mobile per il primo piano è fuori servizio.", "The escalator to the first floor is out of order."),
    ("Il treno per Torino è in partenza dal binario quindici.", "The train to Turin is departing from platform fifteen."),
    ("Ci sono venti minuti di attesa per il prossimo treno.", "There is a twenty-minute wait for the next train."),
    ("Il sottopassaggio è molto affollato a quest'ora del pomeriggio.", "The underpass is very crowded at this time of the afternoon."),
    ("Deve convalidare il biglietto nelle macchinette gialle o verdi.", "You must validate the ticket in the yellow or green machines."),
    ("Scusi, questo treno ferma anche a Prato Centrale?", "Excuse me, does this train also stop at Prato Centrale?"),
    ("Il capotreno è sulla banchina per dare il via.", "The conductor is on the platform to give the signal."),
    ("Ho perso la coincidenza per un minuto soltanto.", "I missed the connection by only one minute."),
    ("Dove posso findare un carrello per le mie valigie?", "Where can I find a trolley for my suitcases?"),
    ("Il tabellone indica che il treno è puntuale.", "The board indicates that the train is on time."),
    ("Attenzione ai borseggiatori nelle zone affollate della stazione.", "Watch out for pickpockets in crowded areas of the station."),
    ("C'è un bar vicino al binario dieci?", "Is there a bar near platform ten?"),
    ("Il treno per l'aeroporto parte ogni trenta minuti circa.", "The train to the airport leaves approximately every thirty minutes."),
    ("Deve scendere alla prossima fermata per il centro.", "You must get off at the next stop for the center."),
    ("La carrozza ristorante si trova al centro del treno.", "The dining car is located in the middle of the train."),
    ("Questo treno ha solo posti di seconda classe.", "This train only has second-class seats."),
    ("Sulle carrozze è obbligatorio l'uso della mascherina?", "Is it mandatory to use a mask on the coaches?"),
    ("Il treno sta arrivando, allontanatevi dal bordo della banchina.", "The train is arriving, move away from the edge of the platform."),
    ("Il binario quindici è in fondo al corridoio a destra.", "Platform fifteen is at the end of the hallway to the right."),
    ("Spero che la coincidenza ci aspetti a Bologna.", "I hope the connection waits for us in Bologna."),
    ("Il viaggio in treno è molto rilassante e panoramico.", "The train journey is very relaxing and scenic."),
    ("Quanto costa un biglietto per il treno notturno?", "How much does a ticket for the night train cost?"),
    ("La stazione di Santa Maria Novella è bellissima.", "Santa Maria Novella station is beautiful."),
    ("Ci sono armadietti per il deposito bagagli qui?", "Are there lockers for luggage storage here?"),
    ("Il treno è composto da otto carrozze passeggeri.", "The train consists of eight passenger coaches."),
    ("Si prega di non gettare oggetti dal finestrino.", "Please do not throw objects from the window."),
    ("Il controllore sta verificando i titoli di viaggio.", "The conductor is checking the travel tickets."),
    ("La porta si apre automaticamente alla fermata.", "The door opens automatically at the stop."),
    ("Buona permanenza in città a tutti i viaggiatori.", "Enjoy your stay in the city to all travelers.")
]
# Fix typos in s6 sentences
s6_sentences[39] = ("Dove posso trovare un carrello per le mie valigie?", "Where can I find a trolley for my suitcases?")

save_scenario("s6", "train_platform", s6_vocab, s6_phrases, s6_sentences)

# Data for s7 bus_ticket
s7_vocab = [
    ("autobus", "bus"), ("biglietto", "ticket"), ("tabaccheria", "tobacco shop"), ("urbano", "city / urban"), ("singolo", "single"),
    ("giornata", "day"), ("intero", "entire"), ("convalidare", "validate"), ("bordo", "board"), ("linea", "line"),
    ("colosseo", "Colosseum"), ("termini", "Termini station"), ("fermata", "stop"), ("lato", "side"), ("strada", "street"),
    ("chiesto", "asked"), ("autista", "driver"), ("abbonamento", "subscription / pass"), ("settimanale", "weekly"), ("mezzi", "transportation"),
    ("pubblici", "public"), ("settimana", "week"), ("carta", "card"), ("trasporti", "transport"), ("area", "area"),
    ("perfetto", "perfect"), ("prendere", "to take"), ("valido", "valid"), ("costa", "costs"), ("euro", "euro"),
    ("biglietteria", "ticket office"), ("macchinetta", "machine"), ("contanti", "cash"), ("resto", "change"), ("orario", "schedule"),
    ("ritardo", "delay"), ("corsa", "ride"), ("prossimo", "next"), ("direzione", "direction"), ("centro", "center"),
    ("mappa", "map"), ("percorso", "route"), ("tessera", "card"), ("multa", "fine"), ("controllo", "check"),
    ("verificare", "verify"), ("salire", "to board"), ("scendere", "to get off"), ("prenotare", "to book"), ("posto", "seat")
]
s7_phrases = [
    ("Vorrei due biglietti", "I would like two tickets"), ("Autobus urbano", "City bus"), ("Biglietti singoli", "Single tickets"), ("Intera giornata", "Entire day"), ("Tre euro in tutto", "Three euros in total"),
    ("Ricordi di convalidarli", "Remember to validate them"), ("Appena sale a bordo", "As soon as you board"), ("Va bene, grazie", "Okay, thank you"), ("Passa per il Colosseo?", "Does it pass by the Colosseum?"), ("Verso la stazione", "Towards the station"),
    ("Deve prendere la linea 85", "You must take line 85"), ("Alla fermata", "At the stop"), ("Dall'altro lato", "On the other side"), ("Della strada", "Of the street"), ("Meno male!", "Thank goodness!"),
    ("Ho chiesto", "I asked"), ("Grazie mille", "Thank you very much"), ("Prego, si figuri", "You're welcome, don't mention it"), ("Abbonamento settimanale", "Weekly pass"), ("Mezzi pubblici", "Public transport"),
    ("Valido per una settimana", "Valid for a week"), ("Carta trasporti", "Transport card"), ("Costa ventiquattro euro", "Costs twenty-four euros"), ("Bus e metro", "Bus and metro"), ("Area urbana", "Urban area"),
    ("La prendo", "I'll take it"), ("Dov'è la fermata?", "Where is the stop?"), ("A che ora passa?", "What time does it come?"), ("Biglietto giornaliero", "Daily ticket"), ("Validare il biglietto", "Validate the ticket"),
    ("Chiedere all'autista", "Ask the driver"), ("Fermata giusta", "Right stop"), ("Direzione centro", "Center direction"), ("Orario bus", "Bus schedule"), ("Prendere la linea", "Take the line"),
    ("Tabaccheria vicina", "Nearby tobacco shop"), ("C'è una multa", "There is a fine"), ("Senza biglietto", "Without a ticket"), ("Controllo biglietti", "Ticket inspection"), ("Scendere alla prossima", "Get off at the next one"),
    ("Prossima corsa", "Next ride"), ("In ritardo", "Late"), ("Quanto costa?", "How much is it?"), ("Biglietto a bordo", "Ticket on board"), ("Sola andata", "One way"),
    ("Posto a sedere", "Seat"), ("Autobus affollato", "Crowded bus"), ("Uscita posteriore", "Rear exit"), ("Entrata anteriore", "Front entrance"), ("Validatrice rotta", "Broken validator")
]
s7_sentences = [
    ("Buongiorno, vorrei due biglietti per l'autobus urbano.", "Good morning, I would like two tickets for the city bus."),
    ("Preferisce i biglietti singoli o uno per l'intera giornata?", "Do you prefer single tickets or one for the entire day?"),
    ("Prendo due biglietti singoli per andare in centro, per favore.", "I'll take two single tickets to go to the center, please."),
    ("I biglietti costano tre euro in tutto in questa tabaccheria.", "The tickets cost three euros in total in this tobacco shop."),
    ("Ricordi di convalidare i biglietti appena sali a bordo del bus.", "Remember to validate the tickets as soon as you board the bus."),
    ("Va bene, grazie mille per il consiglio e buona giornata.", "Okay, thanks a lot for the advice and have a good day."),
    ("Mi scusi autista, questo autobus passa per il Colosseo?", "Excuse me driver, does this bus pass by the Colosseum?"),
    ("No, questo autobus va verso la stazione Termini oggi.", "No, this bus is going towards Termini station today."),
    ("Per il Colosseo deve prendere la linea ottantacinque alla fermata.", "For the Colosseum you must take line eighty-five at the stop."),
    ("La fermata si trova esattamente dall'altro lato della strada.", "The stop is located exactly on the other side of the street."),
    ("Ah, meno male che ho chiesto prima di salire sul bus!", "Ah, thank goodness I asked before getting on the bus!"),
    ("Grazie mille per l'aiuto, stavo per sbagliare direzione.", "Thank you very much for the help, I was about to go the wrong way."),
    ("Prego, si figuri, è un piacere aiutare i turisti.", "You're welcome, don't mention it, it's a pleasure to help tourists."),
    ("Salve, è possibile fare un abbonamento per i mezzi pubblici?", "Hello, is it possible to get a public transport pass?"),
    ("Vorrei un abbonamento che sia valido per una settimana intera.", "I would like a pass that is valid for an entire week."),
    ("Abbiamo la carta trasporti settimanale che costa ventiquattro euro.", "We have the weekly transport card which costs twenty-four euros."),
    ("L'abbonamento vale per tutti i mezzi pubblici, come bus e metro?", "Does the pass work for all public transport, like bus and metro?"),
    ("Sì, vale per tutti i mezzi all'interno dell'area urbana.", "Yes, it's valid for all transport within the urban area."),
    ("Perfetto, la prendo subito, così posso viaggiare tranquillo.", "Perfect, I'll take it right now, so I can travel without worries."),
    ("Dove posso trovare la tabaccheria più vicina alla stazione?", "Where can I find the nearest tobacco shop to the station?"),
    ("Puoi comprare i biglietti urbani anche in quella tabaccheria.", "You can buy city tickets in that tobacco shop too."),
    ("Scusi autista, è questa la fermata giusta per il museo?", "Excuse me driver, is this the right stop for the museum?"),
    ("Ricordati di validare il biglietto appena sali sull'autobus.", "Remember to validate the ticket as soon as you board the bus."),
    ("La linea cinquantatré va in direzione dello stadio Olimpico.", "Line fifty-three goes in the direction of the Olympic stadium."),
    ("Sull'orario del bus c'è scritto che passa ogni dieci minuti.", "On the bus schedule it says it comes every ten minutes."),
    ("Ho paura di aver sbagliato direzione, questo è il centro?", "I'm afraid I went the wrong way, is this the center?"),
    ("Posso comprare il biglietto direttamente dall'autista a bordo?", "Can I buy the ticket directly from the driver on board?"),
    ("A volte la macchinetta validatrice è rotta sul bus.", "Sometimes the validating machine is broken on the bus."),
    ("Deve scrivere la data e l'ora sul biglietto a mano?", "Do you have to write the date and time on the ticket by hand?"),
    ("C'è un controllo dei biglietti alla prossima fermata del bus.", "There is a ticket inspection at the next bus stop."),
    ("La multa per chi viaggia senza biglietto è molto alta.", "The fine for those traveling without a ticket is very high."),
    ("L'autobus è troppo affollato, aspetto la prossima corsa.", "The bus is too crowded, I'll wait for the next ride."),
    ("Deve prenotare la fermata premendo il tasto rosso.", "You must request the stop by pressing the red button."),
    ("A che ora è l'ultima corsa della linea dodici?", "What time is the last ride of line twelve?"),
    ("L'abbonamento mensile è più conveniente per chi lavora.", "The monthly pass is more convenient for those who work."),
    ("Posso portare la bicicletta sull'autobus urbano oggi?", "Can I bring my bicycle on the city bus today?"),
    ("Dov'è la mappa con tutte le linee degli autobus?", "Where is the map with all the bus lines?"),
    ("Il pullman per l'aeroporto parte da via Giolitti.", "The shuttle to the airport leaves from via Giolitti."),
    ("C'è molta coda alla biglietteria automatica della metro.", "There is a long line at the metro's automatic ticket machine."),
    ("Scusi, questo posto a sedere è riservato agli anziani?", "Excuse me, is this seat reserved for the elderly?"),
    ("L'autobus ha saltato la fermata perché era troppo pieno.", "The bus skipped the stop because it was too full."),
    ("Quanto dura la validità di un biglietto singolo?", "How long is a single ticket valid for?"),
    ("Il biglietto vale per novanta minuti dalla convalida.", "The ticket is valid for ninety minutes from validation."),
    ("Speriamo che l'autobus arrivi presto, fa molto freddo.", "Let's hope the bus arrives soon, it's very cold."),
    ("Deve scendere alla fermata dopo il semaforo a destra.", "You must get off at the stop after the traffic light on the right."),
    ("La linea notturna passa ogni mezz'ora circa.", "The night line comes approximately every half hour."),
    ("C'è uno sciopero dei mezzi pubblici domani mattina.", "There is a public transport strike tomorrow morning."),
    ("Devo timbrare il biglietto ogni volta che cambio bus?", "Do I have to stamp the ticket every time I change buses?"),
    ("No, se il tempo non è scaduto non serve timbrare.", "No, if the time hasn't expired you don't need to stamp."),
    ("Il conducente guida molto velocemente in questa strada.", "The driver is driving very fast on this street."),
    ("Potete spostarvi verso il centro dell'autobus, per favore?", "Can you move towards the center of the bus, please?"),
    ("L'uscita è dalla porta centrale o posteriore.", "The exit is from the middle or rear door."),
    ("Si entra solo dalla porta anteriore del bus.", "You only enter from the front door of the bus."),
    ("L'abbonamento è personale e non può essere ceduto.", "The pass is personal and cannot be transferred."),
    ("C'è l'aria condizionata accesa su questo mezzo?", "Is the air conditioning on in this vehicle?"),
    ("Il bus si ferma vicino ai principali monumenti storici.", "The bus stops near the main historical monuments."),
    ("Dobbiamo scendere alla stazione ferroviaria per il cambio.", "We must get off at the train station for the change."),
    ("Scusi, mi sa dire dove siamo esattamente adesso?", "Excuse me, can you tell me where exactly we are now?"),
    ("Questa linea è sempre molto puntuale la mattina.", "This line is always very punctual in the morning."),
    ("Buon viaggio a tutti i passeggeri della linea ottantacinque!", "Have a good trip to all passengers of line eighty-five!")
]

save_scenario("s7", "bus_ticket", s7_vocab, s7_phrases, s7_sentences)

# Data for s8 metro_directions
s8_vocab = [
    ("linea", "line"), ("rossa", "red"), ("verde", "green"), ("cambio", "transfer / change"), ("uscita", "exit"),
    ("scale", "stairs"), ("biglietteria", "ticket office"), ("mappa", "map"), ("capolinea", "last stop"), ("direzione", "direction"),
    ("fermata", "stop"), ("scendere", "to get off"), ("vaticani", "Vatican"), ("musei", "museums"), ("banchina", "platform"),
    ("giusta", "right / correct"), ("duomo", "Duomo / Cathedral"), ("opposta", "opposite"), ("attraversare", "to cross"), ("sottopassaggio", "underpass"),
    ("cartelli", "signs"), ("alto", "top / high"), ("attento", "careful"), ("metro", "metro / subway"), ("biglietto", "ticket"),
    ("valido", "valid"), ("minuti", "minutes"), ("tranquillamente", "calmly / easily"), ("informazione", "information"), ("san siro", "San Siro"),
    ("lilla", "lilac"), ("lotto", "Lotto station"), ("passante", "passerby"), ("scusa", "excuse me"), ("salve", "hello"),
    ("prendere", "to take"), ("camminare", "to walk"), ("piedi", "foot"), ("vicino", "near"), ("ingresso", "entrance"),
    ("muro", "wall"), ("cima", "top"), ("chiusa", "closed"), ("macchinetta", "machine"), ("perso", "lost"),
    ("cercando", "looking for"), ("mobile", "escalator"), ("tornelli", "turnstiles"), ("abbonamento", "pass"), ("sciopero", "strike")
]
s8_phrases = [
    ("Quale linea?", "Which line?"), ("Linea rossa", "Red line"), ("Linea verde", "Green line"), ("Linea lilla", "Lilac line"), ("Direzione Battistini", "Towards Battistini"),
    ("A quale fermata?", "At which stop?"), ("Scendere a Ottaviano", "Get off at Ottaviano"), ("Pochi passi", "A few steps"), ("Dall'ingresso", "From the entrance"), ("Grazie mille", "Thank you very much"),
    ("Banchina giusta?", "Right platform?"), ("Verso il Duomo", "Towards the Duomo"), ("Direzione opposta", "Opposite direction"), ("Attraversare il sottopassaggio", "Cross the underpass"), ("L'altra banchina", "The other platform"),
    ("Meno male!", "Thank goodness!"), ("Prima che arrivasse", "Before it arrived"), ("Stia attento", "Be careful"), ("Cartelli in alto", "Signs above"), ("Di nulla", "You're welcome"),
    ("Cambiare linea?", "Change lines?"), ("Cambiare con la lilla", "Change to the lilac one"), ("Fino a Lotto", "Until Lotto"), ("Lo stesso biglietto", "The same ticket"), ("Farne un altro", "Make another one"),
    ("Vale novanta minuti", "Valid for ninety minutes"), ("Usarlo tranquillamente", "Use it easily"), ("Per il cambio", "For the transfer"), ("C'è una mappa", "There is a map"), ("Sul muro", "On the wall"),
    ("Il capolinea", "The last stop"), ("Molto lontano", "Very far"), ("In cima alle scale", "At the top of the stairs"), ("Biglietteria chiusa", "Ticket office closed"), ("Usa la macchinetta", "Use the machine"),
    ("Mi sono perso", "I am lost"), ("Cercando il cambio", "Looking for the transfer"), ("Prendere la metro", "Take the metro"), ("Uscita a destra", "Exit on the right"), ("Scale mobili", "Escalators"),
    ("Oltre i tornelli", "Beyond the turnstiles"), ("Timbrare il biglietto", "Stamp the ticket"), ("Abbonamento mensile", "Monthly pass"), ("Mappa della metro", "Metro map"), ("Prossimo treno", "Next train"),
    ("In arrivo", "Arriving"), ("Direzione centro", "Towards center"), ("Fermata successiva", "Next stop"), ("Ultima corsa", "Last ride"), ("Sciopero metro", "Metro strike")
]
s8_sentences = [
    ("Scusi, quale linea devo prendere per i Musei Vaticani?", "Excuse me, which line should I take for the Vatican Museums?"),
    ("Deve prendere la Linea A in direzione Battistini.", "You must take Line A towards Battistini."),
    ("A quale fermata devo scendere per i musei?", "At which stop should I get off for the museums?"),
    ("La fermata si chiama Ottaviano San Pietro.", "The stop is called Ottaviano San Pietro."),
    ("L'ingresso è a pochi passi dalla fermata della metro.", "The entrance is a few steps from the metro stop."),
    ("Grazie mille per l'aiuto, è stato molto gentile.", "Thank you very much for the help, you were very kind."),
    ("Mi scusi, questa è la banchina giusta per il Duomo?", "Excuse me, is this the right platform for the Duomo?"),
    ("No, questa è la direzione opposta per il centro.", "No, this is the opposite direction for the center."),
    ("Deve attraversare il sottopassaggio e andare sull'altra banchina.", "You must cross the underpass and go to the other platform."),
    ("Ah, meno male che ho chiesto prima del treno!", "Ah, thank goodness I asked before the train!"),
    ("Stia attento ai cartelli in alto che indicano la direzione.", "Be careful of the signs above that indicate the direction."),
    ("D'accordo, grazie ancora per l'informazione preziosa.", "Agreed, thanks again for the valuable information."),
    ("Salve, devo andare a San Siro, devo cambiare linea?", "Hello, I need to go to San Siro, do I need to change lines?"),
    ("Sì, prenda la linea rossa e poi cambi con la lilla.", "Yes, take the red line and then change to the lilac one."),
    ("Deve scendere a Lotto per fare il cambio linea.", "You must get off at Lotto to change lines."),
    ("Il biglietto è lo stesso o devo farne un altro?", "Is the ticket the same or do I need to get another one?"),
    ("Il biglietto vale per novanta minuti dalla prima convalida.", "The ticket is valid for ninety minutes from the first validation."),
    ("Può usarlo tranquillamente anche per il cambio di linea.", "You can use it easily for the line change too."),
    ("Perfetto, grazie mille per tutte le informazioni.", "Perfect, thanks a lot for all the information."),
    ("C'è una mappa della metro sul muro della banchina.", "There is a metro map on the wall of the platform."),
    ("Il capolinea della linea rossa è molto lontano da qui.", "The last stop of the red line is very far from here."),
    ("Per il centro devi prendere la linea verde e cambiare.", "For the center you must take the green line and change."),
    ("L'uscita della metro è in cima a queste scale.", "The metro exit is at the top of these stairs."),
    ("La biglietteria è chiusa, deve usare la macchinetta automatica.", "The ticket office is closed, you must use the automatic machine."),
    ("Mi sono perso cercando il cambio per la linea rossa.", "I got lost looking for the transfer for the red line."),
    ("Le scale mobili sono in fondo al corridoio a sinistra.", "The escalators are at the end of the hallway to the left."),
    ("Deve timbrare il biglietto prima di passare i tornelli.", "You must stamp the ticket before passing the turnstiles."),
    ("L'abbonamento mensile si può ricaricare online o qui.", "The monthly pass can be recharged online or here."),
    ("Attenzione, c'è uno sciopero della metro oggi pomeriggio.", "Attention, there is a metro strike this afternoon."),
    ("Il prossimo treno in arrivo va verso la periferia.", "The next arriving train goes towards the outskirts."),
    ("Scusi, questo treno si ferma alla stazione centrale?", "Excuse me, does this train stop at the central station?"),
    ("Deve affrettarsi, le porte si stanno per chiudere.", "You must hurry, the doors are about to close."),
    ("L'aria condizionata non funziona in questa carrozza.", "The air conditioning is not working in this coach."),
    ("C'è molta gente sulla metro nell'ora di punta.", "There are many people on the metro during rush hour."),
    ("Dov'è l'uscita più vicina per piazza del Popolo?", "Where is the nearest exit for Piazza del Popolo?"),
    ("Il biglietto giornaliero è valido per ventiquattro ore.", "The daily ticket is valid for twenty-four hours."),
    ("Attenzione al gradino quando scendete dal treno.", "Watch the step when you get off the train."),
    ("Questa fermata è chiusa per lavori di manutenzione.", "This stop is closed for maintenance work."),
    ("Il viaggio dura solo dieci minuti con la metro.", "The trip only lasts ten minutes with the metro."),
    ("Posso portare il mio cane sulla metro oggi?", "Can I bring my dog on the metro today?"),
    ("Sì, ma deve avere il guinzaglio e la museruola.", "Yes, but it must have a leash and a muzzle."),
    ("La linea lilla è completamente automatica e senza autista.", "The lilac line is completely automatic and without a driver."),
    ("Scusi, mi sa dire se questa è la direzione per Loreto?", "Excuse me, can you tell me if this is the direction for Loreto?"),
    ("No, deve tornare indietro di tre fermate e cambiare.", "No, you must go back three stops and change."),
    ("I tornelli non accettano il mio biglietto cartaceo.", "The turnstiles do not accept my paper ticket."),
    ("Chieda assistenza al personale in stazione se serve.", "Ask for assistance from the staff in the station if needed."),
    ("La mappa digitale mostra i tempi di attesa reali.", "The digital map shows real-time wait times."),
    ("È vietato fumare all'interno di tutte le stazioni.", "Smoking is forbidden inside all stations."),
    ("Tenete la destra sulle scale mobili, per favore.", "Keep to the right on the escalators, please."),
    ("Il treno sta entrando in stazione, allontanatevi.", "The train is entering the station, move away."),
    ("Qual è il capolinea di questa linea verde?", "What is the last stop of this green line?"),
    ("Devo fare il biglietto per i bambini piccoli?", "Do I need to buy a ticket for small children?"),
    ("Sotto i dieci anni il viaggio è gratuito in città.", "Under ten years old the journey is free in the city."),
    ("Mi sono dimenticato lo zaino sulla banchina della metro!", "I forgot my backpack on the metro platform!"),
    ("Corra all'ufficio oggetti smarriti della stazione.", "Run to the station's lost and found office."),
    ("La frequenza dei treni è di tre minuti circa.", "The frequency of trains is about three minutes."),
    ("Non spingete per entrare, c'è posto per tutti.", "Don't push to enter, there is room for everyone."),
    ("La metro è il modo più veloce per girare Roma.", "The metro is the fastest way to get around Rome."),
    ("Speriamo che non ci sia troppa folla oggi.", "Let's hope there isn't too much of a crowd today."),
    ("Buon viaggio in metropolitana a tutti i passeggeri!", "Have a good trip on the subway to all passengers!")
]

save_scenario("s8", "metro_directions", s8_vocab, s8_phrases, s8_sentences)
