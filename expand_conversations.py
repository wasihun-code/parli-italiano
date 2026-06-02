import json

data = {
    "scenarioId": 47,
    "conversations": [
        {
            "id": "buying_smartphone",
            "title": "Buying a Smartphone",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Buongiorno! Posso aiutarla a scegliere un cellulare?",
                    "english": "Good morning! Can I help you choose a smartphone?",
                    "choices": [
                        {"text": "Sì, vorrei un nuovo cellulare.", "english": "Yes, I would like a new smartphone.", "isCorrect": True},
                        {"text": "No, cerco un vecchio computer.", "english": "No, I am looking for an old computer.", "isCorrect": False},
                        {"text": "Sì, voglio un tablet grande.", "english": "Yes, I want a large tablet.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Abbiamo questo modello. Le piace lo schermo?",
                    "english": "We have this model. Do you like the screen?",
                    "choices": [
                        {"text": "Sì, lo schermo è molto grande.", "english": "Yes, the screen is very big.", "isCorrect": True},
                        {"text": "No, la tastiera è troppo piccola.", "english": "No, the keyboard is too small.", "isCorrect": False},
                        {"text": "Sì, il mouse è veloce.", "english": "Yes, the mouse is fast.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Ha centoventi gigabyte di memoria. È sufficiente?",
                    "english": "It has one hundred twenty gigabytes of memory. Is it enough?",
                    "choices": [
                        {"text": "Sì, la memoria è perfetta per me.", "english": "Yes, the memory is perfect for me.", "isCorrect": True},
                        {"text": "No, la batteria è scarica.", "english": "No, the battery is dead.", "isCorrect": False},
                        {"text": "Sì, il volume è alto.", "english": "Yes, the volume is high.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Il prezzo è di seicento euro. Cosa ne pensa?",
                    "english": "The price is six hundred euros. What do you think?",
                    "choices": [
                        {"text": "È un buon prezzo, lo prendo.", "english": "It is a good price, I'll take it.", "isCorrect": True},
                        {"text": "È un brutto film, non lo vedo.", "english": "It's a bad movie, I'm not watching it.", "isCorrect": False},
                        {"text": "È un libro caro, non lo leggo.", "english": "It's an expensive book, I'm not reading it.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Ottima scelta! Serve anche un caricabatterie?",
                    "english": "Great choice! Do you also need a charger?",
                    "choices": [
                        {"text": "Sì, mi serve un caricabatterie rapido.", "english": "Yes, I need a fast charger.", "isCorrect": True},
                        {"text": "No, cerco un ombrello nero.", "english": "No, I am looking for a black umbrella.", "isCorrect": False},
                        {"text": "Sì, vorrei un caffè caldo.", "english": "Yes, I would like a hot coffee.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Lo vuole di colore nero o blu?",
                    "english": "Do you want it in black or blue?",
                    "choices": [
                        {"text": "Lo preferisco nero, grazie.", "english": "I prefer it black, thank you.", "isCorrect": True},
                        {"text": "Lo voglio dolce, per favore.", "english": "I want it sweet, please.", "isCorrect": False},
                        {"text": "Lo vedo rotto, mi dispiace.", "english": "I see it broken, I'm sorry.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "La fotocamera è ottima. Le serve una scheda di memoria?",
                    "english": "The camera is excellent. Do you need a memory card?",
                    "choices": [
                        {"text": "No, la memoria interna basta.", "english": "No, the internal memory is enough.", "isCorrect": True},
                        {"text": "Sì, la cena è pronta.", "english": "Yes, dinner is ready.", "isCorrect": False},
                        {"text": "No, il treno parte ora.", "english": "No, the train is leaving now.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Vuole anche una custodia protettiva?",
                    "english": "Do you also want a protective case?",
                    "choices": [
                        {"text": "Sì, ne vorrei una trasparente.", "english": "Yes, I would like a transparent one.", "isCorrect": True},
                        {"text": "No, vorrei una mela rossa.", "english": "No, I would like a red apple.", "isCorrect": False},
                        {"text": "Sì, cerco una sedia comoda.", "english": "Yes, I am looking for a comfortable chair.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Paga in contanti o con carta di credito?",
                    "english": "Are you paying in cash or with a credit card?",
                    "choices": [
                        {"text": "Pago con la carta di credito.", "english": "I'm paying with the credit card.", "isCorrect": True},
                        {"text": "Mangio con la forchetta.", "english": "I'm eating with the fork.", "isCorrect": False},
                        {"text": "Vado con l'autobus.", "english": "I'm going by bus.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Ecco lo scontrino. Serve una busta?",
                    "english": "Here is the receipt. Do you need a bag?",
                    "choices": [
                        {"text": "No grazie, ho già una borsa.", "english": "No thanks, I already have a bag.", "isCorrect": True},
                        {"text": "Sì grazie, ho molta fame.", "english": "Yes thanks, I am very hungry.", "isCorrect": False},
                        {"text": "No grazie, il tempo è brutto.", "english": "No thanks, the weather is bad.", "isCorrect": False}
                    ]
                }
            ]
        },
        {
            "id": "choosing_headphones",
            "title": "Choosing Headphones",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Salve! Cerca delle cuffie per la musica?",
                    "english": "Hello! Are you looking for headphones for music?",
                    "choices": [
                        {"text": "Sì, vorrei delle cuffie senza fili.", "english": "Yes, I would like wireless headphones.", "isCorrect": True},
                        {"text": "No, voglio dei guanti rossi.", "english": "No, I want red gloves.", "isCorrect": False},
                        {"text": "Sì, cerco delle scarpe nuove.", "english": "Yes, I am looking for new shoes.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Queste cuffie hanno una batteria molto lunga.",
                    "english": "These headphones have a very long battery life.",
                    "choices": [
                        {"text": "Ottimo, la batteria è molto importante.", "english": "Great, the battery is very important.", "isCorrect": True},
                        {"text": "Bello, il mare è calmo.", "english": "Nice, the sea is calm.", "isCorrect": False},
                        {"text": "Bene, la pizza è calda.", "english": "Good, the pizza is hot.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Durano trenta ore. Sono molto comode.",
                    "english": "They last thirty hours. They are very comfortable.",
                    "choices": [
                        {"text": "Posso provare queste cuffie?", "english": "Can I try these headphones?", "isCorrect": True},
                        {"text": "Posso aprire questa finestra?", "english": "Can I open this window?", "isCorrect": False},
                        {"text": "Posso chiamare un taxi?", "english": "Can I call a taxi?", "isCorrect": False}
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Certo! Il suono è molto chiaro. Le piacciono?",
                    "english": "Of course! The sound is very clear. Do you like them?",
                    "choices": [
                        {"text": "Sì, il suono è fantastico.", "english": "Yes, the sound is fantastic.", "isCorrect": True},
                        {"text": "No, il treno è in ritardo.", "english": "No, the train is late.", "isCorrect": False},
                        {"text": "Sì, il caffè è amaro.", "english": "Yes, the coffee is bitter.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Costano cento euro. Sono in promozione.",
                    "english": "They cost one hundred euros. They are on promotion.",
                    "choices": [
                        {"text": "Le prendo, mi piacciono molto.", "english": "I'll take them, I like them a lot.", "isCorrect": True},
                        {"text": "Le lavo, sono molto sporche.", "english": "I wash them, they are very dirty.", "isCorrect": False},
                        {"text": "Le vedo, sono molto lontane.", "english": "I see them, they are very far.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Preferisce il modello bianco o quello nero?",
                    "english": "Do you prefer the white model or the black one?",
                    "choices": [
                        {"text": "Prendo il modello nero, grazie.", "english": "I'll take the black model, thank you.", "isCorrect": True},
                        {"text": "Prendo il treno delle otto.", "english": "I'll take the eight o'clock train.", "isCorrect": False},
                        {"text": "Prendo un gelato alla crema.", "english": "I'll take a cream gelato.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "Hanno anche la riduzione del rumore.",
                    "english": "They also have noise reduction.",
                    "choices": [
                        {"text": "Perfetto per viaggiare in aereo.", "english": "Perfect for traveling by plane.", "isCorrect": True},
                        {"text": "Ottimo per cucinare la pasta.", "english": "Great for cooking pasta.", "isCorrect": False},
                        {"text": "Bene per dormire in giardino.", "english": "Good for sleeping in the garden.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "C'è anche un cavo per usarle con il filo.",
                    "english": "There is also a cable to use them with the wire.",
                    "choices": [
                        {"text": "Utile se la batteria finisce.", "english": "Useful if the battery runs out.", "isCorrect": True},
                        {"text": "Bello se il sole sorge.", "english": "Nice if the sun rises.", "isCorrect": False},
                        {"text": "Male se la pioggia cade.", "english": "Bad if the rain falls.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Le serve un adattatore per l'aereo?",
                    "english": "Do you need an adapter for the plane?",
                    "choices": [
                        {"text": "No grazie, ne ho già uno.", "english": "No thanks, I already have one.", "isCorrect": True},
                        {"text": "Sì grazie, ho molta sete.", "english": "Yes thanks, I am very thirsty.", "isCorrect": False},
                        {"text": "No grazie, cerco un libro.", "english": "No thanks, I'm looking for a book.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Vuole fare un'assicurazione contro i danni?",
                    "english": "Do you want to take out insurance against damage?",
                    "choices": [
                        {"text": "No, per ora non mi serve.", "english": "No, for now I don't need it.", "isCorrect": True},
                        {"text": "Sì, per ora non mangio.", "english": "Yes, for now I'm not eating.", "isCorrect": False},
                        {"text": "No, per ora non dormo.", "english": "No, for now I'm not sleeping.", "isCorrect": False}
                    ]
                }
            ]
        },
        {
            "id": "laptop_specs",
            "title": "Laptop Specs",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Buongiorno. Cerca un computer per lavorare?",
                    "english": "Good morning. Are you looking for a computer for work?",
                    "choices": [
                        {"text": "Sì, vorrei un computer portatile.", "english": "Yes, I would like a laptop computer.", "isCorrect": True},
                        {"text": "No, voglio un cappotto caldo.", "english": "No, I want a warm coat.", "isCorrect": False},
                        {"text": "Sì, cerco un cane piccolo.", "english": "Yes, I am looking for a small dog.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Questo modello ha sedici gigabyte di memoria.",
                    "english": "This model has sixteen gigabytes of memory.",
                    "choices": [
                        {"text": "Sedici gigabyte vanno bene per me.", "english": "Sixteen gigabytes are fine for me.", "isCorrect": True},
                        {"text": "Dieci euro sono troppi.", "english": "Ten euros are too many.", "isCorrect": False},
                        {"text": "Due gatti sono felici.", "english": "Two cats are happy.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "La batteria dura circa dieci ore.",
                    "english": "The battery lasts about ten hours.",
                    "choices": [
                        {"text": "Dieci ore sono ottime per il lavoro.", "english": "Ten hours are great for work.", "isCorrect": True},
                        {"text": "Due ore sono poche per dormire.", "english": "Two hours are few for sleeping.", "isCorrect": False},
                        {"text": "Tre ore sono lunghe per la cena.", "english": "Three hours are long for dinner.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Il computer è molto leggero e sottile.",
                    "english": "The computer is very light and thin.",
                    "choices": [
                        {"text": "Perfetto, lo porto spesso in borsa.", "english": "Perfect, I often carry it in my bag.", "isCorrect": True},
                        {"text": "Ottimo, lo mangio sempre a casa.", "english": "Great, I always eat it at home.", "isCorrect": False},
                        {"text": "Bene, lo vedo spesso al parco.", "english": "Good, I often see it at the park.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Sì, costa novecento euro compresa l'IVA.",
                    "english": "Yes, it costs nine hundred euros including VAT.",
                    "choices": [
                        {"text": "Lo compro, mi serve per l'ufficio.", "english": "I'll buy it, I need it for the office.", "isCorrect": True},
                        {"text": "Lo mangio, mi serve per la cena.", "english": "I eat it, I need it for dinner.", "isCorrect": False},
                        {"text": "Lo leggo, mi serve per lo studio.", "english": "I read it, I need it for studying.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Il sistema operativo è già installato.",
                    "english": "The operating system is already installed.",
                    "choices": [
                        {"text": "Ottimo, così è pronto all'uso.", "english": "Great, so it's ready for use.", "isCorrect": True},
                        {"text": "Bello, così è pronto per il mare.", "english": "Nice, so it's ready for the sea.", "isCorrect": False},
                        {"text": "Male, così è pronto per la pioggia.", "english": "Bad, so it's ready for the rain.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "Ha anche tre porte USB e una porta HDMI.",
                    "english": "It also has three USB ports and one HDMI port.",
                    "choices": [
                        {"text": "Mi servono per collegare il mouse.", "english": "I need them to connect the mouse.", "isCorrect": True},
                        {"text": "Mi servono per cucinare la carne.", "english": "I need them to cook the meat.", "isCorrect": False},
                        {"text": "Mi servono per lavare i vestiti.", "english": "I need them to wash the clothes.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Vuole anche un mouse senza fili?",
                    "english": "Do you also want a wireless mouse?",
                    "choices": [
                        {"text": "Sì, ne vorrei uno piccolo.", "english": "Yes, I would like a small one.", "isCorrect": True},
                        {"text": "No, vorrei un gelato grande.", "english": "No, I would like a large gelato.", "isCorrect": False},
                        {"text": "Sì, cerco un ombrello verde.", "english": "Yes, I'm looking for a green umbrella.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "La tastiera è retroilluminata, le piace?",
                    "english": "The keyboard is backlit, do you like it?",
                    "choices": [
                        {"text": "Sì, è utile per scrivere di sera.", "english": "Yes, it is useful for writing in the evening.", "isCorrect": True},
                        {"text": "No, è inutile per correre nel parco.", "english": "No, it is useless for running in the park.", "isCorrect": False},
                        {"text": "Sì, è comodo per dormire a letto.", "english": "Yes, it is comfortable for sleeping in bed.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Possiamo preparare il pacco in dieci minuti.",
                    "english": "We can prepare the package in ten minutes.",
                    "choices": [
                        {"text": "Perfetto, aspetto qui in negozio.", "english": "Perfect, I'll wait here in the store.", "isCorrect": True},
                        {"text": "Bene, vado a fare il bagno.", "english": "Good, I'm going for a swim.", "isCorrect": False},
                        {"text": "Ottimo, vado a dormire ora.", "english": "Great, I'm going to sleep now.", "isCorrect": False}
                    ]
                }
            ]
        },
        {
            "id": "asking_warranty",
            "title": "Asking about Warranty",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Desidera comprare questo computer?",
                    "english": "Do you want to buy this computer?",
                    "choices": [
                        {"text": "Sì, ma vorrei informazioni sulla garanzia.", "english": "Yes, but I would like information about the warranty.", "isCorrect": True},
                        {"text": "No, ma cerco informazioni sulla pioggia.", "english": "No, but I am looking for information about the rain.", "isCorrect": False},
                        {"text": "Sì, ma voglio informazioni sulla pizza.", "english": "Yes, but I want information about the pizza.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "La garanzia standard è di due anni.",
                    "english": "The standard warranty is two years.",
                    "choices": [
                        {"text": "Due anni sono obbligatori per legge?", "english": "Are two years mandatory by law?", "isCorrect": True},
                        {"text": "Due anni sono troppi per un film?", "english": "Are two years too many for a movie?", "isCorrect": False},
                        {"text": "Due ore sono lunghe per un pranzo?", "english": "Are two hours long for a lunch?", "isCorrect": False}
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Sì, la batteria è coperta per un anno.",
                    "english": "Yes, the battery is covered for one year.",
                    "choices": [
                        {"text": "Bene, allora lo prendo.", "english": "Good, then I'll take it.", "isCorrect": True},
                        {"text": "Male, allora lo butto.", "english": "Badly, then I'll throw it away.", "isCorrect": False},
                        {"text": "Forse, allora lo cerco.", "english": "Maybe, then I'll look for it.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Lo schermo ha due anni di protezione.",
                    "english": "The screen has two years of protection.",
                    "choices": [
                        {"text": "Perfetto, questo mi rassicura molto.", "english": "Perfect, this reassures me a lot.", "isCorrect": True},
                        {"text": "Ottimo, questo mi stanca molto.", "english": "Great, this tires me a lot.", "isCorrect": False},
                        {"text": "Bene, questo mi ferma ora.", "english": "Good, this stops me now.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "La garanzia vale se ha lo scontrino.",
                    "english": "The warranty is valid if you have the receipt.",
                    "choices": [
                        {"text": "Va bene, lo metto in un posto sicuro.", "english": "Alright, I'll put it in a safe place.", "isCorrect": True},
                        {"text": "Vado via, lo porto al parco giochi.", "english": "I'm leaving, I'll take it to the playground.", "isCorrect": False},
                        {"text": "Sto qui, lo mangio subito.", "english": "I'm staying here, I'll eat it immediately.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Copre i difetti di fabbrica, non i danni accidentali.",
                    "english": "It covers manufacturing defects, not accidental damage.",
                    "choices": [
                        {"text": "Capisco, quindi se cade non è coperto.", "english": "I see, so if it falls it is not covered.", "isCorrect": True},
                        {"text": "Capisco, quindi se mangio non è buono.", "english": "I see, so if I eat it's not good.", "isCorrect": False},
                        {"text": "Capisco, quindi se dormo non è tardi.", "english": "I see, so if I sleep it's not late.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "Possiamo estendere la garanzia a tre anni.",
                    "english": "We can extend the warranty to three years.",
                    "choices": [
                        {"text": "Quanto costa l'estensione?", "english": "How much does the extension cost?", "isCorrect": True},
                        {"text": "Quanto pesa l'elefante?", "english": "How much does the elephant weigh?", "isCorrect": False},
                        {"text": "Quanto corre il cavallo?", "english": "How much does the horse run?", "isCorrect": False}
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Costa cinquanta euro in più.",
                    "english": "It costs fifty euros more.",
                    "choices": [
                        {"text": "Va bene, preferisco averla.", "english": "Alright, I prefer to have it.", "isCorrect": True},
                        {"text": "No grazie, preferisco la pizza.", "english": "No thanks, I prefer pizza.", "isCorrect": False},
                        {"text": "Sì, preferisco il mare.", "english": "Yes, I prefer the sea.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "La garanzia è valida in tutta Italia.",
                    "english": "The warranty is valid throughout Italy.",
                    "choices": [
                        {"text": "Ottimo, anche in altre città.", "english": "Great, even in other cities.", "isCorrect": True},
                        {"text": "Male, anche in altri piatti.", "english": "Bad, even in other dishes.", "isCorrect": False},
                        {"text": "Bene, anche in altri boschi.", "english": "Good, even in other woods.", "isCorrect": False}
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "In caso di guasto, può venire qui in negozio.",
                    "english": "In case of a breakdown, you can come here to the store.",
                    "choices": [
                        {"text": "Perfetto, spero di non averne bisogno.", "english": "Perfect, I hope I won't need it.", "isCorrect": True},
                        {"text": "Bello, spero di non mangiare tutto.", "english": "Nice, I hope I won't eat everything.", "isCorrect": False},
                        {"text": "Bene, spero di non dormire troppo.", "english": "Good, I hope I won't sleep too much.", "isCorrect": False}
                    ]
                }
            ]
        }
    ]
}

with open('src/data/exports/shopping/electronics_store/conversations.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
