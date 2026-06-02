import json

data = [
    {
        "id": "conv_police_1",
        "title": "Stolen Wallet",
        "turns": [
            {
                "speaker": "host",
                "text": "Buongiorno. Come posso aiutarla?",
                "translation": "Good morning. How can I help you?"
            },
            {
                "speaker": "learner",
                "text": "Buongiorno. Mi hanno rubato il portafoglio.",
                "translation": "Good morning. My wallet was stolen.",
                "choices": [
                    {
                        "text": "Buongiorno. Mi hanno rubato il portafoglio.",
                        "translation": "Good morning. My wallet was stolen.",
                        "is_correct": True
                    },
                    {
                        "text": "Buongiorno. Mi hanno lavato la giacca blu.",
                        "translation": "Good morning. They washed my blue jacket.",
                        "is_correct": False
                    },
                    {
                        "text": "Buongiorno. Mi hanno comprato un libro qui.",
                        "translation": "Good morning. They bought me a book here.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Mi dispiace. Dove è successo?",
                "translation": "I'm sorry. Where did it happen?"
            },
            {
                "speaker": "learner",
                "text": "È successo sull'autobus, un'ora fa.",
                "translation": "It happened on the bus, an hour ago.",
                "choices": [
                    {
                        "text": "È successo sull'autobus, un'ora fa.",
                        "translation": "It happened on the bus, an hour ago.",
                        "is_correct": True
                    },
                    {
                        "text": "È successo nel cinema, ieri sera.",
                        "translation": "It happened in the cinema, last night.",
                        "is_correct": False
                    },
                    {
                        "text": "È successo in piscina, tre ore fa.",
                        "translation": "It happened in the pool, three hours ago.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Cosa c'era nel portafoglio?",
                "translation": "What was in the wallet?"
            },
            {
                "speaker": "learner",
                "text": "I miei documenti e un po' di soldi.",
                "translation": "My documents and some money.",
                "choices": [
                    {
                        "text": "I miei documenti e un po' di soldi.",
                        "translation": "My documents and some money.",
                        "is_correct": True
                    },
                    {
                        "text": "Le mie chiavi e un po' di formaggio.",
                        "translation": "My keys and some cheese.",
                        "is_correct": False
                    },
                    {
                        "text": "Il mio quaderno e una bella foto.",
                        "translation": "My notebook and a nice photo.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Ha la sua carta d'identità?",
                "translation": "Do you have your ID card?"
            },
            {
                "speaker": "learner",
                "text": "No, era nel portafoglio rubato.",
                "translation": "No, it was in the stolen wallet.",
                "choices": [
                    {
                        "text": "No, era nel portafoglio rubato.",
                        "translation": "No, it was in the stolen wallet.",
                        "is_correct": True
                    },
                    {
                        "text": "No, era nel ristorante costoso.",
                        "translation": "No, it was in the expensive restaurant.",
                        "is_correct": False
                    },
                    {
                        "text": "No, era nel cestino della spesa.",
                        "translation": "No, it was in the shopping basket.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Dobbiamo fare una denuncia. Ha un altro documento?",
                "translation": "We need to file a report. Do you have another document?"
            },
            {
                "speaker": "learner",
                "text": "Sì, ho il mio passaporto in hotel.",
                "translation": "Yes, I have my passport at the hotel.",
                "choices": [
                    {
                        "text": "Sì, ho il mio passaporto in hotel.",
                        "translation": "Yes, I have my passport at the hotel.",
                        "is_correct": True
                    },
                    {
                        "text": "Sì, ho il mio gatto in camera.",
                        "translation": "Yes, I have my cat in the room.",
                        "is_correct": False
                    },
                    {
                        "text": "Sì, ho il mio quaderno a scuola.",
                        "translation": "Yes, I have my notebook at school.",
                        "is_correct": False
                    }
                ]
            }
        ]
    },
    {
        "id": "conv_police_2",
        "title": "Lost Passport",
        "turns": [
            {
                "speaker": "host",
                "text": "Salve. Prego, si accomodi.",
                "translation": "Hello. Please, take a seat."
            },
            {
                "speaker": "learner",
                "text": "Salve. Ho perso il mio passaporto.",
                "translation": "Hello. I lost my passport.",
                "choices": [
                    {
                        "text": "Salve. Ho perso il mio passaporto.",
                        "translation": "Hello. I lost my passport.",
                        "is_correct": True
                    },
                    {
                        "text": "Salve. Ho letto il tuo messaggio.",
                        "translation": "Hello. I read your message.",
                        "is_correct": False
                    },
                    {
                        "text": "Salve. Ho mangiato la mia mela.",
                        "translation": "Hello. I ate my apple.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Quando ha visto il passaporto l'ultima volta?",
                "translation": "When did you see the passport for the last time?"
            },
            {
                "speaker": "learner",
                "text": "L'ho visto ieri sera in albergo.",
                "translation": "I saw it last night in the hotel.",
                "choices": [
                    {
                        "text": "L'ho visto ieri sera in albergo.",
                        "translation": "I saw it last night in the hotel.",
                        "is_correct": True
                    },
                    {
                        "text": "L'ho letto oggi pomeriggio a casa.",
                        "translation": "I read it this afternoon at home.",
                        "is_correct": False
                    },
                    {
                        "text": "L'ho preso stamattina in farmacia.",
                        "translation": "I took it this morning at the pharmacy.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "È sicuro di non averlo dimenticato lì?",
                "translation": "Are you sure you didn't forget it there?"
            },
            {
                "speaker": "learner",
                "text": "Sì, ho già cercato dappertutto in camera.",
                "translation": "Yes, I already looked everywhere in the room.",
                "choices": [
                    {
                        "text": "Sì, ho già cercato dappertutto in camera.",
                        "translation": "Yes, I already looked everywhere in the room.",
                        "is_correct": True
                    },
                    {
                        "text": "Sì, ho già cucinato la pasta in cucina.",
                        "translation": "Yes, I already cooked the pasta in the kitchen.",
                        "is_correct": False
                    },
                    {
                        "text": "Sì, ho già studiato tanto per l'esame.",
                        "translation": "Yes, I already studied a lot for the exam.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Compili questo modulo, per favore.",
                "translation": "Fill out this form, please."
            },
            {
                "speaker": "learner",
                "text": "Va bene, ho bisogno di una penna.",
                "translation": "Alright, I need a pen.",
                "choices": [
                    {
                        "text": "Va bene, ho bisogno di una penna.",
                        "translation": "Alright, I need a pen.",
                        "is_correct": True
                    },
                    {
                        "text": "Va bene, ho paura di quel cane.",
                        "translation": "Alright, I am afraid of that dog.",
                        "is_correct": False
                    },
                    {
                        "text": "Va bene, ho voglia di una pizza.",
                        "translation": "Alright, I am craving a pizza.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Ecco la penna. Scriva in stampatello.",
                "translation": "Here is the pen. Write in block letters."
            },
            {
                "speaker": "learner",
                "text": "Grazie mille per l'aiuto.",
                "translation": "Thank you very much for the help.",
                "choices": [
                    {
                        "text": "Grazie mille per l'aiuto.",
                        "translation": "Thank you very much for the help.",
                        "is_correct": True
                    },
                    {
                        "text": "Grazie mille per il libro.",
                        "translation": "Thank you very much for the book.",
                        "is_correct": False
                    },
                    {
                        "text": "Grazie mille per il caffè.",
                        "translation": "Thank you very much for the coffee.",
                        "is_correct": False
                    }
                ]
            }
        ]
    },
    {
        "id": "conv_police_3",
        "title": "Stolen Phone",
        "turns": [
            {
                "speaker": "host",
                "text": "Buongiorno. Ha bisogno di aiuto?",
                "translation": "Good morning. Do you need help?"
            },
            {
                "speaker": "learner",
                "text": "Sì, qualcuno ha rubato il mio cellulare.",
                "translation": "Yes, someone stole my cellphone.",
                "choices": [
                    {
                        "text": "Sì, qualcuno ha rubato il mio cellulare.",
                        "translation": "Yes, someone stole my cellphone.",
                        "is_correct": True
                    },
                    {
                        "text": "Sì, qualcuno ha bevuto il mio tè verde.",
                        "translation": "Yes, someone drank my green tea.",
                        "is_correct": False
                    },
                    {
                        "text": "Sì, qualcuno ha trovato il mio cappello.",
                        "translation": "Yes, someone found my hat.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Dove si trovava quando è successo?",
                "translation": "Where were you when it happened?"
            },
            {
                "speaker": "learner",
                "text": "Ero in piazza, c'era molta gente.",
                "translation": "I was in the square, there were a lot of people.",
                "choices": [
                    {
                        "text": "Ero in piazza, c'era molta gente.",
                        "translation": "I was in the square, there were a lot of people.",
                        "is_correct": True
                    },
                    {
                        "text": "Ero in teatro, c'era un bel film.",
                        "translation": "I was in the theater, there was a nice movie.",
                        "is_correct": False
                    },
                    {
                        "text": "Ero al mare, c'era molto freddo.",
                        "translation": "I was at the sea, it was very cold.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Che marca e modello era il telefono?",
                "translation": "What brand and model was the phone?"
            },
            {
                "speaker": "learner",
                "text": "Era uno smartphone nero con una cover rossa.",
                "translation": "It was a black smartphone with a red cover.",
                "choices": [
                    {
                        "text": "Era uno smartphone nero con una cover rossa.",
                        "translation": "It was a black smartphone with a red cover.",
                        "is_correct": True
                    },
                    {
                        "text": "Era una macchina blu con le ruote grandi.",
                        "translation": "It was a blue car with big wheels.",
                        "is_correct": False
                    },
                    {
                        "text": "Era una borsa verde con una tasca nuova.",
                        "translation": "It was a green bag with a new pocket.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Conosce il numero di serie del telefono?",
                "translation": "Do you know the serial number of the phone?"
            },
            {
                "speaker": "learner",
                "text": "No, non lo ricordo a memoria.",
                "translation": "No, I don't remember it by heart.",
                "choices": [
                    {
                        "text": "No, non lo ricordo a memoria.",
                        "translation": "No, I don't remember it by heart.",
                        "is_correct": True
                    },
                    {
                        "text": "No, non ho bevuto molta acqua.",
                        "translation": "No, I didn't drink much water.",
                        "is_correct": False
                    },
                    {
                        "text": "No, non ho visto quel ragazzo.",
                        "translation": "No, I didn't see that boy.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Deve chiamare la sua compagnia telefonica per bloccarlo.",
                "translation": "You must call your phone company to block it."
            },
            {
                "speaker": "learner",
                "text": "Va bene, lo farò immediatamente.",
                "translation": "Alright, I will do it immediately.",
                "choices": [
                    {
                        "text": "Va bene, lo farò immediatamente.",
                        "translation": "Alright, I will do it immediately.",
                        "is_correct": True
                    },
                    {
                        "text": "Va bene, lo berrò molto freddo.",
                        "translation": "Alright, I will drink it very cold.",
                        "is_correct": False
                    },
                    {
                        "text": "Va bene, lo leggerò velocemente.",
                        "translation": "Alright, I will read it quickly.",
                        "is_correct": False
                    }
                ]
            }
        ]
    },
    {
        "id": "conv_police_4",
        "title": "Filing the Report",
        "turns": [
            {
                "speaker": "host",
                "text": "Dobbiamo scrivere i suoi dati personali.",
                "translation": "We need to write your personal details."
            },
            {
                "speaker": "learner",
                "text": "Certo. Quali dati le servono?",
                "translation": "Sure. What details do you need?",
                "choices": [
                    {
                        "text": "Certo. Quali dati le servono?",
                        "translation": "Sure. What details do you need?",
                        "is_correct": True
                    },
                    {
                        "text": "Certo. Quali libri le piacciono?",
                        "translation": "Sure. What books do you like?",
                        "is_correct": False
                    },
                    {
                        "text": "Certo. Quali scarpe le servono?",
                        "translation": "Sure. What shoes do you need?",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Il suo nome, cognome e data di nascita.",
                "translation": "Your name, surname and date of birth."
            },
            {
                "speaker": "learner",
                "text": "Mi chiamo Mario Rossi, nato il tre marzo.",
                "translation": "My name is Mario Rossi, born on the third of March.",
                "choices": [
                    {
                        "text": "Mi chiamo Mario Rossi, nato il tre marzo.",
                        "translation": "My name is Mario Rossi, born on the third of March.",
                        "is_correct": True
                    },
                    {
                        "text": "Mi piace molto il pane cotto nel forno.",
                        "translation": "I really like bread baked in the oven.",
                        "is_correct": False
                    },
                    {
                        "text": "Voglio studiare molto bene la lezione.",
                        "translation": "I want to study the lesson very well.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Qual è il suo indirizzo in Italia?",
                "translation": "What is your address in Italy?"
            },
            {
                "speaker": "learner",
                "text": "Alloggio all'Hotel Roma in centro.",
                "translation": "I am staying at Hotel Roma in the center.",
                "choices": [
                    {
                        "text": "Alloggio all'Hotel Roma in centro.",
                        "translation": "I am staying at Hotel Roma in the center.",
                        "is_correct": True
                    },
                    {
                        "text": "Mangio una pizza grande in pizzeria.",
                        "translation": "I eat a large pizza in the pizzeria.",
                        "is_correct": False
                    },
                    {
                        "text": "Compro un regalo per mia madre oggi.",
                        "translation": "I buy a gift for my mother today.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "E il suo numero di telefono per contattarla?",
                "translation": "And your phone number to contact you?"
            },
            {
                "speaker": "learner",
                "text": "Il mio numero è tre quattro due uno.",
                "translation": "My number is three four two one.",
                "choices": [
                    {
                        "text": "Il mio numero è tre quattro due uno.",
                        "translation": "My number is three four two one.",
                        "is_correct": True
                    },
                    {
                        "text": "Il mio gatto è molto stanco oggi.",
                        "translation": "My cat is very tired today.",
                        "is_correct": False
                    },
                    {
                        "text": "Il mio amico è felice di vederti.",
                        "translation": "My friend is happy to see you.",
                        "is_correct": False
                    }
                ]
            },
            {
                "speaker": "host",
                "text": "Firmi la denuncia qui in basso.",
                "translation": "Sign the report down here."
            },
            {
                "speaker": "learner",
                "text": "Ecco la firma. Cosa devo fare ora?",
                "translation": "Here is the signature. What should I do now?",
                "choices": [
                    {
                        "text": "Ecco la firma. Cosa devo fare ora?",
                        "translation": "Here is the signature. What should I do now?",
                        "is_correct": True
                    },
                    {
                        "text": "Ecco la torta. Quando devo uscire da qui?",
                        "translation": "Here is the cake. When should I leave here?",
                        "is_correct": False
                    },
                    {
                        "text": "Ecco la borsa. Perché devo correre tanto?",
                        "translation": "Here is the bag. Why do I have to run so much?",
                        "is_correct": False
                    }
                ]
            }
        ]
    }
]

with open("src/data/exports/miscellaneous/police_report/conversations.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
