import json
import os
import random

def generate_s45():
    scenario_id = "s45"
    base_path = "src/data/exports/shopping/pharmacy_purchase/"
    
    # Vocabulary (Min 50)
    vocab_data = [
        ("farmacia", "pharmacy"), ("farmacista", "pharmacist"), ("medicina", "medicine"), ("farmaco", "drug/medication"),
        ("ricetta", "prescription"), ("mal di gola", "sore throat"), ("febbre", "fever"), ("tosse", "cough"),
        ("raffreddore", "cold"), ("influenza", "flu"), ("dolore", "pain"), ("infiammazione", "inflammation"),
        ("pastiglie", "lozenges/tablets"), ("compresse", "tablets"), ("sciroppo", "syrup"), ("gocce", "drops"),
        ("crema", "cream"), ("gel", "gel"), ("pomata", "ointment"), ("disinfettante", "disinfectant"),
        ("cerotti", "plasters/band-aids"), ("garza", "gauze"), ("benda", "bandage"), ("termometro", "thermometer"),
        ("vitamine", "vitamins"), ("integratori", "supplements"), ("aloe vera", "aloe vera"), ("calendula", "calendula"),
        ("scottatura", "burn/sunburn"), ("irritazione", "irritation"), ("allergia", "allergy"), ("asma", "asthma"),
        ("stomaco", "stomach"), ("testa", "head"), ("pancia", "belly/stomach"), ("denti", "teeth"),
        ("orecchie", "ears"), ("occhi", "eyes"), ("pelle", "skin"), ("naturale", "natural"),
        ("omeopatico", "homeopathic"), ("antibiotico", "antibiotic"), ("antinfiammatorio", "anti-inflammatory"), ("analgesico", "analgesic"),
        ("antipiretico", "antipyretic"), ("effervescente", "effervescent"), ("scadenza", "expiry"), ("dosaggio", "dosage"),
        ("effetto", "effect"), ("controindicazione", "contraindication"), ("pressione", "blood pressure"), ("diabete", "diabetes"),
        ("insonnia", "insomnia"), ("ansia", "anxiety"), ("stanchezza", "tiredness")
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
        ("Come posso aiutarla?", "How can I help you?"), ("Forte mal di gola", "Strong sore throat"), ("Fatica a deglutire", "Difficulty swallowing"),
        ("Cosa mi consiglia?", "What do you recommend?"), ("Ha anche la febbre?", "Do you also have a fever?"), ("Un po' di irritazione", "A bit of irritation"),
        ("Pastiglie da sciogliere", "Lozenges to dissolve"), ("In bocca", "In the mouth"), ("Azione antinfiammatoria", "Anti-inflammatory action"),
        ("Ogni quattro ore", "Every four hours"), ("Prima di dormire", "Before sleeping"), ("Senza ricetta", "Without prescription"),
        ("Una scatola di aspirina", "A box of aspirin"), ("Compresse classiche", "Classic tablets"), ("Quelle effervescenti", "The effervescent ones"),
        ("Con vitamina C", "With vitamin C"), ("Desidera altro?", "Anything else?"), ("Disinfettante e cerotti", "Disinfectant and plasters"),
        ("Scottatura solare", "Sunburn"), ("Sulle spalle", "On the shoulders"), ("Crema alla calendula", "Calendula cream"),
        ("Gel all'aloe vera", "Aloe vera gel"), ("Molto rinfrescanti", "Very refreshing"), ("Va bene per i bambini?", "Is it okay for children?"),
        ("Prodotto naturale", "Natural product"), ("Senza controindicazioni", "No contraindications"), ("Prendo questo", "I'll take this"),
        ("Quanto costa?", "How much is it?"), ("Sei euro e cinquanta", "Six euros and fifty"), ("Effetti collaterali", "Side effects"),
        ("Dose giornaliera", "Daily dose"), ("A stomaco pieno", "On a full stomach"), ("A stomaco vuoto", "On an empty stomach"),
        ("Sciroppo per la tosse", "Cough syrup"), ("Gocce per gli occhi", "Eye drops"), ("Pomata per dolori", "Pain ointment"),
        ("Garza sterile", "Sterile gauze"), ("Benda elastica", "Elastic bandage"), ("Termometro digitale", "Digital thermometer"),
        ("Misurare la pressione", "To measure blood pressure"), ("Salute e benessere", "Health and wellness"), ("Erboristeria", "Herbal medicine"),
        ("Contro il raffreddore", "Against the cold"), ("Per l'influenza", "For the flu"), ("Mal di testa", "Headache"),
        ("Mal di denti", "Toothache"), ("Mal di stomaco", "Stomach ache"), ("Pronto soccorso", "First aid"),
        ("Farmacia di turno", "On-call pharmacy"), ("Ricetta medica", "Medical prescription")
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
        ("Buongiorno, ho un forte mal di gola da ieri.", "Good morning, I've had a strong sore throat since yesterday."),
        ("Faccio molta fatica a deglutire anche i liquidi.", "I have a lot of difficulty swallowing even liquids."),
        ("Cosa mi consiglia per calmare l'irritazione?", "What do you recommend to calm the irritation?"),
        ("Le consiglio queste pastiglie da sciogliere in bocca.", "I recommend these lozenges to dissolve in the mouth."),
        ("Hanno un'azione antinfiammatoria molto efficace.", "They have a very effective anti-inflammatory action."),
        ("Ne prenda una compressa ogni quattro o cinque ore.", "Take one tablet every four or five hours."),
        ("Posso prenderle anche subito prima di andare a dormire?", "Can I take them also right before going to sleep?"),
        ("Vorrei una scatola di aspirina effervescente, per favore.", "I would like a box of effervescent aspirin, please."),
        ("Preferisce le compresse classiche o quelle con vitamina C?", "Do you prefer the classic tablets or those with vitamin C?"),
        ("Mi servirebbero anche del disinfettante e dei cerotti.", "I would also need some disinfectant and some plasters."),
        ("Ho preso una brutta scottatura solare sulle spalle.", "I got a bad sunburn on my shoulders."),
        ("Questa crema alla calendula è molto rinfrescante sulla pelle.", "This calendula cream is very refreshing on the skin."),
        ("Il gel all'aloe vera è un prodotto naturale e sicuro.", "Aloe vera gel is a natural and safe product."),
        ("Ci sono controindicazioni per l'uso sui bambini piccoli?", "Are there contraindications for use on small children?"),
        ("Questo farmaco richiede la ricetta del medico curante.", "This medication requires a prescription from your doctor."),
        ("Quanto costa in tutto questo sciroppo per la tosse?", "How much is this cough syrup in total?"),
        ("Deve agitare bene il flacone prima dell'uso.", "You must shake the bottle well before use."),
        ("Le pastiglie hanno un gusto gradevole all'arancia.", "The lozenges have a pleasant orange taste."),
        ("Il farmacista è stato molto chiaro nelle spiegazioni.", "The pharmacist was very clear in his explanations."),
        ("Ho dimenticato di chiedere il dosaggio giornaliero.", "I forgot to ask about the daily dosage."),
        ("Deve prendere la medicina a stomaco pieno, dopo i pasti.", "You must take the medicine on a full stomach, after meals."),
        ("Questa pomata serve per i dolori muscolari e articolari.", "This ointment is for muscle and joint pain."),
        ("Avete dei cerotti resistenti all'acqua per il mare?", "Do you have waterproof plasters for the seaside?"),
        ("Mi serve un termometro per misurare la febbre.", "I need a thermometer to measure the fever."),
        ("La ferita va disinfettata bene prima di mettere la benda.", "The wound must be disinfected well before putting on the bandage."),
        ("Ci sono effetti collaterali comuni per questo farmaco?", "Are there common side effects for this medication?"),
        ("Vorrei degli integratori di sali minerali per l'estate.", "I would like some mineral salt supplements for the summer."),
        ("Questa farmacia è aperta anche durante la notte?", "Is this pharmacy open even during the night?"),
        ("Può misurarmi la pressione sanguigna, per favore?", "Can you measure my blood pressure, please?"),
        ("Ho un'allergia stagionale ai pollini della zona.", "I have a seasonal allergy to local pollens."),
        ("Mi servirebbe qualcosa per calmare il mal di stomaco.", "I would need something to calm my stomach ache."),
        ("Queste gocce oculari sono molto utili per gli occhi secchi.", "These eye drops are very useful for dry eyes."),
        ("Il farmacista mi ha dato un ottimo consiglio naturale.", "The pharmacist gave me great natural advice."),
        ("Vorrei delle garze sterili e del nastro adesivo medico.", "I'd like some sterile gauze and medical adhesive tape."),
        ("Questa crema solare ha una protezione molto alta.", "This sunscreen has a very high protection."),
        ("Il raffreddore mi impedisce di respirare bene.", "The cold prevents me from breathing well."),
        ("Ha qualcosa per rinforzare le difese immunitarie?", "Do you have something to strengthen the immune defenses?"),
        ("Questo prodotto è senza glutine e senza lattosio.", "This product is gluten-free and lactose-free."),
        ("Quanto tempo ci mette a fare effetto la medicina?", "How long does it take for the medicine to take effect?"),
        ("Non superi mai la dose consigliata dal produttore.", "Never exceed the dose recommended by the manufacturer."),
        ("La scadenza del farmaco è riportata sulla confezione.", "The expiry of the drug is shown on the packaging."),
        ("Vorrei dei tappi per le orecchie per dormire meglio.", "I'd like some earplugs to sleep better."),
        ("Queste vitamine mi aiutano molto contro la stanchezza.", "These vitamins help me a lot against tiredness."),
        ("Il gel rinfresca subito la zona irritata della pelle.", "The gel immediately cools the irritated area of the skin."),
        ("Serve la tessera sanitaria per lo scontrino parlante?", "Is the health card needed for the detailed receipt?"),
        ("Posso avere un sacchetto per le medicine, grazie.", "Can I have a bag for the medicines, thank you."),
        ("Il dolore è diminuito molto dopo la prima compressa.", "The pain decreased a lot after the first tablet."),
        ("Questa è una farmacia omeopatica e tradizionale.", "This is a homeopathic and traditional pharmacy."),
        ("Avete del sapone neutro per pelli sensibili?", "Do you have neutral soap for sensitive skin?"),
        ("Il cotone idrofilo è nel reparto igiene.", "The absorbent cotton is in the hygiene department."),
        ("Cerco un rimedio per il mal d'auto dei bambini.", "I'm looking for a remedy for children's motion sickness."),
        ("Le compresse effervescenti si sciolgono velocemente.", "The effervescent tablets dissolve quickly."),
        ("Ho perso le istruzioni che erano nella scatola.", "I lost the instructions that were in the box."),
        ("Può consigliarmi un buon collirio rinfrescante?", "Can you recommend a good refreshing eye drop?"),
        ("Questa pomata è solo per uso esterno.", "This ointment is for external use only."),
        ("Il farmacista mi ha spiegato come usare lo spray.", "The pharmacist explained to me how to use the spray."),
        ("Sento un leggero prurito sulla pelle del viso.", "I feel a slight itching on the skin of my face."),
        ("Le erbe officinali sono molto efficaci in questo caso.", "Medicinal herbs are very effective in this case."),
        ("Grazie mille per la sua cortesia e disponibilità.", "Thank you very much for your courtesy and availability."),
        ("Le auguro una pronta guarigione!", "I wish you a speedy recovery!")
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

    with open(os.path.join(base_path, f"shopping_pharmacy_purchase_vocabulary.json"), "w", encoding="utf-8") as f:
        json.dump(vocab_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_pharmacy_purchase_phrases.json"), "w", encoding="utf-8") as f:
        json.dump(phrases_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"shopping_pharmacy_purchase_sentences.json"), "w", encoding="utf-8") as f:
        json.dump(sentences_json, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_s45()
