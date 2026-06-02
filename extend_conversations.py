import json

new_msgs = {
  "paying_in_cash": [
    {
      "id": "m6",
      "role": "host",
      "text": "Scusi, aspetti un momento! Ha dimenticato il suo ombrello qui sul bancone.",
      "english": "Excuse me, wait a moment! You forgot your umbrella here on the counter.",
      "choices": [
        {
          "text": "Oh, grazie mille! Sarei dovuto tornare indietro a prenderlo.",
          "english": "Oh, thank you very much! I would have had to come back to get it.",
          "isCorrect": True,
          "feedback": "Great! You thanked the cashier for noticing."
        },
        {
          "text": "Non è il mio ombrello, io odio la pioggia.",
          "english": "It's not my umbrella, I hate the rain.",
          "isCorrect": False,
          "feedback": "It's better to accept the umbrella gracefully in this context."
        },
        {
          "text": "Il conto non è giusto, mancano cinque euro da qui.",
          "english": "The bill is not right, five euros are missing from here.",
          "isCorrect": False,
          "feedback": "You already finished paying."
        }
      ]
    },
    {
      "id": "m7",
      "role": "host",
      "text": "Di nulla. Fuori piove molto forte in questo momento?",
      "english": "You're welcome. Is it raining very hard outside right now?",
      "choices": [
        {
          "text": "Sì, purtroppo piove a dirotto da questa mattina presto.",
          "english": "Yes, unfortunately it's been pouring since early this morning.",
          "isCorrect": True,
          "feedback": "Perfect answer."
        },
        {
          "text": "Voglio pagare in contanti, grazie mille.",
          "english": "I want to pay in cash, thank you very much.",
          "isCorrect": False,
          "feedback": "You already paid."
        },
        {
          "text": "Il mio ombrello è di colore blu scuro e molto grande.",
          "english": "My umbrella is dark blue and very big.",
          "isCorrect": False,
          "feedback": "The host asked about the weather."
        }
      ]
    },
    {
      "id": "m8",
      "role": "host",
      "text": "Se vuole, può aspettare qui dentro finché non smette.",
      "english": "If you want, you can wait inside here until it stops.",
      "choices": [
        {
          "text": "Grazie, è molto gentile, ma devo andare al lavoro subito.",
          "english": "Thanks, you are very kind, but I have to go to work immediately.",
          "isCorrect": True,
          "feedback": "Polite decline."
        },
        {
          "text": "No, il bancomat non funziona bene oggi.",
          "english": "No, the ATM is not working well today.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        },
        {
          "text": "Il ristorante è chiuso per le vacanze estive adesso.",
          "english": "The restaurant is closed for summer holidays now.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        }
      ]
    },
    {
      "id": "m9",
      "role": "host",
      "text": "Capisco perfettamente. Faccia attenzione per la strada, allora.",
      "english": "I understand perfectly. Be careful on the road, then.",
      "choices": [
        {
          "text": "Lo farò sicuramente. Grazie ancora per tutto e buona giornata.",
          "english": "I certainly will. Thanks again for everything and have a good day.",
          "isCorrect": True,
          "feedback": "Very polite farewell."
        },
        {
          "text": "Devo andare a comprare una macchina nuova domani mattina.",
          "english": "I have to go buy a new car tomorrow morning.",
          "isCorrect": False,
          "feedback": "Overly specific and irrelevant."
        },
        {
          "text": "Il treno parte tra cinque minuti, sono in ritardo.",
          "english": "The train leaves in five minutes, I am late.",
          "isCorrect": False,
          "feedback": "A bit abrupt."
        }
      ]
    },
    {
      "id": "m10",
      "role": "host",
      "text": "Buona giornata a lei. Arrivederci!",
      "english": "Have a good day too. Goodbye!",
      "choices": [
        {
          "text": "Arrivederci e a presto!",
          "english": "Goodbye and see you soon!",
          "isCorrect": True,
          "feedback": "Great job finishing the conversation."
        },
        {
          "text": "Il caffè era molto freddo oggi.",
          "english": "The coffee was very cold today.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        },
        {
          "text": "Non voglio pagare il conto adesso.",
          "english": "I don't want to pay the bill now.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        }
      ]
    }
  ],
  "asking_for_change": [
    {
      "id": "m6",
      "role": "host",
      "text": "Scusi, posso chiederle un favore mentre è qui?",
      "english": "Excuse me, can I ask you a favor while you are here?",
      "choices": [
        {
          "text": "Certo, mi dica pure. Come posso aiutarla?",
          "english": "Sure, tell me. How can I help you?",
          "isCorrect": True,
          "feedback": "Friendly and helpful response."
        },
        {
          "text": "No, non ho monete con me.",
          "english": "No, I don't have coins with me.",
          "isCorrect": False,
          "feedback": "You just got coins from them."
        },
        {
          "text": "Il bagno è chiuso, mi dispiace.",
          "english": "The bathroom is closed, I'm sorry.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        }
      ]
    },
    {
      "id": "m7",
      "role": "host",
      "text": "Per caso ha anche una moneta da due euro da cambiare in spiccioli?",
      "english": "By any chance do you also have a two euro coin to change into small change?",
      "choices": [
        {
          "text": "Sì, guardo nel portafoglio. Ecco qui una moneta da due euro.",
          "english": "Yes, I look in my wallet. Here is a two euro coin.",
          "isCorrect": True,
          "feedback": "Good job accommodating their request."
        },
        {
          "text": "Voglio pagare con la carta di credito, grazie.",
          "english": "I want to pay with credit card, thanks.",
          "isCorrect": False,
          "feedback": "You are making change, not paying."
        },
        {
          "text": "Il biglietto costa troppo per me.",
          "english": "The ticket costs too much for me.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        }
      ]
    },
    {
      "id": "m8",
      "role": "host",
      "text": "Perfetto! Le do dieci monete da venti centesimi, va bene?",
      "english": "Perfect! I give you ten twenty-cent coins, is that okay?",
      "choices": [
        {
          "text": "Sì, va benissimo. Le monete piccole sono sempre utili.",
          "english": "Yes, that's fine. Small coins are always useful.",
          "isCorrect": True,
          "feedback": "Natural response."
        },
        {
          "text": "No, voglio cento euro in contanti subito.",
          "english": "No, I want one hundred euros in cash immediately.",
          "isCorrect": False,
          "feedback": "That's not equal to two euros."
        },
        {
          "text": "Questa borsa costa cinquanta euro.",
          "english": "This bag costs fifty euros.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        }
      ]
    },
    {
      "id": "m9",
      "role": "host",
      "text": "Ottimo, ecco i suoi venti centesimi. La ringrazio molto per l'aiuto.",
      "english": "Great, here are your twenty cents. Thank you very much for your help.",
      "choices": [
        {
          "text": "Di nulla, figurati. È stato un piacere aiutarla.",
          "english": "You're welcome, don't mention it. It was a pleasure helping you.",
          "isCorrect": True,
          "feedback": "Very polite."
        },
        {
          "text": "Il pin è sbagliato, provo ancora.",
          "english": "The pin is wrong, I try again.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        },
        {
          "text": "Voglio uno scontrino per questo favore.",
          "english": "I want a receipt for this favor.",
          "isCorrect": False,
          "feedback": "You don't get a receipt for changing money."
        }
      ]
    },
    {
      "id": "m10",
      "role": "host",
      "text": "Bene, ora può andare a prendere il suo caffè. Arrivederci!",
      "english": "Well, now you can go get your coffee. Goodbye!",
      "choices": [
        {
          "text": "Grazie ancora, a presto e buon lavoro!",
          "english": "Thanks again, see you soon and good work!",
          "isCorrect": True,
          "feedback": "Perfect finish."
        },
        {
          "text": "Il treno parte in ritardo oggi.",
          "english": "The train leaves late today.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        },
        {
          "text": "Non mi piace il caffè caldo.",
          "english": "I don't like hot coffee.",
          "isCorrect": False,
          "feedback": "Not very polite."
        }
      ]
    }
  ],
  "card_declined": [
    {
      "id": "m6",
      "role": "host",
      "text": "A proposito, il sistema dei pagamenti elettronici ha problemi da ieri.",
      "english": "By the way, the electronic payment system has been having problems since yesterday.",
      "choices": [
        {
          "text": "Ah, ecco perché la carta non funzionava. Tutto chiaro adesso.",
          "english": "Ah, that's why the card wasn't working. Everything is clear now.",
          "isCorrect": True,
          "feedback": "Good response to the explanation."
        },
        {
          "text": "Voglio pagare con la mia carta di credito americana.",
          "english": "I want to pay with my American credit card.",
          "isCorrect": False,
          "feedback": "You just paid in cash."
        },
        {
          "text": "Il cibo del ristorante non era buono.",
          "english": "The restaurant food wasn't good.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        }
      ]
    },
    {
      "id": "m7",
      "role": "host",
      "text": "Sì, stiamo aspettando il tecnico per riparare la linea internet.",
      "english": "Yes, we are waiting for the technician to repair the internet line.",
      "choices": [
        {
          "text": "Spero che riescano a risolvere il guasto velocemente.",
          "english": "I hope they manage to fix the fault quickly.",
          "isCorrect": True,
          "feedback": "Friendly and empathetic."
        },
        {
          "text": "Voglio un tecnico per il mio computer a casa.",
          "english": "I want a technician for my computer at home.",
          "isCorrect": False,
          "feedback": "Not what they meant."
        },
        {
          "text": "Il prezzo di questa borsa è troppo alto.",
          "english": "The price of this bag is too high.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        }
      ]
    },
    {
      "id": "m8",
      "role": "host",
      "text": "Lo spero anche io! Per fortuna lei aveva dei contanti in tasca.",
      "english": "I hope so too! Luckily you had some cash in your pocket.",
      "choices": [
        {
          "text": "Sì, porto sempre un po' di soldi con me per sicurezza.",
          "english": "Yes, I always carry a little money with me for safety.",
          "isCorrect": True,
          "feedback": "A very natural statement."
        },
        {
          "text": "Io non ho mai contanti, mi dispiace.",
          "english": "I never have cash, I'm sorry.",
          "isCorrect": False,
          "feedback": "Contradicts what just happened."
        },
        {
          "text": "La banca è molto lontana da qui.",
          "english": "The bank is very far from here.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        }
      ]
    },
    {
      "id": "m9",
      "role": "host",
      "text": "È un'ottima abitudine. Grazie per la pazienza e la comprensione.",
      "english": "It's a great habit. Thank you for your patience and understanding.",
      "choices": [
        {
          "text": "Figurati, nessun problema. Buona continuazione e buon lavoro.",
          "english": "Don't mention it, no problem. Have a good continuation and good work.",
          "isCorrect": True,
          "feedback": "Excellent closing remark."
        },
        {
          "text": "Non voglio questo scontrino, voglio i soldi indietro.",
          "english": "I don't want this receipt, I want the money back.",
          "isCorrect": False,
          "feedback": "Unreasonable."
        },
        {
          "text": "Voglio comprare anche un giornale ora.",
          "english": "I want to buy a newspaper now too.",
          "isCorrect": False,
          "feedback": "Conversation is ending."
        }
      ]
    },
    {
      "id": "m10",
      "role": "host",
      "text": "Grazie mille, arrivederci e buona giornata!",
      "english": "Thank you very much, goodbye and have a good day!",
      "choices": [
        {
          "text": "Grazie, arrivederci!",
          "english": "Thanks, goodbye!",
          "isCorrect": True,
          "feedback": "Well done."
        },
        {
          "text": "Il resto è sbagliato.",
          "english": "The change is wrong.",
          "isCorrect": False,
          "feedback": "You already checked."
        },
        {
          "text": "Mi dia la borsa.",
          "english": "Give me the bag.",
          "isCorrect": False,
          "feedback": "You already have it."
        }
      ]
    }
  ],
  "understanding_prices": [
    {
      "id": "m6",
      "role": "host",
      "text": "Ha notato anche la nostra nuova collezione di portafogli in pelle?",
      "english": "Did you also notice our new collection of leather wallets?",
      "choices": [
        {
          "text": "Sì, li ho visti. Sono molto belli, ma non mi servono oggi.",
          "english": "Yes, I saw them. They are very beautiful, but I don't need them today.",
          "isCorrect": True,
          "feedback": "Polite but firm decline."
        },
        {
          "text": "Sì, voglio pagare il portafoglio in contanti.",
          "english": "Yes, I want to pay for the wallet in cash.",
          "isCorrect": False,
          "feedback": "You didn't decide to buy it."
        },
        {
          "text": "La borsa è rotta, voglio restituirla.",
          "english": "The bag is broken, I want to return it.",
          "isCorrect": False,
          "feedback": "You just bought it."
        }
      ]
    },
    {
      "id": "m7",
      "role": "host",
      "text": "Nessun problema. Le lascio un nostro biglietto da visita per la prossima volta.",
      "english": "No problem. I leave you our business card for next time.",
      "choices": [
        {
          "text": "Grazie, lo prendo volentieri. Magari torno il mese prossimo.",
          "english": "Thanks, I take it gladly. Maybe I'll come back next month.",
          "isCorrect": True,
          "feedback": "Good job accepting it politely."
        },
        {
          "text": "Questo biglietto del treno è scaduto.",
          "english": "This train ticket is expired.",
          "isCorrect": False,
          "feedback": "It's a business card, not a train ticket."
        },
        {
          "text": "Non voglio comprare la pelle oggi.",
          "english": "I don't want to buy leather today.",
          "isCorrect": False,
          "feedback": "You already declined."
        }
      ]
    },
    {
      "id": "m8",
      "role": "host",
      "text": "Saremo felici di rivederla. A proposito, abbiamo anche un sito online.",
      "english": "We will be happy to see you again. By the way, we also have an online website.",
      "choices": [
        {
          "text": "Ottimo, controllerò il sito se mi serve qualcos'altro in futuro.",
          "english": "Great, I'll check the website if I need anything else in the future.",
          "isCorrect": True,
          "feedback": "Perfect response."
        },
        {
          "text": "Il mio internet non funziona da due giorni.",
          "english": "My internet hasn't been working for two days.",
          "isCorrect": False,
          "feedback": "A bit overly sharing."
        },
        {
          "text": "Voglio pagare con il bancomat per questo sito.",
          "english": "I want to pay with a debit card for this site.",
          "isCorrect": False,
          "feedback": "You aren't buying anything online right now."
        }
      ]
    },
    {
      "id": "m9",
      "role": "host",
      "text": "Perfetto. Spero che la borsa le piaccia, è di ottima qualità.",
      "english": "Perfect. I hope you like the bag, it is of excellent quality.",
      "choices": [
        {
          "text": "Ne sono sicuro. Mi piace molto il materiale morbido e il colore.",
          "english": "I am sure of it. I really like the soft material and the color.",
          "isCorrect": True,
          "feedback": "A great compliment."
        },
        {
          "text": "Il colore è bruttissimo, ho cambiato idea.",
          "english": "The color is very ugly, I changed my mind.",
          "isCorrect": False,
          "feedback": "You just said it was an excellent choice."
        },
        {
          "text": "Non mi interessa la qualità, voglio solo il resto.",
          "english": "I don't care about the quality, I just want the change.",
          "isCorrect": False,
          "feedback": "Too aggressive."
        }
      ]
    },
    {
      "id": "m10",
      "role": "host",
      "text": "Sono contento. Allora arrivederci e grazie per l'acquisto!",
      "english": "I'm glad. Goodbye then and thank you for your purchase!",
      "choices": [
        {
          "text": "Grazie a lei. Arrivederci e buona serata!",
          "english": "Thank you. Goodbye and have a good evening!",
          "isCorrect": True,
          "feedback": "Great finish to the interaction."
        },
        {
          "text": "La polizia è già qui fuori.",
          "english": "The police is already outside here.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        },
        {
          "text": "Voglio comprare tutto il negozio.",
          "english": "I want to buy the whole shop.",
          "isCorrect": False,
          "feedback": "Irrelevant."
        }
      ]
    }
  ]
}

filepath = 'src/data/exports/miscellaneous/talking_about_money/conversations.json'

with open(filepath, 'r') as f:
    data = json.load(f)

for conv in data['conversations']:
    conv_id = conv['id']
    if conv_id in new_msgs:
        # Check if already appended to avoid duplicates
        if len(conv['messages']) < 10:
            conv['messages'].extend(new_msgs[conv_id])

with open(filepath, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Conversations extended.")
