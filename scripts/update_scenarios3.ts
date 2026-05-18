import * as fs from 'fs';

// ... (Copy all parts here, I will just paste the parts array since I already have it)
const allBlueprints = [
  {
    id: 1,
    phrases: [
      ['Dov\'è l\'uscita?', 'Where is the exit?'],
      ['Cerco il ritiro bagagli.', 'I am looking for the baggage claim.'],
      ['Dove prendo la navetta?', 'Where do I catch the shuttle?'],
      ['Il controllo passaporti è di qua.', 'Passport control is this way.'],
      ['Devo passare la dogana.', 'I need to go through customs.'],
      ['Qual è il mio terminal?', 'Which one is my terminal?']
    ],
    sentences: [
      ['Il mio volo è arrivato in ritardo.', 'My flight arrived late.', {grammarPoint: 'Using "essere" as auxiliary for "arrivare".'}],
      ['I bagagli non sono ancora sul nastro.', 'The luggage is not on the carousel yet.', {grammarPoint: 'Adverb "ancora" used with negative.'}],
      ['Mi scusi, dov\'è l\'uscita più vicina?', 'Excuse me, where is the nearest exit?', {grammarPoint: 'Superlative "più vicina".'}],
      ['La navetta per il centro parte ogni venti minuti.', 'The shuttle to the city center leaves every twenty minutes.', {grammarPoint: 'Present tense of "partire".'}],
      ['Ho solo un bagaglio a mano.', 'I only have a carry-on bag.', {grammarPoint: 'Using "avere" for possession.'}],
      ['Quanto ci vuole per raggiungere il terminal due?', 'How long does it take to reach terminal two?', {grammarPoint: 'Impersonal expression "ci vuole".'}]
    ]
  },
  {
    id: 2,
    phrases: [
      ['Sono qui in vacanza.', 'I am here on holiday.'],
      ['Viaggio per lavoro.', 'I am traveling for work.'],
      ['Mi fermo due settimane.', 'I am staying for two weeks.'],
      ['Ecco il mio passaporto.', 'Here is my passport.'],
      ['Qual è l\'indirizzo dell\'hotel?', 'What is the hotel address?'],
      ['Serve un permesso speciale?', 'Is a special permit required?']
    ],
    sentences: [
      ['Qual è il motivo della sua visita?', 'What is the purpose of your visit?', {grammarPoint: 'Formal "sua" (your).'}],
      ['Ho prenotato un hotel nel centro della città.', 'I booked a hotel in the city center.', {grammarPoint: 'Passato prossimo of "prenotare".'}],
      ['La durata del mio soggiorno è di dieci giorni.', 'The duration of my stay is ten days.', {grammarPoint: 'Use of preposition "di" for duration/amount.'}],
      ['Può mettere il timbro qui, per favore?', 'Could you put the stamp here, please?', {grammarPoint: 'Modal verb "potere" in formal address.'}],
      ['Non ho la residenza in Italia.', 'I do not have residency in Italy.', {grammarPoint: 'Negative statement with "non".'}],
      ['L\'indirizzo in cui alloggerò è via Roma venti.', 'The address where I will be staying is via Roma twenty.', {grammarPoint: 'Future tense of "alloggiare".'}]
    ]
  },
  {
    id: 3,
    phrases: [
      ['Non trovo la mia borsa.', 'I can\'t find my bag.'],
      ['La mia valigia è nera.', 'My suitcase is black.'],
      ['Dov\'è l\'ufficio bagagli?', 'Where is the baggage office?'],
      ['Ho perso la mia valigia.', 'I lost my suitcase.'],
      ['Questa è l\'etichetta del volo.', 'This is the flight tag.'],
      ['È una borsa grande.', 'It is a large bag.']
    ],
    sentences: [
      ['I bagagli del volo da Londra sono sul nastro tre.', 'The luggage from the London flight is on carousel three.', {grammarPoint: 'Plural article "I" for "bagagli".'}],
      ['Credo che la mia valigia sia andata persa.', 'I think my suitcase got lost.', {grammarPoint: 'Subjunctive after "credo che".'}],
      ['Mi può dare una descrizione del bagaglio smarrito?', 'Can you give me a description of the lost luggage?', {grammarPoint: 'Indirect object pronoun "mi".'}],
      ['La mia valigia è grande e nera, con un\'etichetta verde.', 'My suitcase is large and black, with a green tag.', {grammarPoint: 'Adjective agreement.'}],
      ['Dobbiamo compilare un modulo all\'ufficio bagagli.', 'We need to fill out a form at the baggage office.', {grammarPoint: 'Modal verb "dovere" + infinitive.'}],
      ['Speriamo che la ritrovino presto.', 'Let\'s hope they find it soon.', {grammarPoint: 'Subjunctive after "speriamo che".'}]
    ]
  },
  {
    id: 4,
    phrases: [
      ['Mi porti a questo indirizzo.', 'Take me to this address.'],
      ['Andiamo in centro.', 'We are going to the city center.'],
      ['Qual è la tariffa?', 'What is the fare?'],
      ['Giri a destra.', 'Turn right.'],
      ['Giri a sinistra al semaforo.', 'Turn left at the traffic light.'],
      ['Qui va bene, grazie.', 'Here is fine, thank you.']
    ],
    sentences: [
      ['Può accendere il tassametro, per favore?', 'Can you turn on the meter, please?', {grammarPoint: 'Imperative or polite request with "potere".'}],
      ['L\'indirizzo del mio hotel è vicino al centro.', 'My hotel\'s address is near the center.', {grammarPoint: 'Preposition "vicino a".'}],
      ['Quanto costa la corsa dall\'aeroporto alla città?', 'How much does the ride from the airport to the city cost?', {grammarPoint: 'Prepositions "da" and "a" combined with articles.'}],
      ['La prego di girare a destra alla prossima strada.', 'Please turn right at the next street.', {grammarPoint: 'Formal request with "La prego di".'}],
      ['Si fermi qui, qui va benissimo.', 'Stop here, here is perfectly fine.', {grammarPoint: 'Formal imperative of reflexive verb "fermarsi".'}],
      ['Mi serve una ricevuta per il lavoro.', 'I need a receipt for work.', {grammarPoint: 'Use of "servire" with indirect object pronoun.'}]
    ]
  },
  {
    id: 5,
    phrases: [
      ['Un biglietto di andata, per favore.', 'A one-way ticket, please.'],
      ['Un biglietto di andata e ritorno.', 'A return ticket.'],
      ['Vorrei un treno regionale.', 'I would like a regional train.'],
      ['C\'è una Freccia rossa alle due.', 'There is a high-speed train at two.'],
      ['Un posto in seconda classe.', 'A seat in second class.'],
      ['Devo obliterare il biglietto.', 'I have to validate the ticket.']
    ],
    sentences: [
      ['Posso comprare il biglietto alla macchinetta?', 'Can I buy the ticket at the machine?', {grammarPoint: 'Articulated preposition "alla".'}],
      ['Vorrei prenotare un posto sul treno delle tre.', 'I would like to reserve a seat on the three o\'clock train.', {grammarPoint: 'Conditional "vorrei" for polite requests.'}],
      ['Il biglietto per il regionale costa meno della Freccia.', 'The ticket for the regional train costs less than the high-speed one.', {grammarPoint: 'Comparative "meno di".'}],
      ['Non dimenticare di obliterare il biglietto prima di salire.', 'Do not forget to validate the ticket before boarding.', {grammarPoint: 'Negative imperative for "tu" (non + infinitive).'}],
      ['Viaggiamo in seconda classe perché è più economico.', 'We travel in second class because it is cheaper.', {grammarPoint: 'Preposition "in" with classes/categories.'}],
      ['Il posto che ho scelto è vicino al finestrino.', 'The seat I chose is near the window.', {grammarPoint: 'Relative pronoun "che".'}]
    ]
  },
  {
    id: 6,
    phrases: [
      ['Il treno parte dal binario due.', 'The train leaves from platform two.'],
      ['Dov\'è il sottopassaggio?', 'Where is the underpass?'],
      ['Devo fare un cambio a Roma.', 'I have to make a change in Rome.'],
      ['Ho perso la coincidenza.', 'I missed the connection.'],
      ['La mia carrozza è in fondo.', 'My coach is at the end.'],
      ['Ho un posto dal finestrino.', 'I have a window seat.']
    ],
    sentences: [
      ['Ascolta l\'annuncio, il nostro treno è in ritardo.', 'Listen to the announcement, our train is delayed.', {grammarPoint: 'Imperative form "ascolta".'}],
      ['Per raggiungere il binario due, devi prendere il sottopassaggio.', 'To reach platform two, you have to take the underpass.', {grammarPoint: 'Preposition "per" indicating purpose.'}],
      ['Se il treno è in ritardo, perderemo la coincidenza.', 'If the train is delayed, we will miss the connection.', {grammarPoint: 'First conditional (Se + present, future).'}],
      ['La carrozza numero cinque è vicino alla testa del treno.', 'Coach number five is near the front of the train.', {grammarPoint: 'Vocabulary for location.'}],
      ['Scusate, questo è il posto vicino al finestrino?', 'Excuse me, is this the window seat?', {grammarPoint: 'Interrogative structure.'}],
      ['Hanno appena fatto un annuncio per il cambio di binario.', 'They just made an announcement for the platform change.', {grammarPoint: 'Passato prossimo with "appena".'}]
    ]
  },
  {
    id: 7,
    phrases: [
      ['Dove trovo una tabaccheria?', 'Where can I find a tobacco shop?'],
      ['Vorrei un biglietto urbano.', 'I would like a city ticket.'],
      ['Devo validare il biglietto qui?', 'Do I have to validate the ticket here?'],
      ['Posso chiedere all\'autista.', 'I can ask the driver.'],
      ['Che linea devo prendere?', 'Which line should I take?'],
      ['Qual è l\'orario del bus?', 'What is the bus schedule?']
    ],
    sentences: [
      ['Puoi comprare i biglietti urbani in quella tabaccheria.', 'You can buy city tickets in that tobacco shop.', {grammarPoint: 'Demonstrative adjective "quella".'}],
      ['Scusi autista, è questa la fermata giusta per il museo?', 'Excuse me driver, is this the right stop for the museum?', {grammarPoint: 'Vocative and inversion in question.'}],
      ['Ricordati di validare il biglietto appena sali sull\'autobus.', 'Remember to validate the ticket as soon as you board the bus.', {grammarPoint: 'Reflexive imperative "ricordati".'}],
      ['La linea cinquantatré va in direzione dello stadio.', 'Line fifty-three goes in the direction of the stadium.', {grammarPoint: 'Articulated preposition "dello".'}],
      ['Sull\'orario del bus c\'è scritto che passa ogni dieci minuti.', 'On the bus schedule it says it comes every ten minutes.', {grammarPoint: 'Expression "c\'è scritto" (it is written).'}],
      ['Ho paura di aver sbagliato direzione.', 'I am afraid I went the wrong direction.', {grammarPoint: 'Infinitive past "aver sbagliato" after preposition "di".'}]
    ]
  },
  {
    id: 8,
    phrases: [
      ['Prendo la linea rossa.', 'I take the red line.'],
      ['Devo cambiare alla linea verde.', 'I need to change to the green line.'],
      ['Dov\'è il cambio metro?', 'Where is the metro transfer?'],
      ['Prendiamo l\'uscita metro a destra.', 'Let\'s take the metro exit on the right.'],
      ['Le scale sono di là.', 'The stairs are over there.'],
      ['Compro il biglietto alla biglietteria.', 'I buy the ticket at the ticket office.']
    ],
    sentences: [
      ['C\'è una mappa della metro sul muro.', 'There is a metro map on the wall.', {grammarPoint: 'Use of "c\'è".'}],
      ['Il capolinea della linea rossa è molto lontano.', 'The last stop of the red line is very far.', {grammarPoint: 'Noun "capolinea" (invariable).'}],
      ['Per il centro devi prendere la linea verde e poi fare il cambio metro.', 'For the center you must take the green line and then make the metro transfer.', {grammarPoint: 'Conjunction "e poi".'}],
      ['L\'uscita della metro è in cima alle scale.', 'The metro exit is at the top of the stairs.', {grammarPoint: 'Expression "in cima a".'}],
      ['La biglietteria è chiusa, usa la macchinetta.', 'The ticket office is closed, use the machine.', {grammarPoint: 'Adjective "chiusa" agreeing with feminine noun.'}],
      ['Mi sono perso cercando il cambio per la linea rossa.', 'I got lost looking for the transfer for the red line.', {grammarPoint: 'Gerund "cercando" expressing while doing something.'}]
    ]
  },
  {
    id: 9,
    phrases: [
      ['Vada dritto per questa strada.', 'Go straight on this street.'],
      ['Giri l\'angolo a destra.', 'Turn the corner to the right.'],
      ['Ci fermiamo al semaforo.', 'We stop at the traffic light.'],
      ['Passi il ponte vecchio.', 'Cross the old bridge.'],
      ['La piazza è molto vicina.', 'The square is very near.'],
      ['Possiamo andarci a piedi.', 'We can go there on foot.']
    ],
    sentences: [
      ['Mi scusi, sa dov\'è la piazza principale?', 'Excuse me, do you know where the main square is?', {grammarPoint: 'Formal "sa" (do you know).'}],
      ['Vada dritto e poi giri l\'angolo dopo il semaforo.', 'Go straight and then turn the corner after the traffic light.', {grammarPoint: 'Formal imperatives "vada" and "giri".'}],
      ['Il museo è troppo lontano per andarci a piedi?', 'Is the museum too far to go on foot?', {grammarPoint: 'Pronoun "ci" meaning "there".'}],
      ['Attraversi il ponte e la farmacia sarà vicino alla banca.', 'Cross the bridge and the pharmacy will be near the bank.', {grammarPoint: 'Future tense "sarà".'}],
      ['Siamo vicini al centro o è ancora lontano?', 'Are we near the center or is it still far?', {grammarPoint: 'Adjective agreement "vicini".'}],
      ['Se cammina a piedi, ci vorranno venti minuti.', 'If you walk on foot, it will take twenty minutes.', {grammarPoint: 'Future impersonal "ci vorranno".'}]
    ]
  },
  {
    id: 10,
    phrases: [
      ['Ho la patente internazionale.', 'I have an international driver\'s license.'],
      ['Vorrei l\'assicurazione completa.', 'I would like full insurance.'],
      ['Quest\'auto va a benzina o diesel?', 'Does this car take gasoline or diesel?'],
      ['Preferisco un cambio manuale.', 'I prefer a manual transmission.'],
      ['Quanto è il deposito cauzionale?', 'How much is the security deposit?'],
      ['C\'è un graffio sulla portiera.', 'There is a scratch on the door.']
    ],
    sentences: [
      ['Devo mostrare la mia patente e una carta di credito.', 'I must show my driver\'s license and a credit card.', {grammarPoint: 'Use of modal "devo".'}],
      ['Il contratto include l\'assicurazione contro i danni.', 'The contract includes insurance against damages.', {grammarPoint: 'Preposition "contro".'}],
      ['Se sceglie un\'auto a diesel, consumerà meno in autostrada.', 'If you choose a diesel car, you will consume less on the highway.', {grammarPoint: 'First conditional.'}],
      ['Non so guidare una macchina con il cambio manuale.', 'I don\'t know how to drive a car with manual transmission.', {grammarPoint: 'Verb "sapere" + infinitive (to know how to).'}],
      ['Il deposito le sarà rimborsato alla fine del noleggio.', 'The deposit will be refunded to you at the end of the rental.', {grammarPoint: 'Passive voice in the future "sarà rimborsato".'}],
      ['Ho notato un piccolo graffio prima di firmare il contratto.', 'I noticed a small scratch before signing the contract.', {grammarPoint: 'Preposition "prima di" + infinitive.'}]
    ]
  },
  {
    id: 11,
    phrases: [
      ['Vorrei fare il pieno.', 'I would like to fill the tank.'],
      ['Faccio al self service.', 'I\'ll use the self service.'],
      ['Questo è il distributore servito.', 'This is the attended service pump.'],
      ['Quale pompa devo usare?', 'Which pump should I use?'],
      ['Solo benzina senza piombo.', 'Only unleaded gas.'],
      ['Controlla la pressione delle gomme.', 'Check the tire pressure.']
    ],
    sentences: [
      ['Mi faccia il pieno di benzina senza piombo, per favore.', 'Fill it up with unleaded gas, please.', {grammarPoint: 'Formal imperative "faccia".'}],
      ['Ho messo venti litri di diesel al self service.', 'I put twenty liters of diesel at the self service.', {grammarPoint: 'Past participle "messo".'}],
      ['Può controllare anche la pressione delle gomme e l\'olio?', 'Can you also check the tire pressure and the oil?', {grammarPoint: 'Conjunction "anche".'}],
      ['La pompa numero quattro è fuori servizio.', 'Pump number four is out of order.', {grammarPoint: 'Expression "fuori servizio".'}],
      ['Il servizio servito costa leggermente di più del self service.', 'Attended service costs slightly more than self service.', {grammarPoint: 'Comparative "di più di".'}],
      ['Posso avere lo scontrino per il rifornimento?', 'Can I have the receipt for the refueling?', {grammarPoint: 'Request with "posso avere".'}]
    ]
  },
  {
    id: 12,
    phrases: [
      ['Cerco un parcheggio coperto.', 'I am looking for covered parking.'],
      ['Le strisce blu sono a pagamento.', 'Blue lines are paid parking.'],
      ['Devo prendere il ticket parcheggio.', 'I need to get the parking ticket.'],
      ['Costa due euro all\'ora.', 'It costs two euros an hour.'],
      ['Non voglio prendere una multa.', 'I don\'t want to get a fine.'],
      ['C\'è un posto libero laggiù.', 'There is a free spot over there.']
    ],
    sentences: [
      ['Ho lasciato la macchina nel garage sotterraneo.', 'I left the car in the underground garage.', {grammarPoint: 'Preposition "in" + article = "nel".'}],
      ['Serve un permesso speciale per parcheggiare in questa zona.', 'A special permit is needed to park in this area.', {grammarPoint: 'Use of "servire" as "to be needed".'}],
      ['Se parcheggi sulle strisce blu, devi comprare il ticket parcheggio.', 'If you park on the blue lines, you have to buy a parking ticket.', {grammarPoint: 'Preposition "su" + article = "sulle".'}],
      ['Il cartello dice che possiamo sostare solo per un\'ora.', 'The sign says we can only park for an hour.', {grammarPoint: 'Verb "sostare" for parking.'}],
      ['Mi hanno fatto una multa perché non avevo il permesso.', 'They gave me a fine because I didn\'t have the permit.', {grammarPoint: 'Imperfect tense "avevo".'}],
      ['Meno male che abbiamo trovato un posto libero subito.', 'Thank goodness we found a free spot right away.', {grammarPoint: 'Expression "Meno male che".'}]
    ]
  },
  {
    id: 13,
    phrases: [
      ['Mi scusi, mi sono perso.', 'Excuse me, I am lost.'],
      ['Cerco l\'indirizzo dell\'hotel.', 'I am looking for the hotel address.'],
      ['Ho il telefono scarico.', 'My phone is dead.'],
      ['Dov\'è la stazione di polizia?', 'Where is the police station?'],
      ['Ho una mappa offline sul tablet.', 'I have an offline map on my tablet.'],
      ['Può aiutarmi, per favore?', 'Can you help me, please?']
    ],
    sentences: [
      ['Non conosco questa zona, mi sono perso.', 'I do not know this area, I am lost.', {grammarPoint: 'Reflexive verb "perdersi".'}],
      ['Il mio telefono è scarico e non posso chiamare nessuno.', 'My phone is dead and I cannot call anyone.', {grammarPoint: 'Adjective "scarico" for electronics.'}],
      ['Qualcuno può aiutarmi a ritornare in centro?', 'Can someone help me get back to the city center?', {grammarPoint: 'Pronoun "qualcuno".'}],
      ['Non trovo l\'indirizzo dell\'hotel, ho solo il nome.', 'I cannot find the hotel address, I only have the name.', {grammarPoint: 'Use of "trovare".'}],
      ['Meno male che ho scaricato una mappa offline di questa zona.', 'Thank goodness I downloaded an offline map of this area.', {grammarPoint: 'Passato prossimo of "scaricare".'}],
      ['Dovremmo chiedere indicazioni alla polizia locale.', 'We should ask the local police for directions.', {grammarPoint: 'Conditional "dovremmo".'}]
    ]
  },
  {
    id: 14,
    phrases: [
      ['A che ora parte il traghetto?', 'What time does the ferry leave?'],
      ['Il porto è molto grande.', 'The port is very big.'],
      ['Andiamo sull\'isola per il fine settimana.', 'We are going to the island for the weekend.'],
      ['Preferisco stare sul ponte.', 'I prefer to stay on the deck.'],
      ['Abbiamo prenotato una cabina.', 'We booked a cabin.'],
      ['Inizia l\'imbarco dei passeggeri.', 'Passenger boarding is starting.']
    ],
    sentences: [
      ['Vorrei due biglietti per il traghetto verso l\'isola.', 'I would like two ferry tickets to the island.', {grammarPoint: 'Preposition "verso".'}],
      ['L\'orario del traghetto è cambiato a causa del mare mosso.', 'The ferry time changed due to rough seas.', {grammarPoint: 'Expression "a causa di".'}],
      ['L\'imbarco inizia un\'ora prima della partenza.', 'Boarding starts an hour before departure.', {grammarPoint: 'Preposition "prima di".'}],
      ['Abbiamo preso una cabina perché il viaggio dura tutta la notte.', 'We got a cabin because the trip lasts all night.', {grammarPoint: 'Expression "tutta la notte".'}],
      ['Fa freddo sul ponte, rientriamo.', 'It is cold on the deck, let\'s go back inside.', {grammarPoint: 'Impersonal "fa freddo".'}],
      ['Dobbiamo arrivare al porto in anticipo.', 'We must arrive at the port early.', {grammarPoint: 'Expression "in anticipo".'}]
    ]
  },
  {
    id: 15,
    phrases: [
      ['Vorrei noleggiare una bicicletta.', 'I would like to rent a bicycle.'],
      ['Mi serve un casco.', 'I need a helmet.'],
      ['Come funziona il lucchetto?', 'How does the lock work?'],
      ['Ho lasciato una cauzione.', 'I left a deposit.'],
      ['Dov\'è la pista ciclabile?', 'Where is the bike lane?'],
      ['Il campanello è rotto.', 'The bell is broken.']
    ],
    sentences: [
      ['Il noleggio costa dieci euro e include un\'ora.', 'The rental costs ten euros and has one included hour.', {grammarPoint: 'Verb "includere".'}],
      ['A che ora devo fare la restituzione della bicicletta?', 'What time do I have to return the bicycle?', {grammarPoint: 'Noun "restituzione" (return).'}],
      ['Devo usare il lucchetto se la lascio in strada.', 'I have to use the lock if I leave it on the street.', {grammarPoint: 'Direct object pronoun "la".'}],
      ['La pista ciclabile è molto sicura per viaggiare.', 'The bike lane is very safe for traveling.', {grammarPoint: 'Adjective "sicura".'}],
      ['Se c\'è un pezzo rotto, le rimborsiamo la cauzione.', 'If there is a broken part, we will refund your deposit.', {grammarPoint: 'Indirect object pronoun "le" (to you, formal).'}],
      ['Non dimenticare il casco prima di partire.', 'Do not forget the helmet before leaving.', {grammarPoint: 'Negative imperative.'}]
    ]
  },
  {
    id: 16,
    phrases: [
      ['È un\'emergenza!', 'It is an emergency!'],
      ['Chiamate un\'ambulanza.', 'Call an ambulance.'],
      ['Voglio denunciare un furto.', 'I want to report a theft.'],
      ['Mi hanno rubato il portafoglio.', 'My wallet was stolen.'],
      ['Dov\'è la mia ambasciata?', 'Where is my embassy?'],
      ['Ho bisogno di aiuto subito.', 'I need help right away.']
    ],
    sentences: [
      ['Ho perso i documenti e devo contattare l\'ambasciata.', 'I lost my documents and I must contact the embassy.', {grammarPoint: 'Conjunction "e" joining clauses.'}],
      ['C\'è stato un furto in hotel la scorsa notte.', 'There was a theft in the hotel last night.', {grammarPoint: 'Passato prossimo of "esserci" (c\'è stato).'}],
      ['Bisogna chiamare la sicurezza subito.', 'We need to call security right away.', {grammarPoint: 'Impersonal verb "bisogna".'}],
      ['Devo fare una denuncia alla polizia per il mio portafoglio.', 'I must file a police report for my wallet.', {grammarPoint: 'Expression "fare una denuncia".'}],
      ['L\'ambulanza è arrivata in pochi minuti per l\'emergenza.', 'The ambulance arrived in a few minutes for the emergency.', {grammarPoint: 'Expression of time "in pochi minuti".'}],
      ['Per la sua sicurezza, non esca da solo stasera.', 'For your safety, do not go out alone tonight.', {grammarPoint: 'Formal negative imperative "non esca".'}]
    ]
  },
  {
    id: 17,
    phrases: [
      ['Vorrei fare il check-in.', 'I would like to check in.'],
      ['La prenotazione è a mio cognome.', 'The reservation is under my last name.'],
      ['Ho una camera singola.', 'I have a single room.'],
      ['Preferisco una camera doppia.', 'I prefer a double room.'],
      ['Ecco il mio passaporto.', 'Here is my passport.'],
      ['Qual è il codice della porta?', 'What is the door code?']
    ],
    sentences: [
      ['Per il check-in, mi serve il suo passaporto.', 'For check-in, I need your passport.', {grammarPoint: 'Formal possessive "suo".'}],
      ['Può mettere la sua firma su questo modulo?', 'Can you put your signature on this form?', {grammarPoint: 'Preposition "su" + demonstrative "questo".'}],
      ['La tassa di soggiorno non è inclusa nel prezzo.', 'The city tax is not included in the price.', {grammarPoint: 'Passive voice "non è inclusa".'}],
      ['Abbiamo riservato una camera doppia con vista mare.', 'We reserved a double room with a sea view.', {grammarPoint: 'Preposition "con".'}],
      ['Il codice per entrare verrà inviato via messaggio.', 'The code to enter will be sent via message.', {grammarPoint: 'Passive with "venire" in the future.'}],
      ['Mi può confermare il cognome della prenotazione?', 'Can you confirm the last name of the reservation?', {grammarPoint: 'Indirect object pronoun "mi".'}]
    ]
  },
  {
    id: 18,
    phrases: [
      ['Devo fare il check-out.', 'I need to check out.'],
      ['Non ho consumato niente dal minibar.', 'I didn\'t have anything from the minibar.'],
      ['Il pagamento è con carta.', 'The payment is by card.'],
      ['Vorrei una fattura.', 'I would like an invoice.'],
      ['Posso avere una ricevuta?', 'Can I have a receipt?'],
      ['Avete un deposito bagagli?', 'Do you have luggage storage?']
    ],
    sentences: [
      ['Entro che ora dobbiamo lasciare la camera libera?', 'By what time must we leave the room free?', {grammarPoint: 'Preposition "entro" (by).'}],
      ['Abbiamo fatto tardi, possiamo posticipare il check-out?', 'We are late, can we postpone the check-out?', {grammarPoint: 'Expression "fare tardi".'}],
      ['Posso lasciare la valigia nel deposito bagagli fino a stasera?', 'Can I leave my suitcase in the luggage storage until tonight?', {grammarPoint: 'Preposition "fino a".'}],
      ['Ho preso solo un\'acqua dal minibar questa mattina.', 'I only took a water from the minibar this morning.', {grammarPoint: 'Use of "solo".'}],
      ['Vorrei la fattura intestata alla mia azienda, per favore.', 'I would like the invoice made out to my company, please.', {grammarPoint: 'Past participle as adjective "intestata".'}],
      ['Il pagamento è andato a buon fine, ecco la ricevuta.', 'The payment was successful, here is the receipt.', {grammarPoint: 'Expression "andare a buon fine".'}]
    ]
  },
  {
    id: 19,
    phrases: [
      ['L\'aria condizionata non funziona.', 'The air conditioning does not work.'],
      ['Il riscaldamento è troppo alto.', 'The heating is too high.'],
      ['C\'è troppo rumore dalla strada.', 'There is too much noise from the street.'],
      ['La luce in bagno è rotta.', 'The light in the bathroom is broken.'],
      ['L\'acqua della doccia è fredda.', 'The shower water is cold.'],
      ['Vorrei cambiare camera.', 'I would like to change rooms.']
    ],
    sentences: [
      ['Il tappeto è sporco, potete pulirlo?', 'The rug is dirty, can you clean it?', {grammarPoint: 'Pronoun attached to infinitive "pulirlo".'}],
      ['C\'è un problema con l\'aria condizionata, fa troppo caldo.', 'There is a problem with the air conditioning, it is too hot.', {grammarPoint: 'Impersonal "fa caldo".'}],
      ['La doccia è rotta e l\'acqua non scende bene.', 'The shower is broken and the water doesn\'t drain well.', {grammarPoint: 'Adverb "bene".'}],
      ['Non riesco a dormire per il rumore, posso cambiare camera?', 'I can\'t sleep because of the noise, can I change rooms?', {grammarPoint: 'Preposition "per" expressing cause.'}],
      ['Mi dispiace, ma il riscaldamento sembra essere spento.', 'I am sorry, but the heating seems to be turned off.', {grammarPoint: 'Verb "sembrare" + infinitive.'}],
      ['La luce principale non si accende più.', 'The main light does not turn on anymore.', {grammarPoint: 'Reflexive verb "accendersi" and negative "non... più".'}]
    ]
  },
  {
    id: 20,
    phrases: [
      ['Manca il sapone in bagno.', 'There is no soap in the bathroom.'],
      ['Ci serve altra carta igienica.', 'We need more toilet paper.'],
      ['Posso avere una coperta?', 'Can I have a blanket?'],
      ['Il mio cuscino è scomodo.', 'My pillow is uncomfortable.'],
      ['A che ora passano per la pulizia?', 'What time do they come for cleaning?'],
      ['Vorrei degli asciugamani puliti.', 'I would like some clean towels.']
    ],
    sentences: [
      ['Ci può portare degli asciugamani puliti, per favore?', 'Can you bring us some clean towels, please?', {grammarPoint: 'Indirect object pronoun "ci" and partitive "degli".'}],
      ['Abbiamo bisogno di più carta igienica e sapone.', 'We need more toilet paper and soap.', {grammarPoint: 'Expression "avere bisogno di".'}],
      ['Fa molto freddo, avrei bisogno di una coperta in più.', 'It is very cold, I would need an extra blanket.', {grammarPoint: 'Conditional "avrei".'}],
      ['Il phon in camera non si accende.', 'The hair dryer in the room does not turn on.', {grammarPoint: 'Reflexive verb "accendersi".'}],
      ['Le mando qualcuno per la pulizia della stanza subito.', 'I will send someone for the room cleaning right away.', {grammarPoint: 'Indirect object pronoun "Le" (to you, formal).'}],
      ['Posso chiedere un cuscino più morbido?', 'Can I ask for a softer pillow?', {grammarPoint: 'Comparative "più morbido".'}]
    ]
  },
  {
    id: 21,
    phrases: [
      ['Dov\'è il buffet della colazione?', 'Where is the breakfast buffet?'],
      ['Vorrei un succo di frutta.', 'I would like a fruit juice.'],
      ['Questo cornetto è buonissimo.', 'This croissant is delicious.'],
      ['Vorrei delle uova strapazzate.', 'I would like some scrambled eggs.'],
      ['C\'è del formaggio fresco?', 'Is there fresh cheese?'],
      ['Avete prodotti senza glutine?', 'Do you have gluten-free products?']
    ],
    sentences: [
      ['A che ora finisce l\'orario colazione?', 'What time does the breakfast time end?', {grammarPoint: 'Present tense of "finire" (-isc- verb).'}],
      ['La sala della colazione si trova al piano terra.', 'The breakfast room is located on the ground floor.', {grammarPoint: 'Reflexive verb "trovarsi" for location.'}],
      ['Posso avere un cappuccino e un cornetto vuoto?', 'Can I have a cappuccino and a plain croissant?', {grammarPoint: 'Adjective "vuoto".'}],
      ['Offrite opzioni senza glutine nel vostro buffet?', 'Do you offer gluten-free options in your buffet?', {grammarPoint: 'Possessive adjective "vostro".'}],
      ['Vorrei due uova e un po\' di formaggio, grazie.', 'I would like two eggs and a bit of cheese, thank you.', {grammarPoint: 'Partitive expression "un po\' di".'}],
      ['Il succo d\'arancia è appena spremuto?', 'Is the orange juice freshly squeezed?', {grammarPoint: 'Adverb "appena" with past participle.'}]
    ]
  },
  {
    id: 22,
    phrases: [
      ['Ho affittato questo appartamento.', 'I rented this apartment.'],
      ['Sto aspettando l\'host.', 'I am waiting for the host.'],
      ['A quale nome devo suonare sul citofono?', 'Which name should I ring on the intercom?'],
      ['Il portone è chiuso.', 'The building door is closed.'],
      ['Questa serratura è dura.', 'This lock is stiff.'],
      ['Dove avviene la consegna chiavi?', 'Where does the key handoff happen?']
    ],
    sentences: [
      ['L\'host mi ha inviato le regole della casa via mail.', 'The host sent me the house rules via email.', {grammarPoint: 'Passato prossimo with indirect object pronoun "mi".'}],
      ['Il codice porta per entrare è nel messaggio.', 'The door code to enter is in the message.', {grammarPoint: 'Preposition "in" + article = "nel".'}],
      ['Devo digitare il codice e poi suonare il citofono.', 'I have to type the code and then ring the intercom.', {grammarPoint: 'Sequence "e poi".'}],
      ['La serratura fa un po\' di fatica ad aprirsi.', 'The lock struggles a bit to open.', {grammarPoint: 'Expression "fare fatica a".'}],
      ['Incontrerò l\'host per la consegna chiavi alle tre.', 'I will meet the host for the key handoff at three.', {grammarPoint: 'Future tense of "incontrare".'}],
      ['Assicurati di chiudere il portone quando esci.', 'Make sure to close the building door when you leave.', {grammarPoint: 'Imperative reflexive "assicurati di".'}]
    ]
  },
  {
    id: 23,
    phrases: [
      ['Qual è la rete dell\'hotel?', 'What is the hotel\'s network?'],
      ['Posso avere la password wifi?', 'Can I have the Wi-Fi password?'],
      ['Il segnale è molto debole.', 'The signal is very weak.'],
      ['Internet è davvero lento.', 'The internet is really slow.'],
      ['Il Wi-Fi non funziona in camera.', 'The Wi-Fi does not work in the room.'],
      ['Dov\'è il router?', 'Where is the router?']
    ],
    sentences: [
      ['Il segnale è migliore al piano terra vicino alla reception.', 'The signal is better on the ground floor near the reception.', {grammarPoint: 'Comparative "migliore".'}],
      ['Può controllare se la password wifi è corretta?', 'Can you check if the Wi-Fi password is correct?', {grammarPoint: 'Conjunction "se".'}],
      ['Le consiglio di riprovare a connettersi tra cinque minuti.', 'I advise you to try connecting again in five minutes.', {grammarPoint: 'Expression "riprovare a" + infinitive.'}],
      ['La rete è caduta, forse devono riavviare il router.', 'The network went down, maybe they have to restart the router.', {grammarPoint: 'Past participle "caduta" with "essere".'}],
      ['Mi dispiace, ma la connessione internet è molto lenta oggi.', 'I am sorry, but the internet connection is very slow today.', {grammarPoint: 'Adverb "molto" as an intensifier.'}],
      ['Non riesco a collegarmi, la pagina non funziona.', 'I cannot connect, the page does not work.', {grammarPoint: 'Reflexive verb "collegarsi".'}]
    ]
  },
  {
    id: 24,
    phrases: [
      ['Avete un servizio lavanderia?', 'Do you have a laundry service?'],
      ['La lavatrice è occupata.', 'The washing machine is occupied.'],
      ['Posso usare l\'asciugatrice?', 'Can I use the dryer?'],
      ['Dove trovo il detersivo?', 'Where do I find the detergent?'],
      ['Questa camicia va lavata a freddo.', 'This shirt must be washed cold.'],
      ['Le serve per domani mattina.', 'You need it by tomorrow morning.']
    ],
    sentences: [
      ['Qual è il prezzo lavaggio per tre camicie?', 'What is the washing price for three shirts?', {grammarPoint: 'Irregular plural "camicie".'}],
      ['Ho bisogno dei vestiti puliti per domani mattina.', 'I need the clean clothes for tomorrow morning.', {grammarPoint: 'Preposition "per" for deadlines.'}],
      ['L\'hotel offre anche un servizio per stirare i vestiti?', 'Does the hotel also offer a service to iron clothes?', {grammarPoint: 'Verb "offrire" in present tense.'}],
      ['Devo comprare il detersivo o è incluso?', 'Do I have to buy detergent or is it included?', {grammarPoint: 'Adjective "incluso".'}],
      ['Se metti tutto nell\'asciugatrice, si restringe.', 'If you put everything in the dryer, it will shrink.', {grammarPoint: 'Reflexive verb "restringersi".'}],
      ['La lavanderia automatica è in fondo alla strada.', 'The laundromat is down the street.', {grammarPoint: 'Expression "in fondo a".'}]
    ]
  },
  {
    id: 25,
    phrases: [
      ['Vorrei prolungare il mio soggiorno.', 'I would like to extend my stay.'],
      ['Resto un\'altra notte.', 'I am staying one more night.'],
      ['Avete una camera disponibile?', 'Do you have a room available?'],
      ['Posso avere lo stesso prezzo?', 'Can I get the same price?'],
      ['Non vorrei cambiare stanza.', 'I wouldn\'t want to change rooms.'],
      ['Aspetto la sua conferma.', 'I am waiting for your confirmation.']
    ],
    sentences: [
      ['È possibile prolungare la prenotazione per un\'altra notte?', 'Is it possible to extend the reservation for one more night?', {grammarPoint: 'Impersonal structure "È possibile" + infinitive.'}],
      ['Dobbiamo controllare il calendario per vedere se c\'è posto.', 'We must check the calendar to see if there is space.', {grammarPoint: 'Use of "c\'è posto".'}],
      ['Siamo in alta stagione, quindi la tariffa potrebbe aumentare.', 'We are in high season, so the rate might increase.', {grammarPoint: 'Conditional "potrebbe".'}],
      ['Se rimane, le possiamo offrire lo stesso prezzo.', 'If you stay, we can offer you the same price.', {grammarPoint: 'First conditional with formal "le".'}],
      ['Mi faccia sapere quando riceve la conferma dall\'hotel.', 'Let me know when you receive confirmation from the hotel.', {grammarPoint: 'Causative construction "faccia sapere".'}],
      ['Purtroppo deve cambiare stanza perché questa è già prenotata.', 'Unfortunately you have to change rooms because this one is already booked.', {grammarPoint: 'Adverb "già".'}]
    ]
  },
  {
    id: 26,
    phrases: [
      ['Dormo in un ostello stanotte.', 'I am sleeping in a hostel tonight.'],
      ['Ho il letto a castello sopra.', 'I have the top bunk bed.'],
      ['Dov\'è il mio armadietto?', 'Where is my locker?'],
      ['Il bagno condiviso è in fondo.', 'The shared bathroom is at the end.'],
      ['Possiamo usare la cucina comune.', 'We can use the shared kitchen.'],
      ['Serve un lucchetto per l\'armadietto.', 'A lock is needed for the locker.']
    ],
    sentences: [
      ['In questo ostello, dopo le undici c\'è l\'obbligo del silenzio.', 'In this hostel, after eleven there is a quiet rule.', {grammarPoint: 'Noun "obbligo".'}],
      ['Le lenzuola sono incluse nel prezzo del letto a castello.', 'Sheets are included in the price of the bunk bed.', {grammarPoint: 'Feminine plural noun "lenzuola" (irregular).'}],
      ['Se vuoi cucinare, la cucina comune è aperta fino a tardi.', 'If you want to cook, the shared kitchen is open until late.', {grammarPoint: 'Expression "fino a tardi".'}],
      ['Ricordati di portare un lucchetto per chiudere le tue cose.', 'Remember to bring a lock to secure your things.', {grammarPoint: 'Reflexive imperative "ricordati".'}],
      ['Il bagno condiviso viene pulito due volte al giorno.', 'The shared bathroom is cleaned twice a day.', {grammarPoint: 'Passive voice with "venire".'}],
      ['C\'è molto rumore, spero che facciano silenzio presto.', 'There is a lot of noise, I hope they get quiet soon.', {grammarPoint: 'Subjunctive "facciano" after "spero che".'}]
    ]
  },
  {
    id: 27,
    phrases: [
      ['Vorrei prenotare un tavolo.', 'I would like to reserve a table.'],
      ['Un tavolo per due persone.', 'A table for two people.'],
      ['Prenoto per stasera alle otto.', 'I reserve for tonight at eight.'],
      ['Qual è il nome prenotazione?', 'What is the reservation name?'],
      ['Preferiamo mangiare in terrazza.', 'We prefer to eat on the terrace.'],
      ['Se è occupato, va bene all\'interno.', 'If it\'s busy, inside is fine.']
    ],
    sentences: [
      ['Vorrei prenotare un tavolo per due persone alle otto.', 'I would like to book a table for two people at eight o\'clock.', {grammarPoint: 'Telling time "alle otto".'}],
      ['Potete confermare la prenotazione a nome di Rossi?', 'Can you confirm the reservation under the name Rossi?', {grammarPoint: 'Expression "a nome di".'}],
      ['Mi dispiace, ma la terrazza è già tutta prenotata.', 'I am sorry, but the terrace is already fully booked.', {grammarPoint: 'Adjective "tutta" agreeing with the noun.'}],
      ['Il locale è occupato, dovete aspettare venti minuti.', 'The place is busy, you have to wait twenty minutes.', {grammarPoint: 'Modal verb "dovete".'}],
      ['Abbiamo un tavolo libero all\'interno, vicino alla finestra.', 'We have a free table inside, near the window.', {grammarPoint: 'Prepositional phrase "vicino a".'}],
      ['Chiamo per confermare il nostro tavolo di questa sera.', 'I am calling to confirm our table for this evening.', {grammarPoint: 'Preposition "per" indicating purpose.'}]
    ]
  },
  {
    id: 28,
    phrases: [
      ['Un espresso, per favore.', 'An espresso, please.'],
      ['Vorrei un cappuccino.', 'I would like a cappuccino.'],
      ['Prendo un caffè macchiato.', 'I\'ll take a macchiato.'],
      ['Dov\'è lo zucchero?', 'Where is the sugar?'],
      ['Beviamo il caffè al banco.', 'Let\'s drink coffee at the counter.'],
      ['Vorrei anche un cornetto.', 'I would also like a croissant.']
    ],
    sentences: [
      ['In Italia, di solito non si beve il cappuccino dopo pranzo.', 'In Italy, one usually does not drink cappuccino after lunch.', {grammarPoint: 'Impersonal "si beve".'}],
      ['Vorrei il mio macchiato in una tazza di vetro.', 'I would like my macchiato in a glass cup.', {grammarPoint: 'Preposition "di" indicating material.'}],
      ['Mi scusi, posso avere un bicchiere di latte freddo?', 'Excuse me, can I have a glass of cold milk?', {grammarPoint: 'Adjective placement after the noun.'}],
      ['Consumiamo al banco così paghiamo di meno.', 'We are consuming at the counter so we pay less.', {grammarPoint: 'Conjunction "così".'}],
      ['Questo cornetto alla crema è molto buono senza zucchero.', 'This cream croissant is very good without sugar.', {grammarPoint: 'Preposition "alla" to indicate flavor.'}],
      ['Preferisco un espresso macchiato caldo invece che freddo.', 'I prefer a hot macchiato espresso rather than cold.', {grammarPoint: 'Expression "invece che".'}]
    ]
  },
  {
    id: 29,
    phrases: [
      ['Una pizza margherita, per favore.', 'A margherita pizza, please.'],
      ['Vorrei una pizza ai funghi.', 'I would like a mushroom pizza.'],
      ['Una pizza con prosciutto e mozzarella.', 'A pizza with ham and mozzarella.'],
      ['C\'è troppo pomodoro.', 'There is too much tomato.'],
      ['Mi piace l\'olio piccante.', 'I like spicy oil.'],
      ['È una pizza da portare via?', 'Is it a pizza to go?']
    ],
    sentences: [
      ['La vera pizza ha solo pomodoro fresco e mozzarella.', 'Real pizza has only fresh tomato and mozzarella.', {grammarPoint: 'Adverb "solo".'}],
      ['Vorrei due pizze margherita da portare via, per favore.', 'I would like two margherita pizzas to go, please.', {grammarPoint: 'Invariable noun "margherita" or used as an adjective.'}],
      ['Potete aggiungere dei funghi extra sulla mia pizza?', 'Can you add some extra mushrooms on my pizza?', {grammarPoint: 'Partitive "dei" (some).'}],
      ['Questa pizza al prosciutto è appena uscita dal forno.', 'This ham pizza just came out of the oven.', {grammarPoint: 'Expression "appena uscita".'}],
      ['Attenzione, l\'olio sulla tavola è molto piccante.', 'Careful, the oil on the table is very spicy.', {grammarPoint: 'Interjection "attentione".'}],
      ['Preferisco la cottura nel forno a legna.', 'I prefer baking in a wood-fired oven.', {grammarPoint: 'Noun phrase "forno a legna".'}]
    ]
  },
  {
    id: 30,
    phrases: [
      ['Vorrei un piatto di spaghetti.', 'I would like a plate of spaghetti.'],
      ['Prendo le penne al sugo.', 'I\'ll take the penne with sauce.'],
      ['C\'è del ragù di carne?', 'Is there meat sauce?'],
      ['Una carbonara, per favore.', 'A carbonara, please.'],
      ['Mi passi il parmigiano?', 'Can you pass me the parmesan?'],
      ['La pasta è al dente.', 'The pasta is firm to the bite.']
    ],
    sentences: [
      ['La porzione di spaghetti è molto abbondante.', 'The portion of spaghetti is very generous.', {grammarPoint: 'Adjective "abbondante".'}],
      ['La carbonara originale non ha la panna.', 'Original carbonara does not have cream.', {grammarPoint: 'Negative structure with "non".'}],
      ['Cameriere, può portare altro parmigiano per le penne?', 'Waiter, can you bring more parmesan for the penne?', {grammarPoint: 'Indefinite adjective "altro".'}],
      ['Amo quando la pasta è cucinata perfettamente al dente.', 'I love it when the pasta is cooked perfectly al dente.', {grammarPoint: 'Adverb "perfettamente".'}],
      ['Il sugo al ragù deve cuocere per molte ore.', 'Meat sauce must cook for many hours.', {grammarPoint: 'Preposition "per" for duration.'}],
      ['Posso avere mezza porzione di pasta per favore?', 'Can I have a half portion of pasta please?', {grammarPoint: 'Adjective "mezza" agreeing with feminine noun.'}]
    ]
  },
  {
    id: 31,
    phrases: [
      ['Vorrei un gelato.', 'I would like an ice cream.'],
      ['Cono o coppetta?', 'Cone or cup?'],
      ['Quali gusti avete?', 'Which flavors do you have?'],
      ['Vorrei due gusti.', 'I would like two flavors.'],
      ['Un cono piccolo, per favore.', 'A small cone, please.'],
      ['Panna montata sopra?', 'Whipped cream on top?']
    ],
    sentences: [
      ['Prendo un cono con cioccolato e pistacchio.', "I'll take a cone with chocolate and pistachio.", {grammarPoint: 'Using "con" to combine flavors.'}],
      ['Mi dà una coppetta alla fragola?', 'Can I have a strawberry cup?', {grammarPoint: 'Using "alla" to specify flavor.'}],
      ['Il pistacchio di Bronte è delizioso.', 'The pistachio from Bronte is delicious.', {grammarPoint: 'Subject-adjective agreement.'}],
      ['Vorrei assaggiare il gusto del mese.', 'I would like to taste the flavor of the month.', {grammarPoint: 'Usage of "vorrei" + infinitive.'}],
      ['Senza panna, grazie.', 'Without cream, thank you.', {grammarPoint: 'Preposition "senza" for exclusion.'}],
      ['È possibile avere tre gusti in questo cono?', 'Is it possible to have three flavors in this cone?', {grammarPoint: 'Asking for possibilities with "è possibile".'}]
    ]
  },
  {
    id: 32,
    phrases: [
      ['Il conto, per favore.', 'The bill, please.'],
      ['Possiamo pagare?', 'Can we pay?'],
      ['Accettate il bancomat?', 'Do you accept debit cards?'],
      ['Paghiamo insieme.', "We're paying together."],
      ['Ecco la mancia.', 'Here is the tip.'],
      ['Dov\'è il POS?', 'Where is the card terminal?']
    ],
    sentences: [
      ['Possiamo dividere il conto a metà?', 'Can we split the bill in half?', {grammarPoint: 'Verb "dividere" in a question.'}],
      ['Il servizio è incluso nel totale?', 'Is service included in the total?', {grammarPoint: 'Passive construction con "è incluso".'}],
      ['Vorrei pagare con la carta, grazie.', 'I would like to pay by card, thank you.', {grammarPoint: 'Using "con" for payment method.'}],
      ['Facciamo conti separati, per favore.', 'Separate bills, please.', {grammarPoint: 'Common expression "conti separati".'}],
      ['Posso avere lo scontrino?', 'Can I have the receipt?', {grammarPoint: 'Direct object "lo scontrino".'}],
      ['Mi scusi, credo ci sia un errore nel conto.', 'Excuse me, I think there is a mistake in the bill.', {grammarPoint: 'Polite complaint with "credo ci sia".'}]
    ]
  },
  {
    id: 33,
    phrases: [
      ['Sono allergico alle arachidi.', 'I am allergic to peanuts.'],
      ['C\'è del latte in questo piatto?', 'Is there milk in this dish?'],
      ['È senza glutine?', 'Is it gluten-free?'],
      ['Quali sono gli ingredienti?', 'What are the ingredients?'],
      ['Sono molto allergico alle uova.', 'I am very allergic to eggs.'],
      ['Può essere pericoloso per me.', 'It can be dangerous for me.']
    ],
    sentences: [
      ['Questo piatto contiene tracce di frutta a guscio?', 'Does this dish contain traces of nuts?', {grammarPoint: 'Formal inquiry about allergens.'}],
      ['Mi assicura che non ci sia farina?', 'Can you assure me there is no flour?', {grammarPoint: 'Subjunctive after "assicura che".'}],
      ['Ho un\'allergia grave ai latticini.', 'I have a severe allergy to dairy products.', {grammarPoint: 'Using "grave" to describe severity.'}],
      ['Potete preparare la pasta senza glutine?', 'Can you prepare the pasta gluten-free?', {grammarPoint: 'Asking for modifications.'}],
      ['La prego di informare lo chef della mia allergia.', 'Please inform the chef about my allergy.', {grammarPoint: 'Formal request using "La prego".'}],
      ['Cerco un\'alternativa sicura per mia figlia.', 'I am looking for a safe alternative for my daughter.', {grammarPoint: 'Usage of "per" for purpose/benefit.'}]
    ]
  },
  {
    id: 34,
    phrases: [
      ['Avete piatti vegetariani?', 'Do you have vegetarian dishes?'],
      ['Sono vegano.', 'I am vegan.'],
      ['Vorrei un\'insalata mista.', 'I would like a mixed salad.'],
      ['Senza carne né pesce, grazie.', 'Without meat or fish, thank you.'],
      ['Quali piatti hanno solo verdure?', 'Which dishes have only vegetables?'],
      ['C\'è il formaggio dentro?', 'Is there cheese inside?']
    ],
    sentences: [
      ['Posso avere questo piatto senza il formaggio?', 'Can I have this dish without the cheese?', {grammarPoint: 'Modifying a standard dish.'}],
      ['Avete dei primi piatti a base di legumi?', 'Do you have any first courses based on legumes?', {grammarPoint: 'Using "a base di" to describe main ingredients.'}],
      ['Questa zuppa è fatta con brodo di carne?', 'Is this soup made with meat broth?', {grammarPoint: 'Checking for hidden ingredients.'}],
      ['Vorrei un contorno di verdure grigliate.', 'I would like a side of grilled vegetables.', {grammarPoint: 'Specifying a side dish.'}],
      ['Ci sono opzioni vegane nel menù?', 'Are there vegan options on the menu?', {grammarPoint: 'Plural agreement for "opzioni vegane".'}],
      ['Preferisco mangiare piatti senza proteine animali.', 'I prefer to eat dishes without animal proteins.', {grammarPoint: 'Expressing dietary preference.'}]
    ]
  },
  {
    id: 35,
    phrases: [
      ['Un bicchiere di vino rosso, per favore.', 'A glass of red wine, please.'],
      ['Vorrei provare un vino locale.', 'I would like to try a local wine.'],
      ['È un vino secco o dolce?', 'Is it a dry or sweet wine?'],
      ['Cosa mi consiglia?', 'What do you recommend?'],
      ['Prendiamo una bottiglia?', 'Shall we take a bottle?'],
      ['Un bianco molto freddo, grazie.', 'A very cold white, thank you.']
    ],
    sentences: [
      ['Vorrei un vino rosso corposo della regione.', 'I would like a full-bodied red wine from the region.', {grammarPoint: 'Adjective "corposo" for wine.'}],
      ['Questo bianco è perfetto con il pesce.', 'This white is perfect with fish.', {grammarPoint: 'Pairing food and drink.'}],
      ['Posso assaggiare un goccio prima di ordinare?', 'Can I taste a drop before ordering?', {grammarPoint: 'Common bar request.'}],
      ['Ci porti anche un tagliere di salumi, per favore.', 'Bring us a platter of cold cuts too, please.', {grammarPoint: 'Using indirect object "ci".'}],
      ['Qual è il vostro vino della casa?', 'What is your house wine?', {grammarPoint: 'Interrogative "Qual è".'}],
      ['Cerco un vino dolce per accompagnare il dessert.', 'I am looking for a sweet wine to accompany the dessert.', {grammarPoint: 'Purpose using "per" + infinitive.'}]
    ]
  },
  {
    id: 36,
    phrases: [
      ['Vorrei un pezzo di focaccia.', 'I would like a piece of focaccia.'],
      ['È pane fresco di oggi?', 'Is it fresh bread from today?'],
      ['Ne prendo mezzo chilo.', "I'll take half a kilo."],
      ['Avete brioche alla crema?', 'Do you have cream-filled brioche?'],
      ['Due etti di questo, per favore.', 'Two hundred grams of this, please.'],
      ['Può tagliarlo a fette?', 'Can you slice it?']
    ],
    sentences: [
      ['Preferisco il pane integrale rispetto a quello bianco.', 'I prefer whole-grain bread over white bread.', {grammarPoint: 'Comparative "rispetto a".'}],
      ['Vorrei cento grammi di focaccia con le olive.', 'I would like a hundred grams of focaccia with olives.', {grammarPoint: 'Ordering by weight.'}],
      ['Questa brioche è appena uscita dal forno.', 'This brioche just came out of the oven.', {grammarPoint: 'Usage of "appena" for recent actions.'}],
      ['Mi dà un filone di pane non troppo cotto?', 'Can I have a loaf of bread that\'s not too baked?', {grammarPoint: 'Specifying cooking preference.'}],
      ['Quanta focaccia è rimasta?', 'How much focaccia is left?', {grammarPoint: 'Asking about remaining quantity.'}],
      ['Cerco una panetteria artigianale in questa zona.', 'I am looking for an artisanal bakery in this area.', {grammarPoint: 'Adjective agreement.'}]
    ]
  },
  {
    id: 37,
    phrases: [
      ['Un arancino al ragù, per favore.', 'An arancino with meat sauce, please.'],
      ['È pronto da mangiare?', 'Is it ready to eat?'],
      ['Vorrei un panino con la porchetta.', 'I would like a porchetta sandwich.'],
      ['Me lo scalda un po\'?', 'Can you heat it up for me?'],
      ['Senza salse, grazie.', 'Without sauces, thank you.'],
      ['Due supplì classici.', 'Two classic supplì.']
    ],
    sentences: [
      ['Vorrei un cartoccio di pesce fritto misto.', 'I would like a paper cone of mixed fried fish.', {grammarPoint: 'Street food container "cartoccio".'}],
      ['La porchetta di Ariccia è famosa in tutto il mondo.', 'The porchetta from Ariccia is famous all over the world.', {grammarPoint: 'Subject-adjective-location.'}],
      ['Attento, il ripieno è molto caldo!', 'Careful, the filling is very hot!', {grammarPoint: 'Warning with "attento".'}],
      ['Posso avere un tovagliolo di carta?', 'Can I have a paper napkin?', {grammarPoint: 'Practical street food request.'}],
      ['Qual è lo street food tipico di questa città?', 'What is the typical street food of this city?', {grammarPoint: 'Inquiring about local specialties.'}],
      ['Mangiamo questo supplì mentre camminiamo.', 'Let\'s eat this supplì while we walk.', {grammarPoint: 'Conjunction "mentre" for simultaneous actions.'}]
    ]
  },
  {
    id: 38,
    phrases: [
      ['Un caffè macchiato caldo.', 'A hot caffè macchiato.'],
      ['Una spremuta d\'arancia fresca.', 'A fresh orange juice.'],
      ['Devo pagare prima alla cassa?', 'Do I have to pay first at the cash register?'],
      ['Ecco lo scontrino.', 'Here is the receipt.'],
      ['Una brioche alla marmellata.', 'A jam-filled brioche.'],
      ['Un caffè d\'orzo in tazza grande.', 'A barley coffee in a large cup.']
    ],
    sentences: [
      ['In Italia si paga spesso prima di ordinare al banco.', 'In Italy one often pays before ordering at the counter.', {grammarPoint: 'Impersonal "si paga".'}],
      ['Vorrei pane, burro e marmellata per colazione.', 'I would like bread, butter, and jam for breakfast.', {grammarPoint: 'Classic breakfast listing.'}],
      ['Mi dà un bicchiere d\'acqua insieme al caffè?', 'Can I have a glass of water with the coffee?', {grammarPoint: 'Usage of "insieme al".'}],
      ['Non bevo caffeina, preferisco l\'orzo.', 'I don\'t drink caffeine, I prefer barley.', {grammarPoint: 'Expressing preference and reason.'}],
      ['I biscotti fatti in casa sono squisiti.', 'The homemade cookies are exquisite.', {grammarPoint: 'Plural agreement for "squisiti".'}],
      ['Posso avere il latte freddo a parte?', 'Can I have cold milk on the side?', {grammarPoint: 'Requesting items "a parte".'}]
    ]
  },
  {
    id: 39,
    phrases: [
      ['Come si legge questa ricetta?', 'How do you read this recipe?'],
      ['Devo tagliare le verdure fini?', 'Should I cut the vegetables thinly?'],
      ['Mescola bene il composto.', 'Mix the mixture well.'],
      ['Quanta farina serve?', 'How much flour is needed?'],
      ['Aggiungi un filo d\'olio.', 'Add a drizzle of oil.'],
      ['È pronta la padella?', 'Is the pan ready?']
    ],
    sentences: [
      ['Dobbiamo cuocere la pasta in abbondante acqua salata.', 'We must cook the pasta in plenty of salted water.', {grammarPoint: 'Standard cooking instruction.'}],
      ['Manca un pizzico di sale nel sugo.', 'A pinch of salt is missing in the sauce.', {grammarPoint: 'Usage of "manca".'}],
      ['Mescolare l\'olio con la farina piano piano.', 'Mix the oil with the flour slowly.', {grammarPoint: 'Describing a process with "piano piano".'}],
      ['Posso avere la ricetta scritta dopo la lezione?', 'Can I have the written recipe after the lesson?', {grammarPoint: 'Future request.'}],
      ['Non tagliare troppo grandi le patate.', 'Don\'t cut the potatoes too large.', {grammarPoint: 'Negative imperative with infinitive.'}],
      ['Accendi il fuoco sotto la padella.', 'Turn on the heat under the pan.', {grammarPoint: 'Direct imperative instruction.'}]
    ]
  },
  {
    id: 40,
    phrases: [
      ['Cerco dei pomodori maturi.', 'I am looking for ripe tomatoes.'],
      ['Mi dia della mozzarella fresca.', 'Give me some fresh mozzarella.'],
      ['Un etto di prosciutto crudo, per favore.', 'A hundred grams of cured ham, please.'],
      ['Quali olive sono meno salate?', 'Which olives are less salty?'],
      ['Vorrei un po\' di frutta di stagione.', 'I would like some seasonal fruit.'],
      ['Avete un coltello di plastica?', 'Do you have a plastic knife?']
    ],
    sentences: [
      ['Prepariamo un\'insalata caprese con basilico e mozzarella.', 'Let\'s prepare a caprese salad with basil and mozzarella.', {grammarPoint: 'First person plural "prepariamo".'}],
      ['Mi serve un piatto piccolo per assaggiare questo formaggio.', 'I need a small plate to taste this cheese.', {grammarPoint: 'Verb "servire" for needs.'}],
      ['Il prosciutto crudo di Parma è il migliore per i panini.', 'Parma ham is the best for sandwiches.', {grammarPoint: 'Superlative "il migliore".'}],
      ['Può lavare questa frutta per me?', 'Can you wash this fruit for me?', {grammarPoint: 'Requesting a service.'}],
      ['Mettiamo tutto nel sacchetto per il pranzo al parco.', 'Let\'s put everything in the bag for lunch at the park.', {grammarPoint: 'Contextual grouping.'}],
      ['Queste olive nere sono tipiche della zona.', 'These black olives are typical of the area.', {grammarPoint: 'Describing regionality.'}]
    ]
  },
  {
    id: 41,
    phrases: [
      ['Posso provare questa giacca?', 'Can I try on this jacket?'],
      ['Dov\'è il camerino?', 'Where is the fitting room?'],
      ['È troppo grande per me.', 'It is too big for me.'],
      ['Avete una taglia più piccola?', 'Do you have a smaller size?'],
      ['Questo vestito mi piace molto.', 'I like this dress very much.'],
      ['Chiedo al commesso un\'altra taglia.', "I'll ask the shop assistant for another size."]
    ],
    sentences: [
      ['La taglia media è perfetta, non è né stretta né larga.', 'The medium size is perfect, it\'s neither tight nor loose.', {grammarPoint: 'Correlative "né... né".'}],
      ['Vorrei provare questo vestito in blu, se possibile.', 'I would like to try on this dress in blue, if possible.', {grammarPoint: 'Requesting colors.'}],
      ['C\'è molto specchio nel camerino?', 'Is there a lot of mirror in the fitting room?', {grammarPoint: 'Checking facilities.'}],
      ['Questa giacca è troppo elegante per il mio stile.', 'This jacket is too elegant for my style.', {grammarPoint: 'Expressing personal style.'}],
      ['Il commesso è stato molto gentile ad aiutarmi.', 'The shop assistant was very kind to help me.', {grammarPoint: 'Passato prossimo of "essere".'}],
      ['Cerco una taglia grande perché vesta comodo.', 'I\'m looking for a large size so it fits comfortably.', {grammarPoint: 'Reasoning with "perché".'}]
    ]
  },
  {
    id: 42,
    phrases: [
      ['Che numero porta?', 'What shoe size do you wear?'],
      ['Porto il trentotto.', 'I wear size 38.'],
      ['Sono molto comode.', 'They are very comfortable.'],
      ['Mi stanno un po\' strette.', 'They are a bit tight on me.'],
      ['Vorrei un paio di scarpe in pelle.', 'I would like a pair of leather shoes.'],
      ['Avete delle scarpe sportive?', 'Do you have any sneakers?']
    ],
    sentences: [
      ['Queste scarpe sono troppo larghe sul tallone.', 'These shoes are too wide at the heel.', {grammarPoint: 'Specifying a fit problem.'}],
      ['Mi serve un paio di calzini per provarle.', 'I need a pair of socks to try them on.', {grammarPoint: 'Using "le" to refer to shoes.'}],
      ['Preferisco le scarpe in pelle per l\'inverno.', 'I prefer leather shoes for winter.', {grammarPoint: 'Stating seasonal preference.'}],
      ['Le sneakers sono perfette per camminare tutto il giorno.', 'Sneakers are perfect for walking all day.', {grammarPoint: 'Usage of "per" + infinitive.'}],
      ['C\'è un numero più piccolo di questo modello?', 'Is there a smaller size for this model?', {grammarPoint: 'Comparative "più piccolo".'}],
      ['Il cuoio di queste scarpe è di ottima qualità.', 'The leather of these shoes is of excellent quality.', {grammarPoint: 'Evaluating materials.'}]
    ]
  },
  {
    id: 43,
    phrases: [
      ['Prendo un cestino all\'ingresso.', "I'll take a basket at the entrance."],
      ['Dove posso trovare il riso?', 'Where can I find the rice?'],
      ['Mi serve un carrello grande.', 'I need a large cart.'],
      ['Sullo scaffale in fondo a destra.', 'On the shelf at the back to the right.'],
      ['Pago direttamente al cassiere.', 'I pay directly to the cashier.'],
      ['Una confezione di uova da sei.', 'A pack of six eggs.']
    ],
    sentences: [
      ['Cerco la pasta secca integrale, sapete dove si trova?', 'I am looking for whole-grain dry pasta, do you know where it is?', {grammarPoint: 'Reflexive "si trova" for location.'}],
      ['Il latte è nel reparto frigo insieme allo yogurt.', 'The milk is in the fridge section with the yogurt.', {grammarPoint: 'Grouping items by category.'}],
      ['Devo inserire una moneta per sbloccare il carrello?', 'Do I need to insert a coin to unlock the cart?', {grammarPoint: 'Practical supermarket question.'}],
      ['Il cassiere mi ha chiesto se volevo un sacchetto.', 'The cashier asked me if I wanted a bag.', {grammarPoint: 'Indirect question with "se".'}],
      ['Controlla sempre la data di scadenza sullo scaffale.', 'Always check the expiration date on the shelf.', {grammarPoint: 'Imperative advice.'}],
      ['Abbiamo dimenticato di prendere le uova fresche.', 'We forgot to take the fresh eggs.', {grammarPoint: 'Passato prossimo of "dimenticare".'}]
    ]
  },
  {
    id: 44,
    phrases: [
      ['Vorrei un chilo di mele.', 'I would like a kilo of apples.'],
      ['Sono mature queste fragole?', 'Are these strawberries ripe?'],
      ['Posso assaggiare un pezzetto?', 'Can I taste a little piece?'],
      ['A che ora chiude questo banco?', 'At what time does this stall close?'],
      ['Tre zucchine medie, grazie.', 'Three medium zucchini, thank you.'],
      ['Mi dà un sacchetto di carta?', 'Can I have a paper bag?']
    ],
    sentences: [
      ['Al mercato si trovano spesso prodotti più freschi che al supermercato.', 'At the market you often find fresher products than at the supermarket.', {grammarPoint: 'Comparative of majority.'}],
      ['Vorrei mezzo chilo di fragole ben mature.', 'I would like half a kilo of well-ripened strawberries.', {grammarPoint: 'Specifying quantity and quality.'}],
      ['Questo banco ha le zucchine migliori della fiera.', 'This stall has the best zucchini of the fair.', {grammarPoint: 'Relative superlative.'}],
      ['Quanto costa al chilo questa uva?', 'How much per kilo is this grape?', {grammarPoint: 'Asking price by unit.'}],
      ['Metta pure tutto in un unico sacchetto.', 'Go ahead and put everything in a single bag.', {grammarPoint: 'Formal imperative "metta".'}],
      ['Le mele del Trentino sono molto saporite.', 'Apples from Trentino are very flavorful.', {grammarPoint: 'Regional attribution.'}]
    ]
  },
  {
    id: 45,
    phrases: [
      ['Avete dei cerotti per le scarpe?', 'Do you have bandages for shoes?'],
      ['Mi serve una crema idratante.', 'I need a moisturizing cream.'],
      ['Ho un forte mal di testa.', 'I have a strong headache.'],
      ['Qual è la dose consigliata?', 'What is the recommended dose?'],
      ['Qualcosa per il raffreddore, per favore.', 'Something for a cold, please.'],
      ['Chiedo consiglio alla farmacista.', "I'll ask the pharmacist for advice."]
    ],
    sentences: [
      ['Prenda queste gocce tre volte al giorno dopo i pasti.', 'Take these drops three times a day after meals.', {grammarPoint: 'Formal imperative "prenda".'}],
      ['Cerco delle vitamine per avere più energia.', 'I am looking for vitamins to have more energy.', {grammarPoint: 'Stating a medical need.'}],
      ['Questa crema è adatta per le pelli sensibili?', 'Is this cream suitable for sensitive skin?', {grammarPoint: 'Product suitability question.'}],
      ['Il mio raffreddore non passa, cosa posso prendere?', 'My cold isn\'t going away, what can I take?', {grammarPoint: 'Seeking medical help.'}],
      ['Mi servono dei cerotti impermeabili per la piscina.', 'I need waterproof bandages for the pool.', {grammarPoint: 'Specific use case for product.'}],
      ['Quante gocce devo mettere nel bicchiere d\'acqua?', 'How many drops should I put in the glass of water?', {grammarPoint: 'Inquiring about dosage.'}]
    ]
  },
  {
    id: 46,
    phrases: [
      ['Vorrei una cartolina di Roma.', 'I would like a postcard of Rome.'],
      ['Avete dei magneti per il frigo?', 'Do you have any fridge magnets?'],
      ['È un prodotto artigianale locale?', 'Is it a local handmade product?'],
      ['Può incartarlo per un regalo?', 'Can you wrap it for a gift?'],
      ['Attenzione, è molto fragile.', 'Careful, it is very fragile.'],
      ['Vorrei un ricordo di questo viaggio.', 'I would like a souvenir of this trip.']
    ],
    sentences: [
      ['Questa ceramica dipinta a mano è bellissima.', 'This hand-painted ceramic is beautiful.', {grammarPoint: 'Describing craftsmanship.'}],
      ['Devo spedire queste cartoline ai miei amici in America.', 'I have to send these postcards to my friends in America.', {grammarPoint: 'Verb "spedire" with indirect objects.'}],
      ['Cerco un regalo piccolo che non sia troppo pesante in valigia.', 'I am looking for a small gift that isn\'t too heavy in the suitcase.', {grammarPoint: 'Subjunctive in relative clause "che non sia".'}],
      ['Mi assicura che la ceramica arrivi intatta a casa?', 'Can you assure me that the ceramic will arrive intact at home?', {grammarPoint: 'Asking for confirmation.'}],
      ['I magneti sono i souvenir più popolari.', 'Magnets are the most popular souvenirs.', {grammarPoint: 'Superlative construction.'}],
      ['Vorrei comprare qualcosa di veramente tipico e artigianale.', 'I would like to buy something truly typical and handmade.', {grammarPoint: 'Stating quality preference.'}]
    ]
  },
  {
    id: 47,
    phrases: [
      ['Cerco un adattatore universale.', 'I am looking for a universal adapter.'],
      ['Avete un cavo USB-C?', 'Do you have a USB-C cable?'],
      ['Quanto dura la garanzia?', 'How long is the warranty?'],
      ['È compatibile con il mio telefono?', 'Is it compatible with my phone?'],
      ['Vorrei degli auricolari senza fili.', 'I would like some wireless earbuds.'],
      ['Di quanta memoria ha bisogno?', 'How much storage do you need?']
    ],
    sentences: [
      ['Mi serve una presa italiana per il mio asciugacapelli.', 'I need an Italian socket/plug for my hairdryer.', {grammarPoint: 'Practical travel tech need.'}],
      ['Qual è l\'ultimo modello di questo tablet?', 'Which is the latest model of this tablet?', {grammarPoint: 'Checking for newest technology.'}],
      ['Questo cavo è troppo corto per arrivare alla scrivania.', 'This cable is too short to reach the desk.', {grammarPoint: 'Describing a technical problem.'}],
      ['La garanzia copre anche i danni accidentali?', 'Does the warranty also cover accidental damage?', {grammarPoint: 'Terms and conditions question.'}],
      ['Gli auricolari sono in offerta questa settimana.', 'The earbuds are on sale this week.', {grammarPoint: 'Common shopping phrase.'}],
      ['Ho bisogno di più memoria per salvare tutte le foto.', 'I need more storage to save all the photos.', {grammarPoint: 'Explaining storage needs.'}]
    ]
  },
  {
    id: 48,
    phrases: [
      ['Dov\'è il reparto di narrativa?', 'Where is the fiction section?'],
      ['Chi è l\'autore di questo libro?', 'Who is the author of this book?'],
      ['Cerco un dizionario italiano-inglese.', 'I am looking for an Italian-English dictionary.'],
      ['Avete quaderni a righe o a quadretti?', 'Do you have lined or squared notebooks?'],
      ['Mi piace molto la copertina.', 'I really like the cover.'],
      ['Vorrei un romanzo ambientato in Italia.', 'I would like a novel set in Italy.']
    ],
    sentences: [
      ['Questa libreria è molto fornita di testi scolastici.', 'This bookstore is very well-stocked with textbooks.', {grammarPoint: 'Describing store specialty.'}],
      ['Avete l\'ultima opera del mio autore preferito?', 'Do you have the latest work of my favorite author?', {grammarPoint: 'Possessive "mio".'}],
      ['Vorrei un quaderno piccolo per scrivere i miei appunti.', 'I would like a small notebook to write my notes.', {grammarPoint: 'Intended use with "per" + infinitive.'}],
      ['Il dizionario tascabile è molto utile per viaggiare.', 'The pocket dictionary is very useful for traveling.', {grammarPoint: 'Adjective "tascabile".'}],
      ['Questo romanzo è diventato un best-seller in poco tempo.', 'This novel became a bestseller in a short time.', {grammarPoint: 'Past tense of "diventare".'}],
      ['Posso sfogliare il libro prima di comprarlo?', 'Can I browse through the book before buying it?', {grammarPoint: 'Usage of "lo" as clitic on infinitive.'}]
    ]
  },
  {
    id: 49,
    phrases: [
      ['Vorrei fare un reso.', 'I would like to make a return.'],
      ['È possibile fare un cambio?', 'Is it possible to make an exchange?'],
      ['C\'è un piccolo difetto qui.', 'There is a small defect here.'],
      ['Purtroppo è rotto.', 'Unfortunately it is broken.'],
      ['Vorrei un rimborso, se possibile.', 'I would like a refund, if possible.'],
      ['Ho lo scontrino originale.', 'I have the original receipt.']
    ],
    sentences: [
      ['Qual è la vostra politica sui resi?', 'What is your return policy?', {grammarPoint: 'General store policy inquiry.'}],
      ['Posso cambiare questo articolo entro trenta giorni?', 'Can I exchange this item within thirty days?', {grammarPoint: 'Time limit expression "entro".'}],
      ['Mi hanno regalato questo, ma è della taglia sbagliata.', 'They gave me this as a gift, but it\'s the wrong size.', {grammarPoint: 'Past tense "hanno regalato".'}],
      ['Se l\'oggetto è rotto, ha diritto alla sostituzione.', 'If the item is broken, you have the right to a replacement.', {grammarPoint: 'Stating customer rights.'}],
      ['Il rimborso verrà accreditato sulla stessa carta.', 'The refund will be credited to the same card.', {grammarPoint: 'Future tense "verrà".'}],
      ['Senza lo scontrino non possiamo accettare il cambio.', 'Without the receipt, we cannot accept the exchange.', {grammarPoint: 'Store rule explanation.'}]
    ]
  },
  {
    id: 50,
    phrases: [
      ['Posso pagare contactless?', 'Can I pay contactless?'],
      ['Deve inserire il PIN.', 'You must enter the PIN.'],
      ['Serve la firma per questo importo?', 'Is a signature needed for this amount?'],
      ['La transazione è stata rifiutata.', 'The transaction was declined.'],
      ['Pagamento approvato, grazie.', 'Payment approved, thank you.'],
      ['Può riprovare, per favore?', 'Can you try again, please?']
    ],
    sentences: [
      ['Avvicini la carta al terminale per pagare.', 'Bring the card close to the terminal to pay.', {grammarPoint: 'Formal imperative "avvicini".'}],
      ['Mi scusi, non ricordo il PIN di questa carta.', 'I\'m sorry, I don\'t remember the PIN for this card.', {grammarPoint: 'Common payment problem.'}],
      ['L\'importo totale è di trenta euro.', 'The total amount is thirty euros.', {grammarPoint: 'Stating the price.'}],
      ['Forse c\'è un problema con il chip, proviamo a strisciare.', 'Maybe there is a problem with the chip, let\'s try swiping.', {grammarPoint: 'Troubleshooting payment.'}],
      ['Può darmi la ricevuta del pagamento approvato?', 'Can you give me the receipt for the approved payment?', {grammarPoint: 'Formal request "Può darmi".'}],
      ['La mia banca ha bloccato la carta per sicurezza.', 'My bank blocked the card for security reasons.', {grammarPoint: 'Explaining card failure.'}]
    ]
  },
  {
    id: 51,
    phrases: [
      ['Vorrei aprire un conto corrente.', 'I would like to open a bank account.'],
      ['Devo fare un prelievo.', 'I need to make a withdrawal.'],
      ['Dov\'è lo sportello automatico?', 'Where is the ATM?'],
      ['Ecco il mio documento d\'identità.', 'Here is my ID document.'],
      ['Serve il codice fiscale?', 'Is the tax code needed?'],
      ['Deve compilare questo modulo.', 'You must fill out this form.']
    ],
    sentences: [
      ['Vorrei versare questo assegno sul mio conto corrente.', 'I would like to deposit this check into my bank account.', {grammarPoint: 'Specific banking action.'}],
      ['Qual è il limite giornaliero per il prelievo al bancomat?', 'What is the daily limit for ATM withdrawals?', {grammarPoint: 'Interrogative "Qual è".'}],
      ['Mi serve un modulo per richiedere una nuova carta.', 'I need a form to request a new card.', {grammarPoint: 'Administrative banking task.'}],
      ['Lo sportello chiude tra dieci minuti.', 'The counter closes in ten minutes.', {grammarPoint: 'Time constraint with "tra".'}],
      ['Ho dimenticato il codice fiscale a casa.', 'I forgot my tax code at home.', {grammarPoint: 'Reporting a problem.'}],
      ['Posso fare un deposito in contanti qui?', 'Can I make a cash deposit here?', {grammarPoint: 'Asking for service availability.'}]
    ]
  },
  {
    id: 52,
    phrases: [
      ['Vorrei tre francobolli per l\'estero.', 'I would like three stamps for abroad.'],
      ['Devo spedire questo pacco.', 'I need to send this package.'],
      ['È una lettera o una raccomandata?', 'Is it a letter or registered mail?'],
      ['Chi è il destinatario?', 'Who is the recipient?'],
      ['Scriva il suo nome come mittente.', 'Write your name as the sender.'],
      ['C\'è molta coda oggi.', 'There is a long line today.']
    ],
    sentences: [
      ['Quanto costa la spedizione prioritaria per gli Stati Uniti?', 'How much is priority shipping to the United States?', {grammarPoint: 'Inquiring about international shipping costs.'}],
      ['Deve prendere il biglietto per fare la coda.', 'You must take a ticket to stand in line.', {grammarPoint: 'Post office procedure instruction.'}],
      ['La raccomandata è il modo più sicuro per spedire documenti.', 'Registered mail is the safest way to send documents.', {grammarPoint: 'General administrative advice.'}],
      ['Mi serve un modulo per la spedizione internazionale.', 'I need a form for international shipping.', {grammarPoint: 'Requesting documentation.'}],
      ['Il pacco arriverà a destinazione entro una settimana.', 'The package will arrive at its destination within a week.', {grammarPoint: 'Future tense "arriverà".'}],
      ['Ricordati di scrivere l\'indirizzo del mittente sul retro.', 'Remember to write the sender\'s address on the back.', {grammarPoint: 'Imperative instruction "ricordati".'}]
    ]
  },
  {
    id: 53,
    phrases: [
      ['Vorrei solo spuntare i capelli.', 'I would like to just trim my hair.'],
      ['Mi faccia un taglio corto.', 'Give me a short cut.'],
      ['Devo fare anche la barba.', 'I need to do my beard too.'],
      ['Il lavaggio è incluso nel prezzo?', 'Is the wash included in the price?'],
      ['Ho un appuntamento alle tre.', 'I have an appointment at three.'],
      ['Guardi pure nello specchio.', 'Go ahead and look in the mirror.']
    ],
    sentences: [
      ['Non tagli troppo sopra, preferisco tenerli lunghi.', 'Don\'t cut too much on top, I prefer to keep them long.', {grammarPoint: 'Specific styling instruction.'}],
      ['Mi consiglia un taglio adatto al mio viso?', 'Do you recommend a cut suitable for my face?', {grammarPoint: 'Seeking professional advice.'}],
      ['Vorrei lavare i capelli prima del taglio.', 'I would like to wash my hair before the cut.', {grammarPoint: 'Ordering steps in a service.'}],
      ['Questo parrucchiere è molto bravo con le sfumature.', 'This hairdresser is very good with fades.', {grammarPoint: 'Complimenting technical skill.'}],
      ['Posso spostare il mio appuntamento a domani?', 'Can I move my appointment to tomorrow?', {grammarPoint: 'Rescheduling a service.'}],
      ['Mi piace come ha tagliato la barba, grazie.', 'I like how you cut the beard, thank you.', {grammarPoint: 'Giving positive feedback.'}]
    ]
  },
  {
    id: 54,
    phrases: [
      ['Dove si comprano i gettoni?', 'Where do you buy the tokens?'],
      ['Quale programma devo usare?', 'Which cycle should I use?'],
      ['A che temperatura lava questa macchina?', 'At what temperature does this machine wash?'],
      ['Devo dividere i bianchi dai colorati.', 'I must separate whites from colors.'],
      ['Quanto tempo serve per asciugare?', 'How much time is needed to dry?'],
      ['Il lavaggio è finito?', 'Is the wash finished?']
    ],
    sentences: [
      ['Inserisca il gettone e prema il tasto avvio.', 'Insert the token and press the start button.', {grammarPoint: 'Formal imperative instructions.'}],
      ['I capi colorati vanno lavati a trenta gradi.', 'Colored items should be washed at thirty degrees.', {grammarPoint: 'Usage of "vanno" for obligation/necessity.'}],
      ['C\'è un\'asciugatrice libera in fondo?', 'Is there a free dryer at the back?', {grammarPoint: 'Checking availability in laundromat.'}],
      ['Devo mettere il detersivo nel cassetto numero uno.', 'I must put the detergent in drawer number one.', {grammarPoint: 'Specific operational instruction.'}],
      ['Questa lavanderia automatica è aperta ventiquattr\'ore.', 'This laundromat is open twenty-four hours.', {grammarPoint: 'Describing facility hours.'}],
      ['Attenzione a non mescolare i bianchi con le camicie rosse.', 'Careful not to mix whites with red shirts.', {grammarPoint: 'Warning about laundry mistakes.'}]
    ]
  },
  {
    id: 55,
    phrases: [
      ['Che bel sole oggi!', 'What beautiful sun today!'],
      ['Sembra che voglia piovere.', 'It looks like it\'s going to rain.'],
      ['C\'è troppo vento per uscire.', 'There\'s too much wind to go out.'],
      ['È molto nuvoloso stamattina.', 'It\'s very cloudy this morning.'],
      ['Fa un caldo terribile.', 'It\'s terribly hot.'],
      ['Hai preso l\'ombrello?', 'Did you take the umbrella?']
    ],
    sentences: [
      ['Le previsioni del tempo dicono che domani nevicherà.', 'The weather forecast says it will snow tomorrow.', {grammarPoint: 'Reporting info with future tense.'}],
      ['Mi piace quando c\'è il sole ma non fa troppo caldo.', 'I like it when it\'s sunny but not too hot.', {grammarPoint: 'Expressing climatic preference.'}],
      ['Copriti bene perché fuori fa molto freddo.', 'Cover up well because it\'s very cold outside.', {grammarPoint: 'Advice for weather conditions.'}],
      ['La pioggia è necessaria per la campagna in questo periodo.', 'Rain is necessary for the countryside in this period.', {grammarPoint: 'Observational comment.'}],
      ['Spero che il vento cali prima di stasera.', 'I hope the wind dies down before tonight.', {grammarPoint: 'Subjunctive "cali" after "spero che".'}],
      ['Non fidarti delle previsioni, cambiano ogni ora.', 'Don\'t trust the forecast, it changes every hour.', {grammarPoint: 'Negative imperative advice.'}]
    ]
  },
  {
    id: 56,
    phrases: [
      ['Vorrei fissare un appuntamento.', 'I would like to set an appointment.'],
      ['È disponibile per lunedì?', 'Are you available for Monday?'],
      ['Ci vediamo martedì alle dieci.', 'See you Tuesday at ten.'],
      ['Mi serve una conferma scritta.', 'I need a written confirmation.'],
      ['Devo spostare l\'incontro.', 'I need to reschedule the meeting.'],
      ['Purtroppo devo cancellare tutto.', 'Unfortunately I have to cancel everything.']
    ],
    sentences: [
      ['Qual è il primo giorno disponibile per una visita?', 'Which is the first available day for a visit?', {grammarPoint: 'Inquiring about initial availability.'}],
      ['Posso spostare l\'appuntamento dalle dieci alle undici?', 'Can I move the appointment from ten to eleven?', {grammarPoint: 'Usage of "da... a...".'}],
      ['Le manderemo un\'email di conferma entro stasera.', 'We will send you a confirmation email by tonight.', {grammarPoint: 'Future tense for service promise.'}],
      ['Se non puoi venire lunedì, proviamo martedì mattina.', 'If you can\'t come Monday, let\'s try Tuesday morning.', {grammarPoint: 'Negotiating alternative times.'}],
      ['Mi dispiace, ma devo cancellare per un impegno improvviso.', 'I\'m sorry, but I have to cancel due to a sudden commitment.', {grammarPoint: 'Explaining cancellation politely.'}],
      ['È possibile avere un appuntamento nel tardo pomeriggio?', 'Is it possible to have an appointment in the late afternoon?', {grammarPoint: 'Asking for specific time slots.'}]
    ]
  },
  {
    id: 57,
    phrases: [
      ['Quanto costa l\'abbonamento mensile?', 'How much is the monthly membership?'],
      ['Posso fare una lezione di prova?', 'Can I do a trial class?'],
      ['Dov\'è lo spogliatoio maschile?', 'Where is the men\'s changing room?'],
      ['Uso il tapis roulant per dieci minuti.', 'I\'ll use the treadmill for ten minutes.'],
      ['Non esagerare con i pesi.', 'Don\'t overdo it with the weights.'],
      ['Chiedo aiuto all\'istruttore.', "I'll ask the trainer for help."]
    ],
    sentences: [
      ['Mi serve una bottiglia d\'acqua fresca durante l\'allenamento.', 'I need a bottle of fresh water during the workout.', {grammarPoint: 'Expressing a need during activity.'}],
      ['L\'istruttore mi ha preparato una scheda personalizzata.', 'The trainer prepared a personalized workout plan for me.', {grammarPoint: 'Service description.'}],
      ['Gli spogliatoi sono stati appena puliti, sono molto ordinati.', 'The changing rooms have just been cleaned, they are very tidy.', {grammarPoint: 'Passive "sono stati puliti".'}],
      ['Vorrei fare un abbonamento annuale per risparmiare.', 'I would like to get an annual membership to save money.', {grammarPoint: 'Stating financial strategy.'}],
      ['C\'è sempre molta gente sui tapis roulant a quest\'ora.', 'There are always many people on the treadmills at this time.', {grammarPoint: 'Observational comment on traffic.'}],
      ['Posso lasciare la borsa nell\'armadietto dello spogliatoio?', 'Can I leave my bag in the changing room locker?', {grammarPoint: 'Practical facility question.'}]
    ]
  },
  {
    id: 58,
    phrases: [
      ['Come posso fare la tessera?', 'How can I get the card?'],
      ['Vorrei questo libro in prestito.', 'I would like this book on loan.'],
      ['Per favore, mantenete il silenzio.', 'Please, keep silence.'],
      ['Dov\'è la sala lettura?', 'Where is the reading room?'],
      ['Quando è la scadenza del prestito?', 'When is the due date of the loan?'],
      ['Devo restituire questi volumi.', 'I must return these volumes.']
    ],
    sentences: [
      ['Può controllare nel catalogo se il libro è disponibile?', 'Can you check in the catalog if the book is available?', {grammarPoint: 'Formal request with indirect question.'}],
      ['La sala lettura è il posto perfetto per studiare in pace.', 'The reading room is the perfect place to study in peace.', {grammarPoint: 'Describing a location.'}],
      ['Mi serve la tessera della biblioteca per accedere al Wi-Fi.', 'I need the library card to access the Wi-Fi.', {grammarPoint: 'Practical utility requirement.'}],
      ['Se superi la scadenza, devi pagare una piccola multa.', 'If you miss the due date, you must pay a small fine.', {grammarPoint: 'Hypothetical "Se" clause.'}],
      ['Posso restituire il libro anche se la biblioteca è chiusa?', 'Can I return the book even if the library is closed?', {grammarPoint: 'Inquiring about drop-box service.'}],
      ['Cerco un libro di storia che non è presente nel catalogo online.', 'I am looking for a history book that is not in the online catalog.', {grammarPoint: 'Relative clause "che non è".'}]
    ]
  },
  {
    id: 59,
    phrases: [
      ['Buongiorno, come sta?', 'Good morning, how are you?'],
      ['C\'è stato molto rumore ieri sera.', 'There was a lot of noise last night.'],
      ['Può chiudere il portone, per favore?', 'Can you close the building door, please?'],
      ['Ci sono problemi con le scale?', 'Are there problems with the stairs?'],
      ['C\'è della posta per me?', 'Is there any mail for me?'],
      ['Grazie, lei è molto gentile.', 'Thank you, you are very kind.']
    ],
    sentences: [
      ['Il mio vicino di casa mi aiuta sempre con i pacchi pesanti.', 'My neighbor always helps me with heavy packages.', {grammarPoint: 'Social interaction comment.'}],
      ['Mi scusi per il rumore, stavamo spostando dei mobili.', 'Excuse me for the noise, we were moving some furniture.', {grammarPoint: 'Apologizing with reason.'}],
      ['Abbiamo una riunione di condominio lunedì prossimo nel palazzo.', 'We have a condo meeting next Monday in the building.', {grammarPoint: 'Describing community events.'}],
      ['Lascio la porta aperta così entra un po\' d\'aria.', 'I\'ll leave the door open so some air comes in.', {grammarPoint: 'Setting conditions with "così".'}],
      ['Ci vediamo domani mattina sulle scale!', 'See you tomorrow morning on the stairs!', {grammarPoint: 'Friendly neighborhood greeting.'}],
      ['Può ritirare la mia posta mentre sono in vacanza?', 'Can you collect my mail while I am on vacation?', {grammarPoint: 'Asking for a social favor.'}]
    ]
  },
  {
    id: 60,
    phrases: [
      ['Mi serve un idraulico subito.', 'I need a plumber right away.'],
      ['C\'è una perdita d\'acqua in bagno.', 'There is a water leak in the bathroom.'],
      ['Il rubinetto continua a gocciolare.', 'The tap keeps dripping.'],
      ['Questa presa elettrica non funziona.', 'This power outlet doesn\'t work.'],
      ['La caldaia è spenta e fa freddo.', 'The boiler is off and it\'s cold.'],
      ['È un intervento molto urgente!', 'It is a very urgent job!']
    ],
    sentences: [
      ['Chiami l\'elettricista per controllare l\'impianto delle luci.', 'Call the electrician to check the light system.', {grammarPoint: 'Formal imperative "chiami".'}],
      ['Quanto costa riparare il rubinetto della cucina?', 'How much does it cost to repair the kitchen tap?', {grammarPoint: 'Inquiring about repair costs.'}],
      ['L\'idraulico ha detto che bisogna cambiare tutto il pezzo.', 'The plumber said that the whole part needs to be changed.', {grammarPoint: 'Reporting a diagnosis with "bisogna".'}],
      ['Non toccare la presa elettrica con le mani bagnate!', 'Don\'t touch the power outlet with wet hands!', {grammarPoint: 'Safety warning with negative imperative.'}],
      ['La caldaia deve essere revisionata ogni anno per legge.', 'The boiler must be serviced every year by law.', {grammarPoint: 'Passive "essere revisionata".'}],
      ['Cerco qualcuno che possa riparare la perdita entro stasera.', 'I am looking for someone who can repair the leak by tonight.', {grammarPoint: 'Urgent request with subjunctive "possa".'}]
    ]
  }
];

const part3 = [
  {
    id: 61,
    phrases: [
      ['Piacere di conoscerti.', 'Nice to meet you.'],
      ['Sono il nuovo collega.', 'I am the new colleague.'],
      ['Dov\'è la mia scrivania?', 'Where is my desk?'],
      ['Mi serve il badge?', 'Do I need the badge?'],
      ['Chi è il mio responsabile?', 'Who is my manager?'],
      ['A che ora è la pausa pranzo?', 'What time is the lunch break?']
    ],
    sentences: [
      ['Benvenuto nel nostro team!', 'Welcome to our team!', {grammarPoint: 'Use of "nel" (in + il) for masculine singular.'}],
      ['Questa è la tua nuova scrivania.', 'This is your new desk.', {grammarPoint: 'Feminine possessive "tua" matching "scrivania".'}],
      ['Il responsabile ti aspetta in ufficio.', 'The manager is waiting for you in the office.', {grammarPoint: 'Direct object pronoun "ti" before the verb.'}],
      ['Ecco il tuo badge per entrare.', 'Here is your badge to enter.', {grammarPoint: 'Use of "ecco" to present an object.'}],
      ['Di cosa ti occuperai esattamente?', 'What exactly will you be doing?', {grammarPoint: 'Reflexive verb "occuparsi" in the future tense.'}],
      ['I colleghi sono molto simpatici.', 'The colleagues are very nice.', {grammarPoint: 'Plural masculine article "I".'}]
    ]
  },
  {
    id: 62,
    phrases: [
      ['Cominciamo la riunione.', 'Let\'s start the meeting.'],
      ['Qual è l\'agenda di oggi?', 'What is today\'s agenda?'],
      ['Ho preso delle note.', 'I took some notes.'],
      ['Sono d\'accordo con te.', 'I agree with you.'],
      ['Qual è il prossimo passo?', 'What is the next step?'],
      ['Chi scrive il verbale?', 'Who is writing the minutes?']
    ],
    sentences: [
      ['Dobbiamo discutere questo punto importante.', 'We need to discuss this important point.', {grammarPoint: 'Modal verb "dovere" followed by infinitive.'}],
      ['Avete domande su questa decisione?', 'Do you have questions about this decision?', {grammarPoint: 'Present tense of "avere" (plural you).'}],
      ['Non c\'è ancora un accordo totale.', 'There is no total agreement yet.', {grammarPoint: 'Negative construction with "non... ancora".'}],
      ['Identifichiamo il problema principale.', 'Let\'s identify the main problem.', {grammarPoint: 'First person plural imperative/present.'}],
      ['Scriverò io il verbale della riunione.', 'I will write the meeting minutes myself.', {grammarPoint: 'Future tense of "scrivere".'}],
      ['Passiamo al punto successivo.', 'Let\'s move on to the next point.', {grammarPoint: 'Combined preposition "al" (a + il).'}]
    ]
  },
  {
    id: 63,
    phrases: [
      ['Può ripetere, per favore?', 'Can you repeat, please?'],
      ['Non ho capito bene.', 'I didn\'t understand well.'],
      ['Cosa significa questa parola?', 'What does this word mean?'],
      ['Può parlare più lentamente?', 'Can you speak more slowly?'],
      ['Ho un dubbio su questo.', 'I have a doubt about this.'],
      ['Tutto chiaro, grazie.', 'Everything is clear, thanks.']
    ],
    sentences: [
      ['Può spiegarmi meglio questo concetto?', 'Can you explain this concept to me better?', {grammarPoint: 'Enclitic pronoun "mi" attached to infinitive "spiegare".'}],
      ['Mi può fare un esempio pratico?', 'Can you give me a practical example?', {grammarPoint: 'Pronoun "mi" before the modal verb.'}],
      ['Scusi, non capisco il significato.', 'Sorry, I don\'t understand the meaning.', {grammarPoint: 'Formal imperative of "scusare".'}],
      ['È tutto chiaro per lei?', 'Is everything clear for you?', {grammarPoint: 'Formal "lei" used as a pronoun.'}],
      ['Se avete dubbi, chiedete pure.', 'If you have doubts, feel free to ask.', {grammarPoint: 'Use of "pure" to encourage an action.'}]
    ]
  },
  {
    id: 64,
    phrases: [
      ['Ti ho inviato un\'email.', 'I sent you an email.'],
      ['Hai visto l\'allegato?', 'Did you see the attachment?'],
      ['Rispondo subito.', 'I\'ll reply right away.'],
      ['Inoltro il messaggio.', 'I\'m forwarding the message.'],
      ['Qual è l\'oggetto?', 'What is the subject?'],
      ['Ho ricevuto tutto.', 'I received everything.']
    ],
    sentences: [
      ['Le invio la bozza del progetto.', 'I am sending you the project draft.', {grammarPoint: 'Formal indirect object "Le".'}],
      ['Non dimenticare la scadenza di domani.', 'Don\'t forget tomorrow\'s deadline.', {grammarPoint: 'Negative imperative for "tu" (non + infinitive).'}],
      ['Ho dimenticato di aggiungere l\'allegato.', 'I forgot to add the attachment.', {grammarPoint: 'Use of "di" after "dimenticare".'}],
      ['Può rispondere entro stasera?', 'Can you reply by tonight?', {grammarPoint: 'Preposition "entro" for time limits.'}],
      ['Ho salvato l\'email nelle bozze.', 'I saved the email in the drafts.', {grammarPoint: 'Articulated preposition "nelle" (in + le).'}]
    ]
  },
  {
    id: 65,
    phrases: [
      ['Dove si trova l\'aula?', 'Where is the classroom located?'],
      ['Chi è il professore?', 'Who is the professor?'],
      ['Prendo gli appunti.', 'I\'m taking notes.'],
      ['Com\'è andato l\'esame?', 'How did the exam go?'],
      ['Che voto hai preso?', 'What grade did you get?'],
      ['Mi serve l\'iscrizione.', 'I need the enrollment.']
    ],
    sentences: [
      ['Questo semestre è molto impegnativo.', 'This semester is very demanding.', {grammarPoint: 'Adjective "impegnativo" matching masculine singular.'}],
      ['Gli appunti sono nell\'aula magna.', 'The notes are in the main lecture hall.', {grammarPoint: 'Plural masculine article "Gli" before "a".'}],
      ['Devo studiare per l\'esame di storia.', 'I have to study for the history exam.', {grammarPoint: 'Preposition "di" to show subject matter.'}],
      ['Il professore spiega molto bene.', 'The professor explains very well.', {grammarPoint: 'Present tense of "spiegare".'}],
      ['Hai già fatto l\'iscrizione online?', 'Have you already done the online enrollment?', {grammarPoint: 'Use of "già" (already) in the past tense.'}]
    ]
  },
  {
    id: 66,
    phrases: [
      ['Frequento un corso di italiano.', 'I\'m attending an Italian course.'],
      ['Sono al livello A1.', 'I\'m at A1 level.'],
      ['Facciamo conversazione.', 'Let\'s practice conversation.'],
      ['La pronuncia è difficile.', 'The pronunciation is difficult.'],
      ['Devo fare gli esercizi.', 'I have to do the exercises.'],
      ['Vorrei il certificato.', 'I would like the certificate.']
    ],
    sentences: [
      ['Studiamo la grammatica ogni mattina.', 'We study grammar every morning.', {grammarPoint: 'Adverbial phrase "ogni mattina".'}],
      ['La classe è molto internazionale.', 'The class is very international.', {grammarPoint: 'Adjective agreement with "classe" (feminine).'}],
      ['Questo esercizio è per casa.', 'This exercise is for homework.', {grammarPoint: 'Preposition "per" to indicate purpose.'}],
      ['Come posso migliorare la mia pronuncia?', 'How can I improve my pronunciation?', {grammarPoint: 'Possessive "mia" with feminine noun.'}],
      ['Riceverai il certificato alla fine del corso.', 'You will receive the certificate at the end of the course.', {grammarPoint: 'Future tense of "ricevere".'}]
    ]
  },
  {
    id: 67,
    phrases: [
      ['Ho un colloquio domani.', 'I have an interview tomorrow.'],
      ['Ecco il mio curriculum.', 'Here is my CV.'],
      ['Ho molta esperienza.', 'I have a lot of experience.'],
      ['Qual è lo stipendio?', 'What is the salary?'],
      ['Quando posso iniziare?', 'When can I start?'],
      ['Cerco un orario flessibile.', 'I am looking for a flexible schedule.']
    ],
    sentences: [
      ['Parliamo del contratto di lavoro.', 'Let\'s talk about the work contract.', {grammarPoint: 'Articulated preposition "del" (di + il).'}],
      ['Qual è la sua disponibilità immediata?', 'What is your immediate availability?', {grammarPoint: 'Formal possessive "sua".'}],
      ['Ho lavorato tre anni all\'estero.', 'I worked abroad for three years.', {grammarPoint: 'Passato prossimo of "lavorare".'}],
      ['Il colloquio è andato molto bene.', 'The interview went very well.', {grammarPoint: 'Past participle agreement with "colloquio".'}],
      ['Offriamo un contratto a tempo indeterminato.', 'We offer a permanent contract.', {grammarPoint: 'Standard work contract terminology.'}]
    ]
  },
  {
    id: 68,
    phrases: [
      ['Vorrei una postazione.', 'I would like a workspace.'],
      ['Dov\'è la stampante?', 'Where is the printer?'],
      ['La sala è prenotata?', 'Is the room booked?'],
      ['Preferisco la zona silenziosa.', 'I prefer the quiet zone.'],
      ['Voglio un pass giornaliero.', 'I want a daily pass.'],
      ['Come accedo al wifi?', 'How do I access the wifi?']
    ],
    sentences: [
      ['Può prenotare la sala riunioni online.', 'You can book the meeting room online.', {grammarPoint: 'Formal "può" with infinitive.'}],
      ['L\'accesso è consentito h24.', 'Access is allowed 24/7.', {grammarPoint: 'Passive form "è consentito".'}],
      ['Abbiamo abbonamenti mensili convenienti.', 'We have affordable monthly memberships.', {grammarPoint: 'Plural adjective agreement.'}],
      ['La stampante si trova in fondo al corridoio.', 'The printer is at the end of the hallway.', {grammarPoint: 'Reflexive "si trova" for location.'}],
      ['Cerco una postazione vicino alla finestra.', 'I\'m looking for a workspace near the window.', {grammarPoint: 'Preposition "vicino a" plus article.'}]
    ]
  },
  {
    id: 69,
    phrases: [
      ['Devo stampare un file.', 'I need to print a file.'],
      ['In bianco e nero o a colori?', 'In black and white or in color?'],
      ['Quante pagine sono?', 'How many pages are they?'],
      ['Ho una chiavetta USB.', 'I have a USB stick.'],
      ['Voglio la stampa fronte retro.', 'I want double-sided printing.'],
      ['Può scannerizzare questo?', 'Can you scan this?']
    ],
    sentences: [
      ['Mi serve il formato A4.', 'I need the A4 size.', {grammarPoint: 'Indirect object "mi" with "serve".'}],
      ['La carta è finita nella stampante.', 'The paper has run out in the printer.', {grammarPoint: 'Verb "finire" used intransitively.'}],
      ['Inserisca la chiavetta USB qui.', 'Insert the USB stick here.', {grammarPoint: 'Formal imperative "inserisca".'}],
      ['Quanto costa una copia a colori?', 'How much does a color copy cost?', {grammarPoint: 'Interrogative "quanto".'}],
      ['Può scannerizzare queste pagine?', 'Can you scan these pages?', {grammarPoint: 'Demonstrative adjective "queste".'}]
    ]
  },
  {
    id: 70,
    phrases: [
      ['Studiamo insieme oggi?', 'Shall we study together today?'],
      ['Ci vediamo in biblioteca.', 'See you at the library.'],
      ['Facciamo un ripasso veloce.', 'Let\'s do a quick review.'],
      ['Ho finito il primo capitolo.', 'I finished the first chapter.'],
      ['Hai delle domande?', 'Do you have any questions?'],
      ['Facciamo una pausa caffè?', 'Shall we take a coffee break?']
    ],
    sentences: [
      ['Dobbiamo fare questi esercizi per domani.', 'We must do these exercises for tomorrow.', {grammarPoint: 'Demonstrative "questi" plural.'}],
      ['La biblioteca chiude alle sette.', 'The library closes at seven.', {grammarPoint: 'Present tense of "chiudere".'}],
      ['Non capisco bene questo capitolo.', 'I don\'t understand this chapter well.', {grammarPoint: 'Adverb "bene" after the verb.'}],
      ['Ripassiamo gli argomenti principali.', 'Let\'s review the main topics.', {grammarPoint: 'First person plural present/imperative.'}],
      ['Chi vuole un caffè durante la pausa?', 'Who wants a coffee during the break?', {grammarPoint: 'Interrogative pronoun "chi".'}]
    ]
  },
  {
    id: 71,
    phrases: [
      ['Piacere di conoscerti!', 'Nice to meet you!'],
      ['Come ti chiami?', 'What is your name?'],
      ['Di dove sei?', 'Where are you from?'],
      ['Quanti anni hai?', 'How old are you?'],
      ['Il piacere è mio.', 'The pleasure is mine.'],
      ['Studio italiano da un mese.', 'I\'ve been studying Italian for a month.']
    ],
    sentences: [
      ['Mi chiamo Marco e vengo dall\'Italia.', 'My name is Marco and I come from Italy.', {grammarPoint: 'Reflexive "chiamarsi" and "vengo da" + article.'}],
      ['Abito a Roma da due anni.', 'I have lived in Rome for two years.', {grammarPoint: 'Present tense for ongoing actions (da + time).'}],
      ['Quali lingue parli oltre all\'italiano?', 'Which languages do you speak besides Italian?', {grammarPoint: 'Interrogative "quali" plural.'}],
      ['Ho venticinque anni.', 'I am twenty-five years old.', {grammarPoint: 'Use of "avere" to express age.'}],
      ['Sono qui per imparare la lingua.', 'I am here to learn the language.', {grammarPoint: 'Preposition "per" + infinitive.'}]
    ]
  },
  {
    id: 72,
    phrases: [
      ['Vuoi uscire stasera?', 'Do you want to go out tonight?'],
      ['Andiamo al cinema?', 'Shall we go to the cinema?'],
      ['Ci vediamo per cena.', 'See you for dinner.'],
      ['Ci sei sabato sera?', 'Are you free/in on Saturday night?'],
      ['Alle sette davanti al bar.', 'At seven in front of the bar.'],
      ['Va bene per te?', 'Is that okay for you?']
    ],
    sentences: [
      ['Forse arrivo con un po\' di ritardo.', 'Maybe I\'ll arrive a bit late.', {grammarPoint: 'Adverb "forse" at the start.'}],
      ['Sei sicuro di voler venire?', 'Are you sure you want to come?', {grammarPoint: 'Adjective agreement with "sei".'}],
      ['Possiamo incontrarci alle otto invece che alle sette.', 'We can meet at eight instead of seven.', {grammarPoint: 'Enclitic reflexive "ci" on infinitive.'}],
      ['Mi piacerebbe molto andare a cena fuori.', 'I would really like to go out for dinner.', {grammarPoint: 'Conditional "piacerebbe".'}],
      ['Ti faccio sapere entro domani mattina.', 'I\'ll let you know by tomorrow morning.', {grammarPoint: 'Phrase "far sapere" (to let someone know).'}]
    ]
  },
  {
    id: 73,
    phrases: [
      ['Vuoi venire con noi?', 'Do you want to come with us?'],
      ['Facciamo un aperitivo?', 'Shall we have an aperitif?'],
      ['Ho trovato un posto carino.', 'I found a nice place.'],
      ['Fammi sapere se puoi.', 'Let me know if you can.'],
      ['Sì, vengo volentieri!', 'Yes, I\'d love to come!'],
      ['Che fai domenica?', 'What are you doing Sunday?']
    ],
    sentences: [
      ['Ti va di venire al mare sabato?', 'Do you feel like coming to the beach Saturday?', {grammarPoint: 'Expression "ti va di" + infinitive.'}],
      ['Siamo un bel gruppo di amici.', 'We are a nice group of friends.', {grammarPoint: 'Adjective "bel" before a noun.'}],
      ['Purtroppo non posso venire, sono occupato.', 'Unfortunately I can\'t come, I\'m busy.', {grammarPoint: 'Adjective agreement "occupato".'}],
      ['Perché non usciamo tutti insieme?', 'Why don\'t we all go out together?', {grammarPoint: 'Interrogative "perché" for suggestions.'}],
      ['Ti mando l\'indirizzo del posto.', 'I\'ll send you the address of the place.', {grammarPoint: 'Articulated preposition "del".'}]
    ]
  },
  {
    id: 74,
    phrases: [
      ['La musica è troppo alta.', 'The music is too loud.'],
      ['Vuoi qualcosa da bere?', 'Do you want something to drink?'],
      ['Ti piace ballare?', 'Do you like to dance?'],
      ['È una festa divertente.', 'It\'s a fun party.'],
      ['Abbiamo amici comuni.', 'We have mutual friends.'],
      ['Conosci il festeggiato?', 'Do you know the birthday boy/host?']
    ],
    sentences: [
      ['Quanto tempo pensi di restare?', 'How long do you plan to stay?', {grammarPoint: 'Phrase "pensare di" + infinitive.'}],
      ['Devo andare via tra poco.', 'I have to leave soon.', {grammarPoint: 'Phrasal verb "andare via".'}],
      ['Hai già assaggiato questa bevanda?', 'Have you already tasted this drink?', {grammarPoint: 'Demonstrative "questa".'}],
      ['Non conosco quasi nessuno qui.', 'I know almost no one here.', {grammarPoint: 'Negative "non... nessuno".'}],
      ['Ci siamo divertiti molto stasera.', 'We had a lot of fun tonight.', {grammarPoint: 'Reflexive past tense "ci siamo divertiti".'}]
    ]
  },
  {
    id: 75,
    phrases: [
      ['Pronto, chi parla?', 'Hello, who is speaking?'],
      ['Non ti sento bene.', 'I can\'t hear you well.'],
      ['Ti richiamo tra un minuto.', 'I\'ll call you back in a minute.'],
      ['Scusi, ho sbagliato numero.', 'Sorry, I have the wrong number.'],
      ['Lascia un messaggio vocale.', 'Leave a voice message.'],
      ['A dopo allora!', 'See you later then!']
    ],
    sentences: [
      ['Il numero è sempre occupato.', 'The number is always busy.', {grammarPoint: 'Adverb "sempre" placement.'}],
      ['Mi dispiace, ma la linea è disturbata.', 'I\'m sorry, but the line is noisy.', {grammarPoint: 'Conjunction "ma".'}],
      ['Puoi parlare più forte, per favore?', 'Can you speak louder, please?', {grammarPoint: 'Comparative "più forte".'}],
      ['Ho provato a chiamarti prima.', 'I tried to call you earlier.', {grammarPoint: 'Enclitic pronoun "ti".'}],
      ['Mandami la posizione su WhatsApp.', 'Send me the location on WhatsApp.', {grammarPoint: 'Imperative "manda" + "mi".'}]
    ]
  },
  {
    id: 76,
    phrases: [
      ['Scrivimi quando arrivi.', 'Write to me when you arrive.'],
      ['Scusa se non ho risposto.', 'Sorry if I didn\'t reply.'],
      ['Ti mando una emoji.', 'I\'m sending you an emoji.'],
      ['Sono qui davanti!', 'I\'m here in front!'],
      ['Sto arrivando, aspetta.', 'I\'m coming, wait.'],
      ['Ok, perfetto, a tra poco.', 'Ok, perfect, see you soon.']
    ],
    sentences: [
      ['Ho un ritardo di cinque minuti.', 'I am five minutes late.', {grammarPoint: 'Noun "ritardo" with "avere".'}],
      ['Mandami la tua posizione, per favore.', 'Send me your location, please.', {grammarPoint: 'Possessive "tua".'}],
      ['Non riesco a visualizzare il messaggio.', 'I can\'t view the message.', {grammarPoint: 'Phrase "riuscire a" + infinitive.'}],
      ['Ti scrivo appena finisco di lavorare.', 'I\'ll write to you as soon as I finish working.', {grammarPoint: 'Conjunction "appena".'}],
      ['Rispondimi appena puoi, è urgente.', 'Answer me as soon as you can, it\'s urgent.', {grammarPoint: 'Imperative "rispondi" + "mi".'}]
    ]
  },
  {
    id: 77,
    phrases: [
      ['Mi dispiace molto.', 'I am very sorry.'],
      ['È stata colpa mia.', 'It was my fault.'],
      ['Scusami per il ritardo.', 'Forgive me for the delay.'],
      ['C\'era molto traffico.', 'There was a lot of traffic.'],
      ['Ho dimenticato le chiavi.', 'I forgot the keys.'],
      ['Non è un problema.', 'It\'s not a problem.']
    ],
    sentences: [
      ['Scusa, non volevo offenderti.', 'Sorry, I didn\'t mean to offend you.', {grammarPoint: 'Negative "non volevo" + infinitive.'}],
      ['Ti chiedo scusa sinceramente.', 'I sincerely apologize to you.', {grammarPoint: 'Adverb "sinceramente".'}],
      ['Spero che tu possa perdonarmi.', 'I hope you can forgive me.', {grammarPoint: 'Subjunctive "possa" (common in apologies).'}],
      ['Mi sono dimenticato di chiamarti.', 'I forgot to call you.', {grammarPoint: 'Reflexive "dimenticarsi".'}],
      ['Non preoccuparti, succede a tutti.', 'Don\'t worry, it happens to everyone.', {grammarPoint: 'Negative imperative "non preoccuparti".'}]
    ]
  },
  {
    id: 78,
    phrases: [
      ['Che bello questo vestito!', 'How beautiful this dress is!'],
      ['Sei stato bravissimo!', 'You were very good/skilled!'],
      ['Ottimo lavoro davvero.', 'Really excellent work.'],
      ['Mi piace molto la tua casa.', 'I really like your house.'],
      ['Che carino il tuo cane!', 'How cute your dog is!'],
      ['Complimenti per il successo!', 'Congratulations on the success!']
    ],
    sentences: [
      ['Grazie mille per il tuo aiuto.', 'Thanks a lot for your help.', {grammarPoint: 'Preposition "per" to indicate cause.'}],
      ['Anche tu sei molto elegante oggi.', 'You are very elegant today too.', {grammarPoint: 'Adverb "anche" meaning also/too.'}],
      ['Hai fatto un\'ottima scelta.', 'You made an excellent choice.', {grammarPoint: 'Adjective "ottima" before the noun.'}],
      ['Ti stanno molto bene questi occhiali.', 'These glasses look very good on you.', {grammarPoint: 'Expression "stare bene" + clothes.'}],
      ['Sei davvero bravo a cucinare.', 'You are really good at cooking.', {grammarPoint: 'Preposition "a" + infinitive.'}]
    ]
  },
  {
    id: 79,
    phrases: [
      ['Buon compleanno, Marco!', 'Happy birthday, Marco!'],
      ['Tanti auguri di cuore!', 'Best wishes from the heart!'],
      ['Ecco un piccolo regalo.', 'Here is a small gift.'],
      ['Facciamo un brindisi!', 'Let\'s make a toast!'],
      ['La torta è buonissima.', 'The cake is delicious.'],
      ['Spegni le candeline!', 'Blow out the candles!']
    ],
    sentences: [
      ['Spero che tu sia felice oggi.', 'I hope you are happy today.', {grammarPoint: 'Subjunctive "sia" with "spero che".'}],
      ['Abbiamo organizzato una festa sorpresa.', 'We organized a surprise party.', {grammarPoint: 'Passato prossimo of "organizzare".'}],
      ['Quante candeline ci sono sulla torta?', 'How many candles are on the cake?', {grammarPoint: 'Interrogative "quante" plural.'}],
      ['Ti auguro il meglio per il futuro.', 'I wish you the best for the future.', {grammarPoint: 'Verb "augurare" + indirect object.'}],
      ['Cin cin e tanti auguri a te!', 'Cheers and best wishes to you!', {grammarPoint: 'Typical Italian toast "cin cin".'}]
    ]
  },
  {
    id: 80,
    phrases: [
      ['Arrivederci e grazie.', 'Goodbye and thank you.'],
      ['A presto, spero!', 'See you soon, I hope!'],
      ['Buona giornata a tutti!', 'Have a good day everyone!'],
      ['Buona serata, divertitevi.', 'Good evening, have fun.'],
      ['Ci sentiamo nei prossimi giorni.', 'We\'ll talk in the next few days.'],
      ['Salutami la tua famiglia.', 'Say hi to your family for me.']
    ],
    sentences: [
      ['Devo andare adesso, sono in ritardo.', 'I have to go now, I\'m late.', {grammarPoint: 'Modal "devo" + infinitive.'}],
      ['È stato bello vederti dopo tanto tempo.', 'It was nice to see you after a long time.', {grammarPoint: 'Past tense of "essere".'}],
      ['Mi ha fatto piacere conoscerti.', 'I enjoyed meeting you.', {grammarPoint: 'Phrase "fare piacere".'}],
      ['Fai buon viaggio e a risentirci!', 'Have a good trip and talk to you soon!', {grammarPoint: 'Formal "risentirci" (hear from each other).'}],
      ['Scusami, ma ora devo proprio scappare.', 'Excuse me, but I really must run now.', {grammarPoint: 'Use of "proprio" for emphasis.'}]
    ]
  },
  {
    id: 81,
    phrases: [
      ['Due biglietti interi, per favore.', 'Two full price tickets, please.'],
      ['Ho diritto al ridotto?', 'Am I entitled to the reduced price?'],
      ['Vorrei anche un\'audioguida.', 'I would also like an audio guide.'],
      ['Ho la prenotazione online.', 'I have the online booking.'],
      ['Dov\'è il guardaroba?', 'Where is the cloakroom?'],
      ['In quale sala si trova il quadro?', 'In which hall is the painting?']
    ],
    sentences: [
      ['Gli studenti pagano il biglietto ridotto.', 'Students pay the reduced ticket.', {grammarPoint: 'Plural masculine article "Gli".'}],
      ['Non è permesso toccare le sculture.', 'It is not allowed to touch the sculptures.', {grammarPoint: 'Passive construction "non è permesso".'}],
      ['Il museo ospita quadri famosi in tutto il mondo.', 'The museum houses world-famous paintings.', {grammarPoint: 'Adjective "famosi" matching "quadri".'}],
      ['Deve lasciare la borsa al guardaroba.', 'You must leave your bag at the cloakroom.', {grammarPoint: 'Formal modal "deve".'}],
      ['L\'audioguida è disponibile in diverse lingue.', 'The audio guide is available in several languages.', {grammarPoint: 'Adjective "diverse" matching "lingue".'}]
    ]
  },
  {
    id: 82,
    phrases: [
      ['A che ora è la messa?', 'What time is the mass?'],
      ['Per favore, fate silenzio.', 'Please, be quiet.'],
      ['Bisogna avere le spalle coperte.', 'One must have covered shoulders.'],
      ['Ammira lo splendido altare.', 'Admire the splendid altar.'],
      ['Guarda che bella cupola!', 'Look what a beautiful dome!'],
      ['L\'ingresso è libero qui?', 'Is entry free here?']
    ],
    sentences: [
      ['Gli affreschi sono stati recentemente restaurati.', 'The frescoes have been recently restored.', {grammarPoint: 'Passive "sono stati restaurati".'}],
      ['È gradita una piccola offerta per la chiesa.', 'A small donation for the church is appreciated.', {grammarPoint: 'Adjective "gradita" matching "offerta".'}],
      ['Non si possono fare foto durante la messa.', 'You cannot take photos during mass.', {grammarPoint: 'Impersonal "si possono".'}],
      ['La cupola è stata progettata da un famoso architetto.', 'The dome was designed by a famous architect.', {grammarPoint: 'Preposition "da" for the agent.'}],
      ['Entriamo in chiesa con rispetto.', 'Let\'s enter the church with respect.', {grammarPoint: 'First person plural present.'}]
    ]
  },
  {
    id: 83,
    phrases: [
      ['A che ora inizia il film?', 'What time does the movie start?'],
      ['Per quale spettacolo ci sono posti?', 'For which showtime are there seats?'],
      ['È in lingua originale con sottotitoli?', 'Is it in the original language with subtitles?'],
      ['Preferisco il film doppiato.', 'I prefer the dubbed movie.'],
      ['Prendiamo dei popcorn grandi?', 'Shall we get large popcorn?'],
      ['Siamo nella fila dieci.', 'We are in row ten.']
    ],
    sentences: [
      ['I posti non sono numerati.', 'The seats are not numbered.', {grammarPoint: 'Negative plural agreement.'}],
      ['Lo schermo di questa sala è enorme.', 'The screen in this hall is huge.', {grammarPoint: 'Adjective "enorme" is invariable for gender.'}],
      ['Abbiamo prenotato i biglietti online.', 'We booked the tickets online.', {grammarPoint: 'Passato prossimo with "avere".'}],
      ['Qual è il tuo genere di film preferito?', 'What is your favorite movie genre?', {grammarPoint: 'Possessive "tuo".'}],
      ['C\'è troppa gente in fila alla cassa.', 'There are too many people in line at the cash desk.', {grammarPoint: 'Adjective "troppa" matching "gente".'}]
    ]
  },
  {
    id: 84,
    phrases: [
      ['Abbiamo i posti in platea.', 'We have seats in the stalls.'],
      ['Si vede bene dal balcone?', 'Is there a good view from the balcony?'],
      ['Posso avere un programma?', 'Can I have a program?'],
      ['Gli attori sono bravissimi.', 'The actors are very good.'],
      ['Ci vediamo durante l\'intervallo.', 'See you during the intermission.'],
      ['Il sipario si sta aprendo.', 'The curtain is opening.']
    ],
    sentences: [
      ['Il palco è decorato magnificamente.', 'The stage is magnificently decorated.', {grammarPoint: 'Adverb "magnificamente".'}],
      ['Alla fine c\'è stato un lungo applauso.', 'At the end there was a long applause.', {grammarPoint: 'Use of "c\'è stato" (there was).'}],
      ['Gli spettatori devono spegnere i cellulari.', 'Spectators must turn off their cell phones.', {grammarPoint: 'Modal verb "devono".'}],
      ['L\'opera è divisa in tre atti.', 'The opera is divided into three acts.', {grammarPoint: 'Passive "è divisa".'}],
      ['Preferite i posti nel palco o in platea?', 'Do you prefer seats in the box or in the stalls?', {grammarPoint: 'Plural you "preferite".'}]
    ]
  },
  {
    id: 85,
    phrases: [
      ['Quando inizia il concerto?', 'When does the concert start?'],
      ['La band suona molto bene.', 'The band plays very well.'],
      ['Il cantante ha una bella voce.', 'The singer has a beautiful voice.'],
      ['Ho comprato il biglietto online.', 'I bought the ticket online.'],
      ['È un posto in piedi?', 'Is it a standing place?'],
      ['Vogliamo il bis!', 'We want an encore!']
    ],
    sentences: [
      ['L\'ingresso è consentito dalle ore venti.', 'Entry is allowed from 8 PM.', {grammarPoint: 'Preposition "dalle" (da + le).'}],
      ['Il volume della musica è troppo alto.', 'The volume of the music is too high.', {grammarPoint: 'Adjective "alto" matching "volume".'}],
      ['C\'è molta gente davanti al palco.', 'There are many people in front of the stage.', {grammarPoint: 'Preposition "davanti a".'}],
      ['Abbiamo ballato tutta la sera.', 'We danced all evening.', {grammarPoint: 'Expression "tutta la sera".'}],
      ['La band farà un tour in Italia l\'anno prossimo.', 'The band will tour Italy next year.', {grammarPoint: 'Future tense of "fare".'}]
    ]
  },
  {
    id: 86,
    phrases: [
      ['Questa galleria è molto famosa.', 'This gallery is very famous.'],
      ['Chi è l\'artista di questa opera?', 'Who is the artist of this work?'],
      ['Preferisco l\'arte moderna.', 'I prefer modern art.'],
      ['Mi piace lo stile classico.', 'I like the classical style.'],
      ['I colori sono molto vivaci.', 'The colors are very vivid.'],
      ['Vorrei comprare il catalogo.', 'I would like to buy the catalog.']
    ],
    sentences: [
      ['Mi interessa molto la pittura contemporanea.', 'I am very interested in contemporary painting.', {grammarPoint: 'Verb "interessare" used like "piacere".'}],
      ['Questo disegno è fatto a matita.', 'This drawing is done in pencil.', {grammarPoint: 'Passive "è fatto".'}],
      ['L\'esposizione dura fino al prossimo mese.', 'The exhibition lasts until next month.', {grammarPoint: 'Preposition "fino al".'}],
      ['Ci sono molte opere di artisti locali.', 'There are many works by local artists.', {grammarPoint: 'Preposition "di" for authorship.'}],
      ['L\'ingresso alla galleria è gratuito il lunedì.', 'Entry to the gallery is free on Mondays.', {grammarPoint: 'Adjective "gratuito".'}]
    ]
  },
  {
    id: 87,
    phrases: [
      ['Dove inizia il tour guidato?', 'Where does the guided tour start?'],
      ['Aspettiamo il resto del gruppo.', 'We are waiting for the rest of the group.'],
      ['Qual è il punto d\'incontro?', 'What is the meeting point?'],
      ['Quanto dura la visita?', 'How long does the visit last?'],
      ['Mi serve un auricolare.', 'I need a headset.'],
      ['Per favore, seguite la guida.', 'Please follow the guide.']
    ],
    sentences: [
      ['Faremo una breve pausa foto tra poco.', 'We will take a short photo break shortly.', {grammarPoint: 'Future "faremo".'}],
      ['Ci sarà spazio per le domande finali.', 'There will be space for final questions.', {grammarPoint: 'Future "ci sarà".'}],
      ['La durata totale è di circa due ore.', 'The total duration is about two hours.', {grammarPoint: 'Preposition "di" before duration.'}],
      ['Potete sentire bene con l\'auricolare?', 'Can you hear well with the headset?', {grammarPoint: 'Plural modal "potete".'}],
      ['Seguite sempre l\'ombrello colorato della guida.', 'Always follow the guide\'s colored umbrella.', {grammarPoint: 'Imperative "seguite".'}]
    ]
  },
  {
    id: 88,
    phrases: [
      ['Queste rovine sono romane.', 'These ruins are Roman.'],
      ['Visitiamo il castello medievale.', 'Let\'s visit the medieval castle.'],
      ['Camminiamo lungo le mura.', 'Let\'s walk along the walls.'],
      ['Risale al quindicesimo secolo.', 'It dates back to the 15th century.'],
      ['È un sito molto antico.', 'It is a very ancient site.'],
      ['Il panorama è fantastico.', 'The view is fantastic.']
    ],
    sentences: [
      ['Alcune parti sono attualmente in restauro.', 'Some parts are currently under restoration.', {grammarPoint: 'Prepositional phrase "in restauro".'}],
      ['Seguite il percorso indicato sulla mappa.', 'Follow the route indicated on the map.', {grammarPoint: 'Past participle "indicato".'}],
      ['Dalle mura si gode una vista bellissima.', 'From the walls you can enjoy a beautiful view.', {grammarPoint: 'Impersonal "si gode".'}],
      ['Questo edificio ha più di mille anni.', 'This building is more than a thousand years old.', {grammarPoint: 'Phrase "più di" for comparisons.'}],
      ['È vietato salire sulle rovine.', 'It is forbidden to climb on the ruins.', {grammarPoint: 'Expression "è vietato" + infinitive.'}]
    ]
  },
  {
    id: 89,
    phrases: [
      ['Andiamo alla sagra del paese.', 'Let\'s go to the village festival.'],
      ['La processione inizia alle sei.', 'The procession starts at six.'],
      ['A che ora sono i fuochi?', 'What time are the fireworks?'],
      ['Ci sono molte bancarelle carine.', 'There are many cute stalls.'],
      ['È una tradizione locale.', 'It\'s a local tradition.'],
      ['Ci vediamo in piazza principale.', 'See you in the main square.']
    ],
    sentences: [
      ['Molti indossano costumi tradizionali.', 'Many people wear traditional costumes.', {grammarPoint: 'Present tense of "indossare".'}],
      ['Il programma della festa è molto ricco.', 'The festival program is very rich.', {grammarPoint: 'Adjective "ricco" matching "programma".'}],
      ['Abbiamo mangiato cibo tipico alla sagra.', 'We ate typical food at the festival.', {grammarPoint: 'Adjective "tipico" matching "cibo".'}],
      ['I fuochi d\'artificio iniziano a mezzanotte.', 'The fireworks start at midnight.', {grammarPoint: 'Preposition "a" before "mezzanotte".'}],
      ['La piazza è piena di gente stasera.', 'The square is full of people tonight.', {grammarPoint: 'Adjective "piena" matching "piazza".'}]
    ]
  },
  {
    id: 90,
    phrases: [
      ['Vai alla partita oggi?', 'Are you going to the match today?'],
      ['Lo stadio è grandissimo.', 'The stadium is huge.'],
      ['Per quale squadra tifi?', 'Which team do you support?'],
      ['Sono un tifoso della Roma.', 'I am a Roma fan.'],
      ['Che bel goal!', 'What a beautiful goal!'],
      ['Qual è il risultato finale?', 'What is the final score?']
    ],
    sentences: [
      ['Ho un posto numerato in tribuna.', 'I have a numbered seat in the stand.', {grammarPoint: 'Adjective "numerato".'}],
      ['L\'arbitro ha fischiato la fine.', 'The referee blew for the end.', {grammarPoint: 'Passato prossimo of "fischiare".'}],
      ['C\'è molta tensione tra i tifosi.', 'There is a lot of tension among the fans.', {grammarPoint: 'Preposition "tra" (among).'}],
      ['La mia squadra ha vinto il campionato.', 'My team won the championship.', {grammarPoint: 'Possessive "mia" with feminine noun.'}],
      ['Lo stadio si trova fuori città.', 'The stadium is located outside the city.', {grammarPoint: 'Adverbial phrase "fuori città".'}]
    ]
  }
];

const part4 = [
  {
    id: 91,
    phrases: [
      ['È una buona abitudine.', 'It is a good habit.'],
      ['È molto educato.', 'It is very polite.'],
      ['Come devo salutare?', 'How should I greet?'],
      ['A che ora è la cena?', 'What time is dinner?'],
      ['La mancia non è obbligatoria.', 'Tipping is not mandatory.'],
      ['È normale fare questo gesto?', 'Is it normal to make this gesture?']
    ],
    sentences: [
      ['In Italia, è un\'abitudine bere il caffè dopo pranzo.', 'In Italy, it is a habit to drink coffee after lunch.', {grammarPoint: 'Impersonal construction "è un\'abitudine".'}],
      ['È educato salutare quando si entra in un negozio.', 'It is polite to greet when entering a shop.', {grammarPoint: 'Impersonal "si entra".'}],
      ['L\'orario della cena è di solito verso le otto.', 'Dinner time is usually around eight.', {grammarPoint: 'Telling time with "le otto".'}],
      ['Il coperto è spesso incluso nel conto al ristorante.', 'The cover charge is often included in the bill at the restaurant.', {grammarPoint: 'Usage of passive "è incluso".'}],
      ['Dare la mancia non è normale, ma è apprezzato.', 'Tipping is not normal, but it is appreciated.', {grammarPoint: 'Infinitive "dare" used as a subject.'}]
    ]
  },
  {
    id: 92,
    phrases: [
      ['Quando è stato fondato?', 'When was it founded?'],
      ['Risale al Medioevo.', 'It dates back to the Middle Ages.'],
      ['C\'è una famiglia nobile.', 'There is a noble family.'],
      ['È una vecchia leggenda.', 'It is an old legend.'],
      ['Qual è questo monumento?', 'What is this monument?'],
      ['È un racconto interessante.', 'It is an interesting story.']
    ],
    sentences: [
      ['Questo paese è stato fondato dai Romani.', 'This town was founded by the Romans.', {grammarPoint: 'Passive voice "è stato fondato".'}],
      ['Molti palazzi del centro risalgono al Medioevo.', 'Many palaces in the center date back to the Middle Ages.', {grammarPoint: 'Verb "risalire" (to date back).'}],
      ['Questa villa apparteneva a una famiglia nobile.', 'This villa belonged to a noble family.', {grammarPoint: 'Imperfect tense "apparteneva".'}],
      ['C\'è una famosa leggenda su questo castello.', 'There is a famous legend about this castle.', {grammarPoint: 'Use of "c\'è" (there is).'}],
      ['Il monumento si trova nel quartiere antico.', 'The monument is located in the old district.', {grammarPoint: 'Reflexive "si trova" for location.'}]
    ]
  },
  {
    id: 93,
    phrases: [
      ['Ho mal di gola.', 'I have a sore throat.'],
      ['Ho il naso chiuso.', 'I have a blocked nose.'],
      ['Vorrei delle pastiglie.', 'I would like some lozenges.'],
      ['Prendo lo sciroppo.', 'I am taking the syrup.'],
      ['Mi serve un termometro.', 'I need a thermometer.'],
      ['Qual è l\'effetto?', 'What is the effect?']
    ],
    sentences: [
      ['Ho un forte mal di gola da due giorni.', 'I have had a bad sore throat for two days.', {grammarPoint: 'Present tense with "da" for duration.'}],
      ['Per il naso chiuso, le consiglio queste gocce.', 'For a blocked nose, I recommend these drops.', {grammarPoint: 'Formal pronoun "le" (to you).'}],
      ['Quante pastiglie posso prendere al giorno?', 'How many lozenges can I take a day?', {grammarPoint: 'Modal verb "posso".'}],
      ['La dose giornaliera è di un misurino di sciroppo.', 'The daily dose is one measuring cup of syrup.', {grammarPoint: 'Preposition "di" indicating amount.'}],
      ['Questa medicina può causare una leggera sonnolenza.', 'This medicine can cause mild sleepiness.', {grammarPoint: 'Modal verb "può".'}]
    ]
  },
  {
    id: 94,
    phrases: [
      ['Devo vedere un medico.', 'I need to see a doctor.'],
      ['Quali sono i sintomi?', 'What are the symptoms?'],
      ['Ho bisogno di una visita.', 'I need a visit.'],
      ['Ho l\'assicurazione sanitaria.', 'I have health insurance.'],
      ['Ecco la tessera sanitaria.', 'Here is the health card.'],
      ['È solo un controllo.', 'It is just a checkup.']
    ],
    sentences: [
      ['Vorrei prenotare una visita con il medico.', 'I would like to book a visit with the doctor.', {grammarPoint: 'Conditional "vorrei" for polite requests.'}],
      ['Il principale sintomo è una forte tosse secca.', 'The main symptom is a bad dry cough.', {grammarPoint: 'Adjective placement before and after noun.'}],
      ['Il dottore misurerà la pressione prima della visita.', 'The doctor will measure the blood pressure before the visit.', {grammarPoint: 'Future tense "misurerà".'}],
      ['Per favore, porti con sé la tessera sanitaria.', 'Please bring your health card with you.', {grammarPoint: 'Formal imperative "porti".'}],
      ['Dobbiamo aspettare la diagnosi dopo il controllo.', 'We have to wait for the diagnosis after the checkup.', {grammarPoint: 'Modal verb "dobbiamo".'}]
    ]
  },
  {
    id: 95,
    phrases: [
      ['Dov\'è il pronto soccorso?', 'Where is the emergency room?'],
      ['C\'è stato un incidente.', 'There has been an accident.'],
      ['Faccio fatica a respirare.', 'I am having trouble breathing.'],
      ['C\'è molto sangue.', 'There is a lot of blood.'],
      ['Ho un dolore forte.', 'I have a strong pain.'],
      ['Ho bisogno di aiuto subito.', 'I need help immediately.']
    ],
    sentences: [
      ['Portatelo subito al pronto soccorso, è un\'emergenza.', 'Take him to the emergency room immediately, it\'s an emergency.', {grammarPoint: 'Imperative with pronoun "portatelo".'}],
      ['C\'è stato un brutto incidente sulla strada.', 'There was a bad accident on the road.', {grammarPoint: 'Passato prossimo of "esserci" (c\'è stato).'}],
      ['Il paziente ha difficoltà a respirare da solo.', 'The patient has difficulty breathing on his own.', {grammarPoint: 'Preposition "a" after "difficoltà".'}],
      ['L\'infermiere sta arrivando per aiutarla subito.', 'The nurse is coming to help you immediately.', {grammarPoint: 'Present progressive "sta arrivando".'}],
      ['Sento un dolore molto forte alla gamba destra.', 'I feel a very strong pain in my right leg.', {grammarPoint: 'Preposition "a" combined with article (alla).'}],
      ['L\'attesa al pronto soccorso può essere lunga.', 'The wait at the emergency room can be long.', {grammarPoint: 'Feminine adjective agreement.'}]
    ]
  },
  {
    id: 96,
    phrases: [
      ['Devo andare dal dentista.', 'I need to go to the dentist.'],
      ['Mi fa male un dente.', 'A tooth hurts.'],
      ['La gengiva sanguina.', 'The gum is bleeding.'],
      ['Penso di avere una carie.', 'I think I have a cavity.'],
      ['Vorrei la pulizia dei denti.', 'I would like a teeth cleaning.'],
      ['Il dente è molto sensibile.', 'The tooth is very sensitive.']
    ],
    sentences: [
      ['Ho preso appuntamento dal dentista per domani mattina.', 'I made an appointment with the dentist for tomorrow morning.', {grammarPoint: 'Preposition "da" with professions (dal dentista).'}],
      ['Mi fa male un dente quando provo a mordere.', 'A tooth hurts when I try to bite.', {grammarPoint: 'Expression "mi fa male" (it hurts me).'}],
      ['Il dentista ha detto che devo curare una carie.', 'The dentist said I need to treat a cavity.', {grammarPoint: 'Reported speech with "ha detto che".'}],
      ['Farò la pulizia dei denti la prossima settimana.', 'I will get a teeth cleaning next week.', {grammarPoint: 'Future tense "farò".'}],
      ['Sentirai un po\' di dolore, ma ti farò l\'anestesia.', 'You will feel a bit of pain, but I will give you anesthesia.', {grammarPoint: 'Future tense "sentirai", "farò".'}],
      ['La mia gengiva è sensibile alle bevande fredde.', 'My gum is sensitive to cold drinks.', {grammarPoint: 'Preposition "a" combined with article.'}]
    ]
  },
  {
    id: 97,
    phrases: [
      ['Vorrei una scatola di aspirina.', 'I would like a box of aspirin.'],
      ['È una compressa o una capsula?', 'Is it a tablet or a capsule?'],
      ['Da prendere prima dei pasti.', 'To be taken before meals.'],
      ['Da prendere dopo i pasti.', 'To be taken after meals.'],
      ['Due volte al giorno.', 'Twice a day.'],
      ['Ha il farmaco generico?', 'Do you have the generic drug?']
    ],
    sentences: [
      ['Deve prendere una compressa con un bicchiere d\'acqua.', 'You must take one tablet with a glass of water.', {grammarPoint: 'Formal modal "deve".'}],
      ['Le consiglio di prendere questa capsula prima dei pasti.', 'I advise you to take this capsule before meals.', {grammarPoint: 'Formal indirect object pronoun "le".'}],
      ['Prenda questa medicina due volte al giorno.', 'Take this medicine twice a day.', {grammarPoint: 'Formal imperative "prenda".'}],
      ['Legga attentamente il foglietto per ogni controindicazione.', 'Read the leaflet carefully for any contraindication.', {grammarPoint: 'Formal imperative "legga".'}],
      ['Il farmaco generico ha lo stesso effetto e costa meno.', 'The generic drug has the same effect and costs less.', {grammarPoint: 'Comparative "meno".'}]
    ]
  },
  {
    id: 98,
    phrases: [
      ['Vorrei comprare una SIM.', 'I would like to buy a SIM card.'],
      ['Cerco una ricaricabile.', 'I am looking for a prepaid one.'],
      ['Quanti dati ci sono?', 'How much data is there?'],
      ['Ha minuti illimitati?', 'Does it have unlimited minutes?'],
      ['Serve un documento?', 'Is an ID needed?'],
      ['Qual è la copertura?', 'What is the coverage like?']
    ],
    sentences: [
      ['Per attivare la nuova SIM, ho bisogno di un documento.', 'To activate the new SIM, I need an ID.', {grammarPoint: 'Expression "avere bisogno di" (to need).'}],
      ['Vorrei una SIM ricaricabile con molti dati per navigare.', 'I would like a prepaid SIM with a lot of data for browsing.', {grammarPoint: 'Preposition "per" + infinitive.'}],
      ['Questo piano mensile include minuti illimitati.', 'This monthly plan includes unlimited minutes.', {grammarPoint: 'Adjective "illimitati" matching "minuti".'}],
      ['L\'attivazione del nuovo numero richiederà circa venti minuti.', 'The activation of the new number will take about twenty minutes.', {grammarPoint: 'Future tense "richiederà".'}],
      ['Questa compagnia ha un\'ottima copertura in tutta Italia.', 'This company has excellent coverage all over Italy.', {grammarPoint: 'Absolute superlative "ottima".'}]
    ]
  },
  {
    id: 99,
    phrases: [
      ['Il telefono non si collega.', 'The phone does not connect.'],
      ['Qual è il nome della rete?', 'What is the network name?'],
      ['Prova a riavviare.', 'Try to restart it.'],
      ['Il segnale è debole.', 'The signal is weak.'],
      ['Dice che il codice è errato.', 'It says the code is wrong.'],
      ['Sono di nuovo online.', 'I am back online.']
    ],
    sentences: [
      ['Il mio computer non si collega alla rete dell\'hotel.', 'My computer does not connect to the hotel network.', {grammarPoint: 'Reflexive verb "collegarsi".'}],
      ['Qual è il nome della rete e la password per favore?', 'What is the network name and the password please?', {grammarPoint: 'Interrogative "Qual è".'}],
      ['Forse è meglio riavviare il modem per sistemare il problema.', 'Maybe it is better to restart the modem to fix the problem.', {grammarPoint: 'Impersonal "è meglio" + infinitive.'}],
      ['Non riesco a navigare perché il segnale è molto debole.', 'I cannot browse because the signal is very weak.', {grammarPoint: 'Verb "riuscire a" (to manage to/can).'}],
      ['Ho inserito la password ma dice che il codice è errato.', 'I entered the password but it says the code is wrong.', {grammarPoint: 'Conjunction "ma" linking clauses.'}]
    ]
  },
  {
    id: 100,
    phrases: [
      ['Fate la riparazione?', 'Do you do repairs?'],
      ['Ho il vetro rotto.', 'I have broken glass.'],
      ['Lo schermo è nero.', 'The screen is black.'],
      ['Posso avere un preventivo?', 'Can I have a quote?'],
      ['È in garanzia?', 'Is it under warranty?'],
      ['Ho fatto il backup.', 'I did the backup.']
    ],
    sentences: [
      ['Quanto costa la riparazione per un vetro rotto del telefono?', 'How much does the repair cost for a broken phone glass?', {grammarPoint: 'Preposition "per".'}],
      ['Il telefono si accende, ma ha lo schermo nero.', 'The phone turns on, but it has a black screen.', {grammarPoint: 'Reflexive verb "accendersi".'}],
      ['Mi può fare un preventivo prima di ordinare il pezzo?', 'Can you give me a quote before ordering the part?', {grammarPoint: 'Formal request with "può fare".'}],
      ['Questa riparazione dovrebbe essere coperta dalla garanzia.', 'This repair should be covered by the warranty.', {grammarPoint: 'Conditional "dovrebbe" and passive voice.'}],
      ['Qual è il tempo necessario per cambiare la batteria?', 'What is the time needed to change the battery?', {grammarPoint: 'Adjective "necessario".'}]
    ]
  },
  {
    id: 101,
    phrases: [
      ['Devo caricare il telefono.', 'I need to charge the phone.'],
      ['C\'è una presa USB?', 'Is there a USB port?'],
      ['Ho un power bank.', 'I have a power bank.'],
      ['Mi serve un adattatore europeo.', 'I need a European adapter.'],
      ['Hai un cavo lightning?', 'Do you have a Lightning cable?'],
      ['La batteria è scarica.', 'The battery is low.']
    ],
    sentences: [
      ['Devo caricare il portatile perché la batteria è scarica.', 'I need to charge the laptop because the battery is low.', {grammarPoint: 'Causal clause with "perché".'}],
      ['Mi scusi, c\'è una presa libera per caricare il cellulare?', 'Excuse me, is there a free outlet to charge the cell phone?', {grammarPoint: 'Use of "c\'è" for existence.'}],
      ['Ho portato il mio power bank per i lunghi viaggi in treno.', 'I brought my power bank for long train trips.', {grammarPoint: 'Plural adjectives and nouns.'}],
      ['Non posso usare la spina senza un adattatore europeo.', 'I cannot use the plug without a European adapter.', {grammarPoint: 'Negative modal "non posso".'}],
      ['C\'è una presa USB disponibile sull\'aereo o in aeroporto?', 'Is there a USB port available on the plane or at the airport?', {grammarPoint: 'Preposition "su" + article.'}]
    ]
  },
  {
    id: 102,
    phrases: [
      ['Condivido la mia posizione.', 'I share my location.'],
      ['Sto calcolando il percorso.', 'I am calculating the route.'],
      ['Avvia la navigazione.', 'Start the navigation.'],
      ['Ci andiamo a piedi.', 'We are walking there.'],
      ['Posso salvare la mappa.', 'I can save the map.'],
      ['Funziona anche offline.', 'It works offline too.']
    ],
    sentences: [
      ['Ti invio la mia posizione così puoi trovarmi facilmente.', 'I will send you my location so you can find me easily.', {grammarPoint: 'Indirect object pronoun "ti".'}],
      ['Questo percorso è il più veloce in auto ma ci sono pedaggi.', 'This route is the fastest by car but there are tolls.', {grammarPoint: 'Superlative "il più veloce".'}],
      ['Usa l\'app per la navigazione a piedi nel centro storico.', 'Use the app for walking navigation in the historic center.', {grammarPoint: 'Imperative "usa".'}],
      ['Ricordati di scaricare la mappa offline per non usare i dati.', 'Remember to download the offline map to not use data.', {grammarPoint: 'Reflexive imperative "ricordati".'}],
      ['Devo aggiornare l\'applicazione per avere le ultime mappe.', 'I need to update the application to have the latest maps.', {grammarPoint: 'Modal verb "devo".'}]
    ]
  },
  {
    id: 103,
    phrases: [
      ['Facciamo una videochiamata?', 'Shall we do a video call?'],
      ['Accendi il microfono.', 'Turn on the microphone.'],
      ['La telecamera è spenta.', 'The camera is off.'],
      ['Sei muto.', 'You are muted.'],
      ['Posso condividere lo schermo?', 'Can I share the screen?'],
      ['La connessione è lenta.', 'The connection is slow.']
    ],
    sentences: [
      ['Preferisco fare una videochiamata per parlare con la mia famiglia.', 'I prefer to make a video call to talk to my family.', {grammarPoint: 'Verb "preferire".'}],
      ['Non ti sento, penso che il tuo microfono sia spento.', 'I don\'t hear you, I think your microphone is off.', {grammarPoint: 'Subjunctive "sia" after "penso che".'}],
      ['Puoi accendere la telecamera così posso vederti bene?', 'Can you turn on the camera so I can see you well?', {grammarPoint: 'Attached pronoun in "vederti".'}],
      ['Ora proverò a condividere lo schermo per farti vedere il progetto.', 'Now I will try to share the screen to show you the project.', {grammarPoint: 'Causative "farti vedere".'}],
      ['La connessione lenta mi impedisce di vedere bene il video.', 'The slow connection prevents me from seeing the video well.', {grammarPoint: 'Verb "impedire di".'}]
    ]
  },
  {
    id: 104,
    phrases: [
      ['L\'ho visto sul sito web.', 'I saw it on the website.'],
      ['Faccio la prenotazione online.', 'I make the online reservation.'],
      ['Ho la conferma email.', 'I have the email confirmation.'],
      ['Usa il codice QR.', 'Use the QR code.'],
      ['Devo creare un account?', 'Do I need to create an account?'],
      ['C\'è stato un errore.', 'There was an error.']
    ],
    sentences: [
      ['Ho appena fatto una prenotazione online sul vostro sito web.', 'I just made an online reservation on your website.', {grammarPoint: 'Passato prossimo "ho fatto".'}],
      ['Controlla la posta per vedere se è arrivata la conferma.', 'Check your mail to see if the confirmation arrived.', {grammarPoint: 'Imperative "controlla".'}],
      ['Per entrare al museo, puoi semplicemente mostrare il codice QR.', 'To enter the museum, you can simply show the QR code.', {grammarPoint: 'Adverb ending in -mente.'}],
      ['Non riesco a fare il pagamento senza accedere al mio account.', 'I cannot make the payment without logging into my account.', {grammarPoint: 'Preposition "senza" + infinitive.'}],
      ['Volevo sapere se è possibile annullare gratuitamente la prenotazione.', 'I wanted to know if it is possible to cancel the reservation for free.', {grammarPoint: 'Imperfect "volevo" for politeness.'}]
    ]
  },
  {
    id: 105,
    phrases: [
      ['Devo prelevare dei soldi.', 'I need to withdraw some money.'],
      ['Qual è il mio saldo?', 'What is my balance?'],
      ['Controllo il conto.', 'I check the account.'],
      ['La carta è inserita.', 'The card is inserted.'],
      ['Dice che il pin è errato.', 'It says the PIN is wrong.'],
      ['L\'operazione è conclusa.', 'The operation is finished.']
    ],
    sentences: [
      ['Vorrei prelevare cinquanta euro dal mio conto corrente.', 'I would like to withdraw fifty euros from my checking account.', {grammarPoint: 'Conditional "vorrei".'}],
      ['Puoi controllare il saldo prima di ritirare i soldi?', 'Can you check the balance before withdrawing the money?', {grammarPoint: 'Preposition "prima di".'}],
      ['Assicurati che la carta sia inserita correttamente nello sportello.', 'Make sure the card is inserted correctly into the machine.', {grammarPoint: 'Subjunctive "sia" after "assicurati che".'}],
      ['Se metti un pin errato per tre volte, la carta verrà bloccata.', 'If you enter a wrong PIN three times, the card will be blocked.', {grammarPoint: 'Passive future "verrà bloccata".'}],
      ['Purtroppo non ci sono abbastanza contanti disponibili in questo momento.', 'Unfortunately there is not enough cash available right now.', {grammarPoint: 'Adverb "abbastanza".'}]
    ]
  },
  {
    id: 106,
    phrases: [
      ['Chiamate la polizia!', 'Call the police!'],
      ['Vado dai carabinieri.', 'I am going to the Carabinieri.'],
      ['Voglio denunciare un furto.', 'I want to report a theft.'],
      ['Ho un documento perso.', 'I have a lost document.'],
      ['Questa è la descrizione.', 'This is the description.'],
      ['Manca la firma.', 'The signature is missing.']
    ],
    sentences: [
      ['Devo andare subito dalla polizia per denunciare il furto.', 'I have to go to the police right away to report the theft.', {grammarPoint: 'Preposition "da" for people/offices (dalla polizia).'}],
      ['I carabinieri mi hanno chiesto una descrizione della persona.', 'The carabinieri asked me for a description of the person.', {grammarPoint: 'Passato prossimo with indirect pronoun "mi hanno chiesto".'}],
      ['Voglio fare una denuncia per un documento perso in stazione.', 'I want to make a report for a document lost at the station.', {grammarPoint: 'Use of "per" indicating reason.'}],
      ['L\'ufficiale sta scrivendo la denuncia con la data di oggi.', 'The officer is writing the report with today\'s date.', {grammarPoint: 'Present progressive "sta scrivendo".'}],
      ['Metti una firma in fondo alla pagina per confermare.', 'Put a signature at the bottom of the page to confirm.', {grammarPoint: 'Imperative "metti".'}]
    ]
  },
  {
    id: 107,
    phrases: [
      ['Scusi, può aiutarmi?', 'Excuse me, can you help me?'],
      ['Ho bisogno di un favore.', 'I need a favor.'],
      ['Non so dove mi trovo.', 'I do not know where I am.'],
      ['Sto cercando la stazione.', 'I am looking for the station.'],
      ['È un problema piccolo.', 'It is a small problem.'],
      ['Lei è molto gentile.', 'You are very kind.']
    ],
    sentences: [
      ['Mi scusi, può aiutarmi a trovare questa via sulla mappa?', 'Excuse me, can you help me find this street on the map?', {grammarPoint: 'Formal "può aiutarmi" with attached pronoun.'}],
      ['Ho bisogno di una mano con queste valigie pesanti, per favore.', 'I need a hand with these heavy suitcases, please.', {grammarPoint: 'Expression "avere bisogno di".'}],
      ['Sto cercando di capire dove si trova la farmacia più vicina.', 'I am looking to understand where the nearest pharmacy is.', {grammarPoint: 'Present progressive "sto cercando".'}],
      ['Ho solo un problema piccolo con la porta della mia camera.', 'I just have a small problem with the door of my room.', {grammarPoint: 'Diminutive adjective usage.'}],
      ['Grazie davvero per il suo aiuto, è stato molto gentile.', 'Thank you really for your help, you were very kind.', {grammarPoint: 'Formal adjective "suo" and "è stato".'}]
    ]
  },
  {
    id: 108,
    phrases: [
      ['Costa dieci euro.', 'It costs ten euros.'],
      ['Mi manca un centesimo.', 'I am missing a cent.'],
      ['Posso avere il cambio?', 'Can I have the change?'],
      ['È una banconota da venti.', 'It is a twenty banknote.'],
      ['Hai una moneta?', 'Do you have a coin?'],
      ['È molto economico.', 'It is very cheap.']
    ],
    sentences: [
      ['Il prezzo totale è di quindici euro e cinquanta centesimi.', 'The total price is fifteen euros and fifty cents.', {grammarPoint: 'Numbers and currency.'}],
      ['Può farmi il cambio per una banconota da cinquanta euro?', 'Can you give me change for a fifty-euro banknote?', {grammarPoint: 'Formal request with "può farmi".'}],
      ['Hai una moneta da due euro per il carrello della spesa?', 'Do you have a two-euro coin for the shopping cart?', {grammarPoint: 'Preposition "da" indicating value (moneta da due euro).'}],
      ['Questo ristorante è molto buono, ma purtroppo è troppo caro.', 'This restaurant is very good, but unfortunately it is too expensive.', {grammarPoint: 'Adverbs "purtroppo" and "troppo".'}],
      ['Tieni pure il resto, non mi servono le monete.', 'Keep the change, I don\'t need the coins.', {grammarPoint: 'Verb "servire" (to be useful/needed) with indirect object.'}]
    ]
  },
  {
    id: 109,
    phrases: [
      ['Scusa, che ore sono?', 'Excuse me, what time is it?'],
      ['Mangiamo a mezzogiorno.', 'We eat at noon.'],
      ['Arrivo prima di mezzanotte.', 'I arrive before midnight.'],
      ['È la prossima settimana.', 'It is next week.'],
      ['In che mese siamo?', 'What month are we in?'],
      ['Cerca di essere puntuale.', 'Try to be on time.']
    ],
    sentences: [
      ['Mi scusi, mi sa dire che ore sono esattamente adesso?', 'Excuse me, can you tell me what time it is exactly now?', {grammarPoint: 'Indirect question "che ore sono".'}],
      ['Il treno parte alle dodici in punto, a mezzogiorno.', 'The train leaves at exactly twelve, at noon.', {grammarPoint: 'Preposition "a" with specific times.'}],
      ['La festa finirà probabilmente molto dopo la mezzanotte.', 'The party will probably finish well after midnight.', {grammarPoint: 'Future tense "finirà".'}],
      ['Andrò in vacanza in Italia la prossima settimana.', 'I will go on vacation to Italy next week.', {grammarPoint: 'Future tense "andrò".'}],
      ['Mi raccomando, cerca di essere puntuale per l\'appuntamento di domani.', 'Please, try to be on time for tomorrow\'s appointment.', {grammarPoint: 'Expression "mi raccomando".'}]
    ]
  },
  {
    id: 110,
    phrases: [
      ['C\'è stato un errore.', 'There was a mistake.'],
      ['Il numero è sbagliato.', 'The number is wrong.'],
      ['Pensavo fosse diverso.', 'I thought it was different.'],
      ['Mi sento un po\' confuso.', 'I feel a bit confused.'],
      ['Posso riprovare?', 'Can I try again?'],
      ['Va tutto bene, tranquillo.', 'Everything is okay, don\'t worry.']
    ],
    sentences: [
      ['Mi dispiace tanto, ho fatto un errore nella prenotazione.', 'I am so sorry, I made a mistake in the reservation.', {grammarPoint: 'Passato prossimo "ho fatto".'}],
      ['Ho preso il treno sbagliato e ora sono in ritardo.', 'I took the wrong train and now I am late.', {grammarPoint: 'Passato prossimo "ho preso".'}],
      ['Pensavo che l\'appuntamento fosse alle due, mi sono confuso.', 'I thought the appointment was at two, I got confused.', {grammarPoint: 'Imperfect subjunctive "fosse" after "pensavo che".'}],
      ['Ti prego di correggere questo piccolo errore sul documento.', 'Please correct this small mistake on the document.', {grammarPoint: 'Verb "pregare di".'}],
      ['Non volevo disturbarti, spero che vada tutto bene.', 'I did not mean to bother you, I hope everything is okay.', {grammarPoint: 'Subjunctive "vada" after "spero che".'}]
    ]
  },
  {
    id: 111,
    phrases: [
      ['Ho un cane.', 'I have a dog.'],
      ['Il gatto dorme.', 'The cat is sleeping.'],
      ['Ecco un cavallo.', 'Here is a horse.'],
      ['Sento un uccello.', 'I hear a bird.'],
      ['Guardo il pesce.', 'I am looking at the fish.'],
      ['C\'è una bella farfalla.', 'There is a beautiful butterfly.']
    ],
    sentences: [
      ['Il mio cane ama correre nel parco ogni mattina.', 'My dog loves to run in the park every morning.', {grammarPoint: 'Possessive adjective "mio" with article.'}],
      ['Abbiamo visto un bellissimo cavallo bianco nella fattoria.', 'We saw a beautiful white horse at the farm.', {grammarPoint: 'Absolute superlative "bellissimo".'}],
      ['Sento sempre un piccolo uccello cantare sul balcone.', 'I always hear a small bird singing on the balcony.', {grammarPoint: 'Infinitive "cantare" after perception verb.'}],
      ['Il coniglio mangia una carota fresca dal giardino.', 'The rabbit eats a fresh carrot from the garden.', {grammarPoint: 'Present tense of -ARE verb (mangiare).'}],
      ['La bambina guarda una grande farfalla colorata sui fiori.', 'The little girl looks at a large colorful butterfly on the flowers.', {grammarPoint: 'Adjective agreement.'}]
    ]
  },
  {
    id: 112,
    phrases: [
      ['Voglio parlare italiano.', 'I want to speak Italian.'],
      ['Devi ascoltare la musica.', 'You must listen to the music.'],
      ['Mi piace visitare i musei.', 'I like to visit museums.'],
      ['Lavoro in banca.', 'I work in a bank.'],
      ['Studio ogni giorno.', 'I study every day.'],
      ['Cerco i miei occhiali.', 'I am looking for my glasses.']
    ],
    sentences: [
      ['Sto provando a parlare italiano con i miei amici.', 'I am trying to speak Italian with my friends.', {grammarPoint: 'Verb "provare a" + infinitive.'}],
      ['Ascoltare la radio aiuta molto a imparare la lingua.', 'Listening to the radio helps a lot to learn the language.', {grammarPoint: 'Infinitive used as subject.'}],
      ['Domani andiamo a visitare il museo d\'arte moderna in centro.', 'Tomorrow we are going to visit the modern art museum downtown.', {grammarPoint: 'Verb "andare a".'}],
      ['Mia sorella lavora in un ristorante e mangia sempre lì.', 'My sister works in a restaurant and always eats there.', {grammarPoint: 'Present tense of -ARE verbs (lavora, mangia).'}],
      ['Stiamo cercando un buon posto per mangiare la pizza stasera.', 'We are looking for a good place to eat pizza tonight.', {grammarPoint: 'Present progressive "stiamo cercando".'}]
    ]
  },
  {
    id: 113,
    phrases: [
      ['Non riesco a vedere.', 'I cannot see.'],
      ['Prendo un caffè.', 'I am taking a coffee.'],
      ['Devo scrivere una email.', 'I must write an email.'],
      ['Mi piace leggere libri.', 'I like to read books.'],
      ['Posso chiedere una cosa?', 'Can I ask something?'],
      ['Voglio conoscere Roma.', 'I want to know Rome.']
    ],
    sentences: [
      ['Preferisco prendere il treno invece di guidare la macchina.', 'I prefer to take the train instead of driving the car.', {grammarPoint: 'Verb "preferire" + infinitive.'}],
      ['La mia amica mi ha chiesto di scrivere una lunga lettera.', 'My friend asked me to write a long letter.', {grammarPoint: 'Verb "chiedere di" + infinitive.'}],
      ['In Italia puoi leggere il giornale bevendo un buon caffè.', 'In Italy you can read the newspaper while drinking a good coffee.', {grammarPoint: 'Gerund "bevendo".'}],
      ['Ho deciso di vivere in questa bellissima città per sempre.', 'I have decided to live in this beautiful city forever.', {grammarPoint: 'Verb "decidere di" + infinitive.'}],
      ['Devi rispondere al telefono quando tua madre ti chiama!', 'You must answer the phone when your mother calls you!', {grammarPoint: 'Verb "rispondere a" (to answer to).'}]
    ]
  },
  {
    id: 114,
    phrases: [
      ['Non riesco a sentire.', 'I cannot hear.'],
      ['Puoi aprire la finestra?', 'Can you open the window?'],
      ['Ho bisogno di dormire.', 'I need to sleep.'],
      ['A che ora devi partire?', 'What time do you have to leave?'],
      ['Ora posso capire.', 'Now I can understand.'],
      ['Devo finire il lavoro.', 'I must finish the work.']
    ],
    sentences: [
      ['Non riesco a sentire bene la tua voce al telefono.', 'I cannot hear your voice well on the phone.', {grammarPoint: 'Verb "riuscire a" + infinitive.'}],
      ['Domani mattina devo partire presto per il mio lungo viaggio.', 'Tomorrow morning I have to leave early for my long trip.', {grammarPoint: 'Present used for future plans.'}],
      ['Con un po\' di pazienza, puoi capire tutto facilmente.', 'With a bit of patience, you can understand everything easily.', {grammarPoint: 'Adverb ending in -mente (facilmente).'}],
      ['Spero di finire di pulire tutta la casa entro stasera.', 'I hope to finish cleaning the whole house by tonight.', {grammarPoint: 'Verb "finire di" + infinitive.'}],
      ['Anche se fa freddo, preferisco uscire e camminare.', 'Even if it is cold, I prefer to go out and walk.', {grammarPoint: 'Conjunction "anche se" (even if).'}]
    ]
  },
  {
    id: 115,
    phrases: [
      ['Mi sveglio presto.', 'I wake up early.'],
      ['Mi alzo dal letto.', 'I get up from bed.'],
      ['Vado a lavarmi.', 'I am going to wash myself.'],
      ['Devo vestirmi per uscire.', 'I must get dressed to go out.'],
      ['Spero di divertirmi.', 'I hope to have fun.'],
      ['Come ti chiami?', 'What is your name?']
    ],
    sentences: [
      ['Di solito mi sveglio alle sette e mi alzo subito.', 'Usually I wake up at seven and get up immediately.', {grammarPoint: 'Reflexive pronouns "mi" in the present tense.'}],
      ['La mattina mi lavo i denti prima di fare colazione.', 'In the morning I brush my teeth before having breakfast.', {grammarPoint: 'Reflexive used for body parts.'}],
      ['Mi vesto elegante perché stasera ho una cena importante.', 'I dress elegantly because tonight I have an important dinner.', {grammarPoint: 'Reflexive verb "vestirsi".'}],
      ['Alla festa di ieri sera ci siamo divertiti davvero molto.', 'At the party last night we really had a lot of fun.', {grammarPoint: 'Passato prossimo of reflexive verbs with "essere".'}],
      ['Non mi sento bene oggi, quindi voglio solo riposarmi.', 'I don\'t feel well today, so I just want to rest.', {grammarPoint: 'Reflexive pronoun attached to infinitive (riposarmi).'}]
    ]
  },
  {
    id: 116,
    phrases: [
      ['È un piatto molto buono.', 'It is a very good dish.'],
      ['Che bel paesaggio!', 'What a beautiful landscape!'],
      ['Ho una casa grande.', 'I have a big house.'],
      ['Il mio cane è piccolo.', 'My dog is small.'],
      ['Ho comprato un telefono nuovo.', 'I bought a new phone.'],
      ['È una lezione facile.', 'It is an easy lesson.']
    ],
    sentences: [
      ['Questo gelato al pistacchio è davvero molto buono e fresco.', 'This pistachio ice cream is really very good and fresh.', {grammarPoint: 'Adjective placement after noun.'}],
      ['Abbiamo visitato un bel castello grande e antico vicino qui.', 'We visited a beautiful big and old castle near here.', {grammarPoint: 'Multiple adjectives.'}],
      ['Mi piace il tuo nuovo vestito rosso, è molto bello.', 'I like your new red dress, it is very beautiful.', {grammarPoint: 'Adjectives preceding and following the noun.'}],
      ['Per me, questo libro è piccolo ma molto difficile da leggere.', 'For me, this book is small but very difficult to read.', {grammarPoint: 'Adjective + "da" + infinitive (difficile da leggere).'}],
      ['Il mio vecchio computer era molto lento e difficile da usare.', 'My old computer was very slow and difficult to use.', {grammarPoint: 'Imperfect tense "era".'}]
    ]
  }
];

const existingScenariosFile = 'src/data/scenarios.ts';
const content = fs.readFileSync(existingScenariosFile, 'utf8');

const blueprintsStartMatch = content.match(/const blueprints: ScenarioBlueprint\[\] = \[/);
if (!blueprintsStartMatch) {
  console.error('Could not find blueprints start');
  process.exit(1);
}

const startIndex = blueprintsStartMatch.index + blueprintsStartMatch[0].length;

// Find the corresponding closing bracket for the array
let depth = 1;
let endIndex = -1;
for (let i = startIndex; i < content.length; i++) {
  if (content[i] === '[') depth++;
  else if (content[i] === ']') depth--;
  
  if (depth === 0) {
    endIndex = i;
    break;
  }
}

if (endIndex === -1) {
  console.error('Could not find blueprints end');
  process.exit(1);
}

const blueprintsRaw = content.substring(startIndex, endIndex);

// We parse using eval because JSON.parse fails on unquoted keys/single quotes
const parsedBlueprints = eval('[' + blueprintsRaw + ']');

const updatedBlueprintsStrings = parsedBlueprints.map((blueprint: any) => {
  const id = blueprint.id;
  const update = allBlueprints.find(b => b.id === id);
  if (!update) {
    console.warn('No update for scenario ID', id);
    return `  {id: ${id}, category: '${blueprint.category}', title: '${blueprint.title.replace(/'/g, "\\'")}', description: '${blueprint.description.replace(/'/g, "\\'")}', ${blueprint.difficulty ? `difficulty: ${blueprint.difficulty}, ` : ''}focus: ${JSON.stringify(blueprint.focus)}}`;
  }
  
  return `  {id: ${id}, category: '${blueprint.category}', title: '${blueprint.title.replace(/'/g, "\\'")}', description: '${blueprint.description.replace(/'/g, "\\'")}', ${blueprint.difficulty ? `difficulty: ${blueprint.difficulty}, ` : ''}focus: ${JSON.stringify(blueprint.focus)}, phrases: ${JSON.stringify(update.phrases)}, sentences: ${JSON.stringify(update.sentences)}}`;
});

const newContent = content.substring(0, startIndex) + '\n' + updatedBlueprintsStrings.join(',\n') + '\n' + content.substring(endIndex);

fs.writeFileSync(existingScenariosFile, newContent);
console.log('Successfully updated scenarios.ts');
