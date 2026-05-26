import json
import os

def expand_dataset(file_path, new_items):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    existing_answers = {item['correctAnswerItalian'] for item in data}
    for item in new_items:
        if item['correctAnswerItalian'] not in existing_answers:
            data.append(item)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return len(data)

new_phrases_bus = [
    {
        "choicesItalian": ["Dove si compra il biglietto?", "Dove si compra il pane?", "Dove si compra il latte?", "Dove si compra il giornale?"],
        "choicesEnglish": ["Where do you buy the ticket?", "Where do you buy bread?", "Where do you buy milk?", "Where do you buy the newspaper?"],
        "correctAnswerItalian": "Dove si compra il biglietto?",
        "correctAnswerEnglish": "Where do you buy the ticket?",
        "feedback": {
            "correctItalian": "Esatto! La prima domanda da fare per usare il bus.",
            "incorrectItalian": "No, biglietto significa ticket.",
            "correctEnglish": "Exactly! The first question to ask to use the bus.",
            "incorrectEnglish": "No, ticket is biglietto."
        }
    },
    {
        "choicesItalian": ["Si può pagare a bordo?", "Si può pagare dopo?", "Si può pagare con un bacio?", "Si può pagare con la spesa?"],
        "choicesEnglish": ["Can I pay on board?", "Can I pay later?", "Can I pay with a kiss?", "Can I pay with shopping?"],
        "correctAnswerItalian": "Si può pagare a bordo?",
        "correctAnswerEnglish": "Can I pay on board?",
        "feedback": {
            "correctItalian": "Giusto! In alcune città è possibile, in altre no.",
            "incorrectItalian": "Sbagliato. A bordo significa on board.",
            "correctEnglish": "Right! In some cities it is possible, in others not.",
            "incorrectEnglish": "Wrong. On board is a bordo."
        }
    },
    {
        "choicesItalian": ["Quanto dura il biglietto?", "Quanto dura il viaggio?", "Quanto dura la pioggia?", "Quanto dura la notte?"],
        "choicesEnglish": ["How long does the ticket last?", "How long does the journey last?", "How long does the rain last?", "How long does the night last?"],
        "correctAnswerItalian": "Quanto dura il biglietto?",
        "correctAnswerEnglish": "How long does the ticket last?",
        "feedback": {
            "correctItalian": "Ottimo! I biglietti urbani hanno spesso un limite di tempo.",
            "incorrectItalian": "No, dura significa lasts.",
            "correctEnglish": "Great! Urban tickets often have a time limit.",
            "incorrectEnglish": "No, lasts is dura."
        }
    },
    {
        "choicesItalian": ["Deve timbrare il biglietto.", "Deve mangiare il biglietto.", "Deve perdere il biglietto.", "Deve vendere il biglietto."],
        "choicesEnglish": ["You must validate/stamp the ticket.", "You must eat the ticket.", "You must lose the ticket.", "You must sell the ticket."],
        "correctAnswerItalian": "Deve timbrare il biglietto.",
        "correctAnswerEnglish": "You must validate/stamp the ticket.",
        "feedback": {
            "correctItalian": "Esatto! La convalida è obbligatoria.",
            "incorrectItalian": "No, timbrare significa to stamp/validate.",
            "correctEnglish": "Exactly! Validation is mandatory.",
            "incorrectEnglish": "No, to stamp/validate is timbrare."
        }
    },
    {
        "choicesItalian": ["Qual è la prossima fermata?", "Qual è la prossima festa?", "Qual è la prossima città?", "Qual è la prossima via?"],
        "choicesEnglish": ["What is the next stop?", "What is the next party?", "What is the next city?", "What is the next street?"],
        "correctAnswerItalian": "Qual è la prossima fermata?",
        "correctAnswerEnglish": "What is the next stop?",
        "feedback": {
            "correctItalian": "Giusto! Per non mancare la propria destinazione.",
            "incorrectItalian": "Sbagliato. Fermata significa stop.",
            "correctEnglish": "Right! To avoid missing your destination.",
            "incorrectEnglish": "Wrong. Stop is fermata."
        }
    },
    {
        "choicesItalian": ["C'è una fermata qui vicino?", "C'è una casa qui vicino?", "C'è una banca qui vicino?", "C'è una scuola qui vicino?"],
        "choicesEnglish": ["Is there a stop near here?", "Is there a house near here?", "Is there a bank near here?", "Is there a school near here?"],
        "correctAnswerItalian": "C'è una fermata qui vicino?",
        "correctAnswerEnglish": "Is there a stop near here?",
        "feedback": {
            "correctItalian": "Ottimo! Cercare il punto di imbarco.",
            "incorrectItalian": "No, vicino significa near.",
            "correctEnglish": "Great! Looking for the boarding point.",
            "incorrectEnglish": "No, near is vicino."
        }
    },
    {
        "choicesItalian": ["A che ora passa il prossimo?", "A che ora parte il treno?", "A che ora chiude il bar?", "A che ora inizia il film?"],
        "choicesEnglish": ["What time does the next one pass?", "What time does the train leave?", "What time does the bar close?", "What time does the movie start?"],
        "correctAnswerItalian": "A che ora passa il prossimo?",
        "correctAnswerEnglish": "What time does the next one pass?",
        "feedback": {
            "correctItalian": "Esatto! Chiedere la frequenza del servizio.",
            "incorrectItalian": "No, passa significa passes.",
            "correctEnglish": "Exactly! Asking for the service frequency.",
            "incorrectEnglish": "No, passes is passa."
        }
    },
    {
        "choicesItalian": ["È questo il bus per il centro?", "È questo il bus per il mare?", "È questo il bus per la montagna?", "È questo il bus per l'aeroporto?"],
        "choicesEnglish": ["Is this the bus to the center?", "Is this the bus to the sea?", "Is this the bus to the mountains?", "Is this the bus to the airport?"],
        "correctAnswerItalian": "È questo il bus per il centro?",
        "correctAnswerEnglish": "Is this the bus to the center?",
        "feedback": {
            "correctItalian": "Giusto! Verificare la direzione.",
            "incorrectItalian": "Sbagliato. Centro significa center.",
            "correctEnglish": "Right! Verifying the direction.",
            "incorrectEnglish": "Wrong. Center is centro."
        }
    },
    {
        "choicesItalian": ["Mi avvisa alla mia fermata?", "Mi saluta alla mia fermata?", "Mi sveglia alla mia fermata?", "Mi canta alla mia fermata?"],
        "choicesEnglish": ["Will you let me know at my stop?", "Will you say hello at my stop?", "Will you wake me up at my stop?", "Will you sing to me at my stop?"],
        "correctAnswerItalian": "Mi avvisa alla mia fermata?",
        "correctAnswerEnglish": "Will you let me know at my stop?",
        "feedback": {
            "correctItalian": "Ottimo! Chiedere un piccolo aiuto all'autista o a un passeggero.",
            "incorrectItalian": "No, avvisa significa warns/lets know.",
            "correctEnglish": "Great! Asking for a little help from the driver or a passenger.",
            "incorrectEnglish": "No, warns/lets know is avvisa."
        }
    },
    {
        "choicesItalian": ["Scendo alla prossima.", "Salgo alla prossima.", "Corro alla prossima.", "Dormo alla prossima."],
        "choicesEnglish": ["I'm getting off at the next one.", "I'm getting on at the next one.", "I'm running to the next one.", "I'm sleeping at the next one."],
        "correctAnswerItalian": "Scendo alla prossima.",
        "correctAnswerEnglish": "I'm getting off at the next one.",
        "feedback": {
            "correctItalian": "Esatto! Dichiarare l'intenzione di scendere.",
            "incorrectItalian": "No, scendo significa I'm getting off.",
            "correctEnglish": "Exactly! Declaring the intention to get off.",
            "incorrectEnglish": "No, I'm getting off is scendo."
        }
    },
    {
        "choicesItalian": ["L'autobus è molto affollato.", "L'autobus è molto vuoto.", "L'autobus è molto veloce.", "L'autobus è molto pulito."],
        "choicesEnglish": ["The bus is very crowded.", "The bus is very empty.", "The bus is very fast.", "The bus is very clean."],
        "correctAnswerItalian": "L'autobus è molto affollato.",
        "correctAnswerEnglish": "The bus is very crowded.",
        "feedback": {
            "correctItalian": "Giusto! Descrivere la situazione a bordo.",
            "incorrectItalian": "Sbagliato. Affollato significa crowded.",
            "correctEnglish": "Right! Describing the situation on board.",
            "incorrectEnglish": "Wrong. Crowded is affollato."
        }
    },
    {
        "choicesItalian": ["C'è uno sconto per studenti?", "C'è uno sconto per giganti?", "C'è uno sconto per cani?", "C'è uno sconto per turisti?"],
        "choicesEnglish": ["Is there a discount for students?", "Is there a discount for giants?", "Is there a discount for dogs?", "Is there a discount for tourists?"],
        "correctAnswerItalian": "C'è uno sconto per studenti?",
        "correctAnswerEnglish": "Is there a discount for students?",
        "feedback": {
            "correctItalian": "Ottimo! Utile per risparmiare sul viaggio.",
            "incorrectItalian": "No, studenti significa students.",
            "correctEnglish": "Great! Useful for saving on the journey.",
            "incorrectEnglish": "No, students is studenti."
        }
    },
    {
        "choicesItalian": ["Dove posso convalidare?", "Dove posso mangiare?", "Dove posso dormire?", "Dove posso ballare?"],
        "choicesEnglish": ["Where can I validate?", "Where can I eat?", "Where can I sleep?", "Where can I dance?"],
        "correctAnswerItalian": "Dove posso convalidare?",
        "correctAnswerEnglish": "Where can I validate?",
        "feedback": {
            "correctItalian": "Esatto! Cercare la macchinetta per il timbro.",
            "incorrectItalian": "No, convalidare significa validate.",
            "correctEnglish": "Exactly! Looking for the machine for the stamp.",
            "incorrectEnglish": "No, validate is convalidare."
        }
    },
    {
        "choicesItalian": ["L'autobus ha un ritardo.", "L'autobus ha un premio.", "L'autobus ha un colore.", "L'autobus ha un amico."],
        "choicesEnglish": ["The bus is delayed.", "The bus has a prize.", "The bus has a color.", "The bus has a friend."],
        "correctAnswerItalian": "L'autobus ha un ritardo.",
        "correctAnswerEnglish": "The bus is delayed.",
        "feedback": {
            "correctItalian": "Giusto! Una situazione comune nel trasporto pubblico.",
            "incorrectItalian": "Sbagliato. Ritardo significa delay.",
            "correctEnglish": "Right! A common situation in public transport.",
            "incorrectEnglish": "Wrong. Delay is ritardo."
        }
    },
    {
        "choicesItalian": ["Si siede lei?", "Si alza lei?", "Si corre lei?", "Si mangia lei?"],
        "choicesEnglish": ["Are you sitting down?", "Are you getting up?", "Are you running?", "Are you eating?"],
        "correctAnswerItalian": "Si siede lei?",
        "correctAnswerEnglish": "Are you sitting down?",
        "feedback": {
            "correctItalian": "Ottimo! Un gesto di cortesia verso un altro passeggero.",
            "incorrectItalian": "No, siede significa sits.",
            "correctEnglish": "Great! A gesture of courtesy towards another passenger.",
            "incorrectEnglish": "No, sits is siede."
        }
    }
]

new_sentences_bus = [
    {
        "choicesItalian": ["Mi scusi, può dirmi quando arriviamo in Piazza Navona?", "Mi scusi, può dirmi quando arriviamo sulla Luna?", "Mi scusi, può dirmi quando arriviamo a casa sua?", "Mi scusi, può dirmi quando arriviamo al mare?"],
        "choicesEnglish": ["Excuse me, can you tell me when we arrive at Piazza Navona?", "Excuse me, can you tell me when we arrive on the Moon?", "Excuse me, can you tell me when we arrive at your house?", "Excuse me, can you tell me when we arrive at the sea?"],
        "correctAnswerItalian": "Mi scusi, può dirmi quando arriviamo in Piazza Navona?",
        "correctAnswerEnglish": "Excuse me, can you tell me when we arrive at Piazza Navona?",
        "feedback": {
            "correctItalian": "Esatto! Una richiesta di aiuto molto comune per i turisti.",
            "incorrectItalian": "No, Piazza Navona è una celebre piazza di Roma.",
            "correctEnglish": "Exactly! A very common request for help from tourists.",
            "incorrectEnglish": "No, Piazza Navona is a famous square in Rome."
        }
    },
    {
        "choicesItalian": ["Deve timbrare il biglietto nella macchinetta gialla laggiù.", "Deve mangiare il biglietto nella macchinetta gialla laggiù.", "Deve perdere il biglietto nella macchinetta gialla laggiù.", "Deve vendere il biglietto nella macchinetta gialla laggiù."],
        "choicesEnglish": ["You must validate the ticket in the yellow machine over there.", "You must eat the ticket in the yellow machine over there.", "You must lose the ticket in the yellow machine over there.", "You must sell the ticket in the yellow machine over there."],
        "correctAnswerItalian": "Deve timbrare il biglietto nella macchinetta gialla laggiù.",
        "correctAnswerEnglish": "You must validate the ticket in the yellow machine over there.",
        "feedback": {
            "correctItalian": "Giusto! Le istruzioni per la convalida a bordo.",
            "incorrectItalian": "Sbagliato. Timbrare significa validate/stamp.",
            "correctEnglish": "Right! Instructions for validation on board.",
            "incorrectEnglish": "Wrong. To validate/stamp is timbrare."
        }
    },
    {
        "choicesItalian": ["Questo autobus va direttamente alla stazione ferroviaria?", "Questo autobus va direttamente in un altro pianeta?", "Questo autobus va direttamente a dormire?", "Questo autobus va direttamente in banca?"],
        "choicesEnglish": ["Does this bus go directly to the railway station?", "Does this bus go directly to another planet?", "Does this bus go directly to sleep?", "Does this bus go directly to the bank?"],
        "correctAnswerItalian": "Questo autobus va direttamente alla stazione ferroviaria?",
        "correctAnswerEnglish": "Does this bus go directly to the railway station?",
        "feedback": {
            "correctItalian": "Ottimo! Verificare se il bus è quello giusto per la stazione.",
            "incorrectItalian": "No, stazione ferroviaria significa railway station.",
            "correctEnglish": "Great! Verifying if the bus is the right one for the station.",
            "incorrectEnglish": "No, railway station is stazione ferroviaria."
        }
    },
    {
        "choicesItalian": ["C'è molta gente oggi, non riesco a trovare un posto a sedere.", "C'è molta acqua oggi, non riesco a trovare un posto a sedere.", "C'è molta musica oggi, non riesco a trovare un posto a sedere.", "C'è molta neve oggi, non riesco a trovare un posto a sedere."],
        "choicesEnglish": ["There are many people today, I can't find a seat.", "There is a lot of water today, I can't find a seat.", "There is a lot of music today, I can't find a seat.", "There is a lot of snow today, I can't find a seat."],
        "correctAnswerItalian": "C'è molta gente oggi, non riesco a trovare un posto a sedere.",
        "correctAnswerEnglish": "There are many people today, I can't find a seat.",
        "feedback": {
            "correctItalian": "Esatto! Descrivere il disagio dell'affollamento.",
            "incorrectItalian": "No, gente significa people.",
            "correctEnglish": "Exactly! Describing the discomfort of crowding.",
            "incorrectEnglish": "No, people is gente."
        }
    },
    {
        "choicesItalian": ["Scusi, è libera questa sedia o è occupata?", "Scusi, è libera questa strada o è occupata?", "Scusi, è libera questa città o è occupata?", "Scusi, è libera questa vita o è occupata?"],
        "choicesEnglish": ["Excuse me, is this seat free or is it occupied?", "Excuse me, is this street free or is it occupied?", "Excuse me, is this city free or is it occupied?", "Excuse me, is this life free or is it occupied?"],
        "correctAnswerItalian": "Scusi, è libera questa sedia o è occupata?",
        "correctAnswerEnglish": "Excuse me, is this seat free or is it occupied?",
        "feedback": {
            "correctItalian": "Giusto! Chiedere prima di sedersi accanto a qualcuno.",
            "incorrectItalian": "Sbagliato. Libera significa free/available.",
            "correctEnglish": "Right! Asking before sitting next to someone.",
            "incorrectEnglish": "Wrong. Free/available is libera."
        }
    },
    {
        "choicesItalian": ["L'autista ha detto che dobbiamo scendere alla prossima fermata.", "L'autista ha detto che dobbiamo ballare alla prossima fermata.", "L'autista ha detto che dobbiamo cantare alla prossima fermata.", "L'autista ha detto che dobbiamo dormire alla prossima fermata."],
        "choicesEnglish": ["The driver said we have to get off at the next stop.", "The driver said we have to dance at the next stop.", "The driver said we have to sing at the next stop.", "The driver said we have to sleep at the next stop."],
        "correctAnswerItalian": "L'autobus ha detto che dobbiamo scendere alla prossima fermata.",
        "correctAnswerEnglish": "The driver said we have to get off at the next stop.",
        "feedback": {
            "correctItalian": "Ottimo! Riportare un'indicazione ricevuta dall'autista.",
            "incorrectItalian": "No, scendere significa to get off.",
            "correctEnglish": "Great! Reporting an instruction received from the driver.",
            "incorrectEnglish": "No, to get off is scendere."
        }
    },
    {
        "choicesItalian": ["Quanto costa l'abbonamento mensile per i trasporti urbani?", "Quanto costa l'abbonamento mensile per i viaggi spaziali?", "Quanto costa l'abbonamento mensile per i film?", "Quanto costa l'abbonamento mensile per la palestra?"],
        "choicesEnglish": ["How much is the monthly pass for urban transport?", "How much is the monthly pass for space travel?", "How much is the monthly pass for movies?", "How much is the monthly pass for the gym?"],
        "correctAnswerItalian": "Quanto costa l'abbonamento mensile per i trasporti urbani?",
        "correctAnswerEnglish": "How much is the monthly pass for urban transport?",
        "feedback": {
            "correctItalian": "Esatto! Chiedere il prezzo per un uso prolungato.",
            "incorrectItalian": "No, abbonamento mensile significa monthly pass.",
            "correctEnglish": "Exactly! Asking for the price for extended use.",
            "incorrectEnglish": "No, monthly pass is abbonamento mensile."
        }
    },
    {
        "choicesItalian": ["Attenzione, l'autobus sta per partire, tenetevi forte!", "Attenzione, l'autobus sta per volare, tenetevi forte!", "Attenzione, l'autobus sta per dormire, tenetevi forte!", "Attenzione, l'autobus sta per mangiare, tenetevi forte!"],
        "choicesEnglish": ["Watch out, the bus is about to leave, hold on tight!", "Watch out, the bus is about to fly, hold on tight!", "Watch out, the bus is about to sleep, hold on tight!", "Watch out, the bus is about to eat, hold on tightl!"],
        "correctAnswerItalian": "Attenzione, l'autobus sta per partire, tenetevi forte!",
        "correctAnswerEnglish": "Watch out, the bus is about to leave, hold on tight!",
        "feedback": {
            "correctItalian": "Giusto! Un avviso importante per la sicurezza dei passeggeri.",
            "incorrectItalian": "Sbagliato. Partire significa leave/start.",
            "correctEnglish": "Right! An important warning for passenger safety.",
            "incorrectEnglish": "Wrong. To leave/start is partire."
        }
    },
    {
        "choicesItalian": ["Il biglietto vale novanta minuti dalla prima convalida.", "Il biglietto vale novanta anni dalla prima convalida.", "Il biglietto vale novanta giorni dalla prima convalida.", "Il biglietto vale novanta secondi dalla prima convalida."],
        "choicesEnglish": ["The ticket is valid for ninety minutes from the first validation.", "The ticket is valid for ninety years from the first validation.", "The ticket is valid for ninety days from the first validation.", "The ticket is valid for ninety seconds from the first validation."],
        "correctAnswerItalian": "Il biglietto vale novanta minuti dalla prima convalida.",
        "correctAnswerEnglish": "The ticket is valid for ninety minutes from the first validation.",
        "feedback": {
            "correctItalian": "Ottimo! Una regola fondamentale per l'uso dei biglietti a tempo.",
            "incorrectItalian": "No, vale novanta minuti.",
            "correctEnglish": "Great! A fundamental rule for the use of timed tickets.",
            "incorrectEnglish": "No, it's valid for ninety minutes."
        }
    },
    {
        "choicesItalian": ["Per favore, può aprire la porta posteriore del bus?", "Per favore, può aprire la porta del frigorifero?", "Per favore, può aprire la porta di casa sua?", "Per favore, può aprire la porta del paradiso?"],
        "choicesEnglish": ["Please, can you open the rear door of the bus?", "Please, can you open the refrigerator door?", "Please, can you open the door of your house?", "Please, can you open the door to paradise?"],
        "correctAnswerItalian": "Per favore, può aprire la porta posteriore del bus?",
        "correctAnswerEnglish": "Please, can you open the rear door of the bus?",
        "feedback": {
            "correctItalian": "Esatto! Chiedere all'autista di farci scendere se la porta è chiusa.",
            "incorrectItalian": "No, porta posteriore significa rear door.",
            "correctEnglish": "Exactly! Asking the driver to let us off if the door is closed.",
            "incorrectEnglish": "No, rear door is porta posteriore."
        }
    },
    {
        "choicesItalian": ["L'autobus numero sessantaquattro è sempre molto pieno di turisti.", "L'autobus numero sessantaquattro è sempre molto pieno di fiori.", "L'autobus numero sessantaquattro è sempre molto pieno di acqua.", "L'autobus numero sessantaquattro è sempre molto pieno di sogni."],
        "choicesEnglish": ["Bus number 64 is always very full of tourists.", "Bus number 64 is always very full of flowers.", "Bus number 64 is always very full of water.", "Bus number 64 is always very full of dreams."],
        "correctAnswerItalian": "L'autobus numero sessantaquattro è sempre molto pieno di turisti.",
        "correctAnswerEnglish": "Bus number 64 is always very full of tourists.",
        "feedback": {
            "correctItalian": "Giusto! Un'osservazione su una linea celebre per il suo affollamento.",
            "incorrectItalian": "Sbagliato. Turisti significa tourists.",
            "correctEnglish": "Right! An observation on a line famous for its crowding.",
            "incorrectEnglish": "Wrong. Tourists is turisti."
        }
    },
    {
        "choicesItalian": ["Devo cambiare autobus alla prossima fermata per andare al Colosseo.", "Devo cambiare vita alla prossima fermata per andare al Colosseo.", "Devo cambiare casa alla prossima fermata per andare al Colosseo.", "Devo cambiare colore alla prossima fermata per andare al Colosseo."],
        "choicesEnglish": ["I have to change buses at the next stop to go to the Colosseum.", "I have to change my life at the next stop to go to the Colosseum.", "I have to change houses at the next stop to go to the Colosseum.", "I have to change colors at the next stop to go to the Colosseum."],
        "correctAnswerItalian": "Devo cambiare autobus alla prossima fermata per andare al Colosseo.",
        "correctAnswerEnglish": "I have to change buses at the next stop to go to the Colosseum.",
        "feedback": {
            "correctItalian": "Ottimo! Pianificare un cambio di linea per raggiungere la meta.",
            "incorrectItalian": "No, cambiare autobus significa change buses.",
            "correctEnglish": "Great! Planning a line change to reach the destination.",
            "incorrectEnglish": "No, to change buses is cambiare autobus."
        }
    },
    {
        "choicesItalian": ["Scusi, sa se questa linea passa vicino alla fontana di Trevi?", "Scusi, sa se questa linea passa vicino al polo nord?", "Scusi, sa se questa linea passa vicino al sole?", "Scusi, sa se questa linea passa vicino al sottomarino?"],
        "choicesEnglish": ["Excuse me, do you know if this line passes near the Trevi Fountain?", "Excuse me, do you know if this line passes near the North Pole?", "Excuse me, do you know if this line passes near the sun?", "Excuse me, do you know if this line passes near the submarine?"],
        "correctAnswerItalian": "Scusi, sa se questa linea passa vicino alla fontana di Trevi?",
        "correctAnswerEnglish": "Excuse me, do you know if this line passes near the Trevi Fountain?",
        "feedback": {
            "correctItalian": "Esatto! Chiedere informazioni su un monumento famoso.",
            "incorrectItalian": "No, Fontana di Trevi è un monumento iconico di Roma.",
            "correctEnglish": "Exactly! Asking for information about a famous monument.",
            "incorrectEnglish": "No, Trevi Fountain is an iconic monument in Rome."
        }
    },
    {
        "choicesItalian": ["Il controllore sta controllando i biglietti di tutti i passeggeri.", "Il controllore sta mangiando i biglietti di tutti i passeggeri.", "Il controllore sta perdendo i biglietti di tutti i passeggeri.", "Il controllore sta sognando i biglietti di tutti i passeggeri."],
        "choicesEnglish": ["The inspector is checking everyone's tickets.", "The inspector is eating everyone's tickets.", "The inspector is losing everyone's tickets.", "The inspector is dreaming about everyone's tickets."],
        "correctAnswerItalian": "Il controllore sta controllando i biglietti di tutti i passeggeri.",
        "correctAnswerEnglish": "The inspector is checking everyone's tickets.",
        "feedback": {
            "correctItalian": "Giusto! Un momento di tensione se non si ha il biglietto timbrato.",
            "incorrectItalian": "Sbagliato. Controllore significa inspector.",
            "correctEnglish": "Right! A moment of tension if you don't have a stamped ticket.",
            "incorrectEnglish": "Wrong. Inspector is controllore."
        }
    },
    {
        "choicesItalian": ["Mi dispiace, ma non ci sono più biglietti disponibili in questa tabaccheria.", "Mi dispiace, ma non ci sono più sogni disponibili in questa tabaccheria.", "Mi dispiace, ma non ci sono più amici disponibili in questa tabaccheria.", "Mi dispiace, ma non ci sono più colori disponibili in questa tabaccheria."],
        "choicesEnglish": ["I'm sorry, but there are no more tickets available in this shop.", "I'm sorry, but there are no more dreams available in this shop.", "I'm sorry, but there are no more friends available in this shop.", "I'm sorry, but there are no more colors available in this shop."],
        "correctAnswerItalian": "Mi dispiace, ma non ci sono più biglietti disponibili in questa tabaccheria.",
        "correctAnswerEnglish": "I'm sorry, but there are no more tickets available in this shop.",
        "feedback": {
            "correctItalian": "Ottimo! Una risposta negativa che richiede di cercare altrove.",
            "incorrectItalian": "No, biglietti disponibili significa tickets available.",
            "correctEnglish": "Great! A negative response that requires looking elsewhere.",
            "incorrectEnglish": "No, tickets available is biglietti disponibili."
        }
    },
    {
        "choicesItalian": ["Ho perso il portafoglio sull'autobus, cosa devo fare ora?", "Ho perso la testa sull'autobus, cosa devo fare ora?", "Ho perso la strada sull'autobus, cosa devo fare ora?", "Ho perso il tempo sull'autobus, cosa devo fare ora?"],
        "choicesEnglish": ["I lost my wallet on the bus, what should I do now?", "I lost my head on the bus, what should I do now?", "I lost my way on the bus, what should I do now?", "I lost time on the bus, what should I do now?"],
        "correctAnswerItalian": "Ho perso il portafoglio sull'autobus, cosa devo fare ora?",
        "correctAnswerEnglish": "I lost my wallet on the bus, what should I do now?",
        "feedback": {
            "correctItalian": "Esatto! Una situazione di emergenza molto spiacevole.",
            "incorrectItalian": "No, portafoglio significa wallet.",
            "correctEnglish": "Exactly! A very unpleasant emergency situation.",
            "incorrectEnglish": "No, wallet is portafoglio."
        }
    },
    {
        "choicesItalian": ["Si sieda pure, io scendo alla prossima fermata del bus.", "Si sogni pure, io scendo alla prossima fermata del bus.", "Si mangi pure, io scendo alla prossima fermata del bus.", "Si vesta pure, io scendo alla prossima fermata del bus."],
        "choicesEnglish": ["Please sit down, I'm getting off at the next bus stop.", "Please dream away, I'm getting off at the next bus stop.", "Please eat away, I'm getting off at the next bus stop.", "Please get dressed, I'm getting off at the next bus stop."],
        "correctAnswerItalian": "Si sieda pure, io scendo alla prossima fermata del bus.",
        "correctAnswerEnglish": "Please sit down, I'm getting off at the next bus stop.",
        "feedback": {
            "correctItalian": "Giusto! Un modo cortese per offrire il proprio posto.",
            "incorrectItalian": "Sbagliato. Sieda significa sit (imperative/formal).",
            "correctEnglish": "Right! A polite way to offer one's seat.",
            "incorrectEnglish": "Wrong. Sit is sieda."
        }
    },
    {
        "choicesItalian": ["Sa se questo autobus ferma davanti all'ingresso dell'aeroporto?", "Sa se questo autobus ferma sul tetto dell'aeroporto?", "Sa se questo autobus ferma dentro l'aeroporto?", "Sa se questo autobus ferma lontano dall'aeroporto?"],
        "choicesEnglish": ["Do you know if this bus stops in front of the airport entrance?", "Do you know if this bus stops on the airport roof?", "Do you know if this bus stops inside the airport?", "Do you know if this bus stops far from the airport?"],
        "correctAnswerItalian": "Sa se questo autobus ferma davanti all'ingresso dell'aeroporto?",
        "correctAnswerEnglish": "Do you know if this bus stops in front of the airport entrance?",
        "feedback": {
            "correctItalian": "Ottimo! Chiedere conferma sulla fermata esatta per l'aeroporto.",
            "incorrectItalian": "No, ingresso dell'aeroporto significa airport entrance.",
            "correctEnglish": "Great! Asking for confirmation on the exact stop for the airport.",
            "incorrectEnglish": "No, airport entrance is ingresso dell'aeroporto."
        }
    },
    {
        "choicesItalian": ["C'è uno sciopero dei trasporti pubblici previsto per domani?", "C'è una festa dei trasporti pubblici prevista per domani?", "C'è un viaggio dei trasporti pubblici previsto per domani?", "C'è un regalo dei trasporti pubblici previsto per domani?"],
        "choicesEnglish": ["Is there a public transport strike planned for tomorrow?", "Is there a public transport party planned for tomorrow?", "Is there a public transport journey planned for tomorrow?", "Is there a public transport gift planned for tomorrow?"],
        "correctAnswerItalian": "C'è uno sciopero dei trasporti pubblici previsto per domani?",
        "correctAnswerEnglish": "Is there a public transport strike planned for tomorrow?",
        "feedback": {
            "correctItalian": "Esatto! Un'informazione cruciale per evitare disagi.",
            "incorrectItalian": "No, sciopero significa strike.",
            "correctEnglish": "Exactly! Crucial information to avoid inconvenience.",
            "incorrectEnglish": "No, strike is sciopero."
        }
    },
    {
        "choicesItalian": ["Grazie mille per l'aiuto, è stato molto gentile con me.", "Grazie mille per il pane, è stato molto buono con me.", "Grazie mille per il sogni, è stato molto bello con me.", "Grazie mille per il colori, è stato molto forte con me."],
        "choicesEnglish": ["Thank you very much for the help, you were very kind to me.", "Thank you very much for the bread, it was very good with me.", "Thank you very much for the dreams, they were very beautiful with me.", "Thank you very much for the colors, they were very strong with me."],
        "correctAnswerItalian": "Grazie mille per l'aiuto, è stato molto gentile con me.",
        "correctAnswerEnglish": "Thank you very much for the help, you were very kind to me.",
        "feedback": {
            "correctItalian": "Giusto! Un ringraziamento finale dopo aver ricevuto assistenza.",
            "incorrectItalian": "Sbagliato. Gentile significa kind.",
            "correctEnglish": "Right! A final thanks after receiving assistance.",
            "incorrectEnglish": "No, kind is gentile."
        }
    }
]

file_p = 'src/data/exports/travel/bus_ticket/travel_bus_ticket_phrases.json'
file_s = 'src/data/exports/travel/bus_ticket/travel_bus_ticket_sentences.json'

new_p_len = expand_dataset(file_p, new_phrases_bus)
new_s_len = expand_dataset(file_s, new_sentences_bus)

print(f'New lengths for bus_ticket: phrases={new_p_len}, sentences={new_s_len}')
