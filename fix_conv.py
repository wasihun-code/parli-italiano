import json

data = {
  "conversations": [
    {
      "id": "buying_postcards",
      "title": "Buying Postcards",
      "messages": [
        {
          "role": "host",
          "text": "Buongiorno! Cerca qualcosa in particolare?",
          "english": "Good morning! Are you looking for anything in particular?"
        },
        {
          "role": "user",
          "text": "Sì, cerco delle cartoline della città.",
          "english": "Yes, I'm looking for some postcards of the city.",
          "choices": [
            {
              "text": "Sì, cerco delle cartoline della città.",
              "english": "Yes, I'm looking for some postcards of the city.",
              "isCorrect": True
            },
            {
              "text": "Sì, cerco delle calamite del museo.",
              "english": "Yes, I'm looking for some magnets of the museum.",
              "isCorrect": False
            },
            {
              "text": "Sì, cerco dei bracciali per la festa.",
              "english": "Yes, I'm looking for some bracelets for the party.",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Le cartoline sono qui. Ne abbiamo molte.",
          "english": "The postcards are here. We have many."
        },
        {
          "role": "user",
          "text": "Sono bellissime. Avete anche dei francobolli?",
          "english": "They are beautiful. Do you also have stamps?",
          "choices": [
            {
              "text": "Sono bellissime. Avete anche dei francobolli?",
              "english": "They are beautiful. Do you also have stamps?",
              "isCorrect": True
            },
            {
              "text": "Sono bellissimi. Avete anche dei portachiavi?",
              "english": "They are beautiful. Do you also have keychains?",
              "isCorrect": False
            },
            {
              "text": "Sono carissime. Avete anche dei fermacarte?",
              "english": "They are very expensive. Do you also have paperweights?",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Sì, certo. Quanti francobolli le servono?",
          "english": "Yes, of course. How many stamps do you need?"
        },
        {
          "role": "user",
          "text": "Prendo cinque cartoline e cinque francobolli, grazie.",
          "english": "I'll take five postcards and five stamps, thank you.",
          "choices": [
            {
              "text": "Prendo cinque cartoline e cinque francobolli, grazie.",
              "english": "I'll take five postcards and five stamps, thank you.",
              "isCorrect": True
            },
            {
              "text": "Prendo due calamite e tre portachiavi, grazie.",
              "english": "I'll take two magnets and three keychains, thank you.",
              "isCorrect": False
            },
            {
              "text": "Cerco quattro tazze e due piatti, grazie.",
              "english": "I'm looking for four cups and two plates, thank you.",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Perfetto. Desidera comprare anche un piccolo magnete?",
          "english": "Perfect. Do you want to buy a small magnet too?"
        },
        {
          "role": "user",
          "text": "No, per ora va bene così. Quanto costa?",
          "english": "No, that's fine for now. How much is it?",
          "choices": [
            {
              "text": "No, per ora va bene così. Quanto costa?",
              "english": "No, that's fine for now. How much is it?",
              "isCorrect": True
            },
            {
              "text": "Sì, per me va bene così. Quando chiudete?",
              "english": "Yes, that's fine for me. When do you close?",
              "isCorrect": False
            },
            {
              "text": "No, per oggi va bene così. Quanto spendo?",
              "english": "No, that's fine for today. How much do I spend?",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Sono sette euro e cinquanta centesimi in totale.",
          "english": "It is seven euros and fifty cents in total."
        },
        {
          "role": "user",
          "text": "Ecco a lei. Posso pagare con la carta?",
          "english": "Here you go. Can I pay with the card?",
          "choices": [
            {
              "text": "Ecco a lei. Posso pagare con la carta?",
              "english": "Here you go. Can I pay with the card?",
              "isCorrect": True
            },
            {
              "text": "Ecco a lei. Posso pagare con i contanti?",
              "english": "Here you go. Can I pay with cash?",
              "isCorrect": False
            },
            {
              "text": "Ecco a lei. Posso pagare con lo smartphone?",
              "english": "Here you go. Can I pay with the smartphone?",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Certamente, il pos è proprio qui. Grazie!",
          "english": "Certainly, the card reader is right here. Thank you!"
        }
      ]
    },
    {
      "id": "looking_for_gift",
      "title": "Looking for a Local Gift",
      "messages": [
        {
          "role": "host",
          "text": "Benvenuto! Posso aiutarla a trovare un regalo?",
          "english": "Welcome! Can I help you find a gift?"
        },
        {
          "role": "user",
          "text": "Sì, vorrei comprare un regalo per mia madre.",
          "english": "Yes, I would like to buy a gift for my mother.",
          "choices": [
            {
              "text": "Sì, vorrei comprare un regalo per mia madre.",
              "english": "Yes, I would like to buy a gift for my mother.",
              "isCorrect": True
            },
            {
              "text": "Sì, vorrei comprare un ricordo per mio padre.",
              "english": "Yes, I would like to buy a souvenir for my father.",
              "isCorrect": False
            },
            {
              "text": "Sì, vorrei trovare un souvenir per mio fratello.",
              "english": "Yes, I would like to find a souvenir for my brother.",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Che bella idea! Cerca un prodotto tipico locale?",
          "english": "What a beautiful idea! Are you looking for a typical local product?"
        },
        {
          "role": "user",
          "text": "Sì, un pezzo di artigianato tipico di questa città.",
          "english": "Yes, a typical craft piece from this city.",
          "choices": [
            {
              "text": "Sì, un pezzo di artigianato tipico di questa città.",
              "english": "Yes, a typical craft piece from this city.",
              "isCorrect": True
            },
            {
              "text": "Sì, un pezzo di ceramica tipica di questa zona.",
              "english": "Yes, a typical ceramic piece from this area.",
              "isCorrect": False
            },
            {
              "text": "Sì, un oggetto di vetro lavorato in questa regione.",
              "english": "Yes, a worked glass object from this region.",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Abbiamo questi bellissimi oggetti in legno lavorati a mano.",
          "english": "We have these beautiful handmade wooden objects."
        },
        {
          "role": "user",
          "text": "Molto belli. Quanto costa la scatola piccola?",
          "english": "Very beautiful. How much does the small box cost?",
          "choices": [
            {
              "text": "Molto belli. Quanto costa la scatola piccola?",
              "english": "Very beautiful. How much does the small box cost?",
              "isCorrect": True
            },
            {
              "text": "Molto belli. Quanto costa la statuina piccola?",
              "english": "Very beautiful. How much does the small figurine cost?",
              "isCorrect": False
            },
            {
              "text": "Molto belli. Quanto costa il piatto colorato?",
              "english": "Very beautiful. How much does the colored plate cost?",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "La scatola piccola costa quindici euro. È un affare.",
          "english": "The small box costs fifteen euros. It's a bargain."
        },
        {
          "role": "user",
          "text": "Va bene, prendo questa scatola. Può farmi un pacchetto regalo?",
          "english": "Alright, I'll take this box. Can you gift wrap it for me?",
          "choices": [
            {
              "text": "Va bene, prendo questa scatola. Può farmi un pacchetto regalo?",
              "english": "Alright, I'll take this box. Can you gift wrap it for me?",
              "isCorrect": True
            },
            {
              "text": "Va bene, guardo questa statua. Può fare uno sconto speciale?",
              "english": "Alright, I'll look at this statue. Can you do a special discount?",
              "isCorrect": False
            },
            {
              "text": "Va bene, prendo questa tazza. Può darmi un sacchetto di carta?",
              "english": "Alright, I'll take this cup. Can you give me a paper bag?",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Certamente, la confezione regalo è gratuita per i nostri clienti.",
          "english": "Certainly, gift wrapping is free for our customers."
        },
        {
          "role": "user",
          "text": "La ringrazio molto. Ecco i quindici euro.",
          "english": "Thank you very much. Here are the fifteen euros.",
          "choices": [
            {
              "text": "La ringrazio molto. Ecco i quindici euro.",
              "english": "Thank you very much. Here are the fifteen euros.",
              "isCorrect": True
            },
            {
              "text": "La ringrazio molto. Ecco i venti euro.",
              "english": "Thank you very much. Here are the twenty euros.",
              "isCorrect": False
            },
            {
              "text": "La ringrazio molto. Ecco la mia carta di credito.",
              "english": "Thank you very much. Here is my credit card.",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Grazie a lei e buona giornata!",
          "english": "Thank you and have a good day!"
        }
      ]
    },
    {
      "id": "asking_ceramics",
      "title": "Asking about Ceramics",
      "messages": [
        {
          "role": "host",
          "text": "Buongiorno signore. Cerca qualcosa per la casa?",
          "english": "Good morning sir. Are you looking for something for the house?"
        },
        {
          "role": "user",
          "text": "Buongiorno. Sto cercando dei piatti in ceramica tipica.",
          "english": "Good morning. I'm looking for some typical ceramic plates.",
          "choices": [
            {
              "text": "Buongiorno. Sto cercando dei piatti in ceramica tipica.",
              "english": "Good morning. I'm looking for some typical ceramic plates.",
              "isCorrect": True
            },
            {
              "text": "Buongiorno. Sto cercando dei vasi in ceramica bianca.",
              "english": "Good morning. I'm looking for some white ceramic vases.",
              "isCorrect": False
            },
            {
              "text": "Buongiorno. Sto guardando dei bicchieri in vetro soffiato.",
              "english": "Good morning. I'm looking at some blown glass cups.",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Ottima scelta. Le nostre ceramiche sono dipinte a mano.",
          "english": "Excellent choice. Our ceramics are hand-painted."
        },
        {
          "role": "user",
          "text": "Sono bellissimi. Avete anche dei bicchieri abbinati?",
          "english": "They are beautiful. Do you also have matching glasses?",
          "choices": [
            {
              "text": "Sono bellissimi. Avete anche dei bicchieri abbinati?",
              "english": "They are beautiful. Do you also have matching glasses?",
              "isCorrect": True
            },
            {
              "text": "Sono bellissimi. Avete anche delle tazze abbinate?",
              "english": "They are beautiful. Do you also have matching cups?",
              "isCorrect": False
            },
            {
              "text": "Sono bellissimi. Avete anche delle caraffe colorate?",
              "english": "They are beautiful. Do you also have colored pitchers?",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Certo, i bicchieri sono sullo scaffale lì in fondo.",
          "english": "Sure, the glasses are on the shelf back there."
        },
        {
          "role": "user",
          "text": "Li vedo. Quanto costa un set di due piatti?",
          "english": "I see them. How much does a set of two plates cost?",
          "choices": [
            {
              "text": "Li vedo. Quanto costa un set di due piatti?",
              "english": "I see them. How much does a set of two plates cost?",
              "isCorrect": True
            },
            {
              "text": "Li vedo. Quanto costa un set di quattro tazze?",
              "english": "I see them. How much does a set of four cups cost?",
              "isCorrect": False
            },
            {
              "text": "Li vedo. Quanto costa un vaso di piccole dimensioni?",
              "english": "I see them. How much does a small sized vase cost?",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Il set costa trenta euro. È un ottimo prezzo.",
          "english": "The set costs thirty euros. It's an excellent price."
        },
        {
          "role": "user",
          "text": "Va bene, prendo un set. Faccia attenzione, sono fragili.",
          "english": "Alright, I'll take a set. Be careful, they are fragile.",
          "choices": [
            {
              "text": "Va bene, prendo un set. Faccia attenzione, sono fragili.",
              "english": "Alright, I'll take a set. Be careful, they are fragile.",
              "isCorrect": True
            },
            {
              "text": "Va bene, prendo un piatto. Faccia attenzione, è delicato.",
              "english": "Alright, I'll take a plate. Be careful, it is delicate.",
              "isCorrect": False
            },
            {
              "text": "Va bene, prendo un vaso. Faccia attenzione, è pesante.",
              "english": "Alright, I'll take a vase. Be careful, it is heavy.",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Non si preoccupi. Li avvolgo nella carta protettiva.",
          "english": "Don't worry. I will wrap them in protective paper."
        },
        {
          "role": "user",
          "text": "Perfetto. Ecco trenta euro in contanti, grazie mille.",
          "english": "Perfect. Here are thirty euros in cash, thank you very much.",
          "choices": [
            {
              "text": "Perfetto. Ecco trenta euro in contanti, grazie mille.",
              "english": "Perfect. Here are thirty euros in cash, thank you very much.",
              "isCorrect": True
            },
            {
              "text": "Perfetto. Ecco cinquanta euro in contanti, grazie mille.",
              "english": "Perfect. Here are fifty euros in cash, thank you very much.",
              "isCorrect": False
            },
            {
              "text": "Perfetto. Ecco venti euro in contanti, grazie mille.",
              "english": "Perfect. Here are twenty euros in cash, thank you very much.",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Grazie a lei! Arrivederci.",
          "english": "Thank you! Goodbye."
        }
      ]
    },
    {
      "id": "paying_souvenirs",
      "title": "Paying for Souvenirs",
      "messages": [
        {
          "role": "host",
          "text": "Salve! Ha trovato tutto quello che cercava oggi?",
          "english": "Hello! Did you find everything you were looking for today?"
        },
        {
          "role": "user",
          "text": "Sì, grazie. Vorrei pagare questi tre magneti colorati.",
          "english": "Yes, thank you. I would like to pay for these three colored magnets.",
          "choices": [
            {
              "text": "Sì, grazie. Vorrei pagare questi tre magneti colorati.",
              "english": "Yes, thank you. I would like to pay for these three colored magnets.",
              "isCorrect": True
            },
            {
              "text": "Sì, grazie. Vorrei pagare queste due cartoline illustrate.",
              "english": "Yes, thank you. I would like to pay for these two illustrated postcards.",
              "isCorrect": False
            },
            {
              "text": "Sì, grazie. Vorrei comprare questo piccolo calendario locale.",
              "english": "Yes, thank you. I would like to buy this small local calendar.",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Benissimo. I magneti costano due euro l'uno.",
          "english": "Very well. The magnets cost two euros each."
        },
        {
          "role": "user",
          "text": "Quindi in totale sono sei euro. È corretto?",
          "english": "So in total it is six euros. Is that correct?",
          "choices": [
            {
              "text": "Quindi in totale sono sei euro. È corretto?",
              "english": "So in total it is six euros. Is that correct?",
              "isCorrect": True
            },
            {
              "text": "Quindi in totale sono dieci euro. È giusto?",
              "english": "So in total it is ten euros. Is that right?",
              "isCorrect": False
            },
            {
              "text": "Quindi in totale sono otto euro. È esatto?",
              "english": "So in total it is eight euros. Is that exact?",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Sì, esattamente sei euro. Paga in contanti o carta?",
          "english": "Yes, exactly six euros. Do you pay in cash or card?"
        },
        {
          "role": "user",
          "text": "Vorrei pagare con il bancomat, per favore.",
          "english": "I would like to pay with the debit card, please.",
          "choices": [
            {
              "text": "Vorrei pagare con il bancomat, per favore.",
              "english": "I would like to pay with the debit card, please.",
              "isCorrect": True
            },
            {
              "text": "Vorrei pagare in contanti, per favore.",
              "english": "I would like to pay in cash, please.",
              "isCorrect": False
            },
            {
              "text": "Vorrei pagare con la carta di credito, per favore.",
              "english": "I would like to pay with the credit card, please.",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Nessun problema. Può inserire la carta nel lettore verde.",
          "english": "No problem. You can insert the card into the green reader."
        },
        {
          "role": "user",
          "text": "Fatto. Devo inserire anche il codice segreto?",
          "english": "Done. Do I also need to insert the secret code?",
          "choices": [
            {
              "text": "Fatto. Devo inserire anche il codice segreto?",
              "english": "Done. Do I also need to insert the secret code?",
              "isCorrect": True
            },
            {
              "text": "Fatto. Devo firmare anche lo scontrino cartaceo?",
              "english": "Done. Do I also need to sign the paper receipt?",
              "isCorrect": False
            },
            {
              "text": "Fatto. Devo premere anche il tasto verde?",
              "english": "Done. Do I also need to press the green button?",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Sì, per gli importi piccoli a volte non serve, ma qui sì.",
          "english": "Yes, for small amounts sometimes it's not needed, but here yes."
        },
        {
          "role": "user",
          "text": "Ho inserito il codice. La transazione è accettata?",
          "english": "I inserted the code. Is the transaction accepted?",
          "choices": [
            {
              "text": "Ho inserito il codice. La transazione è accettata?",
              "english": "I inserted the code. Is the transaction accepted?",
              "isCorrect": True
            },
            {
              "text": "Ho inserito il codice. Il pagamento è confermato?",
              "english": "I inserted the code. Is the payment confirmed?",
              "isCorrect": False
            },
            {
              "text": "Ho ritirato la carta. Lo scontrino è stampato?",
              "english": "I withdrew the card. Is the receipt printed?",
              "isCorrect": False
            }
          ]
        },
        {
          "role": "host",
          "text": "Sì, tutto a posto. Ecco lo scontrino. Arrivederci!",
          "english": "Yes, all good. Here is the receipt. Goodbye!"
        }
      ]
    }
  ]
}

with open("./src/data/exports/shopping/souvenir_shop/conversations.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
