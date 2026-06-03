import json

def extend_conversations():
    with open('src/data/exports/tech/using_a_map_app/conversations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    new_messages = {
        "finding_pharmacy": [
            {
                "id": "m6",
                "role": "host",
                "text": "Sei arrivato? C'è la croce verde illuminata fuori?",
                "english": "Are you there? Is there the illuminated green cross outside?",
                "choices": [
                    {"text": "Sì, vedo la croce verde. Entro subito.", "isCorrect": True, "feedback": "Great confirmation of arrival."},
                    {"text": "No, vedo solo un panificio molto grande.", "isCorrect": False, "feedback": "You missed the pharmacy!"},
                    {"text": "C'è un semaforo verde, va bene uguale?", "isCorrect": False, "feedback": "You need the pharmacy cross, not a traffic light."}
                ]
            },
            {
                "id": "m7",
                "role": "host",
                "text": "Benissimo. Cerca anche un bancomat lì vicino sulla mappa?",
                "english": "Great. Can you also look for an ATM nearby on the map?",
                "choices": [
                    {"text": "Controllo l'app. C'è un bancomat a cinquanta metri.", "isCorrect": True, "feedback": "Using the map to find nearby services is smart."},
                    {"text": "Non ho la carta di credito con me oggi.", "isCorrect": False, "feedback": "The host asked to find an ATM on the map."},
                    {"text": "Voglio pagare in contanti, non mi serve.", "isCorrect": False, "feedback": "But you might need cash from the ATM!"}
                ]
            },
            {
                "id": "m8",
                "role": "host",
                "text": "Ottimo. Ricorda di chiudere la navigazione per non consumare batteria.",
                "english": "Excellent. Remember to close the navigation to not drain the battery.",
                "choices": [
                    {"text": "Hai ragione, ho chiuso l'app. La batteria ringrazia!", "isCorrect": True, "feedback": "Good habit to close background apps."},
                    {"text": "Lascio lo schermo acceso per tutta la notte.", "isCorrect": False, "feedback": "That will drain the battery completely."},
                    {"text": "Ho già caricato il telefono ieri mattina.", "isCorrect": False, "feedback": "Navigation uses a lot of battery, it's better to close it."}
                ]
            },
            {
                "id": "m9",
                "role": "host",
                "text": "Perfetto. Hai comprato quello che ti serviva in farmacia?",
                "english": "Perfect. Did you buy what you needed at the pharmacy?",
                "choices": [
                    {"text": "Sì, ho preso le medicine. Ora esco.", "isCorrect": True, "feedback": "Mission accomplished at the pharmacy."},
                    {"text": "Ho comprato un litro di latte fresco da bere.", "isCorrect": False, "feedback": "You don't buy milk at the pharmacy!"},
                    {"text": "Non c'erano vestiti della mia taglia purtroppo.", "isCorrect": False, "feedback": "Pharmacies don't sell clothes."}
                ]
            },
            {
                "id": "m10",
                "role": "host",
                "text": "Molto bene. Usa di nuovo la mappa per tornare in hotel.",
                "english": "Very well. Use the map again to return to the hotel.",
                "choices": [
                    {"text": "Imposto l'hotel come destinazione. A tra poco!", "isCorrect": True, "feedback": "Setting the return destination correctly."},
                    {"text": "Non voglio tornare in hotel, vado a ballare.", "isCorrect": False, "feedback": "The scenario requires returning to the hotel."},
                    {"text": "Il navigatore dice di andare in spiaggia a nuotare.", "isCorrect": False, "feedback": "That's definitely not the hotel!"}
                ]
            }
        ],
        "public_transport": [
            {
                "id": "m6",
                "role": "host",
                "text": "Sei sull'autobus? Quante fermate mancano adesso?",
                "english": "Are you on the bus? How many stops are left now?",
                "choices": [
                    {"text": "Sì, sono sull'autobus. Mancano due fermate.", "isCorrect": True, "feedback": "Checking the progress on the bus."},
                    {"text": "Sono in treno per Milano per il fine settimana.", "isCorrect": False, "feedback": "You should be on the bus to the museum!"},
                    {"text": "Non voglio scendere, mi piace stare sull'autobus.", "isCorrect": False, "feedback": "You have to get off at the museum!"}
                ]
            },
            {
                "id": "m7",
                "role": "host",
                "text": "Preparati a scendere. Suona il campanello prima della fermata.",
                "english": "Get ready to get off. Ring the bell before the stop.",
                "choices": [
                    {"text": "Ho suonato il campanello. Vado verso la porta.", "isCorrect": True, "feedback": "Correct action before getting off a bus."},
                    {"text": "Ho suonato la chitarra per i passeggeri del bus.", "isCorrect": False, "feedback": "Wrong kind of bell or ringing!"},
                    {"text": "Dormo fino alla fine della corsa tranquillamente.", "isCorrect": False, "feedback": "Wake up, you'll miss your stop!"}
                ]
            },
            {
                "id": "m8",
                "role": "host",
                "text": "Sei sceso? Guarda la mappa per trovare l'ingresso del museo.",
                "english": "Did you get off? Look at the map to find the museum entrance.",
                "choices": [
                    {"text": "Sì, sono in piazza. L'app dice di andare a sinistra.", "isCorrect": True, "feedback": "Following directions after leaving the bus."},
                    {"text": "Ho perso la mappa e anche le mie scarpe nuove.", "isCorrect": False, "feedback": "How did you manage to do that?"},
                    {"text": "Il museo è nascosto dentro l'autobus rosso.", "isCorrect": False, "feedback": "Museums are not inside buses."}
                ]
            },
            {
                "id": "m9",
                "role": "host",
                "text": "Vedi l'ingresso principale? Ci dovrebbe essere un po' di coda.",
                "english": "Do you see the main entrance? There should be a bit of a line.",
                "choices": [
                    {"text": "Sì, vedo la coda e l'ingresso. Vado lì.", "isCorrect": True, "feedback": "Identifying the destination."},
                    {"text": "Vedo un cane che mangia un osso gigante.", "isCorrect": False, "feedback": "Look for the entrance, not the dog."},
                    {"text": "L'ingresso è nascosto sotto terra al buio.", "isCorrect": False, "feedback": "It's a regular museum, not a bunker!"}
                ]
            },
            {
                "id": "m10",
                "role": "host",
                "text": "Perfetto. Il tuo biglietto digitale è nell'app, vero?",
                "english": "Perfect. Your digital ticket is in the app, right?",
                "choices": [
                    {"text": "Sì, ho il codice a barre sul telefono. Pronto per entrare!", "isCorrect": True, "feedback": "Ready to enter using the digital ticket."},
                    {"text": "Ho dimenticato il biglietto in albergo sul letto.", "isCorrect": False, "feedback": "But you just said it's digital!"},
                    {"text": "Uso la patente di guida per entrare al museo.", "isCorrect": False, "feedback": "A driver's license is not a museum ticket."}
                ]
            }
        ],
        "gps_problems": [
            {
                "id": "m6",
                "role": "host",
                "text": "Senti la voce guida? Cosa dice di fare adesso?",
                "english": "Do you hear the voice guide? What does it say to do now?",
                "choices": [
                    {"text": "Dice di continuare dritto per duecento metri.", "isCorrect": True, "feedback": "Following audio navigation successfully."},
                    {"text": "Dice di cantare una canzone a voce molto alta.", "isCorrect": False, "feedback": "Navigation apps don't ask you to sing."},
                    {"text": "Non parla italiano, parla solo giapponese antico.", "isCorrect": False, "feedback": "The app should be set to a language you understand."}
                ]
            },
            {
                "id": "m7",
                "role": "host",
                "text": "Bene. Attento a non perdere il segnale di nuovo nei vicoli stretti.",
                "english": "Good. Be careful not to lose the signal again in the narrow alleys.",
                "choices": [
                    {"text": "Starò nelle strade principali per avere un buon segnale.", "isCorrect": True, "feedback": "Smart strategy to avoid losing GPS."},
                    {"text": "Vado proprio nel vicolo più buio della città.", "isCorrect": False, "feedback": "That's a bad idea for GPS signal."},
                    {"text": "Il segnale GPS si mangia a colazione con i biscotti.", "isCorrect": False, "feedback": "That doesn't make any sense."}
                ]
            },
            {
                "id": "m8",
                "role": "host",
                "text": "La voce ha detto di girare? L'incrocio è vicino.",
                "english": "Did the voice say to turn? The intersection is close.",
                "choices": [
                    {"text": "Sì, ha detto di girare a sinistra al semaforo.", "isCorrect": True, "feedback": "Listening to specific turn instructions."},
                    {"text": "Ha detto di comprare un panino al prosciutto cotto.", "isCorrect": False, "feedback": "Voice navigation doesn't give food advice."},
                    {"text": "Giro su me stesso per tre volte di fila.", "isCorrect": False, "feedback": "You are not playing a game, follow the map."}
                ]
            },
            {
                "id": "m9",
                "role": "host",
                "text": "Sei quasi arrivato a destinazione. Il segnale è stabile?",
                "english": "You are almost at your destination. Is the signal stable?",
                "choices": [
                    {"text": "Il segnale è perfetto ora. Manca pochissimo.", "isCorrect": True, "feedback": "Confirming the technical issue is fully resolved."},
                    {"text": "Il segnale è fuggito via lontano in montagna.", "isCorrect": False, "feedback": "Let's hope not!"},
                    {"text": "Sto ancora riavviando il telefono per estrema sicurezza.", "isCorrect": False, "feedback": "You already restarted it."}
                ]
            },
            {
                "id": "m10",
                "role": "host",
                "text": "Ottimo. Arrivo riuscito nonostante i problemi tecnici!",
                "english": "Excellent. Successful arrival despite the technical problems!",
                "choices": [
                    {"text": "Missione compiuta! Grazie per l'aiuto con la mappa.", "isCorrect": True, "feedback": "Polite sign-off after successfully arriving."},
                    {"text": "Ho lanciato il telefono nel fiume per la rabbia.", "isCorrect": False, "feedback": "That's an overreaction!"},
                    {"text": "Mi sono perso per sempre in questa grande città.", "isCorrect": False, "feedback": "But you just said you almost arrived!"}
                ]
            }
        ],
        "offline_maps": [
            {
                "id": "m6",
                "role": "host",
                "text": "Manca molto? Controlla la distanza stimata sulla mappa offline.",
                "english": "Is it much further? Check the estimated distance on the offline map.",
                "choices": [
                    {"text": "Dice che mancano cinquecento metri. Cammino veloce.", "isCorrect": True, "feedback": "Checking progress on the offline map."},
                    {"text": "Mancano cinquecento chilometri per arrivare lì.", "isCorrect": False, "feedback": "That's way too far to walk!"},
                    {"text": "Non c'è scritto nulla, la mappa è di carta vecchia.", "isCorrect": False, "feedback": "You are using a digital offline map."}
                ]
            },
            {
                "id": "m7",
                "role": "host",
                "text": "Hai ancora il cinque per cento di batteria. Abbassa la luminosità dello schermo.",
                "english": "You still have five percent battery. Lower the screen brightness.",
                "choices": [
                    {"text": "L'ho abbassata al minimo. Ottima idea per risparmiare.", "isCorrect": True, "feedback": "Lowering brightness is a great battery-saving tip."},
                    {"text": "Ho messo la luminosità al massimo come il sole.", "isCorrect": False, "feedback": "That will drain the last 5% in seconds."},
                    {"text": "Ho rotto lo schermo così non consuma più niente.", "isCorrect": False, "feedback": "Well, that's one way to do it, but you can't use the phone now!"}
                ]
            },
            {
                "id": "m8",
                "role": "host",
                "text": "Bene. Se il telefono si spegne, chiedi a qualcuno dov'è la piazza principale.",
                "english": "Good. If the phone turns off, ask someone where the main square is.",
                "choices": [
                    {"text": "Certo. Mi ricorderò il nome della piazza, per sicurezza.", "isCorrect": True, "feedback": "Good backup plan if the tech fails."},
                    {"text": "Non parlo con nessuno, ho paura degli sconosciuti.", "isCorrect": False, "feedback": "Sometimes you have to ask for directions."},
                    {"text": "Chiedo dove si compra una mucca in centro.", "isCorrect": False, "feedback": "Not very helpful for finding your way!"}
                ]
            },
            {
                "id": "m9",
                "role": "host",
                "text": "Vedo che sei quasi qui. La mappa offline è stata utile, vero?",
                "english": "I see you are almost here. The offline map was useful, wasn't it?",
                "choices": [
                    {"text": "Molto utile! Senza la mappa offline sarei perso.", "isCorrect": True, "feedback": "Appreciating the feature."},
                    {"text": "No, la mappa offline mi ha fatto cadere nel lago.", "isCorrect": False, "feedback": "The map doesn't control where you walk!"},
                    {"text": "Non ho usato la mappa, ho seguito le stelle nel cielo.", "isCorrect": False, "feedback": "Offline maps are more reliable in the city."}
                ]
            },
            {
                "id": "m10",
                "role": "host",
                "text": "Ti vedo! Ce l'hai fatta e il telefono è ancora acceso. Che fortuna!",
                "english": "I see you! You made it and the phone is still on. How lucky!",
                "choices": [
                    {"text": "Sì, appena in tempo. Ora mi serve il caricatore!", "isCorrect": True, "feedback": "Successfully navigated with low battery."},
                    {"text": "Ho un telefono magico che non si spegne assolutamente mai.", "isCorrect": False, "feedback": "Batteries don't work like that."},
                    {"text": "Non sono io, sono un ologramma venuto dal futuro.", "isCorrect": False, "feedback": "Okay, sci-fi time is over!"}
                ]
            }
        ]
    }

    for conv in data['conversations']:
        conv_id = conv['id']
        if conv_id in new_messages:
            conv['messages'].extend(new_messages[conv_id])
            
    with open('src/data/exports/tech/using_a_map_app/conversations.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    extend_conversations()
    print("Conversations extended successfully.")
