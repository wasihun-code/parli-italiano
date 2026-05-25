import json
import os
import random

def generate_s47():
    scenario_id = "s47"
    base_path = "src/data/exports/shopping/electronics_store/"
    
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    # Vocabulary (Min 50)
    vocab_data = [
        ("elettronica", "electronics"), ("negozio", "store"), ("computer", "computer"), ("portatile", "laptop"),
        ("tablet", "tablet"), ("smartphone", "smartphone"), ("auricolari", "earphones"), ("cuffie", "headphones"),
        ("bluetooth", "bluetooth"), ("senza fili", "wireless"), ("caricabatterie", "charger"), ("cavo", "cable"),
        ("adattatore", "adapter"), ("batteria", "battery"), ("memoria", "memory"), ("disco rigido", "hard drive"),
        ("schermo", "screen"), ("tastiera", "keyboard"), ("mouse", "mouse"), ("stampante", "printer"),
        ("altoparlante", "speaker"), ("telecamera", "camera"), ("microfono", "microphone"), ("sistema operativo", "operating system"),
        ("software", "software"), ("app", "app"), ("connessione", "connection"), ("rete", "network"),
        ("wifi", "wifi"), ("velocità", "speed"), ("potenza", "power"), ("capacità", "capacity"),
        ("modello", "model"), ("marca", "brand"), ("garanzia", "warranty"), ("assistenza", "assistance"),
        ("riparazione", "repair"), ("rotto", "broken"), ("nuovo", "new"), ("usato", "used"),
        ("offerta", "offer"), ("sconto", "discount"), ("prezzo", "price"), ("caro", "expensive"),
        ("economico", "cheap"), ("compatibile", "compatible"), ("originale", "original"), ("installato", "installed"),
        ("configurato", "configured"), ("veloce", "fast"), ("lento", "slow"), ("potente", "powerful"),
        ("leggero", "lightweight"), ("pesante", "heavy"), ("professionale", "professional")
    ]
    
    vocab_json = []
    for i, (it, en) in enumerate(vocab_data):
        distractors = [v for v in vocab_data if v != (it, en)]
        selected_distractors = random.sample(distractors, 3)
        choices_it = [it] + [d[0] for d in selected_distractors]
        choices_en = [en] + [d[1] for d in selected_distractors]
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        vocab_json.append({
            "id": f"{scenario_id}-v{i+1}",
            "italian": it,
            "english": en,
            "type": "vocabulary",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Ottimo! '{it}' significa '{en}'. / Great! '{it}' means '{en}'.",
                "incorrect": f"Non è corretto. '{it}' è '{en}'. / Not correct. '{it}' is '{en}'."
            }
        })

    # Phrases (Min 50)
    phrases_data = [
        ("Vorrei degli auricolari", "I would like some earphones"), ("Senza fili", "Wireless"), ("Modello sportivo", "Sports model"),
        ("Uso quotidiano", "Daily use"), ("Ascoltare musica", "To listen to music"), ("Cancellazione del rumore", "Noise cancellation"),
        ("In offerta questa settimana", "On offer this week"), ("Quanto costano?", "How much do they cost?"), ("Ottantanove euro", "Eighty-nine euros"),
        ("Computer portatile", "Laptop computer"), ("Sistema operativo incluso", "Operating system included"), ("Già installato", "Already installed"),
        ("Quanta memoria RAM?", "How much RAM memory?"), ("Sedici gigabyte", "Sixteen gigabytes"), ("Disco SSD", "SSD drive"),
        ("Veloce per il montaggio", "Fast for editing"), ("Uso amatoriale", "Amateur use"), ("Lavoro professionale", "Professional work"),
        ("Modello superiore", "Superior model"), ("Caricabatterie per iPhone", "iPhone charger"), ("Si è rotto", "It broke"),
        ("Sia originale che compatibile", "Both original and compatible"), ("Differenza di prezzo", "Price difference"), ("Venticinque euro", "Twenty-five euros"),
        ("Andare sul sicuro", "To be safe"), ("È compatibile con questo?", "Is it compatible with this?"), ("Quanto dura la batteria?", "How long does the battery last?"),
        ("Ha la garanzia?", "Does it have a warranty?"), ("C'è lo sconto studenti?", "Is there a student discount?"), ("Posso provarlo?", "Can I try it?"),
        ("Dove sono i tablet?", "Where are the tablets?"), ("Mi serve un adattatore", "I need an adapter"), ("Cavo USB-C", "USB-C cable"),
        ("Batteria esterna", "Power bank"), ("Memoria espandibile", "Expandable memory"), ("Schermo touch", "Touch screen"),
        ("Tastiera retroilluminata", "Backlit keyboard"), ("Stampante laser", "Laser printer"), ("Cartucce d'inchiostro", "Ink cartridges"),
        ("Cassa bluetooth", "Bluetooth speaker"), ("Connessione wifi", "Wifi connection"), ("Configurare il dispositivo", "To configure the device"),
        ("Assistenza tecnica", "Technical assistance"), ("Centro riparazioni", "Repair center"), ("È ancora in garanzia", "It's still under warranty"),
        ("Scontrino fiscale", "Tax receipt"), ("Pagamento a rate", "Payment in installments"), ("Tasso zero", "Zero interest"),
        ("Disponibile subito", "Available immediately"), ("Ordinare online", "To order online")
    ]
    
    phrases_json = []
    for i, (it, en) in enumerate(phrases_data):
        distractors = [p for p in phrases_data if p != (it, en)]
        selected_distractors = random.sample(distractors, 3)
        choices_it = [it] + [d[0] for d in selected_distractors]
        choices_en = [en] + [d[1] for d in selected_distractors]
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        phrases_json.append({
            "id": f"{scenario_id}-p{i+1}",
            "italian": it,
            "english": en,
            "type": "phrase",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Ben fatto! '{it}' si traduce '{en}'. / Well done! '{it}' translates to '{en}'.",
                "incorrect": f"Riprova. '{it}' significa '{en}'. / Try again. '{it}' means '{en}'."
            }
        })

    # Sentences (Min 60)
    sentences_data = [
        ("Buongiorno, vorrei degli auricolari bluetooth senza fili.", "Good morning, I would like some wireless bluetooth earphones."),
        ("Cerca un modello sportivo o qualcosa per l'uso quotidiano?", "Are you looking for a sports model or something for daily use?"),
        ("Cerco qualcosa di leggero per ascoltare musica al lavoro.", "I'm looking for something lightweight to listen to music at work."),
        ("Questi hanno un'ottima cancellazione del rumore esterna.", "These have excellent external noise cancellation."),
        ("Sono in offerta questa settimana a un prezzo speciale.", "They are on offer this week at a special price."),
        ("Quanto costano esattamente questi auricolari della Sony?", "How much exactly do these Sony earphones cost?"),
        ("Costano ottantanove euro con lo sconto del venti per cento.", "They cost eighty-nine euros with the twenty percent discount."),
        ("Scusi, questo computer portatile ha il sistema operativo?", "Excuse me, does this laptop have the operating system?"),
        ("Sì, Windows 11 è già installato e configurato per l'uso.", "Yes, Windows 11 is already installed and configured for use."),
        ("Quanta memoria RAM ha questo modello di computer?", "How much RAM memory does this computer model have?"),
        ("Ha sedici gigabyte di RAM e un disco SSD molto veloce.", "It has sixteen gigabytes of RAM and a very fast SSD drive."),
        ("È abbastanza potente per fare del montaggio video amatoriale?", "Is it powerful enough to do some amateur video editing?"),
        ("Per un uso amatoriale va benissimo, è molto reattivo.", "For amateur use it's fine, it's very responsive."),
        ("Se serve per lavoro professionale, le consiglio il superiore.", "If it's for professional work, I recommend the superior one."),
        ("Avete un caricabatterie originale per l'ultimo iPhone?", "Do you have an original charger for the latest iPhone?"),
        ("Il mio caricabatterie si è rotto e ho bisogno di uno nuovo.", "My charger broke and I need a new one."),
        ("Abbiamo sia l'originale Apple che quelli compatibili garantiti.", "We have both the original Apple and guaranteed compatible ones."),
        ("Qual è la differenza di prezzo tra i due modelli?", "What is the price difference between the two models?"),
        ("L'originale costa venticinque euro, il compatibile quindici.", "The original costs twenty-five euros, the compatible fifteen."),
        ("Prendo quello originale, preferisco sempre andare sul sicuro.", "I'll take the original one, I always prefer to be safe."),
        ("Quanto dura la batteria di questo smartphone in conversazione?", "How long does the battery of this smartphone last in conversation?"),
        ("La batteria può durare fino a due giorni con un uso normale.", "The battery can last up to two days with normal use."),
        ("Questo tablet ha la possibilità di inserire una scheda SIM?", "Does this tablet have the possibility to insert a SIM card?"),
        ("Sì, questo è il modello con connessione 5G integrata.", "Yes, this is the model with integrated 5G connection."),
        ("Avete una stampante che sia compatibile con il sistema Mac?", "Do you have a printer that is compatible with the Mac system?"),
        ("Tutte le nostre stampanti laser sono compatibili con Mac e PC.", "All our laser printers are compatible with Mac and PC."),
        ("Mi serve anche un cavo USB lungo almeno due metri.", "I also need a USB cable at least two meters long."),
        ("Ne abbiamo di diverse lunghezze nel reparto accessori.", "We have them in different lengths in the accessories department."),
        ("Questa tastiera è retroilluminata per scrivere al buio?", "Is this keyboard backlit for writing in the dark?"),
        ("Sì, può cambiare anche il colore delle luci sotto i tasti.", "Yes, you can also change the color of the lights under the keys."),
        ("Posso pagare questo computer a rate senza interessi?", "Can I pay for this computer in installments without interest?"),
        ("Sì, abbiamo un finanziamento a tasso zero per dodici mesi.", "Yes, we have zero-interest financing for twelve months."),
        ("Quali documenti servono per aprire la pratica di finanziamento?", "What documents are needed to open the financing file?"),
        ("Serve un documento d'identità valido e il codice fiscale.", "A valid identity document and the tax code are needed."),
        ("La garanzia copre anche i danni accidentali allo schermo?", "Does the warranty also cover accidental damage to the screen?"),
        ("No, la garanzia standard copre solo i difetti di fabbrica.", "No, the standard warranty only covers manufacturing defects."),
        ("Può sottoscrivere un'assicurazione aggiuntiva contro i danni.", "You can take out additional insurance against damage."),
        ("Il mouse è incluso nel prezzo del computer o è a parte?", "Is the mouse included in the price of the computer or separate?"),
        ("In questo modello il mouse wireless è incluso nella scatola.", "In this model, the wireless mouse is included in the box."),
        ("C'è un centro assistenza tecnica qui vicino in città?", "Is there a technical assistance center nearby in the city?"),
        ("Sì, abbiamo il nostro laboratorio riparazioni al primo piano.", "Yes, we have our repair laboratory on the first floor."),
        ("Questa telecamera può registrare video in risoluzione 4K?", "Can this camera record video in 4K resolution?"),
        ("Certamente, ha un sensore di alta qualità e molta memoria.", "Certainly, it has a high-quality sensor and plenty of memory."),
        ("Quanto spazio occupa un minuto di video in alta definizione?", "How much space does one minute of high definition video take?"),
        ("Dipende dalle impostazioni, ma circa duecento megabyte.", "It depends on the settings, but about two hundred megabytes."),
        ("Vorrei vedere degli altoparlanti bluetooth resistenti all'acqua.", "I'd like to see some waterproof bluetooth speakers."),
        ("Questi sono perfetti per essere usati in spiaggia o in piscina.", "These are perfect for being used at the beach or by the pool."),
        ("Si possono collegare due altoparlanti insieme per il suono stereo?", "Can two speakers be connected together for stereo sound?"),
        ("Sì, tramite l'applicazione ufficiale è molto semplice farlo.", "Yes, via the official application it is very simple to do it."),
        ("Mi serve una borsa imbottita per proteggere il mio laptop.", "I need a padded bag to protect my laptop."),
        ("Di quanti pollici è lo schermo del suo computer portatile?", "How many inches is your laptop screen?"),
        ("È un quindici pollici, quindi mi serve una borsa grande.", "It's a fifteen-inch, so I need a large bag."),
        ("Abbiamo diversi modelli in vari colori e materiali resistenti.", "We have different models in various colors and resistant materials."),
        ("Posso avere lo scontrino per la garanzia, per favore?", "Can I have the receipt for the warranty, please?"),
        ("Lo conservi bene, le servirà per qualsiasi assistenza futura.", "Keep it well, you will need it for any future assistance."),
        ("Avete anche delle pellicole protettive per lo smartphone?", "Do you also have protective films for the smartphone?"),
        ("Sì, se vuole possiamo applicarla noi direttamente in negozio.", "Yes, if you want we can apply it ourselves directly in the shop."),
        ("Quanto tempo ci vuole per configurare il nuovo telefono?", "How long does it take to configure the new phone?"),
        ("In circa dieci minuti possiamo trasferire tutti i suoi dati.", "In about ten minutes we can transfer all your data."),
        ("Grazie mille per l'aiuto, siete stati molto professionali.", "Thank you very much for the help, you were very professional.")
    ]
    
    sentences_json = []
    for i, (it, en) in enumerate(sentences_data):
        distractors = [s for s in sentences_data if s != (it, en)]
        selected_distractors = random.sample(distractors, 3)
        choices_it = [it] + [d[0] for d in selected_distractors]
        choices_en = [en] + [d[1] for d in selected_distractors]
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        sentences_json.append({
            "id": f"{scenario_id}-s{i+1}",
            "italian": it,
            "english": en,
            "type": "sentence",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Eccellente! '{it}' significa '{en}'. / Excellent! '{it}' means '{en}'.",
                "incorrect": f"Ops! La traduzione corretta è '{en}'. / Oops! The correct translation is '{en}'."
            }
        })

    with open(os.path.join(base_path, f"shopping_electronics_store_vocabulary.json"), "w", encoding="utf-8") as f:
        json.dump(vocab_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_electronics_store_phrases.json"), "w", encoding="utf-8") as f:
        json.dump(phrases_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_electronics_store_sentences.json"), "w", encoding="utf-8") as f:
        json.dump(sentences_json, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_s47()
