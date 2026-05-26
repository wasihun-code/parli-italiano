import json
import os

def expand_dataset(file_path, new_items):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Check for duplicates (simplified check on correctAnswerItalian)
    existing_answers = {item['correctAnswerItalian'] for item in data}
    for item in new_items:
        if item['correctAnswerItalian'] not in existing_answers:
            data.append(item)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return len(data)

# New items for bike_rental phrases
new_phrases_bike = [
    {
        "choicesItalian": ["È possibile avere un cestino?", "È possibile avere un motore?", "È possibile avere un'auto?", "È possibile avere un volo?"],
        "choicesEnglish": ["Is it possible to have a basket?", "Is it possible to have an engine?", "Is it possible to have a car?", "Is it possible to have a flight?"],
        "correctAnswerItalian": "È possibile avere un cestino?",
        "correctAnswerEnglish": "Is it possible to have a basket?",
        "feedback": {
            "correctItalian": "Esatto! Un cestino è utile per i piccoli acquisti.",
            "incorrectItalian": "No, cestino significa basket.",
            "correctEnglish": "Exactly! A basket is useful for small purchases.",
            "incorrectEnglish": "No, basket is cestino."
        }
    },
    {
        "choicesItalian": ["Il lucchetto è a combinazione?", "Il lucchetto è rotto?", "Il lucchetto è d'oro?", "Il lucchetto è invisibile?"],
        "choicesEnglish": ["Is the lock combination-based?", "Is the lock broken?", "Is the lock made of gold?", "Is the lock invisible?"],
        "correctAnswerItalian": "Il lucchetto è a combinazione?",
        "correctAnswerEnglish": "Is the lock combination-based?",
        "feedback": {
            "correctItalian": "Giusto! Sapere come aprire il lucchetto è fondamentale.",
            "incorrectItalian": "Sbagliato. Si parla di combinazione.",
            "correctEnglish": "Right! Knowing how to open the lock is fundamental.",
            "incorrectEnglish": "Wrong. We are talking about combination."
        }
    },
    {
        "choicesItalian": ["Quanto è la penale in caso di furto?", "Quanto è il premio in caso di furto?", "Quanto è lo sconto in caso di furto?", "Quanto è la festa in caso di furto?"],
        "choicesEnglish": ["How much is the penalty in case of theft?", "How much is the prize in case of theft?", "How much is the discount in case of theft?", "How much is the party in case of theft?"],
        "correctAnswerItalian": "Quanto è la penale in caso di furto?",
        "correctAnswerEnglish": "How much is the penalty in case of theft?",
        "feedback": {
            "correctItalian": "Ottimo! Chiedere dei rischi è molto prudente.",
            "incorrectItalian": "No, penale significa penalty.",
            "correctEnglish": "Great! Asking about the risks is very prudent.",
            "incorrectEnglish": "No, penalty is penale."
        }
    },
    {
        "choicesItalian": ["La catena è sporca di grasso.", "La catena è pulita.", "La catena è nuova.", "La catena è profumata."],
        "choicesEnglish": ["The chain is dirty with grease.", "The chain is clean.", "The chain is new.", "The chain is scented."],
        "correctAnswerItalian": "La catena è sporca di grasso.",
        "correctAnswerEnglish": "The chain is dirty with grease.",
        "feedback": {
            "correctItalian": "Esatto! Attenzione a non sporcarsi i pantaloni.",
            "incorrectItalian": "No, grasso significa grease.",
            "correctEnglish": "Exactly! Be careful not to get your pants dirty.",
            "incorrectEnglish": "No, grease is grasso."
        }
    },
    {
        "choicesItalian": ["Le luci funzionano bene?", "Le luci sono spente?", "Le luci sono rotte?", "Le luci sono blu?"],
        "choicesEnglish": ["Do the lights work well?", "Are the lights off?", "Are the lights broken?", "Are the lights blue?"],
        "correctAnswerItalian": "Le luci funzionano bene?",
        "correctAnswerEnglish": "Do the lights work well?",
        "feedback": {
            "correctItalian": "Giusto! Le luci sono essenziali per la sera.",
            "incorrectItalian": "Sbagliato. Chiedi se funzionano.",
            "correctEnglish": "Right! Lights are essential for the evening.",
            "incorrectEnglish": "Wrong. Ask if they work."
        }
    },
    {
        "choicesItalian": ["Avete anche bici per bambini?", "Avete anche bici per giganti?", "Avete anche bici per cani?", "Avete anche bici per gatti?"],
        "choicesEnglish": ["Do you also have bikes for children?", "Do you also have bikes for giants?", "Do you also have bikes for dogs?", "Do you also have bikes for cats?"],
        "correctAnswerItalian": "Avete anche bici per bambini?",
        "correctAnswerEnglish": "Do you also have bikes for children?",
        "feedback": {
            "correctItalian": "Ottimo! Per chi viaggia con tutta la famiglia.",
            "incorrectItalian": "No, bambini significa children.",
            "correctEnglish": "Great! For those traveling with the whole family.",
            "incorrectEnglish": "No, children is bambini."
        }
    },
    {
        "choicesItalian": ["Posso cambiare marcia?", "Posso cambiare casa?", "Posso cambiare vita?", "Posso cambiare colore?"],
        "choicesEnglish": ["Can I change gear?", "Can I change house?", "Can I change life?", "Can I change color?"],
        "correctAnswerItalian": "Posso cambiare marcia?",
        "correctAnswerEnglish": "Can I change gear?",
        "feedback": {
            "correctItalian": "Esatto! Chiedere come usare il cambio.",
            "incorrectItalian": "No, marcia significa gear.",
            "correctEnglish": "Exactly! Asking how to use the gear.",
            "incorrectEnglish": "No, gear is marcia."
        }
    },
    {
        "choicesItalian": ["Il freno posteriore fischia.", "Il freno posteriore canta.", "Il freno posteriore dorme.", "Il freno posteriore ride."],
        "choicesEnglish": ["The rear brake whistles.", "The rear brake sings.", "The rear brake sleeps.", "The rear brake laughs."],
        "correctAnswerItalian": "Il freno posteriore fischia.",
        "correctAnswerEnglish": "The rear brake whistles.",
        "feedback": {
            "correctItalian": "Giusto! Segnalare un rumore anomalo.",
            "incorrectItalian": "Sbagliato. Fischia significa whistles.",
            "correctEnglish": "Right! Reporting an abnormal noise.",
            "incorrectEnglish": "Wrong. Fischia means whistles."
        }
    },
    {
        "choicesItalian": ["Mi serve una mappa dei percorsi.", "Mi serve una foto dei percorsi.", "Mi serve un video dei percorsi.", "Mi serve un libro dei percorsi."],
        "choicesEnglish": ["I need a map of the paths.", "I need a photo of the paths.", "I need a video of the paths.", "I need a book of the paths."],
        "correctAnswerItalian": "Mi serve una mappa dei percorsi.",
        "correctAnswerEnglish": "I need a map of the paths.",
        "feedback": {
            "correctItalian": "Ottimo! Per pianificare la gita.",
            "incorrectItalian": "No, mappa significa map.",
            "correctEnglish": "Great! To plan the trip.",
            "incorrectEnglish": "No, map is mappa."
        }
    },
    {
        "choicesItalian": ["È compresa l'assistenza stradale?", "È compresa la cena?", "È compresa la musica?", "È compreso il ballo?"],
        "choicesEnglish": ["Is roadside assistance included?", "Is dinner included?", "Is music included?", "Is dancing included?"],
        "correctAnswerItalian": "È compresa l'assistenza stradale?",
        "correctAnswerEnglish": "Is roadside assistance included?",
        "feedback": {
            "correctItalian": "Esatto! Importante in caso di guasti lontano.",
            "incorrectItalian": "No, assistenza stradale significa roadside assistance.",
            "correctEnglish": "Exactly! Important in case of breakdowns far away.",
            "incorrectEnglish": "No, roadside assistance is assistenza stradale."
        }
    },
    {
        "choicesItalian": ["Posso riconsegnarla in un altro punto?", "Posso riconsegnarla in un altro secolo?", "Posso riconsegnarla in un altro pianeta?", "Posso riconsegnarla in un altro ufficio?"],
        "choicesEnglish": ["Can I return it at another point?", "Can I return it in another century?", "Can I return it on another planet?", "Can I return it in another office?"],
        "correctAnswerItalian": "Posso riconsegnarla in un altro punto?",
        "correctAnswerEnglish": "Can I return it at another point?",
        "feedback": {
            "correctItalian": "Giusto! Chiedere la flessibilità della riconsegna.",
            "incorrectItalian": "Sbagliato. Punto significa point.",
            "correctEnglish": "Right! Asking for return flexibility.",
            "incorrectEnglish": "Wrong. Punto means point."
        }
    },
    {
        "choicesItalian": ["Il manubrio è un po' storto.", "Il manubrio è dritto.", "Il manubrio è nuovo.", "Il manubrio è invisibile."],
        "choicesEnglish": ["The handlebar is a bit crooked.", "The handlebar is straight.", "The handlebar is new.", "The handlebar is invisible."],
        "correctAnswerItalian": "Il manubrio è un po' storto.",
        "correctAnswerEnglish": "The handlebar is a bit crooked.",
        "feedback": {
            "correctItalian": "Ottimo! Segnalare un problema di allineamento.",
            "incorrectItalian": "No, storto significa crooked.",
            "correctEnglish": "Great! Reporting an alignment problem.",
            "incorrectEnglish": "No, crooked is storto."
        }
    },
    {
        "choicesItalian": ["Quanto tempo dura la ricarica?", "Quanto tempo dura la festa?", "Quanto tempo dura la pioggia?", "Quanto tempo dura la neve?"],
        "choicesEnglish": ["How long does the charging last?", "How long does the party last?", "How long does the rain last?", "How long does the snow last?"],
        "correctAnswerItalian": "Quanto tempo dura la ricarica?",
        "correctAnswerEnglish": "How long does the charging last?",
        "feedback": {
            "correctItalian": "Esatto! Per le bici elettriche è un dato fondamentale.",
            "incorrectItalian": "No, ricarica significa charging.",
            "correctEnglish": "Exactly! For electric bikes, this is a fundamental piece of data.",
            "incorrectEnglish": "No, charging is ricarica."
        }
    },
    {
        "choicesItalian": ["C'è un parcheggio bici custodito?", "C'è un parcheggio bici segreto?", "C'è un parcheggio bici volante?", "C'è un parcheggio bici sommerso?"],
        "choicesEnglish": ["Is there a guarded bike parking?", "Is there a secret bike parking?", "Is there a flying bike parking?", "Is there an underwater bike parking?"],
        "correctAnswerItalian": "C'è un parcheggio bici custodito?",
        "correctAnswerEnglish": "Is there a guarded bike parking?",
        "feedback": {
            "correctItalian": "Giusto! Per lasciare la bici in sicurezza.",
            "incorrectItalian": "Sbagliato. Custodito significa guarded.",
            "correctEnglish": "Right! To leave the bike safely.",
            "incorrectEnglish": "Wrong. Guarded is custodito."
        }
    },
    {
        "choicesItalian": ["Avete dei seggiolini omologati?", "Avete dei seggiolini di carta?", "Avete dei seggiolini di ghiaccio?", "Avete dei seggiolini di fuoco?"],
        "choicesEnglish": ["Do you have approved child seats?", "Do you have paper child seats?", "Do you have ice child seats?", "Do you have fire child seats?"],
        "correctAnswerItalian": "Avete dei seggiolini omologati?",
        "correctAnswerEnglish": "Do you have approved child seats?",
        "feedback": {
            "correctItalian": "Ottimo! La sicurezza dei bambini prima di tutto.",
            "incorrectItalian": "No, omologati significa approved/certified.",
            "correctEnglish": "Great! Children's safety first.",
            "incorrectEnglish": "No, approved/certified is omologati."
        }
    }
]

# New items for bike_rental sentences
new_sentences_bike = [
    {
        "choicesItalian": ["Il cestino è molto utile per mettere la borsa della spesa.", "Il cestino è molto piccolo per mettere un elefante.", "Il cestino è molto caldo per mettere il ghiaccio.", "Il cestino è molto rotto per mettere nulla."],
        "choicesEnglish": ["The basket is very useful for putting the shopping bag.", "The basket is too small to put an elephant in.", "The basket is too hot to put ice in.", "The basket is too broken to put anything in."],
        "correctAnswerItalian": "Il cestino è molto utile per mettere la borsa della spesa.",
        "correctAnswerEnglish": "The basket is very useful for putting the shopping bag.",
        "feedback": {
            "correctItalian": "Esatto! Il cestino facilita il trasporto di piccoli oggetti.",
            "incorrectItalian": "No, borsa della spesa significa shopping bag.",
            "correctEnglish": "Exactly! The basket makes it easier to carry small objects.",
            "incorrectEnglish": "No, shopping bag is borsa della spesa."
        }
    },
    {
        "choicesItalian": ["Le luci a LED sono automatiche o devo accenderle io?", "Le luci a LED sono magiche o devo sognarle io?", "Le luci a LED sono blu o devo dipingerle io?", "Le luci a LED sono rotte o devo ripararle io?"],
        "choicesEnglish": ["Are the LED lights automatic or do I have to turn them on myself?", "Are the LED lights magical or do I have to dream them myself?", "Are the LED lights blue or do I have to paint them myself?", "Are the LED lights broken or do I have to repair them myself?"],
        "correctAnswerItalian": "Le luci a LED sono automatiche o devo accenderle io?",
        "correctAnswerEnglish": "Are the LED lights automatic or do I have to turn them on myself?",
        "feedback": {
            "correctItalian": "Giusto! Chiedere il funzionamento delle luci per la sicurezza.",
            "incorrectItalian": "Sbagliato. Accenderle significa turn them on.",
            "correctEnglish": "Right! Asking how the lights work for safety.",
            "incorrectEnglish": "Wrong. To turn them on is accenderle."
        }
    },
    {
        "choicesItalian": ["Se mi fermo al bar, devo legare la bici con il lucchetto?", "Se mi fermo al bar, devo ballare con la bici?", "Se mi fermo al bar, devo mangiare la bici?", "Se mi fermo al bar, devo vendere la bici?"],
        "choicesEnglish": ["If I stop at the bar, do I have to lock the bike?", "If I stop at the bar, do I have to dance with the bike?", "If I stop at the bar, do I have to eat the bike?", "If I stop at the bar, do I have to sell the bike?"],
        "correctAnswerItalian": "Se mi fermo al bar, devo legare la bici con il lucchetto?",
        "correctAnswerEnglish": "If I stop at the bar, do I have to lock the bike?",
        "feedback": {
            "correctItalian": "Ottimo! Una domanda pratica per evitare il furto.",
            "incorrectItalian": "No, legare significa to tie/lock.",
            "correctEnglish": "Great! A practical question to avoid theft.",
            "incorrectEnglish": "No, to tie/lock is legare."
        }
    },
    {
        "choicesItalian": ["La catena è uscita, può aiutarmi a rimetterla a posto?", "La catena è scappata, può aiutarmi a correre?", "La catena è morta, può aiutarmi a piangere?", "La catena è stanca, può aiutarmi a dormire?"],
        "choicesEnglish": ["The chain came off, can you help me put it back?", "The chain ran away, can you help me run?", "The chain is dead, can you help me cry?", "The chain is tired, can you help me sleep?"],
        "correctAnswerItalian": "La catena è uscita, può aiutarmi a rimetterla a posto?",
        "correctAnswerEnglish": "The chain came off, can you help me put it back?",
        "feedback": {
            "correctItalian": "Esatto! Chiedere assistenza per un problema tecnico comune.",
            "incorrectItalian": "No, rimetterla a posto significa put it back.",
            "correctEnglish": "Exactly! Asking for assistance for a common technical problem.",
            "incorrectEnglish": "No, put it back is rimetterla a posto."
        }
    },
    {
        "choicesItalian": ["Preferisco una bici con le marce più morbide per la salita.", "Preferisco una bici senza ruote per la salita.", "Preferisco una bici volante per la salita.", "Preferisco una bici di piombo per la salita."],
        "choicesEnglish": ["I prefer a bike with softer gears for the climb.", "I prefer a bike without wheels for the climb.", "I prefer a flying bike for the climb.", "I prefer a lead bike for the climb."],
        "correctAnswerItalian": "Preferisco una bici con le marce più morbide per la salita.",
        "correctAnswerEnglish": "I prefer a bike with softer gears for the climb.",
        "feedback": {
            "correctItalian": "Giusto! Il cambio è fondamentale per le pendenze.",
            "incorrectItalian": "Sbagliato. Morbide significa soft/easy.",
            "correctEnglish": "Right! The gear is fundamental for slopes.",
            "incorrectEnglish": "Wrong. Soft/easy is morbide."
        }
    },
    {
        "choicesItalian": ["C'è una fontanella d'acqua lungo la pista ciclabile?", "C'è una fontanella di vino lungo la pista ciclabile?", "C'è una fontanella di birra lungo la pista ciclabile?", "C'è una fontanella di olio lungo la pista ciclabile?"],
        "choicesEnglish": ["Is there a water fountain along the bike path?", "Is there a wine fountain along the bike path?", "Is there a beer fountain along the bike path?", "Is there an oil fountain along the bike path?"],
        "correctAnswerItalian": "C'è una fontanella d'acqua lungo la pista ciclabile?",
        "correctAnswerEnglish": "Is there a water fountain along the bike path?",
        "feedback": {
            "correctItalian": "Ottimo! Utile per rinfrescarsi durante la pedalata.",
            "incorrectItalian": "No, d'acqua significa of water.",
            "correctEnglish": "Great! Useful for refreshing yourself during the ride.",
            "incorrectEnglish": "No, of water is d'acqua."
        }
    },
    {
        "choicesItalian": ["Ho dimenticato il codice del lucchetto, cosa devo fare?", "Ho dimenticato il mio nome, cosa devo fare?", "Ho dimenticato come si pedala, cosa devo fare?", "Ho dimenticato dove vivo, cosa devo fare?"],
        "choicesEnglish": ["I forgot the lock code, what should I do?", "I forgot my name, what should I do?", "I forgot how to pedal, what should I do?", "I forgot where I live, what should I do?"],
        "correctAnswerItalian": "Ho dimenticato il codice del lucchetto, cosa devo fare?",
        "correctAnswerEnglish": "I forgot the lock code, what should I do?",
        "feedback": {
            "correctItalian": "Esatto! Un imprevisto che richiede l'aiuto del noleggiatore.",
            "incorrectItalian": "No, codice del lucchetto significa lock code.",
            "correctEnglish": "Exactly! An unexpected event that requires the rental agent's help.",
            "incorrectEnglish": "No, lock code is codice del lucchetto."
        }
    },
    {
        "choicesItalian": ["Il sellino è troppo duro, avete un coprisellino in gel?", "Il sellino è troppo alto, avete un coprisellino di piume?", "Il sellino è troppo basso, avete un coprisellino di pietra?", "Il sellino è troppo largo, avete un coprisellino di carta?"],
        "choicesEnglish": ["The saddle is too hard, do you have a gel saddle cover?", "The saddle is too high, do you have a feather saddle cover?", "The saddle is too low, do you have a stone saddle cover?", "The saddle is too wide, do you have a paper saddle cover?"],
        "correctAnswerItalian": "Il sellino è troppo duro, avete un coprisellino in gel?",
        "correctAnswerEnglish": "The saddle is too hard, do you have a gel saddle cover?",
        "feedback": {
            "correctItalian": "Giusto! Per migliorare il comfort durante i lunghi tragitti.",
            "incorrectItalian": "Sbagliato. Duro significa hard.",
            "correctEnglish": "Right! To improve comfort during long journeys.",
            "incorrectEnglish": "Wrong. Hard is duro."
        }
    },
    {
        "choicesItalian": ["Mi hanno rubato la bici, devo chiamare subito la polizia?", "Mi hanno regalato la bici, devo chiamare subito la polizia?", "Mi hanno dipinto la bici, devo chiamare subito la polizia?", "Mi hanno lavato la bici, devo chiamare subito la polizia?"],
        "choicesEnglish": ["My bike was stolen, should I call the police immediately?", "They gave me the bike as a gift, should I call the police immediately?", "They painted my bike, should I call the police immediately?", "They washed my bike, should I call the police immediately?"],
        "correctAnswerItalian": "Mi hanno rubato la bici, devo chiamare subito la polizia?",
        "correctAnswerEnglish": "My bike was stolen, should I call the police immediately?",
        "feedback": {
            "correctItalian": "Ottimo! Una situazione di emergenza seria.",
            "incorrectItalian": "No, rubato significa stolen.",
            "correctEnglish": "Great! A serious emergency situation.",
            "incorrectEnglish": "No, stolen is rubato."
        }
    },
    {
        "choicesItalian": ["Il percorso è illuminato anche di sera o è buio?", "Il percorso è d'oro anche di sera o è d'argento?", "Il percorso è di cioccolato anche di sera o è di vaniglia?", "Il percorso è di nuvole anche di sera o è di fumo?"],
        "choicesEnglish": ["Is the path lit even in the evening or is it dark?", "Is the path made of gold even in the evening or is it silver?", "Is the path made of chocolate even in the evening or is it vanilla?", "Is the path made of clouds even in the evening or is it smoke?"],
        "correctAnswerItalian": "Il percorso è illuminato anche di sera o è buio?",
        "correctAnswerEnglish": "Is the path lit even in the evening or is it dark?",
        "feedback": {
            "correctItalian": "Esatto! Importante per chi rientra tardi.",
            "incorrectItalian": "No, buio significa dark.",
            "correctEnglish": "Exactly! Important for those returning late.",
            "incorrectEnglish": "No, dark is buio."
        }
    },
    {
        "choicesItalian": ["Posso portare la bicicletta sul treno regionale?", "Posso portare la bicicletta sull'aereo?", "Posso portare la bicicletta sottomarino?", "Posso portare la bicicletta nello spazio?"],
        "choicesEnglish": ["Can I take the bicycle on the regional train?", "Can I take the bicycle on the plane?", "Can I take the bicycle on a submarine?", "Can I take the bicycle into space?"],
        "correctAnswerItalian": "Posso portare la bicicletta sul treno regionale?",
        "correctAnswerEnglish": "Can I take the bicycle on the regional train?",
        "feedback": {
            "correctItalian": "Giusto! Molti turisti usano il treno per spostarsi con la bici.",
            "incorrectItalian": "Sbagliato. Treno regionale significa regional train.",
            "correctEnglish": "Right! Many tourists use the train to move around with their bikes.",
            "incorrectEnglish": "Wrong. Regional train is treno regionale."
        }
    },
    {
        "choicesItalian": ["La batteria della bici elettrica è quasi scarica.", "La batteria della bici elettrica è piena di caffè.", "La batteria della bici elettrica è esplosa.", "La batteria della bici elettrica è invisibile."],
        "choicesEnglish": ["The electric bike's battery is almost dead.", "The electric bike's battery is full of coffee.", "The electric bike's battery exploded.", "The electric bike's battery is invisible."],
        "correctAnswerItalian": "La batteria della bici elettrica è quasi scarica.",
        "correctAnswerEnglish": "The electric bike's battery is almost dead.",
        "feedback": {
            "correctItalian": "Ottimo! Segnalare la necessità di ricarica.",
            "incorrectItalian": "No, scarica significa dead/low charge.",
            "correctEnglish": "Great! Reporting the need for charging.",
            "incorrectEnglish": "No, low charge is scarica."
        }
    },
    {
        "choicesItalian": ["Vada piano quando attraversa il centro storico.", "Vada forte quando attraversa il centro storico.", "Vada a dormire quando attraversa il centro storico.", "Vada a cantare quando attraversa il centro storico."],
        "choicesEnglish": ["Go slow when you cross the historic center.", "Go fast when you cross the historic center.", "Go to sleep when you cross the historic center.", "Go singing when you cross the historic center."],
        "correctAnswerItalian": "Vada piano quando attraversa il centro storico.",
        "correctAnswerEnglish": "Go slow when you cross the historic center.",
        "feedback": {
            "correctItalian": "Esatto! Un consiglio per la sicurezza dei pedoni.",
            "incorrectItalian": "No, piano significa slow.",
            "correctEnglish": "Exactly! A tip for pedestrian safety.",
            "incorrectEnglish": "No, slow is piano."
        }
    },
    {
        "choicesItalian": ["Il casco è obbligatorio o è solo consigliato?", "Il casco è proibito o è solo consigliato?", "Il casco è blu o è solo consigliato?", "Il casco è rotto o è solo consigliato?"],
        "choicesEnglish": ["Is the helmet mandatory or is it just recommended?", "Is the helmet forbidden or is it just recommended?", "Is the helmet blue or is it just recommended?", "Is the helmet broken or is it just recommended?"],
        "correctAnswerItalian": "Il casco è obbligatorio o è solo consigliato?",
        "correctAnswerEnglish": "Is the helmet mandatory or is it just recommended?",
        "feedback": {
            "correctItalian": "Giusto! Chiedere le regole locali sulla sicurezza.",
            "incorrectItalian": "Sbagliato. Obbligatorio significa mandatory.",
            "correctEnglish": "Right! Asking about local safety rules.",
            "incorrectEnglish": "Wrong. Mandatory is obbligatorio."
        }
    },
    {
        "choicesItalian": ["C'è molto fango sul sentiero dopo la pioggia di ieri.", "C'è molto zucchero sul sentiero dopo la pioggia di ieri.", "C'è molto oro sul sentiero dopo la pioggia di ieri.", "C'è molto fuoco sul sentiero dopo la pioggia di ieri."],
        "choicesEnglish": ["There is a lot of mud on the path after yesterday's rain.", "There is a lot of sugar on the path after yesterday's rain.", "There is a lot of gold on the path after yesterday's rain.", "There is a lot of fire on the path after yesterday's rain."],
        "correctAnswerItalian": "C'è molto fango sul sentiero dopo la pioggia di ieri.",
        "correctAnswerEnglish": "There is a lot of mud on the path after yesterday's rain.",
        "feedback": {
            "correctItalian": "Ottimo! Una segnalazione sulle condizioni del percorso.",
            "incorrectItalian": "No, fango significa mud.",
            "correctEnglish": "Great! A report on the path conditions.",
            "incorrectEnglish": "No, mud is fango."
        }
    },
    {
        "choicesItalian": ["Posso prolungare il noleggio per un altro giorno?", "Posso prolungare il noleggio per un altro anno?", "Posso prolungare il noleggio per un altro secolo?", "Posso prolungare il noleggio per un altro pianeta?"],
        "choicesEnglish": ["Can I extend the rental for another day?", "Can I extend the rental for another year?", "Can I extend the rental for another century?", "Can I extend the rental for another planet?"],
        "correctAnswerItalian": "Posso prolungare il noleggio per un altro giorno?",
        "correctAnswerEnglish": "Can I extend the rental for another day?",
        "feedback": {
            "correctItalian": "Esatto! Chiedere di tenere la bici più a lungo.",
            "incorrectItalian": "No, prolungare significa to extend.",
            "correctEnglish": "Exactly! Asking to keep the bike longer.",
            "incorrectEnglish": "No, to extend is prolungare."
        }
    },
    {
        "choicesItalian": ["Il cavalletto della bici è rotto e non sta in piedi.", "Il cavalletto della bici è d'oro e non sta in piedi.", "Il cavalletto della bici è invisibile e non sta in piedi.", "Il cavalletto della bici è felice e non sta in piedi."],
        "choicesEnglish": ["The bike's kickstand is broken and won't stand up.", "The bike's kickstand is made of gold and won't stand up.", "The bike's kickstand is invisible and won't stand up.", "The bike's kickstand is happy and won't stand up."],
        "correctAnswerItalian": "Il cavalletto della bici è rotto e non sta in piedi.",
        "correctAnswerEnglish": "The bike's kickstand is broken and won't stand up.",
        "feedback": {
            "correctItalian": "Giusto! Segnalare un problema di stabilità.",
            "incorrectItalian": "Sbagliato. Cavalletto significa kickstand.",
            "correctEnglish": "Right! Reporting a stability problem.",
            "incorrectEnglish": "Wrong. Kickstand is cavalletto."
        }
    },
    {
        "choicesItalian": ["Grazie per avermi gonfiato le gomme, ora va molto meglio.", "Grazie per avermi rotto le gomme, ora va molto meglio.", "Grazie per avermi mangiato le gomme, ora va molto meglio.", "Grazie per avermi sognato le gomme, ora va molto meglio."],
        "choicesEnglish": ["Thanks for inflating the tires, it's much better now.", "Thanks for breaking my tires, it's much better now.", "Thanks for eating my tires, it's much better now.", "Thanks for dreaming about my tires, it's much better now."],
        "correctAnswerItalian": "Grazie per avermi gonfiato le gomme, ora va molto meglio.",
        "correctAnswerEnglish": "Thanks for inflating the tires, it's much better now.",
        "feedback": {
            "correctItalian": "Ottimo! Un ringraziamento per la manutenzione.",
            "incorrectItalian": "No, gonfiato significa inflated.",
            "correctEnglish": "Great! Thanks for the maintenance.",
            "incorrectEnglish": "No, inflated is gonfiato."
        }
    },
    {
        "choicesItalian": ["Dove posso trovare un kit per le riparazioni veloci?", "Dove posso trovare un kit per le riparazioni dell'anima?", "Dove posso trovare un kit per le riparazioni del tempo?", "Dove posso trovare un kit per le riparazioni del mondo?"],
        "choicesEnglish": ["Where can I find a quick repair kit?", "Where can I find a kit for soul repairs?", "Where can I find a kit for time repairs?", "Where can I find a kit for world repairs?"],
        "correctAnswerItalian": "Dove posso trovare un kit per le riparazioni veloci?",
        "correctAnswerEnglish": "Where can I find a quick repair kit?",
        "feedback": {
            "correctItalian": "Esatto! Essere preparati per le piccole forature.",
            "incorrectItalian": "No, kit per riparazioni significa repair kit.",
            "correctEnglish": "Exactly! Being prepared for small punctures.",
            "incorrectEnglish": "No, repair kit is kit per riparazioni."
        }
    },
    {
        "choicesItalian": ["La catena fa uno strano rumore quando pedalo veloce.", "La catena fa una bella canzone quando pedalo veloce.", "La catena fa un bel sogno quando pedalo veloce.", "La catena fa un bel disegno quando pedalo veloce."],
        "choicesEnglish": ["The chain makes a strange noise when I pedal fast.", "The chain makes a beautiful song when I pedal fast.", "The chain makes a beautiful dream when I pedal fast.", "The chain makes a beautiful drawing when I pedal fast."],
        "correctAnswerItalian": "La catena fa uno strano rumore quando pedalo veloce.",
        "correctAnswerEnglish": "The chain makes a strange noise when I pedal fast.",
        "feedback": {
            "correctItalian": "Giusto! Segnalare un rumore meccanico sospetto.",
            "incorrectItalian": "Sbagliato. Rumore significa noise.",
            "correctEnglish": "Right! Reporting a suspicious mechanical noise.",
            "incorrectEnglish": "Wrong. Noise is rumore."
        }
    }
]

file_p = 'src/data/exports/travel/bike_rental/travel_bike_rental_phrases.json'
file_s = 'src/data/exports/travel/bike_rental/travel_bike_rental_sentences.json'

new_p_len = expand_dataset(file_p, new_phrases_bike)
new_s_len = expand_dataset(file_s, new_sentences_bike)

print(f'New lengths for bike_rental: phrases={new_p_len}, sentences={new_s_len}')
