import json
import os

path = "./src/data/exports/tech/online_booking/conversations.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

new_messages_template = [
    {
        "role": "host",
        "text": "Hai visto il prezzo totale?",
        "english": "Did you see the total price?",
        "choices": [
            {
                "text": "Sì, ho visto il prezzo totale. Tutto bene.",
                "english": "Yes, I saw the total price. Everything is fine.",
                "isCorrect": True,
                "feedback": "Correct."
            },
            {
                "text": "Voglio mangiare una pizza con tanta mozzarella.",
                "english": "I want to eat a pizza with a lot of mozzarella.",
                "isCorrect": False,
                "feedback": "Wrong domain."
            },
            {
                "text": "Il mio gatto sta male.",
                "english": "My cat is sick.",
                "isCorrect": False,
                "feedback": "Wrong domain."
            }
        ]
    },
    {
        "role": "host",
        "text": "Ottimo. Hai controllato la data?",
        "english": "Excellent. Did you check the date?",
        "choices": [
            {
                "text": "Sì, ho guardato la data. Esatto.",
                "english": "Yes, I looked at the date. Exactly.",
                "isCorrect": True,
                "feedback": "Correct."
            },
            {
                "text": "Prendo un menu fisso per favore.",
                "english": "I'll take a set menu please.",
                "isCorrect": False,
                "feedback": "Wrong domain."
            },
            {
                "text": "Il medico mi ha dato una cura.",
                "english": "The doctor gave me a cure.",
                "isCorrect": False,
                "feedback": "Wrong domain."
            }
        ]
    },
    {
        "role": "host",
        "text": "Vedi il pulsante verde a destra?",
        "english": "Do you see the green button on the right?",
        "choices": [
            {
                "text": "Sì, vedo il pulsante verde.",
                "english": "Yes, I see the green button.",
                "isCorrect": True,
                "feedback": "Correct."
            },
            {
                "text": "Devo pagare il conto al cameriere.",
                "english": "I have to pay the bill to the waiter.",
                "isCorrect": False,
                "feedback": "Wrong domain."
            },
            {
                "text": "Scusi, dov'è il pronto soccorso?",
                "english": "Excuse me, where is the emergency room?",
                "isCorrect": False,
                "feedback": "Wrong domain."
            }
        ]
    },
    {
        "role": "host",
        "text": "Hai messo i dati della tua carta?",
        "english": "Did you put your card details?",
        "choices": [
            {
                "text": "Sì, ho messo i dati per il pagamento.",
                "english": "Yes, I put the details for the payment.",
                "isCorrect": True,
                "feedback": "Correct."
            },
            {
                "text": "Il gatto nero ha mangiato tutto.",
                "english": "The black cat ate everything.",
                "isCorrect": False,
                "feedback": "Wrong domain."
            },
            {
                "text": "Non voglio andare in ospedale.",
                "english": "I don't want to go to the hospital.",
                "isCorrect": False,
                "feedback": "Wrong domain."
            }
        ]
    },
    {
        "role": "host",
        "text": "Tutto fatto. Puoi stare tranquillo.",
        "english": "All done. You can rest easy.",
        "choices": [
            {
                "text": "Perfetto, grazie mille.",
                "english": "Perfect, thanks a lot.",
                "isCorrect": True,
                "feedback": "Correct."
            },
            {
                "text": "Voglio un tavolo per due persone.",
                "english": "I want a table for two people.",
                "isCorrect": False,
                "feedback": "Wrong domain."
            },
            {
                "text": "La mia casa è molto grande.",
                "english": "My house is very big.",
                "isCorrect": False,
                "feedback": "Wrong domain."
            }
        ]
    }
]

for conv in data["conversations"]:
    m_count = len(conv["messages"])
    while m_count < 10:
        template = dict(new_messages_template[m_count - 5])
        template["id"] = f"m{m_count + 1}"
        conv["messages"].append(template)
        m_count += 1

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Conversations extended to 10 messages.")
