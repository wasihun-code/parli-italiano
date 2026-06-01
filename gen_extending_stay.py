import json
import os

scenario_slug = "accommodation/extending_stay"
base_path = f"src/data/exports/{scenario_slug}"
os.makedirs(base_path, exist_ok=True)

domain_data = {
  "allowed": [
    "prolungare", "soggiorno", "notte", "notti", "fermarmi", "camera", "disponibile", "prezzo",
    "costo", "cambiare", "stessa", "prenotazione", "domani", "giorno", "più", "ancora", "pagare",
    "carta", "contanti", "reception", "valigia", "bagagli", "spostare", "chiave", "rimanere",
    "partire", "partenza", "quando", "fino", "giovedì", "venerdì", "sabato", "domenica", "lunedi",
    "martedì", "mercoledì", "oggi", "ieri", "hotel", "albergo", "letto", "colazione", "inclusa",
    "aggiungere", "supplemento", "tassa", "sconto", "offerta", "libera", "occupata", "prenotata",
    "buongiorno", "buonasera", "grazie", "prego", "scusi", "scusa", "certo", "volentieri", "sì", "no",
    "vorrei", "posso", "dobbiamo", "devo", "può", "aiutarmi", "informazione", "sapere", "controllare",
    "vedo", "computer", "sistema", "fortunatamente", "purtroppo", "mi", "dispiace", "problema",
    "perfetto", "ottimo", "bene", "molto", "poco", "quanto", "quale", "dove", "chi", "come",
    "euro", "centinaio", "cinquanta", "sessanta", "settanta", "ottanta", "novanta", "cento",
    "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci"
  ],
  "forbidden": [
    "volo", "aeroporto", "treno", "stazione", "ristorante", "menu", "cameriere", "ospedale",
    "medico", "farmacia", "mare", "spiaggia", "ombrellone", "museo", "biglietto", "teatro"
  ]
}

conversations_data = {
  "scenarioId": 25,
  "conversations": [
    {
      "id": "extend_one_night",
      "title": "Extend for One Night",
      "description": "Ask the reception to extend your stay by one more night in the same room.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Buongiorno. Posso aiutarla?",
          "english": "Good morning. Can I help you?",
          "choices": [
            {
              "text": "Buongiorno, vorrei un'informazione.",
              "english": "Good morning, I would like some information.",
              "isCorrect": True
            },
            {
              "text": "Buongiorno, vorrei un caffè nero.",
              "isCorrect": False
            },
            {
              "text": "Buongiorno, la mia valigia è rotta.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Certamente, mi dica.",
          "english": "Certainly, tell me.",
          "choices": [
            {
              "text": "Vorrei prolungare il mio soggiorno.",
              "english": "I would like to extend my stay.",
              "isCorrect": True
            },
            {
              "text": "Vorrei lavare i miei vestiti.",
              "isCorrect": False
            },
            {
              "text": "Vorrei un taxi per il centro.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Va bene. Qual è il numero della sua camera?",
          "english": "Alright. What is your room number?",
          "choices": [
            {
              "text": "Sono nella camera duecentocinque.",
              "english": "I am in room two hundred and five.",
              "isCorrect": True
            },
            {
              "text": "Sono nel mio letto caldo.",
              "isCorrect": False
            },
            {
              "text": "Il mio numero di telefono è questo.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Camera duecentocinque, signor Rossi. Per quante notti in più?",
          "english": "Room two hundred and five, Mr. Rossi. For how many extra nights?",
          "choices": [
            {
              "text": "Solo per una notte in più, grazie.",
              "english": "Just for one more night, thanks.",
              "isCorrect": True
            },
            {
              "text": "Solo per un giorno di sole.",
              "isCorrect": False
            },
            {
              "text": "Per molte notti di pioggia.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Controllo il sistema. Un attimo per favore.",
          "english": "I'll check the system. One moment please.",
          "choices": [
            {
              "text": "Certo, aspetto qui senza fretta.",
              "english": "Sure, I'll wait here without rushing.",
              "isCorrect": True
            },
            {
              "text": "Certo, dormo qui sul divano.",
              "isCorrect": False
            },
            {
              "text": "No, vado via molto veloce.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Fortunatamente la camera è libera. Può rimanere lì.",
          "english": "Fortunately the room is free. You can stay there.",
          "choices": [
            {
              "text": "Perfetto, non devo spostare i bagagli.",
              "english": "Perfect, I don't have to move the luggage.",
              "isCorrect": True
            },
            {
              "text": "Perfetto, non devo lavare i capelli.",
              "isCorrect": False
            },
            {
              "text": "Ottimo, la porta è molto chiusa.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Esatto. Il costo è di ottanta euro per la notte.",
          "english": "Exactly. The cost is eighty euros for the night.",
          "choices": [
            {
              "text": "Va bene. La colazione è inclusa?",
              "english": "Alright. Is breakfast included?",
              "isCorrect": True
            },
            {
              "text": "Va bene. Il letto è molto duro?",
              "isCorrect": False
            },
            {
              "text": "Va bene. Dov'è il mio asciugamano?",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Sì, la colazione è inclusa nel prezzo.",
          "english": "Yes, breakfast is included in the price.",
          "choices": [
            {
              "text": "Molto bene. Devo pagare adesso?",
              "english": "Very well. Do I have to pay now?",
              "isCorrect": True
            },
            {
              "text": "Molto bene. Devo pulire adesso?",
              "isCorrect": False
            },
            {
              "text": "Benissimo. Voglio pagare ieri.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Può pagare domani al check-out, se preferisce.",
          "english": "You can pay tomorrow at check-out, if you prefer.",
          "choices": [
            {
              "text": "Sì, preferisco pagare domani mattina.",
              "english": "Yes, I prefer to pay tomorrow morning.",
              "isCorrect": True
            },
            {
              "text": "Sì, preferisco pagare con il gatto.",
              "isCorrect": False
            },
            {
              "text": "No, preferisco dormire tutto il tempo.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "D'accordo. Ho aggiornato la sua prenotazione.",
          "english": "Agreed. I have updated your reservation.",
          "choices": [
            {
              "text": "Grazie mille per l'aiuto. Buona giornata.",
              "english": "Thank you very much for the help. Have a good day.",
              "isCorrect": True,
              "nextMessageId": "END"
            },
            {
              "text": "Grazie mille, buon appetito.",
              "isCorrect": False
            },
            {
              "text": "Grazie, voglio una mela rossa.",
              "isCorrect": False
            }
          ]
        }
      ]
    },
    {
      "id": "change_room",
      "title": "Changing Rooms",
      "description": "Extend your stay but you have to move to a different room.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Buonasera, come posso aiutarla?",
          "english": "Good evening, how can I help you?",
          "choices": [
            {
              "text": "Buonasera, vorrei fermarmi una notte in più.",
              "english": "Good evening, I would like to stay one more night.",
              "isCorrect": True
            },
            {
              "text": "Buonasera, vorrei un piatto freddo.",
              "isCorrect": False
            },
            {
              "text": "Buonasera, cerco una maglia rossa.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Controllo la disponibilità. Qual è la sua camera?",
          "english": "I'll check availability. What is your room?",
          "choices": [
            {
              "text": "La mia camera è la trecentodieci.",
              "english": "My room is three hundred and ten.",
              "isCorrect": True
            },
            {
              "text": "La mia camera è in montagna.",
              "isCorrect": False
            },
            {
              "text": "La camera è molto pulita ora.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "La trecentodieci purtroppo è già prenotata per domani.",
          "english": "The three hundred and ten is unfortunately already booked for tomorrow.",
          "choices": [
            {
              "text": "Oh, capisco. Non avete altre camere?",
              "english": "Oh, I see. Do you have no other rooms?",
              "isCorrect": True
            },
            {
              "text": "Oh, capisco. Avete molto pane?",
              "isCorrect": False
            },
            {
              "text": "Bene. Vado in un altro paese.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Abbiamo una camera doppia libera al primo piano.",
          "english": "We have a free double room on the first floor.",
          "choices": [
            {
              "text": "Posso prendere quella camera allora?",
              "english": "Can I take that room then?",
              "isCorrect": True
            },
            {
              "text": "Posso mangiare quella camera allora?",
              "isCorrect": False
            },
            {
              "text": "No, il primo piano è lontano.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Sì, ma dovrà spostare i suoi bagagli.",
          "english": "Yes, but you will have to move your luggage.",
          "choices": [
            {
              "text": "Nessun problema. A che ora devo cambiare camera?",
              "english": "No problem. What time must I change room?",
              "isCorrect": True
            },
            {
              "text": "Nessun problema. A che ora devo cantare?",
              "isCorrect": False
            },
            {
              "text": "Il bagaglio è molto verde e blu.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Deve lasciare la stanza attuale entro le undici.",
          "english": "You must leave the current room by eleven.",
          "choices": [
            {
              "text": "Va bene, preparerò le valigie per le undici.",
              "english": "Alright, I'll prepare the suitcases for eleven.",
              "isCorrect": True
            },
            {
              "text": "Va bene, preparerò la pasta per le undici.",
              "isCorrect": False
            },
            {
              "text": "No, preferisco uscire alle otto di sera.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "La nuova camera sarà pronta alle quattordici.",
          "english": "The new room will be ready at fourteen.",
          "choices": [
            {
              "text": "Posso lasciare i bagagli in reception?",
              "english": "Can I leave the luggage at the reception?",
              "isCorrect": True
            },
            {
              "text": "Posso lasciare i bagagli nel parco?",
              "isCorrect": False
            },
            {
              "text": "Voglio dormire alle quattordici in strada.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Certamente, abbiamo un deposito bagagli qui dietro.",
          "english": "Certainly, we have a luggage storage back here.",
          "choices": [
            {
              "text": "Ottimo. Qual è il prezzo della nuova camera?",
              "english": "Great. What is the price of the new room?",
              "isCorrect": True
            },
            {
              "text": "Ottimo. Qual è il sapore del formaggio?",
              "isCorrect": False
            },
            {
              "text": "Bene, voglio vedere la mia auto.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Sono cento euro, essendo una camera doppia.",
          "english": "It's one hundred euros, being a double room.",
          "choices": [
            {
              "text": "D'accordo, pago con la mia carta di credito.",
              "english": "Agreed, I pay with my credit card.",
              "isCorrect": True
            },
            {
              "text": "D'accordo, pago con la mia bicicletta.",
              "isCorrect": False
            },
            {
              "text": "No, i soldi sono finiti ieri.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Grazie, ecco la ricevuta. A domani mattina.",
          "english": "Thank you, here is the receipt. See you tomorrow morning.",
          "choices": [
            {
              "text": "A domani, grazie per la disponibilità.",
              "english": "See you tomorrow, thanks for the availability.",
              "isCorrect": True,
              "nextMessageId": "END"
            },
            {
              "text": "A domani, grazie per il pane.",
              "isCorrect": False
            },
            {
              "text": "Sì, vado a dormire ora nel letto.",
              "isCorrect": False
            }
          ]
        }
      ]
    },
    {
      "id": "extend_weekend",
      "title": "Extending Through the Weekend",
      "description": "Extend the stay for two nights over the weekend, discussing the price change.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Salve, ben tornato. Ha bisogno di qualcosa?",
          "english": "Hello, welcome back. Do you need something?",
          "choices": [
            {
              "text": "Salve. Devo partire venerdì, ma vorrei restare.",
              "english": "Hello. I have to leave Friday, but I would like to stay.",
              "isCorrect": True
            },
            {
              "text": "Salve. Devo comprare un biglietto rosso.",
              "isCorrect": False
            },
            {
              "text": "Sì, ho bisogno di una sciarpa blu.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Vorrebbe estendere la prenotazione per il fine settimana?",
          "english": "Would you like to extend the reservation for the weekend?",
          "choices": [
            {
              "text": "Sì, esatto. Fino a domenica mattina, se possibile.",
              "english": "Yes, exactly. Until Sunday morning, if possible.",
              "isCorrect": True
            },
            {
              "text": "Sì, esatto. Fino a lunedì al mare.",
              "isCorrect": False
            },
            {
              "text": "No, parto ieri per la Francia.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Controllo la sua camera, la numero dodici.",
          "english": "I check your room, number twelve.",
          "choices": [
            {
              "text": "Sì, la camera dodici al piano terra.",
              "english": "Yes, room twelve on the ground floor.",
              "isCorrect": True
            },
            {
              "text": "Sì, la camera è molto sporca.",
              "isCorrect": False
            },
            {
              "text": "No, la camera dodici al sole.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "La camera dodici è libera per il fine settimana.",
          "english": "Room twelve is free for the weekend.",
          "choices": [
            {
              "text": "Che fortuna! Qual è il costo per due notti?",
              "english": "How lucky! What is the cost for two nights?",
              "isCorrect": True
            },
            {
              "text": "Che sfortuna! Qual è il sapore?",
              "isCorrect": False
            },
            {
              "text": "Ottimo, il costo per un vestito?",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Il fine settimana costa un po' di più, novanta euro a notte.",
          "english": "The weekend costs a little more, ninety euros per night.",
          "choices": [
            {
              "text": "Capisco. Va bene, centottanta euro in totale.",
              "english": "I understand. Alright, one hundred eighty euros in total.",
              "isCorrect": True
            },
            {
              "text": "Capisco. Va bene, venti euro in totale.",
              "isCorrect": False
            },
            {
              "text": "No, non voglio pagare il letto.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Esatto. Vuole confermare il prolungamento?",
          "english": "Exactly. Do you want to confirm the extension?",
          "choices": [
            {
              "text": "Sì, confermo. Ecco la mia carta per pagare.",
              "english": "Yes, I confirm. Here is my card to pay.",
              "isCorrect": True
            },
            {
              "text": "Sì, confermo. Ecco la mia borsa nera.",
              "isCorrect": False
            },
            {
              "text": "Non voglio confermare, preferisco scappare.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Grazie. Devo aggiornare la chiave magnetica.",
          "english": "Thanks. I have to update the magnetic key.",
          "choices": [
            {
              "text": "Ah certo. Ecco la chiave della camera.",
              "english": "Ah sure. Here is the room key.",
              "isCorrect": True
            },
            {
              "text": "Ah certo. Ecco la porta del bagno.",
              "isCorrect": False
            },
            {
              "text": "No, la chiave è persa per sempre.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Fatto. Ora la chiave funziona fino a domenica.",
          "english": "Done. Now the key works until Sunday.",
          "choices": [
            {
              "text": "Perfetto. L'orario della colazione è lo stesso?",
              "english": "Perfect. Is the breakfast time the same?",
              "isCorrect": True
            },
            {
              "text": "Perfetto. L'orario della cena è domani?",
              "isCorrect": False
            },
            {
              "text": "La chiave è molto bella e nuova.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Sì, sempre dalle sette alle dieci del mattino.",
          "english": "Yes, always from seven to ten in the morning.",
          "choices": [
            {
              "text": "Va bene, ho capito. Grazie delle informazioni.",
              "english": "Alright, I understand. Thanks for the information.",
              "isCorrect": True
            },
            {
              "text": "Va bene, ho perso. Grazie delle parole.",
              "isCorrect": False
            },
            {
              "text": "La colazione è molto salata oggi.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Prego. Le auguro un buon fine settimana qui da noi.",
          "english": "You're welcome. I wish you a good weekend here with us.",
          "choices": [
            {
              "text": "Grazie mille, ci vediamo dopo.",
              "english": "Thank you very much, see you later.",
              "isCorrect": True,
              "nextMessageId": "END"
            },
            {
              "text": "Grazie mille, ci laviamo dopo.",
              "isCorrect": False
            },
            {
              "text": "Buona serata, non mangio più niente.",
              "isCorrect": False
            }
          ]
        }
      ]
    },
    {
      "id": "no_availability",
      "title": "No Availability",
      "description": "Try to extend the stay, but the hotel is completely booked.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Buongiorno. Posso esserle utile?",
          "english": "Good morning. Can I be of use to you?",
          "choices": [
            {
              "text": "Buongiorno. Vorrei fermarmi un'altra notte.",
              "english": "Good morning. I would like to stay another night.",
              "isCorrect": True
            },
            {
              "text": "Buongiorno. Vorrei vendere la mia auto.",
              "isCorrect": False
            },
            {
              "text": "Certo, voglio un cane piccolo.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Mi dispiace, ma siamo al completo domani.",
          "english": "I'm sorry, but we are fully booked tomorrow.",
          "choices": [
            {
              "text": "Davvero? Non c'è nemmeno una camera singola?",
              "english": "Really? Isn't there even a single room?",
              "isCorrect": True
            },
            {
              "text": "Davvero? Non c'è nemmeno un gatto?",
              "isCorrect": False
            },
            {
              "text": "Bene, io vado al ristorante grande.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Purtroppo c'è un grande evento in città. Tutto pieno.",
          "english": "Unfortunately there is a big event in the city. Completely full.",
          "choices": [
            {
              "text": "Che sfortuna. Devo trovare un altro hotel.",
              "english": "What bad luck. I have to find another hotel.",
              "isCorrect": True
            },
            {
              "text": "Che fortuna. Devo trovare un ristorante.",
              "isCorrect": False
            },
            {
              "text": "La città è molto grande e bella.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Posso chiamare l'hotel qui vicino, se vuole.",
          "english": "I can call the hotel nearby, if you want.",
          "choices": [
            {
              "text": "Sì, per favore, sarebbe di grande aiuto.",
              "english": "Yes, please, it would be of great help.",
              "isCorrect": True
            },
            {
              "text": "Sì, per favore, chiama la polizia.",
              "isCorrect": False
            },
            {
              "text": "No, preferisco stare sotto il ponte.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Chiamo subito. Quante notti le servono?",
          "english": "I'll call right away. How many nights do you need?",
          "choices": [
            {
              "text": "Solo una notte, fino a dopodomani.",
              "english": "Only one night, until the day after tomorrow.",
              "isCorrect": True
            },
            {
              "text": "Solo una mela, fino a dopodomani.",
              "isCorrect": False
            },
            {
              "text": "Voglio cinque caffè e molto latte.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Hanno una camera! Ma costa cento euro.",
          "english": "They have a room! But it costs one hundred euros.",
          "choices": [
            {
              "text": "Va bene, la prendo. È molto vicino?",
              "english": "Alright, I'll take it. Is it very close?",
              "isCorrect": True
            },
            {
              "text": "Va bene, la prendo. È molto dolce?",
              "isCorrect": False
            },
            {
              "text": "Non voglio niente di salato oggi.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "È a due minuti a piedi da qui.",
          "english": "It is two minutes walking from here.",
          "choices": [
            {
              "text": "Perfetto. A che ora devo fare il check-out qui?",
              "english": "Perfect. What time must I do the check-out here?",
              "isCorrect": True
            },
            {
              "text": "Perfetto. A che ora devo ballare qui?",
              "isCorrect": False
            },
            {
              "text": "A piedi è molto stancante di notte.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Entro le dieci e mezza, per favore.",
          "english": "By ten thirty, please.",
          "choices": [
            {
              "text": "Va bene, lascerò la stanza per le dieci.",
              "english": "Alright, I will leave the room by ten.",
              "isCorrect": True
            },
            {
              "text": "Va bene, lascerò la tazza per le dieci.",
              "isCorrect": False
            },
            {
              "text": "Dieci e mezza è un orario molto tardi.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "D'accordo. Ho confermato la sua camera nell'altro hotel.",
          "english": "Agreed. I confirmed your room in the other hotel.",
          "choices": [
            {
              "text": "La ringrazio molto. Siete stati molto gentili.",
              "english": "I thank you very much. You have been very kind.",
              "isCorrect": True
            },
            {
              "text": "La ringrazio molto. Siete stati molto arrabbiati.",
              "isCorrect": False
            },
            {
              "text": "Non voglio andare, voglio dormire qui.",
              "isCorrect": False
            }
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "È stato un piacere. Ci vediamo domani mattina.",
          "english": "It was a pleasure. See you tomorrow morning.",
          "choices": [
            {
              "text": "A domani. Buona giornata di lavoro.",
              "english": "See you tomorrow. Have a good work day.",
              "isCorrect": True,
              "nextMessageId": "END"
            },
            {
              "text": "A domani. Buona notte di sonno.",
              "isCorrect": False
            },
            {
              "text": "Ci vediamo ieri, molto presto.",
              "isCorrect": False
            }
          ]
        }
      ]
    }
  ]
}

with open(os.path.join(base_path, "domain.json"), "w", encoding="utf-8") as f:
    json.dump(domain_data, f, indent=2, ensure_ascii=False)

with open(os.path.join(base_path, "conversations.json"), "w", encoding="utf-8") as f:
    json.dump(conversations_data, f, indent=2, ensure_ascii=False)

print("Created domain.json and conversations.json")
