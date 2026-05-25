import json
import random

scenario = "gas_station"
s_code = "s11"
path = f"/home/waseageru/parli-italiano/src/data/exports/travel/{scenario}/"

def save_json(items, filename):
    with open(path + filename, "w") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

def create_items(data, item_type, s_code):
    items = []
    prefix = item_type[0]
    for i, (it, en) in enumerate(data):
        others = [d for d in data if d[0] != it]
        sampled_others = random.sample(others, 3)
        choices_it = [it] + [s[0] for s in sampled_others]
        choices_en = [en] + [s[1] for s in sampled_others]
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        
        item = {
            "id": f"{s_code}-{prefix}{i+1}",
            "italian": it,
            "english": en,
            "type": item_type,
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
              "correctItalian": "Ottimo!" if item_type == "vocabulary" else "Esatto!" if item_type == "phrase" else "Perfetto!",
              "incorrectItalian": f"No, la risposta è \"{it}\".",
              "correctEnglish": "Great!" if item_type == "vocabulary" else "Exactly!" if item_type == "phrase" else "Perfect!",
              "incorrectEnglish": f"No, the answer is \"{en}\"."
            }
        }
        items.append(item)
    return items

# Vocabulary (50+)
vocab_data = [
    ("benzina", "gasoline"), ("gasolio", "diesel"), ("senza piombo", "unleaded"),
    ("pieno", "full tank"), ("pompa", "pump"), ("erogatore", "nozzle"),
    ("self-service", "self-service"), ("servito", "full service"), ("colonnina", "payment terminal"),
    ("banconota", "banknote"), ("carta", "card"), ("olio", "oil"),
    ("acqua", "water"), ("liquido tergicristalli", "windshield fluid"), ("gomme", "tires"),
    ("pressione", "pressure"), ("aria", "air"), ("compressore", "compressor"),
    ("autolavaggio", "car wash"), ("gettone", "token"), ("scontrino", "receipt"),
    ("distributore", "gas station"), ("stazione di servizio", "service station"), ("bar", "bar/cafe"),
    ("bagno", "bathroom"), ("parcheggio", "parking"), ("uscita", "exit"),
    ("entrata", "entrance"), ("prezzo", "price"), ("euro", "euro"),
    ("litro", "liter"), ("tappo", "cap"), ("serbatoio", "fuel tank"),
    ("guanti", "gloves"), ("carta assorbente", "paper towels"), ("vetri", "windows/glass"),
    ("spazzola", "brush"), ("sapone", "soap"), ("asciugatura", "drying"),
    ("aspirapolvere", "vacuum cleaner"), ("manometro", "pressure gauge"), ("valvola", "valve"),
    ("ruota", "wheel"), ("freni", "brakes"), ("luci", "lights"),
    ("batteria", "battery"), ("cavi", "cables"), ("soccorso", "assistance"),
    ("guasto", "breakdown"), ("officina", "repair shop"), ("meccanico", "mechanic")
]

# Phrases (50+)
phrases_data = [
    ("Faccia il pieno", "Fill it up"), ("Cinquanta euro di benzina", "Fifty euros of gas"),
    ("Senza piombo, per favore", "Unleaded, please"), ("Controlli l'olio", "Check the oil"),
    ("Controlli la pressione", "Check the pressure"), ("Dove sono i guanti?", "Where are the gloves?"),
    ("La pompa non funziona", "The pump isn't working"), ("Come si paga?", "How do I pay?"),
    ("Accettate carte?", "Do you accept cards?"), ("Mi serve uno scontrino", "I need a receipt"),
    ("Dov'è il compressore?", "Where is the compressor?"), ("È gratuito?", "Is it free?"),
    ("Serve un gettone?", "Do I need a token?"), ("Il bagno è libero?", "Is the bathroom free?"),
    ("Un caffè, per favore", "A coffee, please"), ("Vorrei lavare l'auto", "I'd like to wash the car"),
    ("Quale programma scelgo?", "Which program should I choose?"), ("Manca il sapone", "The soap is missing"),
    ("La colonnina è rotta", "The terminal is broken"), ("Inserire la carta", "Insert the card"),
    ("Digitare il PIN", "Type the PIN"), ("Selezionare la pompa", "Select the pump"),
    ("Alzi l'erogatore", "Lift the nozzle"), ("Metta il tappo", "Put the cap on"),
    ("Chiuda il serbatoio", "Close the tank"), ("Sposti l'auto", "Move the car"),
    ("Non blocchi il passaggio", "Don't block the way"), ("C'è un'officina?", "Is there a repair shop?"),
    ("Il motore scalda", "The engine is overheating"), ("Mi servono i cavi", "I need the cables"),
    ("La batteria è scarica", "The battery is dead"), ("Quanto costa il diesel?", "How much is diesel?"),
    ("Il prezzo al litro", "The price per liter"), ("È troppo caro", "It's too expensive"),
    ("C'è uno sconto?", "Is there a discount?"), ("Posso gonfiare le gomme?", "Can I inflate the tires?"),
    ("A quanto vanno?", "What pressure should they be?"), ("Due bar e mezzo", "Two and a half bars"),
    ("Grazie dell'aiuto", "Thanks for the help"), ("Buona giornata", "Have a good day"),
    ("Arrivederci", "Goodbye"), ("Buongiorno", "Good morning"),
    ("Buonasera", "Good evening"), ("Mi scusi", "Excuse me"),
    ("Un momento", "One moment"), ("Aspetti pure", "Please wait"),
    ("Prego", "You're welcome"), ("Di nulla", "It's nothing"),
    ("Torni presto", "Come back soon"), ("Buon viaggio", "Have a good trip")
]

# Sentences (60+)
sentences_data = [
    ("Buongiorno, mi faccia il pieno di senza piombo.", "Good morning, fill it up with unleaded for me."),
    ("Potrebbe controllare anche il livello dell'olio?", "Could you also check the oil level?"),
    ("Certo, apro subito il cofano della macchina.", "Sure, I'll open the car hood right away."),
    ("L'olio è a posto, ma manca un po' d'acqua.", "The oil is fine, but it's missing a bit of water."),
    ("Aggiunga pure il liquido per i tergicristalli.", "Go ahead and add some windshield wiper fluid."),
    ("Sono sessantacinque euro in totale, grazie.", "That's sixty-five euros in total, thank you."),
    ("Posso pagare con la carta di credito?", "Can I pay with a credit card?"),
    ("Sì, inserisca pure la carta nel lettore.", "Yes, please insert your card into the reader."),
    ("Scusi, la pompa numero quattro non eroga benzina.", "Excuse me, pump number four is not dispensing gas."),
    ("Deve prima inserire la banconota nel distributore automatico.", "You must first insert the banknote into the automatic distributor."),
    ("Ho messo venti euro, ma non è uscito nulla.", "I put in twenty euros, but nothing came out."),
    ("Controlli se ha selezionato il numero corretto della pompa.", "Check if you have selected the correct pump number."),
    ("Ah, ho dimenticato di premere il tasto di conferma.", "Ah, I forgot to press the confirmation button."),
    ("Dov'è il compressore per controllare la pressione delle gomme?", "Where is the compressor to check the tire pressure?"),
    ("Lo trova dietro l'autolavaggio, accanto ai bidoni.", "You can find it behind the car wash, next to the bins."),
    ("Serve una moneta da un euro per farlo funzionare?", "Do I need a one-euro coin to make it work?"),
    ("No, è un servizio gratuito per i nostri clienti.", "No, it's a free service for our customers."),
    ("Le mie gomme sembrano un po' sgonfie oggi.", "My tires seem a bit flat today."),
    ("La pressione ideale è scritta sul manuale dell'auto.", "The ideal pressure is written in the car manual."),
    ("Vorrei fare il lavaggio completo della carrozzeria.", "I'd like to do a full wash of the bodywork."),
    ("Prenda il gettone alla cassa e scelga il programma.", "Get the token at the cashier and choose the program."),
    ("Il programma numero tre include anche la cera?", "Does program number three also include wax?"),
    ("Sì, costa dodici euro e dura circa dieci minuti.", "Yes, it costs twelve euros and lasts about ten minutes."),
    ("Devo restare dentro l'auto durante il lavaggio?", "Do I have to stay inside the car during the wash?"),
    ("No, è meglio scendere e aspettare qui fuori.", "No, it's better to get out and wait out here."),
    ("Mi scusi, dove posso buttare questi rifiuti?", "Excuse me, where can I throw away this trash?"),
    ("C'è un cestino accanto ad ogni pompa di benzina.", "There is a bin next to every gas pump."),
    ("Saprebbe indicarmi l'officina meccanica più vicina?", "Could you point me to the nearest mechanic's shop?"),
    ("Continui dritto per due chilometri, è sulla destra.", "Keep going straight for two kilometers, it's on the right."),
    ("Ho un problema con la batteria, l'auto non parte.", "I have a problem with the battery, the car won't start."),
    ("Se vuole ho dei cavi per farla ripartire.", "If you want, I have some cables to jump-start it."),
    ("Grazie mille, mi farebbe un grande favore!", "Thank you very much, you'd be doing me a great favor!"),
    ("Quanto costa il diesel oggi al litro?", "How much does diesel cost per liter today?"),
    ("Il prezzo è di un euro e ottanta centesimi.", "The price is one euro and eighty cents."),
    ("È aumentato molto rispetto alla settimana scorsa.", "It has increased a lot compared to last week."),
    ("Sì, i prezzi del carburante cambiano ogni giorno.", "Yes, fuel prices change every day."),
    ("C'è un bar qui dentro dove posso prendere un cornetto?", "Is there a bar in here where I can get a croissant?"),
    ("Sì, il bar è aperto fino alle dieci di sera.", "Yes, the bar is open until ten in the evening."),
    ("Posso avere anche una bottiglia d'acqua naturale?", "Can I also have a bottle of still water?"),
    ("Certamente, sono un euro e cinquanta alla cassa.", "Certainly, it's one euro fifty at the cashier."),
    ("Devo spostare la macchina dopo aver fatto benzina?", "Do I need to move the car after getting gas?"),
    ("Sì, per favore, così libera la pompa per gli altri.", "Yes, please, so you free up the pump for others."),
    ("La parcheggi pure in quegli spazi bianchi lì.", "Just park it in those white spaces over there."),
    ("Mi scusi, dove si trova il bagno?", "Excuse me, where is the bathroom?"),
    ("La chiave è appesa dietro la porta del bar.", "The key is hanging behind the bar door."),
    ("Posso usare il bancomat per pagare il rifornimento?", "Can I use the ATM card to pay for the fuel?"),
    ("Sì, accettiamo tutte le principali carte di debito.", "Yes, we accept all major debit cards."),
    ("Non dimentichi di chiudere bene il tappo del serbatoio.", "Don't forget to close the gas tank cap tightly."),
    ("Grazie del consiglio, stavo quasi per dimenticarmene.", "Thanks for the advice, I was almost about to forget it."),
    ("L'erogatore si è bloccato, cosa devo fare?", "The nozzle is stuck, what should I do?"),
    ("Provi a premere la leva con più forza.", "Try to press the lever with more force."),
    ("Ecco fatto, adesso la benzina sta uscendo.", "There we go, now the gas is coming out."),
    ("Vuole che le pulisca il parabrezza?", "Do you want me to clean your windshield?"),
    ("Sì, grazie, è molto sporco di moscerini.", "Yes, please, it's very dirty with small flies."),
    ("Uso questa spazzola con un po' di sapone.", "I'll use this brush with some soap."),
    ("Adesso si vede molto meglio, grazie!", "Now I can see much better, thank you!"),
    ("Non c'è di che, è un piacere aiutarla.", "You're welcome, it's a pleasure to help you."),
    ("Buon viaggio e guidi con prudenza!", "Have a good trip and drive carefully!"),
    ("Grazie ancora, arrivederci e buon lavoro.", "Thanks again, goodbye and have a good day at work."),
    ("In autostrada la benzina costa sempre di più.", "On the highway, gas always costs more."),
    ("Meglio fare il pieno prima di partire.", "Better to fill up before leaving.")
]

save_json(create_items(vocab_data, "vocabulary", s_code), f"travel_{scenario}_vocabulary.json")
save_json(create_items(phrases_data, "phrase", s_code), f"travel_{scenario}_phrases.json")
save_json(create_items(sentences_data, "sentence", s_code), f"travel_{scenario}_sentences.json")
