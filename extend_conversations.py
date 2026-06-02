import json
import os

file_path = 'src/data/exports/culture/festival/conversations.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

extensions = {
    "festival_welcome": [
        {
            "id": "m6",
            "role": "host",
            "text": "Aspetti! Vuole una mappa dell'evento? È molto utile.",
            "english": "Wait! Do you want a map of the event? It's very useful.",
            "choices": [
                {
                    "text": "Sì, grazie. Mi serve proprio una mappa.",
                    "english": "Yes, thanks. I really need a map.",
                    "isCorrect": True,
                    "feedback": "Great! Maps are always helpful for tourists."
                },
                {
                    "text": "No, non mi piacciono le mappe.",
                    "english": "No, I don't like maps.",
                    "isCorrect": False,
                    "feedback": "You might get lost without a map!"
                },
                {
                    "text": "Dove posso comprare un biglietto aereo?",
                    "english": "Where can I buy a plane ticket?",
                    "isCorrect": False,
                    "feedback": "Wrong domain! You're at a festival, not an airport."
                }
            ]
        },
        {
            "id": "m7",
            "role": "host",
            "text": "Eccola. La mappa mostra dove passa la sfilata storica.",
            "english": "Here it is. The map shows where the historical parade passes.",
            "choices": [
                {
                    "text": "Perfetto, grazie. A che ora passa la sfilata?",
                    "english": "Perfect, thanks. What time does the parade pass?",
                    "isCorrect": True,
                    "feedback": "Asking about the schedule is a good next step."
                },
                {
                    "text": "Non mi interessa la sfilata.",
                    "english": "I'm not interested in the parade.",
                    "isCorrect": False,
                    "feedback": "The parade is the highlight of the festival!"
                },
                {
                    "text": "Voglio prenotare un tavolo al ristorante.",
                    "english": "I want to book a table at the restaurant.",
                    "isCorrect": False,
                    "feedback": "You're in a square, not at a restaurant."
                }
            ]
        },
        {
            "id": "m8",
            "role": "host",
            "text": "La sfilata è la parte più importante. Le piacciono le tradizioni?",
            "english": "The parade is the most important part. Do you like traditions?",
            "choices": [
                {
                    "text": "Sì, molto. Mi piace scoprire la cultura locale.",
                    "english": "Yes, very much. I like discovering local culture.",
                    "isCorrect": True,
                    "feedback": "Showing interest in local traditions is great for learning."
                },
                {
                    "text": "No, preferisco guardare la televisione.",
                    "english": "No, I prefer watching television.",
                    "isCorrect": False,
                    "feedback": "That's a bit boring for a festival attendee!"
                },
                {
                    "text": "Dov'è la chiave della mia camera?",
                    "english": "Where is the key to my room?",
                    "isCorrect": False,
                    "feedback": "Wrong scenario! You are at a festival, not an apartment."
                }
            ]
        },
        {
            "id": "m9",
            "role": "host",
            "text": "Allora le consiglio di andare in piazza presto per vedere bene.",
            "english": "Then I recommend you go to the square early to see well.",
            "choices": [
                {
                    "text": "Grazie del consiglio. Ci vado subito.",
                    "english": "Thanks for the advice. I'm going there right away.",
                    "isCorrect": True,
                    "feedback": "Good plan! The square fills up quickly."
                },
                {
                    "text": "No, preferisco restare qui a sedermi.",
                    "english": "No, I prefer to stay here and sit down.",
                    "isCorrect": False,
                    "feedback": "You'll miss the best view if you stay here!"
                },
                {
                    "text": "Quanto costa l'affitto dell'appartamento?",
                    "english": "How much is the rent for the apartment?",
                    "isCorrect": False,
                    "feedback": "Wrong scenario! You are at a festival, not an apartment."
                }
            ]
        },
        {
            "id": "m10",
            "role": "host",
            "text": "Spero che passi una bella serata. Ci vediamo in giro!",
            "english": "I hope you have a nice evening. See you around!",
            "choices": [
                {
                    "text": "Grazie mille! Buona serata anche a lei.",
                    "english": "Thanks a lot! Have a good evening too.",
                    "isCorrect": True,
                    "feedback": "A polite and friendly way to end the conversation."
                },
                {
                    "text": "Arrivederci. Vado via adesso.",
                    "english": "Goodbye. I'm leaving now.",
                    "isCorrect": False,
                    "feedback": "A bit abrupt for a nice chat."
                },
                {
                    "text": "Dov'è la fermata dell'autobus per Roma?",
                    "english": "Where is the bus stop for Rome?",
                    "isCorrect": False,
                    "feedback": "You're at a festival, the bus stop is far from here!"
                }
            ]
        }
    ],
    "food_stall": [
        {
            "id": "m6",
            "role": "host",
            "text": "Aspetti, vuole anche qualcosa da bere? Abbiamo vino locale.",
            "english": "Wait, do you also want something to drink? We have local wine.",
            "choices": [
                {
                    "text": "Sì, volentieri. Un bicchiere di vino rosso, grazie.",
                    "english": "Yes, gladly. A glass of red wine, thanks.",
                    "isCorrect": True,
                    "feedback": "Perfect! Red wine pairs well with truffle pasta."
                },
                {
                    "text": "No, non bevo mai vino.",
                    "english": "No, I never drink wine.",
                    "isCorrect": False,
                    "feedback": "Water or soda is also available, but wine is the specialty!"
                },
                {
                    "text": "Cerco l'ufficio informazioni turistiche.",
                    "english": "I'm looking for the tourist information office.",
                    "isCorrect": False,
                    "feedback": "You're at a food stall, not an information desk."
                }
            ]
        },
        {
            "id": "m7",
            "role": "host",
            "text": "È un vino rosso delle nostre colline. Ne vuole un bicchiere?",
            "english": "It's a red wine from our hills. Do you want a glass?",
            "choices": [
                {
                    "text": "Sì, sembra ottimo. Quanto costa?",
                    "english": "Yes, it sounds great. How much does it cost?",
                    "isCorrect": True,
                    "feedback": "Good to check the price of drinks too."
                },
                {
                    "text": "No, preferisco una birra fredda.",
                    "english": "No, I prefer a cold beer.",
                    "isCorrect": False,
                    "feedback": "We only have wine and water here."
                },
                {
                    "text": "Vorrei un asciugamano per la doccia.",
                    "english": "I would like a towel for the shower.",
                    "isCorrect": False,
                    "feedback": "Wrong place for bathroom supplies!"
                }
            ]
        },
        {
            "id": "m8",
            "role": "host",
            "text": "Costa tre euro. Il vino è perfetto con il tartufo.",
            "english": "It costs three euros. The wine is perfect with the truffle.",
            "choices": [
                {
                    "text": "Va bene, ecco tre euro. Grazie.",
                    "english": "Okay, here are three euros. Thanks.",
                    "isCorrect": True,
                    "feedback": "A fair price for local wine."
                },
                {
                    "text": "È troppo caro per un bicchiere.",
                    "english": "It's too expensive for a glass.",
                    "isCorrect": False,
                    "feedback": "Actually, it's a very good price for artisanal wine."
                },
                {
                    "text": "Il mio passaporto è scaduto oggi.",
                    "english": "My passport expired today.",
                    "isCorrect": False,
                    "feedback": "What does that have to do with wine?"
                }
            ]
        },
        {
            "id": "m9",
            "role": "host",
            "text": "Vuole un tovagliolo o del pane con la pasta?",
            "english": "Do you want a napkin or some bread with the pasta?",
            "choices": [
                {
                    "text": "Sì, un tovagliolo, per favore.",
                    "english": "Yes, a napkin, please.",
                    "isCorrect": True,
                    "feedback": "Napkins are always useful when eating pasta."
                },
                {
                    "text": "No, non mangio mai il pane.",
                    "english": "No, I never eat bread.",
                    "isCorrect": False,
                    "feedback": "In Italy, bread is usually served with everything!"
                },
                {
                    "text": "Dove posso noleggiare una bicicletta?",
                    "english": "Where can I rent a bike?",
                    "isCorrect": False,
                    "feedback": "You're at a food stall, not a bike rental shop."
                }
            ]
        },
        {
            "id": "m10",
            "role": "host",
            "text": "Buon appetito! Mi faccia sapere se serve altro.",
            "english": "Enjoy your meal! Let me know if you need anything else.",
            "choices": [
                {
                    "text": "Grazie di tutto! La pasta è deliziosa.",
                    "english": "Thanks for everything! The pasta is delicious.",
                    "isCorrect": True,
                    "feedback": "A great way to finish the interaction."
                },
                {
                    "text": "Arrivederci, ho finito di mangiare.",
                    "english": "Goodbye, I've finished eating.",
                    "isCorrect": False,
                    "feedback": "A bit too quick! Enjoy the moment."
                },
                {
                    "text": "A che ora parte il mio volo?",
                    "english": "What time does my flight leave?",
                    "isCorrect": False,
                    "feedback": "No flights at the sagra!"
                }
            ]
        }
    ],
    "parade_info": [
        {
            "id": "m6",
            "role": "host",
            "text": "La sfilata include molti cavalli e sbandieratori. È molto rumorosa!",
            "english": "The parade includes many horses and flag-wavers. It's very loud!",
            "choices": [
                {
                    "text": "Che bello! Mi piacciono molto i cavalli.",
                    "english": "How nice! I like horses very much.",
                    "isCorrect": True,
                    "feedback": "Horses are a traditional part of many Italian parades."
                },
                {
                    "text": "Troppo rumore! Non mi piace.",
                    "english": "Too much noise! I don't like it.",
                    "isCorrect": False,
                    "feedback": "Festivals are often loud and lively!"
                },
                {
                    "text": "Ho bisogno di una medicina per lo stomaco.",
                    "english": "I need a medicine for my stomach.",
                    "isCorrect": False,
                    "feedback": "Wrong topic! We're talking about the parade."
                }
            ]
        },
        {
            "id": "m7",
            "role": "host",
            "text": "Ha una macchina fotografica? Dovrebbe fare delle foto ai costumi.",
            "english": "Do you have a camera? You should take some photos of the costumes.",
            "choices": [
                {
                    "text": "Sì, la prendo subito. I costumi sono bellissimi.",
                    "english": "Yes, I'll get it right away. The costumes are beautiful.",
                    "isCorrect": True,
                    "feedback": "The costumes are very photogenic."
                },
                {
                    "text": "No, non mi piace fare foto.",
                    "english": "No, I don't like taking photos.",
                    "isCorrect": False,
                    "feedback": "You'll miss out on great memories!"
                },
                {
                    "text": "Dov'è la lavanderia più vicina?",
                    "english": "Where is the nearest laundry?",
                    "isCorrect": False,
                    "feedback": "We are outside, far from any laundry."
                }
            ]
        },
        {
            "id": "m8",
            "role": "host",
            "text": "I costumi sono fatti a mano dalle donne del paese. Sono molto antichi.",
            "english": "The costumes are handmade by the women of the village. They are very old.",
            "choices": [
                {
                    "text": "Incredibile! È una tradizione meravigliosa.",
                    "english": "Incredible! It's a wonderful tradition.",
                    "isCorrect": True,
                    "feedback": "Local craftsmanship is highly valued in Italy."
                },
                {
                    "text": "Non mi interessano i vestiti vecchi.",
                    "english": "I'm not interested in old clothes.",
                    "isCorrect": False,
                    "feedback": "These are historical costumes, not just old clothes!"
                },
                {
                    "text": "Quanto costa un biglietto per il museo?",
                    "english": "How much is a ticket for the museum?",
                    "isCorrect": False,
                    "feedback": "The parade is on the street, not in a museum."
                }
            ]
        },
        {
            "id": "m9",
            "role": "host",
            "text": "Dopo la sfilata, ci sono anche i fuochi d'artificio.",
            "english": "After the parade, there are also fireworks.",
            "choices": [
                {
                    "text": "Fantastico! A che ora iniziano i fuochi?",
                    "english": "Fantastic! What time do the fireworks start?",
                    "isCorrect": True,
                    "feedback": "Fireworks are the perfect way to end a festival."
                },
                {
                    "text": "Ho paura dei fuochi d'artificio.",
                    "english": "I'm afraid of fireworks.",
                    "isCorrect": False,
                    "feedback": "They are quite far away, so it's safe!"
                },
                {
                    "text": "Vorrei un cappuccino e un cornetto.",
                    "english": "I would like a cappuccino and a croissant.",
                    "isCorrect": False,
                    "feedback": "It's late at night, too late for breakfast food!"
                }
            ]
        },
        {
            "id": "m10",
            "role": "host",
            "text": "Iniziano a mezzanotte. Sarà una serata bellissima!",
            "english": "They start at midnight. It will be a beautiful evening!",
            "choices": [
                {
                    "text": "Non vedo l'ora! Grazie per le informazioni.",
                    "english": "I can't wait! Thanks for the information.",
                    "isCorrect": True,
                    "feedback": "A great way to conclude the information exchange."
                },
                {
                    "text": "È troppo tardi per me. Vado a dormire.",
                    "english": "It's too late for me. I'm going to sleep.",
                    "isCorrect": False,
                    "feedback": "You'll miss the best part!"
                },
                {
                    "text": "Dov'è il binario per il treno?",
                    "english": "Where is the platform for the train?",
                    "isCorrect": False,
                    "feedback": "The station is far from the village center."
                }
            ]
        }
    ],
    "buying_crafts": [
        {
            "id": "m6",
            "role": "host",
            "text": "Se le interessa, abbiamo anche dei piccoli magneti dipinti a mano.",
            "english": "If you are interested, we also have small hand-painted magnets.",
            "choices": [
                {
                    "text": "Oh, sono carini! Posso vederli?",
                    "english": "Oh, they are cute! Can I see them?",
                    "isCorrect": True,
                    "feedback": "Magnets are great small souvenirs."
                },
                {
                    "text": "No, non mi servono i magneti.",
                    "english": "No, I don't need magnets.",
                    "isCorrect": False,
                    "feedback": "They are very small and don't take up space!"
                },
                {
                    "text": "Vorrei prenotare un tavolo per cena.",
                    "english": "I would like to book a table for dinner.",
                    "isCorrect": False,
                    "feedback": "You're at a craft stall, not a restaurant."
                }
            ]
        },
        {
            "id": "m7",
            "role": "host",
            "text": "Sono leggeri da portare in valigia. Ne vuole vedere uno?",
            "english": "They are light to carry in a suitcase. Do you want to see one?",
            "choices": [
                {
                    "text": "Sì, grazie. Questo con la chiesa è molto bello.",
                    "english": "Yes, thanks. This one with the church is very beautiful.",
                    "isCorrect": True,
                    "feedback": "A nice choice representing the village."
                },
                {
                    "text": "No, preferisco comprare una maglietta.",
                    "english": "No, I prefer to buy a t-shirt.",
                    "isCorrect": False,
                    "feedback": "We don't have t-shirts here, only ceramics and magnets."
                },
                {
                    "text": "C'è il wifi gratuito qui vicino?",
                    "english": "Is there free wifi nearby?",
                    "isCorrect": False,
                    "feedback": "Not at the craft market!"
                }
            ]
        },
        {
            "id": "m8",
            "role": "host",
            "text": "Ogni magnete rappresenta un angolo diverso del nostro borgo.",
            "english": "Each magnet represents a different corner of our village.",
            "choices": [
                {
                    "text": "È un'idea bellissima per un ricordo.",
                    "english": "It's a beautiful idea for a souvenir.",
                    "isCorrect": True,
                    "feedback": "Souvenirs help you remember your trip."
                },
                {
                    "text": "Preferisco i magneti delle grandi città.",
                    "english": "I prefer magnets from big cities.",
                    "isCorrect": False,
                    "feedback": "Small villages have more unique items!"
                },
                {
                    "text": "Ho perso le chiavi dell'appartamento.",
                    "english": "I lost the keys to the apartment.",
                    "isCorrect": False,
                    "feedback": "Wrong scenario! You are at a festival stall."
                }
            ]
        },
        {
            "id": "m9",
            "role": "host",
            "text": "Dato che ha comprato il vaso, le regalo un magnete!",
            "english": "Since you bought the vase, I'll give you a magnet as a gift!",
            "choices": [
                {
                    "text": "Davvero? Grazie mille, è molto gentile!",
                    "english": "Really? Thanks a lot, you're very kind!",
                    "isCorrect": True,
                    "feedback": "It's always nice to get a small gift."
                },
                {
                    "text": "Non lo voglio, grazie lo stesso.",
                    "english": "I don't want it, thanks anyway.",
                    "isCorrect": False,
                    "feedback": "It's free! Why not take it?"
                },
                {
                    "text": "Dove posso trovare un taxi per l'aeroporto?",
                    "english": "Where can I find a taxi for the airport?",
                    "isCorrect": False,
                    "feedback": "There are no taxis in the middle of the sagra."
                }
            ]
        },
        {
            "id": "m10",
            "role": "host",
            "text": "È un piccolo ricordo della sua visita. Grazie e arrivederci!",
            "english": "It's a small souvenir of your visit. Thank you and goodbye!",
            "choices": [
                {
                    "text": "Grazie ancora di tutto. Arrivederci!",
                    "english": "Thanks again for everything. Goodbye!",
                    "isCorrect": True,
                    "feedback": "A perfect ending to your shopping experience."
                },
                {
                    "text": "Va bene, me ne vado ora.",
                    "english": "Okay, I'm leaving now.",
                    "isCorrect": False,
                    "feedback": "A bit rude after receiving a gift!"
                },
                {
                    "text": "Quanto costa il check-out in hotel?",
                    "english": "How much is the check-out in the hotel?",
                    "isCorrect": False,
                    "feedback": "You're at a festival stall, not an hotel!"
                }
            ]
        }
    ]
}

for conversation in data['conversations']:
    conv_id = conversation['id']
    if conv_id in extensions:
        conversation['messages'].extend(extensions[conv_id])

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
