import json
import os
import random

def generate_asking_for_towels():
    scenario = "asking_for_towels"
    prefix = "s20"
    base_path = f"src/data/exports/accommodation/{scenario}/"
    
    # Vocabulary
    vocab_list = [
        ("l'asciugamano", "the towel"), ("grande", "large/big"), ("piccolo", "small"),
        ("la doccia", "the shower"), ("il viso", "the face"), ("pulito", "clean"),
        ("umido", "damp/humid"), ("asciugarsi", "to dry (oneself)"), ("il set completo", "the complete set"),
        ("il ricambio", "the change/spare"), ("il sapone", "the soap"), ("lo shampoo", "the shampoo"),
        ("la carta igienica", "the toilet paper"), ("finire", "to finish/run out"), ("reintegrare", "to replenish"),
        ("la scorta", "the stock/supply"), ("occupato", "occupied"), ("bussare", "to knock"),
        ("la dimenticanza", "the forgetfulness/oversight"), ("la coperta", "the blanket"), ("di lana", "wool/woollen"),
        ("pesante", "heavy"), ("sottile", "thin"), ("il cuscino", "the pillow"),
        ("extra", "extra"), ("duro", "hard"), ("morbido", "soft"),
        ("il coprimaterasso", "the mattress topper"), ("scomodo", "uncomfortable"), ("alto", "high/tall"),
        ("la piscina", "the pool"), ("bagnato", "wet"), ("l'accappatoio", "the bathrobe"),
        ("l'armadio", "the closet/wardrobe"), ("lo scaffale", "the shelf"), ("la biancheria", "the linen"),
        ("le lenzuola", "the sheets"), ("lo stendino", "the drying rack"), ("stendere", "to hang out (laundry)"),
        ("il balcone", "the balcony"), ("il sole", "the sun"), ("il phon", "the hair dryer"),
        ("rotto", "broken"), ("la maniglia", "the handle"), ("appeso", "hanging/hung"),
        ("il set", "the set"), ("il personale", "the staff"), ("la reception", "the front desk"),
        ("il piano", "the floor"), ("la camera", "the room"), ("il numero", "the number"),
        ("il servizio", "the service"), ("il controllo", "the check"), ("la pulizia", "the cleaning")
    ]
    
    vocab_data = []
    for i, (it, en) in enumerate(vocab_list):
        choices_it = [it]
        choices_en = [en]
        others = [v for v in vocab_list if v != (it, en)]
        random.seed(i)
        distractors = random.sample(others, 3)
        for d_it, d_en in distractors:
            choices_it.append(d_it)
            choices_en.append(d_en)
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        vocab_data.append({
            "id": f"{prefix}-v{i+1:02d}",
            "type": "vocabulary",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Correct! '{it}' is '{en}'.",
                "incorrect": f"Wrong. '{it}' means '{en}'."
            }
        })

    # Phrases
    phrase_list = [
        ("Avrei bisogno di una cosa", "I would need something"), ("Un asciugamano grande", "A large towel"),
        ("Asciugamani puliti", "Clean towels"), ("Per la doccia", "For the shower"),
        ("Per il viso", "For the face"), ("Siamo in due", "There are two of us"),
        ("Portare al piano", "To bring to the floor"), ("Un cambio per domani", "A change for tomorrow"),
        ("Un po' umidi", "A bit damp"), ("Non si asciugano", "They don't dry"),
        ("Due set completi", "Two complete sets"), ("Tra cinque minuti", "In five minutes"),
        ("Appesi alla maniglia", "Hanging on the handle"), ("Bussano alla porta", "They knock at the door"),
        ("Carta igienica finita", "Toilet paper run out"), ("Personale delle pulizie", "Cleaning staff"),
        ("Dalla scorta", "From the supply"), ("Non ne ho di scorta", "I don't have any in stock"),
        ("Sto uscendo", "I'm going out"), ("Basta bussare", "Just knock"),
        ("Controllo completo", "Full check"), ("Coperta in più", "Extra blanket"),
        ("Coperta di lana", "Wool blanket"), ("Cuscini extra", "Extra pillows"),
        ("Letto un po' duro", "Bed a bit hard"), ("Coprimaterasso morbido", "Soft mattress topper"),
        ("Pazienza e gentilezza", "Patience and kindness"), ("Cartello non disturbare", "Do not disturb sign"),
        ("Phon rotto", "Broken hair dryer"), ("Cuscino scomodo", "Uncomfortable pillow"),
        ("Asciugamano da piscina", "Pool towel"), ("Incluso nel servizio", "Included in the service"),
        ("Scaffale in alto", "Top shelf"), ("Lenzuola di ricambio", "Spare sheets"),
        ("Non è urgentissimo", "It's not very urgent"), ("Stendino sul balcone", "Drying rack on the balcony"),
        ("Sole che picchia", "Beating sun"), ("Passo tra un'ora", "I'll stop by in an hour"),
        ("Biancheria sporca", "Dirty linen"), ("Due grandi e due piccoli", "Two large and two small"),
        ("Sotto il lavandino", "Under the sink"), ("Dentro l'armadio", "Inside the closet"),
        ("Sulla mensola", "On the shelf"), ("Appena fatto il check-in", "Just checked in"),
        ("Almeno un altro", "At least one more"), ("Set pronto", "Set ready"),
        ("Portare subito", "To bring right away"), ("Aspetto in camera", "I'll wait in the room"),
        ("Rifornire il bagno", "To restock the bathroom"), ("Segnare tutto", "To note everything down"),
        ("Chiamare subito", "To call right away"), ("Molto gentile", "Very kind")
    ]
    
    phrase_data = []
    for i, (it, en) in enumerate(phrase_list):
        choices_it = [it]
        choices_en = [en]
        others = [p for p in phrase_list if p != (it, en)]
        random.seed(i+100)
        distractors = random.sample(others, 3)
        for d_it, d_en in distractors:
            choices_it.append(d_it)
            choices_en.append(d_en)
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        phrase_data.append({
            "id": f"{prefix}-p{i+1:02d}",
            "type": "phrase",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Great! '{it}' is correctly translated as '{en}'.",
                "incorrect": f"Actually, '{it}' means '{en}'."
            }
        })

    # Sentences
    sentence_list = [
        ("In camera ho solo un asciugamano grande.", "In the room I only have one large towel."),
        ("Vorrei degli asciugamani puliti in più, è possibile?", "I'd like some extra clean towels, is it possible?"),
        ("Ci servono un asciugamano per la doccia e due per il viso.", "We need one towel for the shower and two for the face."),
        ("Noi siamo in due in questa camera.", "There are two of us in this room."),
        ("Glieli faccio portare subito al piano.", "I'll have them brought to the floor right away."),
        ("Le serve anche altro, come sapone o shampoo?", "Do you need anything else, like soap or shampoo?"),
        ("Vorrei anche un cambio per domani perché questi sono umidi.", "I'd also like a change for tomorrow because these are damp."),
        ("Gli asciugamani non si asciugano bene in questo bagno.", "The towels don't dry well in this bathroom."),
        ("Le mando due set completi così ha il ricambio.", "I'm sending you two complete sets so you have spares."),
        ("Se non è in camera, li lascio appesi alla maniglia.", "If you're not in the room, I'll leave them hanging on the handle."),
        ("Manca il sapone in bagno e la carta igienica è finita.", "The soap is missing in the bathroom and the toilet paper is finished."),
        ("Il personale delle pulizie ha dimenticato di reintegrare le scorte.", "The cleaning staff forgot to replenish the supplies."),
        ("Posso darle subito sapone e carta dalla reception.", "I can give you soap and paper from the front desk right away."),
        ("Per l'asciugamano, devo mandare su qualcuno tra poco.", "For the towel, I have to send someone up shortly."),
        ("Potete entrare in camera anche se non ci sono.", "You can enter the room even if I'm not there."),
        ("Controllate anche se c'è abbastanza shampoo nella doccia.", "Check also if there is enough shampoo in the shower."),
        ("Mi scusi per la dimenticanza, facciamo un controllo completo.", "Pardon me for the oversight, we'll do a full check."),
        ("Ci può portare due asciugamani grandi e due piccoli?", "Can you bring us two large towels and two small ones?"),
        ("Vorrei anche una coperta in più perché fa freddo.", "I'd also like an extra blanket because it's cold."),
        ("La coperta nell'armadio è troppo sottile per la notte.", "The blanket in the closet is too thin for the night."),
        ("Le porto una coperta di lana molto pesante.", "I'll bring you a very heavy wool blanket."),
        ("Il letto è un po' duro, ma non fa niente.", "The bed is a bit hard, but it doesn't matter."),
        ("Abbiamo un coprimaterasso morbido che potrebbe aiutare.", "We have a soft mattress topper that might help."),
        ("A che ora passano di solito per la pulizia della camera?", "What time do they usually stop by for room cleaning?"),
        ("Ieri la camera forse aveva il cartello 'non disturbare'.", "Yesterday the room perhaps had the 'do not disturb' sign."),
        ("Abbiamo bisogno di asciugamani puliti e di rimettere in ordine.", "We need clean towels and to tidy up."),
        ("Il phon in camera non si accende, forse è rotto.", "The hair dryer in the room doesn't turn on, maybe it's broken."),
        ("Segnalo subito il problema alla reception.", "I'll report the problem to the front desk right away."),
        ("Il mio cuscino è scomodo, troppo alto e duro.", "My pillow is uncomfortable, too high and hard."),
        ("Abbiamo cuscini in memory foam se preferisce.", "We have memory foam pillows if you prefer."),
        ("Potrebbe portarmi anche un asciugamano da piscina?", "Could you also bring me a pool towel?"),
        ("L'accappatoio è incluso nel servizio dell'hotel?", "Is the bathrobe included in the hotel service?"),
        ("Glielo porto insieme al nuovo cuscino tra dieci minuti.", "I'll bring it to you along with the new pillow in ten minutes."),
        ("Non trovo gli asciugamani puliti nell'armadio.", "I can't find the clean towels in the closet."),
        ("Di solito lascio un set pulito nello scaffale in alto.", "I usually leave a clean set on the top shelf."),
        ("Forse l'ospite precedente li ha usati tutti.", "Perhaps the previous guest used them all."),
        ("Puoi portarmene un paio quando torni dal lavoro?", "Can you bring me a couple when you return from work?"),
        ("Sullo stendino sul balcone c'è ancora spazio.", "There is still space on the drying rack on the balcony."),
        ("Il sole oggi è forte e asciugherà tutto in fretta.", "The sun is strong today and will dry everything quickly."),
        ("Ecco gli asciugamani che avevi chiesto, li metto in bagno.", "Here are the towels you asked for, I'll put them in the bathroom."),
        ("Vi lascio anche del sapone e dello shampoo nuovi.", "I'll also leave you some new soap and shampoo."),
        ("Grazie mille, sei stato davvero gentilissimo.", "Thanks a lot, you have been really very kind."),
        ("Basta bussare prima di entrare, noi siamo qui.", "Just knock before entering, we are here."),
        ("Non abbiamo sapone, potete portarcene un po'?", "We don't have soap, can you bring us some?"),
        ("La carta igienica sta per finire, potete portarne altra?", "The toilet paper is about to run out, can you bring more?"),
        ("C'è solo un asciugamano per due persone.", "There is only one towel for two people."),
        ("Preferirei un cuscino più morbido per dormire meglio.", "I would prefer a softer pillow to sleep better."),
        ("La coperta è nell'armadio sopra il letto.", "The blanket is in the closet above the bed."),
        ("Il set di asciugamani comprende anche quello per i piedi.", "The towel set also includes the one for the feet."),
        ("Ho lasciato gli asciugamani sporchi sul pavimento.", "I left the dirty towels on the floor."),
        ("Potete cambiare anche le lenzuola oggi?", "Can you also change the sheets today?"),
        ("La doccia è bagnata e non c'è il tappetino.", "The shower is wet and there is no mat."),
        ("C'è un supplemento per gli asciugamani extra?", "Is there a surcharge for extra towels?"),
        ("No, è un servizio gratuito per i nostri clienti.", "No, it's a free service for our customers."),
        ("Avete anche degli accappatoi della mia taglia?", "Do you also have bathrobes in my size?"),
        ("Controllo subito nel deposito della biancheria.", "I'll check the linen storage right away."),
        ("Grazie per aver portato tutto così velocemente.", "Thanks for bringing everything so quickly."),
        ("Speriamo che ora possiate riposare bene.", "We hope that you can rest well now."),
        ("Buon soggiorno e non esiti a chiamare di nuovo.", "Have a good stay and don't hesitate to call again."),
        ("La cameriera passerà tra dieci minuti col ricambio.", "The maid will stop by in ten minutes with the change."),
        ("Ecco i saponi nuovi e le cuffie per la doccia.", "Here are the new soaps and the shower caps.")
    ]
    
    sentence_data = []
    for i, (it, en) in enumerate(sentence_list):
        choices_it = [it]
        choices_en = [en]
        others = [s for s in sentence_list if s != (it, en)]
        random.seed(i+200)
        distractors = random.sample(others, 3)
        for d_it, d_en in distractors:
            choices_it.append(d_it)
            choices_en.append(d_en)
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        sentence_data.append({
            "id": f"{prefix}-s{i+1:02d}",
            "type": "sentence",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correct": f"Excellent! '{it}' means '{en}'.",
                "incorrect": f"Incorrect. '{en}' is '{it}' in Italian."
            }
        })

    with open(os.path.join(base_path, f"{scenario}_vocabulary.json"), "w") as f:
        json.dump(vocab_data, f, indent=2, ensure_ascii=False)
    with open(os.path.join(base_path, f"{scenario}_phrases.json"), "w") as f:
        json.dump(phrase_data, f, indent=2, ensure_ascii=False)
    with open(os.path.join(base_path, f"{scenario}_sentences.json"), "w") as f:
        json.dump(sentence_data, f, indent=2, ensure_ascii=False)

generate_asking_for_towels()
