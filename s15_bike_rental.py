import json
import os

scenario_id = "s15"
base_path = f"src/data/exports/travel/bike_rental/"
os.makedirs(base_path, exist_ok=True)

def generate_vocab():
    data = []
    vocab_list = [
        ("noleggiare", "to rent", "Prendere qualcosa in cambio di soldi."),
        ("bicicletta", "bicycle", "Mezzo di trasporto a due ruote."),
        ("bici", "bike", "Abbreviazione di bicicletta."),
        ("città", "city", "Luogo urbanizzato."),
        ("mountain bike", "mountain bike", "Bici per percorsi sterrati."),
        ("elettrica", "electric", "Bici con motore a batteria."),
        ("giornata", "day", "L'intero giorno."),
        ("costo", "cost", "Il prezzo da pagare."),
        ("lucchetto", "lock", "Per chiudere la bici."),
        ("casco", "helmet", "Per proteggere la testa."),
        ("catena", "chain", "Parte che trasmette il moto."),
        ("problema", "problem", "Qualcosa che non va."),
        ("cambiare", "to change/exchange", "Sostituire un oggetto."),
        ("modello", "model", "Il tipo di bici."),
        ("nuova", "new", "Mai usata o recente."),
        ("pista ciclabile", "bike path", "Corsia riservata alle bici."),
        ("fiume", "river", "Corso d'acqua."),
        ("pianeggiante", "flat", "Senza salite o discese."),
        ("panoramico", "scenic", "Con una bella vista."),
        ("lungo", "long", "Distanza elevata."),
        ("parco", "park", "Area verde."),
        ("consiglio", "advice", "Suggerimento utile."),
        ("pedale", "pedal", "Dove si appoggia il piede."),
        ("freno", "brake", "Per fermare la bici."),
        ("ruota", "wheel", "Parte rotonda."),
        ("gonfiare", "to inflate", "Mettere aria nelle ruote."),
        ("pompa", "pump", "Strumento per gonfiare."),
        ("sellino", "saddle", "Dove ci si siede sulla bici."),
        ("manubrio", "handlebar", "Per dirigere la bici."),
        ("cambio", "gears", "Per regolare lo sforzo."),
        ("altezza", "height", "Regolazione del sellino."),
        ("sicuro", "safe", "Senza pericoli."),
        ("chiave", "key", "Per il lucchetto."),
        ("noleggio", "rental", "Il servizio di affitto."),
        ("tariffa", "rate", "Prezzo orario o giornaliero."),
        ("deposito", "deposit", "Soldi lasciati come garanzia."),
        ("documento", "ID", "Carta d'identità per il noleggio."),
        ("restituire", "to return", "Riportare la bici."),
        ("ritardo", "delay", "Riportare la bici dopo l'orario."),
        ("mappa", "map", "Per vedere i percorsi ciclabili."),
        ("percorso", "route/path", "La via da seguire."),
        ("chilometro", "kilometer", "Unità di distanza."),
        ("ora", "hour", "Unità di tempo."),
        ("riparazione", "repair", "Aggiustare la bici."),
        ("gomma a terra", "flat tire", "Quando manca aria."),
        ("cestino", "basket", "Per portare oggetti sulla bici."),
        ("luci", "lights", "Per vedere e farsi vedere di notte."),
        ("campanello", "bell", "Per avvisare i pedoni."),
        ("seggiolino", "child seat", "Per portare un bambino."),
        ("assistenza", "assistance", "Aiuto in caso di guasto.")
    ]
    
    for i, (ita, eng, desc) in enumerate(vocab_list):
        choices_ita = [ita]
        choices_eng = [eng]
        distractors = [v for v in vocab_list if v[0] != ita]
        import random
        random.seed(i + 900)
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
        ("Vorrei noleggiare una bici.", "I would like to rent a bike.", "Esprimere il desiderio di noleggio."),
        ("Per l'intera giornata.", "For the whole day.", "Specificare la durata."),
        ("Quanto costa al giorno?", "How much does it cost per day?", "Chiedere il prezzo."),
        ("Bici da città o mountain bike?", "City bike or mountain bike?", "Opzioni di scelta."),
        ("È incluso il lucchetto?", "Is the lock included?", "Chiedere degli accessori."),
        ("Serve il casco?", "Do I need a helmet?", "Domanda sulla sicurezza."),
        ("Ho un problema con la catena.", "I have a problem with the chain.", "Segnalare un guasto."),
        ("La catena continua a scendere.", "The chain keeps coming off.", "Descrivere il problema tecnico."),
        ("Vorrei cambiare la bici.", "I would like to change the bike.", "Chiedere una sostituzione."),
        ("È lo stesso modello.", "It is the same model.", "Confrontare due bici."),
        ("Nuova di zecca.", "Brand new.", "Descrivere un oggetto mai usato."),
        ("Ci sono piste ciclabili?", "Are there bike paths?", "Chiedere sui percorsi."),
        ("Consiglio il percorso lungo il fiume.", "I recommend the route along the river.", "Dare un suggerimento."),
        ("È tutto pianeggiante.", "It is all flat.", "Descrivere l'altimetria."),
        ("Molto panoramico.", "Very scenic.", "Descrivere la bellezza del percorso."),
        ("Quanto è lungo il tragitto?", "How long is the journey?", "Chiedere la distanza."),
        ("Fino al parco regionale.", "Up to the regional park.", "Indicare la meta."),
        ("Grazie del consiglio.", "Thanks for the advice.", "Ringraziamento."),
        ("Serve un documento?", "Do I need an ID?", "Chiedere le formalità."),
        ("Bisogna lasciare un deposito?", "Do I need to leave a deposit?", "Domanda sulla cauzione."),
        ("A che ora devo riportarla?", "What time do I have to bring it back?", "Chiedere l'orario di consegna."),
        ("Il sellino è troppo alto.", "The saddle is too high.", "Segnalare scomodità."),
        ("Può abbassare il sellino?", "Can you lower the saddle?", "Richiedere una regolazione."),
        ("Le gomme sono sgonfie.", "The tires are flat.", "Segnalare mancanza d'aria."),
        ("Mi serve una pompa.", "I need a pump.", "Richiedere uno strumento."),
        ("Il freno non funziona bene.", "The brake doesn't work well.", "Segnalare un pericolo."),
        ("C'è un cestino anteriore?", "Is there a front basket?", "Chiedere un accessorio per oggetti."),
        ("Avete bici per bambini?", "Do you have kids' bikes?", "Chiedere opzioni per famiglia."),
        ("Vorrei una bici elettrica.", "I would like an electric bike.", "Scegliere un tipo specifico."),
        ("La batteria è carica?", "Is the battery charged?", "Verifica per bici elettrica."),
        ("Dove trovo una mappa?", "Where can I find a map?", "Cercare orientamento."),
        ("Il lucchetto è bloccato.", "The lock is stuck.", "Segnalare un problema con la chiave."),
        ("Ho forato la gomma.", "I have a flat tire.", "Segnalare un danno."),
        ("Potete ripararla?", "Can you repair it?", "Richiedere assistenza."),
        ("Quanto dista il centro?", "How far is the center?", "Chiedere la distanza."),
        ("Posso portarla sul treno?", "Can I take it on the train?", "Chiedere regole di trasporto."),
        ("È un percorso impegnativo?", "Is it a challenging route?", "Chiedere sulla difficoltà."),
        ("Ci sono molte salite?", "Are there many climbs?", "Chiedere sulla pendenza."),
        ("Il campanello non suona.", "The bell doesn't ring.", "Segnalare un piccolo guasto."),
        ("Le luci sono obbligatorie?", "Are lights mandatory?", "Chiedere regole di sicurezza."),
        ("Mi dà anche una borsa laterale?", "Can you also give me a pannier?", "Richiedere accessori extra."),
        ("Posso pagare con carta?", "Can I pay by card?", "Chiedere il metodo di pagamento."),
        ("Ecco il mio documento.", "Here is my ID.", "Consegnare l'identità."),
        ("Spero che non piova.", "I hope it doesn't rain.", "Preoccupazione meteo."),
        ("Dove posso parcheggiare?", "Where can I park?", "Chiedere della sosta."),
        ("Attenzione ai pedoni.", "Watch out for pedestrians.", "Regola di guida."),
        ("Sempre sulla destra.", "Always on the right.", "Regola della strada."),
        ("Buona pedalata!", "Happy cycling!", "Augurio tipico."),
        ("La bici è molto leggera.", "The bike is very light.", "Osservazione tecnica."),
        ("Torno tra due ore.", "I'll be back in two hours.", "Comunicare l'orario.")
    ]
    
    for i, (ita, eng, desc) in enumerate(phrases_list):
        choices_ita = [ita]
        choices_eng = [eng]
        distractors = [p for p in phrases_list if p[0] != ita]
        import random
        random.seed(i + 1000)
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
        ("\"Vorrei noleggiare due bici per l'intera giornata.\" \"Certo, abbiamo bici da città o mountain bike.\"", "\"I'd like to rent two bikes for the whole day.\" \"Sure, we have city bikes or mountain bikes.\"", "Inizio noleggio."),
        ("\"Quanto costano le bici elettriche?\" \"Trenta euro al giorno, incluso il casco.\"", "\"How much are the electric bikes?\" \"Thirty euros per day, including the helmet.\"", "Chiedere il prezzo delle bici elettriche."),
        ("\"È incluso il lucchetto nel prezzo?\" \"Sì, ve ne diamo uno per ogni bici.\"", "\"Is the lock included in the price?\" \"Yes, we give you one for each bike.\"", "Verifica accessori."),
        ("\"Ho un problema con la catena, continua a scendere.\" \"Mi dispiace, gliela cambio subito.\"", "\"I have a problem with the chain, it keeps coming off.\" \"I'm sorry, I'll change it for you right away.\"", "Segnalare un guasto."),
        ("\"Preferirei cambiare la bici per sicurezza.\" \"Certamente, prenda questo modello nuovo.\"", "\"I'd prefer to change the bike for safety.\" \"Certainly, take this new model.\"", "Sostituzione veicolo."),
        ("\"Ci sono delle belle piste ciclabili qui intorno?\" \"Sì, le consiglio quella lungo il fiume.\"", "\"Are there any nice bike paths around here?\" \"Yes, I recommend the one along the river.\"", "Chiedere consigli sui percorsi."),
        ("\"Il percorso è pianeggiante?\" \"Sì, è perfetto per una passeggiata rilassante.\"", "\"Is the route flat?\" \"Yes, it's perfect for a relaxing ride.\"", "Chiedere sulla difficoltà."),
        ("\"Quanto è lungo il giro fino al parco?\" \"Sono circa dodici chilometri tra andata e ritorno.\"", "\"How long is the ride to the park?\" \"It's about twelve kilometers round trip.\"", "Chiedere la distanza."),
        ("\"Serve un documento per il noleggio?\" \"Sì, serve la carta d'identità.\"", "\"Do I need an ID for the rental?\" \"Yes, you need your ID card.\"", "Formalità burocratiche."),
        ("\"Dobbiamo lasciare un deposito in contanti?\" \"Sì, venti euro a bicicletta.\"", "\"Do we need to leave a cash deposit?\" \"Yes, twenty euros per bicycle.\"", "Informazioni sulla cauzione."),
        ("\"A che ora chiude il negozio stasera?\" \"Chiudiamo alle diciannove in punto.\"", "\"What time does the shop close tonight?\" \"We close at 7 PM sharp.\"", "Orari di restituzione."),
        ("\"Può regolarmi l'altezza del sellino?\" \"Certamente, salga pure per provare.\"", "\"Can you adjust the saddle height for me?\" \"Certainly, go ahead and get on to try.\"", "Regolazione comfort."),
        ("\"Le gomme mi sembrano un po' sgonfie.\" \"Le gonfio subito con la pompa.\"", "\"The tires look a bit flat to me.\" \"I'll inflate them right away with the pump.\"", "Manutenzione rapida."),
        ("\"I freni fischiano molto, è normale?\" \"No, meglio controllare le pastiglie.\"", "\"The brakes squeak a lot, is that normal?\" \"No, better check the pads.\"", "Sicurezza freni."),
        ("\"Avete un seggiolino per un bambino di tre anni?\" \"Sì, lo montiamo sulla bici da città.\"", "\"Do you have a child seat for a three-year-old?\" \"Yes, we mount it on the city bike.\"", "Noleggio per famiglie."),
        ("\"Posso pagare il noleggio con la carta di credito?\" \"Sì, accettiamo tutte le carte principali.\"", "\"Can I pay for the rental with a credit card?\" \"Yes, we accept all major cards.\"", "Metodo di pagamento."),
        ("\"Dove possiamo parcheggiare le bici in centro?\" \"Ci sono molte rastrelliere vicino alla piazza.\"", "\"Where can we park the bikes downtown?\" \"There are many racks near the square.\"", "Consigli per la sosta."),
        ("\"C'è una mappa dei percorsi ciclabili disponibile?\" \"Sì, ecco a lei una brochure gratuita.\"", "\"Is there a map of the bike paths available?\" \"Yes, here is a free brochure for you.\"", "Orientamento."),
        ("\"Se foro una gomma, cosa devo fare?\" \"Ci chiami e veniamo a portarvi una bici nuova.\"", "\"If I get a flat tire, what should I do?\" \"Call us and we'll come bring you a new bike.\"", "Assistenza stradale."),
        ("\"La bici elettrica ha molta autonomia?\" \"Sì, può fare fino a sessanta chilometri.\"", "\"Does the electric bike have a lot of range?\" \"Yes, it can do up to sixty kilometers.\"", "Dettagli tecnici."),
        ("\"Speriamo che il tempo rimanga bello per tutto il giorno.\" \"Sì, le previsioni sono ottime.\"", "\"Let's hope the weather stays nice all day.\" \"Yes, the forecast is great.\"", "Chiacchiere sul meteo."),
        ("\"Il percorso lungo il fiume è panoramico?\" \"Sì, vedrete molti uccelli e una vecchia diga.\"", "\"Is the route along the river scenic?\" \"Yes, you'll see many birds and an old dam.\"", "Attrazioni sul percorso."),
        ("\"Si può pedalare anche nella zona pedonale?\" \"Sì, ma vada molto piano e faccia attenzione.\"", "\"Can one cycle in the pedestrian zone too?\" \"Yes, but go very slowly and be careful.\"", "Regole locali."),
        ("\"Grazie mille per la gentilezza!\" \"Prego, buona pedalata e buon divertimento!\"", "\"Thank you very much for your kindness!\" \"You're welcome, happy cycling and have fun!\"", "Conclusione cordiale."),
        ("\"Quanto tempo ci vuole per arrivare al parco?\" \"Circa quaranta minuti con calma.\"", "\"How long does it take to get to the park?\" \"About forty minutes at a leisurely pace.\"", "Stima del tempo."),
        ("\"C'è un cestino per mettere lo zaino?\" \"Sì, glielo monto subito sul manubrio.\"", "\"Is there a basket to put the backpack in?\" \"Yes, I'll mount it on the handlebar for you right away.\"", "Accessori pratici."),
        ("\"Bisogna indossare il casco in città?\" \"Non è obbligatorio, ma è consigliato.\"", "\"Is it mandatory to wear a helmet in the city?\" \"It's not mandatory, but it's recommended.\"", "Regole di sicurezza."),
        ("\"Il campanello è importante per avvisare i pedoni.\" \"Sì, lo usi specialmente negli incroci.\"", "\"The bell is important to warn pedestrians.\" \"Yes, use it especially at intersections.\"", "Consigli di guida."),
        ("\"Possiamo cambiare il percorso a metà strada?\" \"Certo, la mappa mostra diverse varianti.\"", "\"Can we change the route halfway?\" \"Of course, the map shows several variations.\"", "Flessibilità."),
        ("\"Le luci si accendono da sole?\" \"Sì, hanno un sensore crepuscolare.\"", "\"Do the lights turn on by themselves?\" \"Yes, they have a twilight sensor.\"", "Tecnologia bici."),
        ("\"Posso noleggiare la bici solo per un'ora?\" \"Sì, la tariffa minima è di cinque euro.\"", "\"Can I rent the bike for just one hour?\" \"Yes, the minimum rate is five euros.\"", "Noleggio breve."),
        ("\"Avete un lucchetto più robusto?\" \"Sì, abbiamo anche le catene d'acciaio.\"", "\"Do you have a sturdier lock?\" \"Yes, we also have steel chains.\"", "Sicurezza furti."),
        ("\"La sella è un po' dura, avete dei coprisella?\" \"Sì, ne abbiamo alcuni in gel molto comodi.\"", "\"The saddle is a bit hard, do you have seat covers?\" \"Yes, we have some very comfortable gel ones.\"", "Comfort extra."),
        ("\"Dove finisce la pista ciclabile?\" \"Finisce proprio davanti alla stazione dei treni.\"", "\"Where does the bike path end?\" \"It ends right in front of the train station.\"", "Informazioni fine percorso."),
        ("\"Si può portare la bici sul traghetto?\" \"Sì, di solito è gratuito per le biciclette.\"", "\"Can one take the bike on the ferry?\" \"Yes, it's usually free for bicycles.\"", "Trasporto multimodale."),
        ("\"C'è molta salita per andare in collina?\" \"Sì, per quello vi consiglio la bici elettrica.\"", "\"Is there a lot of climbing to go to the hills?\" \"Yes, for that I recommend the electric bike.\"", "Scelta del mezzo."),
        ("\"Avete anche i caschi per bambini?\" \"Sì, di tutte le taglie, dai due anni in su.\"", "\"Do you have helmets for kids too?\" \"Yes, all sizes, from two years old up.\"", "Sicurezza famiglia."),
        ("\"Il noleggio include un'assicurazione contro il furto?\" \"Sì, ma c'è una franchigia di cinquanta euro.\"", "\"Does the rental include theft insurance?\" \"Yes, but there's a fifty-euro deductible.\"", "Assicurazione."),
        ("\"Dov'è il negozio di noleggio più vicino al porto?\" \"È proprio dietro l'ufficio informazioni.\"", "\"Where is the nearest rental shop to the port?\" \"It's right behind the information office.\"", "Posizione."),
        ("\"Posso tenere la bici durante la notte?\" \"Sì, ma deve avere un posto sicuro dove chiuderla.\"", "\"Can I keep the bike overnight?\" \"Yes, but you must have a safe place to lock it up.\"", "Noleggio notturno."),
        ("\"C'è molta gente sulla pista ciclabile la domenica?\" \"Sì, è molto frequentata dalle famiglie.\"", "\"Are there many people on the bike path on Sundays?\" \"Yes, it's very popular with families.\"", "Affollamento."),
        ("\"Il cambio non entra bene, gratta un po'.\" \"Lo regoliamo subito, è solo un cavo allentato.\"", "\"The gears don't engage well, they grind a bit.\" \"We'll adjust it right away, it's just a loose cable.\"", "Manutenzione tecnica."),
        ("\"Avete delle bici con le marce?\" \"Sì, tutte le nostre bici hanno almeno sette marce.\"", "\"Do you have bikes with gears?\" \"Yes, all our bikes have at least seven gears.\"", "Dotazione tecnica."),
        ("\"Si può fare il giro del lago in bici?\" \"Sì, è un percorso di circa venti chilometri.\"", "\"Can one bike around the lake?\" \"Yes, it's a route of about twenty kilometers.\"", "Idee di viaggio."),
        ("\"Ho dimenticato di riportare il lucchetto!\" \"Non si preoccupi, lo porti domani mattina.\"", "\"I forgot to bring back the lock!\" \"Don't worry, bring it tomorrow morning.\"", "Piccoli errori."),
        ("\"La batteria della bici elettrica è quasi scarica.\" \"La colleghi alla presa qui in officina.\"", "\"The electric bike's battery is almost dead.\" \"Plug it into the socket here in the workshop.\"", "Ricarica."),
        ("\"Avete delle bici tandem?\" \"Sì, ne abbiamo uno solo, meglio prenotarlo.\"", "\"Do you have tandem bikes?\" \"Yes, we only have one, better to book it.\"", "Mezzi speciali."),
        ("\"C'è un limite di peso per il portapacchi?\" \"Sì, massimo dieci chilogrammi.\"", "\"Is there a weight limit for the luggage rack?\" \"Yes, maximum ten kilograms.\"", "Limiti di carico."),
        ("\"Il campanello è obbligatorio per legge?\" \"Sì, come le luci e i freni funzionanti.\"", "\"Is the bell mandatory by law?\" \"Yes, like lights and working brakes.\"", "Codice della strada."),
        ("\"Possiamo avere uno sconto per un gruppo di dieci persone?\" \"Sì, vi faccio il dieci per cento di sconto.\"", "\"Can we have a discount for a group of ten people?\" \"Yes, I'll give you a ten percent discount.\"", "Sconti comitive."),
        ("\"La bici è troppo pesante per me.\" \"Proviamo questo modello in alluminio, è più leggero.\"", "\"The bike is too heavy for me.\" \"Let's try this aluminum model, it's lighter.\"", "Scelta ergonomica."),
        ("\"Dov'è l'inizio della pista ciclabile?\" \"Oltrepassi il ponte e la vedrà sulla sinistra.\"", "\"Where is the start of the bike path?\" \"Cross the bridge and you'll see it on the left.\"", "Trovare la via."),
        ("\"Avete dei kit per riparare le forature?\" \"Sì, ve ne diamo uno incluso nel noleggio.\"", "\"Do you have puncture repair kits?\" \"Yes, we give you one included in the rental.\"", "Autonomia passeggero."),
        ("\"Il manubrio è un po' storto.\" \"Lo raddrizziamo subito con questa chiave.\"", "\"The handlebar is a bit crooked.\" \"We'll straighten it right away with this wrench.\"", "Piccola regolazione."),
        ("\"Si può andare in bici sul marciapiede?\" \"No, è vietato se non c'è la corsia apposita.\"", "\"Can one bike on the sidewalk?\" \"No, it's forbidden unless there's a dedicated lane.\"", "Regole di convivenza."),
        ("\"La sella è troppo bassa per le mie gambe.\" \"La alziamo subito, ecco fatto.\"", "\"The saddle is too low for my legs.\" \"We'll raise it right away, there you go.\"", "Comfort di guida."),
        ("\"C'è un servizio di recupero bici se rimaniamo bloccati?\" \"Sì, chiamate il numero sul telaio.\"", "\"Is there a bike recovery service if we get stuck?\" \"Yes, call the number on the frame.\"", "Emergenze."),
        ("\"Vogliamo fare una foto con le bici!\" \"Mettetevi davanti all'insegna, vi aiuto io.\"", "\"We want to take a photo with the bikes!\" \"Get in front of the sign, I'll help you.\"", "Ricordi."),
        ("\"La catena è sporca di grasso, attenti ai pantaloni.\" \"Grazie, li arrotoliamo subito.\"", "\"The chain is greasy, watch your pants.\" \"Thanks, we'll roll them up right away.\"", "Consigli pratici."),
        ("\"Siete pronti per la gita?\" \"Sì, carichi e pronti a pedalare!\"", "\"Are you ready for the trip?\" \"Yes, energized and ready to pedal!\"", "Entusiasmo.")
    ]
    
    for i, (ita, eng, desc) in enumerate(sentences_list):
        choices_ita = [ita]
        choices_eng = [eng]
        distractors = [s for s in sentences_list if s[0] != ita]
        import random
        random.seed(i + 1100)
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

with open(os.path.join(base_path, "travel_bike_rental_vocabulary.json"), "w", encoding="utf-8") as f:
    json.dump(generate_vocab(), f, ensure_ascii=False, indent=2)

with open(os.path.join(base_path, "travel_bike_rental_phrases.json"), "w", encoding="utf-8") as f:
    json.dump(generate_phrases(), f, ensure_ascii=False, indent=2)

with open(os.path.join(base_path, "travel_bike_rental_sentences.json"), "w", encoding="utf-8") as f:
    json.dump(generate_sentences(), f, ensure_ascii=False, indent=2)
