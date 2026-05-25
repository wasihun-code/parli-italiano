import json
import os
import random

def generate_s42():
    scenario_id = "s42"
    base_path = "src/data/exports/shopping/shoe_store/"
    
    # Vocabulary (Min 50)
    vocab_data = [
        ("scarpe", "shoes"), ("ginnastica", "gym/sneakers"), ("numero", "size (shoes)"), ("marca", "brand"),
        ("stretto", "tight"), ("punta", "toe (of shoe)"), ("eleganti", "elegant"), ("pelle", "leather"),
        ("lacci", "laces"), ("stringato", "lace-up"), ("calzascarpe", "shoehorn"), ("tacco", "heel"),
        ("scomode", "uncomfortable"), ("confortevoli", "comfortable"), ("stabili", "stable"), ("sandali", "sandals"),
        ("stivali", "boots"), ("pantofole", "slippers"), ("suola", "sole"), ("pianta larga", "wide fit"),
        ("scamosciato", "suede"), ("impermeabile", "waterproof"), ("soletta", "insole"), ("lucido", "polished"),
        ("opaco", "matte"), ("mocassini", "loafers"), ("ballerine", "ballet flats"), ("zeppa", "wedge"),
        ("calzature", "footwear"), ("stringhe", "shoelaces"), ("caviglia", "ankle"), ("tallone", "heel (body part)"),
        ("collo del piede", "instep"), ("gomma", "rubber"), ("cuoio", "leather/hide"), ("vernice", "patent leather"),
        ("sportive", "sporty"), ("trekking", "hiking"), ("corsa", "running"), ("calcio", "soccer"),
        ("tennis", "tennis"), ("mare", "sea/beach"), ("scogli", "rocks"), ("neve", "snow"),
        ("pioggia", "rain"), ("fango", "mud"), ("pulizia", "cleaning"), ("spazzola", "brush"),
        ("crema", "cream"), ("lucidante", "polishing"), ("panno", "cloth"), ("scatola", "box"),
        ("commesso", "shop assistant"), ("prova", "trial/trying on"), ("vetrina", "window display")
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
                "incorrect": f"Non è corretto. '{it}' è '{en}'. / Incorrect. '{it}' is '{en}'."
            }
        })

    # Phrases (Min 50)
    phrases_data = [
        ("Che numero porta?", "What size do you wear?"), ("Porto il 42", "I wear size 42"),
        ("In vetrina", "In the window"), ("Scarpe da ginnastica", "Sneakers"), ("Un po' stretto", "A bit tight"),
        ("Meglio il 42 e mezzo", "42.5 is better"), ("Scarpe eleganti", "Formal shoes"), ("Modello stringato", "Lace-up model"),
        ("Vuole un calzascarpe?", "Do you want a shoehorn?"), ("Scarpe col tacco", "High-heeled shoes"),
        ("Plateau interno", "Internal platform"), ("Faccia due passi", "Take a few steps"), ("Sono molto stabili", "They are very stable"),
        ("Le prendo!", "I'll take them!"), ("Di questa marca", "Of this brand"), ("Pelle nera", "Black leather"),
        ("Pelle marrone", "Brown leather"), ("Senza lacci", "Without laces"), ("Suola di gomma", "Rubber sole"),
        ("Pianta larga", "Wide fit"), ("Impermeabili all'acqua", "Waterproof"), ("Per una cerimonia", "For a ceremony"),
        ("Molto confortevoli", "Very comfortable"), ("Un po' scomode", "A bit uncomfortable"), ("Vanno bene?", "Do they fit?"),
        ("Mi stringono", "They pinch me"), ("Sono larghe", "They are loose"), ("Posso provare queste?", "Can I try these on?"),
        ("In fondo al negozio", "In the back of the store"), ("Nuovo arrivo", "New arrival"), ("Sconto del 30%", "30% discount"),
        ("Prezzo scontato", "Discounted price"), ("Ottima qualità", "Great quality"), ("Stivali da pioggia", "Rain boots"),
        ("Sandali estivi", "Summer sandals"), ("Pantofole da casa", "House slippers"), ("Scarpe da trekking", "Hiking shoes"),
        ("Suola antiscivolo", "Non-slip sole"), ("Tacco alto", "High heel"), ("Tacco basso", "Low heel"),
        ("Scarpe da corsa", "Running shoes"), ("Numero mancante", "Missing size"), ("Vado a vedere", "I'll go see"),
        ("In magazzino", "In the stockroom"), ("Consegna a domicilio", "Home delivery"), ("Garanzia due anni", "Two-year warranty"),
        ("Spray protettivo", "Protective spray"), ("Lucidare le scarpe", "To polish shoes"), ("Calze di cotone", "Cotton socks"),
        ("Stringere i lacci", "To tighten the laces")
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
                "correct": f"Ottimo! '{it}' si dice '{en}'. / Great! '{it}' is said as '{en}'.",
                "incorrect": f"Sbagliato. '{it}' si traduce '{en}'. / Wrong. '{it}' translates to '{en}'."
            }
        })

    # Sentences (Min 60)
    sentences_data = [
        ("Potrei provare quelle scarpe in vetrina?", "Could I try those shoes in the window?"),
        ("Di solito porto il numero 42.", "I usually wear size 42."),
        ("Il 42 mi sta un po' stretto in punta.", "Size 42 is a bit tight at the toe."),
        ("Le porto anche un 42 e mezzo.", "I'll bring you a 42.5 as well."),
        ("Cerco delle scarpe eleganti per un matrimonio.", "I'm looking for formal shoes for a wedding."),
        ("Preferisco il modello nero stringato.", "I prefer the black lace-up model."),
        ("Avete il numero 43 di queste scarpe?", "Do you have size 43 of these shoes?"),
        ("Vuole usare un calzascarpe per provarle?", "Do you want to use a shoehorn to try them on?"),
        ("Queste scarpe col tacco sembrano scomode.", "These high-heeled shoes seem uncomfortable."),
        ("Hanno un plateau che le rende stabili.", "They have a platform that makes them stable."),
        ("Faccio due passi per sentire la comodità.", "I'll take a few steps to feel the comfort."),
        ("Queste scarpe da ginnastica sono molto leggere.", "These sneakers are very light."),
        ("La suola è fatta di gomma antiscivolo.", "The sole is made of non-slip rubber."),
        ("Mi serve uno spray per pulire il camoscio.", "I need a spray to clean the suede."),
        ("Quanto costano questi stivali in pelle?", "How much do these leather boots cost?"),
        ("C'è uno sconto per l'acquisto di due paia?", "Is there a discount for buying two pairs?"),
        ("Le scarpe sportive sono in fondo al corridoio.", "The sports shoes are at the end of the aisle."),
        ("Questi sandali sono perfetti per il mare.", "These sandals are perfect for the seaside."),
        ("Mi fanno male i piedi con queste scarpe.", "My feet hurt with these shoes."),
        ("Sento che la scarpa scivola sul tallone.", "I feel the shoe slipping at the heel."),
        ("Questi lacci sono troppo lunghi.", "These laces are too long."),
        ("Veste meglio una pianta larga per me.", "A wide fit suits me better."),
        ("Avete una marca più economica?", "Do you have a cheaper brand?"),
        ("Vorrei vedere il catalogo della nuova collezione.", "I'd like to see the new collection catalog."),
        ("Queste pantofole sono molto calde e morbide.", "These slippers are very warm and soft."),
        ("Devo cambiare queste scarpe perché sono piccole.", "I have to exchange these shoes because they are small."),
        ("Avete scarpe impermeabili per la pioggia?", "Do you have waterproof shoes for the rain?"),
        ("Mi piace molto il colore di queste ballerine.", "I really like the color of these ballet flats."),
        ("Il tacco è troppo alto per camminare molto.", "The heel is too high for walking a lot."),
        ("Potrebbe misurarmi il piede, per favore?", "Could you measure my foot, please?"),
        ("Queste scarpe stringate sono molto classiche.", "These lace-up shoes are very classic."),
        ("C'è un difetto sulla pelle di questa scarpa.", "There is a defect on the leather of this shoe."),
        ("Posso avere una scatola nuova?", "Can I have a new box?"),
        ("Accettate pagamenti con carta di credito?", "Do you accept credit card payments?"),
        ("Il commesso mi ha consigliato bene.", "The shop assistant gave me good advice."),
        ("Cerco scarpe da trekking per la montagna.", "I'm looking for hiking shoes for the mountains."),
        ("Questa marca veste un po' piccolo.", "This brand runs a bit small."),
        ("Il cuoio è molto resistente.", "The leather is very resistant."),
        ("Le scarpe da calcio sono in offerta.", "The soccer shoes are on offer."),
        ("Vorrei provare anche il colore marrone.", "I would like to try the brown color too."),
        ("Queste zeppe sono molto di moda.", "These wedges are very fashionable."),
        ("Mi serve una soletta ammortizzata.", "I need a cushioned insole."),
        ("Le stringhe si sono rotte subito.", "The shoelaces broke immediately."),
        ("Quanto viene il totale con l'IVA?", "How much is the total with VAT?"),
        ("Sono le ultime paia rimaste in magazzino.", "They are the last pairs left in the stockroom."),
        ("Il mocassino è molto comodo per l'ufficio.", "The loafer is very comfortable for the office."),
        ("Non hanno la mia misura disponibile.", "They don't have my size available."),
        ("Posso prenotare il mio numero?", "Can I pre-order my size?"),
        ("La spedizione arriva in tre giorni.", "The shipment arrives in three days."),
        ("Queste scarpe sono fatte a mano.", "These shoes are handmade."),
        ("Il design è molto moderno e innovativo.", "The design is very modern and innovative."),
        ("C'è una garanzia per la suola?", "Is there a warranty for the sole?"),
        ("Queste scarpe sono troppo pesanti.", "These shoes are too heavy."),
        ("Cerco qualcosa di più traspirante.", "I'm looking for something more breathable."),
        ("Le scarpe bianche si sporcano facilmente.", "White shoes get dirty easily."),
        ("Ho bisogno di un lucido per scarpe.", "I need a shoe polish."),
        ("Le scarpe sono esposte in vetrina.", "The shoes are displayed in the window."),
        ("Potrebbe aiutarmi a allacciare queste?", "Could you help me lace these up?"),
        ("Questa suola è troppo dura.", "This sole is too hard."),
        ("Il prezzo è un po' alto per me.", "The price is a bit high for me.")
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
                "incorrect": f"Riprova. La risposta è '{en}'. / Try again. The answer is '{en}'."
            }
        })

    with open(os.path.join(base_path, f"shopping_shoe_store_vocabulary.json"), "w", encoding="utf-8") as f:
        json.dump(vocab_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_shoe_store_phrases.json"), "w", encoding="utf-8") as f:
        json.dump(phrases_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_shoe_store_sentences.json"), "w", encoding="utf-8") as f:
        json.dump(sentences_json, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_s42()
