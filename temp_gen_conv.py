import json

def generate_conversations():
    conversations = [
        {
            "id": "passport_control",
            "title": "Controllo Passaporti",
            "description": "Navigate the mandatory passport check upon arrival.",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Buongiorno. Il passaporto e la carta d'imbarco, per favore.",
                    "english": "Good morning. Passport and boarding pass, please.",
                    "choices": [
                        {
                            "text": "Buongiorno. Ecco il mio passaporto e la carta d'imbarco.",
                            "english": "Good morning. Here is my passport and boarding pass.",
                            "isCorrect": True,
                            "feedback": "Perfect! Polite and you provided exactly what was asked."
                        },
                        {
                            "text": "Buongiorno. Cerco la mia valigia nera sul nastro.",
                            "isCorrect": False,
                            "feedback": "You are at passport control, not baggage claim yet!"
                        },
                        {
                            "text": "Buongiorno. Dove posso trovare un taxi per il centro?",
                            "isCorrect": False,
                            "feedback": "Wait until you exit the airport for a taxi."
                        }
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Grazie. Qual è lo scopo del suo viaggio in Italia?",
                    "english": "Thank you. What is the purpose of your trip to Italy?",
                    "choices": [
                        {
                            "text": "Sono qui in vacanza per visitare alcune città d'arte.",
                            "english": "I am here on vacation to visit some art cities.",
                            "isCorrect": True,
                            "feedback": "Great. Stating 'vacanza' (holiday) is a common and clear answer."
                        },
                        {
                            "text": "Ho perso il mio volo per Milano questa mattina.",
                            "isCorrect": False,
                            "feedback": "The officer is asking why you are here, not about flight issues."
                        },
                        {
                            "text": "Vorrei comprare un biglietto per il treno veloce.",
                            "isCorrect": False,
                            "feedback": "You can do that after you pass the control."
                        }
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Molto bene. Quanto tempo ha intenzione di rimanere?",
                    "english": "Very well. How long do you intend to stay?",
                    "choices": [
                        {
                            "text": "Rimango in Italia per circa dieci giorni.",
                            "english": "I am staying in Italy for about ten days.",
                            "isCorrect": True,
                            "feedback": "Correct. Giving a specific duration is helpful."
                        },
                        {
                            "text": "Il mio bagaglio non è arrivato con il volo.",
                            "isCorrect": False,
                            "feedback": "Wrong office! This is passport control."
                        },
                        {
                            "text": "C'è un bagno vicino al controllo passaporti?",
                            "isCorrect": False,
                            "feedback": "Focus on the officer's question first."
                        }
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Dove alloggerà durante la sua permanenza?",
                    "english": "Where will you be staying during your stay?",
                    "choices": [
                        {
                            "text": "Prenderò la navetta per l'hotel in centro.",
                            "english": "I will take the shuttle to the hotel in the center.",
                            "isCorrect": True,
                            "feedback": "Excellent. Explaining your transportation and destination clearly."
                        },
                        {
                            "text": "Mi serve un carrello per trasportare le valigie.",
                            "isCorrect": False,
                            "feedback": "You are still at the passport booth!"
                        },
                        {
                            "text": "Il treno per Roma parte dal binario numero tre.",
                            "isCorrect": False,
                            "feedback": "That's information for later."
                        }
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Ha un biglietto di ritorno per il suo paese?",
                    "english": "Do you have a return ticket to your country?",
                    "choices": [
                        {
                            "text": "Sì, ho il volo di ritorno per il venti maggio.",
                            "english": "Yes, I have the return flight for May 20th.",
                            "isCorrect": True,
                            "feedback": "Good. Providing the date shows you have a plan to return."
                        },
                        {
                            "text": "Mi piace molto mangiare la pizza italiana.",
                            "isCorrect": False,
                            "feedback": "Not relevant to the officer's question about tickets."
                        },
                        {
                            "text": "Il mio passaporto è scaduto l'anno scorso.",
                            "isCorrect": False,
                            "feedback": "Don't say that! You need a valid passport."
                        }
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Viaggia da solo o con la famiglia?",
                    "english": "Are you traveling alone or with your family?",
                    "choices": [
                        {
                            "text": "Viaggio da solo per motivi di turismo.",
                            "english": "I am traveling alone for tourism reasons.",
                            "isCorrect": True,
                            "feedback": "Clear and simple answer."
                        },
                        {
                            "text": "La mia famiglia vive in una grande casa rossa.",
                            "isCorrect": False,
                            "feedback": "The officer is asking about your current trip."
                        },
                        {
                            "text": "Cerco un ristorante aperto a quest'ora.",
                            "isCorrect": False,
                            "feedback": "You are still in the immigration area."
                        }
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "Ha qualcosa da dichiarare alla dogana?",
                    "english": "Do you have anything to declare at customs?",
                    "choices": [
                        {
                            "text": "No, non ho nulla da dichiarare. Solo effetti personali.",
                            "english": "No, I have nothing to declare. Only personal effects.",
                            "isCorrect": True,
                            "feedback": "Standard response if you don't have restricted items."
                        },
                        {
                            "text": "Sì, vorrei comprare un orologio molto costoso.",
                            "isCorrect": False,
                            "feedback": "The officer is asking what you ALREADY have."
                        },
                        {
                            "text": "La dogana è troppo lontana dall'uscita.",
                            "isCorrect": False,
                            "feedback": "Irrelevant to the declaration question."
                        }
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Per favore, metta il pollice destro sullo scanner.",
                    "english": "Please, place your right thumb on the scanner.",
                    "choices": [
                        {
                            "text": "Va bene, ecco il mio pollice sullo scanner.",
                            "english": "Alright, here is my thumb on the scanner.",
                            "isCorrect": True,
                            "feedback": "Following instructions is important for a smooth entry."
                        },
                        {
                            "text": "Ho dimenticato di lavare le mani stamattina.",
                            "isCorrect": False,
                            "feedback": "Just follow the instruction without extra comments."
                        },
                        {
                            "text": "Il mio pollice è molto piccolo e verde.",
                            "isCorrect": False,
                            "feedback": "Nonsense answer."
                        }
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Ha un'assicurazione sanitaria per il viaggio?",
                    "english": "Do you have travel health insurance?",
                    "choices": [
                        {
                            "text": "Sì, ho un'assicurazione valida per tutta l'Europa.",
                            "english": "Yes, I have insurance valid for all of Europe.",
                            "isCorrect": True,
                            "feedback": "Very good. Having insurance is often recommended or required."
                        },
                        {
                            "text": "No, non mangio carne durante il mio soggiorno.",
                            "isCorrect": False,
                            "feedback": "Insurance is about health, not diet!"
                        },
                        {
                            "text": "L'ospedale è vicino alla stazione dei treni.",
                            "isCorrect": False,
                            "feedback": "Answer the question about having insurance."
                        }
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Va bene. Tutto in regola. Benvenuto in Italia!",
                    "english": "Alright. Everything is in order. Welcome to Italy!",
                    "choices": [
                        {
                            "text": "Grazie mille, è stato molto gentile. Arrivederci!",
                            "english": "Thank you very much, you have been very kind. Goodbye!",
                            "isCorrect": True,
                            "feedback": "A polite closing to a successful interaction."
                        },
                        {
                            "text": "Dove posso trovare un carrello per le valigie?",
                            "isCorrect": False,
                            "feedback": "Thank the officer first!"
                        },
                        {
                            "text": "La mia valigia è molto pesante e rossa.",
                            "isCorrect": False,
                            "feedback": "Irrelevant to the passport officer."
                        }
                    ]
                }
            ]
        },
        {
            "id": "baggage_claim",
            "title": "Ritiro Bagagli",
            "description": "Find your luggage and get a trolley.",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Scusi, sa qual è il nastro per il volo da New York?",
                    "english": "Excuse me, do you know which belt is for the flight from New York?",
                    "choices": [
                        {
                            "text": "Sì, deve guardare lo schermo. È il nastro numero otto.",
                            "english": "Yes, you should look at the screen. It is belt number eight.",
                            "isCorrect": True,
                            "feedback": "Correct. Identifying the correct belt via the screens."
                        },
                        {
                            "text": "Il mio passaporto è nuovo e molto blu.",
                            "isCorrect": False,
                            "feedback": "Nobody asked about your passport here."
                        },
                        {
                            "text": "Vorrei un caffè e un cornetto al bar.",
                            "isCorrect": False,
                            "feedback": "Wait until you have your bags!"
                        }
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Ah, grazie. Secondo lei è lontano da qui?",
                    "english": "Ah, thank you. In your opinion, is it far from here?",
                    "choices": [
                        {
                            "text": "No, è proprio qui vicino, dopo le scale mobili.",
                            "english": "No, it's right near here, after the escalators.",
                            "isCorrect": True,
                            "feedback": "Good directions. 'Scale mobili' are escalators."
                        },
                        {
                            "text": "Sì, la dogana è chiusa a quest'ora.",
                            "isCorrect": False,
                            "feedback": "Irrelevant to the distance of the belt."
                        },
                        {
                            "text": "Ho perso il mio volo in coincidenza.",
                            "isCorrect": False,
                            "feedback": "Not related to the location of the belt."
                        }
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Perfetto. Mi serve un carrello per le valigie. Dove sono?",
                    "english": "Perfect. I need a trolley for the suitcases. Where are they?",
                    "choices": [
                        {
                            "text": "Ci sono molti carrelli vicino all'ingresso del nastro.",
                            "english": "There are many trolleys near the belt entrance.",
                            "isCorrect": True,
                            "feedback": "Useful info. Trolleys are usually right there."
                        },
                        {
                            "text": "Il bagno è in fondo al corridoio a destra.",
                            "isCorrect": False,
                            "feedback": "They asked for a trolley, not a toilet!"
                        },
                        {
                            "text": "La mia valigia non è arrivata oggi.",
                            "isCorrect": False,
                            "feedback": "Wait for the bags first before complaining."
                        }
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Eccoli, li vedo. Sa se bisogna pagare per usarli?",
                    "english": "There they are, I see them. Do you know if one has to pay to use them?",
                    "choices": [
                        {
                            "text": "In questo aeroporto i carrelli sono gratuiti.",
                            "english": "In this airport the trolleys are free.",
                            "isCorrect": True,
                            "feedback": "Good to know! 'Gratuiti' means free."
                        },
                        {
                            "text": "Il volo è arrivato con un'ora di ritardo.",
                            "isCorrect": False,
                            "feedback": "Irrelevant to the cost of the trolley."
                        },
                        {
                            "text": "La biglietteria è chiusa per pausa pranzo.",
                            "isCorrect": False,
                            "feedback": "You don't need a ticket office for a trolley."
                        }
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Vedo che il nastro ha iniziato a muoversi!",
                    "english": "I see that the belt has started moving!",
                    "choices": [
                        {
                            "text": "Sì, speriamo che le nostre valigie arrivino presto.",
                            "english": "Yes, let's hope our suitcases arrive soon.",
                            "isCorrect": True,
                            "feedback": "A natural comment while waiting for bags."
                        },
                        {
                            "text": "Il nastro è fatto di cioccolato fondente.",
                            "isCorrect": False,
                            "feedback": "Nonsense answer."
                        },
                        {
                            "text": "Mi serve un taxi per l'aeroporto.",
                            "isCorrect": False,
                            "feedback": "You are already at the airport."
                        }
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Di che colore è la sua valigia?",
                    "english": "What color is your suitcase?",
                    "choices": [
                        {
                            "text": "La mia valigia è grande e di colore blu scuro.",
                            "english": "My suitcase is large and dark blue.",
                            "isCorrect": True,
                            "feedback": "Describing your bag helps you stay focused."
                        },
                        {
                            "text": "Il mio colore preferito è il giallo sole.",
                            "isCorrect": False,
                            "feedback": "The host is asking about the suitcase color."
                        },
                        {
                            "text": "Vengo da una piccola città vicino al mare.",
                            "isCorrect": False,
                            "feedback": "Irrelevant to the suitcase description."
                        }
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "La mia invece è rossa e piccola. Eccola!",
                    "english": "Mine instead is red and small. There it is!",
                    "choices": [
                        {
                            "text": "Ottimo! La prenda pure, io aspetto ancora la mia.",
                            "english": "Great! Go ahead and take it, I'm still waiting for mine.",
                            "isCorrect": True,
                            "feedback": "Polite acknowledgement."
                        },
                        {
                            "text": "La valigia rossa è piena di pomodori.",
                            "isCorrect": False,
                            "feedback": "Unlikely and irrelevant."
                        },
                        {
                            "text": "Dov'è l'ufficio degli oggetti smarriti?",
                            "isCorrect": False,
                            "feedback": "Wait a bit longer before going there."
                        }
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Le serve un aiuto per caricare la valigia sul carrello?",
                    "english": "Do you need help loading the suitcase onto the trolley?",
                    "choices": [
                        {
                            "text": "Grazie, è molto gentile. La mia valigia è pesante.",
                            "english": "Thank you, you are very kind. My suitcase is heavy.",
                            "isCorrect": True,
                            "feedback": "Accepting help politely."
                        },
                        {
                            "text": "No, non mi piace viaggiare in aereo.",
                            "isCorrect": False,
                            "feedback": "Doesn't answer the offer for help."
                        },
                        {
                            "text": "Il carrello ha tre ruote rotte.",
                            "isCorrect": False,
                            "feedback": "Just say yes or no to the help."
                        }
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Adesso dobbiamo andare verso l'uscita, giusto?",
                    "english": "Now we have to go towards the exit, right?",
                    "choices": [
                        {
                            "text": "Sì, l'uscita è dopo la zona della dogana.",
                            "english": "Yes, the exit is after the customs area.",
                            "isCorrect": True,
                            "feedback": "Correct navigation."
                        },
                        {
                            "text": "Sì, vorrei volare di nuovo domani.",
                            "isCorrect": False,
                            "feedback": "Irrelevant to exiting the airport."
                        },
                        {
                            "text": "L'uscita è chiusa per manutenzione.",
                            "isCorrect": False,
                            "feedback": "Unlikely in a major airport."
                        }
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Bene, andiamo allora. Buona giornata!",
                    "english": "Well, let's go then. Have a good day!",
                    "choices": [
                        {
                            "text": "Grazie anche a lei! Arrivederci.",
                            "english": "Thanks to you too! Goodbye.",
                            "isCorrect": True,
                            "feedback": "A friendly and natural closing."
                        },
                        {
                            "text": "Ho fame, dove si mangia una buona pizza?",
                            "isCorrect": False,
                            "feedback": "A bit abrupt. Finish the conversation first."
                        },
                        {
                            "text": "Il controllo passaporti è stato veloce.",
                            "isCorrect": False,
                            "feedback": "That's in the past now."
                        }
                    ]
                }
            ]
        },
        {
            "id": "lost_luggage",
            "title": "Oggetti Smarriti",
            "description": "Report a missing suitcase at the Lost and Found office.",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Buongiorno. Come posso aiutarla oggi?",
                    "english": "Good morning. How can I help you today?",
                    "choices": [
                        {
                            "text": "Buongiorno. Purtroppo la mia valigia non è arrivata.",
                            "english": "Good morning. Unfortunately, my suitcase has not arrived.",
                            "isCorrect": True,
                            "feedback": "Clear and direct. Reporting the problem is the first step."
                        },
                        {
                            "text": "Buongiorno. Vorrei un'informazione sul treno veloce.",
                            "isCorrect": False,
                            "feedback": "This is the Lost and Found office, not the train station."
                        },
                        {
                            "text": "Buongiorno. Il mio passaporto è nel carrello.",
                            "isCorrect": False,
                            "feedback": "Don't leave your passport in a trolley!"
                        }
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Mi dispiace molto. Qual era il suo numero di volo?",
                    "english": "I'm very sorry. What was your flight number?",
                    "choices": [
                        {
                            "text": "Il mio volo era l'AZ 610 da New York JFK.",
                            "english": "My flight was AZ 610 from New York JFK.",
                            "isCorrect": True,
                            "feedback": "Perfect. Flight numbers are essential for tracking."
                        },
                        {
                            "text": "C'è molto traffico fuori dall'aeroporto.",
                            "isCorrect": False,
                            "feedback": "The officer needs your flight details."
                        },
                        {
                            "text": "Vengo dall'Italia e parlo un po' di inglese.",
                            "isCorrect": False,
                            "feedback": "Not helpful for finding a bag."
                        }
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "E di che colore è la sua valigia? È grande o piccola?",
                    "english": "And what color is your suitcase? Is it big or small?",
                    "choices": [
                        {
                            "text": "È una valigia grande, di colore blu scuro.",
                            "english": "It is a large suitcase, dark blue in color.",
                            "isCorrect": True,
                            "feedback": "Good description. Color and size help identification."
                        },
                        {
                            "text": "La mia carta d'identità è scaduta ieri.",
                            "isCorrect": False,
                            "feedback": "Irrelevant to the suitcase description."
                        },
                        {
                            "text": "Il nastro numero otto è fermo ora.",
                            "isCorrect": False,
                            "feedback": "The officer needs the bag details, not the belt status."
                        }
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Ha ancora la ricevuta del bagaglio che le hanno dato al check-in?",
                    "english": "Do you still have the luggage receipt they gave you at check-in?",
                    "choices": [
                        {
                            "text": "Sì, eccola. L'ho attaccata alla carta d'imbarco.",
                            "english": "Yes, here it is. I attached it to the boarding pass.",
                            "isCorrect": True,
                            "feedback": "Excellent. That receipt has the tracking barcode."
                        },
                        {
                            "text": "No, non ho fame in questo momento.",
                            "isCorrect": False,
                            "feedback": "The officer said 'ricevuta' (receipt), not 'ricetta' (recipe) or food!"
                        },
                        {
                            "text": "Il taxi costa troppo per andare in centro.",
                            "isCorrect": False,
                            "feedback": "Irrelevant to the lost luggage process."
                        }
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "D'accordo. Qual è la marca della sua valigia?",
                    "english": "Alright. What is the brand of your suitcase?",
                    "choices": [
                        {
                            "text": "La marca è Samsonite, è un modello rigido.",
                            "english": "The brand is Samsonite, it is a hard-shell model.",
                            "isCorrect": True,
                            "feedback": "Providing the brand helps narrow down the search."
                        },
                        {
                            "text": "La mia marca preferita di pasta è Barilla.",
                            "isCorrect": False,
                            "feedback": "Irrelevant to the suitcase brand."
                        },
                        {
                            "text": "Non mi piacciono i vestiti di marca.",
                            "isCorrect": False,
                            "feedback": "Just state the brand of the bag."
                        }
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "C'è un'etichetta con il suo nome sulla valigia?",
                    "english": "Is there a tag with your name on the suitcase?",
                    "choices": [
                        {
                            "text": "Sì, c'è un'etichetta nera con il mio nome e indirizzo.",
                            "english": "Yes, there is a black tag with my name and address.",
                            "isCorrect": True,
                            "feedback": "Very useful for identifying the owner."
                        },
                        {
                            "text": "Il mio nome è scritto sulla sabbia.",
                            "isCorrect": False,
                            "feedback": "Nonsense answer."
                        },
                        {
                            "text": "Ho perso il mio portafoglio nel taxi.",
                            "isCorrect": False,
                            "feedback": "Focus on the suitcase tag."
                        }
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "Bene. Dove alloggerà qui in città?",
                    "english": "Good. Where will you be staying here in the city?",
                    "choices": [
                        {
                            "text": "Alloggerò presso l'Hotel Roma, in via Nazionale.",
                            "english": "I will be staying at Hotel Roma, on via Nazionale.",
                            "isCorrect": True,
                            "feedback": "They need this to deliver your bag later."
                        },
                        {
                            "text": "Alloggerò in una tenda sulla spiaggia.",
                            "isCorrect": False,
                            "feedback": "Probably not where you want your bag delivered."
                        },
                        {
                            "text": "Il mio amico abita in una città lontana.",
                            "isCorrect": False,
                            "feedback": "Provide your current address."
                        }
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Può lasciarmi un suo numero di telefono?",
                    "english": "Can you leave me your phone number?",
                    "choices": [
                        {
                            "text": "Certamente. Il mio numero è +39 345 678 901.",
                            "english": "Certainly. My number is +39 345 678 901.",
                            "isCorrect": True,
                            "feedback": "Essential for being contacted."
                        },
                        {
                            "text": "Il numero del mio volo era AZ 610.",
                            "isCorrect": False,
                            "feedback": "They asked for your phone number."
                        },
                        {
                            "text": "Non ho un telefono, preferisco le lettere.",
                            "isCorrect": False,
                            "feedback": "Not practical for lost luggage updates."
                        }
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Grazie. Ecco una copia del rapporto di smarrimento.",
                    "english": "Thank you. Here is a copy of the loss report.",
                    "choices": [
                        {
                            "text": "Grazie. Quando pensa che arriverà la valigia?",
                            "english": "Thank you. When do you think the suitcase will arrive?",
                            "isCorrect": True,
                            "feedback": "A fair question to ask."
                        },
                        {
                            "text": "Questa carta è molto bella e bianca.",
                            "isCorrect": False,
                            "feedback": "It's a formal document, not art."
                        },
                        {
                            "text": "Posso avere un caffè mentre aspetto?",
                            "isCorrect": False,
                            "feedback": "You should go to a bar for that."
                        }
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Di solito entro 24 o 48 ore. La chiameremo noi.",
                    "english": "Usually within 24 or 48 hours. We will call you.",
                    "choices": [
                        {
                            "text": "Va bene, aspetterò la vostra chiamata. Arrivederci.",
                            "english": "Alright, I will wait for your call. Goodbye.",
                            "isCorrect": True,
                            "feedback": "A polite and professional conclusion."
                        },
                        {
                            "text": "Dov'è il negozio di souvenir più vicino?",
                            "isCorrect": False,
                            "feedback": "Focus on the lost bag first!"
                        },
                        {
                            "text": "Il mio volo era in ritardo di due ore.",
                            "isCorrect": False,
                            "feedback": "You already gave the flight details."
                        }
                    ]
                }
            ]
        },
        {
            "id": "transportation_to_city",
            "title": "Trasporto per la Città",
            "description": "Find the best way to get to the city center.",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Buongiorno. Ha bisogno di informazioni sui trasporti per il centro?",
                    "english": "Good morning. Do you need information on transport to the center?",
                    "choices": [
                        {
                            "text": "Sì, grazie. Qual è il modo più veloce per arrivare in centro?",
                            "english": "Yes, thank you. What is the fastest way to get to the center?",
                            "isCorrect": True,
                            "feedback": "Good question. Speed is often a priority after a flight."
                        },
                        {
                            "text": "Sì, il mio passaporto è nella borsa.",
                            "isCorrect": False,
                            "feedback": "The host is asking about transport, not documents."
                        },
                        {
                            "text": "Sì, la mia valigia è molto pesante.",
                            "isCorrect": False,
                            "feedback": "They are offering help with directions, not carrying bags."
                        }
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Il treno 'Leonardo Express' è il più veloce. Ci mette solo trenta minuti.",
                    "english": "The 'Leonardo Express' train is the fastest. It only takes thirty minutes.",
                    "choices": [
                        {
                            "text": "Ottimo. Dove posso comprare i biglietti per il treno?",
                            "english": "Great. Where can I buy tickets for the train?",
                            "isCorrect": True,
                            "feedback": "Logic step. Once you pick a transport, you need tickets."
                        },
                        {
                            "text": "Ottimo. Il mio volo è arrivato in anticipo.",
                            "isCorrect": False,
                            "feedback": "Irrelevant to buying train tickets."
                        },
                        {
                            "text": "Ottimo. La dogana è stata molto lenta.",
                            "isCorrect": False,
                            "feedback": "Doesn't help you get to the city."
                        }
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Può comprarli alla biglietteria automatica o allo sportello.",
                    "english": "You can buy them at the automatic ticket machine or at the counter.",
                    "choices": [
                        {
                            "text": "Accettano la carta di credito o solo contanti?",
                            "english": "Do they accept credit cards or only cash?",
                            "isCorrect": True,
                            "feedback": "Important practical question for a traveler."
                        },
                        {
                            "text": "C'è un ristorante tipico qui vicino?",
                            "isCorrect": False,
                            "feedback": "Stay focused on getting your ticket!"
                        },
                        {
                            "text": "Ho perso le chiavi di casa mia.",
                            "isCorrect": False,
                            "feedback": "Not something the transport info desk can help with."
                        }
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Accettano entrambi. La stazione è al piano superiore, segua le indicazioni.",
                    "english": "They accept both. The station is on the upper floor, follow the signs.",
                    "choices": [
                        {
                            "text": "Grazie. Quanto costa un biglietto per la stazione Termini?",
                            "english": "Thank you. How much does a ticket to Termini station cost?",
                            "isCorrect": True,
                            "feedback": "Checking the price is always a good idea."
                        },
                        {
                            "text": "Grazie. Il bagno è molto pulito qui.",
                            "isCorrect": False,
                            "feedback": "A bit of a random comment!"
                        },
                        {
                            "text": "Grazie. Cerco un taxi per l'hotel.",
                            "isCorrect": False,
                            "feedback": "You just decided to take the train!"
                        }
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Il biglietto costa 14 euro. Ricordi di convalidarlo prima di salire.",
                    "english": "The ticket costs 14 euros. Remember to validate it before boarding.",
                    "choices": [
                        {
                            "text": "Capito. Dove si convalidano i biglietti?",
                            "english": "Understood. Where are the tickets validated?",
                            "isCorrect": True,
                            "feedback": "Very important step in Italy to avoid fines."
                        },
                        {
                            "text": "Capito. Mi piace molto il numero quattordici.",
                            "isCorrect": False,
                            "feedback": "Irrelevant to the validation process."
                        },
                        {
                            "text": "Capito. Il treno è fatto di metallo.",
                            "isCorrect": False,
                            "feedback": "Irrelevant observation."
                        }
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Ci sono delle macchinette verdi o gialle all'inizio del binario.",
                    "english": "There are green or yellow machines at the beginning of the platform.",
                    "choices": [
                        {
                            "text": "Perfetto, le cercherò sicuramente.",
                            "english": "Perfect, I will definitely look for them.",
                            "isCorrect": True,
                            "feedback": "Confirmation of understanding."
                        },
                        {
                            "text": "Le macchinette vendono solo caramelle.",
                            "isCorrect": False,
                            "feedback": "In this context, they are for validation."
                        },
                        {
                            "text": "Il verde è il mio colore della fortuna.",
                            "isCorrect": False,
                            "feedback": "Irrelevant to the task."
                        }
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "C'è anche un autobus navetta che costa meno del treno.",
                    "english": "There is also a shuttle bus that costs less than the train.",
                    "choices": [
                        {
                            "text": "Interessante. Quanto tempo ci mette l'autobus?",
                            "english": "Interesting. How long does the bus take?",
                            "isCorrect": True,
                            "feedback": "Comparing time vs cost is smart."
                        },
                        {
                            "text": "L'autobus è troppo grande per me.",
                            "isCorrect": False,
                            "feedback": "Nonsense answer."
                        },
                        {
                            "text": "Preferisco camminare fino al centro.",
                            "isCorrect": False,
                            "feedback": "It's too far to walk from the airport!"
                        }
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "L'autobus ci mette circa un'ora, dipende dal traffico.",
                    "english": "The bus takes about an hour, it depends on the traffic.",
                    "choices": [
                        {
                            "text": "Allora preferisco il treno, è più veloce.",
                            "english": "Then I prefer the train, it's faster.",
                            "isCorrect": True,
                            "feedback": "Making a decision based on the information provided."
                        },
                        {
                            "text": "Il traffico in Italia è sempre molto calmo.",
                            "isCorrect": False,
                            "feedback": "Often not true, especially in big cities."
                        },
                        {
                            "text": "L'ora è composta da sessanta minuti.",
                            "isCorrect": False,
                            "feedback": "Irrelevant fact."
                        }
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Ottima scelta. Il binario del treno è proprio lì davanti.",
                    "english": "Excellent choice. The train platform is right there in front.",
                    "choices": [
                        {
                            "text": "Grazie mille per tutte le informazioni.",
                            "english": "Thank you very much for all the information.",
                            "isCorrect": True,
                            "feedback": "Polite acknowledgement before leaving."
                        },
                        {
                            "text": "Il binario è molto lungo e dritto.",
                            "isCorrect": False,
                            "feedback": "Irrelevant observation."
                        },
                        {
                            "text": "Cerco un volo per la Sicilia.",
                            "isCorrect": False,
                            "feedback": "You just arrived!"
                        }
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Prego. Il treno parte ogni quindici minuti. Buon viaggio!",
                    "english": "You're welcome. The train leaves every fifteen minutes. Have a good trip!",
                    "choices": [
                        {
                            "text": "Grazie di nuovo. Arrivederci!",
                            "english": "Thanks again. Goodbye!",
                            "isCorrect": True,
                            "feedback": "Perfect. A polite way to conclude the interaction."
                        },
                        {
                            "text": "La mia valigia è ancora sul nastro.",
                            "isCorrect": False,
                            "feedback": "If so, you shouldn't be at the transport desk!"
                        },
                        {
                            "text": "Il volo era molto turbolento.",
                            "isCorrect": False,
                            "feedback": "Irrelevant to the final goodbye."
                        }
                    ]
                }
            ]
        }
    ]
    
    output = {
        "scenarioId": 1,
        "conversations": conversations
    }
    
    with open('src/data/exports/travel/airport_arrival/conversations.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_conversations()
