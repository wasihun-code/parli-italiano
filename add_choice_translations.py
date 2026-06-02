import json

def add_english_to_choices():
    file_path = 'src/data/exports/culture/live_music/conversations.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for conv in data['conversations']:
        for msg in conv['messages']:
            for choice in msg['choices']:
                if choice['isCorrect'] and 'english' not in choice:
                    # Map the italian text to english
                    it = choice['text']
                    # We can use a simple mapping or just set it based on our previous knowledge
                    # For new messages m6-m10 in each conversation
                    
                    translations = {
                        "Ho solo le chiavi e il portafoglio qui.": "I only have my keys and wallet here.",
                        "Sì, grazie! È molto utile per orientarsi.": "Yes, thanks! It's very useful for orienting oneself.",
                        "Capito, grazie per l'informazione.": "Understood, thanks for the information.",
                        "Sì, dove si trovano esattamente?": "Yes, where are they located exactly?",
                        "Grazie, vado subito a controllare. Buon concerto!": "Thanks, I'm going to check right away. Have a good concert!",
                        "Sì, prendo un pacchetto di patatine, grazie.": "Yes, I'll take a pack of chips, thanks.",
                        "Va bene, ecco i due euro. Grazie!": "Alright, here are the two euros. Thanks!",
                        "Sì, per favore. Uno è sufficiente.": "Yes, please. One is enough.",
                        "Sì, vedo. Mi sposto subito verso il palco.": "Yes, I see. I'm moving toward the stage right away.",
                        "Grazie mille, buona serata anche a te!": "Thank you very much, have a good evening too!",
                        "No, non lo sapevo. Come si chiama il gruppo?": "No, I didn't know. What is the group called?",
                        "Capito. Allora il cantante inizia più tardi.": "Understood. So the singer starts later.",
                        "Perfetto, ho tempo per fare un giro.": "Perfect, I have time to take a look around.",
                        "Grazie, ma non fumo. Resto qui vicino.": "Thanks, but I don't smoke. I'll stay nearby.",
                        "Lo spero proprio! Grazie per le informazioni.": "I really hope so! Thanks for the information.",
                        "Sì, li ho visti vicino alle magliette.": "Yes, I saw them near the t-shirts.",
                        "Credo che costino dieci euro l'uno.": "I think they cost ten euros each.",
                        "Fai bene, sono molto belli e colorati.": "You're right, they are very beautiful and colorful.",
                        "Sì, suonano in un'altra città qui vicino.": "Yes, they are playing in another city nearby.",
                        "Assolutamente! Una serata da ricordare. Ciao!": "Absolutely! An evening to remember. Bye!"
                    }
                    if it in translations:
                        choice['english'] = translations[it]

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

add_english_to_choices()
