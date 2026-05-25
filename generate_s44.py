import json
import os
import random

def generate_s44():
    scenario_id = "s44"
    base_path = "src/data/exports/shopping/outdoor_market/"
    
    # Vocabulary (Min 50)
    vocab_data = [
        ("mercato", "market"), ("bancarella", "stall"), ("venditore", "seller"), ("cliente", "customer"),
        ("frutta", "fruit"), ("verdura", "vegetables"), ("chilo", "kilo"), ("mezzo chilo", "half kilo"),
        ("etto", "100 grams"), ("ciliegie", "cherries"), ("fragole", "strawberries"), ("pesche", "peaches"),
        ("albicocche", "apricots"), ("uva", "grapes"), ("mele", "apples"), ("pere", "pears"),
        ("arance", "oranges"), ("limoni", "lemons"), ("mandarini", "mandarins"), ("anguria", "watermelon"),
        ("melone", "melon"), ("pomodori", "tomatoes"), ("insalata", "salad"), ("carciofi", "artichokes"),
        ("zucchine", "zucchini"), ("melanzane", "eggplants"), ("peperoni", "peppers"), ("patate", "potatoes"),
        ("cipolle", "onions"), ("aglio", "garlic"), ("carote", "carrots"), ("spinaci", "spinach"),
        ("fagiolini", "green beans"), ("piselli", "peas"), ("fave", "broad beans"), ("zucca", "pumpkin"),
        ("cavolfiore", "cauliflower"), ("broccoli", "broccoli"), ("finocchi", "fennel"), ("sedano", "celery"),
        ("prezzemolo", "parsley"), ("basilico", "basil"), ("sacchetto", "bag"), ("cestino", "basket/punnet"),
        ("cassetta", "crate"), ("bilancia", "scale"), ("prezzo", "price"), ("sconto", "discount"),
        ("fresco", "fresh"), ("locale", "local"), ("biologico", "organic"), ("provenienza", "origin"),
        ("stagione", "season"), ("maturo", "ripe"), ("acerbo", "unripe")
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
                "correct": f"Bravo! '{it}' significa '{en}'. / Well done! '{it}' means '{en}'.",
                "incorrect": f"Sbagliato. '{it}' è '{en}'. / Wrong. '{it}' is '{en}'."
            }
        })

    # Phrases (Min 50)
    phrases_data = [
        ("Quanto costano?", "How much do they cost?"), ("Al chilo", "Per kilo"), ("Ne vuole un cestino?", "Do you want a punnet?"),
        ("Mezzo chilo", "Half a kilo"), ("Due chili di pomodori", "Two kilos of tomatoes"), ("Pomodori da insalata", "Salad tomatoes"),
        ("Colti stamattina", "Picked this morning"), ("Quattro carciofi", "Four artichokes"), ("Quanto le devo?", "How much do I owe you?"),
        ("Sono siciliane?", "Are they Sicilian?"), ("Senza semi", "Seedless"), ("Tre chili", "Three kilos"),
        ("Posso sceglierle io?", "Can I choose them myself?"), ("Prenda il sacchetto", "Take the bag"), ("Ultime cassette!", "Last crates!"),
        ("Tutto a un euro", "Everything for one euro"), ("Se prende tutto", "If you take everything"), ("Affare fatto!", "Deal done!"),
        ("Buona serata!", "Have a good evening!"), ("Frutta fresca", "Fresh fruit"), ("Verdura di stagione", "Seasonal vegetables"),
        ("Direttamente dalla zona", "Directly from the area"), ("Dolcissime!", "Very sweet!"), ("Belle queste ciliegie", "These cherries are beautiful"),
        ("Cosa le è rimasto?", "What do you have left?"), ("Solo queste pesche", "Only these peaches"), ("Un po' d'uva", "A bit of grapes"),
        ("Le faccio tre euro", "I'll give it to you for three euros"), ("Faccia pure lei", "Go ahead (you do it)"), ("Venga a vedere!", "Come and see!"),
        ("Prezzi bassi", "Low prices"), ("Prodotti della terra", "Earth's products"), ("Appena arrivati", "Just arrived"),
        ("Assaggi pure!", "Go ahead and taste!"), ("È molto buono", "It's very good"), ("Me ne dia sei", "Give me six of them"),
        ("Un mazzetto di basilico", "A bunch of basil"), ("Cipolle rosse", "Red onions"), ("Patate novelle", "New potatoes"),
        ("Senza impegno", "No obligation"), ("Prezzo fisso", "Fixed price"), ("Offerta del giorno", "Offer of the day"),
        ("Frutta sciroppata", "Fruit in syrup"), ("Verdura cotta", "Cooked vegetables"), ("Borsa della spesa", "Shopping bag"),
        ("Peso netto", "Net weight"), ("Tutto biologico", "All organic"), ("Coltivato in Italia", "Grown in Italy"),
        ("Gusto naturale", "Natural taste"), ("Fresco di giornata", "Fresh today")
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
                "correct": f"Ottimo! '{it}' si traduce '{en}'. / Great! '{it}' translates to '{en}'.",
                "incorrect": f"Non proprio. '{it}' è '{en}'. / Not quite. '{it}' is '{en}'."
            }
        })

    # Sentences (Min 60)
    sentences_data = [
        ("Guardi che belle queste ciliegie, sono appena arrivate!", "Look how beautiful these cherries are, they just arrived!"),
        ("Quanto costano al chilo i pomodori da insalata?", "How much per kilo are the salad tomatoes?"),
        ("Ne vorrei un cestino da mezzo chilo, grazie.", "I would like a half-kilo punnet, thank you."),
        ("Mi dia due chili di pomodori e quattro carciofi.", "Give me two kilos of tomatoes and four artichokes."),
        ("Questi carciofi li abbiamo colti proprio stamattina.", "We picked these artichokes just this morning."),
        ("Quanto le devo in tutto per questa spesa?", "How much do I owe you in total for these groceries?"),
        ("Queste arance sono siciliane e senza semi.", "These oranges are Sicilian and seedless."),
        ("Ne vorrei tre chili, posso sceglierle io?", "I'd like three kilos, can I choose them myself?"),
        ("Prenda pure il sacchetto lì vicino per la frutta.", "Go ahead and take the bag nearby for the fruit."),
        ("Il prezzo è di un euro e cinquanta al chilo.", "The price is one euro and fifty per kilo."),
        ("Forza ragazzi, ultime cassette rimaste a un euro!", "Come on guys, last crates left for one euro!"),
        ("Cosa le è rimasto di frutta per questa sera?", "What fruit do you have left for this evening?"),
        ("Se prende tutto quello che resta, le faccio tre euro.", "If you take everything that's left, I'll charge you three euros."),
        ("Affare fatto, prendo tutto io e grazie mille.", "Deal, I'll take it all and thank you very much."),
        ("Queste pesche sono dolcissime e molto mature.", "These peaches are very sweet and very ripe."),
        ("Vorrei mezzo chilo di albicocche e un po' d'uva.", "I'd like half a kilo of apricots and some grapes."),
        ("Il mercato chiude tra mezz'ora, approfittatene!", "The market closes in half an hour, take advantage of it!"),
        ("Avete della verdura biologica prodotta localmente?", "Do you have any locally produced organic vegetables?"),
        ("Le patate sono ottime per farle al forno.", "The potatoes are great for baking in the oven."),
        ("Mi serve un mazzetto di prezzemolo e uno di basilico.", "I need a bunch of parsley and one of basil."),
        ("Questi peperoni sono perfetti da fare alla griglia.", "These peppers are perfect for grilling."),
        ("Posso assaggiare un pezzetto di questo melone?", "Can I taste a small piece of this melon?"),
        ("Certo, senta com'è dolce e profumato!", "Sure, taste how sweet and fragrant it is!"),
        ("Vorrei una testa di cavolfiore e dei broccoli.", "I'd like a head of cauliflower and some broccoli."),
        ("Le zucchine sono molto tenere e senza troppi semi.", "The zucchini are very tender and without too many seeds."),
        ("Quanto pesano queste mele in tutto?", "How much do these apples weigh in total?"),
        ("Metta tutto nel sacchetto di carta, per favore.", "Put everything in the paper bag, please."),
        ("Cerco delle melanzane per fare la parmigiana.", "I'm looking for some eggplants to make parmigiana."),
        ("Queste cipolle rosse vengono direttamente da Tropea.", "These red onions come directly from Tropea."),
        ("Avete dei fagiolini freschi da sgranare?", "Do you have fresh green beans to shell?"),
        ("Il venditore è sempre molto cordiale e onesto.", "The seller is always very cordial and honest."),
        ("Preferisco comprare al mercato invece che al supermercato.", "I prefer to buy at the market instead of the supermarket."),
        ("I prezzi del mercato sono spesso più convenienti.", "Market prices are often more affordable."),
        ("C'è molta gente tra le bancarelle stamattina.", "There are many people among the stalls this morning."),
        ("Mi piace l'atmosfera vivace del mercato all'aperto.", "I like the lively atmosphere of the open-air market."),
        ("Ha del resto per una banconota da venti euro?", "Do you have change for a twenty-euro note?"),
        ("Le fragole sono deliziose con un po' di limone.", "Strawberries are delicious with a bit of lemon."),
        ("Cerco dell'insalata novella, molto tenera.", "I'm looking for some very tender spring salad."),
        ("Questi limoni hanno la buccia edibile?", "Do these lemons have edible peel?"),
        ("Si possono mangiare anche i fiori di zucca.", "You can also eat the zucchini flowers."),
        ("Mi dia un chilo di carote e due di patate.", "Give me a kilo of carrots and two of potatoes."),
        ("L'uva nera è più dolce di quella bianca?", "Is the black grapes sweeter than the white ones?"),
        ("Questo melone è troppo acerbo, ne ha uno più maturo?", "This melon is too unripe, do you have a riper one?"),
        ("Le albicocche sono ricche di vitamine.", "Apricots are rich in vitamins."),
        ("Voglio fare una macedonia per il pranzo.", "I want to make a fruit salad for lunch."),
        ("I finocchi sono molto rinfrescanti in estate.", "Fennels are very refreshing in summer."),
        ("Avete dell'aglio fresco o solo quello secco?", "Do you have fresh garlic or only dry ones?"),
        ("Quante arance ci vogliono per fare una spremuta?", "How many oranges does it take to make a juice?"),
        ("Le pere sono molto succose quest'anno.", "The pears are very juicy this year."),
        ("Questo cestino di lamponi quanto viene?", "How much is this punnet of raspberries?"),
        ("Preferisco scegliere la verdura con le mie mani.", "I prefer to choose the vegetables with my own hands."),
        ("Il profumo della frutta fresca è meraviglioso.", "The scent of fresh fruit is wonderful."),
        ("Mi serve dello zenzero per fare una tisana.", "I need some ginger to make a herbal tea."),
        ("Le castagne arrivano solo in autunno.", "Chestnuts only arrive in autumn."),
        ("C'è un banco che vende formaggi locali?", "Is there a stall that sells local cheeses?"),
        ("Posso pagare con Satispay o solo contanti?", "Can I pay with Satispay or only cash?"),
        ("Il parcheggio vicino al mercato è sempre pieno.", "The parking near the market is always full."),
        ("Porto sempre la mia borsa di tela per la spesa.", "I always bring my canvas bag for shopping."),
        ("Grazie per lo sconto, a sabato prossimo!", "Thanks for the discount, see you next Saturday!"),
        ("Buon lavoro e buona giornata a lei!", "Good luck with your work and have a good day!")
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
                "correct": f"Eccellente! '{it}' significa '{en}'. / Excellent! '{it}' means '{en}'.",
                "incorrect": f"Non proprio. La traduzione è '{en}'. / Not quite. The translation is '{en}'."
            }
        })

    with open(os.path.join(base_path, f"shopping_outdoor_market_vocabulary.json"), "w", encoding="utf-8") as f:
        json.dump(vocab_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_outdoor_market_phrases.json"), "w", encoding="utf-8") as f:
        json.dump(phrases_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_outdoor_market_sentences.json"), "w", encoding="utf-8") as f:
        json.dump(sentences_json, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_s44()
