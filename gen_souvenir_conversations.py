import json

conversations = {
  "conversations": [
    {
      "id": "buying_postcards",
      "title": "Buying Postcards",
      "turns": [
        {
          "speaker": "host",
          "text": "Buongiorno! Cerca qualcosa in particolare?",
          "translation": "Good morning! Are you looking for anything in particular?"
        },
        {
          "speaker": "learner",
          "text": "Sì, cerco delle cartoline della città.",
          "translation": "Yes, I'm looking for some postcards of the city.",
          "choices": [
            {
              "text": "Sì, cerco delle cartoline della città.",
              "translation": "Yes, I'm looking for some postcards of the city.",
              "isCorrect": True
            },
            {
              "text": "Sì, mangio delle verdure dalla cucina.",
              "translation": "Yes, I eat some vegetables from the kitchen.",
              "isCorrect": False
            },
            {
              "text": "Sì, scrivo delle email per la scuola.",
              "translation": "Yes, I write some emails for the school.",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Le cartoline sono qui. Ne abbiamo molte.",
          "translation": "The postcards are here. We have many."
        },
        {
          "speaker": "learner",
          "text": "Sono bellissime. Avete anche dei francobolli?",
          "translation": "They are beautiful. Do you also have stamps?",
          "choices": [
            {
              "text": "Sono bellissime. Avete anche dei francobolli?",
              "translation": "They are beautiful. Do you also have stamps?",
              "isCorrect": True
            },
            {
              "text": "Sono divertenti. Avete anche dei termosifoni?",
              "translation": "They are fun. Do you also have radiators?",
              "isCorrect": False
            },
            {
              "text": "Sono grandissime. Avete anche dei portafogli?",
              "translation": "They are huge. Do you also have wallets?",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Sì, certo. Quanti francobolli le servono?",
          "translation": "Yes, of course. How many stamps do you need?"
        },
        {
          "speaker": "learner",
          "text": "Prendo cinque cartoline e cinque francobolli, grazie.",
          "translation": "I'll take five postcards and five stamps, thank you.",
          "choices": [
            {
              "text": "Prendo cinque cartoline e cinque francobolli, grazie.",
              "translation": "I'll take five postcards and five stamps, thank you.",
              "isCorrect": True
            },
            {
              "text": "Compro cinque magliette e cinque pantaloncini, grazie.",
              "translation": "I buy five t-shirts and five shorts, thank you.",
              "isCorrect": False
            },
            {
              "text": "Mangio cinque fragoline e cinque cioccolatini, grazie.",
              "translation": "I eat five strawberries and five chocolates, thank you.",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Perfetto. Desidera comprare anche un piccolo magnete?",
          "translation": "Perfect. Do you want to buy a small magnet too?"
        },
        {
          "speaker": "learner",
          "text": "No, per ora va bene così. Quanto costa?",
          "translation": "No, that's fine for now. How much is it?",
          "choices": [
            {
              "text": "No, per ora va bene così. Quanto costa?",
              "translation": "No, that's fine for now. How much is it?",
              "isCorrect": True
            },
            {
              "text": "Sì, per lui va bene così. Quando balla?",
              "translation": "Yes, it's fine for him. When does he dance?",
              "isCorrect": False
            },
            {
              "text": "No, per voi va bene così. Quanta pasta?",
              "translation": "No, it's fine for you. How much pasta?",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Sono sette euro e cinquanta centesimi in totale.",
          "translation": "It is seven euros and fifty cents in total."
        },
        {
          "speaker": "learner",
          "text": "Ecco a lei. Posso pagare con la carta?",
          "translation": "Here you go. Can I pay with the card?",
          "choices": [
            {
              "text": "Ecco a lei. Posso pagare con la carta?",
              "translation": "Here you go. Can I pay with the card?",
              "isCorrect": True
            },
            {
              "text": "Ecco a lei. Posso giocare con la palla?",
              "translation": "Here you go. Can I play with the ball?",
              "isCorrect": False
            },
            {
              "text": "Ecco a lei. Posso dormire con la porta?",
              "translation": "Here you go. Can I sleep with the door?",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Certamente, il pos è proprio qui. Grazie!",
          "translation": "Certainly, the card reader is right here. Thank you!"
        }
      ]
    },
    {
      "id": "looking_for_gift",
      "title": "Looking for a Local Gift",
      "turns": [
        {
          "speaker": "host",
          "text": "Benvenuto! Posso aiutarla a trovare un regalo?",
          "translation": "Welcome! Can I help you find a gift?"
        },
        {
          "speaker": "learner",
          "text": "Sì, vorrei comprare un regalo per mia madre.",
          "translation": "Yes, I would like to buy a gift for my mother.",
          "choices": [
            {
              "text": "Sì, vorrei comprare un regalo per mia madre.",
              "translation": "Yes, I would like to buy a gift for my mother.",
              "isCorrect": True
            },
            {
              "text": "No, vorrei mangiare un panino con mio padre.",
              "translation": "No, I would like to eat a sandwich with my father.",
              "isCorrect": False
            },
            {
              "text": "Sì, dovrei studiare un libro per mia zia.",
              "translation": "Yes, I should study a book for my aunt.",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Che bella idea! Cerca un prodotto tipico locale?",
          "translation": "What a beautiful idea! Are you looking for a typical local product?"
        },
        {
          "speaker": "learner",
          "text": "Sì, un pezzo di artigianato tipico di questa città.",
          "translation": "Yes, a typical craft piece from this city.",
          "choices": [
            {
              "text": "Sì, un pezzo di artigianato tipico di questa città.",
              "translation": "Yes, a typical craft piece from this city.",
              "isCorrect": True
            },
            {
              "text": "Sì, un pezzo di cioccolata amara di quella nonna.",
              "translation": "Yes, a piece of bitter chocolate from that grandmother.",
              "isCorrect": False
            },
            {
              "text": "No, un chilo di formaggio fresco da questo prato.",
              "translation": "No, a kilo of fresh cheese from this meadow.",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Abbiamo questi bellissimi oggetti in legno lavorati a mano.",
          "translation": "We have these beautiful handmade wooden objects."
        },
        {
          "speaker": "learner",
          "text": "Molto belli. Quanto costa la scatola piccola?",
          "translation": "Very beautiful. How much does the small box cost?",
          "choices": [
            {
              "text": "Molto belli. Quanto costa la scatola piccola?",
              "translation": "Very beautiful. How much does the small box cost?",
              "isCorrect": True
            },
            {
              "text": "Molto lenti. Quanto corre la macchina bianca?",
              "translation": "Very slow. How fast does the white car run?",
              "isCorrect": False
            },
            {
              "text": "Molto bassi. Quanto salta la ragazza bionda?",
              "translation": "Very short. How high does the blonde girl jump?",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "La scatola piccola costa quindici euro. È un affare.",
          "translation": "The small box costs fifteen euros. It's a bargain."
        },
        {
          "speaker": "learner",
          "text": "Va bene, prendo questa scatola. Le faccio un pacchetto regalo?",
          "translation": "Alright, I'll take this box. Can you wrap it?",
          "choices": [
            {
              "text": "Va bene, prendo questa scatola. Le faccio un pacchetto regalo?",
              "translation": "Alright, I'll take this box. Can you wrap it?",
              "isCorrect": True
            },
            {
              "text": "Va male, lascio questa bottiglia. Mi mangio un biscotto dolce?",
              "translation": "Alright, I'll leave this bottle. Do I eat a sweet biscuit?",
              "isCorrect": False
            },
            {
              "text": "Va bene, guardo questa finestra. Ci metto un fazzoletto pulito?",
              "translation": "Alright, I'll look at this window. Do I put a clean tissue?",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Certamente, la confezione regalo è gratuita per i nostri clienti.",
          "translation": "Certainly, gift wrapping is free for our customers."
        },
        {
          "speaker": "learner",
          "text": "La ringrazio molto. Ecco i quindici euro.",
          "translation": "Thank you very much. Here are the fifteen euros.",
          "choices": [
            {
              "text": "La ringrazio molto. Ecco i quindici euro.",
              "translation": "Thank you very much. Here are the fifteen euros.",
              "isCorrect": True
            },
            {
              "text": "La saluto presto. Ecco le quindici mele.",
              "translation": "I greet you soon. Here are the fifteen apples.",
              "isCorrect": False
            },
            {
              "text": "La chiamo spesso. Ecco i quindici cani.",
              "translation": "I call you often. Here are the fifteen dogs.",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Grazie a lei e buona giornata!",
          "translation": "Thank you and have a good day!"
        }
      ]
    },
    {
      "id": "asking_ceramics",
      "title": "Asking about Ceramics",
      "turns": [
        {
          "speaker": "host",
          "text": "Buongiorno signore. Cerca qualcosa per la casa?",
          "translation": "Good morning sir. Are you looking for something for the house?"
        },
        {
          "speaker": "learner",
          "text": "Buongiorno. Sto cercando dei piatti in ceramica tipica.",
          "translation": "Good morning. I'm looking for some typical ceramic plates.",
          "choices": [
            {
              "text": "Buongiorno. Sto cercando dei piatti in ceramica tipica.",
              "translation": "Good morning. I'm looking for some typical ceramic plates.",
              "isCorrect": True
            },
            {
              "text": "Buonasera. Sto mangiando dei frutti in campagna aperta.",
              "translation": "Good evening. I'm eating some fruits in the open countryside.",
              "isCorrect": False
            },
            {
              "text": "Buongiorno. Sto ascoltando dei brani in discoteca locale.",
              "translation": "Good morning. I'm listening to some tracks in the local disco.",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Ottima scelta. Le nostre ceramiche sono dipinte a mano.",
          "translation": "Excellent choice. Our ceramics are hand-painted."
        },
        {
          "speaker": "learner",
          "text": "Sono bellissimi. Avete anche dei bicchieri abbinati?",
          "translation": "They are beautiful. Do you also have matching glasses?",
          "choices": [
            {
              "text": "Sono bellissimi. Avete anche dei bicchieri abbinati?",
              "translation": "They are beautiful. Do you also have matching glasses?",
              "isCorrect": True
            },
            {
              "text": "Sono grandissimi. Volete anche dei quaderni colorati?",
              "translation": "They are huge. Do you also want colored notebooks?",
              "isCorrect": False
            },
            {
              "text": "Sono leggerissimi. Potete anche dei tappeti rovinati?",
              "translation": "They are very light. Can you also some ruined carpets?",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Certo, i bicchieri sono sullo scaffale lì in fondo.",
          "translation": "Sure, the glasses are on the shelf back there."
        },
        {
          "speaker": "learner",
          "text": "Li vedo. Quanto costa un set di due piatti?",
          "translation": "I see them. How much does a set of two plates cost?",
          "choices": [
            {
              "text": "Li vedo. Quanto costa un set di due piatti?",
              "translation": "I see them. How much does a set of two plates cost?",
              "isCorrect": True
            },
            {
              "text": "Li bevo. Quando dorme un re di due regni?",
              "translation": "I drink them. When does a king of two kingdoms sleep?",
              "isCorrect": False
            },
            {
              "text": "Li lavo. Perché canta un coro di due voci?",
              "translation": "I wash them. Why does a choir of two voices sing?",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Il set costa trenta euro. È un ottimo prezzo.",
          "translation": "The set costs thirty euros. It's an excellent price."
        },
        {
          "speaker": "learner",
          "text": "Va bene, prendo un set. Faccia attenzione, sono fragili.",
          "translation": "Alright, I'll take a set. Be careful, they are fragile.",
          "choices": [
            {
              "text": "Va bene, prendo un set. Faccia attenzione, sono fragili.",
              "translation": "Alright, I'll take a set. Be careful, they are fragile.",
              "isCorrect": True
            },
            {
              "text": "Va male, lascio un dvd. Mangia peperone, sono leggeri.",
              "translation": "Alright, I'll leave a dvd. Eat bell pepper, they are light.",
              "isCorrect": False
            },
            {
              "text": "Va bene, bevo un the. Pensa colazione, sono difficili.",
              "translation": "Alright, I'll drink a tea. Think breakfast, they are difficult.",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Non si preoccupi. Li avvolgo nella carta protettiva.",
          "translation": "Don't worry. I will wrap them in protective paper."
        },
        {
          "speaker": "learner",
          "text": "Perfetto. Ecco trenta euro in contanti, grazie mille.",
          "translation": "Perfect. Here are thirty euros in cash, thank you very much.",
          "choices": [
            {
              "text": "Perfetto. Ecco trenta euro in contanti, grazie mille.",
              "translation": "Perfect. Here are thirty euros in cash, thank you very much.",
              "isCorrect": True
            },
            {
              "text": "Perfetto. Ecco trenta cani in giardino, ciao presto.",
              "translation": "Perfect. Here are thirty dogs in the garden, bye soon.",
              "isCorrect": False
            },
            {
              "text": "Perfetto. Ecco trenta libri in biblioteca, molto bene.",
              "translation": "Perfect. Here are thirty books in the library, very well.",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Grazie a lei! Arrivederci.",
          "translation": "Thank you! Goodbye."
        }
      ]
    },
    {
      "id": "paying_souvenirs",
      "title": "Paying for Souvenirs",
      "turns": [
        {
          "speaker": "host",
          "text": "Salve! Ha trovato tutto quello che cercava oggi?",
          "translation": "Hello! Did you find everything you were looking for today?"
        },
        {
          "speaker": "learner",
          "text": "Sì, grazie. Vorrei pagare questi tre magneti colorati.",
          "translation": "Yes, thank you. I would like to pay for these three colored magnets.",
          "choices": [
            {
              "text": "Sì, grazie. Vorrei pagare questi tre magneti colorati.",
              "translation": "Yes, thank you. I would like to pay for these three colored magnets.",
              "isCorrect": True
            },
            {
              "text": "No, prego. Potrei mangiare questi tre biscotti salati.",
              "translation": "No, you're welcome. I could eat these three salty biscuits.",
              "isCorrect": False
            },
            {
              "text": "Sì, grazie. Dovrei lavare questi tre pantaloni vecchi.",
              "translation": "Yes, thank you. I should wash these three old pants.",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Benissimo. I magneti costano due euro l'uno.",
          "translation": "Very well. The magnets cost two euros each."
        },
        {
          "speaker": "learner",
          "text": "Quindi in totale sono sei euro. È corretto?",
          "translation": "So in total it is six euros. Is that correct?",
          "choices": [
            {
              "text": "Quindi in totale sono sei euro. È corretto?",
              "translation": "So in total it is six euros. Is that correct?",
              "isCorrect": True
            },
            {
              "text": "Quindi in valigia sono sei chili. È pensante?",
              "translation": "So in the suitcase it's six kilos. Is it heavy?",
              "isCorrect": False
            },
            {
              "text": "Quindi in piscina sono sei metri. È profondo?",
              "translation": "So in the pool it's six meters. Is it deep?",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Sì, esattamente sei euro. Paga in contanti o carta?",
          "translation": "Yes, exactly six euros. Do you pay in cash or card?"
        },
        {
          "speaker": "learner",
          "text": "Vorrei pagare con il bancomat, per favore.",
          "translation": "I would like to pay with the debit card, please.",
          "choices": [
            {
              "text": "Vorrei pagare con il bancomat, per favore.",
              "translation": "I would like to pay with the debit card, please.",
              "isCorrect": True
            },
            {
              "text": "Vorrei dormire con il gattino, per favore.",
              "translation": "I would like to sleep with the kitten, please.",
              "isCorrect": False
            },
            {
              "text": "Vorrei ballare con il cameriere, per favore.",
              "translation": "I would like to dance with the waiter, please.",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Nessun problema. Può inserire la carta nel lettore verde.",
          "translation": "No problem. You can insert the card into the green reader."
        },
        {
          "speaker": "learner",
          "text": "Fatto. Devo inserire anche il codice segreto?",
          "translation": "Done. Do I also need to insert the secret code?",
          "choices": [
            {
              "text": "Fatto. Devo inserire anche il codice segreto?",
              "translation": "Done. Do I also need to insert the secret code?",
              "isCorrect": True
            },
            {
              "text": "Cotto. Devo cucinare anche il pollo arrosto?",
              "translation": "Cooked. Do I also need to cook the roast chicken?",
              "isCorrect": False
            },
            {
              "text": "Rotto. Devo buttare anche il piatto sporco?",
              "translation": "Broken. Do I also need to throw the dirty plate?",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Sì, per gli importi piccoli a volte non serve, ma qui sì.",
          "translation": "Yes, for small amounts sometimes it's not needed, but here yes."
        },
        {
          "speaker": "learner",
          "text": "Ho inserito il codice. La transazione è accettata?",
          "translation": "I inserted the code. Is the transaction accepted?",
          "choices": [
            {
              "text": "Ho inserito il codice. La transazione è accettata?",
              "translation": "I inserted the code. Is the transaction accepted?",
              "isCorrect": True
            },
            {
              "text": "Ho mangiato il panino. La digestione è completata?",
              "translation": "I ate the sandwich. Is digestion completed?",
              "isCorrect": False
            },
            {
              "text": "Ho guardato il film. La televisione è spenta?",
              "translation": "I watched the movie. Is the television off?",
              "isCorrect": False
            }
          ]
        },
        {
          "speaker": "host",
          "text": "Sì, tutto a posto. Ecco lo scontrino. Arrivederci!",
          "translation": "Yes, all good. Here is the receipt. Goodbye!"
        }
      ]
    }
  ]
}

def validate_lengths(convs):
    for c in convs["conversations"]:
        for t in c["turns"]:
            if "choices" in t:
                correct = next(ch for ch in t["choices"] if ch["isCorrect"])
                cl = len(correct["text"])
                for ch in t["choices"]:
                    dl = len(ch["text"])
                    diff = abs(cl - dl) / max(cl, 1)
                    if diff > 0.4:
                        print(f"Warning: Distractor length difference > 40% in {c['id']}: '{ch['text']}' (len {dl} vs correct {cl})")

validate_lengths(conversations)

with open("src/data/exports/shopping/souvenir_shop/conversations.json", "w") as f:
    json.dump(conversations, f, indent=2, ensure_ascii=False)
print("Saved conversations.json")
