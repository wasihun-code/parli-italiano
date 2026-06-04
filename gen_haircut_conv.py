import json

def get_length_range(text):
    l = len(text)
    return int(l * 0.6), int(l * 1.4)

def check_distractor(correct_text, distractor_text):
    min_l, max_l = get_length_range(correct_text)
    return min_l <= len(distractor_text) <= max_l

scenario = {
    "scenarioId": 53,
    "conversations": [
        {
            "id": "booking_haircut",
            "title": "Booking a Haircut",
            "description": "Call the hair salon to book an appointment for tomorrow.",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Buongiorno, Parrucchiere da Marco. Come posso aiutarla?",
                    "english": "Good morning, Marco's Hair Salon. How can I help you?",
                    "choices": [
                        {
                            "text": "Buongiorno, vorrei prenotare un taglio per domani.",
                            "english": "Good morning, I would like to book a cut for tomorrow.",
                            "isCorrect": True,
                            "feedback": "Perfect! Clear and polite request for an appointment."
                        },
                        {
                            "text": "Ciao, dove sono le mie forbici per i capelli?",
                            "english": "Hi, where are my hair scissors?",
                            "isCorrect": False,
                            "feedback": "A bit informal, and you aren't looking for scissors!"
                        },
                        {
                            "text": "Buongiorno, vorrei mangiare una pizza grande.",
                            "english": "Good morning, I would like to eat a large pizza.",
                            "isCorrect": False,
                            "feedback": "Wrong place! This is a hair salon, not a pizzeria."
                        }
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Certamente. Preferisce la mattina o il pomeriggio?",
                    "english": "Certainly. Do you prefer the morning or the afternoon?",
                    "choices": [
                        {
                            "text": "Preferisco la mattina, verso le dieci è possibile?",
                            "english": "I prefer the morning, is it possible around ten?",
                            "isCorrect": True,
                            "feedback": "Good. Specifying a time makes booking easier."
                        },
                        {
                            "text": "Preferisco il treno delle dieci per andare via.",
                            "english": "I prefer the ten o'clock train to go away.",
                            "isCorrect": False,
                            "feedback": "You are booking a haircut, not a train ticket!"
                        },
                        {
                            "text": "Sì, mi piace molto la mattina quando c'è il sole.",
                            "english": "Yes, I like the morning very much when it's sunny.",
                            "isCorrect": False,
                            "feedback": "A bit vague. You need to pick a time."
                        }
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Alle dieci è perfetto. Solo taglio o vuole anche il colore?",
                    "english": "Ten o'clock is perfect. Just a cut or do you also want color?",
                    "choices": [
                        {
                            "text": "Solo taglio e shampoo, grazie. Quanto tempo ci vuole?",
                            "english": "Just a cut and shampoo, thanks. How long does it take?",
                            "isCorrect": True,
                            "feedback": "Great. Clarifying the service and asking for duration."
                        },
                        {
                            "text": "Vorrei un volo per Roma, grazie per l'informazione.",
                            "english": "I would like a flight to Rome, thanks for the info.",
                            "isCorrect": False,
                            "feedback": "Off-topic! No flights here."
                        },
                        {
                            "text": "Sì, mi piace il colore rosso per la mia nuova auto.",
                            "english": "Yes, I like the color red for my new car.",
                            "isCorrect": False,
                            "feedback": "The host is asking if you WANT a color service now."
                        }
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Circa un'ora. Mi può dire il suo nome, per favore?",
                    "english": "About an hour. Can you tell me your name, please?",
                    "choices": [
                        {
                            "text": "Mi chiamo Luca. Ci vediamo domani alle dieci allora.",
                            "english": "My name is Luca. See you tomorrow at ten then.",
                            "isCorrect": True,
                            "feedback": "Excellent. You provided your name and confirmed the time."
                        },
                        {
                            "text": "Mi chiamo Luca e sono un barbiere molto bravo qui.",
                            "english": "My name is Luca and I am a very good barber here.",
                            "isCorrect": False,
                            "feedback": "You are the customer here, not the barber!"
                        },
                        {
                            "text": "Il mio nome è Luca e cerco un film da vedere oggi.",
                            "english": "My name is Luca and I'm looking for a movie to see today.",
                            "isCorrect": False,
                            "feedback": "No movies at the hairdresser!"
                        }
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Perfetto, Luca. Appuntamento fissato. Ha un numero di telefono?",
                    "english": "Perfect, Luca. Appointment set. Do you have a phone number?",
                    "choices": [
                        {
                            "text": "Sì, il mio numero è 340 1234567. Mi manda un messaggio?",
                            "english": "Yes, my number is 340 1234567. Will you send me a message?",
                            "isCorrect": True,
                            "feedback": "Great. Providing contact info for the reminder."
                        },
                        {
                            "text": "No, non ho un telefono ma ho un vecchio computer.",
                            "english": "No, I don't have a phone but I have an old computer.",
                            "isCorrect": False,
                            "feedback": "They need a way to contact you for the appointment."
                        },
                        {
                            "text": "Sì, il mio numero preferito è il sette fortuna.",
                            "english": "Yes, my favorite number is lucky seven.",
                            "isCorrect": False,
                            "feedback": "They need your phone number, not your lucky number!"
                        }
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Certo, le mando un promemoria stasera. È la prima volta qui?",
                    "english": "Sure, I'll send you a reminder tonight. Is it your first time here?",
                    "choices": [
                        {
                            "text": "Sì, è la prima volta. Ho letto ottime recensioni online.",
                            "english": "Yes, it's the first time. I read great reviews online.",
                            "isCorrect": True,
                            "feedback": "Good answer. Reviews are a common way to find salons."
                        },
                        {
                            "text": "No, non mangio mai qui perché non mi piace il cibo.",
                            "english": "No, I never eat here because I don't like the food.",
                            "isCorrect": False,
                            "feedback": "Again, this is not a restaurant!"
                        },
                        {
                            "text": "Sì, la prima volta che vado al mare questo anno.",
                            "english": "Yes, the first time I go to the sea this year.",
                            "isCorrect": False,
                            "feedback": "Stay focused on the salon visit."
                        }
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "Mi fa piacere! Preferisce un parrucchiere in particolare?",
                    "english": "I'm glad! Do you prefer a particular hairdresser?",
                    "choices": [
                        {
                            "text": "No, non conosco nessuno. Mi fido della vostra scelta.",
                            "english": "No, I don't know anyone. I trust your choice.",
                            "isCorrect": True,
                            "feedback": "Polite and easy for the host to manage."
                        },
                        {
                            "text": "Sì, preferisco un medico che parla molto bene inglese.",
                            "english": "Yes, I prefer a doctor who speaks English very well.",
                            "isCorrect": False,
                            "feedback": "You need a hairdresser, not a doctor!"
                        },
                        {
                            "text": "No, non mi piace nessuno in questa città grande.",
                            "english": "No, I don't like anyone in this big city.",
                            "isCorrect": False,
                            "feedback": "That's a bit negative and off-topic."
                        }
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Va bene. Domani ci sarà Marco, è il nostro esperto.",
                    "english": "Alright. Tomorrow Marco will be there, he is our expert.",
                    "choices": [
                        {
                            "text": "Ottimo, grazie mille. Marco sembra molto bravo.",
                            "english": "Great, thanks a lot. Marco seems very good.",
                            "isCorrect": True,
                            "feedback": "Positive confirmation."
                        },
                        {
                            "text": "Marco è un nome che non mi piace per niente.",
                            "english": "Marco is a name that I don't like at all.",
                            "isCorrect": False,
                            "feedback": "Don't be rude about the stylist's name!"
                        },
                        {
                            "text": "Ottimo, vorrei comprare un giornale da Marco.",
                            "english": "Great, I would like to buy a newspaper from Marco.",
                            "isCorrect": False,
                            "feedback": "He is a hairdresser, not a newsstand owner."
                        }
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Lo è! Ricordi che siamo in via Roma 10, vicino alla banca.",
                    "english": "He is! Remember we are at via Roma 10, near the bank.",
                    "choices": [
                        {
                            "text": "Va bene, conosco la zona. Non avrò problemi a trovarvi.",
                            "english": "Alright, I know the area. I won't have problems finding you.",
                            "isCorrect": True,
                            "feedback": "Confirming you know the location."
                        },
                        {
                            "text": "La banca è chiusa oggi perché è domenica pomeriggio.",
                            "english": "The bank is closed today because it's Sunday afternoon.",
                            "isCorrect": False,
                            "feedback": "Irrelevant information about the bank's hours."
                        },
                        {
                            "text": "Vorrei aprire un conto in via Roma domani mattina.",
                            "english": "I would like to open an account in via Roma tomorrow morning.",
                            "isCorrect": False,
                            "feedback": "You are going for a haircut, not to the bank!"
                        }
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Perfetto. Allora ci vediamo domani alle dieci. Buona giornata!",
                    "english": "Perfect. Then we'll see you tomorrow at ten. Have a good day!",
                    "choices": [
                        {
                            "text": "Grazie mille, a domani! Buona giornata anche a lei.",
                            "english": "Thanks a lot, see you tomorrow! Have a good day too.",
                            "isCorrect": True,
                            "feedback": "Polite exit. You successfully finished the call."
                        },
                        {
                            "text": "Grazie, voglio pagare tutto adesso con la carta.",
                            "english": "Thanks, I want to pay everything now with the card.",
                            "isCorrect": False,
                            "feedback": "You pay at the salon tomorrow, not on the phone."
                        },
                        {
                            "text": "Sì, a domani al cinema per vedere quel film.",
                            "english": "Yes, see you tomorrow at the cinema to see that movie.",
                            "isCorrect": False,
                            "feedback": "Remember, you are going to the hairdresser!"
                        }
                    ]
                }
            ]
        },
        {
            "id": "describing_style",
            "title": "Describing the Style",
            "description": "Explain to the hairdresser exactly how you want your hair cut.",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Buongiorno! Si sieda pure qui. Come li facciamo oggi?",
                    "english": "Good morning! Have a seat here. How are we doing them today?",
                    "choices": [
                        {
                            "text": "Buongiorno. Vorrei un taglio corto ai lati e più lungo sopra.",
                            "english": "Good morning. I would like a short cut on the sides and longer on top.",
                            "isCorrect": True,
                            "feedback": "Perfect. Very clear instructions for the style."
                        },
                        {
                            "text": "Buongiorno. Vorrei un menu fisso per pranzo.",
                            "english": "Good morning. I would like a set menu for lunch.",
                            "isCorrect": False,
                            "feedback": "You are not at a restaurant!"
                        },
                        {
                            "text": "Ciao! Mi piacciono molto i tuoi capelli oggi.",
                            "english": "Hi! I like your hair very much today.",
                            "isCorrect": False,
                            "feedback": "A nice compliment, but you need to say what YOU want."
                        }
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Ho capito. E dietro? Facciamo una spuntatina o tagliamo di più?",
                    "english": "I understand. And the back? Should we do a trim or cut more?",
                    "choices": [
                        {
                            "text": "Solo una spuntatina dietro, non troppo corto per favore.",
                            "english": "Just a trim in the back, not too short please.",
                            "isCorrect": True,
                            "feedback": "Good. Using 'spuntatina' correctly for a trim."
                        },
                        {
                            "text": "Vorrei un biglietto per il retro del treno.",
                            "english": "I would like a ticket for the back of the train.",
                            "isCorrect": False,
                            "feedback": "Nonsense. This is a haircut!"
                        },
                        {
                            "text": "Tagliamo tutto, voglio essere calvo da domani.",
                            "english": "Let's cut everything, I want to be bald from tomorrow.",
                            "isCorrect": False,
                            "feedback": "The host asked if you want a trim or more, but this is extreme!"
                        }
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Va bene. Usiamo le forbici o preferisce la macchinetta?",
                    "english": "Alright. Shall we use scissors or do you prefer the clipper?",
                    "choices": [
                        {
                            "text": "Preferisco le forbici, il taglio sembra più naturale.",
                            "english": "I prefer scissors, the cut looks more natural.",
                            "isCorrect": True,
                            "feedback": "Excellent choice and reasoning."
                        },
                        {
                            "text": "Usi pure il rasoio per la mia barba lunga.",
                            "english": "Go ahead and use the razor for my long beard.",
                            "isCorrect": False,
                            "feedback": "They are talking about your hair style right now."
                        },
                        {
                            "text": "Non mi piacciono le macchine veloci e rosse.",
                            "english": "I don't like fast and red cars.",
                            "isCorrect": False,
                            "feedback": "The host means the hair clipper, not cars!"
                        }
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "D'accordo. Vuole anche lavare i capelli prima di iniziare?",
                    "english": "Agreed. Do you also want to wash your hair before starting?",
                    "choices": [
                        {
                            "text": "Sì, grazie. Preferisco lavarli prima del taglio.",
                            "english": "Yes, thanks. I prefer to wash them before the cut.",
                            "isCorrect": True,
                            "feedback": "Good choice for a clean cut."
                        },
                        {
                            "text": "No, ho già mangiato molta pasta, grazie.",
                            "english": "No, I already ate a lot of pasta, thanks.",
                            "isCorrect": False,
                            "feedback": "Washing hair, not eating!"
                        },
                        {
                            "text": "Sì, lavo io il pavimento di questo negozio.",
                            "english": "Yes, I'll wash the floor of this shop myself.",
                            "isCorrect": False,
                            "feedback": "You are the customer, not the cleaner!"
                        }
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Perfetto. Venga pure al lavatesta. L'acqua va bene così?",
                    "english": "Perfect. Come to the wash station. Is the water okay like this?",
                    "choices": [
                        {
                            "text": "Sì, la temperatura dell'acqua è perfetta, grazie.",
                            "english": "Yes, the water temperature is perfect, thanks.",
                            "isCorrect": True,
                            "feedback": "Good confirmation of comfort."
                        },
                        {
                            "text": "No, l'acqua del mare è troppo salata oggi.",
                            "english": "No, the sea water is too salty today.",
                            "isCorrect": False,
                            "feedback": "This isn't the sea or soup!"
                        },
                        {
                            "text": "Voglio l'acqua frizzante da bere subito.",
                            "english": "I want sparkling water to drink right now.",
                            "isCorrect": False,
                            "feedback": "You aren't drinking it!"
                        }
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Bene. Come preferisce le basette? Lunghe o corte?",
                    "english": "Good. How do you prefer the sideburns? Long or short?",
                    "choices": [
                        {
                            "text": "Le vorrei corte e sfumate, per favore.",
                            "english": "I would like them short and faded, please.",
                            "isCorrect": True,
                            "feedback": "Good technical detail."
                        },
                        {
                            "text": "Voglio le basette blu come il mare.",
                            "english": "I want blue sideburns like the sea.",
                            "isCorrect": False,
                            "feedback": "That's a very unusual request for sideburns!"
                        },
                        {
                            "text": "Mi piacciono le basi della cucina.",
                            "english": "I like the basics of cooking.",
                            "isCorrect": False,
                            "feedback": "Basette means sideburns, not cooking basics!"
                        }
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "D'accordo. E per la frangia? La lasciamo lunga?",
                    "english": "Agreed. And for the fringe? Should we leave it long?",
                    "choices": [
                        {
                            "text": "No, la tagli pure un po' sopra le sopracciglia.",
                            "english": "No, cut it a bit above the eyebrows.",
                            "isCorrect": True,
                            "feedback": "Clear instruction for the fringe."
                        },
                        {
                            "text": "Sì, mi piace la Francia in estate.",
                            "english": "Yes, I like France in the summer.",
                            "isCorrect": False,
                            "feedback": "Frangia is fringe, not the country France!"
                        },
                        {
                            "text": "Voglio una frangia di fiori rossi.",
                            "english": "I want a fringe of red flowers.",
                            "isCorrect": False,
                            "feedback": "Hair, not flowers!"
                        }
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Capito. Ha dei capelli molto folti. Usa prodotti particolari?",
                    "english": "Understood. You have very thick hair. Do you use particular products?",
                    "choices": [
                        {
                            "text": "Uso solo uno shampoo neutro ogni due giorni.",
                            "english": "I only use a neutral shampoo every two days.",
                            "isCorrect": True,
                            "feedback": "Simple and direct answer."
                        },
                        {
                            "text": "Uso la marmellata per i miei capelli.",
                            "english": "I use jam for my hair.",
                            "isCorrect": False,
                            "feedback": "Jam is for bread, not hair!"
                        },
                        {
                            "text": "Sì, uso molti prodotti per pulire la casa.",
                            "english": "Yes, I use many products to clean the house.",
                            "isCorrect": False,
                            "feedback": "The host is asking about hair products."
                        }
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Le consiglio un balsamo per renderli più morbidi.",
                    "english": "I recommend a conditioner to make them softer.",
                    "choices": [
                        {
                            "text": "Grazie del consiglio, lo proverò sicuramente.",
                            "english": "Thanks for the advice, I will definitely try it.",
                            "isCorrect": True,
                            "feedback": "Accepting professional advice."
                        },
                        {
                            "text": "No, il balsamo è per le labbra secche.",
                            "english": "No, lip balm is for dry lips.",
                            "isCorrect": False,
                            "feedback": "Balsamo in Italian means conditioner for hair too."
                        },
                        {
                            "text": "Voglio un balsamo che sa di pizza calda.",
                            "english": "I want a conditioner that tastes like hot pizza.",
                            "isCorrect": False,
                            "feedback": "Conditioner is not for eating!"
                        }
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Prego. Allora iniziamo con il taglio. Si rilassi pure.",
                    "english": "You're welcome. Then let's start with the cut. Just relax.",
                    "choices": [
                        {
                            "text": "Va bene, sono pronto. Grazie mille.",
                            "english": "Alright, I'm ready. Thanks a lot.",
                            "isCorrect": True,
                            "feedback": "Ready to start."
                        },
                        {
                            "text": "No, non voglio rilassarmi, voglio correre.",
                            "english": "No, I don't want to relax, I want to run.",
                            "isCorrect": False,
                            "feedback": "Stay still during a haircut!"
                        },
                        {
                            "text": "Sì, mi rilasso guardando la televisione.",
                            "english": "Yes, I relax by watching television.",
                            "isCorrect": False,
                            "feedback": "Just relax in the chair for now."
                        }
                    ]
                }
            ]
        },
        {
            "id": "during_the_cut",
            "title": "During the Cut",
            "description": "Interact with the hairdresser while they are working on your hair.",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Tutto bene? Le piace come sta venendo il taglio?",
                    "english": "Everything okay? Do you like how the cut is coming along?",
                    "choices": [
                        {
                            "text": "Sì, mi piace molto. Non tagli troppo sopra, però.",
                            "english": "Yes, I like it a lot. Don't cut too much on top, though.",
                            "isCorrect": True,
                            "feedback": "Good feedback. It's important to speak up during the cut."
                        },
                        {
                            "text": "Sì, il film al cinema è molto bello oggi.",
                            "english": "Yes, the movie at the cinema is very beautiful today.",
                            "isCorrect": False,
                            "feedback": "Focus! You are getting a haircut."
                        },
                        {
                            "text": "No, non mi piace affatto il barbiere qui.",
                            "english": "No, I don't like the barber here at all.",
                            "isCorrect": False,
                            "feedback": "Too direct and potentially rude!"
                        }
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Non si preoccupi, lascerò la lunghezza giusta. Vuole scalare i capelli?",
                    "english": "Don't worry, I'll leave the right length. Do you want to layer the hair?",
                    "choices": [
                        {
                            "text": "Sì, li scali pure un po' per dare volume.",
                            "english": "Yes, layer them a bit to give volume.",
                            "isCorrect": True,
                            "feedback": "Great. Using 'scalare' (to layer) correctly."
                        },
                        {
                            "text": "No, non voglio scalare la montagna alta.",
                            "english": "No, I don't want to climb the high mountain.",
                            "isCorrect": False,
                            "feedback": "Wrong kind of 'scalare'! Here it means layering hair."
                        },
                        {
                            "text": "Voglio i capelli blu come il cielo oggi.",
                            "english": "I want blue hair like the sky today.",
                            "isCorrect": False,
                            "feedback": "That's about color, not layering."
                        }
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Ottima idea. Ora uso un po' di gel o preferisce la lacca?",
                    "english": "Great idea. Now I'll use a bit of gel or do you prefer hairspray?",
                    "choices": [
                        {
                            "text": "Preferisco un po' di gel, ma non troppo.",
                            "english": "I prefer a bit of gel, but not too much.",
                            "isCorrect": True,
                            "feedback": "Clear preference for styling products."
                        },
                        {
                            "text": "Preferisco molto il latte nel caffè caldo.",
                            "english": "I prefer milk in hot coffee very much.",
                            "isCorrect": False,
                            "feedback": "You are still at the hairdresser!"
                        },
                        {
                            "text": "Usi pure la colla per carta sul mio viso.",
                            "english": "Go ahead and use paper glue on my face.",
                            "isCorrect": False,
                            "feedback": "Ouch! Don't use glue on hair or face."
                        }
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Ecco fatto. Guardi pure nello specchio dietro. Le piace?",
                    "english": "All done. Have a look in the back mirror. Do you like it?",
                    "choices": [
                        {
                            "text": "Sì, è perfetto! Proprio come lo volevo. Grazie.",
                            "english": "Yes, it's perfect! Just how I wanted it. Thanks.",
                            "isCorrect": True,
                            "feedback": "Positive reinforcement is always appreciated."
                        },
                        {
                            "text": "No, lo specchio è rotto in mille pezzi.",
                            "english": "No, the mirror is broken into a thousand pieces.",
                            "isCorrect": False,
                            "feedback": "Don't be negative unless it's actually broken."
                        },
                        {
                            "text": "Chi è quella persona brutta nello specchio?",
                            "english": "Who is that ugly person in the mirror?",
                            "isCorrect": False,
                            "feedback": "That person in the mirror is you!"
                        }
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Mi fa piacere. Allora togliamo la mantellina e abbiamo finito.",
                    "english": "I'm glad. Let's take off the cape then and we're finished.",
                    "choices": [
                        {
                            "text": "Grazie mille. Dove posso pagare il conto?",
                            "english": "Thanks a lot. Where can I pay the bill?",
                            "isCorrect": True,
                            "feedback": "Good transition to the payment phase."
                        },
                        {
                            "text": "Voglio un'altra mantellina rossa per me.",
                            "english": "I want another red cape for myself.",
                            "isCorrect": False,
                            "feedback": "Why? You are done!"
                        },
                        {
                            "text": "Dov'è il mio bagaglio per il viaggio?",
                            "english": "Where is my luggage for the trip?",
                            "isCorrect": False,
                            "feedback": "You didn't bring luggage to the salon."
                        }
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Può pagare alla cassa. Vuole comprare il gel che ho usato?",
                    "english": "You can pay at the counter. Do you want to buy the gel I used?",
                    "choices": [
                        {
                            "text": "Sì, mi piace molto l'effetto. Quanto costa?",
                            "english": "Yes, I like the effect very much. How much does it cost?",
                            "isCorrect": True,
                            "feedback": "Good interest in professional products."
                        },
                        {
                            "text": "No, il gel è per i capelli dei miei amici.",
                            "english": "No, the gel is for my friends' hair.",
                            "isCorrect": False,
                            "feedback": "The host is asking if YOU want to buy it."
                        },
                        {
                            "text": "Sì, voglio comprare una gelateria intera.",
                            "english": "Yes, I want to buy an entire ice cream shop.",
                            "isCorrect": False,
                            "feedback": "Gelato is ice cream, gel is hair product!"
                        }
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "Costa dieci euro. Abbiamo anche una tessera fedeltà.",
                    "english": "It costs ten euros. We also have a loyalty card.",
                    "choices": [
                        {
                            "text": "Interessante. Come funziona questa tessera?",
                            "english": "Interesting. How does this card work?",
                            "isCorrect": True,
                            "feedback": "Asking for more information."
                        },
                        {
                            "text": "Ho già una tessera per la biblioteca locale.",
                            "english": "I already have a card for the local library.",
                            "isCorrect": False,
                            "feedback": "The host is talking about the salon's loyalty card."
                        },
                        {
                            "text": "La fedeltà è molto importante nel matrimonio.",
                            "english": "Loyalty is very important in marriage.",
                            "isCorrect": False,
                            "feedback": "Stay focused on the shop's loyalty program!"
                        }
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Dopo dieci tagli, l'undicesimo è in omaggio.",
                    "english": "After ten cuts, the eleventh one is free.",
                    "choices": [
                        {
                            "text": "Bellissimo! Allora la prendo volentieri.",
                            "english": "Beautiful! Then I'll gladly take it.",
                            "isCorrect": True,
                            "feedback": "Accepting the loyalty card."
                        },
                        {
                            "text": "Dieci tagli sono troppi per i miei capelli.",
                            "english": "Ten cuts are too many for my hair.",
                            "isCorrect": False,
                            "feedback": "It's a cumulative offer over time."
                        },
                        {
                            "text": "Voglio undici pizze in omaggio subito.",
                            "english": "I want eleven free pizzas right now.",
                            "isCorrect": False,
                            "feedback": "Still not a pizzeria!"
                        }
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Ottimo. Le sta davvero bene questo nuovo look.",
                    "english": "Great. This new look really suits you.",
                    "choices": [
                        {
                            "text": "Grazie mille, mi sento molto meglio ora.",
                            "english": "Thanks a lot, I feel much better now.",
                            "isCorrect": True,
                            "feedback": "Expressing satisfaction."
                        },
                        {
                            "text": "No, il mio look è sempre lo stesso da anni.",
                            "english": "No, my look has always been the same for years.",
                            "isCorrect": False,
                            "feedback": "The host was giving you a compliment."
                        },
                        {
                            "text": "Guardo sempre il look dei famosi online.",
                            "english": "I always look at famous people's looks online.",
                            "isCorrect": False,
                            "feedback": "Irrelevant comment about celebrities."
                        }
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Mi fa piacere. Venga pure con me verso la cassa.",
                    "english": "I'm glad. Come with me towards the counter.",
                    "choices": [
                        {
                            "text": "Certamente, la seguo subito alla cassa.",
                            "english": "Certainly, I'll follow you to the counter right away.",
                            "isCorrect": True,
                            "feedback": "Ready to pay."
                        },
                        {
                            "text": "No, voglio restare qui sulla sedia comoda.",
                            "english": "No, I want to stay here on the comfortable chair.",
                            "isCorrect": False,
                            "feedback": "You need to go and pay for the service."
                        },
                        {
                            "text": "La cassa è piena di soldi veri?",
                            "english": "Is the register full of real money?",
                            "isCorrect": False,
                            "feedback": "What a strange and suspicious question!"
                        }
                    ]
                }
            ]
        },
        {
            "id": "payment_and_tip",
            "title": "Payment & Tip",
            "description": "Pay for your haircut and leave a tip for the great service.",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Spero che sia soddisfatto. In totale sono venticinque euro.",
                    "english": "I hope you are satisfied. In total it's twenty-five euros.",
                    "choices": [
                        {
                            "text": "Sì, molto soddisfatto. Posso pagare con la carta?",
                            "english": "Yes, very satisfied. Can I pay with card?",
                            "isCorrect": True,
                            "feedback": "Polite and asking for payment method."
                        },
                        {
                            "text": "È troppo caro, non voglio pagare niente.",
                            "english": "It's too expensive, I don't want to pay anything.",
                            "isCorrect": False,
                            "feedback": "That's not very nice!"
                        },
                        {
                            "text": "Vorrei un tavolo per due persone, grazie.",
                            "english": "I would like a table for two people, thanks.",
                            "isCorrect": False,
                            "feedback": "Again, not a restaurant!"
                        }
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Certamente, accettiamo tutte le carte. Ecco a lei.",
                    "english": "Certainly, we accept all cards. Here you go.",
                    "choices": [
                        {
                            "text": "Ecco fatto. Vorrei lasciare anche una piccola mancia.",
                            "english": "There we go. I would also like to leave a small tip.",
                            "isCorrect": True,
                            "feedback": "Very kind! Tips are appreciated for good service."
                        },
                        {
                            "text": "Ecco la mia carta d'identità originale.",
                            "english": "Here is my original identity card.",
                            "isCorrect": False,
                            "feedback": "They need your payment card, not ID!"
                        },
                        {
                            "text": "Non ho soldi, arrivederci e grazie mille.",
                            "english": "I have no money, goodbye and thanks a lot.",
                            "isCorrect": False,
                            "feedback": "You must pay for services!"
                        }
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Grazie mille, molto gentile! Le serve la ricevuta?",
                    "english": "Thank you very much, very kind! Do you need the receipt?",
                    "choices": [
                        {
                            "text": "Sì, grazie. Mi serve per il mio ufficio.",
                            "english": "Yes, thanks. I need it for my office.",
                            "isCorrect": True,
                            "feedback": "Perfectly normal request."
                        },
                        {
                            "text": "No, voglio un biglietto aereo per Londra.",
                            "english": "No, I want a plane ticket for London.",
                            "isCorrect": False,
                            "feedback": "Still no planes!"
                        },
                        {
                            "text": "Sì, vorrei la ricetta medica del dottore.",
                            "english": "Yes, I would like the doctor's medical prescription.",
                            "isCorrect": False,
                            "feedback": "You need a receipt, not a medical prescription."
                        }
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Ecco la ricevuta. Grazie ancora e arrivederci!",
                    "english": "Here is the receipt. Thank you again and goodbye!",
                    "choices": [
                        {
                            "text": "Grazie a lei, arrivederci e buona giornata!",
                            "english": "Thanks to you, goodbye and have a good day!",
                            "isCorrect": True,
                            "feedback": "Polite and standard closing."
                        },
                        {
                            "text": "Ciao, ci vediamo al cinema stasera.",
                            "english": "Hi, see you at the cinema tonight.",
                            "isCorrect": False,
                            "feedback": "Maybe, but just say goodbye for now."
                        },
                        {
                            "text": "A presto al gate imbarco dell'aeroporto.",
                            "english": "See you soon at the airport boarding gate.",
                            "isCorrect": False,
                            "feedback": "Enough with the airport!"
                        }
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Spero di rivederla presto. Come ci ha trovati?",
                    "english": "I hope to see you again soon. How did you find us?",
                    "choices": [
                        {
                            "text": "Ho visto la vostra insegna camminando per strada.",
                            "english": "I saw your sign walking down the street.",
                            "isCorrect": True,
                            "feedback": "Providing feedback on their visibility."
                        },
                        {
                            "text": "Vi ho trovati in un bosco molto buio.",
                            "english": "I found you in a very dark forest.",
                            "isCorrect": False,
                            "feedback": "The salon is in the city, not a forest!"
                        },
                        {
                            "text": "Cercavo un gatto perso e sono entrato.",
                            "english": "I was looking for a lost cat and I came in.",
                            "isCorrect": False,
                            "feedback": "A bit of a strange way to find a hairdresser."
                        }
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Ottimo. Se porta un amico, avrà uno sconto speciale.",
                    "english": "Great. If you bring a friend, you will have a special discount.",
                    "choices": [
                        {
                            "text": "Davvero? Allora lo dirò sicuramente ai miei amici.",
                            "english": "Really? Then I will definitely tell my friends.",
                            "isCorrect": True,
                            "feedback": "Interested in the referral program."
                        },
                        {
                            "text": "Non ho amici, vivo da solo in una grotta.",
                            "english": "I have no friends, I live alone in a cave.",
                            "isCorrect": False,
                            "feedback": "That's a bit sad and probably not true!"
                        },
                        {
                            "text": "Sì, porto il mio amico elefante domani.",
                            "english": "Yes, I'll bring my elephant friend tomorrow.",
                            "isCorrect": False,
                            "feedback": "Elephants don't need haircuts at a salon!"
                        }
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "Ecco il mio biglietto da visita con il numero diretto.",
                    "english": "Here is my business card with the direct number.",
                    "choices": [
                        {
                            "text": "Grazie, lo metto subito nel mio portafoglio.",
                            "english": "Thanks, I'll put it in my wallet right away.",
                            "isCorrect": True,
                            "feedback": "Saving contact info."
                        },
                        {
                            "text": "Voglio un biglietto per il teatro stasera.",
                            "english": "I want a ticket for the theater tonight.",
                            "isCorrect": False,
                            "feedback": "Biglietto da visita means business card, not a theater ticket!"
                        },
                        {
                            "text": "Non mi piacciono i biglietti di carta piccola.",
                            "english": "I don't like small paper tickets.",
                            "isCorrect": False,
                            "feedback": "It's a business card, very useful for appointments."
                        }
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Siamo aperti dal lunedì al sabato, dalle nove alle otto.",
                    "english": "We are open from Monday to Saturday, from nine to eight.",
                    "choices": [
                        {
                            "text": "Bene, allora la prossima volta verrò di sabato.",
                            "english": "Good, then next time I'll come on Saturday.",
                            "isCorrect": True,
                            "feedback": "Planning future visits."
                        },
                        {
                            "text": "Aprite anche alle tre di notte per me?",
                            "english": "Do you also open at three in the morning for me?",
                            "isCorrect": False,
                            "feedback": "They have standard business hours."
                        },
                        {
                            "text": "Sì, preferisco i giorni in cui piove molto.",
                            "english": "Yes, I prefer the days when it rains a lot.",
                            "isCorrect": False,
                            "feedback": "The host is giving you their opening hours."
                        }
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Perfetto. Vuole iscriversi alla nostra newsletter?",
                    "english": "Perfect. Do you want to sign up for our newsletter?",
                    "choices": [
                        {
                            "text": "No grazie, ricevo già troppe email ogni giorno.",
                            "english": "No thanks, I already receive too many emails every day.",
                            "isCorrect": True,
                            "feedback": "Polite refusal."
                        },
                        {
                            "text": "Sì, voglio leggere le notizie del mondo.",
                            "english": "Yes, I want to read world news.",
                            "isCorrect": False,
                            "feedback": "A salon newsletter is about offers and hair, not world news."
                        },
                        {
                            "text": "Sì, mi piace molto scrivere lettere lunghe.",
                            "english": "Yes, I like writing long letters very much.",
                            "isCorrect": False,
                            "feedback": "A newsletter is something you receive, not write."
                        }
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Capisco perfettamente. Arrivederci allora, a presto!",
                    "english": "I perfectly understand. Goodbye then, see you soon!",
                    "choices": [
                        {
                            "text": "Arrivederci e grazie ancora di tutto! A presto.",
                            "english": "Goodbye and thanks again for everything! See you soon.",
                            "isCorrect": True,
                            "feedback": "Final polite goodbye."
                        },
                        {
                            "text": "Sì, ci vediamo tra dieci anni esatti.",
                            "english": "Yes, see you in exactly ten years.",
                            "isCorrect": False,
                            "feedback": "Hopefully you'll need a haircut sooner than that!"
                        },
                        {
                            "text": "Voglio restare qui a dormire ora.",
                            "english": "I want to stay here to sleep now.",
                            "isCorrect": False,
                            "feedback": "This is a salon, not a hotel!"
                        }
                    ]
                }
            ]
        }
    ]
}

with open('./src/data/exports/daily_life/haircut/conversations.json', 'w') as f:
    json.dump(scenario, f, indent=2, ensure_ascii=False)
