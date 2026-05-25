import json
import os

scenario_id = "s12"
base_path = f"src/data/exports/travel/parking/"
os.makedirs(base_path, exist_ok=True)

def generate_vocab():
    data = []
    vocab_list = [
        ("parcheggio", "parking", "Dove lasci la macchina."),
        ("auto", "car", "Il mezzo di trasporto."),
        ("macchina", "car", "Sinonimo di auto."),
        ("ticket", "ticket", "Il biglietto del parcheggio."),
        ("biglietto", "ticket", "Sinonimo di ticket."),
        ("cassa", "pay station", "Dove si paga."),
        ("monete", "coins", "Soldi in metallo."),
        ("carta di credito", "credit card", "Metodo di pagamento elettronico."),
        ("ora", "hour", "Unità di tempo."),
        ("tariffa", "rate", "Il prezzo del servizio."),
        ("giornaliero", "daily", "Per tutto il giorno."),
        ("uscita", "exit", "Da dove si esce."),
        ("entrata", "entrance", "Da dove si entra."),
        ("divieto", "prohibition", "Cosa non si può fare."),
        ("sosta", "parking/stop", "Fermata prolungata."),
        ("marciapiede", "sidewalk", "Dove camminano i pedoni."),
        ("vigile", "traffic officer", "Chi controlla il traffico."),
        ("multa", "fine", "La sanzione da pagare."),
        ("rimozione", "towing", "Portare via l'auto."),
        ("garage", "garage", "Parcheggio al coperto."),
        ("sotterraneo", "underground", "Sotto il livello del suolo."),
        ("custodito", "guarded", "Sorvegliato da qualcuno."),
        ("libero", "free/vacant", "Posto non occupato."),
        ("occupato", "occupied", "Posto non disponibile."),
        ("strisce blu", "blue lines", "Parcheggio a pagamento."),
        ("strisce bianche", "white lines", "Parcheggio gratuito."),
        ("disco orario", "parking disk", "Per indicare l'ora di arrivo."),
        ("parchimetro", "parking meter", "La macchinetta in strada."),
        ("sbarra", "barrier", "L'asta che chiude l'accesso."),
        ("ricevuta", "receipt", "Documento di pagamento."),
        ("resto", "change", "Soldi restituiti."),
        ("sensore", "sensor", "Rileva la presenza dell'auto."),
        ("telecamera", "camera", "Per la sorveglianza."),
        ("targa", "license plate", "Il numero dell'auto."),
        ("abbonamento", "subscription", "Pagamento periodico."),
        ("prenotazione", "reservation", "Posto riservato prima."),
        ("posto", "spot", "Lo spazio per l'auto."),
        ("manovra", "maneuver", "Movimento dell'auto."),
        ("retromarcia", "reverse", "Andare all'indietro."),
        ("freno a mano", "handbrake", "Per bloccare l'auto."),
        ("motore", "engine", "La parte che dà potenza."),
        ("chiavi", "keys", "Servono per aprire e partire."),
        ("specchietto", "mirror", "Per vedere dietro."),
        ("volante", "steering wheel", "Per girare l'auto."),
        ("ruota", "wheel", "Parte rotonda dell'auto."),
        ("benzina", "gasoline", "Carburante comune."),
        ("ricarica", "charging", "Per le auto elettriche."),
        ("elettrica", "electric", "Auto che usa batteria."),
        ("parcheggiare", "to park", "L'azione di lasciare l'auto."),
        ("guidare", "to drive", "L'azione di condurre l'auto.")
    ]
    
    for i, (ita, eng, desc) in enumerate(vocab_list):
        choices_ita = [ita]
        choices_eng = [eng]
        # Add distractors
        distractors = [v for v in vocab_list if v[0] != ita]
        import random
        random.seed(i)
        sample = random.sample(distractors, 3)
        for d in sample:
            choices_ita.append(d[0])
            choices_eng.append(d[1])
        
        # Shuffle aligned
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
        ("Quanto costa il parcheggio?", "How much does parking cost?", "Chiedere il prezzo."),
        ("Dove si trova la cassa?", "Where is the pay station?", "Cercare dove pagare."),
        ("Accetta carte di credito?", "Do you accept credit cards?", "Chiedere il metodo di pagamento."),
        ("È un parcheggio custodito?", "Is it a guarded parking lot?", "Chiedere sulla sicurezza."),
        ("Ho preso una multa.", "I got a fine.", "Segnalare una sanzione."),
        ("Ho perso il ticket.", "I lost the ticket.", "Segnalare la perdita del biglietto."),
        ("Quanto tempo posso stare?", "How long can I stay?", "Chiedere il limite di tempo."),
        ("Solo contanti, per favore.", "Cash only, please.", "Indicazione sul pagamento."),
        ("La sbarra non si apre.", "The barrier doesn't open.", "Segnalare un malfunzionamento."),
        ("Il parchimetro è rotto.", "The parking meter is broken.", "Segnalare un guasto."),
        ("Mi serve la ricevuta.", "I need the receipt.", "Richiedere prova di pagamento."),
        ("Posso parcheggiare qui?", "Can I park here?", "Chiedere il permesso."),
        ("Solo per residenti.", "For residents only.", "Un limite di parcheggio."),
        ("Strisce blu a pagamento.", "Blue lines are paid.", "Spiegare il tipo di strisce."),
        ("Mettere il disco orario.", "Put the parking disk.", "Un'azione necessaria."),
        ("Attenzione alla rimozione.", "Beware of towing.", "Un avvertimento."),
        ("Gira a destra.", "Turn right.", "Dare indicazioni."),
        ("Al prossimo incrocio.", "At the next intersection.", "Specificare dove girare."),
        ("Parcheggio sotterraneo.", "Underground parking.", "Tipo di parcheggio."),
        ("Tariffa oraria.", "Hourly rate.", "Prezzo per ora."),
        ("Tariffa massima.", "Maximum rate.", "Limite di spesa."),
        ("Giornata intera.", "Whole day.", "Durata del parcheggio."),
        ("Prima ora gratuita.", "First hour free.", "Offerta speciale."),
        ("Ore successive.", "Following hours.", "Costi dopo la prima ora."),
        ("Uscita pedonale.", "Pedestrian exit.", "Per chi cammina."),
        ("Accanto all'uscita.", "Next to the exit.", "Posizione della cassa."),
        ("Non si preoccupi.", "Don't worry.", "Rassicurazione."),
        ("Molto gentile.", "Very kind.", "Ringraziamento."),
        ("Divieto di sosta.", "No parking.", "Segnale stradale."),
        ("Rimozione forzata.", "Forced towing.", "Conseguenza del divieto."),
        ("Non l'avevo visto.", "I hadn't seen it.", "Giustificazione."),
        ("Parcheggio regolare.", "Regular parking.", "Posto autorizzato."),
        ("Vado subito.", "I'm going right away.", "Azione immediata."),
        ("Chiavi in macchina.", "Keys in the car.", "Un errore comune."),
        ("Prenotazione online.", "Online reservation.", "Modo moderno di prenotare."),
        ("Posto riservato.", "Reserved spot.", "Spazio non disponibile."),
        ("Carico e scarico.", "Loading and unloading.", "Zona per merci."),
        ("Passi carrabili.", "Driveways.", "Vietato ostruire."),
        ("Parcheggio disabili.", "Disabled parking.", "Posti speciali."),
        ("Navetta per il centro.", "Shuttle to the center.", "Servizio aggiuntivo."),
        ("Aperto h24.", "Open 24/7.", "Orario continuato."),
        ("Video sorveglianza.", "Video surveillance.", "Sicurezza elettronica."),
        ("Pagamento anticipato.", "Prepayment.", "Pagare prima."),
        ("Ritirare il ticket.", "Pick up the ticket.", "Azione all'entrata."),
        ("Inserire il ticket.", "Insert the ticket.", "Azione alla cassa."),
        ("Pagare all'uscita.", "Pay at the exit.", "Procedura comune."),
        ("Posto libero al piano uno.", "Free spot on floor one.", "Indicazione."),
        ("Parcheggio pieno.", "Parking full.", "Nessun posto disponibile."),
        ("Abbonamento mensile.", "Monthly subscription.", "Per chi parcheggia spesso."),
        ("Ricarica elettrica.", "Electric charging.", "Per auto moderne.")
    ]
    
    for i, (ita, eng, desc) in enumerate(phrases_list):
        choices_ita = [ita]
        choices_eng = [eng]
        distractors = [p for p in phrases_list if p[0] != ita]
        import random
        random.seed(i + 100)
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
        ("\"Quanto costa il parcheggio all'ora?\" \"Due euro.\"", "\"How much does parking cost per hour?\" \"Two euros.\"", "Chiedere e rispondere sul prezzo."),
        ("\"C'è una tariffa massima giornaliera?\" \"Sì, quindici euro.\"", "\"Is there a maximum daily rate?\" \"Yes, fifteen euros.\"", "Informarsi sul costo giornaliero."),
        ("\"Dove si trova la cassa automatica?\" \"Vicino all'uscita.\"", "\"Where is the automatic pay station?\" \"Near the exit.\"", "Cercare il punto di pagamento."),
        ("\"La cassa accetta le carte?\" \"Sì, accetta tutto.\"", "\"Does the pay station accept cards?\" \"Yes, it accepts everything.\"", "Verificare i metodi di pagamento."),
        ("\"Posso parcheggiare qui?\" \"No, c'è il divieto di sosta.\"", "\"Can I park here?\" \"No, there is a no parking sign.\"", "Chiedere il permesso di sosta."),
        ("\"Dov'è un parcheggio regolare?\" \"Gira al prossimo incrocio.\"", "\"Where is a regular parking lot?\" \"Turn at the next intersection.\"", "Cercare un posto autorizzato."),
        ("\"Ho perso il mio ticket.\" \"Deve pagare la tariffa massima.\"", "\"I lost my ticket.\" \"You must pay the maximum rate.\"", "Gestire lo smarrimento del biglietto."),
        ("\"Il parcheggio è custodito?\" \"Sì, c'è la videosorveglianza.\"", "\"Is the parking lot guarded?\" \"Yes, there is video surveillance.\"", "Chiedere della sicurezza."),
        ("\"Serve il disco orario qui?\" \"Sì, per massimo un'ora.\"", "\"Is a parking disk needed here?\" \"Yes, for one hour maximum.\"", "Informarsi sulle regole della zona."),
        ("\"Le strisce blu sono a pagamento?\" \"Sì, dalle otto alle venti.\"", "\"Are the blue lines paid?\" \"Yes, from 8 AM to 8 PM.\"", "Regole sulle strisce blu."),
        ("\"Quanto tempo posso lasciare l'auto?\" \"Tutto il tempo che vuole.\"", "\"How long can I leave the car?\" \"As long as you want.\"", "Durata della sosta."),
        ("\"Scusi, ho preso una multa.\" \"Deve andare al comando dei vigili.\"", "\"Excuse me, I got a fine.\" \"You must go to the traffic police station.\"", "Cosa fare in caso di multa."),
        ("\"C'è un garage sotterraneo?\" \"Sì, l'entrata è a destra.\"", "\"Is there an underground garage?\" \"Yes, the entrance is on the right.\"", "Cercare parcheggio coperto."),
        ("\"Il parchimetro è rotto, cosa faccio?\" \"Usi l'app o cerchi un altro.\"", "\"The parking meter is broken, what do I do?\" \"Use the app or find another one.\"", "Problemi tecnici."),
        ("\"Ho dimenticato le chiavi in macchina!\" \"Chiami subito un fabbro.\"", "\"I forgot the keys in the car!\" \"Call a locksmith right away.\"", "Emergenza chiavi."),
        ("\"Posso prenotare un posto online?\" \"Sì, sul nostro sito ufficiale.\"", "\"Can I reserve a spot online?\" \"Yes, on our official website.\"", "Prenotazioni."),
        ("\"C'è la ricarica per auto elettriche?\" \"Sì, al secondo piano.\"", "\"Is there charging for electric cars?\" \"Yes, on the second floor.\"", "Servizi moderni."),
        ("\"Quanto costa la prima ora?\" \"La prima ora è gratuita.\"", "\"How much is the first hour?\" \"The first hour is free.\"", "Promozioni."),
        ("\"La sbarra non si alza.\" \"Prema il tasto per l'assistenza.\"", "\"The barrier doesn't go up.\" \"Press the button for assistance.\"", "Problemi all'uscita."),
        ("\"Mi serve la ricevuta per il lavoro.\" \"La cassa la emette dopo il pagamento.\"", "\"I need the receipt for work.\" \"The machine issues it after payment.\"", "Documentazione."),
        ("\"È rimozione forzata qui?\" \"Sì, è un passo carrabile.\"", "\"Is it forced towing here?\" \"Yes, it's a driveway.\"", "Avvertimenti gravi."),
        ("\"Dove posso parcheggiare gratis?\" \"Sulle strisce bianche.\"", "\"Where can I park for free?\" \"On the white lines.\"", "Risparmiare sul parcheggio."),
        ("\"C'è una navetta per il centro?\" \"Sì, passa ogni dieci minuti.\"", "\"Is there a shuttle to the center?\" \"Yes, it runs every ten minutes.\"", "Collegamenti."),
        ("\"Il parcheggio è pieno?\" \"Sì, torni tra mezz'ora.\"", "\"Is the parking lot full?\" \"Yes, come back in half an hour.\"", "Stato del parcheggio."),
        ("\"Accetta monete da due euro?\" \"Sì, e dà anche il resto.\"", "\"Does it accept two-euro coins?\" \"Yes, and it also gives change.\"", "Dettagli sul pagamento."),
        ("\"Il vigile sta scrivendo una multa.\" \"Presto, sposta la macchina!\"", "\"The officer is writing a fine.\" \"Quick, move the car!\"", "Situazione urgente."),
        ("\"Qual è la tariffa notturna?\" \"Dalle venti è forfettaria.\"", "\"What is the night rate?\" \"From 8 PM it is a flat rate.\"", "Orari notturni."),
        ("\"Dov'è il posto per disabili?\" \"Proprio davanti all'ingresso.\"", "\"Where is the disabled spot?\" \"Right in front of the entrance.\"", "Accessibilità."),
        ("\"Posso pagare con l'app?\" \"Sì, usi il codice sulla macchinetta.\"", "\"Can I pay with the app?\" \"Yes, use the code on the machine.\"", "Tecnologia."),
        ("\"La macchina è troppo grande per questo posto.\" \"Cerchiamo un altro spazio.\"", "\"The car is too big for this spot.\" \"Let's look for another space.\"", "Problemi di spazio."),
        ("\"Buongiorno, un giornaliero per favore.\" \"Ecco a lei, quindici euro.\"", "\"Good morning, a daily pass please.\" \"Here you go, fifteen euros.\"", "Acquisto pass."),
        ("\"Scusi, dov'è l'uscita pedonale?\" \"Segua le frecce verdi sul muro.\"", "\"Excuse me, where is the pedestrian exit?\" \"Follow the green arrows on the wall.\"", "Orientamento."),
        ("\"La targa è obbligatoria per il ticket?\" \"Sì, deve inserirla sulla tastiera.\"", "\"Is the license plate mandatory for the ticket?\" \"Yes, you must enter it on the keyboard.\"", "Inserimento dati."),
        ("\"Ho parcheggiato sul marciapiede.\" \"Attento, rischi la rimozione.\"", "\"I parked on the sidewalk.\" \"Careful, you risk being towed.\"", "Comportamento rischioso."),
        ("\"C'è un limite di altezza?\" \"Sì, massimo due metri.\"", "\"Is there a height limit?\" \"Yes, maximum two meters.\"", "Limiti strutturali."),
        ("\"Il parcheggio è videosorvegliato?\" \"Sì, ventiquattro ore su ventiquattro.\"", "\"Is the parking lot under video surveillance?\" \"Yes, twenty-four hours a day.\"", "Sicurezza."),
        ("\"Posso lasciare le chiavi al custode?\" \"No, le porti con sé.\"", "\"Can I leave the keys with the attendant?\" \"No, take them with you.\"", "Regole del garage."),
        ("\"Quanto tempo ho per uscire dopo aver pagato?\" \"Quindici minuti.\"", "\"How much time do I have to exit after paying?\" \"Fifteen minutes.\"", "Tempo di uscita."),
        ("\"La macchinetta non mi ha dato il resto.\" \"Chiami il numero sul cartello.\"", "\"The machine didn't give me change.\" \"Call the number on the sign.\"", "Reclami."),
        ("\"C'è un abbonamento settimanale?\" \"Sì, costa cinquanta euro.\"", "\"Is there a weekly subscription?\" \"Yes, it costs fifty euros.\"", "Opzioni a lungo termine."),
        ("\"Ho dimenticato dove ho parcheggiato!\" \"Al piano blu, settore C.\"", "\"I forgot where I parked!\" \"On the blue floor, sector C.\"", "Sbadataggine."),
        ("\"Il biglietto è scaduto.\" \"Deve pagare un supplemento alla cassa.\"", "\"The ticket has expired.\" \"You must pay a surcharge at the pay station.\"", "Scadenza."),
        ("\"C'è un parcheggio per moto?\" \"Sì, nell'angolo in fondo.\"", "\"Is there parking for motorcycles?\" \"Yes, in the far corner.\"", "Altri mezzi."),
        ("\"Il sensore è rosso, il posto è occupato.\" \"Andiamo al piano superiore.\"", "\"The sensor is red, the spot is occupied.\" \"Let's go to the upper floor.\"", "Sistemi di parcheggio."),
        ("\"Scusi, questo è il mio posto prenotato.\" \"Ah, scusi, mi sposto subito.\"", "\"Excuse me, this is my reserved spot.\" \"Ah, sorry, I'm moving right away.\"", "Conflitti."),
        ("\"Si può pagare all'uscita con la carta?\" \"Sì, direttamente alla sbarra.\"", "\"Can I pay at the exit with a card?\" \"Yes, directly at the barrier.\"", "Comodità."),
        ("\"C'è molta coda alla cassa.\" \"Usi quella automatica esterna.\"", "\"There is a long line at the pay station.\" \"Use the external automatic one.\"", "Risparmiare tempo."),
        ("\"Devo esporre il ticket sul cruscotto?\" \"Sì, ben visibile.\"", "\"Do I need to display the ticket on the dashboard?\" \"Yes, clearly visible.\"", "Istruzioni."),
        ("\"La targa è registrata nel sistema?\" \"Sì, la sbarra si aprirà da sola.\"", "\"Is the license plate registered in the system?\" \"Yes, the barrier will open by itself.\"", "Automazione."),
        ("\"C'è un'area per carico e scarico?\" \"Sì, solo per quindici minuti.\"", "\"Is there a loading and unloading area?\" \"Yes, for fifteen minutes only.\"", "Breve sosta."),
        ("\"Quanto dista il parcheggio dal centro?\" \"Solo cinque minuti a piedi.\"", "\"How far is the parking from the center?\" \"Only five minutes on foot.\"", "Distanza."),
        ("\"Il parcheggio chiude di notte?\" \"No, è sempre aperto.\"", "\"Does the parking lot close at night?\" \"No, it is always open.\"", "Orari."),
        ("\"C'è lo sconto per i clienti dell'hotel?\" \"Sì, porti il ticket alla reception.\"", "\"Is there a discount for hotel guests?\" \"Yes, take the ticket to the reception.\"", "Sconti."),
        ("\"La macchina davanti a me è bloccata.\" \"Chiamo subito l'assistenza.\"", "\"The car in front of me is stuck.\" \"I'm calling assistance right away.\"", "Imprevisti."),
        ("\"Posso pagare con monete da cinquanta centesimi?\" \"Sì, la cassa le accetta.\"", "\"Can I pay with fifty-cent coins?\" \"Yes, the machine accepts them.\"", "Monete."),
        ("\"Ho bisogno di aiuto per la manovra.\" \"La aiuto io, non si preoccupi.\"", "\"I need help with the maneuver.\" \"I'll help you, don't worry.\"", "Cortesia."),
        ("\"Il freno a mano è tirato?\" \"Sì, la macchina è sicura.\"", "\"Is the handbrake on?\" \"Yes, the car is secure.\"", "Sicurezza del veicolo."),
        ("\"Dove sono le chiavi della macchina?\" \"Le ho messe nello zaino.\"", "\"Where are the car keys?\" \"I put them in the backpack.\"", "Organizzazione."),
        ("\"Il motore fa un brutto rumore.\" \"Meglio lasciarla qui e chiamare il carro attrezzi.\"", "\"The engine is making a bad noise.\" \"Better leave it here and call the tow truck.\"", "Guasti."),
        ("\"Siamo arrivati al parcheggio giusto?\" \"Sì, guarda il nome sull'insegna.\"", "\"Have we arrived at the right parking lot?\" \"Yes, look at the name on the sign.\"", "Verifica.")
    ]
    
    for i, (ita, eng, desc) in enumerate(sentences_list):
        choices_ita = [ita]
        choices_eng = [eng]
        distractors = [s for s in sentences_list if s[0] != ita]
        import random
        random.seed(i + 200)
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

with open(os.path.join(base_path, "travel_parking_vocabulary.json"), "w", encoding="utf-8") as f:
    json.dump(generate_vocab(), f, ensure_ascii=False, indent=2)

with open(os.path.join(base_path, "travel_parking_phrases.json"), "w", encoding="utf-8") as f:
    json.dump(generate_phrases(), f, ensure_ascii=False, indent=2)

with open(os.path.join(base_path, "travel_parking_sentences.json"), "w", encoding="utf-8") as f:
    json.dump(generate_sentences(), f, ensure_ascii=False, indent=2)
