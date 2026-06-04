import json

scenario_id = 54
conversations = [
    {
        "id": "using_the_laundromat",
        "title": "Using the Laundromat",
        "description": "Learn how to use the self-service machines and get tokens.",
        "messages": [
            {
                "id": "m1",
                "role": "host",
                "text": "Buongiorno! Benvenuti alla nostra lavanderia. Avete mai usato queste macchine?",
                "english": "Good morning! Welcome to our laundromat. Have you ever used these machines?",
                "choices": [
                    {"text": "No, è la mia prima volta. Mi può aiutare?", "isCorrect": True, "english": "No, it's my first time. Can you help me?"},
                    {"text": "Sì, ho già mangiato una pizza molto buona.", "isCorrect": False},
                    {"text": "No, preferisco andare al cinema stasera.", "isCorrect": False}
                ]
            },
            {
                "id": "m2",
                "role": "host",
                "text": "Certamente. Per prima cosa, dovete cambiare i soldi in gettoni.",
                "english": "Certainly. First, you need to change your money into tokens.",
                "choices": [
                    {"text": "Dove si trova la macchina dei gettoni?", "isCorrect": True, "english": "Where is the token machine?"},
                    {"text": "Qual è il numero del dottore di base?", "isCorrect": False},
                    {"text": "Quanto costa un biglietto per il treno?", "isCorrect": False}
                ]
            },
            {
                "id": "m3",
                "role": "host",
                "text": "È laggiù, vicino all'ingresso. Accetta banconote da cinque e dieci euro.",
                "english": "It's over there, near the entrance. It accepts five and ten euro notes.",
                "choices": [
                    {"text": "Va bene, vado a prendere i gettoni adesso.", "isCorrect": True, "english": "All right, I'm going to get the tokens now."},
                    {"text": "Capito, ordino subito un caffè al bar.", "isCorrect": False},
                    {"text": "D'accordo, cerco un parcheggio per l'auto.", "isCorrect": False}
                ]
            },
            {
                "id": "m4",
                "role": "host",
                "text": "Quanti chili di bucato avete da lavare oggi?",
                "english": "How many kilos of laundry do you have to wash today?",
                "choices": [
                    {"text": "Ho circa otto chili di vestiti colorati.", "isCorrect": True, "english": "I have about eight kilos of colored clothes."},
                    {"text": "Ho circa due chili di mele rosse e dolci.", "isCorrect": False},
                    {"text": "Ho quasi dieci euro nel mio portafoglio.", "isCorrect": False}
                ]
            },
            {
                "id": "m5",
                "role": "host",
                "text": "Allora vi serve la lavatrice grande, quella numero otto.",
                "english": "Then you need the large washing machine, number eight.",
                "choices": [
                    {"text": "Grazie, metto subito i vestiti dentro.", "isCorrect": True, "english": "Thanks, I'll put the clothes inside right away."},
                    {"text": "Grazie, chiamo subito un taxi veloce.", "isCorrect": False},
                    {"text": "Grazie, cerco subito un tavolo vuoto.", "isCorrect": False}
                ]
            },
            {
                "id": "m6",
                "role": "host",
                "text": "Avete già il detersivo o volete comprarlo qui?",
                "english": "Do you already have detergent or do you want to buy it here?",
                "choices": [
                    {"text": "Non ce l'ho, vorrei comprare una dose.", "isCorrect": True, "english": "I don't have it, I'd like to buy a dose."},
                    {"text": "Non lo so, vorrei vedere un film lungo.", "isCorrect": False},
                    {"text": "Non mi va, vorrei ordinare un dolce.", "isCorrect": False}
                ]
            },
            {
                "id": "m7",
                "role": "host",
                "text": "Potete acquistarlo al distributore automatico qui accanto.",
                "english": "You can buy it at the vending machine next to here.",
                "choices": [
                    {"text": "Mi serve anche l'ammorbidente per le lenzuola?", "isCorrect": True, "english": "Do I also need softener for the sheets?"},
                    {"text": "Mi serve anche un ombrello per la pioggia?", "isCorrect": False},
                    {"text": "Mi serve anche un dizionario per studiare?", "isCorrect": False}
                ]
            },
            {
                "id": "m8",
                "role": "host",
                "text": "Sì, se volete i vestiti più morbidi e profumati.",
                "english": "Yes, if you want the clothes softer and more scented.",
                "choices": [
                    {"text": "Allora prendo sia il detersivo che l'ammorbidente.", "isCorrect": True, "english": "Then I'll take both the detergent and the softener."},
                    {"text": "Allora compro sia il giornale che la rivista.", "isCorrect": False},
                    {"text": "Allora porto sia la borsa che lo zainetto.", "isCorrect": False}
                ]
            },
            {
                "id": "m9",
                "role": "host",
                "text": "Perfetto. Una volta messi i vestiti, inserite due gettoni.",
                "english": "Perfect. Once the clothes are in, insert two tokens.",
                "choices": [
                    {"text": "E poi devo chiudere bene l'oblò, giusto?", "isCorrect": True, "english": "And then I have to close the porthole well, right?"},
                    {"text": "E poi devo pagare il conto al cameriere?", "isCorrect": False},
                    {"text": "E poi devo spegnere la luce della stanza?", "isCorrect": False}
                ]
            },
            {
                "id": "m10",
                "role": "host",
                "text": "Esatto. Se l'oblò non è chiuso, la macchina non parte.",
                "english": "Exactly. If the porthole isn't closed, the machine won't start.",
                "choices": [
                    {"text": "Capito. Grazie mille per le spiegazioni.", "isCorrect": True, "english": "Understood. Thanks a lot for the explanations."},
                    {"text": "Capito. Cerco subito la fermata del bus.", "isCorrect": False},
                    {"text": "Capito. Voglio un bicchiere di acqua.", "isCorrect": False}
                ]
            }
        ]
    },
    {
        "id": "choosing_the_wash_cycle",
        "title": "Choosing the Wash Cycle",
        "description": "Select the correct temperature and program for your laundry.",
        "messages": [
            {
                "id": "m1",
                "role": "host",
                "text": "Adesso dobbiamo scegliere il programma giusto. Cosa dovete lavare?",
                "english": "Now we need to choose the right program. What do you have to wash?",
                "choices": [
                    {"text": "Ho molte magliette di cotone bianco.", "isCorrect": True, "english": "I have many white cotton t-shirts."},
                    {"text": "Ho molte scarpe da tennis vecchie.", "isCorrect": False},
                    {"text": "Ho molti libri di storia antica.", "isCorrect": False}
                ]
            },
            {
                "id": "m2",
                "role": "host",
                "text": "Per il cotone bianco consiglio il ciclo a sessanta gradi.",
                "english": "For white cotton I recommend the sixty-degree cycle.",
                "choices": [
                    {"text": "Non è troppo caldo? Ho paura che si restringano.", "isCorrect": True, "english": "Isn't it too hot? I'm afraid they might shrink."},
                    {"text": "Non è troppo caro? Ho paura che costi troppo.", "isCorrect": False},
                    {"text": "Non è troppo tardi? Ho paura di fare tardi.", "isCorrect": False}
                ]
            },
            {
                "id": "m3",
                "role": "host",
                "text": "Se avete paura, possiamo usare il programma a quaranta gradi.",
                "english": "If you're afraid, we can use the forty-degree program.",
                "choices": [
                    {"text": "Sì, quaranta gradi mi sembra più sicuro.", "isCorrect": True, "english": "Yes, forty degrees seems safer to me."},
                    {"text": "Sì, quaranta persone mi sembra troppo.", "isCorrect": False},
                    {"text": "Sì, quaranta minuti mi sembra poco.", "isCorrect": False}
                ]
            },
            {
                "id": "m4",
                "role": "host",
                "text": "Benissimo. Volete anche fare il prelavaggio per le macchie?",
                "english": "Very well. Do you also want to do the pre-wash for stains?",
                "choices": [
                    {"text": "No, i vestiti non sono molto sporchi.", "isCorrect": True, "english": "No, the clothes are not very dirty."},
                    {"text": "No, i bambini non sono molto stanchi.", "isCorrect": False},
                    {"text": "No, i panini non sono molto buoni.", "isCorrect": False}
                ]
            },
            {
                "id": "m5",
                "role": "host",
                "text": "Va bene. E per la centrifuga? Volete quella forte?",
                "english": "All right. And for the spin cycle? Do you want the strong one?",
                "choices": [
                    {"text": "Sì, così i vestiti si asciugano più in fretta.", "isCorrect": True, "english": "Yes, so the clothes dry faster."},
                    {"text": "Sì, così i piatti si rompono più in fretta.", "isCorrect": False},
                    {"text": "Sì, così i cani corrono più in fretta.", "isCorrect": False}
                ]
            },
            {
                "id": "m6",
                "role": "host",
                "text": "Allora selezionate il tasto con l'icona della spirale.",
                "english": "Then select the button with the spiral icon.",
                "choices": [
                    {"text": "Ho premuto il tasto. Ora cosa devo fare?", "isCorrect": True, "english": "I pressed the button. Now what should I do?"},
                    {"text": "Ho aperto la porta. Ora cosa devo fare?", "isCorrect": False},
                    {"text": "Ho chiuso il libro. Ora cosa devo fare?", "isCorrect": False}
                ]
            },
            {
                "id": "m7",
                "role": "host",
                "text": "Ora girate la manopola sul programma numero due.",
                "english": "Now turn the knob to program number two.",
                "choices": [
                    {"text": "Fatto. Vedo che il display segna quaranta minuti.", "isCorrect": True, "english": "Done. I see the display shows forty minutes."},
                    {"text": "Fatto. Vedo che il cameriere porta il conto.", "isCorrect": False},
                    {"text": "Fatto. Vedo che il treno arriva in stazione.", "isCorrect": False}
                ]
            },
            {
                "id": "m8",
                "role": "host",
                "text": "Esatto. Quello è il tempo necessario per il lavaggio.",
                "english": "Exactly. That is the time needed for the wash.",
                "choices": [
                    {"text": "Posso andare via o devo restare qui?", "isCorrect": True, "english": "Can I leave or do I have to stay here?"},
                    {"text": "Posso mangiare qui o devo uscire?", "isCorrect": False},
                    {"text": "Posso dormire qui o devo andare?", "isCorrect": False}
                ]
            },
            {
                "id": "m9",
                "role": "host",
                "text": "Potete andare, ma tornate puntuali per svuotare la macchina.",
                "english": "You can go, but come back on time to empty the machine.",
                "choices": [
                    {"text": "Tornerò tra quaranta minuti esatti.", "isCorrect": True, "english": "I'll be back in exactly forty minutes."},
                    {"text": "Mangerò tra quaranta minuti esatti.", "isCorrect": False},
                    {"text": "Partirò tra quaranta minuti esatti.", "isCorrect": False}
                ]
            },
            {
                "id": "m10",
                "role": "host",
                "text": "Ottimo. Il timer vi aiuterà a controllare il tempo.",
                "english": "Great. The timer will help you check the time.",
                "choices": [
                    {"text": "Grazie, a più tardi allora!", "isCorrect": True, "english": "Thanks, see you later then!"},
                    {"text": "Grazie, a più caffè allora!", "isCorrect": False},
                    {"text": "Grazie, a più film allora!", "isCorrect": False}
                ]
            }
        ]
    },
    {
        "id": "adding_detergent",
        "title": "Adding Detergent",
        "description": "Put detergent and softener in the correct compartments.",
        "messages": [
            {
                "id": "m1",
                "role": "host",
                "text": "Prima di far partire la lavatrice, dobbiamo mettere i prodotti.",
                "english": "Before starting the washing machine, we need to put the products in.",
                "choices": [
                    {"text": "Dove devo versare il detersivo liquido?", "isCorrect": True, "english": "Where should I pour the liquid detergent?"},
                    {"text": "Dove devo mettere lo zucchero nel caffè?", "isCorrect": False},
                    {"text": "Dove devo buttare la carta del pane?", "isCorrect": False}
                ]
            },
            {
                "id": "m2",
                "role": "host",
                "text": "C'è un cassetto in alto. Vedete lo scomparto con il simbolo 'II'?",
                "english": "There's a drawer at the top. Do you see the compartment with the 'II' symbol?",
                "choices": [
                    {"text": "Sì, lo vedo. Devo metterlo tutto lì?", "isCorrect": True, "english": "Yes, I see it. Should I put it all there?"},
                    {"text": "Sì, lo vedo. Devo berlo tutto adesso?", "isCorrect": False},
                    {"text": "Sì, lo vedo. Devo leggerlo tutto oggi?", "isCorrect": False}
                ]
            },
            {
                "id": "m3",
                "role": "host",
                "text": "Sì, mettete una dose di detersivo nello scomparto 'II'.",
                "english": "Yes, put a dose of detergent in compartment 'II'.",
                "choices": [
                    {"text": "E l'ammorbidente dove va inserito invece?", "isCorrect": True, "english": "And where should the softener be inserted instead?"},
                    {"text": "E il passaporto dove va inserito invece?", "isCorrect": False},
                    {"text": "E il bancomat dove va inserito invece?", "isCorrect": False}
                ]
            },
            {
                "id": "m4",
                "role": "host",
                "text": "L'ammorbidente va nel piccolo scomparto con il fiore.",
                "english": "The softener goes in the small compartment with the flower.",
                "choices": [
                    {"text": "Devo aggiungere anche del candeggiante per i bianchi?", "isCorrect": True, "english": "Do I also need to add bleach for the whites?"},
                    {"text": "Devo aggiungere anche del pepe nero per la pasta?", "isCorrect": False},
                    {"text": "Devo aggiungere anche del miele caldo per il tè?", "isCorrect": False}
                ]
            },
            {
                "id": "m5",
                "role": "host",
                "text": "Solo se volete un bianco molto brillante, ma non è obbligatorio.",
                "english": "Only if you want a very bright white, but it's not mandatory.",
                "choices": [
                    {"text": "No, per oggi il detersivo è sufficiente.", "isCorrect": True, "english": "No, for today the detergent is sufficient."},
                    {"text": "No, per oggi il dottore è occupato.", "isCorrect": False},
                    {"text": "No, per oggi il negozio è chiuso.", "isCorrect": False}
                ]
            },
            {
                "id": "m6",
                "role": "host",
                "text": "Va bene. Chiudete pure il cassetto con delicatezza.",
                "english": "All right. Go ahead and close the drawer gently.",
                "choices": [
                    {"text": "Ecco fatto, il cassetto è chiuso bene.", "isCorrect": True, "english": "There we go, the drawer is closed well."},
                    {"text": "Ecco fatto, il cameriere è arrivato.", "isCorrect": False},
                    {"text": "Ecco fatto, il biglietto è pagato.", "isCorrect": False}
                ]
            },
            {
                "id": "m7",
                "role": "host",
                "text": "Ora potete premere il tasto 'Avvio' per iniziare.",
                "english": "Now you can press the 'Start' button to begin.",
                "choices": [
                    {"text": "La luce è diventata verde. È partita?", "isCorrect": True, "english": "The light has turned green. Has it started?"},
                    {"text": "La mela è diventata rossa. È buona?", "isCorrect": False},
                    {"text": "La borsa è diventata blu. È nuova?", "isCorrect": False}
                ]
            },
            {
                "id": "m8",
                "role": "host",
                "text": "Sì, sentite l'acqua che entra nel cestello?",
                "english": "Yes, can you hear the water entering the drum?",
                "choices": [
                    {"text": "Sì, la macchina ha iniziato a girare.", "isCorrect": True, "english": "Yes, the machine has started to spin."},
                    {"text": "Sì, la macchina ha iniziato a volare.", "isCorrect": False},
                    {"text": "Sì, la macchina ha iniziato a cantare.", "isCorrect": False}
                ]
            },
            {
                "id": "m9",
                "role": "host",
                "text": "Perfetto. Non aprite l'oblò finché non ha finito.",
                "english": "Perfect. Don't open the porthole until it's finished.",
                "choices": [
                    {"text": "Certo, so che l'oblò rimane bloccato durante il lavaggio.", "isCorrect": True, "english": "Of course, I know the porthole stays locked during the wash."},
                    {"text": "Certo, so che il cinema rimane aperto fino a mezzanotte.", "isCorrect": False},
                    {"text": "Certo, so che il ristorante rimane chiuso il lunedì.", "isCorrect": False}
                ]
            },
            {
                "id": "m10",
                "role": "host",
                "text": "Bravissimi. Avete fatto tutto correttamente.",
                "english": "Very good. You did everything correctly.",
                "choices": [
                    {"text": "Grazie, è stato più facile di quanto pensassi.", "isCorrect": True, "english": "Thanks, it was easier than I thought."},
                    {"text": "Grazie, è stato più caro di quanto pensassi.", "isCorrect": False},
                    {"text": "Grazie, è stato più tardi di quanto pensassi.", "isCorrect": False}
                ]
            }
        ]
    },
    {
        "id": "using_the_dryer",
        "title": "Using the Dryer",
        "description": "Dry your clothes and set the right temperature.",
        "messages": [
            {
                "id": "m1",
                "role": "host",
                "text": "Il lavaggio è finito. Adesso volete usare l'asciugatrice?",
                "english": "The wash is finished. Do you want to use the dryer now?",
                "choices": [
                    {"text": "Sì, fuori piove e i vestiti sono molto bagnati.", "isCorrect": True, "english": "Yes, it's raining outside and the clothes are very wet."},
                    {"text": "Sì, fuori fa caldo e i vestiti sono molto asciutti.", "isCorrect": False},
                    {"text": "Sì, fuori c'è vento e i vestiti sono molto puliti.", "isCorrect": False}
                ]
            },
            {
                "id": "m2",
                "role": "host",
                "text": "Mettete il bucato nell'asciugatrice numero dodici.",
                "english": "Put the laundry in dryer number twelve.",
                "choices": [
                    {"text": "Devo separare i tessuti pesanti da quelli leggeri?", "isCorrect": True, "english": "Should I separate heavy fabrics from light ones?"},
                    {"text": "Devo separare i pomodori grandi da quelli piccoli?", "isCorrect": False},
                    {"text": "Devo separare i bicchieri sporchi da quelli puliti?", "isCorrect": False}
                ]
            },
            {
                "id": "m3",
                "role": "host",
                "text": "Sarebbe meglio, così si asciugano in modo uniforme.",
                "english": "It would be better, so they dry evenly.",
                "choices": [
                    {"text": "Allora metto i jeans da una parte e le camicie dall'altra.", "isCorrect": True, "english": "Then I'll put the jeans on one side and the shirts on the other."},
                    {"text": "Allora metto le scarpe da una parte e il cappello dall'altra.", "isCorrect": False},
                    {"text": "Allora metto le mele da una parte e le pere dall'altra.", "isCorrect": False}
                ]
            },
            {
                "id": "m4",
                "role": "host",
                "text": "Ottima idea. Quale temperatura volete impostare?",
                "english": "Great idea. What temperature do you want to set?",
                "choices": [
                    {"text": "Vorrei una temperatura media per non rovinare le camicie.", "isCorrect": True, "english": "I'd like a medium temperature so as not to ruin the shirts."},
                    {"text": "Vorrei una temperatura fredda per non rovinare il gelato.", "isCorrect": False},
                    {"text": "Vorrei una temperatura calda per non rovinare la pasta.", "isCorrect": False}
                ]
            },
            {
                "id": "m5",
                "role": "host",
                "text": "Allora premete il tasto 'Medium' sul pannello.",
                "english": "Then press the 'Medium' button on the panel.",
                "choices": [
                    {"text": "Quanti minuti servono per un carico completo?", "isCorrect": True, "english": "How many minutes are needed for a full load?"},
                    {"text": "Quanti euro servono per un caffè macchiato?", "isCorrect": False},
                    {"text": "Quanti giorni servono per un viaggio lungo?", "isCorrect": False}
                ]
            },
            {
                "id": "m6",
                "role": "host",
                "text": "Di solito trenta minuti sono sufficienti per tutto.",
                "english": "Usually thirty minutes are enough for everything.",
                "choices": [
                    {"text": "Servono altri gettoni per l'asciugatrice?", "isCorrect": True, "english": "Are other tokens needed for the dryer?"},
                    {"text": "Servono altri occhiali per la televisione?", "isCorrect": False},
                    {"text": "Servono altri biglietti per la metropolitana?", "isCorrect": False}
                ]
            },
            {
                "id": "m7",
                "role": "host",
                "text": "Sì, serve un gettone ogni quindici minuti.",
                "english": "Yes, one token is needed every fifteen minutes.",
                "choices": [
                    {"text": "Quindi inserisco due gettoni per mezz'ora.", "isCorrect": True, "english": "So I'll insert two tokens for half an hour."},
                    {"text": "Quindi compro due gelati per merenda.", "isCorrect": False},
                    {"text": "Quindi prendo due taxi per andare.", "isCorrect": False}
                ]
            },
            {
                "id": "m8",
                "role": "host",
                "text": "Esatto. Ricordatevi di pulire il filtro della lanugine.",
                "english": "Exactly. Remember to clean the lint filter.",
                "choices": [
                    {"text": "Dove si trova il filtro da pulire?", "isCorrect": True, "english": "Where is the filter to be cleaned?"},
                    {"text": "Dove si trova il bagno da pulire?", "isCorrect": False},
                    {"text": "Dove si trova il tavolo da pulire?", "isCorrect": False}
                ]
            },
            {
                "id": "m9",
                "role": "host",
                "text": "È proprio qui sotto l'apertura dell'oblò.",
                "english": "It's right here under the porthole opening.",
                "choices": [
                    {"text": "Ho tolto la polvere. Adesso posso avviare.", "isCorrect": True, "english": "I've removed the dust. Now I can start it."},
                    {"text": "Ho tolto le scarpe. Adesso posso entrare.", "isCorrect": False},
                    {"text": "Ho tolto la borsa. Adesso posso sedermi.", "isCorrect": False}
                ]
            },
            {
                "id": "m10",
                "role": "host",
                "text": "Perfetto. I vostri vestiti saranno caldi e asciutti tra poco.",
                "english": "Perfect. Your clothes will be warm and dry soon.",
                "choices": [
                    {"text": "Grazie mille per l'aiuto oggi!", "isCorrect": True, "english": "Thanks a lot for the help today!"},
                    {"text": "Grazie mille per la pizza oggi!", "isCorrect": False},
                    {"text": "Grazie mille per il film oggi!", "isCorrect": False}
                ]
            }
        ]
    }
]

data = {
    "scenarioId": scenario_id,
    "conversations": conversations
}

with open("/home/waseageru/parli-italiano/src/data/exports/daily_life/laundry_machine/conversations.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
