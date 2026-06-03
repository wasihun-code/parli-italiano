import json

translations = {
    "Sì, l'ho aperta. Sono in via Roma, davanti al bar.": "Yes, I opened it. I am in via Roma, in front of the bar.",
    "Va bene, cerco \"farmacia\" sulla mappa. Vediamo.": "Alright, I'll search for \"pharmacy\" on the map. Let's see.",
    "Sì, la vedo. Devo andare dritto per trecento metri.": "Yes, I see it. I have to go straight for three hundred meters.",
    "Gira a destra dopo trecento metri. Ricevuto, vado.": "Turn right after three hundred meters. Received, I'm going.",
    "Sì, sono quasi arrivato. Ti scrivo tra poco. Grazie!": "Yes, I'm almost there. I'll write to you shortly. Thanks!",
    "Sì, vedo la croce verde. Entro subito.": "Yes, I see the green cross. I'm going in right now.",
    "Controllo l'app. C'è un bancomat a cinquanta metri.": "I'll check the app. There's an ATM fifty meters away.",
    "Hai ragione, ho chiuso l'app. La batteria ringrazia!": "You're right, I closed the app. The battery thanks you!",
    "Sì, ho preso le medicine. Ora esco.": "Yes, I got the medicines. I'm leaving now.",
    "Imposto l'hotel come destinazione. A tra poco!": "I'm setting the hotel as destination. See you shortly!",
    "Buona idea. Quale linea devo prendere per andare lì?": "Good idea. Which line should I take to go there?",
    "Controllo subito. La linea 12 parte tra cinque minuti.": "I'll check right away. Line 12 leaves in five minutes.",
    "Sto correndo. Vedo la fermata dell'autobus e il bus.": "I'm running. I see the bus stop and the bus.",
    "Sì, dice che mancano quattro fermate. Siamo vicini.": "Yes, it says four stops left. We are close.",
    "Piazza Navona, capito. Ti chiamo quando arrivo lì.": "Piazza Navona, understood. I'll call you when I arrive there.",
    "Sì, sono sull'autobus. Mancano due fermate.": "Yes, I'm on the bus. Two stops left.",
    "Ho suonato il campanello. Vado verso la porta.": "I rang the bell. I'm going towards the door.",
    "Sì, sono in piazza. L'app dice di andare a sinistra.": "Yes, I'm in the square. The app says to go left.",
    "Sì, vedo la coda e l'ingresso. Vado lì.": "Yes, I see the queue and the entrance. I'm going there.",
    "Sì, ho il codice a barre sul telefono. Pronto per entrare!": "Yes, I have the barcode on the phone. Ready to enter!",
    "No, il segnale GPS è debole. Non so dove sono.": "No, the GPS signal is weak. I don't know where I am.",
    "Va bene, provo a spostarmi. Lo schermo è bloccato.": "Alright, I'll try to move. The screen is frozen.",
    "Sto riavviando l'app... ecco, ora il segnale è tornato!": "I'm restarting the app... there, now the signal is back!",
    "Sì, ora vedo la freccia blu. Devo tornare indietro.": "Yes, now I see the blue arrow. I have to go back.",
    "Ottimo consiglio, alzo il volume. Ci vediamo dopo!": "Great advice, I'll turn up the volume. See you later!",
    "Dice di continuare dritto per duecento metri.": "It says to continue straight for two hundred meters.",
    "Starò nelle strade principali per avere un buon segnale.": "I will stay on the main streets to have a good signal.",
    "Sì, ha detto di girare a sinistra al semaforo.": "Yes, it said to turn left at the traffic light.",
    "Il segnale è perfetto ora. Manca pochissimo.": "The signal is perfect now. Very little is left.",
    "Missione compiuta! Grazie per l'aiuto con la mappa.": "Mission accomplished! Thanks for the help with the map.",
    "No, ho solo il dieci per cento. Devo sbrigarmi.": "No, I only have ten percent. I have to hurry.",
    "Giusto. Come si scarica la mappa della città?": "Right. How do you download the city map?",
    "Fatto. Ora posso chiudere la connessione internet?": "Done. Can I close the internet connection now?",
    "Ottimo, ora la batteria durerà molto di più.": "Great, now the battery will last much longer.",
    "Arrivo subito. Speriamo che il telefono resti acceso!": "I'm coming right away. Let's hope the phone stays on!",
    "Dice che mancano cinquecento metri. Cammino veloce.": "It says there are five hundred meters left. I'm walking fast.",
    "L'ho abbassata al minimo. Ottima idea per risparmiare.": "I lowered it to the minimum. Great idea to save it.",
    "Certo. Mi ricorderò il nome della piazza, per sicurezza.": "Sure. I will remember the name of the square, just in case.",
    "Molto utile! Senza la mappa offline sarei perso.": "Very useful! Without the offline map I would be lost.",
    "Sì, appena in tempo. Ora mi serve il caricatore!": "Yes, just in time. Now I need the charger!"
}

def fix_english_translations():
    with open('src/data/exports/tech/using_a_map_app/conversations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for conv in data['conversations']:
        for msg in conv['messages']:
            if 'english' not in msg:
                print(f"Missing english in host msg: {msg['text']}")
            for choice in msg['choices']:
                if choice.get('isCorrect') == True:
                    text = choice['text']
                    if 'english' not in choice:
                        if text in translations:
                            choice['english'] = translations[text]
                        else:
                            print(f"Missing translation for: {text}")
                            
    with open('src/data/exports/tech/using_a_map_app/conversations.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    fix_english_translations()
    print("English translations added to correct choices.")
