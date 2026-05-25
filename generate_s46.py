import json
import os
import random

def generate_s46():
    scenario_id = "s46"
    base_path = "src/data/exports/shopping/souvenir_shop/"
    
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    # Vocabulary (Min 50)
    vocab_data = [
        ("souvenir", "souvenir"), ("regalo", "gift"), ("cartolina", "postcard"), ("calamita", "magnet"),
        ("francobollo", "stamp"), ("maglietta", "t-shirt"), ("ceramica", "ceramic"), ("piatto", "plate"),
        ("tazza", "mug"), ("portachiavi", "keychain"), ("statuetta", "figurine"), ("miniatura", "miniature"),
        ("artigianato", "handicraft"), ("fatto a mano", "handmade"), ("artistico", "artistic"), ("tradizionale", "traditional"),
        ("locale", "local"), ("tipico", "typical"), ("vetro", "glass"), ("pelle", "leather"),
        ("seta", "silk"), ("legno", "wood"), ("maschera", "mask"), ("veneziano", "Venetian"),
        ("fiorentino", "Florentine"), ("romano", "Roman"), ("napoletano", "Neapolitan"), ("siciliano", "Sicilian"),
        ("colore", "color"), ("taglia", "size"), ("piccolo", "small"), ("grande", "large"),
        ("medio", "medium"), ("prezzo", "price"), ("sconto", "discount"), ("offerta", "offer"),
        ("costoso", "expensive"), ("economico", "cheap"), ("fragile", "fragile"), ("delicato", "delicate"),
        ("imballaggio", "packaging"), ("scatola", "box"), ("busta", "bag/envelope"), ("scontrino", "receipt"),
        ("cassa", "cash register"), ("contanti", "cash"), ("carta", "card"), ("pagare", "to pay"),
        ("comprare", "to buy"), ("scegliere", "to choose"), ("consiglio", "advice"), ("vetrina", "store window"),
        ("scaffale", "shelf"), ("entrata", "entrance"), ("uscita", "exit")
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
        ("Quanto costa?", "How much is it?"), ("Quanto costano queste?", "How much do these cost?"), ("Quella grande", "The large one"),
        ("Quella piccola", "The small one"), ("Cinquanta centesimi", "Fifty cents"), ("Un euro", "One euro"),
        ("Ne prendo tre", "I'll take three"), ("Avete i francobolli?", "Do you have stamps?"), ("Solo per l'Europa", "Only for Europe"),
        ("Me ne dia quattro", "Give me four of them"), ("A forma di Colosseo", "In the shape of the Colosseum"), ("Mi fa uno sconto?", "Will you give me a discount?"),
        ("Se ne prende tre", "If you take three"), ("Quaranta euro in tutto", "Forty euros in total"), ("Taglie e colori diversi", "Different sizes and colors"),
        ("Scelga pure quelle", "Go ahead and choose those"), ("Fatto a mano", "Handmade"), ("Ceramica artigianale", "Artisanal ceramic"),
        ("Dipinto a mano", "Hand-painted"), ("Molto delicato", "Very delicate"), ("Mettere in valigia", "To put in the suitcase"),
        ("Imballarlo bene", "To pack it well"), ("Abbondante pluriball", "Abundant bubble wrap"), ("Scatola rigida", "Rigid box"),
        ("Allora lo prendo", "Then I'll take it"), ("Vorrei un portachiavi", "I'd like a keychain"), ("Cosa mi consiglia?", "What do you recommend?"),
        ("Un regalo per un amico", "A gift for a friend"), ("Qualcosa di tipico", "Something typical"), ("Della zona", "From the area"),
        ("In offerta speciale", "On special offer"), ("Prezzo fisso", "Fixed price"), ("Posso pagare con carta?", "Can I pay by card?"),
        ("Solo in contanti", "Cash only"), ("Dov'è la cassa?", "Where is the cash register?"), ("Mi serve la ricevuta", "I need the receipt"),
        ("Una busta, per favore", "A bag, please"), ("È molto caro", "It's very expensive"), ("È un buon affare", "It's a good deal"),
        ("Guardi pure", "Feel free to look"), ("Posso toccare?", "Can I touch?"), ("Non si preoccupi", "Don't worry"),
        ("Ecco il resto", "Here is the change"), ("Grazie mille", "Many thanks"), ("Arrivederci", "Goodbye"),
        ("Buona giornata", "Have a good day"), ("Tutto qui, grazie", "That's all, thank you"), ("Volevo vedere quello", "I wanted to see that one"),
        ("Di che materiale è?", "What material is it?"), ("È vera pelle?", "Is it real leather?")
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
        ("Buongiorno, quanto costano queste cartoline?", "Good morning, how much do these postcards cost?"),
        ("Quelle grandi costano un euro, quelle piccole cinquanta centesimi.", "The large ones cost one euro, the small ones fifty cents."),
        ("Ne prendo tre grandi e due piccole, grazie.", "I'll take three large ones and two small ones, thank you."),
        ("Avete anche i francobolli per spedirle all'estero?", "Do you also have stamps to send them abroad?"),
        ("Sì, ma purtroppo abbiamo solo quelli per l'Europa.", "Yes, but unfortunately we only have those for Europe."),
        ("Me ne dia quattro, per favore, e anche questa calamita.", "Give me four of them, please, and also this magnet."),
        ("Vorrei la calamita a forma di Colosseo, è molto bella.", "I would like the magnet in the shape of the Colosseum, it's very beautiful."),
        ("Se prendo tre di queste magliette, mi fa un po' di sconto?", "If I take three of these t-shirts, will you give me a discount?"),
        ("Le magliette costano quindici euro l'una nel nostro negozio.", "The t-shirts cost fifteen euros each in our shop."),
        ("Se ne prende tre, gliele posso fare quaranta euro in tutto.", "If you take three, I can do them for forty euros in total."),
        ("Posso scegliere taglie e colori diversi per le magliette?", "Can I choose different sizes and colors for the t-shirts?"),
        ("Certamente, scelga pure tutte quelle che preferisce.", "Certainly, go ahead and choose all the ones you prefer."),
        ("Questo piatto in ceramica è fatto a mano da artigiani?", "Is this ceramic plate handmade by artisans?"),
        ("Sì, è ceramica artigianale di Deruta, dipinta a mano.", "Yes, it is artisanal ceramic from Deruta, hand-painted."),
        ("È un oggetto molto delicato, devo metterlo in valigia.", "It's a very delicate object, I have to put it in my suitcase."),
        ("Potrebbe imballarlo bene per evitare che si rompa?", "Could you pack it well to prevent it from breaking?"),
        ("Lo avvolgo in abbondante pluriball e lo metto in una scatola.", "I'll wrap it in plenty of bubble wrap and put it in a box."),
        ("Userò una scatola rigida per proteggere meglio la ceramica.", "I'll use a rigid box to better protect the ceramic."),
        ("Grazie mille per la sua gentilezza, allora lo prendo.", "Thank you very much for your kindness, then I'll take it."),
        ("Cerco un regalo speciale per mia madre, cosa mi consiglia?", "I'm looking for a special gift for my mother, what do you recommend?"),
        ("Abbiamo degli splendidi foulard di seta prodotti a Como.", "We have some splendid silk scarves produced in Como."),
        ("Preferisce qualcosa in pelle o un oggetto decorativo?", "Do you prefer something in leather or a decorative object?"),
        ("Questi portachiavi sono fatti con il cuoio toscano originale.", "These keychains are made with original Tuscan leather."),
        ("Vorrei vedere quella statuetta sulla mensola in alto.", "I'd like to see that figurine on the top shelf."),
        ("È una miniatura in marmo di Carrara molto pregiata.", "It is a very precious miniature in Carrara marble."),
        ("Qual è il prezzo finale di questo set di tazze?", "What is the final price of this set of mugs?"),
        ("C'è un'offerta speciale se acquista anche il vassoio coordinato.", "There is a special offer if you also buy the matching tray."),
        ("Posso pagare con la carta di credito o accettate solo contanti?", "Can I pay by credit card or do you only accept cash?"),
        ("Accettiamo tutte le principali carte, non si preoccupi.", "We accept all major cards, don't worry."),
        ("Mi serve lo scontrino per la detrazione fiscale, grazie.", "I need the receipt for the tax deduction, thank you."),
        ("Può mettermi tutto in una busta robusta, per favore?", "Can you put everything in a sturdy bag, please?"),
        ("Questo articolo è prodotto localmente o è d'importazione?", "Is this item produced locally or is it imported?"),
        ("È tutto artigianato locale garantito al cento per cento.", "It's all guaranteed 100% local handicraft."),
        ("Vorrei tre di questi piccoli souvenir a forma di torre.", "I would like three of these small tower-shaped souvenirs."),
        ("Avete magliette della nazionale italiana di calcio?", "Do you have Italian national football team t-shirts?"),
        ("Sì, sono nell'angolo in fondo a sinistra del negozio.", "Yes, they are in the back left corner of the shop."),
        ("C'è una taglia più grande per questo modello di maglia?", "Is there a larger size for this shirt model?"),
        ("Controllo subito in magazzino se è rimasta un'ultima XL.", "I'll check the warehouse immediately if there's one last XL left."),
        ("Questa maschera veneziana è veramente stupenda e colorata.", "This Venetian mask is truly wonderful and colorful."),
        ("È fatta in cartapesta secondo l'antica tradizione.", "It is made of papier-mâché according to ancient tradition."),
        ("Si può appendere al muro o è solo da indossare?", "Can it be hung on the wall or is it only to be worn?"),
        ("Ha un gancio sul retro proprio per essere appesa.", "It has a hook on the back specifically to be hung."),
        ("Il prezzo mi sembra un po' alto, è possibile trattare?", "The price seems a bit high to me, is it possible to negotiate?"),
        ("Sui prodotti artigianali purtroppo il prezzo è fisso.", "On artisanal products, unfortunately, the price is fixed."),
        ("Però posso regalarle una cartolina a sua scelta.", "However, I can give you a postcard of your choice as a gift."),
        ("Va bene, è molto gentile, accetto volentieri.", "Okay, you're very kind, I'll gladly accept."),
        ("Dov'è l'uscita del negozio, per favore?", "Where is the exit of the shop, please?"),
        ("Deve passare davanti alla cassa e poi girare a destra.", "You must pass in front of the cash register and then turn right."),
        ("Grazie per i consigli, tornerò sicuramente a trovarvi.", "Thanks for the advice, I will definitely come back to visit you."),
        ("Buon proseguimento di vacanza in Italia!", "Have a nice continuation of your holiday in Italy!"),
        ("Questo portafoglio in pelle è molto morbido al tatto.", "This leather wallet is very soft to the touch."),
        ("È disponibile anche in nero o solo in marrone?", "Is it also available in black or only in brown?"),
        ("C'è anche nero e blu scuro, glieli mostro subito.", "There's also black and dark blue, I'll show them to you right away."),
        ("Le cartoline sono già affrancate o devo comprare i francobolli?", "Are the postcards already stamped or do I have to buy stamps?"),
        ("Deve comprare i francobolli a parte, costano un euro e dieci.", "You have to buy the stamps separately, they cost one euro and ten."),
        ("Mi dà anche una penna per scrivere i saluti?", "Can you also give me a pen to write the greetings?"),
        ("Certo, ne abbiamo con il nome della città sopra.", "Sure, we have some with the name of the city on them."),
        ("Quanto tempo ci vuole per spedire un pacco in America?", "How long does it take to ship a package to America?"),
        ("Circa due settimane con la spedizione ordinaria.", "About two weeks with ordinary shipping."),
        ("Preferisco portarlo io in valigia, è più sicuro.", "I prefer to carry it myself in my suitcase, it's safer.")
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

    with open(os.path.join(base_path, f"shopping_souvenir_shop_vocabulary.json"), "w", encoding="utf-8") as f:
        json.dump(vocab_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_souvenir_shop_phrases.json"), "w", encoding="utf-8") as f:
        json.dump(phrases_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_souvenir_shop_sentences.json"), "w", encoding="utf-8") as f:
        json.dump(sentences_json, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_s46()
