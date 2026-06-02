import json

def expand_conversations():
    file_path = 'src/data/exports/shopping/pharmacy_purchase/conversations.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Conv 1: buying_sunscreen
    conv1 = data['conversations'][0]
    conv1['messages'].extend([
        {
            "id": "m6",
            "role": "host",
            "text": "Ecco qui la ricevuta. Serve anche una busta?",
            "english": "Here is the receipt. Do you also need a bag?",
            "choices": [
                {"text": "No, grazie. Metto tutto nello zaino.", "isCorrect": True, "feedback": "Natural response declining a bag."},
                {"text": "No, grazie. Voglio un panino al prosciutto.", "isCorrect": False, "feedback": "Food talk is forbidden."},
                {"text": "Sì, voglio un asciugamano per la spiaggia.", "isCorrect": False, "feedback": "A pharmacy does not sell beach towels."}
            ]
        },
        {
            "id": "m7",
            "role": "host",
            "text": "Perfetto. Attenzione al sole di oggi, è molto forte.",
            "english": "Perfect. Be careful of the sun today, it's very strong.",
            "choices": [
                {"text": "Lo so, starò all'ombra durante le ore centrali.", "isCorrect": True, "feedback": "Good response to the warning."},
                {"text": "Lo so, comprerò un ombrello da pioggia.", "isCorrect": False, "feedback": "Rain umbrellas are irrelevant here."},
                {"text": "Lo so, il frigo non funziona bene.", "isCorrect": False, "feedback": "Appliance talk is forbidden."}
            ]
        },
        {
            "id": "m8",
            "role": "host",
            "text": "Faccia attenzione anche a mettere la crema spesso.",
            "english": "Also be careful to apply the cream often.",
            "choices": [
                {"text": "Sì, la rimetterò dopo ogni bagno in mare.", "isCorrect": True, "feedback": "Correct usage of sunscreen."},
                {"text": "Sì, la rimetterò sul pane tostato.", "isCorrect": False, "feedback": "Don't eat sunscreen!"},
                {"text": "Sì, il treno per Roma è sempre in ritardo.", "isCorrect": False, "feedback": "Train talk is forbidden."}
            ]
        },
        {
            "id": "m9",
            "role": "host",
            "text": "Bravissimo. Le auguro una buona giornata e buone vacanze.",
            "english": "Very good. I wish you a good day and happy holidays.",
            "choices": [
                {"text": "Grazie mille, anche a lei e buon lavoro.", "isCorrect": True, "feedback": "Polite closing."},
                {"text": "Grazie mille, il cane deve mangiare adesso.", "isCorrect": False, "feedback": "Pet talk is forbidden."},
                {"text": "Grazie mille, ho perso le chiavi dell'hotel.", "isCorrect": False, "feedback": "Hotel talk is forbidden."}
            ]
        },
        {
            "id": "m10",
            "role": "host",
            "text": "Arrivederci! Torni a trovarci se ha bisogno.",
            "english": "Goodbye! Come visit us again if you need to.",
            "choices": [
                {"text": "Arrivederci! Lo farò sicuramente.", "isCorrect": True, "feedback": "Final goodbye."},
                {"text": "Vorrei ordinare una pizza margherita.", "isCorrect": False, "feedback": "Pizza talk is forbidden."},
                {"text": "Il bagno della camera non ha l'acqua calda.", "isCorrect": False, "feedback": "Hotel talk is forbidden."}
            ]
        }
    ])

    # Conv 2: remedy_cough
    conv2 = data['conversations'][1]
    conv2['messages'].extend([
        {
            "id": "m6",
            "role": "host",
            "text": "Ecco qui il resto di cinque euro. Ha bisogno di un sacchetto per portare tutto?",
            "english": "Here is your change of five euros. Do you need a bag to carry everything?",
            "choices": [
                {"text": "Sì, un piccolo sacchetto sarebbe comodo, grazie.", "isCorrect": True, "feedback": "Polite acceptance of the bag."},
                {"text": "Sì, vorrei un sacco a pelo per dormire fuori.", "isCorrect": False, "feedback": "Pharmacies don't sell sleeping bags."},
                {"text": "Sì, mi serve un vestito elegante stasera.", "isCorrect": False, "feedback": "Clothing talk is forbidden."}
            ]
        },
        {
            "id": "m7",
            "role": "host",
            "text": "Certo, eccolo qua. Si ricordi di bere anche molta acqua calda.",
            "english": "Sure, here it is. Remember to also drink a lot of warm water.",
            "choices": [
                {"text": "Ottimo consiglio. Posso bere anche del tè caldo con il miele?", "isCorrect": True, "feedback": "Asking an appropriate follow-up question."},
                {"text": "Ottimo consiglio. Posso guidare la barca sul lago?", "isCorrect": False, "feedback": "Boat talk is irrelevant."},
                {"text": "Ottimo consiglio. Il mio orologio è fermo da ieri.", "isCorrect": False, "feedback": "Watch talk is forbidden."}
            ]
        },
        {
            "id": "m8",
            "role": "host",
            "text": "Assolutamente, il tè caldo aiuta molto la gola infiammata.",
            "english": "Absolutely, hot tea helps an inflamed throat a lot.",
            "choices": [
                {"text": "Perfetto, allora stasera mi preparerò un tè caldo.", "isCorrect": True, "feedback": "Agreeing to the advice."},
                {"text": "Perfetto, allora stasera andrò a ballare in discoteca.", "isCorrect": False, "feedback": "Clubbing is bad for a cough."},
                {"text": "Perfetto, allora stasera guarderò il torneo di calcio.", "isCorrect": False, "feedback": "Soccer is irrelevant here."}
            ]
        },
        {
            "id": "m9",
            "role": "host",
            "text": "Se la tosse non passa dopo tre giorni, le consiglio di vedere un medico.",
            "english": "If the cough doesn't go away after three days, I advise you to see a doctor.",
            "choices": [
                {"text": "Capisco, se peggiora chiamerò un dottore. Grazie.", "isCorrect": True, "feedback": "Accepting the medical advice."},
                {"text": "Capisco, se peggiora comprerò una nuova macchina.", "isCorrect": False, "feedback": "Car talk is forbidden."},
                {"text": "Capisco, se peggiora andrò a nuotare in piscina.", "isCorrect": False, "feedback": "Swimming talk is irrelevant."}
            ]
        },
        {
            "id": "m10",
            "role": "host",
            "text": "Bene, si riguardi e buona guarigione!",
            "english": "Good, take care of yourself and get well soon!",
            "choices": [
                {"text": "Grazie ancora per l'aiuto. Arrivederci!", "isCorrect": True, "feedback": "Friendly goodbye."},
                {"text": "Devo trovare la fermata dell'autobus numero dieci.", "isCorrect": False, "feedback": "Bus talk is forbidden."},
                {"text": "La mia camera non è stata pulita stamattina.", "isCorrect": False, "feedback": "Hotel talk is forbidden."}
            ]
        }
    ])

    # Conv 3: asking_bandages
    conv3 = data['conversations'][2]
    conv3['messages'].extend([
        {
            "id": "m6",
            "role": "host",
            "text": "Spero che il taglio guarisca presto. Lavi la ferita prima di mettere il cerotto.",
            "english": "I hope the cut heals soon. Wash the wound before applying the bandage.",
            "choices": [
                {"text": "Certo, la laverò bene con acqua prima di usare il disinfettante.", "isCorrect": True, "feedback": "Confirming the correct procedure."},
                {"text": "Certo, la laverò bene nel fiume vicino alla stazione.", "isCorrect": False, "feedback": "River water is dirty, not good for a cut."},
                {"text": "Certo, comprerò un gelato al cioccolato più tardi.", "isCorrect": False, "feedback": "Ice cream talk is forbidden."}
            ]
        },
        {
            "id": "m7",
            "role": "host",
            "text": "Bravissimo, l'igiene è molto importante per evitare infezioni.",
            "english": "Very good, hygiene is very important to avoid infections.",
            "choices": [
                {"text": "Assolutamente sì. I cerotti sono resistenti all'acqua?", "isCorrect": True, "feedback": "Asking a relevant question about the product."},
                {"text": "Assolutamente sì. Posso noleggiare una bicicletta qui?", "isCorrect": False, "feedback": "Bike rental talk is forbidden."},
                {"text": "Assolutamente sì. C'è un parcheggio gratuito vicino?", "isCorrect": False, "feedback": "Parking talk is irrelevant."}
            ]
        },
        {
            "id": "m8",
            "role": "host",
            "text": "Sì, questi cerotti sono impermeabili. Può fare la doccia tranquillamente.",
            "english": "Yes, these bandages are waterproof. You can take a shower safely.",
            "choices": [
                {"text": "Perfetto, era proprio quello che mi serviva sapere.", "isCorrect": True, "feedback": "Expressing satisfaction."},
                {"text": "Perfetto, allora cucinerò la pasta stasera.", "isCorrect": False, "feedback": "Cooking talk is forbidden."},
                {"text": "Perfetto, il museo apre alle nove di mattina.", "isCorrect": False, "feedback": "Museum talk is irrelevant."}
            ]
        },
        {
            "id": "m9",
            "role": "host",
            "text": "Se vede arrossamento, mi raccomando, non lo trascuri.",
            "english": "If you see redness, please, do not neglect it.",
            "choices": [
                {"text": "Va bene, controllerò il taglio ogni giorno. Grazie.", "isCorrect": True, "feedback": "Promising to monitor the cut."},
                {"text": "Va bene, controllerò i biglietti del concerto.", "isCorrect": False, "feedback": "Ticket talk is forbidden."},
                {"text": "Va bene, controllerò se piove fuori dalla finestra.", "isCorrect": False, "feedback": "Weather talk is irrelevant."}
            ]
        },
        {
            "id": "m10",
            "role": "host",
            "text": "Di nulla. Torni pure se ha altri problemi.",
            "english": "You're welcome. Come back if you have other problems.",
            "choices": [
                {"text": "Lo farò. Buona giornata e buon lavoro!", "isCorrect": True, "feedback": "Polite farewell."},
                {"text": "Il wifi nell'appartamento non si connette.", "isCorrect": False, "feedback": "Wifi talk is forbidden."},
                {"text": "Dov'è il supermercato più vicino per favore?", "isCorrect": False, "feedback": "Supermarket talk is forbidden here."}
            ]
        }
    ])

    # Conv 4: checking_prescription
    conv4 = data['conversations'][3]
    conv4['messages'].extend([
        {
            "id": "m6",
            "role": "host",
            "text": "Se l'ibuprofene le dà fastidio allo stomaco, lo prenda a stomaco pieno.",
            "english": "If the ibuprofen bothers your stomach, take it on a full stomach.",
            "choices": [
                {"text": "Grazie per il consiglio, lo prenderò dopo aver mangiato.", "isCorrect": True, "feedback": "Agreeing with the medical instruction."},
                {"text": "Grazie per il consiglio, andrò in biblioteca domani.", "isCorrect": False, "feedback": "Library talk is forbidden."},
                {"text": "Grazie per il consiglio, devo cambiare le lenzuola.", "isCorrect": False, "feedback": "Bedding talk is irrelevant."}
            ]
        },
        {
            "id": "m7",
            "role": "host",
            "text": "Esatto, mai a stomaco vuoto. Le gocce invece vanno prese prima dei pasti.",
            "english": "Exactly, never on an empty stomach. The drops instead should be taken before meals.",
            "choices": [
                {"text": "Ho capito. Le gocce prima e le compresse dopo.", "isCorrect": True, "feedback": "Summarizing the instructions correctly."},
                {"text": "Ho capito. Il traghetto parte tra due ore.", "isCorrect": False, "feedback": "Ferry talk is forbidden."},
                {"text": "Ho capito. Ho perso il mio ombrello blu.", "isCorrect": False, "feedback": "Umbrella talk is forbidden."}
            ]
        },
        {
            "id": "m8",
            "role": "host",
            "text": "Perfetto, ha capito benissimo. La scatola di gocce dura circa un mese.",
            "english": "Perfect, you understood very well. The box of drops lasts about a month.",
            "choices": [
                {"text": "Bene, quindi non dovrò tornare presto per un'altra scatola.", "isCorrect": True, "feedback": "Making a logical deduction."},
                {"text": "Bene, quindi non dovrò pagare il pedaggio autostradale.", "isCorrect": False, "feedback": "Highway talk is forbidden."},
                {"text": "Bene, quindi non dovrò comprare un nuovo vestito.", "isCorrect": False, "feedback": "Clothing talk is forbidden."}
            ]
        },
        {
            "id": "m9",
            "role": "host",
            "text": "No, per un po' di tempo è a posto. Le serve la ricevuta per le tasse?",
            "english": "No, for a while you are fine. Do you need the receipt for taxes?",
            "choices": [
                {"text": "Sì, per favore, ecco la mia tessera sanitaria per lo scontrino.", "isCorrect": True, "feedback": "Providing the health card for the receipt."},
                {"text": "Sì, per favore, ecco il mio passaporto per volare a Roma.", "isCorrect": False, "feedback": "Passport talk is forbidden."},
                {"text": "Sì, per favore, ecco la mia patente di guida internazionale.", "isCorrect": False, "feedback": "Driver's license talk is irrelevant."}
            ]
        },
        {
            "id": "m10",
            "role": "host",
            "text": "Ecco lo scontrino con il codice fiscale. Buona giornata e si riguardi!",
            "english": "Here is the receipt with your tax code. Have a good day and take care!",
            "choices": [
                {"text": "La ringrazio molto per la disponibilità. Arrivederci!", "isCorrect": True, "feedback": "A polite and appropriate goodbye."},
                {"text": "Il servizio in camera è stato molto lento oggi.", "isCorrect": False, "feedback": "Room service talk is forbidden."},
                {"text": "Non riesco a trovare il mio gatto nero.", "isCorrect": False, "feedback": "Pet talk is forbidden."}
            ]
        }
    ])

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    expand_conversations()
