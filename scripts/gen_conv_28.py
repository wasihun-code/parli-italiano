import json
import random

scenario_id = 28

conversations = []

# Conv 1: Quick Espresso at the Bar
conv1 = {
    "id": "quick_espresso_bar",
    "title": "Quick Espresso at the Bar",
    "description": "Order a quick espresso at the counter and pay.",
    "messages": [
        {"role": "barista", "text": "Buongiorno! Cosa ti preparo?", "english": "Good morning! What can I get you?"},
        {"role": "barista", "text": "Un caffè normale o macchiato?", "english": "A regular coffee or with a spot of milk?"},
        {"role": "barista", "text": "Certo. Lo bevi qui al banco?", "english": "Sure. Will you drink it here at the counter?"},
        {"role": "barista", "text": "Ecco il tuo caffè. Zucchero?", "english": "Here is your coffee. Sugar?"},
        {"role": "barista", "text": "È lì sulla destra, prego.", "english": "It's right there on the right, you're welcome."},
        {"role": "barista", "text": "Tutto a posto? Ti è piaciuto?", "english": "Is everything alright? Did you like it?"},
        {"role": "barista", "text": "Ottimo. Devi pagare ora?", "english": "Excellent. Do you need to pay now?"},
        {"role": "barista", "text": "Sono un euro e venti, per favore.", "english": "It's one euro and twenty, please."},
        {"role": "barista", "text": "Ecco il resto di ottanta centesimi.", "english": "Here is your change of eighty cents."},
        {"role": "barista", "text": "Grazie a te. Buona giornata!", "english": "Thank you. Have a good day!"}
    ],
    "user_correct": [
        "Buongiorno! Vorrei un caffè, per favore.",
        "Un caffè normale, grazie mille.",
        "Sì, lo bevo qui al banco, grazie.",
        "Sì, un po' di zucchero, per favore.",
        "Perfetto, lo metto da solo, grazie.",
        "Sì, molto buono. Un ottimo caffè.",
        "Sì, vorrei pagare adesso, grazie.",
        "Ecco una moneta da due euro.",
        "Grazie mille per il resto.",
        "Buona giornata anche a te! Arrivederci."
    ],
    "user_distractors": [
        ["Buonasera! Vorrei un gelato, per favore.", "Buongiorno! Vorrei un piatto, per favore."],
        ["Un succo di mela, grazie mille.", "Un tè molto caldo, grazie mille."],
        ["No, lo mangio nel letto, grazie.", "Sì, lo bevo qui in bagno, grazie."],
        ["No, un po' di formaggio, per favore.", "Sì, un po' di pepe nero, per favore."],
        ["Perfetto, lo butto da solo, grazie.", "Perfetto, lo vendo da solo, grazie."],
        ["Sì, molto lento. Un brutto caffè.", "Sì, molto rosso. Un grande caffè."],
        ["Sì, vorrei ballare adesso, grazie.", "No, vorrei gridare adesso, grazie."],
        ["Ecco una scarpa da due euro.", "Ecco una maglia da due euro."],
        ["Grazie mille per il libro.", "Grazie mille per il gatto."],
        ["Buona colazione anche a te! Arrivederci.", "Buona mezzanotte anche a te! Arrivederci."]
    ]
}

# Conv 2: Order with Pastry
conv2 = {
    "id": "order_with_pastry",
    "title": "Order with Pastry",
    "description": "Order a cappuccino and a pastry.",
    "messages": [
        {"role": "barista", "text": "Salve! Desidera ordinare?", "english": "Hello! Would you like to order?"},
        {"role": "barista", "text": "Un cappuccino. E da mangiare?", "english": "A cappuccino. And to eat?"},
        {"role": "barista", "text": "Vuoto, alla crema o al cioccolato?", "english": "Plain, with cream or with chocolate?"},
        {"role": "barista", "text": "Un cornetto alla crema. Altro?", "english": "A croissant with cream. Anything else?"},
        {"role": "barista", "text": "D'accordo. Si siede al tavolo?", "english": "Alright. Are you sitting at a table?"},
        {"role": "barista", "text": "Bene, le porto tutto io.", "english": "Good, I'll bring everything to you."},
        {"role": "barista", "text": "Ecco il cappuccino e il cornetto.", "english": "Here is the cappuccino and the croissant."},
        {"role": "barista", "text": "Spero sia di suo gradimento.", "english": "I hope it is to your liking."},
        {"role": "barista", "text": "Posso portarle via la tazza?", "english": "Can I take your cup away?"},
        {"role": "barista", "text": "Va bene, le porto il conto.", "english": "Alright, I'll bring you the bill."}
    ],
    "user_correct": [
        "Salve! Sì, vorrei un cappuccino.",
        "Sì, vorrei anche un cornetto.",
        "Un cornetto alla crema, per favore.",
        "No, basta così, grazie mille.",
        "Sì, mi siedo al tavolo fuori.",
        "Perfetto, la aspetto al tavolo.",
        "Grazie mille, ha un bell'aspetto.",
        "Sì, è davvero tutto molto buono.",
        "Sì, certo. Vorrei pagare, per favore.",
        "Grazie, pago con la carta di credito."
    ],
    "user_distractors": [
        ["Salve! Sì, vorrei un asciugamano.", "Salve! Sì, vorrei un mappamondo."],
        ["Sì, vorrei anche un divano.", "Sì, vorrei anche un tappeto."],
        ["Un bicchiere alla menta, per favore.", "Un cappello alla crema, per favore."],
        ["Sì, pasta così, grazie mille.", "No, porta così, grazie mille."],
        ["Sì, mi siedo al ponte fuori.", "No, mi siedo al parco fuori."],
        ["Perfetto, la aspetto in cucina.", "Perfetto, la aspetto in ufficio."],
        ["Grazie mille, ha un bell'orologio.", "Grazie mille, ha un bell'ombrello."],
        ["Sì, è davvero tutto molto vuoto.", "Sì, è davvero tutto molto stanco."],
        ["Sì, certo. Vorrei nuotare, per favore.", "Sì, certo. Vorrei saltare, per favore."],
        ["Grazie, pago con la porta di casa.", "Grazie, pago con la pizza di ieri."]
    ]
}

# Conv 3: Decaf Specialty Coffee
conv3 = {
    "id": "decaf_specialty_coffee",
    "title": "Decaf Specialty Coffee",
    "description": "Order a decaffeinated macchiato and a glass of water.",
    "messages": [
        {"role": "barista", "text": "Buongiorno! Dimmi pure.", "english": "Good morning! Tell me."},
        {"role": "barista", "text": "Decaffeinato. Lo vuoi macchiato?", "english": "Decaffeinated. Do you want it with milk?"},
        {"role": "barista", "text": "Latte freddo o latte caldo?", "english": "Cold milk or hot milk?"},
        {"role": "barista", "text": "Caldo. Vuoi anche dell'acqua?", "english": "Hot. Do you also want some water?"},
        {"role": "barista", "text": "Liscia o frizzante?", "english": "Still or sparkling?"},
        {"role": "barista", "text": "Ecco a te l'acqua e il caffè.", "english": "Here is your water and coffee."},
        {"role": "barista", "text": "Serve altro per caso?", "english": "Do you need anything else by chance?"},
        {"role": "barista", "text": "Il bagno è in fondo a destra.", "english": "The bathroom is down the hall to the right."},
        {"role": "barista", "text": "Certo, vuoi lo scontrino?", "english": "Sure, do you want the receipt?"},
        {"role": "barista", "text": "Ecco a te. Arrivederci!", "english": "Here you go. Goodbye!"}
    ],
    "user_correct": [
        "Buongiorno! Vorrei un decaffeinato.",
        "Sì, un po' macchiato, per favore.",
        "Con un po' di latte caldo.",
        "Sì, un bicchiere d'acqua, grazie.",
        "Acqua liscia, va benissimo.",
        "Grazie mille, sei molto gentile.",
        "No grazie. Scusa, dov'è il bagno?",
        "Perfetto, vado e poi pago.",
        "Sì, lo scontrino, per favore.",
        "Grazie e buon lavoro! Ciao."
    ],
    "user_distractors": [
        ["Buongiorno! Vorrei un dizionario.", "Buongiorno! Vorrei un temperino."],
        ["Sì, un po' bagnato, per favore.", "Sì, un po' sporcato, per favore."],
        ["Con un po' di burro caldo.", "Con un po' di sale caldo."],
        ["Sì, un cucchiaio d'acqua, grazie.", "No, un fazzoletto d'acqua, grazie."],
        ["Acqua sporca, va benissimo.", "Acqua amara, va benissimo."],
        ["Grazie mille, sei molto pesante.", "Grazie mille, sei molto invisibile."],
        ["No grazie. Scusa, dov'è il museo?", "No grazie. Scusa, dov'è il treno?"],
        ["Perfetto, nuoto e poi pago.", "Perfetto, corro e poi pago."],
        ["Sì, lo specchio, per favore.", "Sì, lo scoiattolo, per favore."],
        ["Grazie e buon viaggio! Ciao.", "Grazie e buon appetito! Ciao."]
    ]
}

# Conv 4: Meeting a Friend
conv4 = {
    "id": "meeting_a_friend",
    "title": "Meeting a Friend",
    "description": "Order drinks for yourself and a friend who just arrived.",
    "messages": [
        {"role": "barista", "text": "Ciao! Siete in due oggi?", "english": "Hi! Are there two of you today?"},
        {"role": "barista", "text": "Prendete da bere o da mangiare?", "english": "Are you getting something to drink or to eat?"},
        {"role": "barista", "text": "Due caffè. Come li preferite?", "english": "Two coffees. How do you prefer them?"},
        {"role": "barista", "text": "Un espresso e un americano. Altro?", "english": "An espresso and an Americano. Anything else?"},
        {"role": "barista", "text": "Arrivano subito. Vi sedete?", "english": "They are coming right up. Are you sitting down?"},
        {"role": "barista", "text": "Prego. L'americano è bollente.", "english": "Here you go. The Americano is boiling hot."},
        {"role": "barista", "text": "Tutto bene con i caffè?", "english": "Is everything fine with the coffees?"},
        {"role": "barista", "text": "Volete pagare conti separati?", "english": "Do you want to pay separate bills?"},
        {"role": "barista", "text": "Va bene, allora pago tutto insieme.", "english": "Alright, then I pay it all together."},
        {"role": "barista", "text": "Sono tre euro in totale.", "english": "It's three euros in total."}
    ],
    "user_correct": [
        "Ciao! Sì, aspetto un amico.",
        "Solo da bere per ora, grazie.",
        "Un espresso per me e un americano per lui.",
        "No, prendiamo solo i caffè.",
        "Sì, ci sediamo a quel tavolo.",
        "Grazie per l'avvertimento, farà attenzione.",
        "Sì, sono perfetti, grazie mille.",
        "No, offro io oggi. Pago tutto insieme.",
        "Esatto, quant'è il totale?",
        "Ecco a te, tieni il resto."
    ],
    "user_distractors": [
        ["Ciao! Sì, aspetto un autobus.", "Ciao! Sì, aspetto un pacco."],
        ["Solo da pulire per ora, grazie.", "Solo da cucire per ora, grazie."],
        ["Un gelato per me e un tavolo per lui.", "Un cuscino per me e un divano per lui."],
        ["No, vendiamo solo i caffè.", "No, compriamo solo i fiumi."],
        ["Sì, ci sediamo a quel soffitto.", "Sì, ci sediamo a quel balcone."],
        ["Grazie per il formaggio, farà attenzione.", "Grazie per il cuscino, farà attenzione."],
        ["Sì, sono quadrati, grazie mille.", "Sì, sono rotondi, grazie mille."],
        ["No, apro io oggi. Pago tutto insieme.", "No, lavo io oggi. Pago tutto insieme."],
        ["Esatto, quant'è il tavolo?", "Esatto, quant'è il bicchiere?"],
        ["Ecco a te, tieni il muro.", "Ecco a te, tieni il tetto."]
    ]
}

data = {
    "scenarioId": scenario_id,
    "conversations": []
}

for conv in [conv1, conv2, conv3, conv4]:
    msgs = []
    for i in range(10):
        msg = {
            "id": f"m{i+1}",
            "role": conv["messages"][i]["role"],
            "text": conv["messages"][i]["text"],
            "english": conv["messages"][i]["english"],
            "choices": [
                {
                    "text": conv["user_correct"][i],
                    "isCorrect": True
                },
                {
                    "text": conv["user_distractors"][i][0],
                    "isCorrect": False
                },
                {
                    "text": conv["user_distractors"][i][1],
                    "isCorrect": False
                }
            ]
        }
        # Shuffle choices
        random.shuffle(msg["choices"])
        msgs.append(msg)
        
    data["conversations"].append({
        "id": conv["id"],
        "title": conv["title"],
        "description": conv["description"],
        "messages": msgs
    })

with open("src/data/exports/dining/ordering_coffee/conversations.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Generated conversations.json")
