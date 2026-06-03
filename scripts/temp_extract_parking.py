import json
import re
import random

def split_sentences(text):
    # Split by ., ?, ! but keep the delimiter
    return re.findall(r'[^.!?]+[.!?]*', text)

def clean_text(text):
    return text.strip()

scenario_id = 12
prefix = "travel_parking"
base_path = "src/data/exports/travel/parking/"

with open(base_path + 'conversations.json', 'r', encoding='utf-8') as f:
    conv_data = json.load(f)

# Extract unique sentences and their translations
sentences_map = {}

# Manual mapping for user sentences as they don't have English in the JSON but I know them
user_sentences_raw = {
    "Sì, cerco un parcheggio qui vicino. È difficile?": "Yes, I am looking for a parking spot nearby. Is it difficult?",
    "Sì, le vedo. Qual è la differenza tra blu e bianco?": "Yes, I see them. What is the difference between blue and white?",
    "Capisco. Allora cerco un posto con le strisce bianche.": "I understand. Then I'll look for a spot with white lines.",
    "Ah, peccato. Allora parcheggio sulle strisce blu, è meglio.": "Ah, too bad. Then I'll park on the blue lines, it's better.",
    "Certamente, vado subito a pagare. Grazie mille!": "Certainly, I'm going to pay right away. Thanks a lot!",
    "Sì, grazie. Non capisco come funziona questa macchinetta.": "Yes, thanks. I don't understand how this machine works.",
    "Va bene, inserisco la targa. Ecco fatto. E dopo?": "Alright, I'll enter the plate. Done. And then?",
    "Voglio restare per due ore. Quanto costa il parcheggio?": "I want to stay for two hours. How much does parking cost?",
    "Pago con la carta di credito. Devo inserirla qui?": "I pay with the credit card. Do I have to insert it here?",
    "Tasto verde... confermato. Ho preso la ricevuta, grazie!": "Green button... confirmed. I took the receipt, thanks!",
    "No, non l'ho letto bene. Cosa dice il cartello?": "No, I didn't read it well. What does the sign say?",
    "Ah, capisco. Adesso sono le diciannove, quindi non posso?": "Ah, I understand. Now it's 7 PM, so I can't?",
    "Cos'è il disco orario? Non ne ho mai visto uno.": "What is a parking disc? I've never seen one.",
    "Ah, ho capito. Posso restare solo per un'ora lì?": "Ah, I see. Can I stay for only one hour there?",
    "Perfetto, lo faccio subito. Grazie per la spiegazione!": "Perfect, I'll do it right away. Thanks for the explanation!",
    "Sì, ma la macchinetta non accetta le mie monete.": "Yes, but the machine doesn't accept my coins.",
    "Davvero? È gratis tutto il giorno o solo la mattina?": "Really? Is it free all day or only in the morning?",
    "Che bella notizia! Vale per tutte le zone della città?": "What great news! Is it valid for all areas of the city?",
    "Siamo lontani dalla stazione qui, vero?": "We are far from the station here, right?",
    "Ottimo, allora la lascio qui. Grazie per l'informazione!": "Great, then I'll leave it here. Thanks for the information!"
}

# Mapping for individual parts
parts_map = {
    "Buongiorno!": "Good morning!",
    "Cerca un posto per parcheggiare l'auto?": "Are you looking for a place to park the car?",
    "In centro è difficile.": "In the center it is difficult.",
    "Vede quelle strisce blu e bianche per terra?": "Do you see those blue and white lines on the ground?",
    "Le strisce blu sono a pagamento.": "The blue lines are for paid parking.",
    "Quelle bianche sono gratuite.": "The white ones are free.",
    "Attenzione però.": "Watch out though.",
    "I posti bianchi sono quasi tutti occupati dai residenti.": "The white spots are almost all occupied by residents.",
    "Va bene.": "Alright.",
    "Ricordi di pagare alla macchinetta ed esporre il biglietto.": "Remember to pay at the machine and display the ticket.",
    "Scusi, ha bisogno di aiuto con la macchinetta del parcheggio?": "Excuse me, do you need help with the parking machine?",
    "È semplice.": "It's simple.",
    "Prima deve inserire il numero di targa della sua auto.": "First you must enter your car's license plate number.",
    "Ora deve scegliere il tempo.": "Now you must choose the time.",
    "Quanto tempo vuole restare?": "How long do you want to stay?",
    "Costa un euro e cinquanta all'ora.": "It costs one euro and fifty per hour.",
    "Può pagare con monete o carta.": "You can pay with coins or card.",
    "Sì, esatto.": "Yes, exactly.",
    "Prema il tasto verde per confermare e ritiri la ricevuta.": "Press the green button to confirm and collect the receipt.",
    "Attenzione!": "Watch out!",
    "Ha letto il cartello prima di parcheggiare l'auto?": "Did you read the sign before parking the car?",
    "Dice che il parcheggio è riservato ai residenti dalle otto alle venti.": "It says that parking is reserved for residents from eight to twenty.",
    "Esatto.": "Exactly.",
    "Però c'è un altro posto lì, dove serve il disco orario.": "But there is another spot there, where you need a parking disc.",
    "È un cartoncino per indicare l'ora di arrivo.": "It's a small card to indicate the arrival time.",
    "Si mette sul cruscotto.": "You put it on the dashboard.",
    "Sì, massimo un'ora.": "Yes, maximum one hour.",
    "Deve girare la ruota sull'ora di adesso.": "You must turn the wheel to the current hour.",
    "Sta cercando di pagare il parcheggio oggi?": "Are you trying to pay for parking today?",
    "Ma oggi è domenica!": "But today is Sunday!",
    "Lo sa che la domenica il parcheggio è gratis?": "Do you know that on Sundays parking is free?",
    "È gratis per tutto il giorno festivo.": "It is free for the entire holiday.",
    "Non deve mettere soldi.": "You don't have to put money in.",
    "Quasi tutte, tranne vicino all'ospedale e alla stazione.": "Almost all, except near the hospital and the station.",
    "Sì, siamo in centro.": "Yes, we are in the center.",
    "Può lasciare l'auto qui senza problemi.": "You can leave the car here without problems.",
    "Sì, cerco un parcheggio qui vicino.": "Yes, I am looking for a parking spot nearby.",
    "È difficile?": "Is it difficult?",
    "Sì, le vedo.": "Yes, I see them.",
    "Qual è la differenza tra blu e bianco?": "What is the difference between blue and white?",
    "Capisco.": "I understand.",
    "Allora cerco un posto con le strisce bianche.": "Then I'll look for a spot with white lines.",
    "Ah, peccato.": "Ah, too bad.",
    "Allora parcheggio sulle strisce blu, è meglio.": "Then I'll park on the blue lines, it's better.",
    "Certamente, vado subito a pagare.": "Certainly, I'm going to pay right away.",
    "Grazie mille!": "Thanks a lot!",
    "Sì, grazie.": "Yes, thanks.",
    "Non capisco come funziona questa macchinetta.": "I don't understand how this machine works.",
    "Va bene, inserisco la targa.": "Alright, I'll enter the plate.",
    "Ecco fatto.": "Done.",
    "E dopo?": "And then?",
    "Voglio restare per due ore.": "I want to stay for two hours.",
    "Quanto costa il parcheggio?": "How much does parking cost?",
    "Pago con la carta di credito.": "I pay with the credit card.",
    "Devo inserirla qui?": "Do I have to insert it here?",
    "Tasto verde...": "Green button...",
    "confermato.": "confirmed.",
    "Ho preso la ricevuta, grazie!": "I took the receipt, thanks!",
    "No, non l'ho letto bene.": "No, I didn't read it well.",
    "Cosa dice il cartello?": "What does the sign say?",
    "Adesso sono le diciannove, quindi non posso?": "Now it's 7 PM, so I can't?",
    "Cos'è il disco orario?": "What is a parking disc?",
    "Non ne ho mai visto uno.": "I've never seen one.",
    "Ah, ho capito.": "Ah, I see.",
    "Posso restare solo per un'ora lì?": "Can I stay for only one hour there?",
    "Perfetto, lo faccio subito.": "Perfect, I'll do it right away.",
    "Grazie per la spiegazione!": "Thanks for the explanation!",
    "Sì, ma la macchinetta non accetta le mie monete.": "Yes, but the machine doesn't accept my coins.",
    "Davvero?": "Really?",
    "È gratis tutto il giorno o solo la mattina?": "Is it free all day or only in the morning?",
    "Che bella notizia!": "What great news!",
    "Vale per tutte le zone della città?": "Is it valid for all areas of the city?",
    "Siamo lontani dalla stazione qui, vero?": "We are far from the station here, right?",
    "Ottimo, allora la lascio qui.": "Great, then I'll leave it here.",
    "Grazie per l'informazione!": "Thanks for the information!"
}

# Vocabulary extraction
vocab_dict = {
    "parcheggio": "parking",
    "posto": "spot",
    "macchina": "car",
    "auto": "car",
    "parcheggiare": "to park",
    "strisce": "lines",
    "blu": "blue",
    "bianche": "white",
    "pagamento": "payment",
    "gratuite": "free",
    "occupati": "occupied",
    "residenti": "residents",
    "macchinetta": "machine",
    "biglietto": "ticket",
    "targa": "license plate",
    "tempo": "time",
    "monete": "coins",
    "carta": "card",
    "ricevuta": "receipt",
    "cartello": "sign",
    "disco": "disc",
    "orario": "schedule",
    "cruscotto": "dashboard",
    "ruota": "wheel",
    "domenica": "Sunday",
    "gratis": "free",
    "festivo": "holiday",
    "stazione": "station",
    "ospedale": "hospital",
    "centro": "center",
    "difficile": "difficult",
    "differenza": "difference",
    "cerca": "look for",
    "vede": "see",
    "terra": "ground",
    "esporre": "display",
    "bisogno": "need",
    "aiuto": "help",
    "semplice": "simple",
    "inserire": "insert",
    "numero": "number",
    "scegliere": "choose",
    "costa": "cost",
    "euro": "euro",
    "cinquanta": "fifty",
    "prema": "press",
    "tasto": "button",
    "verde": "green",
    "confermare": "confirm",
    "ritiri": "collect",
    "letto": "read",
    "riservato": "reserved",
    "otto": "eight",
    "venti": "twenty",
    "serve": "need",
    "cartoncino": "cardboard",
    "indicare": "indicate",
    "arrivo": "arrival",
    "massimo": "maximum",
    "girare": "turn",
    "cercando": "trying",
    "pagare": "pay",
    "accetta": "accept",
    "notizia": "news",
    "vale": "valid",
    "zone": "areas",
    "città": "city",
    "lontani": "far",
    "vero": "right",
    "lasciare": "leave",
    "problemi": "problems"
}

# Semantic categories for distractors
semantic_categories = {
    "colors": ["blu", "bianche", "gialle", "rosse", "verdi", "nere"],
    "parking_objects": ["macchinetta", "parcometro", "disco", "cartello", "biglietto", "ricevuta", "targa"],
    "locations": ["parcheggio", "posto", "strisce", "centro", "stazione", "ospedale", "garage"],
    "time": ["orario", "ora", "minuti", "tempo", "domenica", "mattina", "sera"],
    "payment": ["pagamento", "monete", "carta", "credito", "euro", "costa", "gratis"]
}

def get_vocab_distractors(word):
    cat = None
    for c, words in semantic_categories.items():
        if word in words:
            cat = c
            break
    if cat:
        options = [w for w in semantic_categories[cat] if w != word]
        random.shuffle(options)
        return options[:3]
    else:
        options = [w for w in vocab_dict.keys() if w != word]
        random.shuffle(options)
        return options[:3]

# 1. Vocabulary JSON
vocab_json = []
for i, (it, en) in enumerate(vocab_dict.items()):
    dist_it = get_vocab_distractors(it)
    choices_it = [it] + dist_it
    random.shuffle(choices_it)
    choices_en = []
    for c in choices_it:
        choices_en.append(vocab_dict.get(c, "???"))
    
    vocab_json.append({
        "id": f"s12-v{i+1}",
        "italian": it,
        "english": en,
        "type": "vocabulary",
        "choicesItalian": choices_it,
        "choicesEnglish": choices_en,
        "feedback": {
            "correctItalian": "Esatto!",
            "incorrectItalian": f"No, è '{it}'.",
            "correctEnglish": "Great!",
            "incorrectEnglish": f"No, it is '{it}'."
        },
        "audio": {"italian": ""}
    })

# 2. Sentences and Phrases
all_sentences = []
all_phrases = []

for it, en in parts_map.items():
    if len(it.split()) <= 4:
        all_phrases.append((it, en))
    else:
        all_sentences.append((it, en))

def get_sentence_distractors(it, source_list):
    others = [s[0] for s in source_list if s[0] != it]
    random.shuffle(others)
    return others[:3]

sentences_json = []
for i, (it, en) in enumerate(all_sentences):
    dist_it = get_sentence_distractors(it, all_sentences)
    choices_it = [it] + dist_it
    random.shuffle(choices_it)
    choices_en = []
    for c in choices_it:
        found = False
        for sit, sen in all_sentences:
            if sit == c:
                choices_en.append(sen)
                found = True
                break
        if not found: choices_en.append("???")

    sentences_json.append({
        "id": f"s12-s{i+1}",
        "italian": it,
        "english": en,
        "type": "sentence",
        "choicesItalian": choices_it,
        "choicesEnglish": choices_en,
        "feedback": {
            "correctItalian": "Perfetto!",
            "incorrectItalian": "Non è corretto.",
            "correctEnglish": "Perfect!",
            "incorrectEnglish": "That is not correct."
        },
        "audio": {"italian": ""}
    })

phrases_json = []
for i, (it, en) in enumerate(all_phrases):
    dist_it = get_sentence_distractors(it, all_phrases)
    choices_it = [it] + dist_it
    random.shuffle(choices_it)
    choices_en = []
    for c in choices_it:
        found = False
        for pit, pen in all_phrases:
            if pit == c:
                choices_en.append(pen)
                found = True
                break
        if not found: choices_en.append("???")

    phrases_json.append({
        "id": f"s12-p{i+1}",
        "italian": it,
        "english": en,
        "type": "phrase",
        "choicesItalian": choices_it,
        "choicesEnglish": choices_en,
        "feedback": {
            "correctItalian": "Ottimo!",
            "incorrectItalian": "Riprova.",
            "correctEnglish": "Great!",
            "incorrectEnglish": "Try again."
        },
        "audio": {"italian": ""}
    })

# Write files
with open(base_path + f'{prefix}_vocabulary.json', 'w', encoding='utf-8') as f:
    json.dump(vocab_json, f, indent=2, ensure_ascii=False)
with open(base_path + f'{prefix}_phrases.json', 'w', encoding='utf-8') as f:
    json.dump(phrases_json, f, indent=2, ensure_ascii=False)
with open(base_path + f'{prefix}_sentences.json', 'w', encoding='utf-8') as f:
    json.dump(sentences_json, f, indent=2, ensure_ascii=False)
