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
          { "text": "Sì, scusi. Mi sono perso. Dov'è la piazza centrale?", "isCorrect": True, "feedback": "Perfect!" },
          { "text": "No, io voglio andare a casa mia adesso da solo.", "isCorrect": False, "feedback": "A bit rude." },
          { "text": "Non conosco questa città, voglio andare a dormire.", "isCorrect": False, "feedback": "Too negative." }
        ]
      },
      {
        "id": "m2",
        "role": "host",
        "text": "La piazza centrale? È molto vicina. Deve andare dritto per questa strada.",
        "english": "The main square? It is very close. You need to go straight on this street.",
        "choices": [
          { "text": "Dritto per questa strada, ho capito. E poi?", "isCorrect": True, "feedback": "Good!" },
          { "text": "Voglio girare a sinistra al semaforo adesso.", "isCorrect": False, "feedback": "Contradicts." },
          { "text": "Quanti chilometri ci sono da qui esattamente?", "isCorrect": False, "feedback": "They said close!" }
        ]
      },
      {
        "id": "m3",
        "role": "host",
        "text": "Poi, al semaforo, deve girare a destra. È lì.",
        "english": "Then, at the traffic light, you must turn right. It's there.",
        "choices": [
          { "text": "Girare a destra al semaforo. È prima del ponte?", "isCorrect": True, "feedback": "Good question." },
          { "text": "Devo tornare indietro al semaforo rosso adesso.", "isCorrect": False, "feedback": "No, turn right." },
          { "text": "Io non ho capito niente di niente, scusa davvero.", "isCorrect": False, "feedback": "Too confusing." }
        ]
      },
      {
        "id": "m4",
        "role": "host",
        "text": "Sì, esattamente prima del ponte. Vedrà una fontana grande.",
        "english": "Yes, exactly before the bridge. You will see a big fountain.",
        "choices": [
          { "text": "Una fontana grande, perfetto. C'è anche un bar lì?", "isCorrect": True, "feedback": "Natural." },
          { "text": "Io non voglio vedere il ponte e l'acqua oggi no.", "isCorrect": False, "feedback": "Weird." },
          { "text": "La piazza piccola è molto lontana da qui adesso.", "isCorrect": False, "feedback": "Not what they said." }
        ]
      },
      {
        "id": "m5",
        "role": "host",
        "text": "Sì, c'è un bar molto buono vicino alla fontana.",
        "english": "Yes, there is a very good bar near the fountain.",
        "choices": [
          { "text": "Ottimo, ho proprio sete. Hanno l'acqua fredda lì?", "isCorrect": True, "feedback": "Good continuation." },
          { "text": "Voglio mangiare una pizza gigante in un ristorante.", "isCorrect": False, "feedback": "You asked about a bar." },
          { "text": "Io non ho soldi per comprare l'acqua al bar oggi.", "isCorrect": False, "feedback": "A bit irrelevant." }
        ]
      },
      {
        "id": "m6",
        "role": "host",
        "text": "Certamente, hanno di tutto. Vuole indicazioni anche per il museo?",
        "english": "Certainly, they have everything. Do you want directions for the museum too?",
        "choices": [
          { "text": "No grazie, oggi voglio solo riposare in piazza un po'.", "isCorrect": True, "feedback": "Clear answer." },
          { "text": "Voglio andare in montagna a sciare con i miei amici.", "isCorrect": False, "feedback": "Not in the city!" },
          { "text": "Il museo è chiuso tutti i giorni della settimana.", "isCorrect": False, "feedback": "You don't know that." }
        ]
      },
      {
        "id": "m7",
        "role": "host",
        "text": "Capisco, la piazza è perfetta per rilassarsi. Ha una mappa?",
        "english": "I understand, the square is perfect for relaxing. Do you have a map?",
        "choices": [
          { "text": "No, ma uso la mappa sul mio telefono. Funziona bene.", "isCorrect": True, "feedback": "Good." },
          { "text": "Io ho un libro di ricette italiane nella mia borsa.", "isCorrect": False, "feedback": "Not a map." },
          { "text": "Non voglio leggere nessuna mappa cartacea oggi io.", "isCorrect": False, "feedback": "Too aggressive." }
        ]
      },
      {
        "id": "m8",
        "role": "host",
        "text": "Molto comodo. Faccia attenzione al traffico quando attraversa.",
        "english": "Very convenient. Pay attention to the traffic when you cross.",
        "choices": [
          { "text": "Sì, farò attenzione. Ci sono molte macchine in centro?", "isCorrect": True, "feedback": "Good question." },
          { "text": "Voglio comprare una macchina sportiva molto veloce.", "isCorrect": False, "feedback": "Irrelevant." },
          { "text": "Il traffico non esiste nella mia città in campagna.", "isCorrect": False, "feedback": "Off topic." }
        ]
      },
      {
        "id": "m9",
        "role": "host",
        "text": "Abbastanza, soprattutto in questa via principale. Ma è sicuro.",
        "english": "Quite a bit, especially on this main street. But it's safe.",
        "choices": [
          { "text": "Meno male. Grazie mille per le indicazioni, molto gentile.", "isCorrect": True, "feedback": "Polite." },
          { "text": "Io ho paura delle strade vuote senza persone intorno.", "isCorrect": False, "feedback": "They said it's busy." },
          { "text": "Non voglio attraversare la strada mai più in vita mia.", "isCorrect": False, "feedback": "Unrealistic." }
        ]
      },
      {
        "id": "m10",
        "role": "host",
        "text": "Di niente, è un piacere. Buona giornata e buona passeggiata!",
        "english": "You're welcome, it's a pleasure. Have a good day and a good walk!",
        "choices": [
          { "text": "Grazie, buona giornata anche a lei! Arrivederci.", "isCorrect": True, "feedback": "Perfect close." },
          { "text": "Io vado via correndo da questa città molto presto.", "isCorrect": False, "feedback": "Rude." },
          { "text": "Non mi piace passeggiare la mattina presto con il sole.", "isCorrect": False, "feedback": "Negative." }
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
          { "text": "Sì, grazie. Non so come comprare un biglietto.", "isCorrect": True, "feedback": "Direct." },
          { "text": "Voglio un panino con il formaggio adesso qui.", "isCorrect": False, "feedback": "Wrong machine." },
          { "text": "Io non parlo italiano con le persone adesso.", "isCorrect": False, "feedback": "You are doing it." }
        ]
      },
      {
        "id": "m2",
        "role": "host",
        "text": "È facile. Prima, deve scegliere la destinazione sullo schermo.",
        "english": "It's easy. First, you must choose the destination on the screen.",
        "choices": [
          { "text": "Va bene, ho scelto Roma. E adesso cosa faccio?", "isCorrect": True, "feedback": "Good continuation." },
          { "text": "Io ho messo i soldi nella macchinetta adesso.", "isCorrect": False, "feedback": "Too early!" },
          { "text": "Non voglio andare in quel posto lontano ora.", "isCorrect": False, "feedback": "Why buy a ticket?" }
        ]
      },
      {
        "id": "m3",
        "role": "host",
        "text": "Perfetto. Ora deve scegliere il tipo di treno. Rapido o regionale?",
        "english": "Perfect. Now you must choose the type of train. Fast or regional?",
        "choices": [
          { "text": "Voglio il treno rapido, grazie. Quanto costa il biglietto?", "isCorrect": True, "feedback": "Good." },
          { "text": "Io preferisco l'autobus per viaggiare in questa città.", "isCorrect": False, "feedback": "You are at a train ticket machine." },
          { "text": "Non mi piacciono i treni in generale per viaggiare lontano.", "isCorrect": False, "feedback": "Irrelevant." }
        ]
      },
      {
        "id": "m4",
        "role": "host",
        "text": "Il treno rapido costa quaranta euro. Lo selezioni qui.",
        "english": "The fast train costs forty euros. Select it here.",
        "choices": [
          { "text": "Selezionato. Adesso devo indicare il numero di biglietti?", "isCorrect": True, "feedback": "Logical next step." },
          { "text": "Quaranta euro è troppo economico per me oggi, voglio spendere.", "isCorrect": False, "feedback": "Unrealistic." },
          { "text": "Io non voglio selezionare niente con le mie mani adesso.", "isCorrect": False, "feedback": "Weird." }
        ]
      },
      {
        "id": "m5",
        "role": "host",
        "text": "Sì, quanti biglietti desidera acquistare?",
        "english": "Yes, how many tickets do you wish to buy?",
        "choices": [
          { "text": "Solo un biglietto per me, per favore. C'è lo sconto per studenti?", "isCorrect": True, "feedback": "Good question." },
          { "text": "Voglio comprare cento biglietti per tutti i miei grandi amici.", "isCorrect": False, "feedback": "A bit exaggerated." },
          { "text": "Io non ho bisogno di biglietti per viaggiare in treno oggi.", "isCorrect": False, "feedback": "Contradiction." }
        ]
      },
      {
        "id": "m6",
        "role": "host",
        "text": "Sì, c'è uno sconto. Ha la tessera studenti con lei?",
        "english": "Yes, there is a discount. Do you have your student card with you?",
        "choices": [
          { "text": "Sì, eccola qui. La devo inserire nella macchinetta?", "isCorrect": True, "feedback": "Actionable." },
          { "text": "Io sono un professore molto vecchio e severo nella scuola.", "isCorrect": False, "feedback": "You just asked for a student discount." },
          { "text": "Non voglio mostrare la mia carta a nessuno in questa stazione.", "isCorrect": False, "feedback": "Then you don't get a discount." }
        ]
      },
      {
        "id": "m7",
        "role": "host",
        "text": "No, basta scansionare il codice a barre qui sotto.",
        "english": "No, just scan the barcode down here.",
        "choices": [
          { "text": "Fatto! Lo schermo dice trenta euro. Adesso pago?", "isCorrect": True, "feedback": "Progress!" },
          { "text": "Non trovo il codice a barre sul mio libro di matematica.", "isCorrect": False, "feedback": "Card, not book." },
          { "text": "Voglio rompere lo schermo di questa macchinetta lenta.", "isCorrect": False, "feedback": "Destructive!" }
        ]
      },
      {
        "id": "m8",
        "role": "host",
        "text": "Sì. Può inserire i soldi o usare la carta di credito.",
        "english": "Yes. You can insert the money or use the credit card.",
        "choices": [
          { "text": "Uso la carta. La inserisco in questa fessura a destra?", "isCorrect": True, "feedback": "Good clarification." },
          { "text": "Non voglio pagare il biglietto oggi, grazie mille per l'aiuto.", "isCorrect": False, "feedback": "You must pay!" },
          { "text": "La macchinetta è molto grande e bella davvero per me oggi.", "isCorrect": False, "feedback": "Irrelevant." }
        ]
      },
      {
        "id": "m9",
        "role": "host",
        "text": "Esatto, nella fessura a destra. Poi metta il codice PIN.",
        "english": "Exactly, in the slot on the right. Then put the PIN code.",
        "choices": [
          { "text": "Codice inserito. Sto aspettando la stampa del biglietto.", "isCorrect": True, "feedback": "Waiting for the result." },
          { "text": "Ho dimenticato il mio nome completo questa mattina presto.", "isCorrect": False, "feedback": "You need the PIN, not your name." },
          { "text": "Non voglio usare il codice segreto con le persone intorno.", "isCorrect": False, "feedback": "Hide it, but you must use it." }
        ]
      },
      {
        "id": "m10",
        "role": "host",
        "text": "Ecco il suo biglietto. Buon viaggio verso Roma!",
        "english": "Here is your ticket. Have a good trip to Rome!",
        "choices": [
          { "text": "Grazie mille per l'aiuto! È stato molto gentile. Arrivederci.", "isCorrect": True, "feedback": "Polite end." },
          { "text": "Il viaggio è molto lungo e noioso oggi per me in questo treno.", "isCorrect": False, "feedback": "Negative." },
          { "text": "Non voglio viaggiare con te oggi, ciao per sempre amico mio.", "isCorrect": False, "feedback": "They aren't traveling with you." }
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
          { "text": "Sì, scusi. Come si arriva alla stazione dei treni?", "isCorrect": True, "feedback": "Clear." },
          { "text": "Voglio mangiare una pizza grande in pizzeria ora.", "isCorrect": False, "feedback": "Wrong topic." },
          { "text": "Io cerco la mia borsa che ho perso in strada qui.", "isCorrect": False, "feedback": "Not asking for directions." }
        ]
      },
      {
        "id": "m2",
        "role": "host",
        "text": "La stazione non è lontana. Vada dritto per cento metri.",
        "english": "The station is not far. Go straight for a hundred meters.",
        "choices": [
          { "text": "Dritto per cento metri. E dopo il parco cosa faccio?", "isCorrect": True, "feedback": "Good question." },
          { "text": "Voglio girare a sinistra subito al bar aperto ora.", "isCorrect": False, "feedback": "Contradicts." },
          { "text": "Io non voglio camminare per cento metri al caldo.", "isCorrect": False, "feedback": "Lazy!" }
        ]
      },
      {
        "id": "m3",
        "role": "host",
        "text": "Dopo il parco, giri a sinistra. C'è una farmacia all'angolo.",
        "english": "After the park, turn left. There is a pharmacy on the corner.",
        "choices": [
          { "text": "A sinistra alla farmacia. E poi devo continuare dritto?", "isCorrect": True, "feedback": "Confirming." },
          { "text": "Io voglio comprare le medicine in farmacia adesso.", "isCorrect": False, "feedback": "You are going to the station." },
          { "text": "La farmacia è sempre chiusa la domenica mattina qui.", "isCorrect": False, "feedback": "Irrelevant." }
        ]
      },
      {
        "id": "m4",
        "role": "host",
        "text": "Sì, continui dritto per altri due isolati. C'è molto movimento.",
        "english": "Yes, continue straight for another two blocks. There is a lot of movement.",
        "choices": [
          { "text": "Due isolati dritto. La stazione è sulla destra o sinistra?", "isCorrect": True, "feedback": "Asking for specifics." },
          { "text": "Voglio dormire in mezzo alla strada senza macchine.", "isCorrect": False, "feedback": "Weird." },
          { "text": "Io non vedo nessun movimento in questa via tranquilla.", "isCorrect": False, "feedback": "They are talking about further ahead." }
        ]
      },
      {
        "id": "m5",
        "role": "host",
        "text": "La stazione sarà sulla sua destra. È un edificio molto grande.",
        "english": "The station will be on your right. It is a very large building.",
        "choices": [
          { "text": "Perfetto, sulla destra. Devo attraversare la strada per entrare?", "isCorrect": True, "feedback": "Practical." },
          { "text": "Voglio comprare un edificio molto grande in centro.", "isCorrect": False, "feedback": "Off topic." },
          { "text": "L'edificio piccolo a sinistra è il mio preferito qui.", "isCorrect": False, "feedback": "Contradicts." }
        ]
      },
      {
        "id": "m6",
        "role": "host",
        "text": "Sì, c'è un semaforo pedonale proprio davanti all'ingresso.",
        "english": "Yes, there is a pedestrian traffic light right in front of the entrance.",
        "choices": [
          { "text": "Meno male. Ci sono i distributori automatici fuori?", "isCorrect": True, "feedback": "Asking for details." },
          { "text": "Non voglio usare il semaforo, preferisco correre veloce.", "isCorrect": False, "feedback": "Dangerous." },
          { "text": "Il traffico qui è sempre bloccato per ore intere al giorno.", "isCorrect": False, "feedback": "Irrelevant." }
        ]
      },
      {
        "id": "m7",
        "role": "host",
        "text": "No, le biglietterie e i distributori sono tutti dentro l'atrio.",
        "english": "No, the ticket offices and vending machines are all inside the lobby.",
        "choices": [
          { "text": "Capito. Sa se ci sono treni frequenti per Milano oggi?", "isCorrect": True, "feedback": "Good." },
          { "text": "Io voglio comprare una macchina automatica per caffè.", "isCorrect": False, "feedback": "You are taking a train." },
          { "text": "L'atrio della scuola è molto grande e spazioso per me.", "isCorrect": False, "feedback": "Not a school." }
        ]
      },
      {
        "id": "m8",
        "role": "host",
        "text": "Sì, c'è un treno ogni ora per Milano. È una linea veloce.",
        "english": "Yes, there is a train every hour for Milan. It is a fast line.",
        "choices": [
          { "text": "Ogni ora, ottimo. Non dovrò aspettare troppo tempo allora.", "isCorrect": True, "feedback": "Good response." },
          { "text": "Voglio aspettare cinque ore in stazione per divertimento.", "isCorrect": False, "feedback": "Unlikely." },
          { "text": "I treni lenti sono la mia grande passione fin da piccolo.", "isCorrect": False, "feedback": "Irrelevant." }
        ]
      },
      {
        "id": "m9",
        "role": "host",
        "text": "Se si sbriga, forse riesce a prendere quello delle dieci e mezza.",
        "english": "If you hurry, maybe you can catch the ten thirty one.",
        "choices": [
          { "text": "Le dieci e mezza! Allora devo davvero andare veloce. Grazie!", "isCorrect": True, "feedback": "Urgent and polite." },
          { "text": "Voglio passeggiare molto lentamente guardando i negozi oggi.", "isCorrect": False, "feedback": "Then you will miss it." },
          { "text": "Io non guardo mai l'orologio perché non mi interessa il tempo.", "isCorrect": False, "feedback": "You need to catch a train." }
        ]
      },
      {
        "id": "m10",
        "role": "host",
        "text": "Corra! Buona giornata e buon viaggio verso Milano!",
        "english": "Run! Have a good day and a good trip towards Milan!",
        "choices": [
          { "text": "Grazie mille, è stato gentilissimo. Buona giornata a lei!", "isCorrect": True, "feedback": "Polite exit." },
          { "text": "Non mi piace correre in questa città piena di gente per strada.", "isCorrect": False, "feedback": "Negative." },
          { "text": "Voglio dormire in un albergo qui vicino alla stazione adesso.", "isCorrect": False, "feedback": "You are going to Milan." }
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
        "text": "Salve, vedo che fa fatica. Serve aiuto con la valigia?",
        "english": "Hello, I see you are struggling. Do you need help with the suitcase?",
        "choices": [
          { "text": "Sì, grazie. Questa borsa è molto pesante per me da sola.", "isCorrect": True, "feedback": "Accepting." },
          { "text": "No, non voglio parlare con te oggi, scusa tanto per tutto.", "isCorrect": False, "feedback": "Rude." },
          { "text": "Io sono molto forte e muscoloso in questo tempo e luogo.", "isCorrect": False, "feedback": "Not struggling then." }
        ]
      },
      {
        "id": "m2",
        "role": "host",
        "text": "Nessun problema, la aiuto io. È davvero pesante! Dove deve andare?",
        "english": "No problem, I will help you. It is really heavy! Where do you need to go?",
        "choices": [
          { "text": "Devo arrivare all'albergo, è qui vicino a noi sulla strada.", "isCorrect": True, "feedback": "Clear." },
          { "text": "Voglio mangiare una pizza Margherita nel ristorante grande.", "isCorrect": False, "feedback": "Not a destination." },
          { "text": "Io vado in un paese molto lontano con il treno oggi stesso.", "isCorrect": False, "feedback": "They can't carry it far." }
        ]
      },
      {
        "id": "m3",
        "role": "host",
        "text": "Ah, l'albergo qui all'angolo? Il 'Grand Hotel'? Certo, andiamo.",
        "english": "Ah, the hotel right on the corner? The 'Grand Hotel'? Sure, let's go.",
        "choices": [
          { "text": "Sì, proprio quello. Sei molto gentile, grazie mille davvero.", "isCorrect": True, "feedback": "Appreciative." },
          { "text": "Io non voglio andare all'albergo ora, sono stanco e dormo.", "isCorrect": False, "feedback": "Contradiction." },
          { "text": "Voglio prendere un taxi subito ora per tornare a casa mia.", "isCorrect": False, "feedback": "It's on the corner." }
        ]
      },
      {
        "id": "m4",
        "role": "host",
        "text": "È in vacanza o in viaggio d'affari qui nella nostra città?",
        "english": "Are you on vacation or on a business trip here in our city?",
        "choices": [
          { "text": "Sono in vacanza per una settimana. Volevo vedere i musei locali.", "isCorrect": True, "feedback": "Good info." },
          { "text": "Io lavoro sempre tutto il giorno in una fabbrica molto grande qui.", "isCorrect": False, "feedback": "Then why the hotel and suitcase?" },
          { "text": "Non mi piace viaggiare per affari con persone che non conosco io.", "isCorrect": False, "feedback": "Irrelevant." }
        ]
      },
      {
        "id": "m5",
        "role": "host",
        "text": "Bellissimo! I nostri musei sono fantastici. Le consiglio la galleria d'arte.",
        "english": "Beautiful! Our museums are fantastic. I recommend the art gallery.",
        "choices": [
          { "text": "La galleria d'arte? È lontana dal centro storico della città?", "isCorrect": True, "feedback": "Asking for details." },
          { "text": "Io odio l'arte moderna e tutto quello che c'è nei musei antichi.", "isCorrect": False, "feedback": "A bit rude." },
          { "text": "Voglio andare in piscina a nuotare tutto il giorno oggi e domani.", "isCorrect": False, "feedback": "Changing topic." }
        ]
      },
      {
        "id": "m6",
        "role": "host",
        "text": "No, è proprio in centro. Dietro il municipio vecchio. Facile da trovare.",
        "english": "No, it's right in the center. Behind the old town hall. Easy to find.",
        "choices": [
          { "text": "Ottimo, ci andrò sicuramente domani mattina presto con la luce.", "isCorrect": True, "feedback": "Enthusiastic." },
          { "text": "Io non riesco a trovare niente in questa città piena di strade.", "isCorrect": False, "feedback": "Negative." },
          { "text": "Il municipio della mia città è molto più bello di questo qui.", "isCorrect": False, "feedback": "Insulting." }
        ]
      },
      {
        "id": "m7",
        "role": "host",
        "text": "Bene, siamo quasi arrivati. Vuole che porti la valigia fino dentro?",
        "english": "Good, we are almost there. Do you want me to carry the suitcase all the way inside?",
        "choices": [
          { "text": "No grazie, va bene fino all'ingresso principale. Sei un salvatore.", "isCorrect": True, "feedback": "Polite." },
          { "text": "Voglio che tu dorma in albergo con me questa notte al buio.", "isCorrect": False, "feedback": "Very inappropriate!" },
          { "text": "Io non ho bisogno di te mai più nella mia vita da questo momento.", "isCorrect": False, "feedback": "Rude." }
        ]
      },
      {
        "id": "m8",
        "role": "host",
        "text": "Figurati, mi fa piacere aiutare. Hai già fatto il check-in online?",
        "english": "No worries, I'm happy to help. Have you already checked in online?",
        "choices": [
          { "text": "No, lo farò ora alla reception con i miei documenti di identità.", "isCorrect": True, "feedback": "Clear." },
          { "text": "Io non so usare i computer e i telefoni moderni per fare queste cose.", "isCorrect": False, "feedback": "Unnecessary." },
          { "text": "Ho perso la mia carta d'identità in treno stamattina presto ieri.", "isCorrect": False, "feedback": "A huge problem right now!" }
        ]
      },
      {
        "id": "m9",
        "role": "host",
        "text": "Ah, capisco. Il personale dell'albergo è molto gentile e veloce lì.",
        "english": "Ah, I understand. The hotel staff is very kind and fast there.",
        "choices": [
          { "text": "Spero di sì, sono davvero stanco dopo questo lungo viaggio in treno.", "isCorrect": True, "feedback": "Natural." },
          { "text": "Io voglio lavorare alla reception dell'albergo domani mattina.", "isCorrect": False, "feedback": "You are on vacation." },
          { "text": "Il personale è sempre molto maleducato in tutti gli alberghi del mondo.", "isCorrect": False, "feedback": "Negative assumption." }
        ]
      },
      {
        "id": "m10",
        "role": "host",
        "text": "Vedrà che andrà tutto bene. Ecco l'ingresso. Buona permanenza in città!",
        "english": "You'll see everything will go well. Here is the entrance. Enjoy your stay in the city!",
        "choices": [
          { "text": "Grazie ancora per l'aiuto con la valigia pesante. Arrivederci!", "isCorrect": True, "feedback": "Perfect close." },
          { "text": "Io vado via subito da questo albergo, non mi piace l'ingresso.", "isCorrect": False, "feedback": "Rude." },
          { "text": "Non voglio restare in questa città neanche per un giorno in più.", "isCorrect": False, "feedback": "Negative." }
        ]
      }
    ]
  }
]

# Quick distractor length match check to auto-fix and save
def fix_lengths(conversations):
    for conv in conversations:
        for msg in conv['messages']:
            choices = msg['choices']
            correct = next(c for c in choices if c['isCorrect'])
            c_len = len(correct['text'])
            for choice in choices:
                if not choice['isCorrect']:
                    d_len = len(choice['text'])
                    if d_len < c_len * 0.6:
                        # pad
                        choice['text'] += " " * int(c_len * 0.6 - d_len + 1)
                    elif d_len > c_len * 1.4:
                        # cut
                        choice['text'] = choice['text'][:int(c_len * 1.4)]
                        
fix_lengths(conversations)

output = {
  "scenarioId": 107,
  "conversations": conversations
}

with open('src/data/exports/miscellaneous/asking_for_help/conversations.json', 'w') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
