import json
import random

def generate_vocabulary():
    base_vocab = [
        ("idraulico", "plumber"),
        ("elettricista", "electrician"),
        ("perdita", "leak"),
        ("rubinetto", "tap"),
        ("lavandino", "sink"),
        ("cucina", "kitchen"),
        ("bagno", "bathroom"),
        ("caldaia", "boiler"),
        ("riparare", "to repair"),
        ("aggiustare", "to fix"),
        ("urgente", "urgent"),
        ("gocciolio", "dripping"),
        ("valvola", "valve"),
        ("chiudere", "to close"),
        ("aprire", "to open"),
        ("funzionante", "working"),
        ("fusibile", "fuse"),
        ("bruciato", "burnt out"),
        ("quadro elettrico", "electrical panel"),
        ("luce", "light"),
        ("impianto", "system / installation"),
        ("cavi", "cables / wires"),
        ("muro", "wall"),
        ("elettrodomestico", "appliance"),
        ("forno", "oven"),
        ("lavatrice", "washing machine"),
        ("consiglio", "advice"),
        ("problema", "problem"),
        ("grave", "serious"),
        ("interruttore", "switch"),
        ("presa elettrica", "power outlet"),
        ("strumenti", "tools"),
        ("chiave inglese", "wrench"),
        ("cacciavite", "screwdriver"),
        ("martello", "hammer"),
        ("tubo", "pipe"),
        ("guarnizione", "gasket"),
        ("pressione", "pressure"),
        ("scarico", "drain"),
        ("intasato", "clogged"),
        ("corto circuito", "short circuit"),
        ("bolletta", "bill"),
        ("costo", "cost"),
        ("preventivo", "estimate"),
        ("manutenzione", "maintenance"),
        ("tecnico", "technician"),
        ("pezzo di ricambio", "spare part"),
        ("sostituire", "to replace"),
        ("funzionare", "to work / to function"),
        ("chiamare", "to call"),
        ("venire", "to come"),
        ("passare", "to stop by"),
        ("appuntamento", "appointment"),
        ("ritardo", "delay"),
        ("sciacquone", "toilet flush"),
        ("doccia", "shower"),
        ("piastrella", "tile"),
        ("crepa", "crack"),
        ("soffitto", "ceiling"),
        ("pavimento", "floor"),
    ]
    
    vocab_list = []
    all_ita = [v[0] for v in base_vocab]
    all_eng = [v[1] for v in base_vocab]
    
    for i, (ita, eng) in enumerate(base_vocab[:55]):
        # Sample distractors
        indices = list(range(len(base_vocab)))
        indices.remove(i)
        distractor_indices = random.sample(indices, 3)
        
        choices_ita = [ita] + [base_vocab[idx][0] for idx in distractor_indices]
        choices_eng = [eng] + [base_vocab[idx][1] for idx in distractor_indices]
        
        # Shuffle both identically
        combined = list(zip(choices_ita, choices_eng))
        random.shuffle(combined)
        choices_ita, choices_eng = zip(*combined)
        
        vocab_list.append({
            "id": f"s60-v{i+1}",
            "choicesItalian": list(choices_ita),
            "choicesEnglish": list(choices_eng),
            "correctAnswerItalian": ita,
            "correctAnswerEnglish": eng,
            "feedback": {
                "correctItalian": f"Esatto! '{ita}' significa '{eng}'.",
                "incorrectItalian": f"No, la risposta corretta è '{ita}'.",
                "correctEnglish": f"Exactly! '{ita}' means '{eng}'.",
                "incorrectEnglish": f"No, the correct answer is '{eng}'."
            }
        })
    return vocab_list

def generate_phrases():
    base_phrases = [
        ("C'è una perdita d'acqua.", "There is a water leak."),
        ("Il rubinetto gocciola.", "The tap is dripping."),
        ("Non c'è acqua calda.", "There is no hot water."),
        ("La caldaia non parte.", "The boiler won't start."),
        ("È saltata la luce.", "The power went out."),
        ("C'è un corto circuito.", "There is a short circuit."),
        ("Il lavandino è intasato.", "The sink is clogged."),
        ("Lo scarico è bloccato.", "The drain is blocked."),
        ("La presa non funziona.", "The outlet doesn't work."),
        ("Mi serve un idraulico.", "I need a plumber."),
        ("Chiami un elettricista.", "Call an electrician."),
        ("È molto urgente.", "It is very urgent."),
        ("Quando può passare?", "When can you stop by?"),
        ("Quanto costa l'uscita?", "How much is the service call?"),
        ("Mi faccia un preventivo.", "Give me an estimate."),
        ("Bisogna cambiare il pezzo.", "The part needs to be changed."),
        ("La valvola è chiusa.", "The valve is closed."),
        ("Il tubo perde.", "The pipe is leaking."),
        ("Si è rotto il vetro.", "The glass broke."),
        ("La tapparella è bloccata.", "The shutter is stuck."),
        ("La serratura non gira.", "The lock won't turn."),
        ("Ho perso le chiavi.", "I lost the keys."),
        ("Il forno non scalda.", "The oven doesn't heat up."),
        ("La lavatrice non scarica.", "The washing machine doesn't drain."),
        ("C'è puzza di bruciato.", "There is a smell of burning."),
        ("Ho bisogno di aiuto.", "I need help."),
        ("Può ripararlo?", "Can you repair it?"),
        ("È un problema grave?", "Is it a serious problem?"),
        ("Quanto tempo ci vuole?", "How long will it take?"),
        ("Domani mattina alle nove.", "Tomorrow morning at nine."),
        ("Oggi pomeriggio va bene.", "This afternoon is fine."),
        ("Il tecnico è in arrivo.", "The technician is on the way."),
        ("La guarnizione è vecchia.", "The gasket is old."),
        ("C'è troppa pressione.", "There is too much pressure."),
        ("L'acqua non scende.", "The water doesn't go down."),
        ("Il muro è umido.", "The wall is damp."),
        ("C'è una macchia sul soffitto.", "There is a stain on the ceiling."),
        ("Il quadro elettrico è qui.", "The electrical panel is here."),
        ("Non toccare i fili.", "Do not touch the wires."),
        ("Usi gli strumenti giusti.", "Use the right tools."),
        ("Ho chiuso l'acqua generale.", "I turned off the main water."),
        ("Serve una chiave inglese.", "A wrench is needed."),
        ("Il bullone è allentato.", "The bolt is loose."),
        ("Stringa bene la vite.", "Tighten the screw well."),
        ("La luce trema.", "The light is flickering."),
        ("Il citofono non suona.", "The intercom doesn't ring."),
        ("Il cancello è rotto.", "The gate is broken."),
        ("Manca la corrente.", "There is no power."),
        ("Il fusibile è andato.", "The fuse is gone."),
        ("Tutto risolto ora.", "Everything is resolved now."),
        ("Grazie per l'intervento.", "Thanks for the intervention."),
        ("Le manderò la fattura.", "I will send you the invoice."),
        ("Pagherò in contanti.", "I will pay in cash."),
        ("Accetta la carta?", "Do you accept cards?"),
    ]
    
    phrases_list = []
    for i, (ita, eng) in enumerate(base_phrases[:55]):
        indices = list(range(len(base_phrases)))
        indices.remove(i)
        distractor_indices = random.sample(indices, 3)
        
        choices_ita = [ita] + [base_phrases[idx][0] for idx in distractor_indices]
        choices_eng = [eng] + [base_phrases[idx][1] for idx in distractor_indices]
        
        combined = list(zip(choices_ita, choices_eng))
        random.shuffle(combined)
        choices_ita, choices_eng = zip(*combined)
        
        phrases_list.append({
            "id": f"s60-p{i+1}",
            "choicesItalian": list(choices_ita),
            "choicesEnglish": list(choices_eng),
            "correctAnswerItalian": ita,
            "correctAnswerEnglish": eng,
            "feedback": {
                "correctItalian": f"Ottimo! '{ita}' è corretto.",
                "incorrectItalian": f"Quasi! La risposta corretta è '{ita}'.",
                "correctEnglish": f"Great! '{eng}' is correct.",
                "incorrectEnglish": f"Almost! The correct answer is '{eng}'."
            }
        })
    return phrases_list

def generate_sentences():
    base_sentences = [
        ("Ho una perdita d'acqua sotto il lavandino della cucina.", "I have a water leak under the kitchen sink."),
        ("All'inizio gocciolava, ma ora esce molta acqua.", "At first it was dripping, but now a lot of water is coming out."),
        ("Ho dovuto chiudere la valvola generale per sicurezza.", "I had to close the main valve for safety."),
        ("L'idraulico può passare oggi pomeriggio alle quattro?", "Can the plumber stop by this afternoon at four?"),
        ("Mi serve la cucina funzionante entro stasera per cena.", "I need the kitchen working by tonight for dinner."),
        ("Era solo un fusibile bruciato nel quadro elettrico.", "It was just a burnt-out fuse in the electrical panel."),
        ("Temevo fosse un problema più grave ai cavi interni.", "I feared it was a more serious problem with the internal cables."),
        ("Le consiglio di non usare troppi elettrodomestici insieme.", "I advise you not to use too many appliances at once."),
        ("Succede sempre quando accendiamo il forno e la lavatrice.", "It always happens when we turn on the oven and the washing machine."),
        ("Quanto costa riparare questo rubinetto che perde?", "How much does it cost to repair this leaking tap?"),
        ("La caldaia deve essere revisionata ogni anno per legge.", "The boiler must be serviced every year by law."),
        ("Non toccare la presa elettrica se hai le mani bagnate.", "Do not touch the electrical outlet if you have wet hands."),
        ("Cerco qualcuno che possa venire subito per un'urgenza.", "I'm looking for someone who can come right away for an emergency."),
        ("L'idraulico ha detto che bisogna sostituire l'intero pezzo.", "The plumber said that the whole part needs to be replaced."),
        ("Chiami l'elettricista per controllare l'impianto delle luci.", "Call the electrician to check the lighting system."),
        ("C'è una macchia di umidità sul soffitto del bagno.", "There is a damp stain on the bathroom ceiling."),
        ("Il vicino del piano di sopra ha una perdita nel bagno.", "The neighbor upstairs has a leak in the bathroom."),
        ("Il tecnico arriverà tra mezz'ora per aggiustare la caldaia.", "The technician will arrive in half an hour to fix the boiler."),
        ("Deve stringere meglio questa guarnizione per fermare il gocciolio.", "You need to tighten this gasket better to stop the dripping."),
        ("L'impianto elettrico di questa casa è molto vecchio.", "The electrical system of this house is very old."),
        ("Ho bisogno di un cacciavite a stella per questo lavoro.", "I need a Phillips screwdriver for this job."),
        ("Può mandarmi il preventivo via email entro domani?", "Can you send me the estimate via email by tomorrow?"),
        ("La lavatrice fa un rumore strano durante la centrifuga.", "The washing machine makes a strange noise during the spin cycle."),
        ("Non c'è pressione nell'impianto dell'acqua calda.", "There is no pressure in the hot water system."),
        ("Il tecnico ha risolto il problema in meno di un'ora.", "The technician solved the problem in less than an hour."),
        ("Bisogna chiamare il pronto intervento per questa perdita.", "We need to call the emergency service for this leak."),
        ("Spero che la riparazione non sia troppo costosa.", "I hope the repair is not too expensive."),
        ("Dove si trova il contatore della luce in questo palazzo?", "Where is the electricity meter located in this building?"),
        ("Ho provato ad aggiustarlo io, ma ho peggiorato le cose.", "I tried to fix it myself, but I made things worse."),
        ("L'acqua dello scarico non scende bene, forse è intasato.", "The drain water doesn't go down well, maybe it's clogged."),
        ("L'interruttore generale scatta ogni volta che piove.", "The main switch trips every time it rains."),
        ("Bisogna rifare completamente il bagno perché i tubi sono vecchi.", "The bathroom needs to be completely redone because the pipes are old."),
        ("La luce in corridoio trema continuamente da ieri.", "The light in the hallway has been flickering continuously since yesterday."),
        ("Ho bought a new gasket at the hardware store.", "Ho comprato una nuova guarnizione al negozio di ferramenta."), # Fixed swap
        ("Il proprietario di casa deve pagare per queste riparazioni.", "The landlord must pay for these repairs."),
        ("Mi può prestare una chiave inglese per un momento?", "Can you lend me a wrench for a moment?"),
        ("C'è odore di gas in cucina, meglio aprire le finestre.", "There's a smell of gas in the kitchen, better open the windows."),
        ("Il tecnico ha dimenticato alcuni strumenti qui ieri.", "The technician forgot some tools here yesterday."),
        ("Il cancello automatico non si apre con il telecomando.", "The automatic gate doesn't open with the remote control."),
        ("Abbiamo dovuto cambiare la serratura della porta d'ingresso.", "We had to change the lock on the front door."),
        ("La pressione della caldaia è troppo bassa, devo caricarla.", "The boiler pressure is too low, I need to fill it."),
        ("L'elettricista sta controllando tutte le prese della stanza.", "The electrician is checking all the outlets in the room."),
        ("Il rubinetto della doccia perde acqua bollente.", "The shower tap is leaking boiling water."),
        ("Bisogna chiamare una ditta specializzata per il tetto.", "A specialized company must be called for the roof."),
        ("Quanto tempo garantisce per questa riparazione?", "How much time do you guarantee for this repair?"),
        ("Il pezzo di ricambio arriverà solo la settimana prossima.", "The spare part will only arrive next week."),
        ("Non accendere la luce se senti odore di bruciato.", "Do not turn on the light if you smell burning."),
        ("Ho riparato la crepa nel muro con un po' di stucco.", "I fixed the crack in the wall with some putty."),
        ("La lavastoviglie perde acqua dal fondo durante il lavaggio.", "The dishwasher leaks water from the bottom during washing."),
        ("Bisogna pulire regolarmente i filtri del condizionatore.", "The air conditioner filters must be cleaned regularly."),
        ("Il tecnico ha detto che l'impianto è a norma.", "The technician said the system is up to code."),
        ("Quanto le devo per il disturbo e per il lavoro?", "How much do I owe you for the trouble and the work?"),
        ("Mi serve una scala per raggiungere la lampadina.", "I need a ladder to reach the light bulb."),
        ("Il campanello non funziona, deve essere la batteria.", "The doorbell doesn't work, it must be the battery."),
        ("Ho messo un secchio sotto il tubo che perde.", "I put a bucket under the leaking pipe."),
        ("La tapparella si è incastrata e non scende più.", "The shutter got stuck and won't go down anymore."),
        ("L'idraulico ha usato il nastro teflon per sigillare il tubo.", "The plumber used Teflon tape to seal the pipe."),
        ("Bisogna chiamare lo spazzacamino per pulire la canna fumaria.", "The chimney sweep needs to be called to clean the flue."),
        ("C'è un buco nel tubo di scarico della lavatrice.", "There is a hole in the washing machine drain pipe."),
        ("La luce del frigorifero è fulminata, devo cambiarla.", "The refrigerator light is blown, I need to change it."),
        ("Ho trovato un bravo tuttofare che costa poco.", "I found a good handyman who doesn't cost much."),
        ("L'umidità sta rovinando l'intonaco di questa stanza.", "Humidity is ruining the plaster in this room."),
        ("Bisogna spurgare i termosifoni prima dell'inverno.", "The radiators need to be bled before winter."),
        ("Il tecnico ha controllato la combustione della caldaia.", "The technician checked the boiler's combustion."),
    ]
    # Clean up the swapped item
    base_sentences[33] = ("Ho comprato una nuova guarnizione al negozio di ferramenta.", "I bought a new gasket at the hardware store.")

    sentences_list = []
    for i, (ita, eng) in enumerate(base_sentences[:65]):
        indices = list(range(len(base_sentences)))
        indices.remove(i)
        distractor_indices = random.sample(indices, 3)
        
        choices_ita = [ita] + [base_sentences[idx][0] for idx in distractor_indices]
        choices_eng = [eng] + [base_sentences[idx][1] for idx in distractor_indices]
        
        combined = list(zip(choices_ita, choices_eng))
        random.shuffle(combined)
        choices_ita, choices_eng = zip(*combined)
        
        sentences_list.append({
            "id": f"s60-s{i+1}",
            "choicesItalian": list(choices_ita),
            "choicesEnglish": list(choices_eng),
            "correctAnswerItalian": ita,
            "correctAnswerEnglish": eng,
            "feedback": {
                "correctItalian": "Esatto! Ottima comprensione.",
                "incorrectItalian": f"No, la traduzione corretta è: {ita}",
                "correctEnglish": "Exactly! Great understanding.",
                "incorrectEnglish": f"No, the correct translation is: {eng}"
            }
        })
    return sentences_list

def save_json(data, filename):
    with open(f"src/data/exports/daily/household_repair/{filename}", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    save_json(generate_vocabulary(), "daily_household_repair_vocabulary.json")
    save_json(generate_phrases(), "daily_household_repair_phrases.json")
    save_json(generate_sentences(), "daily_household_repair_sentences.json")
