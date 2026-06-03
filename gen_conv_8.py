import json

def get_len_range(text):
    l = len(text)
    return int(l * 0.6), int(l * 1.4)

def check_length(correct, d1, d2):
    min_l, max_l = get_len_range(correct)
    for d in [d1, d2]:
        if not (min_l <= len(d) <= max_l):
            print(f"WARNING: Length mismatch! Correct: '{correct}' ({len(correct)}), Distractor: '{d}' ({len(d)})")

# Conversation 1: Ticket Machine
c1_messages = [
    {
        "id": "m1",
        "role": "host",
        "text": "Buongiorno! Hai bisogno di aiuto con la macchinetta?",
        "english": "Good morning! Do you need help with the machine?",
        "choices": [
            {"text": "Sì, vorrei comprare un biglietto per la metro.", "isCorrect": True, "feedback": "Correct! You identified your goal."},
            {"text": "Sì, vorrei comprare un chilo di mele rosse.", "isCorrect": False, "feedback": "This is a ticket machine, not a fruit stall."},
            {"text": "No, sto cercando un tavolo per quattro persone.", "isCorrect": False, "feedback": "You don't need a table at a metro station."}
        ]
    },
    {
        "id": "m2",
        "role": "host",
        "text": "Certo. Quale tipo di biglietto preferisci comprare?",
        "english": "Sure. Which type of ticket do you prefer to buy?",
        "choices": [
            {"text": "Vorrei un biglietto semplice per una corsa sola.", "isCorrect": True, "feedback": "Good choice for a single trip."},
            {"text": "Vorrei un biglietto per il treno per Milano.", "isCorrect": False, "feedback": "This machine only sells metro tickets."},
            {"text": "Vorrei un biglietto per il concerto di stasera.", "isCorrect": False, "feedback": "You can't buy concert tickets here."}
        ]
    },
    {
        "id": "m3",
        "role": "host",
        "text": "Va bene. Vuoi pagare con i contanti o con la carta?",
        "english": "Alright. Do you want to pay with cash or with a card?",
        "choices": [
            {"text": "Preferisco pagare con la mia carta di credito.", "isCorrect": True, "feedback": "Card payments are very common and easy."},
            {"text": "Preferisco pagare con questi vecchi bottoni.", "isCorrect": False, "feedback": "You must use valid currency or a card."},
            {"text": "Preferisco pagare con un pezzo di formaggio.", "isCorrect": False, "feedback": "Food is not a valid form of payment here."}
        ]
    },
    {
        "id": "m4",
        "role": "host",
        "text": "Ottimo. Inserisci la carta nel lettore qui a destra.",
        "english": "Excellent. Insert the card into the reader here on the right.",
        "choices": [
            {"text": "Fatto. Devo inserire anche il mio codice segreto?", "isCorrect": True, "feedback": "Good question about security."},
            {"text": "Fatto. Devo inserire anche il mio numero civico?", "isCorrect": False, "feedback": "The machine only needs your PIN, if requested."},
            {"text": "Fatto. Devo inserire anche il mio gatto nero?", "isCorrect": False, "feedback": "That won't help you get a ticket!"}
        ]
    },
    {
        "id": "m5",
        "role": "host",
        "text": "No, è contactless. Aspetta un momento il biglietto.",
        "english": "No, it is contactless. Wait a moment for the ticket.",
        "choices": [
            {"text": "Dov'è l'uscita del biglietto? Non la vedo bene.", "isCorrect": True, "feedback": "It's important to find where the ticket drops."},
            {"text": "Dov'è l'uscita del cinema? Non la vedo bene.", "isCorrect": False, "feedback": "You are in a metro station, not a cinema."},
            {"text": "Dov'è l'uscita del bosco? Non la vedo bene.", "isCorrect": False, "feedback": "Focus on finding your ticket."}
        ]
    },
    {
        "id": "m6",
        "role": "host",
        "text": "Il biglietto esce nel vano in basso. Eccolo qui!",
        "english": "The ticket comes out in the compartment below. Here it is!",
        "choices": [
            {"text": "Grazie mille. Devo convalidarlo ai tornelli?", "isCorrect": True, "feedback": "Yes, you must use it to enter."},
            {"text": "Grazie mille. Devo cucinarlo con le patate?", "isCorrect": False, "feedback": "Don't cook it! It's a ticket."},
            {"text": "Grazie mille. Devo lavarlo con il sapone?", "isCorrect": False, "feedback": "Keep it dry so it works."}
        ]
    },
    {
        "id": "m7",
        "role": "host",
        "text": "Sì, inseriscilo nella fessura per aprire il tornello.",
        "english": "Yes, insert it into the slot to open the turnstile.",
        "choices": [
            {"text": "Capito. Poi devo riprendere il biglietto, vero?", "isCorrect": True, "feedback": "Correct! You need it to exit later."},
            {"text": "Capito. Poi devo regalare il biglietto, vero?", "isCorrect": False, "feedback": "No, you must keep it for your trip."},
            {"text": "Capito. Poi devo mangiare il biglietto, vero?", "isCorrect": False, "feedback": "Definitely don't eat the ticket."}
        ]
    },
    {
        "id": "m8",
        "role": "host",
        "text": "Esatto. Tienilo con te fino alla fine del viaggio.",
        "english": "Exactly. Keep it with you until the end of the trip.",
        "choices": [
            {"text": "Va bene. Sai quale linea va verso il centro?", "isCorrect": True, "feedback": "Good follow-up question."},
            {"text": "Va bene. Sai quale pizza va verso il centro?", "isCorrect": False, "feedback": "Stick to the metro lines."},
            {"text": "Va bene. Sai quale fiume va verso il centro?", "isCorrect": False, "feedback": "Ask about the metro lines."}
        ]
    },
    {
        "id": "m9",
        "role": "host",
        "text": "Devi prendere la linea rossa in direzione sud.",
        "english": "You should take the red line in the south direction.",
        "choices": [
            {"text": "Grazie per l'aiuto. Buona giornata a lei!", "isCorrect": True, "feedback": "Polite end to the interaction."},
            {"text": "Grazie per l'aiuto. Buona notte a lei!", "isCorrect": False, "feedback": "It is not night time."},
            {"text": "Grazie per l'aiuto. Buona fortuna a lei!", "isCorrect": False, "feedback": "Buona giornata is more standard."}
        ]
    },
    {
        "id": "m10",
        "role": "host",
        "text": "Prego! Buon viaggio in metropolitana.",
        "english": "You're welcome! Have a good trip on the metro.",
        "choices": [
            {"text": "Arrivederci e grazie ancora di tutto.", "isCorrect": True, "feedback": "A perfect goodbye."},
            {"text": "Arrivederci e grazie ancora di nulla.", "isCorrect": False, "feedback": "That sounds a bit rude."},
            {"text": "Arrivederci e grazie ancora di sale.", "isCorrect": False, "feedback": "That doesn't make sense."}
        ]
    }
]

# Conversation 2: Asking for directions to Colosseum
c2_messages = [
    {
        "id": "m1",
        "role": "host",
        "text": "Scusi, la vedo confusa. Cerca una stazione?",
        "english": "Excuse me, you look confused. Are you looking for a station?",
        "choices": [
            {"text": "Sì, vorrei andare al Colosseo con la metro.", "isCorrect": True, "feedback": "Clear goal statement."},
            {"text": "Sì, vorrei andare al cinema con la barca.", "isCorrect": False, "feedback": "You can't take a boat to the cinema here."},
            {"text": "No, vorrei andare al mare con la neve.", "isCorrect": False, "feedback": "That's not possible."}
        ]
    },
    {
        "id": "m2",
        "role": "host",
        "text": "Per il Colosseo deve prendere la linea blu.",
        "english": "For the Colosseum you must take the blue line.",
        "choices": [
            {"text": "Va bene. In quale direzione devo andare?", "isCorrect": True, "feedback": "Crucial question for metro travel."},
            {"text": "Va bene. In quale canzone devo andare?", "isCorrect": False, "feedback": "You need a direction, not a song."},
            {"text": "Va bene. In quale scatola devo andare?", "isCorrect": False, "feedback": "You need to follow a direction."}
        ]
    },
    {
        "id": "m3",
        "role": "host",
        "text": "Deve andare in direzione Laurentina. È chiaro?",
        "english": "You must go in the Laurentina direction. Is it clear?",
        "choices": [
            {"text": "Sì, Laurentina. Quante fermate mancano?", "isCorrect": True, "feedback": "Good to know how long it will take."},
            {"text": "Sì, Laurentina. Quante torte mancano?", "isCorrect": False, "feedback": "Ask about the stops, not cakes."},
            {"text": "Sì, Laurentina. Quante penne mancano?", "isCorrect": False, "feedback": "Focus on the metro stops."}
        ]
    },
    {
        "id": "m4",
        "role": "host",
        "text": "Sono solo tre fermate da qui. È molto veloce.",
        "english": "It's only three stops from here. It's very fast.",
        "choices": [
            {"text": "Ottimo. Devo cambiare linea per arrivare?", "isCorrect": True, "feedback": "Checking for transfers is smart."},
            {"text": "Ottimo. Devo cambiare casa per arrivare?", "isCorrect": False, "feedback": "No need to move house!"},
            {"text": "Ottimo. Devo cambiare aria per arrivare?", "isCorrect": False, "feedback": "Ask about the metro line change."}
        ]
    },
    {
        "id": "m5",
        "role": "host",
        "text": "No, è un viaggio diretto sulla linea blu.",
        "english": "No, it is a direct trip on the blue line.",
        "choices": [
            {"text": "Perfetto. Come si chiama la fermata giusta?", "isCorrect": True, "feedback": "Confirming the name of the stop."},
            {"text": "Perfetto. Come si chiama la pizza giusta?", "isCorrect": False, "feedback": "Stay in the travel context."},
            {"text": "Perfetto. Come si chiama la sedia giusta?", "isCorrect": False, "feedback": "Ask about the metro stop."}
        ]
    },
    {
        "id": "m6",
        "role": "host",
        "text": "La fermata si chiama proprio 'Colosseo'.",
        "english": "The stop is actually called 'Colosseo'.",
        "choices": [
            {"text": "Ah, facile da ricordare! Grazie mille.", "isCorrect": True, "feedback": "Polite and simple."},
            {"text": "Ah, facile da cucinare! Grazie mille.", "isCorrect": False, "feedback": "You aren't cooking the stop name!"},
            {"text": "Ah, facile da lavare! Grazie mille.", "isCorrect": False, "feedback": "Use 'ricordare' for names."}
        ]
    },
    {
        "id": "m7",
        "role": "host",
        "text": "Prego. Tenga d'occhio il display sul treno.",
        "english": "You're welcome. Keep an eye on the display on the train.",
        "choices": [
            {"text": "Sì, lo farò. I treni passano spesso qui?", "isCorrect": True, "feedback": "Asking about frequency."},
            {"text": "Sì, lo farò. I cani passano spesso qui?", "isCorrect": False, "feedback": "You are waiting for trains."},
            {"text": "Sì, lo farò. I venti passano spesso qui?", "isCorrect": False, "feedback": "Focus on the train schedule."}
        ]
    },
    {
        "id": "m8",
        "role": "host",
        "text": "Sì, passa un treno ogni cinque minuti circa.",
        "english": "Yes, a train passes about every five minutes.",
        "choices": [
            {"text": "Benissimo. C'è molta gente a quest'ora?", "isCorrect": True, "feedback": "Natural question about crowds."},
            {"text": "Benissimo. C'è molta frutta a quest'ora?", "isCorrect": False, "feedback": "Ask about the crowd level."},
            {"text": "Benissimo. C'è molta acqua a quest'ora?", "isCorrect": False, "feedback": "The question is about people."}
        ]
    },
    {
        "id": "m9",
        "role": "host",
        "text": "Sì, è l'ora di punta. Sarà un po' affollato.",
        "english": "Yes, it is rush hour. It will be a bit crowded.",
        "choices": [
            {"text": "Va bene, starò attento ai miei oggetti.", "isCorrect": True, "feedback": "Good safety awareness."},
            {"text": "Va bene, starò attento ai miei sogni.", "isCorrect": False, "feedback": "Pay attention to your belongings."},
            {"text": "Va bene, starò attento ai miei libri.", "isCorrect": False, "feedback": "Objects/belongings is more general."}
        ]
    },
    {
        "id": "m10",
        "role": "host",
        "text": "Saggia decisione. Buon viaggio e si diverta!",
        "english": "Wise decision. Have a good trip and enjoy yourself!",
        "choices": [
            {"text": "Grazie ancora dell'aiuto. Arrivederci!", "isCorrect": True, "feedback": "Polite exit."},
            {"text": "Grazie ancora del fumo. Arrivederci!", "isCorrect": False, "feedback": "That's not helpful."},
            {"text": "Grazie ancora del buio. Arrivederci!", "isCorrect": False, "feedback": "Be polite."}
        ]
    }
]

# Conversation 3: On the platform
c3_messages = [
    {
        "id": "m1",
        "role": "host",
        "text": "Scusa, sai se questo è il binario per il centro?",
        "english": "Excuse me, do you know if this is the platform for the center?",
        "choices": [
            {"text": "Sì, credo di sì. Guardo subito la mappa.", "isCorrect": True, "feedback": "Helpful response."},
            {"text": "Sì, credo di sì. Guardo subito la luna.", "isCorrect": False, "feedback": "The moon won't help you navigate the metro."},
            {"text": "No, non credo. Guardo subito il muro.", "isCorrect": False, "feedback": "Look at the map for info."}
        ]
    },
    {
        "id": "m2",
        "role": "host",
        "text": "Grazie. La direzione è 'Termini', giusto?",
        "english": "Thanks. The direction is 'Termini', right?",
        "choices": [
            {"text": "Sì, esatto. Termini è la direzione giusta.", "isCorrect": True, "feedback": "Confirming the direction."},
            {"text": "Sì, esatto. Termini è la colazione giusta.", "isCorrect": False, "feedback": "We are talking about metro directions."},
            {"text": "Sì, esatto. Termini è la vacanza giusta.", "isCorrect": False, "feedback": "Stay in the travel context."}
        ]
    },
    {
        "id": "m3",
        "role": "host",
        "text": "Ottimo. Sai se il prossimo treno è veloce?",
        "english": "Great. Do you know if the next train is fast?",
        "choices": [
            {"text": "Sì, la metro è sempre abbastanza veloce.", "isCorrect": True, "feedback": "General positive statement."},
            {"text": "Sì, la metro è sempre abbastanza salata.", "isCorrect": False, "feedback": "A metro isn't salty!"},
            {"text": "Sì, la metro è sempre abbastanza amara.", "isCorrect": False, "feedback": "Metro trains aren't bitter."}
        ]
    },
    {
        "id": "m4",
        "role": "host",
        "text": "Bene. Hai già timbrato il tuo biglietto?",
        "english": "Good. Have you already stamped your ticket?",
        "choices": [
            {"text": "Sì, l'ho timbrato per entrare dai tornelli.", "isCorrect": True, "feedback": "Correct procedure."},
            {"text": "Sì, l'ho mangiato per entrare dai tornelli.", "isCorrect": False, "feedback": "Don't eat your ticket!"},
            {"text": "Sì, l'ho lavato per entrare dai tornelli.", "isCorrect": False, "feedback": "Keep it dry."}
        ]
    },
    {
        "id": "m5",
        "role": "host",
        "text": "Anch'io. È importante per evitare la multa.",
        "english": "Me too. It is important to avoid the fine.",
        "choices": [
            {"text": "Sì, le multe sono molto care in questa città.", "isCorrect": True, "feedback": "True statement."},
            {"text": "Sì, le torte sono molto care in questa città.", "isCorrect": False, "feedback": "We are talking about fines."},
            {"text": "Sì, le scarpe sono molto care in questa città.", "isCorrect": False, "feedback": "Focus on the context."}
        ]
    },
    {
        "id": "m6",
        "role": "host",
        "text": "Guarda, il treno sta arrivando al binario!",
        "english": "Look, the train is arriving at the platform!",
        "choices": [
            {"text": "Perfetto. Dobbiamo stare dietro la linea gialla.", "isCorrect": True, "feedback": "Important safety rule."},
            {"text": "Perfetto. Dobbiamo stare dietro la linea rossa.", "isCorrect": False, "feedback": "The safety line is yellow."},
            {"text": "Perfetto. Dobbiamo stare dietro la linea verde.", "isCorrect": False, "feedback": "Follow the yellow line rule."}
        ]
    },
    {
        "id": "m7",
        "role": "host",
        "text": "Hai ragione, la sicurezza è fondamentale.",
        "english": "You're right, safety is fundamental.",
        "choices": [
            {"text": "Speriamo di trovare un posto per sedersi.", "isCorrect": True, "feedback": "Common wish on a train."},
            {"text": "Speriamo di trovare un gatto per sedersi.", "isCorrect": False, "feedback": "You need a seat, not a cat."},
            {"text": "Speriamo di trovare un mare per sedersi.", "isCorrect": False, "feedback": "Look for a seat."}
        ]
    },
    {
        "id": "m8",
        "role": "host",
        "text": "Sembra molto affollato, forse staremo in piedi.",
        "english": "It looks very crowded, maybe we will stand.",
        "choices": [
            {"text": "Non importa, il viaggio è molto breve.", "isCorrect": True, "feedback": "Patient attitude."},
            {"text": "Non importa, il viaggio è molto lungo.", "isCorrect": False, "feedback": "You said it was short earlier."},
            {"text": "Non importa, il viaggio è molto caro.", "isCorrect": False, "feedback": "Focus on the duration."}
        ]
    },
    {
        "id": "m9",
        "role": "host",
        "text": "Sì, mancano solo quattro fermate al centro.",
        "english": "Yes, only four stops left to the center.",
        "choices": [
            {"text": "Allora scendiamo insieme alla stazione?", "isCorrect": True, "feedback": "Nice social interaction."},
            {"text": "Allora corriamo insieme alla stazione?", "isCorrect": False, "feedback": "No need to run on the train."},
            {"text": "Allora dormiamo insieme alla stazione?", "isCorrect": False, "feedback": "Stay awake for your stop."}
        ]
    },
    {
        "id": "m10",
        "role": "host",
        "text": "Certamente. Mi fa piacere scambiare due chiacchiere.",
        "english": "Certainly. I'm happy to chat a bit.",
        "choices": [
            {"text": "Anche a me. Saliamo sul treno adesso.", "isCorrect": True, "feedback": "Good transition to boarding."},
            {"text": "Anche a me. Saliamo sul tetto adesso.", "isCorrect": False, "feedback": "Don't go on the roof!"},
            {"text": "Anche a me. Saliamo sul mare adesso.", "isCorrect": False, "feedback": "Get on the train."}
        ]
    }
]

# Conversation 4: Changing lines
c4_messages = [
    {
        "id": "m1",
        "role": "host",
        "text": "Dobbiamo scendere qui per cambiare linea.",
        "english": "We must get off here to change lines.",
        "choices": [
            {"text": "Va bene. Dobbiamo seguire i cartelli?", "isCorrect": True, "feedback": "Good navigation instinct."},
            {"text": "Va bene. Dobbiamo seguire i piccioni?", "isCorrect": False, "feedback": "Pigeons won't help you find the way."},
            {"text": "Va bene. Dobbiamo seguire i sogni?", "isCorrect": False, "feedback": "Follow the signs (cartelli)."}
        ]
    },
    {
        "id": "m2",
        "role": "host",
        "text": "Sì, seguiamo le frecce per la linea rossa.",
        "english": "Yes, let's follow the arrows for the red line.",
        "choices": [
            {"text": "Vedo un cartello lì. Indica a sinistra.", "isCorrect": True, "feedback": "Active participation in finding the way."},
            {"text": "Vedo un gatto lì. Indica a sinistra.", "isCorrect": False, "feedback": "Look for signs, not animals."},
            {"text": "Vedo un mare lì. Indica a sinistra.", "isCorrect": False, "feedback": "Stay in the station context."}
        ]
    },
    {
        "id": "m3",
        "role": "host",
        "text": "Hai ragione. Dobbiamo fare un lungo corridoio.",
        "english": "You're right. We have to walk down a long corridor.",
        "choices": [
            {"text": "Spero che non ci siano troppe scale.", "isCorrect": True, "feedback": "Common concern in metro stations."},
            {"text": "Spero che non ci siano troppe pizze.", "isCorrect": False, "feedback": "Pizzas aren't a problem in corridors."},
            {"text": "Spero che non ci siano troppe penne.", "isCorrect": False, "feedback": "Focus on the physical environment."}
        ]
    },
    {
        "id": "m4",
        "role": "host",
        "text": "Purtroppo ci sono le scale mobili. Sono rotte.",
        "english": "Unfortunately there are escalators. They are broken.",
        "choices": [
            {"text": "Peccato! Allora facciamo le scale a piedi.", "isCorrect": True, "feedback": "Accepting the situation."},
            {"text": "Peccato! Allora facciamo le scale a nuoto.", "isCorrect": False, "feedback": "You can't swim up stairs!"},
            {"text": "Peccato! Allora facciamo le scale a volo.", "isCorrect": False, "feedback": "You have to walk."}
        ]
    },
    {
        "id": "m5",
        "role": "host",
        "text": "Sì, un po' di esercizio fa bene alla salute.",
        "english": "Yes, a bit of exercise is good for your health.",
        "choices": [
            {"text": "Certamente. Siamo arrivati al binario giusto?", "isCorrect": True, "feedback": "Checking progress."},
            {"text": "Certamente. Siamo arrivati al divano giusto?", "isCorrect": False, "feedback": "You are at a platform (binario)."},
            {"text": "Certamente. Siamo arrivati al bosco giusto?", "isCorrect": False, "feedback": "Focus on the metro station."}
        ]
    },
    {
        "id": "m6",
        "role": "host",
        "text": "Sì, questo è il binario della linea rossa.",
        "english": "Yes, this is the red line platform.",
        "choices": [
            {"text": "Ottimo. Qual è la direzione per la spiaggia?", "isCorrect": True, "feedback": "New destination question."},
            {"text": "Ottimo. Qual è la direzione per la pioggia?", "isCorrect": False, "feedback": "You are looking for the beach (spiaggia)."},
            {"text": "Ottimo. Qual è la direzione per la nuvola?", "isCorrect": False, "feedback": "Ask about your destination."}
        ]
    },
    {
        "id": "m7",
        "role": "host",
        "text": "Devi andare verso il capolinea di Ostia.",
        "english": "You must go towards the Ostia terminus.",
        "choices": [
            {"text": "Capito. Il biglietto è valido anche qui?", "isCorrect": True, "feedback": "Important question about validity."},
            {"text": "Capito. Il biglietto è salato anche qui?", "isCorrect": False, "feedback": "Tickets aren't salty."},
            {"text": "Capito. Il biglietto è amaro anche qui?", "isCorrect": False, "feedback": "Question the validity (valido)."}
        ]
    },
    {
        "id": "m8",
        "role": "host",
        "text": "Sì, il biglietto dura cento minuti in totale.",
        "english": "Yes, the ticket lasts one hundred minutes in total.",
        "choices": [
            {"text": "Perfetto, allora ho ancora molto tempo.", "isCorrect": True, "feedback": "Reassured about the ticket."},
            {"text": "Perfetto, allora ho ancora molto riso.", "isCorrect": False, "feedback": "You have time (tempo), not rice."},
            {"text": "Perfetto, allora ho ancora molto sale.", "isCorrect": False, "feedback": "The context is time."}
        ]
    },
    {
        "id": "m9",
        "role": "host",
        "text": "Esatto. Guarda, il treno arriva tra un minuto.",
        "english": "Exactly. Look, the train arrives in one minute.",
        "choices": [
            {"text": "Grazie di tutto, sei stato molto gentile.", "isCorrect": True, "feedback": "Appreciative closing."},
            {"text": "Grazie di tutto, sei stato molto brutto.", "isCorrect": False, "feedback": "That's very mean!"},
            {"text": "Grazie di tutto, sei stato molto freddo.", "isCorrect": False, "feedback": "Be polite."}
        ]
    },
    {
        "id": "m10",
        "role": "host",
        "text": "Di nulla. Buon proseguimento e buona giornata!",
        "english": "You're welcome. Good luck with the rest and have a good day!",
        "choices": [
            {"text": "Grazie, anche a te. Ciao e arrivederci!", "isCorrect": True, "feedback": "Friendly and polite."},
            {"text": "Grazie, anche a te. Ciao e a mai più!", "isCorrect": False, "feedback": "That's a bit harsh."},
            {"text": "Grazie, anche a te. Ciao e a domani!", "isCorrect": False, "feedback": "Arrivederci is more appropriate if you won't see them."}
        ]
    }
]

conversations = [
    {"id": "buying_ticket_machine", "title": "Alla Macchinetta", "description": "Buy a metro ticket using the automatic machine.", "messages": c1_messages},
    {"id": "directions_colosseum", "title": "Direzione Colosseo", "description": "Ask for directions to visit the famous Colosseum.", "messages": c2_messages},
    {"id": "on_the_platform", "title": "Sul Binario", "description": "Confirm the correct direction while waiting on the platform.", "messages": c3_messages},
    {"id": "changing_lines", "title": "Cambio Linea", "description": "Navigate the station to change from one line to another.", "messages": c4_messages}
]

# Validation
for conv in conversations:
    for msg in conv["messages"]:
        correct = [c for c in msg["choices"] if c["isCorrect"]][0]["text"]
        distractors = [c["text"] for c in msg["choices"] if not c["isCorrect"]]
        check_length(correct, distractors[0], distractors[1])

with open("src/data/exports/travel/metro_directions/conversations.json", "w", encoding="utf-8") as f:
    json.dump({"scenarioId": 8, "conversations": conversations}, f, ensure_ascii=False, indent=2)

print("Successfully generated conversations.json")
