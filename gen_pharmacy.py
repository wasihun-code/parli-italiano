import json

conversations_data = {
  "scenarioId": 45,
  "conversations": [
    {
      "id": "buying_sunscreen",
      "title": "Buying Sunscreen",
      "description": "Purchase sunscreen and aloe vera at the pharmacy.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Buongiorno! Prego, mi dica, di cosa ha bisogno?",
          "english": "Good morning! Please, tell me, what do you need?",
          "choices": [
            {
              "text": "Buongiorno. Sto cercando una buona crema solare per il viso.",
              "isCorrect": True,
              "feedback": "Perfect! Polite and direct."
            },
            {
              "text": "Buongiorno. Sto cercando un tavolo per due persone.",
              "isCorrect": False,
              "feedback": "You are at the pharmacy, not a restaurant!"
            },
            {
              "text": "Buongiorno. Sto cercando un biglietto per il treno.",
              "isCorrect": False,
              "feedback": "Pharmacies don't sell train tickets."
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Certo. Che fattore di protezione cerca? Alta o media?",
          "english": "Sure. What protection factor are you looking for? High or medium?",
          "choices": [
            {
              "text": "Vorrei una protezione molto alta, almeno cinquanta.",
              "isCorrect": True,
              "feedback": "Excellent! SPF 50 is 'protezione cinquanta'."
            },
            {
              "text": "Vorrei una bottiglia d'acqua frizzante molto fredda.",
              "isCorrect": False,
              "feedback": "You need sunscreen, not water."
            },
            {
              "text": "Vorrei un tavolo vicino alla finestra, per favore.",
              "isCorrect": False,
              "feedback": "Still not a restaurant!"
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Ecco questa è ottima, specifica per pelli sensibili. Serve altro?",
          "english": "Here, this one is excellent, specifically for sensitive skin. Do you need anything else?",
          "choices": [
            {
              "text": "Sì, grazie. Avete anche un doposole o dell'aloe vera?",
              "isCorrect": True,
              "feedback": "Great follow-up question for after-sun care."
            },
            {
              "text": "Sì, grazie. Avete anche una bella sciarpa di lana?",
              "isCorrect": False,
              "feedback": "Pharmacies don't usually sell wool scarves."
            },
            {
              "text": "Sì, grazie. Avete anche il sale e il pepe nero?",
              "isCorrect": False,
              "feedback": "You are not cooking right now."
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Sì, abbiamo un gel all'aloe molto fresco. Lo aggiungo?",
          "english": "Yes, we have a very fresh aloe gel. Shall I add it?",
          "choices": [
            {
              "text": "Sì, perfetto. Quanto viene il tutto in totale?",
              "isCorrect": True,
              "feedback": "Good! Asking for the total price."
            },
            {
              "text": "Sì, perfetto. Quando parte il prossimo autobus?",
              "isCorrect": False,
              "feedback": "This is a pharmacy, not a bus stop."
            },
            {
              "text": "Sì, perfetto. Dove sono i camerini per provare?",
              "isCorrect": False,
              "feedback": "You don't need fitting rooms for aloe gel."
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Sono ventotto euro e cinquanta centesimi, per favore.",
          "english": "That's twenty-eight euros and fifty cents, please.",
          "choices": [
            {
              "text": "Ecco a lei. Posso pagare con la carta di credito?",
              "isCorrect": True,
              "feedback": "Perfect response to complete the payment."
            },
            {
              "text": "Ecco a lei. Posso pagare con i biglietti del cinema?",
              "isCorrect": False,
              "feedback": "Cinema tickets are not accepted as payment."
            },
            {
              "text": "Ecco a lei. Posso ordinare anche un caffè macchiato?",
              "isCorrect": False,
              "feedback": "You cannot order coffee at a pharmacy."
            }
          ]
        }
      ]
    },
    {
      "id": "remedy_cough",
      "title": "Remedy for a Cough",
      "description": "Ask the pharmacist for a cough syrup and lozenges.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Salve, ha bisogno di un consiglio o di una medicina?",
          "english": "Hello, do you need advice or some medicine?",
          "choices": [
            {
              "text": "Salve. Ho una brutta tosse da due giorni. Cosa mi consiglia?",
              "isCorrect": True,
              "feedback": "Excellent! Stating the symptom and asking for advice."
            },
            {
              "text": "Salve. Ho una brutta camera d'albergo. Cosa mi consiglia?",
              "isCorrect": False,
              "feedback": "The pharmacist cannot help with your hotel room."
            },
            {
              "text": "Salve. Ho un biglietto aereo scaduto. Cosa mi consiglia?",
              "isCorrect": False,
              "feedback": "The pharmacist cannot help with expired flights."
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Capisco. È una tosse secca o ha anche del catarro?",
          "english": "I understand. Is it a dry cough or do you also have phlegm?",
          "choices": [
            {
              "text": "È una tosse molto secca, soprattutto durante la notte.",
              "isCorrect": True,
              "feedback": "Perfect description of a dry cough."
            },
            {
              "text": "È un libro molto noioso, soprattutto durante la notte.",
              "isCorrect": False,
              "feedback": "You need to describe your cough, not a book."
            },
            {
              "text": "È un piatto molto salato, soprattutto verso la fine.",
              "isCorrect": False,
              "feedback": "You are at a pharmacy, not a restaurant."
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Allora le do questo sciroppo calmante. Ne prenda un cucchiaio prima di dormire.",
          "english": "Then I'll give you this soothing syrup. Take a spoonful before sleeping.",
          "choices": [
            {
              "text": "Va bene. Avete anche delle caramelle per la gola irritata?",
              "isCorrect": True,
              "feedback": "Good follow-up asking for throat lozenges."
            },
            {
              "text": "Va bene. Avete anche delle scarpe per la montagna rocciosa?",
              "isCorrect": False,
              "feedback": "Pharmacies don't sell hiking shoes."
            },
            {
              "text": "Va bene. Avete anche delle verdure fresche dal contadino?",
              "isCorrect": False,
              "feedback": "You can't buy fresh vegetables at a pharmacy."
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Certo, abbiamo queste al miele e limone. Aiutano molto.",
          "english": "Sure, we have these with honey and lemon. They help a lot.",
          "choices": [
            {
              "text": "Perfetto, prendo anche quelle. Devo avere la ricetta medica?",
              "isCorrect": True,
              "feedback": "Great question checking if a prescription is needed."
            },
            {
              "text": "Perfetto, prendo anche quelle. Devo avere il passaporto verde?",
              "isCorrect": False,
              "feedback": "You don't need a passport to buy lozenges."
            },
            {
              "text": "Perfetto, prendo anche quelle. Devo usare la patente nuova?",
              "isCorrect": False,
              "feedback": "Your driver's license is irrelevant here."
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "No, sono prodotti da banco, non serve la ricetta. Sono quindici euro.",
          "english": "No, they are over-the-counter products, no prescription needed. That's fifteen euros.",
          "choices": [
            {
              "text": "Ecco a lei venti euro. Grazie per il consiglio utile.",
              "isCorrect": True,
              "feedback": "Perfect! Paying and thanking the pharmacist."
            },
            {
              "text": "Ecco a lei venti euro. Grazie per il bel taglio di capelli.",
              "isCorrect": False,
              "feedback": "You didn't get a haircut!"
            },
            {
              "text": "Ecco a lei venti euro. Grazie per aver lavato la macchina.",
              "isCorrect": False,
              "feedback": "The pharmacist didn't wash your car."
            }
          ]
        }
      ]
    },
    {
      "id": "asking_bandages",
      "title": "Asking for Bandages",
      "description": "Buy bandages and disinfectant for a minor cut.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Buongiorno, serve aiuto? Vedo che si tiene il braccio.",
          "english": "Good morning, need help? I see you are holding your arm.",
          "choices": [
            {
              "text": "Buongiorno. Sì, mi sono tagliato e mi servono dei cerotti.",
              "isCorrect": True,
              "feedback": "Clear explanation of the problem and what you need."
            },
            {
              "text": "Buongiorno. Sì, mi sono perso e mi serve una bella mappa.",
              "isCorrect": False,
              "feedback": "You are asking for a map at a pharmacy."
            },
            {
              "text": "Buongiorno. Sì, mi sono stancato e mi serve una panchina.",
              "isCorrect": False,
              "feedback": "The pharmacist cannot provide a bench."
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Mi dispiace. Ha già disinfettato la ferita o le serve un disinfettante?",
          "english": "I'm sorry. Have you already disinfected the wound or do you need a disinfectant?",
          "choices": [
            {
              "text": "Non l'ho disinfettata. Vorrei comprare anche un disinfettante, per favore.",
              "isCorrect": True,
              "feedback": "Good! Requesting the disinfectant as suggested."
            },
            {
              "text": "Non l'ho disinfettata. Vorrei comprare anche un televisore, per favore.",
              "isCorrect": False,
              "feedback": "A pharmacy does not sell televisions."
            },
            {
              "text": "Non l'ho disinfettata. Vorrei comprare anche un cappotto, per favore.",
              "isCorrect": False,
              "feedback": "A pharmacy does not sell coats."
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Va bene, ecco un disinfettante delicato e una scatola di cerotti misti.",
          "english": "All right, here is a mild disinfectant and a box of assorted bandages.",
          "choices": [
            {
              "text": "Grazie mille. Quanto devo pagare in totale per questi due?",
              "isCorrect": True,
              "feedback": "Correct way to ask for the total price."
            },
            {
              "text": "Grazie mille. Quando parte il prossimo treno per la città?",
              "isCorrect": False,
              "feedback": "You are not at the train station."
            },
            {
              "text": "Grazie mille. Quanto devo aspettare per visitare il museo?",
              "isCorrect": False,
              "feedback": "You are not buying museum tickets."
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Sono dodici euro. Vuole anche una garza nel caso il taglio sia profondo?",
          "english": "It's twelve euros. Do you also want a gauze in case the cut is deep?",
          "choices": [
            {
              "text": "No, non è molto profondo, i cerotti sono sufficienti. Pago in contanti.",
              "isCorrect": True,
              "feedback": "Perfect! Clarifying the situation and how you pay."
            },
            {
              "text": "No, non è molto profondo, i calzini sono sufficienti. Pago in contanti.",
              "isCorrect": False,
              "feedback": "Socks won't help your cut!"
            },
            {
              "text": "No, non è molto profondo, gli occhiali sono sufficienti. Pago in contanti.",
              "isCorrect": False,
              "feedback": "Glasses won't help your cut!"
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "D'accordo. Ecco a lei il resto di tre euro e lo scontrino.",
          "english": "Agreed. Here is your change of three euros and the receipt.",
          "choices": [
            {
              "text": "La ringrazio molto. Arrivederci e le auguro una buona giornata.",
              "isCorrect": True,
              "feedback": "Excellent and polite goodbye."
            },
            {
              "text": "La ringrazio molto. Arrivederci e buon viaggio verso casa.",
              "isCorrect": False,
              "feedback": "The pharmacist is at work, not traveling."
            },
            {
              "text": "La ringrazio molto. Arrivederci e buon appetito per stasera.",
              "isCorrect": False,
              "feedback": "A bit unusual to say 'enjoy your meal' right now."
            }
          ]
        }
      ]
    },
    {
      "id": "checking_prescription",
      "title": "Checking a Prescription",
      "description": "Show the pharmacist a prescription and ask for headache medicine.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Il prossimo cliente per favore! Buongiorno, prego.",
          "english": "Next customer please! Good morning, please go ahead.",
          "choices": [
            {
              "text": "Buongiorno. Ho una ricetta medica del mio dottore per queste medicine.",
              "isCorrect": True,
              "feedback": "Clear opening, presenting your prescription."
            },
            {
              "text": "Buongiorno. Ho una lettera d'amore del mio dottore per queste medicine.",
              "isCorrect": False,
              "feedback": "A love letter won't help you get medicine!"
            },
            {
              "text": "Buongiorno. Ho una vecchia mappa del mio dottore per queste medicine.",
              "isCorrect": False,
              "feedback": "A map won't help you get medicine!"
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Vediamo la ricetta. Ah, d'accordo, sono delle gocce. Vado a prenderle subito.",
          "english": "Let's see the prescription. Ah, alright, they are drops. I'll go get them right away.",
          "choices": [
            {
              "text": "Grazie. Mentre aspetta, avete anche qualcosa di forte per il mal di testa?",
              "isCorrect": True,
              "feedback": "Good multi-tasking! Asking for an additional item."
            },
            {
              "text": "Grazie. Mentre aspetta, avete anche qualcosa di forte per dipingere i muri?",
              "isCorrect": False,
              "feedback": "Pharmacies don't sell paint."
            },
            {
              "text": "Grazie. Mentre aspetta, avete anche qualcosa di forte per lavare i piatti?",
              "isCorrect": False,
              "feedback": "You need dish soap from a supermarket, not here."
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Sì, certo. Le serve qualcosa da prendere con l'acqua o masticabile?",
          "english": "Yes, of course. Do you need something to take with water or chewable?",
          "choices": [
            {
              "text": "Preferisco le compresse da prendere con un po' d'acqua, grazie.",
              "isCorrect": True,
              "feedback": "Perfect! Describing your preference clearly."
            },
            {
              "text": "Preferisco le patatine da prendere con un po' d'acqua, grazie.",
              "isCorrect": False,
              "feedback": "You can't buy chips for a headache here."
            },
            {
              "text": "Preferisco le matite da prendere con un po' d'acqua, grazie.",
              "isCorrect": False,
              "feedback": "Pencils are not medicine."
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Ecco le sue gocce e l'ibuprofene per il mal di testa. Le serve un sacchetto?",
          "english": "Here are your drops and the ibuprofen for the headache. Do you need a bag?",
          "choices": [
            {
              "text": "No, grazie, le metto nel mio zaino. Quant'è il conto?",
              "isCorrect": True,
              "feedback": "Good response declining the bag and asking for the price."
            },
            {
              "text": "No, grazie, le metto nel mio frigorifero. Quant'è il conto?",
              "isCorrect": False,
              "feedback": "You aren't taking them to your fridge right now."
            },
            {
              "text": "No, grazie, le metto nel mio forno. Quant'è il conto?",
              "isCorrect": False,
              "feedback": "Don't put medicine in an oven!"
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "In totale sono ventiquattro euro. Paga con il bancomat?",
          "english": "In total it's twenty-four euros. Are you paying with a debit card?",
          "choices": [
            {
              "text": "Sì, pago con il bancomat. Ecco a lei, grazie mille e arrivederci.",
              "isCorrect": True,
              "feedback": "Excellent! Finalizing the payment and saying goodbye."
            },
            {
              "text": "Sì, pago con il bancomat. Ecco a lei, grazie mille e buon appetito.",
              "isCorrect": False,
              "feedback": "You don't say 'buon appetito' here."
            },
            {
              "text": "Sì, pago con il bancomat. Ecco a lei, grazie mille e buonanotte.",
              "isCorrect": False,
              "feedback": "It's morning, so 'buonanotte' is inappropriate."
            }
          ]
        }
      ]
    }
  ]
}

with open("src/data/exports/shopping/pharmacy_purchase/conversations.json", "w") as f:
    json.dump(conversations_data, f, indent=2, ensure_ascii=False)
