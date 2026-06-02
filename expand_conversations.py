import json

def expand_conversations():
    file_path = 'src/data/exports/culture/live_music/conversations.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Conversation 1: Finding the Venue
    conv1 = data['conversations'][0]
    conv1['messages'].extend([
        {
            "id": "m6",
            "role": "host",
            "text": "Hai altro nelle tasche? Per favore, svuota tutto.",
            "english": "Do you have anything else in your pockets? Please, empty everything.",
            "choices": [
                {"text": "Ho solo le chiavi e il portafoglio qui.", "isCorrect": True, "feedback": "Cooperating with security check."},
                {"text": "Il mio gatto mangia solo croccantini piccoli.", "isCorrect": False, "feedback": "Pets are not allowed and irrelevant."},
                {"text": "Cerco un ombrello per la pioggia di domani.", "isCorrect": False, "feedback": "Stay in the security context."}
            ]
        },
        {
            "id": "m7",
            "role": "host",
            "text": "Va bene. Vuoi una mappa del locale?",
            "english": "Alright. Do you want a map of the venue?",
            "choices": [
                {"text": "Sì, grazie! È molto utile per orientarsi.", "isCorrect": True, "feedback": "Accepting the map."},
                {"text": "No, preferisco comprare un giornale sportivo.", "isCorrect": False, "feedback": "Focus on the venue map."},
                {"text": "Il treno per Napoli è già partito?", "isCorrect": False, "feedback": "Forbidden transportation talk."}
            ]
        },
        {
            "id": "m8",
            "role": "host",
            "text": "Prego. Ricorda che è vietato fumare all'interno.",
            "english": "You're welcome. Remember that smoking is forbidden inside.",
            "choices": [
                {"text": "Capito, grazie per l'informazione.", "isCorrect": True, "feedback": "Acknowledging the rules."},
                {"text": "Vorrei ordinare una camera con balcone.", "isCorrect": False, "feedback": "Hotel talk is forbidden."},
                {"text": "Il mio computer non si accende più oggi.", "isCorrect": False, "feedback": "Tech problems are irrelevant."}
            ]
        },
        {
            "id": "m9",
            "role": "host",
            "text": "Hai bisogno di sapere dove sono i bagni?",
            "english": "Do you need to know where the bathrooms are?",
            "choices": [
                {"text": "Sì, dove si trovano esattamente?", "isCorrect": True, "feedback": "Asking for directions to bathrooms."},
                {"text": "No, cerco una farmacia per lo sciroppo.", "isCorrect": False, "feedback": "Medical talk is forbidden."},
                {"text": "Il citofono del palazzo suona forte.", "isCorrect": False, "feedback": "Housing talk is forbidden."}
            ]
        },
        {
            "id": "m10",
            "role": "host",
            "text": "Sono in fondo a sinistra, vicino all'uscita.",
            "english": "They are at the back on the left, near the exit.",
            "choices": [
                {"text": "Grazie, vado subito a controllare. Buon concerto!", "isCorrect": True, "feedback": "Polite conclusion."},
                {"text": "Voglio prenotare un volo per la Sicilia.", "isCorrect": False, "feedback": "Travel talk is forbidden."},
                {"text": "Il frigo in cucina è completamente vuoto.", "isCorrect": False, "feedback": "Domestic talk is forbidden."}
            ]
        }
    ])

    # Conversation 2: Ordering Drinks
    conv2 = data['conversations'][1]
    conv2['messages'].extend([
        {
            "id": "m6",
            "role": "host",
            "text": "Vuoi anche qualcosa da mangiare? Abbiamo delle patatine.",
            "english": "Do you also want something to eat? We have some chips.",
            "choices": [
                {"text": "Sì, prendo un pacchetto di patatine, grazie.", "isCorrect": True, "feedback": "Ordering a snack."},
                {"text": "No, cerco un cuscino morbido per dormire.", "isCorrect": False, "feedback": "Lodging talk is forbidden."},
                {"text": "Il mio passaporto scade tra due mesi.", "isCorrect": False, "feedback": "Travel talk is forbidden."}
            ]
        },
        {
            "id": "m7",
            "role": "host",
            "text": "Ecco a te. Sono altri due euro per le patatine.",
            "english": "Here you go. It's two more euros for the chips.",
            "choices": [
                {"text": "Va bene, ecco i due euro. Grazie!", "isCorrect": True, "feedback": "Paying for snacks."},
                {"text": "Il citofono è rotto, non posso entrare.", "isCorrect": False, "feedback": "Housing talk is forbidden."},
                {"text": "Prendo un taxi per andare in centro città.", "isCorrect": False, "feedback": "Transportation talk is forbidden."}
            ]
        },
        {
            "id": "m8",
            "role": "host",
            "text": "Perfetto. Hai bisogno di un tovagliolo?",
            "english": "Perfect. Do you need a napkin?",
            "choices": [
                {"text": "Sì, per favore. Uno è sufficiente.", "isCorrect": True, "feedback": "Requesting a napkin."},
                {"text": "No, cerco la ricetta per la torta.", "isCorrect": False, "feedback": "Cooking talk is irrelevant."},
                {"text": "Il medico mi ha dato una medicina amara.", "isCorrect": False, "feedback": "Medical talk is forbidden."}
            ]
        },
        {
            "id": "m9",
            "role": "host",
            "text": "Ecco il tovagliolo. Attento, c'è molta gente al bar.",
            "english": "Here is the napkin. Careful, there are many people at the bar.",
            "choices": [
                {"text": "Sì, vedo. Mi sposto subito verso il palco.", "isCorrect": True, "feedback": "Moving to a less crowded area."},
                {"text": "Voglio prenotare una camera doppia, grazie.", "isCorrect": False, "feedback": "Hotel talk is forbidden."},
                {"text": "Il mio volo per Parigi è al gate quattro.", "isCorrect": False, "feedback": "Airport talk is forbidden."}
            ]
        },
        {
            "id": "m10",
            "role": "host",
            "text": "Ottima idea. Goditi la musica e la birra!",
            "english": "Great idea. Enjoy the music and the beer!",
            "choices": [
                {"text": "Grazie mille, buona serata anche a te!", "isCorrect": True, "feedback": "Friendly closing."},
                {"text": "Il citofono non funziona da una settimana.", "isCorrect": False, "feedback": "Housing talk is forbidden."},
                {"text": "Cerco un idraulico per il lavandino rotto.", "isCorrect": False, "feedback": "Domestic talk is forbidden."}
            ]
        }
    ])

    # Conversation 3: Concert Details
    conv3 = data['conversations'][2]
    conv3['messages'].extend([
        {
            "id": "m6",
            "role": "host",
            "text": "Sai che c'è un gruppo di apertura prima del cantante?",
            "english": "Do you know there's an opening act before the singer?",
            "choices": [
                {"text": "No, non lo sapevo. Come si chiama il gruppo?", "isCorrect": True, "feedback": "Asking for more info about the opening act."},
                {"text": "Il mio letto è molto scomodo stasera.", "isCorrect": False, "feedback": "Hotel talk is forbidden."},
                {"text": "Prendo un autobus per andare al museo.", "isCorrect": False, "feedback": "Transportation talk is forbidden."}
            ]
        },
        {
            "id": "m7",
            "role": "host",
            "text": "Si chiamano 'I Giovani'. Suonano per trenta minuti.",
            "english": "They are called 'I Giovani'. They play for thirty minutes.",
            "choices": [
                {"text": "Capito. Allora il cantante inizia più tardi.", "isCorrect": True, "feedback": "Understanding the schedule."},
                {"text": "Il citofono suona sempre alle otto di sera.", "isCorrect": False, "feedback": "Housing talk is forbidden."},
                {"text": "Voglio ordinare una bistecca ben cotta.", "isCorrect": False, "feedback": "Restaurant talk is forbidden."}
            ]
        },
        {
            "id": "m8",
            "role": "host",
            "text": "Esatto. Verso le nove e mezza il palco sarà pronto.",
            "english": "Exactly. Around nine-thirty the stage will be ready.",
            "choices": [
                {"text": "Perfetto, ho tempo per fare un giro.", "isCorrect": True, "feedback": "Planning the wait time."},
                {"text": "Il mio bagaglio è stato smarrito dal treno.", "isCorrect": False, "feedback": "Travel talk is forbidden."},
                {"text": "Devo chiamare il medico per la ricetta.", "isCorrect": False, "feedback": "Medical talk is forbidden."}
            ]
        },
        {
            "id": "m9",
            "role": "host",
            "text": "C'è anche un'area fumatori fuori, se ti serve.",
            "english": "There's also a smoking area outside, if you need it.",
            "choices": [
                {"text": "Grazie, ma non fumo. Resto qui vicino.", "isCorrect": True, "feedback": "Declining and staying put."},
                {"text": "Voglio prenotare un hotel con colazione.", "isCorrect": False, "feedback": "Hotel talk is forbidden."},
                {"text": "Il bagno della mia camera è sporco.", "isCorrect": False, "feedback": "Hotel talk is forbidden."}
            ]
        },
        {
            "id": "m10",
            "role": "host",
            "text": "Va bene. Sarà uno spettacolo indimenticabile!",
            "english": "Alright. It will be an unforgettable show!",
            "choices": [
                {"text": "Lo spero proprio! Grazie per le informazioni.", "isCorrect": True, "feedback": "Positive closure."},
                {"text": "Il mio volo è stato cancellato per nebbia.", "isCorrect": False, "feedback": "Airport talk is forbidden."},
                {"text": "Le chiavi dell'appartamento sono sul tavolo.", "isCorrect": False, "feedback": "Housing talk is forbidden."}
            ]
        }
    ])

    # Conversation 4: Meeting Other Fans
    conv4 = data['conversations'][3]
    conv4['messages'].extend([
        {
            "id": "m6",
            "role": "host",
            "text": "Hai visto se vendono anche i poster del tour?",
            "english": "Did you see if they also sell tour posters?",
            "choices": [
                {"text": "Sì, li ho visti vicino alle magliette.", "isCorrect": True, "feedback": "Confirming poster availability."},
                {"text": "No, il mio frigo è rotto da ieri.", "isCorrect": False, "feedback": "Domestic talk is forbidden."},
                {"text": "Prendo un treno per andare a Venezia.", "isCorrect": False, "feedback": "Transportation talk is forbidden."}
            ]
        },
        {
            "id": "m7",
            "role": "host",
            "text": "Ottimo! Quanto costano, lo sai?",
            "english": "Great! Do you know how much they cost?",
            "choices": [
                {"text": "Credo che costino dieci euro l'uno.", "isCorrect": True, "feedback": "Providing price info."},
                {"text": "Il citofono del palazzo non apre.", "isCorrect": False, "feedback": "Housing talk is forbidden."},
                {"text": "Voglio una camera con vista sulla montagna.", "isCorrect": False, "feedback": "Hotel talk is forbidden."}
            ]
        },
        {
            "id": "m8",
            "role": "host",
            "text": "Dieci euro è un buon prezzo. Ne prendo uno.",
            "english": "Ten euros is a good price. I'll get one.",
            "choices": [
                {"text": "Fai bene, sono molto belli e colorati.", "isCorrect": True, "feedback": "Encouraging the purchase."},
                {"text": "Il medico mi ha visitato la gola oggi.", "isCorrect": False, "feedback": "Medical talk is forbidden."},
                {"text": "Prendo l'autobus per tornare a casa.", "isCorrect": False, "feedback": "Transportation talk is forbidden."}
            ]
        },
        {
            "id": "m9",
            "role": "host",
            "text": "Sai se il gruppo suona di nuovo domani?",
            "english": "Do you know if the band is playing again tomorrow?",
            "choices": [
                {"text": "Sì, suonano in un'altra città qui vicino.", "isCorrect": True, "feedback": "Providing info on next shows."},
                {"text": "No, il mio bagaglio è troppo grande.", "isCorrect": False, "feedback": "Travel talk is forbidden."},
                {"text": "Voglio ordinare un piatto di pasta al forno.", "isCorrect": False, "feedback": "Restaurant talk is forbidden."}
            ]
        },
        {
            "id": "m10",
            "role": "host",
            "text": "Peccato, non posso andare. Ma stasera è stato top!",
            "english": "Too bad, I can't go. But tonight was top!",
            "choices": [
                {"text": "Assolutamente! Una serata da ricordare. Ciao!", "isCorrect": True, "feedback": "Positive conclusion and goodbye."},
                {"text": "Il citofono è ancora rotto, che noia.", "isCorrect": False, "feedback": "Housing talk is forbidden."},
                {"text": "Il mio volo parte alle sei di mattina.", "isCorrect": False, "feedback": "Airport talk is forbidden."}
            ]
        }
    ])

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

expand_conversations()
