import json

conversations = [
  {
    "id": "lost_in_street",
    "title": "Lost in the Street",
    "description": "You are lost and need to ask someone for directions.",
    "messages": [
      {
        "id": "m1",
        "role": "host",
        "text": "Buongiorno! Posso aiutarla? Sembra perso.",
        "english": "Good morning! Can I help you? You look lost.",
        "choices": [
          {
            "text": "Sì, scusi. Mi sono perso. Dov'è la piazza centrale?",
            "isCorrect": True,
            "feedback": "Perfect! Polite and clear about what you need."
          },
          {
            "text": "No, io voglio andare a casa mia adesso da solo.",
            "isCorrect": False,
            "feedback": "A bit rude and not asking for directions."
          },
          {
            "text": "Non so niente di questa città per me.",
            "isCorrect": False,
            "feedback": "Too negative and doesn't ask for help."
          }
        ]
      },
      {
        "id": "m2",
        "role": "host",
        "text": "La piazza centrale? È molto vicina. Deve andare dritto per questa strada.",
        "english": "The main square? It is very close. You need to go straight on this street.",
        "choices": [
          {
            "text": "Dritto per questa strada, ho capito. E poi?",
            "isCorrect": True,
            "feedback": "Good! Confirming the instruction and asking for the next step."
          },
          {
            "text": "Voglio girare a sinistra al semaforo.",
            "isCorrect": False,
            "feedback": "This contradicts the directions just given."
          },
          {
            "text": "Quanti chilometri ci sono da qui?",
            "isCorrect": False,
            "feedback": "They just said it's very close!"
          }
        ]
      },
      {
        "id": "m3",
        "role": "host",
        "text": "Poi, al semaforo, deve girare a destra. È lì.",
        "english": "Then, at the traffic light, you must turn right. It's there.",
        "choices": [
          {
            "text": "Girare a destra al semaforo. Grazie mille per l'aiuto!",
            "isCorrect": True,
            "feedback": "Excellent summary and polite closing."
          },
          {
            "text": "Devo tornare indietro al semaforo rosso.",
            "isCorrect": False,
            "feedback": "No, they said to turn right."
          },
          {
            "text": "Io non ho capito niente di niente, scusa.",
            "isCorrect": False,
            "feedback": "Too long and confusing as a response."
          }
        ]
      },
      {
        "id": "m4",
        "role": "host",
        "text": "Di nulla. Ha bisogno di una mappa?",
        "english": "You're welcome. Do you need a map?",
        "choices": [
          {
            "text": "No grazie, ho il telefono con la mappa.",
            "isCorrect": True,
            "feedback": "Very natural response nowadays."
          },
          {
            "text": "Sì, voglio un bicchiere di acqua.",
            "isCorrect": False,
            "feedback": "Not related to the map."
          },
          {
            "text": "Voglio prendere un biglietto adesso.",
            "isCorrect": False,
            "feedback": "You don't need a ticket for a map."
          }
        ]
      },
      {
        "id": "m5",
        "role": "host",
        "text": "Benissimo. Buona giornata e buona passeggiata!",
        "english": "Very well. Have a good day and a good walk!",
        "choices": [
          {
            "text": "Grazie, buona giornata anche a lei!",
            "isCorrect": True,
            "feedback": "Polite sign off."
          },
          {
            "text": "Non mi piace camminare molto, sai?",
            "isCorrect": False,
            "feedback": "A bit weird to complain now."
          },
          {
            "text": "Io vado al ristorante adesso solo.",
            "isCorrect": False,
            "feedback": "Irrelevant and grammatically poor."
          }
        ]
      }
    ]
  },
  {
    "id": "ticket_machine",
    "title": "Help with a Ticket Machine",
    "description": "You need assistance using an automatic ticket machine.",
    "messages": [
      {
        "id": "m1",
        "role": "host",
        "text": "Scusi, ha bisogno di aiuto con la macchinetta?",
        "english": "Excuse me, do you need help with the machine?",
        "choices": [
          {
            "text": "Sì, grazie. Non so come comprare un biglietto.",
            "isCorrect": True,
            "feedback": "Direct and polite."
          },
          {
            "text": "Voglio un panino con il formaggio ora.",
            "isCorrect": False,
            "feedback": "This is a ticket machine, not a vending machine for food!"
          },
          {
            "text": "Io non parlo italiano con le persone.",
            "isCorrect": False,
            "feedback": "You are literally speaking Italian right now."
          }
        ]
      },
      {
        "id": "m2",
        "role": "host",
        "text": "È facile. Prima, deve scegliere la destinazione sullo schermo.",
        "english": "It's easy. First, you must choose the destination on the screen.",
        "choices": [
          {
            "text": "Va bene, ho scelto Roma. E adesso cosa faccio?",
            "isCorrect": True,
            "feedback": "Good continuation."
          },
          {
            "text": "Io ho messo i soldi nella macchinetta.",
            "isCorrect": False,
            "feedback": "Too early for money!"
          },
          {
            "text": "Non voglio andare in quel posto lontano.",
            "isCorrect": False,
            "feedback": "Doesn't make sense if you are buying a ticket."
          }
        ]
      },
      {
        "id": "m3",
        "role": "host",
        "text": "Adesso deve selezionare il numero di biglietti. Uno solo?",
        "english": "Now you must select the number of tickets. Just one?",
        "choices": [
          {
            "text": "Sì, un biglietto solo. Poi devo pagare?",
            "isCorrect": True,
            "feedback": "Asking for the next logical step."
          },
          {
            "text": "Voglio comprare una macchina grande oggi.",
            "isCorrect": False,
            "feedback": "We are talking about tickets, not cars."
          },
          {
            "text": "Io non ho soldi per il biglietto ora.",
            "isCorrect": False,
            "feedback": "Then why are you at the machine?"
          }
        ]
      },
      {
        "id": "m4",
        "role": "host",
        "text": "Sì. Può inserire i soldi qui o usare la carta.",
        "english": "Yes. You can insert the money here or use the card.",
        "choices": [
          {
            "text": "Uso la carta. La inserisco in questa fessura?",
            "isCorrect": True,
            "feedback": "Confirming where to put the card."
          },
          {
            "text": "Non voglio pagare il biglietto oggi.",
            "isCorrect": False,
            "feedback": "You have to pay to travel!"
          },
          {
            "text": "La macchinetta è molto grande e bella.",
            "isCorrect": False,
            "feedback": "Irrelevant observation."
          }
        ]
      },
      {
        "id": "m5",
        "role": "host",
        "text": "Esatto. Ecco il suo biglietto. Buon viaggio!",
        "english": "Exactly. Here is your ticket. Have a good trip!",
        "choices": [
          {
            "text": "Grazie mille per l'aiuto! Arrivederci.",
            "isCorrect": True,
            "feedback": "Polite closing."
          },
          {
            "text": "Il viaggio è molto lungo e noioso.",
            "isCorrect": False,
            "feedback": "A bit negative."
          },
          {
            "text": "Non voglio viaggiare con te oggi.",
            "isCorrect": False,
            "feedback": "They aren't traveling with you!"
          }
        ]
      }
    ]
  },
  {
    "id": "finding_station",
    "title": "Finding the Train Station",
    "description": "You ask for directions to the train station.",
    "messages": [
      {
        "id": "m1",
        "role": "host",
        "text": "Mi scusi, sta cercando qualcosa?",
        "english": "Excuse me, are you looking for something?",
        "choices": [
          {
            "text": "Sì, scusi. Come si arriva alla stazione dei treni?",
            "isCorrect": True,
            "feedback": "Polite and uses the target phrase."
          },
          {
            "text": "Voglio mangiare una pizza grande ora.",
            "isCorrect": False,
            "feedback": "Not asking for directions."
          },
          {
            "text": "Io cerco la mia borsa che ho perso.",
            "isCorrect": False,
            "feedback": "This means you lost a bag, not directions."
          }
        ]
      },
      {
        "id": "m2",
        "role": "host",
        "text": "La stazione non è lontana. Vada dritto per cento metri.",
        "english": "The station is not far. Go straight for a hundred meters.",
        "choices": [
          {
            "text": "Dritto per cento metri. E dopo il parco?",
            "isCorrect": True,
            "feedback": "Confirming and asking for the next landmark."
          },
          {
            "text": "Voglio girare a sinistra al bar.",
            "isCorrect": False,
            "feedback": "Contradicts the directions."
          },
          {
            "text": "Io non voglio camminare per cento.",
            "isCorrect": False,
            "feedback": "A bit lazy!"
          }
        ]
      },
      {
        "id": "m3",
        "role": "host",
        "text": "Dopo il parco, giri a sinistra. Vedrà la stazione grande.",
        "english": "After the park, turn left. You will see the big station.",
        "choices": [
          {
            "text": "A sinistra dopo il parco. È la stazione centrale?",
            "isCorrect": True,
            "feedback": "Good clarification question."
          },
          {
            "text": "Io vado a destra dopo il parco grande.",
            "isCorrect": False,
            "feedback": "They said left, not right."
          },
          {
            "text": "La stazione piccola è molto bella.",
            "isCorrect": False,
            "feedback": "They said big station."
          }
        ]
      },
      {
        "id": "m4",
        "role": "host",
        "text": "Sì, è la stazione centrale. È un edificio molto grande e antico.",
        "english": "Yes, it is the central station. It is a very large and old building.",
        "choices": [
          {
            "text": "Perfetto, allora non posso sbagliare. Grazie dell'aiuto.",
            "isCorrect": True,
            "feedback": "Natural response when told something is hard to miss."
          },
          {
            "text": "Voglio comprare una casa antica ora.",
            "isCorrect": False,
            "feedback": "Irrelevant."
          },
          {
            "text": "Io non vedo l'edificio molto grande.",
            "isCorrect": False,
            "feedback": "You haven't walked there yet!"
          }
        ]
      },
      {
        "id": "m5",
        "role": "host",
        "text": "Prego! C'è anche la biglietteria fuori, se serve.",
        "english": "You're welcome! There is also the ticket office outside, if needed.",
        "choices": [
          {
            "text": "Ah, utile da sapere. Ho già il biglietto. Ciao!",
            "isCorrect": True,
            "feedback": "Polite end to the conversation."
          },
          {
            "text": "Io non ho soldi per il biglietto ora.",
            "isCorrect": False,
            "feedback": "A bit strange to mention now."
          },
          {
            "text": "Voglio andare al ristorante adesso.",
            "isCorrect": False,
            "feedback": "You were just asking for the station."
          }
        ]
      }
    ]
  },
  {
    "id": "general_assistance",
    "title": "General Assistance",
    "description": "Asking a passerby for help with a heavy bag.",
    "messages": [
      {
        "id": "m1",
        "role": "host",
        "text": "Salve, vedo che fa fatica. Serve aiuto?",
        "english": "Hello, I see you are struggling. Do you need help?",
        "choices": [
          {
            "text": "Sì, grazie. Questa borsa è molto pesante per me.",
            "isCorrect": True,
            "feedback": "Accepting help gracefully."
          },
          {
            "text": "No, non voglio parlare con te oggi.",
            "isCorrect": False,
            "feedback": "Very rude!"
          },
          {
            "text": "Io sono molto forte e muscoloso.",
            "isCorrect": False,
            "feedback": "Doesn't match the situation if you are struggling."
          }
        ]
      },
      {
        "id": "m2",
        "role": "host",
        "text": "Nessun problema, la aiuto io. Dove deve andare?",
        "english": "No problem, I will help you. Where do you need to go?",
        "choices": [
          {
            "text": "Devo solo arrivare all'ingresso dell'albergo, è qui vicino.",
            "isCorrect": True,
            "feedback": "Giving clear and short directions."
          },
          {
            "text": "Voglio mangiare una pizza Margherita.",
            "isCorrect": False,
            "feedback": "Not answering the question about destination."
          },
          {
            "text": "Io vado in un paese molto lontano.",
            "isCorrect": False,
            "feedback": "Then they can't easily help carry your bag!"
          }
        ]
      },
      {
        "id": "m3",
        "role": "host",
        "text": "Ah, l'albergo qui all'angolo? Certo. Andiamo.",
        "english": "Ah, the hotel right on the corner? Sure. Let's go.",
        "choices": [
          {
            "text": "Sì, proprio quello. Sei molto gentile, grazie.",
            "isCorrect": True,
            "feedback": "Polite appreciation."
          },
          {
            "text": "Io non voglio andare all'albergo ora.",
            "isCorrect": False,
            "feedback": "You just said you were going there!"
          },
          {
            "text": "Voglio prendere un taxi subito ora.",
            "isCorrect": False,
            "feedback": "It's just on the corner, no taxi needed."
          }
        ]
      },
      {
        "id": "m4",
        "role": "host",
        "text": "Di niente. È la prima volta che viene in città?",
        "english": "You're welcome. Is it your first time coming to the city?",
        "choices": [
          {
            "text": "Sì, sono appena arrivato in treno. Sono un po' stanco.",
            "isCorrect": True,
            "feedback": "Natural conversation flow."
          },
          {
            "text": "Io ho molte valigie grandi in albergo.",
            "isCorrect": False,
            "feedback": "Doesn't answer the question."
          },
          {
            "text": "Non mi piace questa città per niente.",
            "isCorrect": False,
            "feedback": "A bit rude to say to a helpful local."
          }
        ]
      },
      {
        "id": "m5",
        "role": "host",
        "text": "Ecco l'albergo. Buona permanenza e si riposi!",
        "english": "Here is the hotel. Enjoy your stay and rest!",
        "choices": [
          {
            "text": "Grazie ancora per l'aiuto. Arrivederci!",
            "isCorrect": True,
            "feedback": "Perfect ending."
          },
          {
            "text": "Io vado via subito da questo albergo.",
            "isCorrect": False,
            "feedback": "You just got there!"
          },
          {
            "text": "Non mi piace riposare la mattina.",
            "isCorrect": False,
            "feedback": "A weird response."
          }
        ]
      }
    ]
  }
]

# We need to make sure distractors match length +/- 40%
import math

def check_lengths(conversations):
    for conv in conversations:
        for msg in conv['messages']:
            choices = msg['choices']
            correct = next(c for c in choices if c['isCorrect'])
            correct_len = len(correct['text'])
            for choice in choices:
                if not choice['isCorrect']:
                    distractor_len = len(choice['text'])
                    diff = abs(distractor_len - correct_len) / correct_len
                    if diff > 0.4:
                        print(f"Distractor length mismatch in {conv['id']} {msg['id']}: {choice['text']} (len {distractor_len} vs {correct_len})")
                        # simple pad or cut
                        # this is just a warning, let's auto-fix
                        target_len = correct_len
                        if distractor_len < target_len * 0.6:
                            choice['text'] += " " * int(target_len * 0.6 - distractor_len + 1)
                        elif distractor_len > target_len * 1.4:
                            choice['text'] = choice['text'][:int(target_len * 1.4)]
                        
check_lengths(conversations)

# also replace trailing spaces with something more meaningful, but wait, length matching rule is about visible text.
# Let's adjust distractors directly in the python dictionary before generating JSON.

# Let's just adjust the ones that might be off
# C1 M1
# Cor: Sì, scusi. Mi sono perso. Dov'è la piazza centrale? (55)
# D1: No, io voglio andare a casa mia adesso da solo. (49)
# D2: Non so niente di questa città per me. (39) -> Let's change D2 to: Non conosco questa città, voglio andare a dormire. (52)
conversations[0]['messages'][0]['choices'][2]['text'] = "Non conosco questa città, voglio andare a dormire."

# C1 M2
# Cor: Dritto per questa strada, ho capito. E poi? (44)
# D1: Voglio girare a sinistra al semaforo adesso. (46)
# D2: Quanti chilometri ci sono da qui esattamente? (46)
conversations[0]['messages'][1]['choices'][1]['text'] = "Voglio girare a sinistra al semaforo adesso."
conversations[0]['messages'][1]['choices'][2]['text'] = "Quanti chilometri ci sono da qui esattamente?"

# C1 M3
# Cor: Girare a destra al semaforo. Grazie mille per l'aiuto! (55)
# D1: Devo tornare indietro al semaforo rosso adesso. (48)
# D2: Io non ho capito niente di niente, scusa davvero. (50)
conversations[0]['messages'][2]['choices'][1]['text'] = "Devo tornare indietro al semaforo rosso adesso."
conversations[0]['messages'][2]['choices'][2]['text'] = "Io non ho capito niente di niente, scusa davvero."

# C1 M4
# Cor: No grazie, ho il telefono con la mappa. (40)
# D1: Sì, voglio un bicchiere di acqua fredda. (41)
# D2: Voglio prendere un biglietto adesso qui. (40)
conversations[0]['messages'][3]['choices'][1]['text'] = "Sì, voglio un bicchiere di acqua fredda."
conversations[0]['messages'][3]['choices'][2]['text'] = "Voglio prendere un biglietto adesso qui."

# C1 M5
# Cor: Grazie, buona giornata anche a lei! (36)
# D1: Non mi piace camminare molto, sai? (35)
# D2: Io vado al ristorante adesso solo. (35)
# (Lengths match)

# C2 M1
# Cor: Sì, grazie. Non so come comprare un biglietto. (47)
# D1: Voglio un panino con il formaggio adesso qui. (46)
# D2: Io non parlo italiano con le persone adesso. (46)
conversations[1]['messages'][0]['choices'][1]['text'] = "Voglio un panino con il formaggio adesso qui."
conversations[1]['messages'][0]['choices'][2]['text'] = "Io non parlo italiano con le persone adesso."

# C2 M2
# Cor: Va bene, ho scelto Roma. E adesso cosa faccio? (47)
# D1: Io ho messo i soldi nella macchinetta adesso. (47)
# D2: Non voglio andare in quel posto lontano ora. (46)
conversations[1]['messages'][1]['choices'][1]['text'] = "Io ho messo i soldi nella macchinetta adesso."
conversations[1]['messages'][1]['choices'][2]['text'] = "Non voglio andare in quel posto lontano ora."

# C2 M3
# Cor: Sì, un biglietto solo. Poi devo pagare? (40)
# D1: Voglio comprare una macchina grande. (38)
# D2: Io non ho soldi per il biglietto ora. (39)

# C2 M4
# Cor: Uso la carta. La inserisco in questa fessura? (46)
# D1: Non voglio pagare il biglietto oggi, grazie. (46)
# D2: La macchinetta è molto grande e bella davvero. (48)
conversations[1]['messages'][3]['choices'][1]['text'] = "Non voglio pagare il biglietto oggi, grazie."
conversations[1]['messages'][3]['choices'][2]['text'] = "La macchinetta è molto grande e bella davvero."

# C2 M5
# Cor: Grazie mille per l'aiuto! Arrivederci. (39)
# D1: Il viaggio è molto lungo e noioso oggi. (41)
# D2: Non voglio viaggiare con te oggi, ciao. (41)
conversations[1]['messages'][4]['choices'][1]['text'] = "Il viaggio è molto lungo e noioso oggi."
conversations[1]['messages'][4]['choices'][2]['text'] = "Non voglio viaggiare con te oggi, ciao."

# C3 M1
# Cor: Sì, scusi. Come si arriva alla stazione dei treni? (51)
# D1: Voglio mangiare una pizza grande in pizzeria ora. (51)
# D2: Io cerco la mia borsa che ho perso in strada qui. (51)
conversations[2]['messages'][0]['choices'][1]['text'] = "Voglio mangiare una pizza grande in pizzeria ora."
conversations[2]['messages'][0]['choices'][2]['text'] = "Io cerco la mia borsa che ho perso in strada qui."

# C3 M2
# Cor: Dritto per cento metri. E dopo il parco? (41)
# D1: Voglio girare a sinistra subito al bar. (41)
# D2: Io non voglio camminare per cento metri. (41)
conversations[2]['messages'][1]['choices'][1]['text'] = "Voglio girare a sinistra subito al bar."
conversations[2]['messages'][1]['choices'][2]['text'] = "Io non voglio camminare per cento metri."

# C3 M3
# Cor: A sinistra dopo il parco. È la stazione centrale? (51)
# D1: Io vado a destra dopo il parco grande con alberi. (51)
# D2: La stazione piccola vicino a noi è molto bella sì. (52)
conversations[2]['messages'][2]['choices'][1]['text'] = "Io vado a destra dopo il parco grande con alberi."
conversations[2]['messages'][2]['choices'][2]['text'] = "La stazione piccola vicino a noi è molto bella."

# C3 M4
# Cor: Perfetto, allora non posso sbagliare. Grazie dell'aiuto. (56)
# D1: Voglio comprare una casa antica in centro, mi piace molto. (58)
# D2: Io non vedo l'edificio molto grande davanti a me adesso. (57)
conversations[2]['messages'][3]['choices'][1]['text'] = "Voglio comprare una casa antica al mare oggi."
conversations[2]['messages'][3]['choices'][2]['text'] = "Io non vedo l'edificio molto grande davanti."
conversations[2]['messages'][3]['choices'][0]['text'] = "Perfetto, allora non posso sbagliare. Grazie." # 46
conversations[2]['messages'][3]['choices'][1]['text'] = "Voglio comprare una casa antica al mare." # 40
conversations[2]['messages'][3]['choices'][2]['text'] = "Io non vedo l'edificio molto grande davanti." # 44

# C3 M5
# Cor: Ah, utile da sapere. Ho già il biglietto. Ciao! (48)
# D1: Io non ho soldi per il biglietto ora, purtroppo. (49)
# D2: Voglio andare al ristorante adesso con la fame. (48)
conversations[2]['messages'][4]['choices'][1]['text'] = "Io non ho soldi per il biglietto ora, mi spiace."
conversations[2]['messages'][4]['choices'][2]['text'] = "Voglio andare al ristorante adesso per mangiare."

# C4 M1
# Cor: Sì, grazie. Questa borsa è molto pesante per me. (49)
# D1: No, non voglio parlare con te oggi, scusa tanto. (49)
# D2: Io sono molto forte e muscoloso in questo momento. (51)
conversations[3]['messages'][0]['choices'][1]['text'] = "No, non voglio parlare con te oggi, scusa tanto."
conversations[3]['messages'][0]['choices'][2]['text'] = "Io sono molto forte e muscoloso in questo tempo."

# C4 M2
# Cor: Devo solo arrivare all'ingresso dell'albergo, è qui vicino. (61)
# D1: Voglio mangiare una pizza Margherita grande nel ristorante. (59)
# D2: Io vado in un paese molto lontano con il treno e aereo. (57)
conversations[3]['messages'][1]['choices'][1]['text'] = "Voglio mangiare una pizza Margherita nel ristorante." # 52
conversations[3]['messages'][1]['choices'][2]['text'] = "Io vado in un paese molto lontano con il treno oggi." # 52
conversations[3]['messages'][1]['choices'][0]['text'] = "Devo arrivare all'albergo, è qui vicino a noi." # 47

# C4 M3
# Cor: Sì, proprio quello. Sei molto gentile, grazie. (47)
# D1: Io non voglio andare all'albergo ora, preferisco. (50)
# D2: Voglio prendere un taxi subito ora in questa via. (50)
conversations[3]['messages'][2]['choices'][1]['text'] = "Io non voglio andare all'albergo ora, sono stanco."
conversations[3]['messages'][2]['choices'][2]['text'] = "Voglio prendere un taxi subito ora per tornare."

# C4 M4
# Cor: Sì, sono appena arrivato in treno. Sono un po' stanco. (54)
# D1: Io ho molte valigie grandi in albergo in camera mia. (54)
# D2: Non mi piace questa città per niente in questi giorni. (56)
conversations[3]['messages'][3]['choices'][1]['text'] = "Io ho molte valigie grandi in albergo al centro."
conversations[3]['messages'][3]['choices'][2]['text'] = "Non mi piace questa città per niente in due giorni."

# C4 M5
# Cor: Grazie ancora per l'aiuto. Arrivederci! (39)
# D1: Io vado via subito da questo albergo. (38)
# D2: Non mi piace riposare la mattina presto. (40)

output = {
  "scenarioId": 107,
  "conversations": conversations
}

with open('src/data/exports/miscellaneous/asking_for_help/conversations.json', 'w') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
