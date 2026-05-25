import json
import os
import random

def generate_room_problem():
    scenario = "room_problem"
    prefix = "s19"
    base_path = f"src/data/exports/accommodation/{scenario}/"
    
    # Vocabulary
    vocab_list = [
        ("il problema", "the problem"), ("la camera", "the room"), ("l'aria condizionata", "the air conditioning"),
        ("funzionare", "to work/function"), ("la temperatura", "the temperature"), ("il termostato", "the thermostat"),
        ("il muro", "the wall"), ("tiepido", "lukewarm"), ("caldo", "hot/warm"), ("il tecnico", "the technician"),
        ("riparare", "to repair/fix"), ("cambiare", "to change"), ("fretta", "hurry/haste"),
        ("risolvere", "to solve"), ("gli asciugamani", "the towels"), ("il bagno", "the bathroom"),
        ("la svista", "the oversight"), ("il set completo", "the complete set"), ("la carta igienica", "the toilet paper"),
        ("la cameriera ai piani", "the floor maid/housekeeper"), ("il guasto", "the breakdown/fault"), ("la luce", "the light"),
        ("la lampadina", "the light bulb"), ("rotto", "broken"), ("il rumore", "the noise"),
        ("i vicini", "the neighbors"), ("disturbare", "to disturb"), ("la finestra", "the window"),
        ("chiudere", "to close"), ("aprire", "to open"), ("la serratura", "the lock"),
        ("la chiave", "the key"), ("non gira", "does not turn"), ("il frigo", "the fridge"),
        ("vuoto", "empty"), ("sporco", "dirty"), ("pulire", "to clean"), ("l'odore", "the smell"),
        ("la doccia", "the shower"), ("l'acqua calda", "the hot water"), ("mancare", "to be missing"),
        ("il riscaldamento", "the heating"), ("il telecomando", "the remote control"), ("le pile", "the batteries"),
        ("scarico", "dead/empty (battery/drain)"), ("il cuscino", "the pillow"), ("la coperta", "the blanket"),
        ("extra", "extra"), ("il letto", "the bed"), ("scomodo", "uncomfortable"),
        ("la colazione", "the breakfast"), ("il reclamo", "the complaint"), ("lo staff", "the staff"),
        ("scusarsi", "to apologize"), ("immediatamente", "immediately")
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
                "incorrect": f"Actually, '{it}' means '{en}'."
            }
        })

    # Phrases
    phrase_list = [
        ("Chiamo dalla camera", "I'm calling from room"), ("Non sembra funzionare", "Doesn't seem to work"),
        ("Impostare la temperatura", "To set the temperature"), ("Termostato a muro", "Wall thermostat"),
        ("Esce aria tiepida", "Lukewarm air is coming out"), ("Fa molto caldo", "It is very hot"),
        ("Mandare un tecnico", "To send a technician"), ("Ripararla subito", "To fix it right away"),
        ("Cambieremo camera", "We will change rooms"), ("In fretta", "In a hurry"),
        ("Mancano gli asciugamani", "Towels are missing"), ("In bagno", "In the bathroom"),
        ("Ci scusi per la svista", "Pardon us for the oversight"), ("Set completo", "Complete set"),
        ("Provvedo immediatamente", "I'll see to it immediately"), ("Manca la carta igienica", "Toilet paper is missing"),
        ("Cameriera ai piani", "Floor housekeeper"), ("Tra cinque minuti", "In five minutes"),
        ("La ringrazio", "I thank you"), ("C'è un guasto", "There is a fault"),
        ("La luce non si accende", "The light doesn't turn on"), ("Lampadina bruciata", "Burnt out light bulb"),
        ("La serratura è rotta", "The lock is broken"), ("Troppo rumore", "Too much noise"),
        ("Vicini rumorosi", "Noisy neighbors"), ("Finestra che non chiude", "Window that doesn't close"),
        ("Acqua solo fredda", "Only cold water"), ("Doccia intasata", "Clogged shower"),
        ("Frigo che non raffredda", "Fridge that doesn't cool"), ("Camera ancora sporca", "Room still dirty"),
        ("Cattivo odore", "Bad smell"), ("Mancano le coperte", "Blankets are missing"),
        ("Cuscino troppo duro", "Pillow too hard"), ("Letto scomodo", "Uncomfortable bed"),
        ("Telecomando senza pile", "Remote without batteries"), ("Riscaldamento spento", "Heating off"),
        ("Senza acqua calda", "Without hot water"), ("Chiave che non gira", "Key that doesn't turn"),
        ("Segnalare un problema", "To report a problem"), ("Parlare con il manager", "To speak with the manager"),
        ("Fare un reclamo", "To make a complaint"), ("Chiedere uno sconto", "To ask for a discount"),
        ("Scusate il disturbo", "Sorry for the disturbance"), ("Spero che si risolva", "I hope it gets resolved"),
        ("Grazie per l'aiuto", "Thanks for the help"), ("Servizio scadente", "Poor service"),
        ("Personale gentile", "Kind staff"), ("Soluzione rapida", "Quick solution"),
        ("Prendere nota", "To take note"), ("Tornare tra poco", "To return shortly"),
        ("Tutto risolto", "Everything resolved"), ("Ancora rotto", "Still broken")
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
                "correct": f"Great! '{it}' translates to '{en}'.",
                "incorrect": f"No, '{it}' means '{en}'."
            }
        })

    # Sentences
    sentence_list = [
        ("Salve, chiamo dalla camera quattrocentodue.", "Hello, I'm calling from room four hundred two."),
        ("L'aria condizionata sembra non funzionare correttamente.", "The air conditioning doesn't seem to be working properly."),
        ("Mi dispiace molto per questo inconveniente.", "I'm very sorry for this inconvenience."),
        ("Ha provato a impostare la temperatura dal termostato?", "Have you tried to set the temperature from the thermostat?"),
        ("Sì, ma esce solo aria tiepida e non rinfresca.", "Yes, but only lukewarm air comes out and it doesn't cool."),
        ("Fa molto caldo in camera nonostante l'aria sia accesa.", "It's very hot in the room even though the air is on."),
        ("Mando subito un tecnico a controllare il guasto.", "I'm sending a technician immediately to check the fault."),
        ("Se non riusciamo a ripararla, le cambieremo camera.", "If we can't repair it, we will change your room."),
        ("Grazie, spero che il problema si risolva in fretta.", "Thanks, I hope the problem is resolved quickly."),
        ("Abbiamo appena fatto il check-in ma mancano gli asciugamani.", "We just checked in but the towels are missing."),
        ("Ci scusi per questa svista del nostro personale.", "Pardon us for this oversight by our staff."),
        ("Provvedo a mandarle un set completo di asciugamani.", "I'll see to sending you a complete set of towels."),
        ("Già che ci siamo, manca anche la carta igienica.", "While we're at it, the toilet paper is also missing."),
        ("La cameriera ai piani sarà da lei tra cinque minuti.", "The floor housekeeper will be with you in five minutes."),
        ("La ringrazio molto per la sua assistenza rapida.", "I thank you very much for your quick assistance."),
        ("La luce nel bagno non si accende stasera.", "The light in the bathroom doesn't turn on tonight."),
        ("Forse si è bruciata la lampadina principale.", "Maybe the main light bulb has burnt out."),
        ("La serratura della porta sembra essere bloccata.", "The door lock seems to be stuck."),
        ("La chiave non gira bene nella toppa.", "The key doesn't turn well in the keyhole."),
        ("C'è troppo rumore proveniente dalla camera accanto.", "There is too much noise coming from the next room."),
        ("I vicini stanno gridando e non riusciamo a dormire.", "The neighbors are shouting and we can't sleep."),
        ("Potrebbe chiedere loro di fare meno rumore?", "Could you ask them to make less noise?"),
        ("Certamente, mando subito qualcuno a controllare la situazione.", "Certainly, I'm sending someone immediately to check the situation."),
        ("La finestra della camera non si chiude bene.", "The room window doesn't close properly."),
        ("Entra troppa aria fredda dall'esterno.", "Too much cold air is coming in from outside."),
        ("Dalla doccia esce solo acqua fredda, non c'è acqua calda.", "Only cold water is coming out of the shower, there is no hot water."),
        ("Il riscaldamento sembra essere completamente spento.", "The heating seems to be completely turned off."),
        ("Il frigo in camera non raffredda le bevande.", "The fridge in the room doesn't cool the drinks."),
        ("La camera non è stata pulita oggi, è ancora sporca.", "The room hasn't been cleaned today, it's still dirty."),
        ("C'è un cattivo odore che proviene dal bagno.", "There is a bad smell coming from the bathroom."),
        ("Mancano le coperte extra nell'armadio.", "The extra blankets are missing in the closet."),
        ("Il cuscino è troppo duro, ne vorrei uno più morbido.", "The pillow is too hard, I'd like a softer one."),
        ("Il letto è molto scomodo per la mia schiena.", "The bed is very uncomfortable for my back."),
        ("Il telecomando della TV è senza pile.", "The TV remote is without batteries."),
        ("Voglio segnalare un problema serio con la camera.", "I want to report a serious problem with the room."),
        ("Vorrei parlare con il manager dell'hotel, per favore.", "I would like to speak with the hotel manager, please."),
        ("Voglio fare un reclamo ufficiale per il servizio.", "I want to make an official complaint about the service."),
        ("Spero che possiate offrirmi uno sconto per il disturbo.", "I hope you can offer me a discount for the disturbance."),
        ("Mi scuso ancora, faremo il possibile per aiutarla.", "I apologize again, we will do our best to help you."),
        ("Grazie per la vostra pazienza e comprensione.", "Thanks for your patience and understanding."),
        ("Il tecnico arriverà tra meno di dieci minuti.", "The technician will arrive in less than ten minutes."),
        ("Abbiamo risolto il problema con l'acqua calda.", "We have resolved the problem with the hot water."),
        ("La nuova camera è pronta al secondo piano.", "The new room is ready on the second floor."),
        ("Possiamo aiutarla a spostare i suoi bagagli?", "Can we help you move your luggage?"),
        ("Sì grazie, apprezzo molto questo gesto.", "Yes thanks, I really appreciate this gesture."),
        ("Speriamo che la nuova sistemazione sia migliore.", "We hope the new accommodation is better."),
        ("Questa camera è molto più silenziosa della prima.", "This room is much quieter than the first one."),
        ("Tutto sembra funzionare perfettamente ora.", "Everything seems to be working perfectly now."),
        ("Grazie per aver risolto tutto così velocemente.", "Thanks for having resolved everything so quickly."),
        ("Siamo a sua completa disposizione per ogni necessità.", "We are at your complete disposal for any need."),
        ("C'è qualcos'altro che possiamo fare per lei?", "Is there anything else we can do for you?"),
        ("No per ora va bene così, grazie mille.", "No for now it's fine like this, thanks a lot."),
        ("Vi auguro un buon proseguimento di serata.", "I wish you a good continuation of the evening."),
        ("Il rubinetto del lavandino perde acqua.", "The sink faucet is leaking water."),
        ("Il Wi-Fi non prende bene in questa camera.", "The Wi-Fi doesn't have a good signal in this room."),
        ("La TV non si accende, forse è staccata la spina.", "The TV doesn't turn on, maybe the plug is disconnected."),
        ("Manca il sapone nella doccia.", "The soap is missing in the shower."),
        ("Le lenzuola non sembrano pulite.", "The sheets don't seem clean."),
        ("C'è una macchia sul tappeto.", "There is a stain on the carpet."),
        ("L'ascensore è fuori servizio al momento.", "The elevator is out of service at the moment."),
        ("Devo fare le scale fino al quinto piano.", "I have to take the stairs up to the fifth floor.")
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

generate_room_problem()
