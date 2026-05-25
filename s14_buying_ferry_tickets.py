import json
import os

scenario_id = "s14"
base_path = f"src/data/exports/travel/buying_ferry_tickets/"
os.makedirs(base_path, exist_ok=True)

def generate_vocab():
    data = []
    vocab_list = [
        ("traghetto", "ferry", "Grande nave per passeggeri e auto."),
        ("biglietto", "ticket", "Titolo di viaggio."),
        ("andata", "one way", "Solo per andare."),
        ("ritorno", "return", "Per tornare indietro."),
        ("molo", "pier/dock", "Dove attracca la nave."),
        ("partenza", "departure", "L'orario in cui si parte."),
        ("arrivo", "arrival", "L'orario in cui si arriva."),
        ("botteghino", "ticket office", "Dove si comprano i biglietti."),
        ("imbarcare", "to board/embark", "Salire sulla nave."),
        ("auto", "car", "Veicolo da trasportare."),
        ("modello", "model", "Il tipo di auto."),
        ("lunghezza", "length", "Quanto è lunga l'auto."),
        ("supplemento", "surcharge", "Costo aggiuntivo."),
        ("garage", "garage", "Zona della nave per le auto."),
        ("anticipare", "to move up", "Partire prima del previsto."),
        ("ritardare", "to delay", "Partire dopo il previsto."),
        ("cambio", "change/exchange", "Modifica del biglietto."),
        ("gratuito", "free of charge", "Che non costa nulla."),
        ("disponibilità", "availability", "Posti liberi."),
        ("originale", "original", "Il biglietto iniziale."),
        ("prossimo", "next", "Quello che viene dopo."),
        ("tratta", "route", "Il percorso via mare."),
        ("ponte", "deck", "Piano della nave."),
        ("cabina", "cabin", "Stanza per dormire in nave."),
        ("poltrona", "seat/armchair", "Posto a sedere numerato."),
        ("scalo", "stopover", "Sosta intermedia."),
        ("mare", "sea", "Acqua salata."),
        ("onde", "waves", "Movimento dell'acqua."),
        ("mal di mare", "seasickness", "Sentirsi male in nave."),
        ("giubbotto di salvataggio", "life jacket", "Per la sicurezza."),
        ("scialuppa", "lifeboat", "Piccola barca di emergenza."),
        ("equipaggio", "crew", "Chi lavora sulla nave."),
        ("capitano", "captain", "Chi comanda la nave."),
        ("biglietteria", "ticket counter", "Sinonimo di botteghino."),
        ("prenotazione", "reservation", "Posto assicurato prima."),
        ("imbarco", "boarding", "L'azione di salire."),
        ("ponte auto", "car deck", "Dove si lasciano le macchine."),
        ("portellone", "hatch/gate", "La porta grande della nave."),
        ("ancora", "anchor", "Per fermare la nave."),
        ("porto", "port/harbor", "Dove partono le navi."),
        ("isola", "island", "Terra circondata dal mare."),
        ("costa", "coast", "Terra vicino al mare."),
        ("biglietto elettronico", "e-ticket", "Biglietto sul telefono."),
        ("codice di prenotazione", "booking code", "Numero per il check-in."),
        ("check-in", "check-in", "Accettazione prima dell'imbarco."),
        ("tariffa", "fare", "Il prezzo del viaggio."),
        ("ridotto", "reduced", "Prezzo più basso per bambini o anziani."),
        ("intero", "full price", "Prezzo standard."),
        ("residenti", "residents", "Chi vive sull'isola."),
        ("stagione", "season", "Periodo dell'anno.")
    ]
    
    for i, (ita, eng, desc) in enumerate(vocab_list):
        choices_ita = [ita]
        choices_eng = [eng]
        distractors = [v for v in vocab_list if v[0] != ita]
        import random
        random.seed(i + 600)
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
        ("Vorrei due biglietti per Capri.", "I would like two tickets for Capri.", "Fare una richiesta al botteghino."),
        ("Solo andata o anche ritorno?", "One way or return as well?", "Chiedere il tipo di viaggio."),
        ("Andata e ritorno, per favore.", "Round trip, please.", "Specificare il tipo di viaggio."),
        ("Da quale molo parte?", "From which pier does it depart?", "Chiedere il punto di partenza."),
        ("Il prossimo traghetto.", "The next ferry.", "Specificare l'orario desiderato."),
        ("Tra venti minuti.", "In twenty minutes.", "Indicare il tempo rimanente."),
        ("Quanto costa in totale?", "How much is it in total?", "Chiedere il prezzo complessivo."),
        ("Vorrei imbarcare l'auto.", "I would like to board the car.", "Richiedere il trasporto del veicolo."),
        ("Qual è il modello dell'auto?", "What is the car model?", "Richiesta di informazioni tecniche."),
        ("C'è posto nel garage?", "Is there room in the garage?", "Chiedere disponibilità per l'auto."),
        ("Il supplemento per l'auto.", "The surcharge for the car.", "Specificare un costo extra."),
        ("Vorrei anticipare la partenza.", "I would like to move up the departure.", "Chiedere di partire prima."),
        ("C'è posto alle tredici?", "Is there room at 1 PM?", "Verificare disponibilità oraria."),
        ("C'è un costo aggiuntivo?", "Is there an additional cost?", "Chiedere se si deve pagare di più."),
        ("Il cambio è gratuito.", "The change is free.", "Informare che non ci sono costi di modifica."),
        ("Mi dia il biglietto originale.", "Give me the original ticket.", "Richiesta di documento."),
        ("Ho il mal di mare.", "I have seasickness.", "Segnalare un malessere."),
        ("Dov'è la mia cabina?", "Where is my cabin?", "Cercare il proprio alloggio."),
        ("Posso stare sul ponte?", "Can I stay on the deck?", "Chiedere dove si può sostare."),
        ("L'imbarco è iniziato.", "Boarding has started.", "Avviso di partenza imminente."),
        ("Controlli il biglietto.", "Check the ticket.", "Istruzione per il personale o passeggero."),
        ("Si parte in orario.", "We depart on time.", "Conferma della puntualità."),
        ("C'è un bar a bordo?", "Is there a bar on board?", "Chiedere dei servizi."),
        ("Quanto dura la traversata?", "How long does the crossing take?", "Chiedere la durata del viaggio."),
        ("Sconto per residenti.", "Discount for residents.", "Menzione di una tariffa speciale."),
        ("Biglietto ridotto per bambini.", "Reduced ticket for children.", "Specificare categoria di prezzo."),
        ("Deve fare il check-in.", "You need to check in.", "Istruzione pre-imbarco."),
        ("Mostri il documento d'identità.", "Show your ID.", "Richiesta di riconoscimento."),
        ("Il mare è mosso oggi.", "The sea is rough today.", "Descrizione delle condizioni marine."),
        ("Indossi il giubbotto.", "Wear the jacket.", "Istruzione di sicurezza."),
        ("Siamo quasi arrivati.", "We have almost arrived.", "Avviso di fine viaggio."),
        ("Il porto è molto grande.", "The port is very large.", "Descrizione del luogo."),
        ("Cerco la biglietteria.", "I'm looking for the ticket office.", "Orientamento."),
        ("Ho una prenotazione online.", "I have an online reservation.", "Dichiarare il possesso di un biglietto."),
        ("Stampi il biglietto.", "Print the ticket.", "Azione necessaria."),
        ("Il traghetto è in ritardo.", "The ferry is late.", "Segnalare un disservizio."),
        ("Qual è la tratta?", "What is the route?", "Chiedere il percorso."),
        ("C'è la connessione Wi-Fi?", "Is there Wi-Fi connection?", "Chiedere di internet."),
        ("Dove sono le scialuppe?", "Where are the lifeboats?", "Chiedere della sicurezza."),
        ("Il capitano sta parlando.", "The captain is speaking.", "Attenzione agli annunci."),
        ("Vietato fumare sul ponte.", "No smoking on the deck.", "Regola di bordo."),
        ("Tenere i cani al guinzaglio.", "Keep dogs on a leash.", "Regola per animali."),
        ("Area relax con poltrone.", "Relax area with armchairs.", "Descrizione servizi."),
        ("Uscire dal garage subito.", "Exit the garage immediately.", "Istruzione di sicurezza."),
        ("Chiudere il portellone.", "Close the hatch.", "Azione tecnica."),
        ("Siamo in mezzo al mare.", "We are in the middle of the sea.", "Localizzazione."),
        ("Vedo l'isola laggiù.", "I see the island over there.", "Osservazione."),
        ("Prendiamo un caffè?", "Shall we have a coffee?", "Proposta di svago."),
        ("La traversata è tranquilla.", "The crossing is calm.", "Stato del mare."),
        ("Grazie dell'informazione.", "Thanks for the information.", "Ringraziamento.")
    ]
    
    for i, (ita, eng, desc) in enumerate(phrases_list):
        choices_ita = [ita]
        choices_eng = [eng]
        distractors = [p for p in phrases_list if p[0] != ita]
        import random
        random.seed(i + 700)
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
        ("\"Vorrei due biglietti per il traghetto per Capri.\" \"Solo andata o anche ritorno?\"", "\"I'd like two tickets for the ferry to Capri.\" \"One way or return too?\"", "Acquistare biglietti."),
        ("\"Andata e ritorno, per favore.\" \"Il prossimo parte tra venti minuti.\"", "\"Round trip, please.\" \"The next one leaves in twenty minutes.\"", "Specificare tipo e orario."),
        ("\"Quanto costano i biglietti?\" \"In totale sono quaranta euro.\"", "\"How much are the tickets?\" \"In total they are forty euros.\"", "Chiedere il prezzo."),
        ("\"Da quale molo parte la nave?\" \"Dal molo numero tre, a destra.\"", "\"From which pier does the ship leave?\" \"From pier number three, on the right.\"", "Chiedere il molo."),
        ("\"Vorrei imbarcare anche l'auto per la Sardegna.\" \"Qual è la lunghezza del veicolo?\"", "\"I'd like to board the car for Sardinia too.\" \"What is the length of the vehicle?\"", "Trasporto auto."),
        ("\"È una Fiat 500, è piccola.\" \"Va bene, il supplemento è di sessanta euro.\"", "\"It's a Fiat 500, it's small.\" \"Alright, the surcharge is sixty euros.\"", "Dettagli veicolo e costo."),
        ("\"C'è ancora posto nel garage della nave?\" \"Sì, ma deve sbrigarsi con l'imbarco.\"", "\"Is there still room in the ship's garage?\" \"Yes, but you must hurry with boarding.\"", "Disponibilità garage."),
        ("\"Vorrei anticipare la partenza alle tredici.\" \"Vediamo se c'è disponibilità.\"", "\"I'd like to move up the departure to 1 PM.\" \"Let's see if there is availability.\"", "Cambiare orario."),
        ("\"C'è un costo per cambiare il biglietto?\" \"No, per questa tariffa è gratuito.\"", "\"Is there a cost to change the ticket?\" \"No, for this fare it's free.\"", "Costi di modifica."),
        ("\"Ecco il mio biglietto originale.\" \"Grazie, le stampo subito quello nuovo.\"", "\"Here is my original ticket.\" \"Thank you, I'll print the new one for you right away.\"", "Sostituzione biglietto."),
        ("\"Quanto dura la traversata per l'isola?\" \"Circa un'ora e mezza.\"", "\"How long does the crossing to the island take?\" \"About an hour and a half.\"", "Durata del viaggio."),
        ("\"Soffre di mal di mare?\" \"Sì, a volte, se il mare è molto mosso.\"", "\"Do you suffer from seasickness?\" \"Yes, sometimes, if the sea is very rough.\"", "Conversazione sulla salute."),
        ("\"Dove sono i giubbotti di salvataggio?\" \"Sotto ogni poltrona e in cabina.\"", "\"Where are the life jackets?\" \"Under every seat and in the cabin.\"", "Sicurezza di bordo."),
        ("\"C'è un bar sul ponte superiore?\" \"Sì, serve anche panini e snack.\"", "\"Is there a bar on the upper deck?\" \"Yes, it also serves sandwiches and snacks.\"", "Servizi di ristorazione."),
        ("\"Devo fare il check-in online?\" \"Sì, le invieremo un codice sul telefono.\"", "\"Do I need to check in online?\" \"Yes, we will send you a code on your phone.\"", "Procedure digitali."),
        ("\"A che ora dobbiamo essere al porto?\" \"Almeno un'ora prima della partenza.\"", "\"What time should we be at the port?\" \"At least one hour before departure.\"", "Orari di arrivo."),
        ("\"C'è lo sconto per i residenti siciliani?\" \"Sì, mostri un documento valido.\"", "\"Is there a discount for Sicilian residents?\" \"Yes, show a valid document.\"", "Tariffe speciali."),
        ("\"Possiamo portare il cane sul traghetto?\" \"Sì, ma deve restare sul ponte esterno.\"", "\"Can we bring the dog on the ferry?\" \"Yes, but it must stay on the outer deck.\"", "Animali a bordo."),
        ("\"La nave è molto grande, ha dodici piani.\" \"Speriamo di non perderci!\"", "\"The ship is very large, it has twelve floors.\" \"Let's hope we don't get lost!\"", "Impressioni sulla nave."),
        ("\"Il capitano ha annunciato un breve ritardo.\" \"Peccato, arriveremo tardi a cena.\"", "\"The captain announced a short delay.\" \"Too bad, we'll arrive late for dinner.\"", "Notizie sul viaggio."),
        ("\"C'è una zona per bambini a bordo?\" \"Sì, al piano quattro vicino al cinema.\"", "\"Is there a kids' area on board?\" \"Yes, on floor four near the cinema.\"", "Servizi per famiglie."),
        ("\"Posso fumare in cabina?\" \"Assolutamente no, è vietato ovunque al chiuso.\"", "\"Can I smoke in the cabin?\" \"Absolutely not, it's forbidden everywhere indoors.\"", "Regole di sicurezza."),
        ("\"Il mare sembra molto calmo oggi.\" \"Sì, sarà una traversata piacevole.\"", "\"The sea looks very calm today.\" \"Yes, it will be a pleasant crossing.\"", "Condizioni meteo."),
        ("\"Dobbiamo lasciare l'auto aperta nel garage?\" \"No, la chiuda e inserisca l'allarme.\"", "\"Do we need to leave the car open in the garage?\" \"No, close it and set the alarm.\"", "Istruzioni per l'auto."),
        ("\"Qual è il numero del molo per la Sardegna?\" \"Il molo dieci, in fondo a sinistra.\"", "\"What is the pier number for Sardinia?\" \"Pier ten, at the far left.\"", "Trovare l'imbarco."),
        ("\"C'è la connessione internet in mezzo al mare?\" \"C'è il Wi-Fi a pagamento sul ponte.\"", "\"Is there internet connection in the middle of the sea?\" \"There is paid Wi-Fi on the deck.\"", "Tecnologia."),
        ("\"Mi scusi, dov'è l'uscita per i passeggeri a piedi?\" \"Segua le frecce gialle per il molo.\"", "\"Excuse me, where is the exit for foot passengers?\" \"Follow the yellow arrows to the pier.\"", "Sbarco."),
        ("\"Ho dimenticato la borsa in auto!\" \"Deve chiedere il permesso per scendere in garage.\"", "\"I forgot my bag in the car!\" \"You must ask for permission to go down to the garage.\"", "Dimenticanza."),
        ("\"C'è un ristorante alla carta o solo self-service?\" \"Ci sono entrambi al piano sei.\"", "\"Is there an a la carte restaurant or only self-service?\" \"There are both on floor six.\"", "Opzioni per mangiare."),
        ("\"Siamo arrivati in porto?\" \"Sì, stiamo attraccando proprio ora.\"", "\"Have we arrived at the port?\" \"Yes, we are docking right now.\"", "Arrivo."),
        ("\"Buongiorno, biglietti per l'Elba per favore.\" \"Auto o solo passeggeri?\"", "\"Good morning, tickets for Elba please.\" \"Car or passengers only?\"", "Acquisto rapido."),
        ("\"Quanto costa il supplemento per la cabina?\" \"Trenta euro per una doppia.\"", "\"How much is the surcharge for the cabin?\" \"Thirty euros for a double.\"", "Upgrade viaggio."),
        ("\"Il traghetto delle dieci è già partito?\" \"Sì, è partito con cinque minuti di anticipo.\"", "\"Has the 10 AM ferry already left?\" \"Yes, it left five minutes early.\"", "Informazione orari."),
        ("\"È possibile rimborsare il biglietto?\" \"Solo se ha l'assicurazione annullamento.\"", "\"Is it possible to refund the ticket?\" \"Only if you have cancellation insurance.\"", "Politiche di rimborso."),
        ("\"Dove posso caricare il telefono?\" \"Ci sono delle prese vicino alle poltrone.\"", "\"Where can I charge my phone?\" \"There are sockets near the armchairs.\"", "Energia."),
        ("\"C'è molta aria sul ponte, fa freddo.\" \"Entriamo nel salone principale.\"", "\"There's a lot of wind on the deck, it's cold.\" \"Let's go into the main lounge.\"", "Meteo di bordo."),
        ("\"Guardate, ci sono i delfini!\" \"Dove? Ah sì, li vedo a destra della nave.\"", "\"Look, there are dolphins!\" \"Where? Ah yes, I see them to the right of the ship.\"", "Avvistamenti."),
        ("\"Il portellone del garage si sta aprendo.\" \"Torniamo in macchina per sbarcare.\"", "\"The garage hatch is opening.\" \"Let's get back in the car to disembark.\"", "Fase di sbarco."),
        ("\"Siamo in ritardo per la coincidenza?\" \"No, la nave recupererà tempo in mare.\"", "\"Are we late for the connection?\" \"No, the ship will make up time at sea.\"", "Preoccupazione ritardi."),
        ("\"Posso pagare con la carta di debito?\" \"Sì, accettiamo tutti i circuiti principali.\"", "\"Can I pay with a debit card?\" \"Yes, we accept all major circuits.\"", "Pagamento."),
        ("\"C'è l'aria condizionata troppo forte qui.\" \"Spostiamoci in una zona più calda.\"", "\"The air conditioning is too strong here.\" \"Let's move to a warmer area.\"", "Comfort."),
        ("\"Il biglietto vale anche per il bus sull'isola?\" \"No, deve comprarlo a bordo del bus.\"", "\"Is the ticket valid for the bus on the island too?\" \"No, you must buy it on the bus.\"", "Integrazione trasporti."),
        ("\"Quanti passeggeri può portare questa nave?\" \"Fino a duemila persone.\"", "\"How many passengers can this ship carry?\" \"Up to two thousand people.\"", "Curiosità."),
        ("\"Dobbiamo consegnare le chiavi della cabina?\" \"Sì, alla reception prima di scendere.\"", "\"Do we need to hand in the cabin keys?\" \"Yes, at the reception before going down.\"", "Fine soggiorno."),
        ("\"Il panorama della costa è bellissimo.\" \"Sì, facciamo una foto insieme.\"", "\"The view of the coast is beautiful.\" \"Yes, let's take a photo together.\"", "Turismo."),
        ("\"C'è un medico a bordo in caso di emergenza?\" \"Sì, c'è un'infermeria al piano tre.\"", "\"Is there a doctor on board in case of emergency?\" \"Yes, there is an infirmary on floor three.\"", "Salute."),
        ("\"Quanto dista il porto dal centro città?\" \"Circa un chilometro, c'è un bus navetta.\"", "\"How far is the port from the city center?\" \"About one kilometer, there is a shuttle bus.\"", "Logistica."),
        ("\"Abbiamo preso il traghetto sbagliato!\" \"No, guardi, il nome sulla fiancata è corretto.\"", "\"We took the wrong ferry!\" \"No, look, the name on the side is correct.\"", "Paura di sbagliare."),
        ("\"Si può scendere in garage durante la navigazione?\" \"No, è vietato per motivi di sicurezza.\"", "\"Can one go down to the garage during navigation?\" \"No, it's forbidden for security reasons.\"", "Regole strette."),
        ("\"Grazie mille per l'aiuto con i bagagli.\" \"Prego, è un piacere.\"", "\"Thank you very much for the help with the luggage.\" \"You're welcome, it's a pleasure.\"", "Cortesia personale."),
        ("\"Il bar chiude trenta minuti prima dell'arrivo.\" \"Allora prendiamo l'ultimo caffè subito.\"", "\"The bar closes thirty minutes before arrival.\" \"Then let's have the last coffee now.\"", "Orari servizi."),
        ("\"C'è un'area fumatori esterna?\" \"Sì, a poppa sul ponte sei.\"", "\"Is there an outdoor smoking area?\" \"Yes, at the stern on deck six.\"", "Servizi fumatori."),
        ("\"Le scialuppe sono state controllate ieri.\" \"Bene, mi sento più sicuro.\"", "\"The lifeboats were checked yesterday.\" \"Good, I feel safer.\"", "Sicurezza."),
        ("\"Quanto costa un biglietto per l'auto lunga?\" \"Dipende, se supera i cinque metri costa di più.\"", "\"How much is a ticket for a long car?\" \"It depends, if it exceeds five meters it costs more.\"", "Tariffe veicoli."),
        ("\"Siamo pronti per la manovra di attracco?\" \"Sì, tutti i passeggeri devono lasciare i ponti esterni.\"", "\"Are we ready for the docking maneuver?\" \"Yes, all passengers must leave the outer decks.\"", "Fine viaggio."),
        ("\"Posso avere una coperta per la notte?\" \"Sì, la chieda al personale in cabina.\"", "\"Can I have a blanket for the night?\" \"Yes, ask the cabin staff for it.\"", "Richiesta comfort."),
        ("\"Il biglietto è andata e ritorno per lo stesso giorno?\" \"Sì, è un'offerta giornaliera.\"", "\"Is the ticket round trip for the same day?\" \"Yes, it's a daily offer.\"", "Dettagli offerta."),
        ("\"La nave oscilla un po'.\" \"Non si preoccupi, è normale con questo vento.\"", "\"The ship is swaying a bit.\" \"Don't worry, it's normal with this wind.\"", "Rassicurazione."),
        ("\"Dov'è il bagno più vicino?\" \"In fondo al corridoio, dopo il bar.\"", "\"Where is the nearest bathroom?\" \"At the end of the hallway, after the bar.\"", "Necessità."),
        ("\"Speriamo di vedere il tramonto dal mare.\" \"Sì, sarà uno spettacolo fantastico.\"", "\"Let's hope to see the sunset from the sea.\" \"Yes, it will be a fantastic sight.\"", "Desiderio.")
    ]
    
    for i, (ita, eng, desc) in enumerate(sentences_list):
        choices_ita = [ita]
        choices_eng = [eng]
        distractors = [s for s in sentences_list if s[0] != ita]
        import random
        random.seed(i + 800)
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

with open(os.path.join(base_path, "travel_buying_ferry_tickets_vocabulary.json"), "w", encoding="utf-8") as f:
    json.dump(generate_vocab(), f, ensure_ascii=False, indent=2)

with open(os.path.join(base_path, "travel_buying_ferry_tickets_phrases.json"), "w", encoding="utf-8") as f:
    json.dump(generate_phrases(), f, ensure_ascii=False, indent=2)

with open(os.path.join(base_path, "travel_buying_ferry_tickets_sentences.json"), "w", encoding="utf-8") as f:
    json.dump(generate_sentences(), f, ensure_ascii=False, indent=2)
