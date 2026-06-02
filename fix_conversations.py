import json

file_path = '/home/waseageru/parli-italiano/src/data/exports/culture/museum_tickets/conversations.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Improvements for buying_two_tickets
data['conversations'][0]['messages'][0]['choices'][1] = { "text": "Buongiorno, dove posso comprare una guida?", "english": "Good morning, where can I buy a guide?", "isCorrect": False, "feedback": "Off topic." }
data['conversations'][0]['messages'][0]['choices'][2] = { "text": "Buongiorno, c'è una mostra temporanea oggi?", "english": "Good morning, is there a temporary exhibition today?", "isCorrect": False, "feedback": "Off topic." }

data['conversations'][0]['messages'][1]['choices'][1] = { "text": "Vorrei prenotare un tavolo, grazie.", "english": "I would like to book a table, thank you.", "isCorrect": False, "feedback": "Wrong location." }
data['conversations'][0]['messages'][1]['choices'][2] = { "text": "Vorrei pagare con la carta, grazie.", "english": "I would like to pay by card, thank you.", "isCorrect": False, "feedback": "Too early." }

data['conversations'][0]['messages'][2]['choices'][1] = { "text": "Sì, grazie. Dov'è l'uscita?", "english": "Yes, thank you. Where is the exit?", "isCorrect": False, "feedback": "Irrelevant." }
data['conversations'][0]['messages'][2]['choices'][2] = { "text": "Sì, grazie. Quanto costa?", "english": "Yes, thank you. How much does it cost?", "isCorrect": False, "feedback": "Wait for info." }

data['conversations'][0]['messages'][3]['choices'][1] = { "text": "Va bene, dove sono le sale?", "english": "All right, where are the rooms?", "isCorrect": False, "feedback": "Answer the question first." }
data['conversations'][0]['messages'][3]['choices'][2] = { "text": "Va bene, preferisco di no.", "english": "All right, I prefer not.", "isCorrect": False, "feedback": "Refused exhibition." }

data['conversations'][0]['messages'][4]['choices'][1] = { "text": "Sì, una guida è molto utile, grazie.", "english": "Yes, a guide is very useful, thank you.", "isCorrect": False, "feedback": "Asking for guide instead." }
data['conversations'][0]['messages'][4]['choices'][2] = { "text": "Sì, l'audioguida è utile, grazie.", "english": "Yes, the audio guide is useful, thank you.", "isCorrect": False, "feedback": "Asking for audio guide instead." }

data['conversations'][0]['messages'][5]['choices'][1] = { "text": "Pago in contanti alla cassa, grazie.", "english": "I'll pay in cash at the cash desk, thank you.", "isCorrect": False, "feedback": "Wait for instructions." }
data['conversations'][0]['messages'][5]['choices'][2] = { "text": "Pago tutto insieme adesso, grazie.", "english": "I'll pay all together now, thank you.", "isCorrect": False, "feedback": "Redundant." }

data['conversations'][0]['messages'][6]['choices'][1] = { "text": "Certo, un momento.", "english": "Sure, one moment.", "isCorrect": False, "feedback": "Action not done yet." }
data['conversations'][0]['messages'][6]['choices'][2] = { "text": "Certo, arrivo ora.", "english": "Sure, I'm coming now.", "isCorrect": False, "feedback": "Nonsense here." }

data['conversations'][0]['messages'][7]['choices'][1] = { "text": "Grazie mille. Dove posso lasciare la borsa?", "english": "Thank you very much. Where can I leave the bag?", "isCorrect": False, "feedback": "Off topic." }
data['conversations'][0]['messages'][7]['choices'][2] = { "text": "Grazie mille. Posso fare delle fotografie?", "english": "Thank you very much. Can I take photographs?", "isCorrect": False, "feedback": "Off topic." }

data['conversations'][0]['messages'][8]['choices'][1] = { "text": "Capito. Grazie e buona giornata!", "english": "Understood. Thanks and have a good day!", "isCorrect": False, "feedback": "You should leave now." }
data['conversations'][0]['messages'][8]['choices'][2] = { "text": "Capito. Grazie e a più tardi!", "english": "Understood. Thanks and see you later!", "isCorrect": False, "feedback": "You should leave now." }

data['conversations'][0]['messages'][9]['choices'][1] = { "text": "A domani!", "english": "See you tomorrow!", "isCorrect": False, "feedback": "Wrong time." }
data['conversations'][0]['messages'][9]['choices'][2] = { "text": "Buonasera!", "english": "Good evening!", "isCorrect": False, "feedback": "A bit early." }

# Improvements for asking_for_student_discount
data['conversations'][1]['messages'][0]['choices'][1] = { "text": "Buongiorno. Posso avere una mappa gratuita?", "english": "Good morning. Can I have a free map?", "isCorrect": False, "feedback": "Off topic." }
data['conversations'][1]['messages'][0]['choices'][2] = { "text": "Buongiorno. A che ora apre la galleria?", "english": "Good morning. What time does the gallery open?", "isCorrect": False, "feedback": "Off topic." }

data['conversations'][1]['messages'][1]['choices'][1] = { "text": "Sono con un gruppo, ci sono delle riduzioni?", "english": "I am with a group, are there any reductions?", "isCorrect": False, "feedback": "Wrong role." }
data['conversations'][1]['messages'][1]['choices'][2] = { "text": "Sono un residente, ho diritto allo sconto?", "english": "I am a resident, am I entitled to the discount?", "isCorrect": False, "feedback": "Wrong role." }

data['conversations'][1]['messages'][2]['choices'][1] = { "text": "Perfetto, sono ancora studente.", "english": "Perfect, I am still a student.", "isCorrect": False, "feedback": "Redundant." }
data['conversations'][1]['messages'][2]['choices'][2] = { "text": "Perfetto, ecco i miei documenti.", "english": "Perfect, here are my documents.", "isCorrect": False, "feedback": "Wait for request." }

data['conversations'][1]['messages'][3]['choices'][1] = { "text": "Va bene il mio passaporto per lo sconto?", "english": "Is my passport okay for the discount?", "isCorrect": False, "feedback": "Wrong document." }
data['conversations'][1]['messages'][3]['choices'][2] = { "text": "Ho dimenticato il mio documento a casa.", "english": "I forgot my document at home.", "isCorrect": False, "feedback": "No discount then." }

data['conversations'][1]['messages'][4]['choices'][1] = { "text": "Certo, un momento solo.", "english": "Sure, just a moment.", "isCorrect": False, "feedback": "Not shown yet." }
data['conversations'][1]['messages'][4]['choices'][2] = { "text": "Sì, lo cerco subito.", "english": "Yes, I'll look for it right away.", "isCorrect": False, "feedback": "Not shown yet." }

data['conversations'][1]['messages'][5]['choices'][1] = { "text": "Bene! Posso pagare?", "english": "Good! Can I pay?", "isCorrect": False, "feedback": "Wait." }
data['conversations'][1]['messages'][5]['choices'][2] = { "text": "Ottimo! Ecco i soldi.", "english": "Great! Here is the money.", "isCorrect": False, "feedback": "Wait." }

data['conversations'][1]['messages'][6]['choices'][1] = { "text": "No, preferisco andare da solo, grazie.", "english": "No, I prefer to go alone, thank you.", "isCorrect": False, "feedback": "Answer the question." }
data['conversations'][1]['messages'][6]['choices'][2] = { "text": "No, ho già una mappa del museo, grazie.", "english": "No, I already have a museum map, thank you.", "isCorrect": False, "feedback": "Redundant." }

data['conversations'][1]['messages'][7]['choices'][1] = { "text": "Grazie. Posso usare questo biglietto domani?", "english": "Thanks. Can I use this ticket tomorrow?", "isCorrect": False, "feedback": "Off topic." }
data['conversations'][1]['messages'][7]['choices'][2] = { "text": "Grazie. Dove posso trovare una guida gratuita?", "english": "Thanks. Where can I find a free guide?", "isCorrect": False, "feedback": "Off topic." }

data['conversations'][1]['messages'][8]['choices'][1] = { "text": "Perfetto, allora ho tempo per vedere tutto.", "english": "Perfect, then I have time to see everything.", "isCorrect": False, "feedback": "Redundant." }
data['conversations'][1]['messages'][8]['choices'][2] = { "text": "Perfetto, allora posso fare molte foto.", "english": "Perfect, then I can take many photos.", "isCorrect": False, "feedback": "Off topic." }

data['conversations'][1]['messages'][9]['choices'][1] = { "text": "Grazie, buona giornata!", "english": "Thanks, have a good day!", "isCorrect": False, "feedback": "Wait for final bye." }
data['conversations'][1]['messages'][9]['choices'][2] = { "text": "Grazie, a presto!", "english": "Thanks, see you soon!", "isCorrect": False, "feedback": "Wait for final bye." }

# Improvements for renting_an_audio_guide
data['conversations'][2]['messages'][0]['choices'][1] = { "text": "Sì, ho già fatto la prenotazione ieri.", "english": "Yes, I already made the reservation yesterday.", "isCorrect": False, "feedback": "Redundant." }
data['conversations'][2]['messages'][0]['choices'][2] = { "text": "Sì, ho già visitato la mostra principale.", "english": "Yes, I already visited the main exhibition.", "isCorrect": False, "feedback": "Then why are you here?" }

data['conversations'][2]['messages'][1]['choices'][1] = { "text": "Vorrei una mappa del museo, grazie.", "english": "I would like a map of the museum, thank you.", "isCorrect": False, "feedback": "Wrong request." }
data['conversations'][2]['messages'][1]['choices'][2] = { "text": "Vorrei un biglietto intero, per favore.", "english": "I would like a full price ticket, please.", "isCorrect": False, "feedback": "You already have it." }

data['conversations'][2]['messages'][2]['choices'][1] = { "text": "La preferisco in italiano, per favore.", "english": "I prefer it in Italian, please.", "isCorrect": False, "feedback": "Are you learning?" }
data['conversations'][2]['messages'][2]['choices'][2] = { "text": "La preferisco in spagnolo, se possibile.", "english": "I prefer it in Spanish, if possible.", "isCorrect": False, "feedback": "Wrong language choice." }

data['conversations'][2]['messages'][3]['choices'][1] = { "text": "Va bene. Devo pagare adesso in contanti?", "english": "All right. Do I have to pay now in cash?", "isCorrect": False, "feedback": "Wait for payment info." }
data['conversations'][2]['messages'][3]['choices'][2] = { "text": "Va bene. Devo compilare un modulo qui?", "english": "All right. Do I have to fill out a form here?", "isCorrect": False, "feedback": "Off topic." }

data['conversations'][2]['messages'][4]['choices'][1] = { "text": "Ecco il mio passaporto europeo. Va bene?", "english": "Here is my European passport. Is it okay?", "isCorrect": False, "feedback": "Different document." }
data['conversations'][2]['messages'][4]['choices'][2] = { "text": "Ecco il mio tesserino studente. Va bene?", "english": "Here is my student card. Is it okay?", "isCorrect": False, "feedback": "Wrong document for deposit." }

data['conversations'][2]['messages'][5]['choices'][1] = { "text": "Grazie. Dove posso trovare le spiegazioni?", "english": "Thanks. Where can I find the explanations?", "isCorrect": False, "feedback": "In the guide." }
data['conversations'][2]['messages'][5]['choices'][2] = { "text": "Grazie. Quanto dura la visita guidata?", "english": "Thanks. How long does the guided visit last?", "isCorrect": False, "feedback": "No guided visit." }

data['conversations'][2]['messages'][6]['choices'][1] = { "text": "Capito. Posso cambiare la lingua dell'audioguida?", "english": "Understood. Can I change the language of the audio guide?", "isCorrect": False, "feedback": "You already chose it." }
data['conversations'][2]['messages'][6]['choices'][2] = { "text": "Capito. Posso andare in tutte le sale del museo?", "english": "Understood. Can I go to all the museum rooms?", "isCorrect": False, "feedback": "Off topic." }

data['conversations'][2]['messages'][7]['choices'][1] = { "text": "Ottimo. Devo pagare un deposito cauzionale oggi?", "english": "Great. Do I have to pay a security deposit today?", "isCorrect": False, "feedback": "Document is the deposit." }
data['conversations'][2]['messages'][7]['choices'][2] = { "text": "Ottimo. Devo mostrare di nuovo il mio documento?", "english": "Great. Do I have to show my document again?", "isCorrect": False, "feedback": "They have it." }

data['conversations'][2]['messages'][8]['choices'][1] = { "text": "Va bene, grazie mille per le informazioni.", "english": "All right, thanks a lot for the information.", "isCorrect": False, "feedback": "Not helpful enough." }
data['conversations'][2]['messages'][8]['choices'][2] = { "text": "Va bene, grazie mille e buona giornata.", "english": "All right, thanks a lot and have a good day.", "isCorrect": False, "feedback": "You are leaving." }

data['conversations'][2]['messages'][9]['choices'][1] = { "text": "Arrivederci e a presto!", "english": "Goodbye and see you soon!", "isCorrect": False, "feedback": "A bit informal." }
data['conversations'][2]['messages'][9]['choices'][2] = { "text": "Arrivederci e buona visita!", "english": "Goodbye and have a good visit!", "isCorrect": False, "feedback": "You are the visitor." }

# Improvements for checking_closing_time
data['conversations'][3]['messages'][0]['choices'][1] = { "text": "Sì, ma prima vorrei vedere i prezzi.", "english": "Yes, but first I would like to see the prices.", "isCorrect": False, "feedback": "Off topic." }
data['conversations'][3]['messages'][0]['choices'][2] = { "text": "Sì, ma prima vorrei una mappa gratuita.", "english": "Yes, but first I would like a free map.", "isCorrect": False, "feedback": "Off topic." }

data['conversations'][3]['messages'][1]['choices'][1] = { "text": "A che ora apre la biglietteria domani?", "english": "What time does the ticket office open tomorrow?", "isCorrect": False, "feedback": "Ask about today." }
data['conversations'][3]['messages'][1]['choices'][2] = { "text": "A che ora inizia l'ultima visita guidata?", "english": "What time does the last guided visit start?", "isCorrect": False, "feedback": "Off topic." }

data['conversations'][3]['messages'][2]['choices'][1] = { "text": "Ho solo due ore. Posso visitare anche la mostra?", "english": "I only have two hours. Can I also visit the exhibition?", "isCorrect": False, "feedback": "Too much for 2h." }
data['conversations'][3]['messages'][2]['choices'][2] = { "text": "Ho solo due ore. Devo comprare un altro biglietto?", "english": "I only have two hours. Do I have to buy another ticket?", "isCorrect": False, "feedback": "Wait." }

data['conversations'][3]['messages'][3]['choices'][1] = { "text": "Capito. E domani ci sono riduzioni?", "english": "Understood. And tomorrow are there reductions?", "isCorrect": False, "feedback": "Off topic." }
data['conversations'][3]['messages'][3]['choices'][2] = { "text": "Capito. E domani è aperto tutto il giorno?", "english": "Understood. And tomorrow is it open all day?", "isCorrect": False, "feedback": "Ask about opening time." }

data['conversations'][3]['messages'][4]['choices'][1] = { "text": "Se compro il biglietto ora, posso entrare subito?", "english": "If I buy the ticket now, can I enter immediately?", "isCorrect": False, "feedback": "Yes, but ask about tomorrow." }
data['conversations'][3]['messages'][4]['choices'][2] = { "text": "Se compro il biglietto ora, ho diritto allo sconto?", "english": "If I buy the ticket now, am I entitled to the discount?", "isCorrect": False, "feedback": "Off topic." }

data['conversations'][3]['messages'][5]['choices'][1] = { "text": "Questa è un'ottima notizia! Allora torno domani mattina.", "english": "This is great news! Then I'll come back tomorrow morning.", "isCorrect": False, "feedback": "Buy it now." }
data['conversations'][3]['messages'][5]['choices'][2] = { "text": "Questa è un'ottima notizia! Allora prendo due biglietti.", "english": "This is great news! Then I'll take two tickets.", "isCorrect": False, "feedback": "Only one." }

data['conversations'][3]['messages'][6]['choices'][1] = { "text": "No, per oggi preferisco fare una passeggiata.", "english": "No, for today I prefer to go for a walk.", "isCorrect": False, "feedback": "You are at the museum." }
data['conversations'][3]['messages'][6]['choices'][2] = { "text": "No, per oggi non ho abbastanza tempo, grazie.", "english": "No, for today I don't have enough time, thank you.", "isCorrect": False, "feedback": "You just said 2h is enough." }

data['conversations'][3]['messages'][7]['choices'][1] = { "text": "Grazie mille. Dove posso trovare un bar?", "english": "Thank you very much. Where can I find a bar?", "isCorrect": False, "feedback": "Off topic." }
data['conversations'][3]['messages'][7]['choices'][2] = { "text": "Grazie mille. Posso portare la borsa?", "english": "Thank you very much. Can I bring the bag?", "isCorrect": False, "feedback": "Off topic." }

data['conversations'][3]['messages'][8]['choices'][1] = { "text": "Molto bene, allora entro. Buona giornata!", "english": "Very well, then I enter. Have a good day!", "isCorrect": False, "feedback": "Wait." }
data['conversations'][3]['messages'][8]['choices'][2] = { "text": "Molto bene, allora inizio la mia visita.", "english": "Very well, then I start my visit.", "isCorrect": False, "feedback": "Wait." }

data['conversations'][3]['messages'][9]['choices'][1] = { "text": "A presto!", "english": "See you soon!", "isCorrect": False, "feedback": "A bit informal." }
data['conversations'][3]['messages'][9]['choices'][2] = { "text": "A domani!", "english": "See you tomorrow!", "isCorrect": False, "feedback": "Wrong time." }

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
