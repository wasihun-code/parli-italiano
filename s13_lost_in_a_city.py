import json
import os

scenario_id = "s13"
base_path = f"src/data/exports/travel/lost_in_a_city/"
os.makedirs(base_path, exist_ok=True)

def generate_vocab():
    data = []
    vocab_list = [
        ("perso", "lost", "Quando non sai dove sei."),
        ("mappa", "map", "Rappresentazione del territorio."),
        ("incrocio", "intersection", "Dove due strade si incontrano."),
        ("direzione", "direction", "Verso dove vai."),
        ("sbagliata", "wrong", "Non quella giusta."),
        ("indietro", "back", "Verso il punto di partenza."),
        ("vicino", "near", "A poca distanza."),
        ("lontano", "far", "A grande distanza."),
        ("angolo", "corner", "Punto di svolta."),
        ("strada", "street/road", "Via di comunicazione."),
        ("piazza", "square", "Spazio aperto in città."),
        ("fontana", "fountain", "Struttura che eroga acqua."),
        ("hotel", "hotel", "Posto dove dormire."),
        ("insegna", "sign", "Cartello luminoso o scritto."),
        ("navigatore", "navigator/GPS", "App per trovare la strada."),
        ("scarico", "dead/uncharged", "Senza batteria."),
        ("telefono", "phone", "Dispositivo per comunicare."),
        ("indicazioni", "directions", "Informazioni sulla via."),
        ("pazienza", "patience", "Capacità di aspettare o aiutare."),
        ("angolo", "corner", "Punto d'incontro tra vie."),
        ("passi", "steps", "Piccola distanza a piedi."),
        ("chiaro", "clear", "Comprensibile."),
        ("destra", "right", "Lato opposto al sinistro."),
        ("sinistra", "left", "Lato opposto al destro."),
        ("diritto", "straight", "Senza girare."),
        ("centro", "center", "Parte principale della città."),
        ("quartiere", "neighborhood", "Zona della città."),
        ("monumento", "monument", "Opera storica o artistica."),
        ("chiesa", "church", "Edificio religioso."),
        ("museo", "museum", "Posto dove ci sono opere d'arte."),
        ("ponte", "bridge", "Struttura sopra l'acqua."),
        ("fiume", "river", "Corso d'acqua dolce."),
        ("fermata", "stop", "Dove si prende il bus o metro."),
        ("stazione", "station", "Dove arrivano i treni."),
        ("turista", "tourist", "Chi viaggia per piacere."),
        ("passante", "passerby", "Persona che cammina per strada."),
        ("aiuto", "help", "Assistenza a qualcuno."),
        ("mostrare", "to show", "Far vedere qualcosa."),
        ("trovare", "to find", "Riuscire a vedere."),
        ("cercare", "to look for", "Tantare di trovare."),
        ("girare", "to turn", "Cambiare direzione."),
        ("seguire", "to follow", "Andare dietro o lungo."),
        ("tornare", "to return", "Andare di nuovo in un posto."),
        ("arrivare", "to arrive", "Raggiungere la meta."),
        ("chiedere", "to ask", "Domandare aiuto."),
        ("scorrere", "to scroll", "Muoversi sulla mappa digitale."),
        ("ingrandire", "to zoom in", "Vedere più da vicino."),
        ("segnale", "signal", "Connessione internet."),
        ("via", "street", "Nome della strada."),
        ("corso", "main street", "Viale principale.")
    ]
    
    for i, (ita, eng, desc) in enumerate(vocab_list):
        choices_ita = [ita]
        choices_eng = [eng]
        distractors = [v for v in vocab_list if v[0] != ita]
        import random
        random.seed(i + 300)
        sample = random.sample(distractors, 3)
        for d in sample:
            choices_ita.append(d[0])
            choices_eng.append(d[1])
        
        combined = list(zip(choices_ita, choices_eng))
        random.shuffle(combined)
        choices_ita, choices_eng = zip(*combined)
        
        data.append({
            "id": f"{scenario_id}-v{i+1}",
            "italian": ita,
            "english": eng,
            "type": "vocabulary",
            "choicesItalian": list(choices_ita),
            "choicesEnglish": list(choices_eng),
            "correctAnswerItalian": ita,
            "correctAnswerEnglish": eng,
            "feedback": {
                "correctItalian": f"Esatto! {desc}",
                "incorrectItalian": f"No, '{ita}' è {desc.lower()}",
                "correctEnglish": f"Correct! {eng} refers to {ita}.",
                "incorrectEnglish": f"No, the correct word is {eng}."
            }
        })
    return data

def generate_phrases():
    data = []
    phrases_list = [
        ("Mi sono perso.", "I am lost.", "Dichiarare di aver perso la strada."),
        ("Cerco Piazza Navona.", "I am looking for Piazza Navona.", "Specificare la meta."),
        ("Può aiutarmi?", "Can you help me?", "Chiedere assistenza."),
        ("Dove ci troviamo?", "Where are we?", "Chiedere la posizione attuale."),
        ("È lontano da qui?", "Is it far from here?", "Chiedere la distanza."),
        ("Tornare indietro.", "To go back.", "Muoversi verso il punto precedente."),
        ("Girare a destra.", "To turn right.", "Cambiare direzione a destra."),
        ("Girare a sinistra.", "To turn left.", "Cambiare direzione a sinistra."),
        ("Andare diritto.", "To go straight.", "Continuare senza girare."),
        ("Fino all'incrocio.", "Up to the intersection.", "Indicare un punto di riferimento."),
        ("Direzione sbagliata.", "Wrong direction.", "Quando non si va verso la meta."),
        ("Segua le indicazioni.", "Follow the signs.", "Consiglio per trovare la via."),
        ("Mostrare sulla mappa.", "To show on the map.", "Richiesta di aiuto visivo."),
        ("Proprio dietro l'angolo.", "Just around the corner.", "Indica vicinanza estrema."),
        ("A pochi passi.", "A few steps away.", "Molto vicino."),
        ("Il telefono è scarico.", "The phone is dead.", "Segnalare un problema tecnico."),
        ("In fondo alla strada.", "At the end of the street.", "Indicare la fine della via."),
        ("Sulla sinistra.", "On the left.", "Posizione a sinistra."),
        ("Sulla destra.", "On the right.", "Posizione a destra."),
        ("Insegna luminosa.", "Neon sign.", "Punto di riferimento visivo."),
        ("Grazie infinite.", "Thank you so much.", "Ringraziamento sentito."),
        ("Mi sono smarrito.", "I got lost.", "Sinonimo di 'mi sono perso'."),
        ("Qual è la via per il centro?", "Which is the way to the center?", "Chiedere indicazioni per il centro."),
        ("Sono un turista.", "I am a tourist.", "Presentarsi."),
        ("Non capisco dove sono.", "I don't understand where I am.", "Esprimere confusione."),
        ("C'è una fermata della metro?", "Is there a metro stop?", "Cercare trasporti."),
        ("Dov'è il monumento?", "Where is the monument?", "Cercare un sito storico."),
        ("Mi può indicare la via?", "Can you point me the way?", "Richiesta di direzione."),
        ("Siamo molto lontani?", "Are we very far?", "Preoccupazione sulla distanza."),
        ("Devo prendere un bus?", "Do I need to take a bus?", "Chiedere se serve un mezzo."),
        ("Cerco l'hotel Astoria.", "I'm looking for the Astoria hotel.", "Esempio specifico di meta."),
        ("Cinquecento metri.", "Five hundred meters.", "Misura di distanza."),
        ("Gira l'angolo.", "Turn the corner.", "Istruzione semplice."),
        ("Segua via del Corso.", "Follow via del Corso.", "Istruzione specifica."),
        ("Piazza Navona è vicina.", "Piazza Navona is nearby.", "Rassicurazione."),
        ("Siamo in via del Tritone.", "We are in via del Tritone.", "Localizzazione."),
        ("Troverà la piazza.", "You will find the square.", "Promessa di successo."),
        ("Grazie per la pazienza.", "Thanks for your patience.", "Cortesia."),
        ("Non ho più internet.", "I don't have internet anymore.", "Problema di connessione."),
        ("Il navigatore non funziona.", "The navigator isn't working.", "Problema app."),
        ("Ho bisogno di una mappa cartacea.", "I need a paper map.", "Richiesta oggetto fisico."),
        ("Dov'è l'ufficio turistico?", "Where is the tourist office?", "Cercare informazioni ufficiali."),
        ("Mi scusi, un'informazione.", "Excuse me, a piece of information.", "Approcciare un passante."),
        ("Vada sempre dritto.", "Go straight ahead.", "Istruzione comune."),
        ("Oltrepassi il ponte.", "Cross the bridge.", "Passare sopra un ponte."),
        ("La chiesa è di fronte.", "The church is opposite.", "Posizione frontale."),
        ("A metà strada.", "Halfway.", "Posizione intermedia."),
        ("Non si può sbagliare.", "You can't miss it.", "Rassicurazione che è facile."),
        ("È un quartiere antico.", "It's an old neighborhood.", "Descrizione zona."),
        ("Siamo proprio qui.", "We are right here.", "Punto esatto sulla mappa.")
    ]
    
    for i, (ita, eng, desc) in enumerate(phrases_list):
        choices_ita = [ita]
        choices_eng = [eng]
        distractors = [p for p in phrases_list if p[0] != ita]
        import random
        random.seed(i + 400)
        sample = random.sample(distractors, 3)
        for d in sample:
            choices_ita.append(d[0])
            choices_eng.append(d[1])
        
        combined = list(zip(choices_ita, choices_eng))
        random.shuffle(combined)
        choices_ita, choices_eng = zip(*combined)
        
        data.append({
            "id": f"{scenario_id}-p{i+1}",
            "italian": ita,
            "english": eng,
            "type": "phrase",
            "choicesItalian": list(choices_ita),
            "choicesEnglish": list(choices_eng),
            "correctAnswerItalian": ita,
            "correctAnswerEnglish": eng,
            "feedback": {
                "correctItalian": f"Ottimo! {desc}",
                "incorrectItalian": f"No, questa frase significa: {eng}",
                "correctEnglish": f"Great! '{ita}' means '{eng}'.",
                "incorrectEnglish": f"No, the correct translation is '{eng}'."
            }
        })
    return data

def generate_sentences():
    data = []
    sentences_list = [
        ("\"Mi scusi, mi sono perso.\" \"Non si preoccupi, dove deve andare?\"", "\"Excuse me, I'm lost.\" \"Don't worry, where do you need to go?\"", "Inizio di una richiesta di aiuto."),
        ("\"Sto cercando Piazza Navona.\" \"Deve tornare indietro fino all'incrocio.\"", "\"I'm looking for Piazza Navona.\" \"You must go back to the intersection.\"", "Indicazioni per una piazza famosa."),
        ("\"Stavo andando nella direzione sbagliata?\" \"Sì, deve girare a destra.\"", "\"Was I going in the wrong direction?\" \"Yes, you must turn right.\"", "Conferma di un errore di percorso."),
        ("\"Può mostrarmi sulla mappa dove siamo?\" \"Siamo all'angolo di questa via.\"", "\"Can you show me on the map where we are?\" \"We are at the corner of this street.\"", "Uso della mappa."),
        ("\"La Fontana di Trevi è lontana?\" \"No, è a pochi passi da qui.\"", "\"Is the Trevi Fountain far?\" \"No, it's a few steps from here.\"", "Chiedere la distanza per un monumento."),
        ("\"Il mio telefono è scarico, cerco un hotel.\" \"Quale hotel sta cercando?\"", "\"My phone is dead, I'm looking for a hotel.\" \"Which hotel are you looking for?\"", "Problema tecnico e meta."),
        ("\"L'hotel Astoria è in fondo a questa strada?\" \"Sì, circa cinquecento metri sulla sinistra.\"", "\"Is the Astoria hotel at the end of this street?\" \"Yes, about five hundred meters on the left.\"", "Specificare la posizione dell'hotel."),
        ("\"Vede quell'insegna luminosa?\" \"Sì, la vedo, grazie infinite!\"", "\"Do you see that bright sign?\" \"Yes, I see it, thank you so much!\"", "Identificare un punto di riferimento."),
        ("\"Scusi, cerco la fermata della metro.\" \"Vada dritto per duecento metri.\"", "\"Excuse me, I'm looking for the metro stop.\" \"Go straight for two hundred meters.\"", "Cercare il trasporto pubblico."),
        ("\"È meglio andare a piedi o in bus?\" \"A piedi è più veloce, è vicino.\"", "\"Is it better to go on foot or by bus?\" \"On foot is faster, it's nearby.\"", "Confrontare opzioni di movimento."),
        ("\"Mi sono smarrito in questo quartiere.\" \"Non si agiti, il centro è da quella parte.\"", "\"I got lost in this neighborhood.\" \"Don't panic, the center is that way.\"", "Rassicurazione."),
        ("\"C'è un ufficio turistico qui vicino?\" \"Sì, in Piazza del Popolo.\"", "\"Is there a tourist office nearby?\" \"Yes, in Piazza del Popolo.\"", "Cercare informazioni ufficiali."),
        ("\"Posso usare il suo navigatore?\" \"Certo, guardi pure il mio schermo.\"", "\"Can I use your navigator?\" \"Of course, feel free to look at my screen.\"", "Gentilezza di un passante."),
        ("\"Sulla mappa vedo un ponte, è quello?\" \"Sì, quello è Ponte Sisto.\"", "\"On the map I see a bridge, is that it?\" \"Yes, that is Ponte Sisto.\"", "Verifica sulla mappa."),
        ("\"Mi sono perso cercando il museo.\" \"Giri a sinistra dopo la chiesa.\"", "\"I got lost looking for the museum.\" \"Turn left after the church.\"", "Indicazioni con punti di riferimento."),
        ("\"Questa è via del Corso?\" \"No, questa è via Ripetta.\"", "\"Is this via del Corso?\" \"No, this is via Ripetta.\"", "Chiedere conferma del nome della via."),
        ("\"Il segnale GPS non funziona bene.\" \"Succede tra questi palazzi alti.\"", "\"The GPS signal isn't working well.\" \"It happens between these tall buildings.\"", "Problemi di tecnologia in città."),
        ("\"Quanto dista il fiume?\" \"È proprio in fondo alla via.\"", "\"How far is the river?\" \"It's right at the end of the street.\"", "Distanza da un punto naturale."),
        ("\"C'è un punto di riferimento famoso?\" \"Sì, il Pantheon è dietro l'angolo.\"", "\"Is there a famous landmark?\" \"Yes, the Pantheon is around the corner.\"", "Cercare monumenti."),
        ("\"Siamo nella direzione giusta per il Colosseo?\" \"No, state andando verso il Vaticano.\"", "\"Are we in the right direction for the Colosseum?\" \"No, you are going towards the Vatican.\"", "Correzione di rotta."),
        ("\"Mi scusi, per andare alla stazione?\" \"Prenda il bus numero sessantaquattro.\"", "\"Excuse me, to go to the station?\" \"Take bus number sixty-four.\"", "Chiedere il bus per la stazione."),
        ("\"C'è una mappa in questa piazza?\" \"Sì, sul cartello marrone laggiù.\"", "\"Is there a map in this square?\" \"Yes, on the brown sign over there.\"", "Cercare mappe pubbliche."),
        ("\"Siamo molto lontani dal nostro hotel?\" \"No, mancano solo dieci minuti a piedi.\"", "\"Are we very far from our hotel?\" \"No, it's only ten minutes away on foot.\"", "Rassicurazione sulla distanza."),
        ("\"Giri a destra al semaforo.\" \"Va bene, grazie per l'aiuto!\"", "\"Turn right at the traffic light.\" \"Okay, thanks for the help!\"", "Seguire istruzioni semplici."),
        ("\"Mi sono perso, non trovo più la macchina.\" \"Dove l'aveva parcheggiata?\"", "\"I'm lost, I can't find the car anymore.\" \"Where had you parked it?\"", "Perdere l'auto."),
        ("\"Il mio amico ha la mappa, ma si è allontanato.\" \"Proviamo a chiamarlo.\"", "\"My friend has the map, but he walked away.\" \"Let's try to call him.\"", "Amico smarrito."),
        ("\"Scusi, questa strada porta al porto?\" \"No, questa va verso la montagna.\"", "\"Excuse me, does this road lead to the port?\" \"No, this one goes towards the mountain.\"", "Chiedere la meta della strada."),
        ("\"Cercate il centro storico?\" \"Sì, ci siamo persi nei vicoli.\"", "\"Are you looking for the historic center?\" \"Yes, we got lost in the alleys.\"", "Persi nei vicoli."),
        ("\"Vada sempre dritto finché non vede il mare.\" \"Grazie, ora è tutto chiaro.\"", "\"Go straight until you see the sea.\" \"Thanks, everything is clear now.\"", "Indicazioni semplici."),
        ("\"Mi scusi, un passante mi ha detto di girare qui.\" \"Ha ragione, il museo è lì.\"", "\"Excuse me, a passerby told me to turn here.\" \"He's right, the museum is there.\"", "Conferma di indicazioni precedenti."),
        ("\"Sulla mappa questo è un parco?\" \"Sì, è Villa Borghese.\"", "\"On the map is this a park?\" \"Yes, it's Villa Borghese.\"", "Identificare zone verdi."),
        ("\"Il navigatore dice di girare, ma c'è un muro.\" \"Forse la mappa non è aggiornata.\"", "\"The navigator says to turn, but there's a wall.\" \"Maybe the map is not updated.\"", "Errori del navigatore."),
        ("\"Mi sono perso, cerco un taxi.\" \"C'è un posteggio taxi in quella piazza.\"", "\"I'm lost, I'm looking for a taxi.\" \"There's a taxi stand in that square.\"", "Cercare un taxi."),
        ("\"Può scrivermi l'indirizzo sulla mappa?\" \"Certo, ecco qui il punto esatto.\"", "\"Can you write the address on the map for me?\" \"Sure, here is the exact point.\"", "Aiuto scritto."),
        ("\"Siamo vicini alla fontana?\" \"Sì, senta il rumore dell'acqua.\"", "\"Are we near the fountain?\" \"Yes, listen to the sound of the water.\"", "Usare i sensi per orientarsi."),
        ("\"Ho perso la bussola, non capisco il Nord.\" \"Guardi dove tramonta il sole.\"", "\"I lost my bearings, I don't understand North.\" \"Look where the sun sets.\"", "Orientamento naturale."),
        ("\"Questo incrocio è molto confusionario.\" \"Segua la folla verso la piazza.\"", "\"This intersection is very confusing.\" \"Follow the crowd towards the square.\"", "Gestire il caos."),
        ("\"Mi scusi, cerco via Veneto.\" \"È la terza traversa a sinistra.\"", "\"Excuse me, I'm looking for via Veneto.\" \"It's the third side street on the left.\"", "Contare le traverse."),
        ("\"Siamo finiti in una zona residenziale.\" \"Dobbiamo tornare sulla strada principale.\"", "\"We ended up in a residential area.\" \"We need to get back on the main road.\"", "Sbagliare zona."),
        ("\"C'è un bar dove posso caricare il telefono?\" \"Sì, provi quello all'angolo.\"", "\"Is there a bar where I can charge my phone?\" \"Yes, try the one on the corner.\"", "Cercare ricarica."),
        ("\"Cerco il consolato, mi sono perso.\" \"È in quella villa dietro gli alberi.\"", "\"I'm looking for the consulate, I'm lost.\" \"It's in that villa behind the trees.\"", "Cercare edifici istituzionali."),
        ("\"Quanto tempo ci vuole per arrivare al porto?\" \"Circa venti minuti a piedi.\"", "\"How long does it take to get to the port?\" \"About twenty minutes on foot.\"", "Tempo di percorrenza."),
        ("\"La mappa digitale non carica.\" \"Usi quella cartacea del ristorante.\"", "\"The digital map isn't loading.\" \"Use the paper one from the restaurant.\"", "Alternativa alla tecnologia."),
        ("\"Siamo nella piazza giusta?\" \"Sì, questa è Piazza del Campo.\"", "\"Are we in the right square?\" \"Yes, this is Piazza del Campo.\"", "Verifica della posizione."),
        ("\"Cercate la torre?\" \"Sì, dove l'hanno nascosta?\"", "\"Are you looking for the tower?\" \"Yes, where did they hide it?\"", "Ironia tra turisti."),
        ("\"Mi scusi, sono straniero e mi sono perso.\" \"Non si preoccupi, l'aiuto io.\"", "\"Excuse me, I'm a foreigner and I'm lost.\" \"Don't worry, I'll help you.\"", "Gentilezza locale."),
        ("\"È questa la via per il mercato?\" \"Sì, è proprio questa qui.\"", "\"Is this the way to the market?\" \"Yes, it's this one right here.\"", "Conferma del percorso."),
        ("\"Dobbiamo attraversare la strada?\" \"Sì, sulle strisce pedonali laggiù.\"", "\"Do we need to cross the street?\" \"Yes, on the crosswalk over there.\"", "Istruzioni di sicurezza."),
        ("\"Mi sono perso, cerco la spiaggia.\" \"Segua il profumo del mare.\"", "\"I'm lost, I'm looking for the beach.\" \"Follow the scent of the sea.\"", "Orientamento sensoriale."),
        ("\"Questa mappa è troppo piccola.\" \"Ne compriamo una più grande in edicola.\"", "\"This map is too small.\" \"Let's buy a larger one at the newsstand.\"", "Problemi di scala."),
        ("\"Dov'è il castello?\" \"Guardi in alto, sulla collina.\"", "\"Where is the castle?\" \"Look up, on the hill.\"", "Punto di riferimento elevato."),
        ("\"Siamo tornati al punto di partenza!\" \"Abbiamo fatto un giro a vuoto.\"", "\"We are back at the starting point!\" \"We went in a circle.\"", "Errore di orientamento."),
        ("\"Il navigatore dice che siamo arrivati.\" \"Ma qui non c'è nulla!\"", "\"The navigator says we have arrived.\" \"But there's nothing here!\"", "Incongruenza del GPS."),
        ("\"Chiediamo a quel poliziotto?\" \"Sì, è l'idea migliore.\"", "\"Shall we ask that policeman?\" \"Yes, it's the best idea.\"", "Cercare autorità."),
        ("\"Siamo sulla riva destra o sinistra?\" \"Siamo sulla riva sinistra del Tevere.\"", "\"Are we on the right or left bank?\" \"We are on the left bank of the Tiber.\"", "Orientamento fluviale."),
        ("\"Cercate il teatro?\" \"Sì, abbiamo uno spettacolo tra poco.\"", "\"Are you looking for the theater?\" \"Yes, we have a show soon.\"", "Urgenza di trovare la via."),
        ("\"Mi sono perso, non ricordo il nome dell'hotel.\" \"Ha una ricevuta o un'email?\"", "\"I'm lost, I don't remember the hotel name.\" \"Do you have a receipt or an email?\"", "Dimenticanza."),
        ("\"Vada oltre quel grande arco.\" \"D'accordo, grazie mille.\"", "\"Go beyond that large arch.\" \"Alright, thank you very much.\"", "Seguire indicazioni architettoniche."),
        ("\"Siamo in una zona a traffico limitato?\" \"Sì, solo per i residenti.\"", "\"Are we in a limited traffic zone?\" \"Yes, for residents only.\"", "Regole della città."),
        ("\"Grazie della pazienza, siamo un po' confusi.\" \"È normale, la città è un labirinto!\"", "\"Thanks for your patience, we're a bit confused.\" \"It's normal, the city is a labyrinth!\"", "Comprensione finale.")
    ]
    
    for i, (ita, eng, desc) in enumerate(sentences_list):
        choices_ita = [ita]
        choices_eng = [eng]
        distractors = [s for s in sentences_list if s[0] != ita]
        import random
        random.seed(i + 500)
        sample = random.sample(distractors, 3)
        for d in sample:
            choices_ita.append(d[0])
            choices_eng.append(d[1])
        
        combined = list(zip(choices_ita, choices_eng))
        random.shuffle(combined)
        choices_ita, choices_eng = zip(*combined)
        
        data.append({
            "id": f"{scenario_id}-s{i+1}",
            "italian": ita,
            "english": eng,
            "type": "sentence",
            "choicesItalian": list(choices_ita),
            "choicesEnglish": list(choices_eng),
            "correctAnswerItalian": ita,
            "correctAnswerEnglish": eng,
            "feedback": {
                "correctItalian": f"Ottimo! {desc}",
                "incorrectItalian": f"No, questo dialogo significa: {eng}",
                "correctEnglish": f"Great! This means: {eng}",
                "incorrectEnglish": f"No, the correct dialogue is: {eng}"
            }
        })
    return data

with open(os.path.join(base_path, "travel_lost_in_a_city_vocabulary.json"), "w", encoding="utf-8") as f:
    json.dump(generate_vocab(), f, ensure_ascii=False, indent=2)

with open(os.path.join(base_path, "travel_lost_in_a_city_phrases.json"), "w", encoding="utf-8") as f:
    json.dump(generate_phrases(), f, ensure_ascii=False, indent=2)

with open(os.path.join(base_path, "travel_lost_in_a_city_sentences.json"), "w", encoding="utf-8") as f:
    json.dump(generate_sentences(), f, ensure_ascii=False, indent=2)
