import json

scenario_id = 103

conversations = [
    {
        "id": "c1_bad_connection",
        "title": "Bad Connection",
        "description": "Start a video call but experience connection issues.",
        "messages": [
            {
                "id": "c1_m1",
                "role": "host",
                "text": "Ciao! Mi senti bene?",
                "english": "Hi! Can you hear me well?",
                "choices": [
                    {
                        "text": "Ciao, purtroppo ti sento molto male.",
                        "isCorrect": True,
                        "feedback": "Perfetto!"
                    },
                    {
                        "text": "Ciao, la finestra è chiusa ora.",
                        "isCorrect": False,
                        "feedback": "This is about a window, not the call."
                    },
                    {
                        "text": "Ciao, mangio una mela grande.",
                        "isCorrect": False,
                        "feedback": "This means you are eating an apple."
                    }
                ]
            },
            {
                "id": "c1_m2",
                "role": "host",
                "text": "Oh no. Forse è la mia connessione?",
                "english": "Oh no. Maybe it's my connection?",
                "choices": [
                    {
                        "text": "Forse, la tua immagine si blocca.",
                        "isCorrect": True,
                        "feedback": "Esatto!"
                    },
                    {
                        "text": "Forse, il tuo quaderno è piccolo.",
                        "isCorrect": False,
                        "feedback": "This means your notebook is small."
                    },
                    {
                        "text": "Forse, la tua macchina è veloce.",
                        "isCorrect": False,
                        "feedback": "This means your car is fast."
                    }
                ]
            },
            {
                "id": "c1_m3",
                "role": "host",
                "text": "Provo a togliere il video. Meglio ora?",
                "english": "I'll try turning off the video. Better now?",
                "choices": [
                    {
                        "text": "Sì, adesso la voce è più chiara.",
                        "isCorrect": True,
                        "feedback": "Perfetto!"
                    },
                    {
                        "text": "Sì, adesso la sedia è più comoda.",
                        "isCorrect": False,
                        "feedback": "This means the chair is more comfortable."
                    },
                    {
                        "text": "Sì, adesso la mela è più dolce.",
                        "isCorrect": False,
                        "feedback": "This means the apple is sweeter."
                    }
                ]
            },
            {
                "id": "c1_m4",
                "role": "host",
                "text": "Bene. Hai il file per la riunione?",
                "english": "Good. Do you have the file for the meeting?",
                "choices": [
                    {
                        "text": "Sì, ho il file aperto sullo schermo.",
                        "isCorrect": True,
                        "feedback": "Giusto!"
                    },
                    {
                        "text": "Sì, ho il cane chiuso in giardino.",
                        "isCorrect": False,
                        "feedback": "This means you have the dog in the garden."
                    },
                    {
                        "text": "Sì, ho il pane cotto nel forno.",
                        "isCorrect": False,
                        "feedback": "This means you have bread in the oven."
                    }
                ]
            },
            {
                "id": "c1_m5",
                "role": "host",
                "text": "Perfetto, puoi condividere lo schermo?",
                "english": "Perfect, can you share the screen?",
                "choices": [
                    {
                        "text": "Certo, condivido lo schermo subito.",
                        "isCorrect": True,
                        "feedback": "Ottimo!"
                    },
                    {
                        "text": "Certo, pulisco la scarpa stasera.",
                        "isCorrect": False,
                        "feedback": "This means you will clean the shoe."
                    },
                    {
                        "text": "Certo, bevo un bicchiere di latte.",
                        "isCorrect": False,
                        "feedback": "This means you drink a glass of milk."
                    }
                ]
            },
            {
                "id": "c1_m6",
                "role": "host",
                "text": "Lo vedo! Ma sei in muto adesso.",
                "english": "I see it! But you are on mute now.",
                "choices": [
                    {
                        "text": "Scusa, accendo subito il microfono.",
                        "isCorrect": True,
                        "feedback": "Corretto!"
                    },
                    {
                        "text": "Scusa, compro subito il giornale.",
                        "isCorrect": False,
                        "feedback": "This means you buy the newspaper."
                    },
                    {
                        "text": "Scusa, mangio subito il biscotto.",
                        "isCorrect": False,
                        "feedback": "This means you eat the cookie."
                    }
                ]
            },
            {
                "id": "c1_m7",
                "role": "host",
                "text": "Ora ti sento. Andiamo alla pagina due?",
                "english": "Now I hear you. Shall we go to page two?",
                "choices": [
                    {
                        "text": "Va bene, vado alla pagina due.",
                        "isCorrect": True,
                        "feedback": "Esatto!"
                    },
                    {
                        "text": "Va bene, vado alla piazza centrale.",
                        "isCorrect": False,
                        "feedback": "This means you go to the main square."
                    },
                    {
                        "text": "Va bene, vado alla festa stasera.",
                        "isCorrect": False,
                        "feedback": "This means you go to the party."
                    }
                ]
            },
            {
                "id": "c1_m8",
                "role": "host",
                "text": "Vedo dei numeri strani qui. Sbaglio?",
                "english": "I see some strange numbers here. Am I wrong?",
                "choices": [
                    {
                        "text": "Hai ragione, controllo i dati adesso.",
                        "isCorrect": True,
                        "feedback": "Benissimo!"
                    },
                    {
                        "text": "Hai ragione, controllo il gatto fuori.",
                        "isCorrect": False,
                        "feedback": "This means you check the cat outside."
                    },
                    {
                        "text": "Hai ragione, controllo il forno caldo.",
                        "isCorrect": False,
                        "feedback": "This means you check the hot oven."
                    }
                ]
            },
            {
                "id": "c1_m9",
                "role": "host",
                "text": "Ok. La connessione sembra stabile ora, vero?",
                "english": "Ok. The connection seems stable now, right?",
                "choices": [
                    {
                        "text": "Sì, la connessione è molto stabile.",
                        "isCorrect": True,
                        "feedback": "Ottimo!"
                    },
                    {
                        "text": "Sì, la sedia è molto comoda.",
                        "isCorrect": False,
                        "feedback": "This means the chair is comfortable."
                    },
                    {
                        "text": "Sì, la mela è molto dolce.",
                        "isCorrect": False,
                        "feedback": "This means the apple is sweet."
                    }
                ]
            },
            {
                "id": "c1_m10",
                "role": "host",
                "text": "Perfetto. Allora ci aggiorniamo dopo.",
                "english": "Perfect. Then we'll catch up later.",
                "choices": [
                    {
                        "text": "D'accordo, ciao e a più tardi.",
                        "isCorrect": True,
                        "feedback": "Arrivederci!"
                    },
                    {
                        "text": "D'accordo, lavo i piatti stasera.",
                        "isCorrect": False,
                        "feedback": "This means you wash the dishes."
                    },
                    {
                        "text": "D'accordo, compro i libri domani.",
                        "isCorrect": False,
                        "feedback": "This means you buy the books."
                    }
                ]
            }
        ]
    },
    {
        "id": "c2_muted_mic",
        "title": "Muted Microphone",
        "description": "Handle a video call where someone is muted.",
        "messages": [
            {
                "id": "c2_m1",
                "role": "host",
                "text": "Ehi, ci sei? Non ti sento.",
                "english": "Hey, are you there? I can't hear you.",
                "choices": [
                    {
                        "text": "Ci sono, scusa, avevo il microfono spento.",
                        "isCorrect": True,
                        "feedback": "Perfetto!"
                    },
                    {
                        "text": "Ci sono, scusa, avevo il maglione rosso.",
                        "isCorrect": False,
                        "feedback": "This means you had a red sweater."
                    },
                    {
                        "text": "Ci sono, scusa, avevo il gatto grande.",
                        "isCorrect": False,
                        "feedback": "This means you had a big cat."
                    }
                ]
            },
            {
                "id": "c2_m2",
                "role": "host",
                "text": "Ah, ecco. Adesso ti sento forte e chiaro.",
                "english": "Ah, there. Now I hear you loud and clear.",
                "choices": [
                    {
                        "text": "Ottimo, la mia connessione oggi è buona.",
                        "isCorrect": True,
                        "feedback": "Giusto!"
                    },
                    {
                        "text": "Ottimo, la mia colazione oggi è buona.",
                        "isCorrect": False,
                        "feedback": "This means your breakfast is good."
                    },
                    {
                        "text": "Ottimo, la mia macchina oggi è lenta.",
                        "isCorrect": False,
                        "feedback": "This means your car is slow."
                    }
                ]
            },
            {
                "id": "c2_m3",
                "role": "host",
                "text": "Puoi accendere anche la telecamera?",
                "english": "Can you also turn on the camera?",
                "choices": [
                    {
                        "text": "Certo, accendo la telecamera in un attimo.",
                        "isCorrect": True,
                        "feedback": "Esatto!"
                    },
                    {
                        "text": "Certo, accendo la luce nella stanza piccola.",
                        "isCorrect": False,
                        "feedback": "This means you turn on the light in the small room."
                    },
                    {
                        "text": "Certo, lavo la tazza in un secondo.",
                        "isCorrect": False,
                        "feedback": "This means you wash the cup in a second."
                    }
                ]
            },
            {
                "id": "c2_m4",
                "role": "host",
                "text": "Ti vedo. Iniziamo a parlare del progetto?",
                "english": "I see you. Shall we start talking about the project?",
                "choices": [
                    {
                        "text": "Sì, andiamo direttamente al primo punto.",
                        "isCorrect": True,
                        "feedback": "Benissimo!"
                    },
                    {
                        "text": "Sì, mangiamo direttamente un bel gelato.",
                        "isCorrect": False,
                        "feedback": "This means you eat ice cream."
                    },
                    {
                        "text": "Sì, leggiamo direttamente un bel libro.",
                        "isCorrect": False,
                        "feedback": "This means you read a book."
                    }
                ]
            },
            {
                "id": "c2_m5",
                "role": "host",
                "text": "Hai visto il documento che ho inviato?",
                "english": "Did you see the document I sent?",
                "choices": [
                    {
                        "text": "Sì, l'ho appena aperto sul mio schermo.",
                        "isCorrect": True,
                        "feedback": "Corretto!"
                    },
                    {
                        "text": "Sì, l'ho appena perso sul mio tavolo.",
                        "isCorrect": False,
                        "feedback": "This means you lost it on your table."
                    },
                    {
                        "text": "Sì, l'ho appena bevuto sul mio divano.",
                        "isCorrect": False,
                        "feedback": "This means you drank it on your sofa."
                    }
                ]
            },
            {
                "id": "c2_m6",
                "role": "host",
                "text": "Vuoi condividere tu lo schermo per la presentazione?",
                "english": "Do you want to share the screen for the presentation?",
                "choices": [
                    {
                        "text": "Sì, clicco su condividi schermo subito.",
                        "isCorrect": True,
                        "feedback": "Ottimo!"
                    },
                    {
                        "text": "Sì, clicco su compra biglietto subito.",
                        "isCorrect": False,
                        "feedback": "This means you buy a ticket."
                    },
                    {
                        "text": "Sì, clicco su chiudi finestra subito.",
                        "isCorrect": False,
                        "feedback": "This means you close the window."
                    }
                ]
            },
            {
                "id": "c2_m7",
                "role": "host",
                "text": "Ok, vedo tutto. La qualità video è buona.",
                "english": "Ok, I see everything. The video quality is good.",
                "choices": [
                    {
                        "text": "Meno male, temevo che la connessione cadesse.",
                        "isCorrect": True,
                        "feedback": "Giusto!"
                    },
                    {
                        "text": "Meno male, temevo che la mela cadesse.",
                        "isCorrect": False,
                        "feedback": "This means you feared the apple would fall."
                    },
                    {
                        "text": "Meno male, temevo che la borsa cadesse.",
                        "isCorrect": False,
                        "feedback": "This means you feared the bag would fall."
                    }
                ]
            },
            {
                "id": "c2_m8",
                "role": "host",
                "text": "Sì, non preoccuparti. Andiamo avanti.",
                "english": "Yes, don't worry. Let's move forward.",
                "choices": [
                    {
                        "text": "Perfetto, allora passiamo alla prossima slide.",
                        "isCorrect": True,
                        "feedback": "Esatto!"
                    },
                    {
                        "text": "Perfetto, allora passiamo alla prossima pizza.",
                        "isCorrect": False,
                        "feedback": "This means you move to the next pizza."
                    },
                    {
                        "text": "Perfetto, allora passiamo alla prossima piazza.",
                        "isCorrect": False,
                        "feedback": "This means you move to the next square."
                    }
                ]
            },
            {
                "id": "c2_m9",
                "role": "host",
                "text": "Tutto chiaro. Hai altre domande su questo?",
                "english": "Everything is clear. Do you have other questions about this?",
                "choices": [
                    {
                        "text": "No, per me è tutto molto chiaro così.",
                        "isCorrect": True,
                        "feedback": "Benissimo!"
                    },
                    {
                        "text": "No, per me è tutto molto salato così.",
                        "isCorrect": False,
                        "feedback": "This means everything is very salty."
                    },
                    {
                        "text": "No, per me è tutto molto stanco così.",
                        "isCorrect": False,
                        "feedback": "This means everything is very tired."
                    }
                ]
            },
            {
                "id": "c2_m10",
                "role": "host",
                "text": "Perfetto, allora possiamo chiudere la videochiamata.",
                "english": "Perfect, then we can close the video call.",
                "choices": [
                    {
                        "text": "Grazie mille, chiudo la chiamata, buona giornata!",
                        "isCorrect": True,
                        "feedback": "A presto!"
                    },
                    {
                        "text": "Grazie mille, chiudo la porta, buona giornata!",
                        "isCorrect": False,
                        "feedback": "This means you close the door."
                    },
                    {
                        "text": "Grazie mille, chiudo la borsa, buona giornata!",
                        "isCorrect": False,
                        "feedback": "This means you close the bag."
                    }
                ]
            }
        ]
    },
    {
        "id": "c3_screen_share",
        "title": "Screen Sharing",
        "description": "Explaining how to share the screen during a call.",
        "messages": [
            {
                "id": "c3_m1",
                "role": "host",
                "text": "Ciao! Sei pronto per mostrare la presentazione?",
                "english": "Hi! Are you ready to show the presentation?",
                "choices": [
                    {
                        "text": "Sì, sono pronto, dimmi come condividere.",
                        "isCorrect": True,
                        "feedback": "Esatto!"
                    },
                    {
                        "text": "Sì, sono pronto, dimmi come mangiare.",
                        "isCorrect": False,
                        "feedback": "This means tell me how to eat."
                    },
                    {
                        "text": "Sì, sono pronto, dimmi come dormire.",
                        "isCorrect": False,
                        "feedback": "This means tell me how to sleep."
                    }
                ]
            },
            {
                "id": "c3_m2",
                "role": "host",
                "text": "C'è un pulsante verde in basso. Lo vedi?",
                "english": "There is a green button at the bottom. Do you see it?",
                "choices": [
                    {
                        "text": "Sì, vedo il pulsante verde con la freccia.",
                        "isCorrect": True,
                        "feedback": "Perfetto!"
                    },
                    {
                        "text": "Sì, vedo il cane verde con la palla.",
                        "isCorrect": False,
                        "feedback": "This means you see a green dog."
                    },
                    {
                        "text": "Sì, vedo il fiore verde con la foglia.",
                        "isCorrect": False,
                        "feedback": "This means you see a green flower."
                    }
                ]
            },
            {
                "id": "c3_m3",
                "role": "host",
                "text": "Clicca lì. Dovrebbe apparire un menu a tendina.",
                "english": "Click there. A drop-down menu should appear.",
                "choices": [
                    {
                        "text": "Fatto. Ora vedo una finestra con diverse opzioni.",
                        "isCorrect": True,
                        "feedback": "Giusto!"
                    },
                    {
                        "text": "Fatto. Ora vedo una pizza con diversi gusti.",
                        "isCorrect": False,
                        "feedback": "This means you see a pizza with flavors."
                    },
                    {
                        "text": "Fatto. Ora vedo una borsa con diverse penne.",
                        "isCorrect": False,
                        "feedback": "This means you see a bag with pens."
                    }
                ]
            },
            {
                "id": "c3_m4",
                "role": "host",
                "text": "Scegli 'Condividi schermo intero' e poi conferma.",
                "english": "Choose 'Share entire screen' and then confirm.",
                "choices": [
                    {
                        "text": "Ok, ho confermato. Riesci a vedere il mio schermo?",
                        "isCorrect": True,
                        "feedback": "Benissimo!"
                    },
                    {
                        "text": "Ok, ho confermato. Riesci a vedere il mio cane?",
                        "isCorrect": False,
                        "feedback": "This means you ask to see your dog."
                    },
                    {
                        "text": "Ok, ho confermato. Riesci a vedere il mio gatto?",
                        "isCorrect": False,
                        "feedback": "This means you ask to see your cat."
                    }
                ]
            },
            {
                "id": "c3_m5",
                "role": "host",
                "text": "Sì, perfetto. Vedo il tuo schermo ora.",
                "english": "Yes, perfect. I see your screen now.",
                "choices": [
                    {
                        "text": "Ottimo, ora apro il file della presentazione.",
                        "isCorrect": True,
                        "feedback": "Corretto!"
                    },
                    {
                        "text": "Ottimo, ora apro il frigo della cucina.",
                        "isCorrect": False,
                        "feedback": "This means you open the fridge."
                    },
                    {
                        "text": "Ottimo, ora apro il libro di storia.",
                        "isCorrect": False,
                        "feedback": "This means you open the history book."
                    }
                ]
            },
            {
                "id": "c3_m6",
                "role": "host",
                "text": "Riesci a metterla in modalità schermo intero?",
                "english": "Can you put it in full-screen mode?",
                "choices": [
                    {
                        "text": "Certo, clicco sul simbolo dello schermo intero.",
                        "isCorrect": True,
                        "feedback": "Esatto!"
                    },
                    {
                        "text": "Certo, clicco sul simbolo della mela rossa.",
                        "isCorrect": False,
                        "feedback": "This means you click the red apple symbol."
                    },
                    {
                        "text": "Certo, clicco sul simbolo della pizza calda.",
                        "isCorrect": False,
                        "feedback": "This means you click the hot pizza symbol."
                    }
                ]
            },
            {
                "id": "c3_m7",
                "role": "host",
                "text": "Così è molto meglio, si legge benissimo.",
                "english": "That's much better, it reads very well.",
                "choices": [
                    {
                        "text": "Bene, se non mi senti fammi un cenno.",
                        "isCorrect": True,
                        "feedback": "Perfetto!"
                    },
                    {
                        "text": "Bene, se non mi lavi fammi un cenno.",
                        "isCorrect": False,
                        "feedback": "This means if you don't wash me."
                    },
                    {
                        "text": "Bene, se non mi mangi fammi un cenno.",
                        "isCorrect": False,
                        "feedback": "This means if you don't eat me."
                    }
                ]
            },
            {
                "id": "c3_m8",
                "role": "host",
                "text": "Non ti preoccupare, l'audio è perfetto adesso.",
                "english": "Don't worry, the audio is perfect right now.",
                "choices": [
                    {
                        "text": "Grazie, posso iniziare a spiegare la prima parte.",
                        "isCorrect": True,
                        "feedback": "Giusto!"
                    },
                    {
                        "text": "Grazie, posso iniziare a mangiare la prima parte.",
                        "isCorrect": False,
                        "feedback": "This means you eat the first part."
                    },
                    {
                        "text": "Grazie, posso iniziare a bere la prima parte.",
                        "isCorrect": False,
                        "feedback": "This means you drink the first part."
                    }
                ]
            },
            {
                "id": "c3_m9",
                "role": "host",
                "text": "Vai pure. C'è molto ritardo nell'immagine?",
                "english": "Go ahead. Is there much delay in the image?",
                "choices": [
                    {
                        "text": "No, sembra che la connessione sia molto rapida.",
                        "isCorrect": True,
                        "feedback": "Ottimo!"
                    },
                    {
                        "text": "No, sembra che la lumaca sia molto rapida.",
                        "isCorrect": False,
                        "feedback": "This means the snail is very fast."
                    },
                    {
                        "text": "No, sembra che la sedia sia molto comoda.",
                        "isCorrect": False,
                        "feedback": "This means the chair is comfortable."
                    }
                ]
            },
            {
                "id": "c3_m10",
                "role": "host",
                "text": "Ottimo. Continua pure con la presentazione allora.",
                "english": "Great. Please continue with the presentation then.",
                "choices": [
                    {
                        "text": "D'accordo, passo subito alla slide successiva.",
                        "isCorrect": True,
                        "feedback": "Benissimo!"
                    },
                    {
                        "text": "D'accordo, passo subito al negozio successivo.",
                        "isCorrect": False,
                        "feedback": "This means you move to the next shop."
                    },
                    {
                        "text": "D'accordo, passo subito al mercato successivo.",
                        "isCorrect": False,
                        "feedback": "This means you move to the next market."
                    }
                ]
            }
        ]
    },
    {
        "id": "c4_turn_off_camera",
        "title": "Turn Off Camera",
        "description": "Turning off the camera to save bandwidth.",
        "messages": [
            {
                "id": "c4_m1",
                "role": "host",
                "text": "Ciao, purtroppo la tua immagine va a scatti.",
                "english": "Hi, unfortunately your image is stuttering.",
                "choices": [
                    {
                        "text": "Oh, mi dispiace. La connessione è un po' debole oggi.",
                        "isCorrect": True,
                        "feedback": "Perfetto!"
                    },
                    {
                        "text": "Oh, mi dispiace. La finestra è un po' sporca oggi.",
                        "isCorrect": False,
                        "feedback": "This means the window is dirty."
                    },
                    {
                        "text": "Oh, mi dispiace. La maglietta è un po' stretta oggi.",
                        "isCorrect": False,
                        "feedback": "This means the t-shirt is tight."
                    }
                ]
            },
            {
                "id": "c4_m2",
                "role": "host",
                "text": "Forse possiamo spegnere la telecamera per migliorare l'audio?",
                "english": "Maybe we can turn off the camera to improve the audio?",
                "choices": [
                    {
                        "text": "Buona idea, spengo la mia telecamera adesso.",
                        "isCorrect": True,
                        "feedback": "Esatto!"
                    },
                    {
                        "text": "Buona idea, accendo il forno caldo adesso.",
                        "isCorrect": False,
                        "feedback": "This means you turn on the oven."
                    },
                    {
                        "text": "Buona idea, chiudo il libro verde adesso.",
                        "isCorrect": False,
                        "feedback": "This means you close the green book."
                    }
                ]
            },
            {
                "id": "c4_m3",
                "role": "host",
                "text": "Perfetto, ora ti sento molto meglio. Tu mi senti?",
                "english": "Perfect, now I hear you much better. Can you hear me?",
                "choices": [
                    {
                        "text": "Sì, anche io ti sento chiaramente senza il video.",
                        "isCorrect": True,
                        "feedback": "Benissimo!"
                    },
                    {
                        "text": "Sì, anche io mangio chiaramente senza il video.",
                        "isCorrect": False,
                        "feedback": "This means you eat clearly."
                    },
                    {
                        "text": "Sì, anche io dormo chiaramente senza il video.",
                        "isCorrect": False,
                        "feedback": "This means you sleep clearly."
                    }
                ]
            },
            {
                "id": "c4_m4",
                "role": "host",
                "text": "Vuoi che spenga anche io la mia telecamera?",
                "english": "Do you want me to turn off my camera too?",
                "choices": [
                    {
                        "text": "Non è necessario, riesco a vederti bene.",
                        "isCorrect": True,
                        "feedback": "Giusto!"
                    },
                    {
                        "text": "Non è necessario, riesco a mangiarti bene.",
                        "isCorrect": False,
                        "feedback": "This means you can eat me well."
                    },
                    {
                        "text": "Non è necessario, riesco a lavarti bene.",
                        "isCorrect": False,
                        "feedback": "This means you can wash me well."
                    }
                ]
            },
            {
                "id": "c4_m5",
                "role": "host",
                "text": "Va bene, la tengo accesa. Parliamo del lavoro?",
                "english": "Alright, I'll keep it on. Shall we talk about work?",
                "choices": [
                    {
                        "text": "Sì, apriamo il file condiviso per favore.",
                        "isCorrect": True,
                        "feedback": "Corretto!"
                    },
                    {
                        "text": "Sì, apriamo il frigorifero grande per favore.",
                        "isCorrect": False,
                        "feedback": "This means you open the fridge."
                    },
                    {
                        "text": "Sì, chiudiamo la borsa pesante per favore.",
                        "isCorrect": False,
                        "feedback": "This means you close the bag."
                    }
                ]
            },
            {
                "id": "c4_m6",
                "role": "host",
                "text": "Certo, lo sto aprendo. Un secondo di pazienza.",
                "english": "Sure, I'm opening it. A second of patience.",
                "choices": [
                    {
                        "text": "Tranquillo, aspetto che si carichi la pagina.",
                        "isCorrect": True,
                        "feedback": "Ottimo!"
                    },
                    {
                        "text": "Tranquillo, aspetto che si rompa la sedia.",
                        "isCorrect": False,
                        "feedback": "This means you wait for the chair to break."
                    },
                    {
                        "text": "Tranquillo, aspetto che si lavi il gatto.",
                        "isCorrect": False,
                        "feedback": "This means you wait for the cat to wash."
                    }
                ]
            },
            {
                "id": "c4_m7",
                "role": "host",
                "text": "Ecco, ce l'ho. Leggi anche tu il primo paragrafo?",
                "english": "Here, I got it. Are you reading the first paragraph too?",
                "choices": [
                    {
                        "text": "Sì, ho il testo davanti a me sul monitor.",
                        "isCorrect": True,
                        "feedback": "Esatto!"
                    },
                    {
                        "text": "Sì, ho il cane davanti a me sul letto.",
                        "isCorrect": False,
                        "feedback": "This means you have the dog on the bed."
                    },
                    {
                        "text": "Sì, ho il gatto davanti a me sul divano.",
                        "isCorrect": False,
                        "feedback": "This means you have the cat on the sofa."
                    }
                ]
            },
            {
                "id": "c4_m8",
                "role": "host",
                "text": "Perfetto. Secondo te ci sono modifiche da fare?",
                "english": "Perfect. In your opinion, are there modifications to make?",
                "choices": [
                    {
                        "text": "Credo di sì, c'è un errore nella seconda riga.",
                        "isCorrect": True,
                        "feedback": "Giusto!"
                    },
                    {
                        "text": "Credo di sì, c'è un uccello nella seconda stanza.",
                        "isCorrect": False,
                        "feedback": "This means there is a bird in the room."
                    },
                    {
                        "text": "Credo di sì, c'è un gatto nella seconda strada.",
                        "isCorrect": False,
                        "feedback": "This means there is a cat in the street."
                    }
                ]
            },
            {
                "id": "c4_m9",
                "role": "host",
                "text": "Vero! Correggo subito l'errore. Altro da segnalare?",
                "english": "True! I'll fix the error immediately. Anything else to point out?",
                "choices": [
                    {
                        "text": "No, il resto del testo va benissimo così.",
                        "isCorrect": True,
                        "feedback": "Perfetto!"
                    },
                    {
                        "text": "No, il resto del cibo va benissimo così.",
                        "isCorrect": False,
                        "feedback": "This means the rest of the food is fine."
                    },
                    {
                        "text": "No, il resto del vino va benissimo così.",
                        "isCorrect": False,
                        "feedback": "This means the rest of the wine is fine."
                    }
                ]
            },
            {
                "id": "c4_m10",
                "role": "host",
                "text": "Bene, salviamo il file e terminiamo la riunione.",
                "english": "Good, let's save the file and end the meeting.",
                "choices": [
                    {
                        "text": "D'accordo, grazie per il tempo, ci sentiamo presto.",
                        "isCorrect": True,
                        "feedback": "Benissimo!"
                    },
                    {
                        "text": "D'accordo, grazie per il pane, ci mangiamo presto.",
                        "isCorrect": False,
                        "feedback": "This means thanks for the bread."
                    },
                    {
                        "text": "D'accordo, grazie per il vino, ci beviamo presto.",
                        "isCorrect": False,
                        "feedback": "This means thanks for the wine."
                    }
                ]
            }
        ]
    }
]

with open('src/data/exports/tech/video_call/conversations.json', 'w', encoding='utf-8') as f:
    json.dump({"scenarioId": scenario_id, "conversations": conversations}, f, ensure_ascii=False, indent=2)

print("conversations.json generated successfully.")
