import json
import os
import random

def generate_s43():
    scenario_id = "s43"
    base_path = "src/data/exports/shopping/grocery_store/"
    
    # Vocabulary (Min 50)
    vocab_data = [
        ("prosciutto", "ham"), ("salumi", "cold cuts"), ("etto", "100 grams"), ("formaggio", "cheese"),
        ("pecorino", "pecorino cheese"), ("pane", "bread"), ("latte", "milk"), ("olio", "oil"),
        ("oliva", "olive"), ("corsia", "aisle"), ("corridoio", "aisle/corridor"), ("cassa", "checkout"),
        ("sacchetto", "bag"), ("contanti", "cash"), ("carta", "card"), ("pasta", "pasta"),
        ("riso", "rice"), ("uova", "eggs"), ("burro", "butter"), ("yogurt", "yogurt"),
        ("frutta", "fruit"), ("verdura", "vegetables"), ("carne", "meat"), ("pesce", "fish"),
        ("zucchero", "sugar"), ("sale", "salt"), ("caffè", "coffee"), ("tè", "tea"),
        ("biscotti", "cookies"), ("cereali", "cereals"), ("marmellata", "jam"), ("miele", "honey"),
        ("vino", "wine"), ("birra", "beer"), ("acqua", "water"), ("succo", "juice"),
        ("pomodoro", "tomato"), ("cipolla", "onion"), ("aglio", "garlic"), ("patate", "potatoes"),
        ("mele", "apples"), ("banane", "bananas"), ("arance", "oranges"), ("limone", "lemon"),
        ("scontrino", "receipt"), ("bilancia", "scale"), ("carrello", "cart"), ("cestino", "basket"),
        ("reparto", "department"), ("scadenza", "expiry"), ("offerta", "offer"), ("fresco", "fresh"),
        ("surgelati", "frozen foods"), ("scatolame", "canned goods"), ("bevande", "drinks")
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
            "type": "vocabulary",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Ottimo! '{it}' significa '{en}'. / Great! '{it}' means '{en}'.",
                "incorrect": f"Ops! '{it}' si traduce '{en}'. / Oops! '{it}' translates to '{en}'."
            }
        })

    # Phrases (Min 50)
    phrases_data = [
        ("Vorrei un etto", "I would like 100g"), ("Prosciutto crudo", "Raw ham"), ("Tagliato fine", "Thinly sliced"),
        ("Desidera altro?", "Anything else?"), ("Basta così", "That's all"), ("Dove posso trovare...?", "Where can I find...?"),
        ("Corsia quattro", "Aisle four"), ("Metà corridoio", "Middle of the aisle"), ("A lunga conservazione", "UHT / Long-life"),
        ("Vicino alla pasta", "Near the pasta"), ("Ha la carta fedeltà?", "Do you have a loyalty card?"), ("Paga in contanti?", "Paying in cash?"),
        ("Con la carta", "With the card"), ("Serve il sacchetto?", "Do you need a bag?"), ("Uno biodegradabile", "A biodegradable one"),
        ("Buona giornata!", "Have a good day!"), ("Al banco dei salumi", "At the deli counter"), ("Duecento grammi", "Two hundred grams"),
        ("Un pezzetto di pecorino", "A small piece of pecorino"), ("Olio d'oliva", "Olive oil"), ("Corsia in fondo", "Back aisle"),
        ("Prezzo al chilo", "Price per kilo"), ("In offerta speciale", "On special offer"), ("Frutta di stagione", "Seasonal fruit"),
        ("Verdura fresca", "Fresh vegetables"), ("Reparto surgelati", "Frozen food department"), ("Data di scadenza", "Expiry date"),
        ("Prendere il carrello", "To take the cart"), ("Mettere nel cestino", "To put in the basket"), ("Fare la spesa", "To go grocery shopping"),
        ("Lista della spesa", "Shopping list"), ("Quanto pesa?", "How much does it weigh?"), ("Pesare sulla bilancia", "To weigh on the scale"),
        ("Pane appena sfornato", "Freshly baked bread"), ("Latte intero", "Whole milk"), ("Latte scremato", "Skimmed milk"),
        ("Uova biologiche", "Organic eggs"), ("Succo di frutta", "Fruit juice"), ("Acqua naturale", "Still water"),
        ("Acqua frizzante", "Sparkling water"), ("Vino rosso", "Red wine"), ("Vino bianco", "White wine"),
        ("Scontrino fiscale", "Sales receipt"), ("Resto in monete", "Change in coins"), ("Banconota da dieci", "Ten-euro bill"),
        ("Cassa veloce", "Self-checkout / Express"), ("Tessera punti", "Points card"), ("Prodotti locali", "Local products"),
        ("Sotto vuoto", "Vacuum packed"), ("Ben cotto", "Well done / Well cooked")
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
            "type": "phrase",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Eccellente! '{it}' è '{en}'. / Excellent! '{it}' is '{en}'.",
                "incorrect": f"Riprova. '{it}' significa '{en}'. / Try again. '{it}' means '{en}'."
            }
        })

    # Sentences (Min 60)
    sentences_data = [
        ("Vorrei un etto di prosciutto crudo, per favore.", "I would like 100g of raw ham, please."),
        ("Lo vuole tagliato molto fine o più spesso?", "Do you want it sliced very thin or thicker?"),
        ("Ne prendo un pezzetto, circa duecento grammi.", "I'll take a piece, about two hundred grams."),
        ("Dove posso trovare l'olio d'oliva extra vergine?", "Where can I find extra virgin olive oil?"),
        ("L'olio è nella corsia quattro, a metà corridoio.", "The oil is in aisle four, in the middle of the aisle."),
        ("Il latte si trova vicino al reparto frigo.", "The milk is located near the refrigerated section."),
        ("Ha la carta fedeltà per raccogliere i punti?", "Do you have a loyalty card to collect points?"),
        ("Paga con la carta o preferisce i contanti?", "Are you paying by card or do you prefer cash?"),
        ("Mi serve un sacchetto biodegradabile, grazie.", "I need a biodegradable bag, thank you."),
        ("Quanto costa al chilo questo formaggio pecorino?", "How much per kilo does this pecorino cheese cost?"),
        ("Questa verdura non mi sembra molto fresca.", "This vegetable doesn't seem very fresh to me."),
        ("C'è un'offerta speciale su questo tipo di pasta.", "There's a special offer on this type of pasta."),
        ("Dove sono i carrelli della spesa?", "Where are the shopping carts?"),
        ("Deve pesare la frutta prima di andare alla cassa.", "You must weigh the fruit before going to the checkout."),
        ("Ho dimenticato di prendere le uova.", "I forgot to get the eggs."),
        ("C'è molta coda alla cassa stamattina.", "There is a long line at the checkout this morning."),
        ("Il pane appena sfornato profuma moltissimo.", "The freshly baked bread smells great."),
        ("Vorrei una bottiglia di vino rosso toscano.", "I would like a bottle of Tuscan red wine."),
        ("Avete prodotti senza glutine in questo negozio?", "Do you have gluten-free products in this store?"),
        ("Controlli sempre la data di scadenza sui prodotti.", "Always check the expiry date on products."),
        ("Mi serve un cestino perché devo prendere poco.", "I need a basket because I only need a few things."),
        ("Il reparto surgelati è in fondo a destra.", "The frozen food department is at the back on the right."),
        ("Vorrei mezzo chilo di macinato di manzo.", "I would like half a kilo of ground beef."),
        ("Questi pomodori sono molto maturi e saporiti.", "These tomatoes are very ripe and tasty."),
        ("Posso avere lo scontrino, per favore?", "Can I have the receipt, please?"),
        ("Mi dispiace, abbiamo finito il latte intero.", "I'm sorry, we've run out of whole milk."),
        ("C'è uno sconto del venti per cento oggi.", "There is a twenty percent discount today."),
        ("Quanta acqua devo comprare per la settimana?", "How much water do I need to buy for the week?"),
        ("Preferisco i biscotti integrali per colazione.", "I prefer whole grain cookies for breakfast."),
        ("Questo succo di frutta è senza zuccheri aggiunti.", "This fruit juice has no added sugars."),
        ("Posso pagare con il cellulare?", "Can I pay with my phone?"),
        ("Dov'è il reparto della cura della persona?", "Where is the personal care department?"),
        ("Mi servono delle pile stilo per il telecomando.", "I need some AA batteries for the remote control."),
        ("Il tonno in scatola è in offerta 'prendi due'.", "The canned tuna is on a 'buy two' offer."),
        ("Vorrei del parmigiano reggiano stagionato.", "I would like some aged Parmigiano Reggiano."),
        ("Questo yogurt è alla fragola o ai cereali?", "Is this yogurt strawberry or cereal flavored?"),
        ("Le mele sono nel reparto ortofrutta.", "The apples are in the fruit and vegetable section."),
        ("Serve una moneta da un euro per il carrello.", "A one-euro coin is needed for the cart."),
        ("Il sapone per i piatti è finito.", "The dish soap is finished."),
        ("Vorrei provare questa nuova marca di caffè.", "I would like to try this new brand of coffee."),
        ("La marmellata è nel corridoio delle colazioni.", "The jam is in the breakfast aisle."),
        ("Quante arance ci sono in questo sacco?", "How many oranges are in this bag?"),
        ("Il riso per risotti è di ottima qualità.", "The risotto rice is of excellent quality."),
        ("Potrebbe aiutarmi a raggiungere quello scaffale?", "Could you help me reach that shelf?"),
        ("C'è un errore sullo scontrino, credo.", "There's an error on the receipt, I think."),
        ("Vorrei restituire questo prodotto difettoso.", "I would like to return this defective product."),
        ("Il supermercato chiude alle ore ventuno.", "The supermarket closes at 9 PM."),
        ("La domenica mattina siamo sempre aperti.", "We are always open on Sunday mornings."),
        ("Prenda pure un volantino delle offerte.", "Go ahead and take a flyer of the offers."),
        ("Il burro è nel banco frigo laggiù.", "The butter is in the refrigerated counter over there."),
        ("Cercavo del sale marino integrale.", "I was looking for whole sea salt."),
        ("Le buste della spesa sono sotto la cassa.", "The shopping bags are under the checkout counter."),
        ("Il tonno è nel reparto pesce in scatola.", "The tuna is in the canned fish department."),
        ("Mi serve della carta igienica.", "I need some toilet paper."),
        ("Il detersivo è troppo pesante da portare.", "The detergent is too heavy to carry."),
        ("Vorrei dei panini al latte morbidi.", "I would like some soft milk rolls."),
        ("Avete del pesce fresco oggi?", "Do you have fresh fish today?"),
        ("Questo miele è prodotto localmente.", "This honey is produced locally."),
        ("I cereali sono molto croccanti.", "The cereals are very crunchy."),
        ("Grazie e arrivederci alla prossima!", "Thank you and see you next time!")
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
            "type": "sentence",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Perfetto! '{it}' significa '{en}'. / Perfect! '{it}' means '{en}'.",
                "incorrect": f"No, la traduzione corretta è '{en}'. / No, the correct translation is '{en}'."
            }
        })

    with open(os.path.join(base_path, f"shopping_grocery_store_vocabulary.json"), "w", encoding="utf-8") as f:
        json.dump(vocab_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_grocery_store_phrases.json"), "w", encoding="utf-8") as f:
        json.dump(phrases_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_grocery_store_sentences.json"), "w", encoding="utf-8") as f:
        json.dump(sentences_json, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_s43()
