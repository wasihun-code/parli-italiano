import json
import os

def generate_s41():
    scenario_id = "s41"
    base_path = "src/data/exports/shopping/clothing_store/"
    
    # Vocabulary (Min 50)
    vocab_data = [
        ("pantaloni", "pants"), ("taglia", "size"), ("stretti", "tight"), ("magazzino", "stockroom"),
        ("camerini", "fitting rooms"), ("giacche", "jackets"), ("camicia", "shirt"), ("lino", "linen"),
        ("costo", "cost"), ("saldi", "sales"), ("sconto", "discount"), ("bianco", "white"),
        ("celeste", "light blue"), ("abito", "dress/suit"), ("matrimonio", "wedding"), ("elegante", "elegant"),
        ("formale", "formal"), ("floreale", "floral"), ("moda", "fashion"), ("gonna", "skirt"),
        ("maglione", "sweater"), ("calze", "socks"), ("cappotto", "coat"), ("sciarpa", "scarf"),
        ("guanti", "gloves"), ("cappello", "hat"), ("cintura", "belt"), ("borsa", "bag"),
        ("portafoglio", "wallet"), ("specchio", "mirror"), ("commesso", "shop assistant"), ("cliente", "customer"),
        ("cassa", "cash desk"), ("scontrino", "receipt"), ("bancomat", "debit card"), ("contanti", "cash"),
        ("provare", "to try on"), ("cambiare", "to exchange"), ("reso", "return"), ("rimborso", "refund"),
        ("seta", "silk"), ("cotone", "cotton"), ("lana", "wool"), ("velluto", "velvet"),
        ("pelle", "leather"), ("jeans", "jeans"), ("maglietta", "t-shirt"), ("polo", "polo shirt"),
        ("canottiera", "tank top"), ("pigiama", "pajamas"), ("intimo", "underwear"), ("costume", "swimsuit"),
        ("occhiali", "glasses"), ("orecchini", "earrings"), ("collana", "necklace")
    ]
    
    vocab_json = []
    for i, (it, en) in enumerate(vocab_data):
        distractors = [v for v in vocab_data if v != (it, en)]
        import random
        selected_distractors = random.sample(distractors, 3)
        choices_it = [it] + [d[0] for d in selected_distractors]
        choices_en = [en] + [d[1] for d in selected_distractors]
        
        # Shuffle together
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        
        vocab_json.append({
            "id": f"{scenario_id}-v{i+1}",
            "type": "vocabulary",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Eccellente! '{it}' significa '{en}'. / Excellent! '{it}' means '{en}'.",
                "incorrect": f"Spiacente! '{it}' significa '{en}'. / Sorry! '{it}' means '{en}'."
            }
        })

    # Phrases (Min 50)
    phrases_data = [
        ("Quanto costa?", "How much does it cost?"), ("Posso provare?", "Can I try it on?"),
        ("Che taglia?", "What size?"), ("Taglia media", "Medium size"), ("In magazzino", "In stock"),
        ("I saldi", "The sales"), ("Lo sconto", "The discount"), ("Prezzo finale", "Final price"),
        ("Camerini liberi", "Free fitting rooms"), ("Cerco un abito", "I'm looking for a dress"),
        ("Troppo stretto", "Too tight"), ("Un po' largo", "A bit loose"), ("Senza maniche", "Sleeveless"),
        ("Maniche lunghe", "Long sleeves"), ("In saldo", "On sale"), ("Nuova collezione", "New collection"),
        ("Tutto esaurito", "Sold out"), ("Disponibile in blu", "Available in blue"), ("Puro cotone", "Pure cotton"),
        ("Solo bianco", "Only white"), ("Taglia 42", "Size 42"), ("Una taglia in più", "A size up"),
        ("Una taglia in meno", "A size down"), ("Dove sono i camerini?", "Where are the fitting rooms?"),
        ("Vicino alle giacche", "Near the jackets"), ("In fondo a sinistra", "In the back on the left"),
        ("Vado a controllare", "I'll go check"), ("Elegante ma informale", "Elegant but informal"),
        ("Di moda quest'anno", "Fashionable this year"), ("Abito floreale", "Floral dress"),
        ("Camicia di lino", "Linen shirt"), ("Venti per cento", "Twenty percent"), ("Sconto del 20%", "20% discount"),
        ("Celeste chiaro", "Light blue"), ("Ottimo prezzo", "Great price"), ("Veste bene", "It fits well"),
        ("Veste piccolo", "It runs small"), ("Veste grande", "It runs large"), ("Posso cambiare?", "Can I exchange it?"),
        ("Ho lo scontrino", "I have the receipt"), ("Pagamento con carta", "Payment by card"),
        ("Solo contanti", "Only cash"), ("Borsa di pelle", "Leather bag"), ("Cintura nera", "Black belt"),
        ("Giacca estiva", "Summer jacket"), ("Cappotto invernale", "Winter coat"), ("Sciarpa di lana", "Woolen scarf"),
        ("Guanti caldi", "Warm gloves"), ("Seta naturale", "Natural silk"), ("Provatelo pure", "Go ahead and try it")
    ]
    
    phrases_json = []
    for i, (it, en) in enumerate(phrases_data):
        distractors = [p for p in phrases_data if p != (it, en)]
        import random
        selected_distractors = random.sample(distractors, 3)
        choices_it = [it] + [d[0] for d in selected_distractors]
        choices_en = [en] + [d[1] for d in selected_distractors]
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        phrases_json.append({
            "id": f"{scenario_id}-p{i+1}",
            "type": "phrase",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Ottimo! '{it}' si traduce '{en}'. / Great! '{it}' translates to '{en}'.",
                "incorrect": f"Non proprio. '{it}' è '{en}'. / Not quite. '{it}' is '{en}'."
            }
        })

    # Sentences (Min 60)
    sentences_data = [
        ("Vorrei provare questa camicia.", "I would like to try on this shirt."),
        ("Avrebbe una taglia in più?", "Would you have a size up?"),
        ("Questi pantaloni sono troppo stretti.", "These pants are too tight."),
        ("Dove posso trovare i camerini?", "Where can I find the fitting rooms?"),
        ("I camerini sono in fondo a sinistra.", "The fitting rooms are in the back on the left."),
        ("Quanto costa questo abito elegante?", "How much does this elegant dress cost?"),
        ("C'è uno sconto su questa giacca?", "Is there a discount on this jacket?"),
        ("I saldi iniziano la prossima settimana.", "The sales start next week."),
        ("Questa camicia è disponibile in blu?", "Is this shirt available in blue?"),
        ("Abbiamo solo il bianco e il celeste.", "We only have white and light blue."),
        ("Cerco un abito per un matrimonio.", "I am looking for a dress for a wedding."),
        ("Questo abito floreale è molto di moda.", "This floral dress is very fashionable."),
        ("Posso pagare con il bancomat?", "Can I pay with a debit card?"),
        ("Accettate solo pagamenti in contanti?", "Do you only accept cash payments?"),
        ("Vado a controllare in magazzino.", "I'll go check in the stockroom."),
        ("Penso che mi serva una 44.", "I think I need a 44."),
        ("La taglia 42 mi stringe un po'.", "Size 42 is a bit tight on me."),
        ("Questo tessuto è puro lino.", "This fabric is pure linen."),
        ("Il prezzo finale è 36 euro.", "The final price is 36 euros."),
        ("Vorrei restituire questo maglione.", "I would like to return this sweater."),
        ("Ho perso lo scontrino fiscale.", "I lost the tax receipt."),
        ("Posso avere un rimborso?", "Can I have a refund?"),
        ("Preferisco la taglia media.", "I prefer the medium size."),
        ("Questa gonna mi sta molto bene.", "This skirt fits me very well."),
        ("Il colore non mi piace molto.", "I don't like the color very much."),
        ("C'è una taglia più piccola?", "Is there a smaller size?"),
        ("Avete questa maglietta in cotone?", "Do you have this t-shirt in cotton?"),
        ("I camerini sono occupati al momento.", "The fitting rooms are occupied at the moment."),
        ("Posso provare anche queste scarpe?", "Can I try these shoes too?"),
        ("Questa giacca è troppo cara.", "This jacket is too expensive."),
        ("C'è qualcosa di più economico?", "Is there something cheaper?"),
        ("Il commesso è stato molto gentile.", "The shop assistant was very kind."),
        ("Veste un po' largo in vita.", "It fits a bit loose at the waist."),
        ("Le maniche sono troppo lunghe.", "The sleeves are too long."),
        ("Cerco qualcosa di meno formale.", "I am looking for something less formal."),
        ("Questo abito è perfetto per me.", "This dress is perfect for me."),
        ("Posso vedere quella borsa in vetrina?", "Can I see that bag in the window?"),
        ("È un regalo per una mia amica.", "It is a gift for a friend of mine."),
        ("Potrebbe farmi un pacchetto regalo?", "Could you make a gift wrap for me?"),
        ("L'armadio è pieno di vestiti nuovi.", "The closet is full of new clothes."),
        ("Mi serve una cintura di pelle nera.", "I need a black leather belt."),
        ("Queste calze sono molto calde.", "These socks are very warm."),
        ("Il cappotto è in offerta speciale.", "The coat is on special offer."),
        ("Non trovo la mia taglia usuale.", "I can't find my usual size."),
        ("Questo maglione punge un po'.", "This sweater itches a bit."),
        ("La seta è di ottima qualità.", "The silk is of excellent quality."),
        ("Cerco una sciarpa da abbinare.", "I'm looking for a scarf to match."),
        ("I guanti sono troppo piccoli.", "The gloves are too small."),
        ("Quanto viene con lo sconto?", "How much is it with the discount?"),
        ("Voglio provare quel vestito rosso.", "I want to try on that red dress."),
        ("I pantaloni sono in magazzino.", "The pants are in the stockroom."),
        ("Mi piace molto questo stile.", "I really like this style."),
        ("È disponibile in altri colori?", "Is it available in other colors?"),
        ("La cassa è laggiù a destra.", "The cash desk is over there on the right."),
        ("Serve la tessera fedeltà?", "Do I need the loyalty card?"),
        ("Ho dimenticato il portafoglio.", "I forgot my wallet."),
        ("Torni a trovarci presto!", "Come back and see us soon!"),
        ("Buona giornata e grazie mille.", "Good day and thank you very much."),
        ("I saldi finiscono domani.", "The sales end tomorrow."),
        ("Questo vestito è troppo lungo.", "This dress is too long.")
    ]
    
    sentences_json = []
    for i, (it, en) in enumerate(sentences_data):
        distractors = [s for s in sentences_data if s != (it, en)]
        import random
        selected_distractors = random.sample(distractors, 3)
        choices_it = [it] + [d[0] for d in selected_distractors]
        choices_en = [en] + [d[1] for d in selected_distractors]
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        sentences_json.append({
            "id": f"{scenario_id}-s{i+1}",
            "type": "sentence",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Ben fatto! '{it}' significa '{en}'. / Well done! '{it}' means '{en}'.",
                "incorrect": f"Riprova! La traduzione è '{en}'. / Try again! The translation is '{en}'."
            }
        })

    with open(os.path.join(base_path, f"shopping_clothing_store_vocabulary.json"), "w", encoding="utf-8") as f:
        json.dump(vocab_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_clothing_store_phrases.json"), "w", encoding="utf-8") as f:
        json.dump(phrases_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_clothing_store_sentences.json"), "w", encoding="utf-8") as f:
        json.dump(sentences_json, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_s41()
