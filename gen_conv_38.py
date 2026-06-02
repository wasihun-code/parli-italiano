import json

data = {
    "scenarioId": 38,
    "conversations": [
        {
            "id": "quick_espresso",
            "title": "Quick Espresso",
            "description": "Order a quick espresso at the counter.",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Buongiorno! Prego, dimmi pure.",
                    "english": "Good morning! Please, tell me.",
                    "choices": [
                        {"text": "Buongiorno. Un caffè, per favore.", "isCorrect": True, "feedback": "Perfetto!"},
                        {"text": "Voglio un tavolo grande ora.", "isCorrect": False, "feedback": "Too aggressive and not right for a quick espresso."},
                        {"text": "Dov'è il bagno degli uomini?", "isCorrect": False, "feedback": "Start with ordering!"}
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Certamente. Normale o macchiato?",
                    "english": "Certainly. Normal or with a spot of milk?",
                    "choices": [
                        {"text": "Normale, grazie. Molto gentile.", "isCorrect": True, "feedback": "Ottimo."},
                        {"text": "Voglio un piatto di pasta.", "isCorrect": False, "feedback": "You don't order pasta at a breakfast bar."},
                        {"text": "Non mi piace il caffè oggi.", "isCorrect": False, "feedback": "Then why did you order it?"}
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Ecco il tuo caffè. Zucchero?",
                    "english": "Here is your coffee. Sugar?",
                    "choices": [
                        {"text": "Sì, una bustina, per favore.", "isCorrect": True, "feedback": "Benissimo."},
                        {"text": "No, non mangio mai niente.", "isCorrect": False, "feedback": "Sugar is for the coffee, not eating."},
                        {"text": "Voglio un pezzo di torta.", "isCorrect": False, "feedback": "Answer the question about sugar first."}
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Lo zucchero è lì sul banco.",
                    "english": "The sugar is there on the counter.",
                    "choices": [
                        {"text": "Ah, lo vedo, grazie mille!", "isCorrect": True, "feedback": "Great response."},
                        {"text": "Non c'è il mio tavolo qui.", "isCorrect": False, "feedback": "You are at the counter."},
                        {"text": "Vado via senza pagare ora.", "isCorrect": False, "feedback": "You must pay!"}
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Vuoi anche un bicchiere d'acqua?",
                    "english": "Do you also want a glass of water?",
                    "choices": [
                        {"text": "Sì, grazie, acqua naturale.", "isCorrect": True, "feedback": "Perfect."},
                        {"text": "No, voglio un vino rosso.", "isCorrect": False, "feedback": "It's morning!"},
                        {"text": "Non ho sete, voglio bere.", "isCorrect": False, "feedback": "Contradictory."}
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Ecco l'acqua. Mangi qualcosa?",
                    "english": "Here is the water. Are you eating anything?",
                    "choices": [
                        {"text": "No, oggi solo un caffè, grazie.", "isCorrect": True, "feedback": "Good."},
                        {"text": "Voglio mangiare una bistecca.", "isCorrect": False, "feedback": "Not at a breakfast bar."},
                        {"text": "Sì, ma non so cosa voglio.", "isCorrect": False, "feedback": "Usually you decide quickly at the bar."}
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "Va bene. Sei di fretta oggi?",
                    "english": "Alright. Are you in a hurry today?",
                    "choices": [
                        {"text": "Sì, devo andare al lavoro.", "isCorrect": True, "feedback": "Very natural."},
                        {"text": "No, vivo qui per sempre.", "isCorrect": False, "feedback": "A bit strange."},
                        {"text": "Non parlo mai di lavoro.", "isCorrect": False, "feedback": "Too blunt."}
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Allora fai presto! Quant'è?",
                    "english": "Then be quick! How much is it?",
                    "choices": [
                        {"text": "Quanto costa in totale?", "isCorrect": True, "feedback": "Correct way to ask."},
                        {"text": "Non voglio pagare niente.", "isCorrect": False, "feedback": "You have to pay."},
                        {"text": "È troppo caro per me oggi.", "isCorrect": False, "feedback": "You don't know the price yet!"}
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Sono un euro e venti.",
                    "english": "It's one euro and twenty.",
                    "choices": [
                        {"text": "Ecco due euro, tieni il resto.", "isCorrect": True, "feedback": "Generous and correct."},
                        {"text": "Non ho soldi, mi dispiace.", "isCorrect": False, "feedback": "You must pay!"},
                        {"text": "Ti do cento euro in contanti.", "isCorrect": False, "feedback": "Too big of a bill for a coffee."}
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Grazie, buona giornata e buon lavoro!",
                    "english": "Thank you, have a good day and good work!",
                    "choices": [
                        {"text": "Grazie a te, buona giornata!", "isCorrect": True, "feedback": "Perfect closing."},
                        {"text": "Non voglio lavorare oggi.", "isCorrect": False, "feedback": "Not a standard polite response."},
                        {"text": "Dove posso andare a dormire?", "isCorrect": False, "feedback": "Irrelevant now."}
                    ]
                }
            ]
        },
        {
            "id": "cappuccino_and_pastry",
            "title": "Cappuccino and Pastry",
            "description": "Order a cappuccino and a brioche.",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Buongiorno! Cosa ti preparo?",
                    "english": "Good morning! What can I make you?",
                    "choices": [
                        {"text": "Vorrei un cappuccino, per favore.", "isCorrect": True, "feedback": "Good start."},
                        {"text": "Voglio un tavolo grande qui.", "isCorrect": False, "feedback": "Not what was asked."},
                        {"text": "Dove posso comprare i biglietti?", "isCorrect": False, "feedback": "Wrong place."}
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Certo! Lo vuoi con tanto latte?",
                    "english": "Sure! Do you want it with a lot of milk?",
                    "choices": [
                        {"text": "Sì, con tanto latte, grazie.", "isCorrect": True, "feedback": "Good."},
                        {"text": "No, senza caffè per niente.", "isCorrect": False, "feedback": "Then it's not a cappuccino."},
                        {"text": "Voglio un tè molto caldo.", "isCorrect": False, "feedback": "You just ordered a cappuccino."}
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Ottimo. Vuoi anche mangiare qualcosa?",
                    "english": "Excellent. Do you also want to eat something?",
                    "choices": [
                        {"text": "Sì, una brioche alla marmellata.", "isCorrect": True, "feedback": "Classic Italian breakfast."},
                        {"text": "Voglio un pezzo di pizza.", "isCorrect": False, "feedback": "Not typical for a sweet breakfast."},
                        {"text": "Non ho fame, ma mangio molto.", "isCorrect": False, "feedback": "Contradictory."}
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Mi dispiace, la marmellata è finita.",
                    "english": "I'm sorry, the jam is finished.",
                    "choices": [
                        {"text": "Allora prendo una brioche vuota.", "isCorrect": True, "feedback": "Good backup plan."},
                        {"text": "Allora non voglio il cappuccino.", "isCorrect": False, "feedback": "A bit extreme!"},
                        {"text": "Dov'è il negozio di frutta?", "isCorrect": False, "feedback": "Irrelevant."}
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Una brioche vuota e un cappuccino.",
                    "english": "A plain brioche and a cappuccino.",
                    "choices": [
                        {"text": "Sì, esatto. Va benissimo così.", "isCorrect": True, "feedback": "Good confirmation."},
                        {"text": "No, ho cambiato idea ora.", "isCorrect": False, "feedback": "Make up your mind!"},
                        {"text": "Voglio anche un caffè nero.", "isCorrect": False, "feedback": "You already ordered a lot."}
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Ecco a te. Mangi qui al banco?",
                    "english": "Here you go. Are you eating here at the counter?",
                    "choices": [
                        {"text": "Sì, mangio qui al banco.", "isCorrect": True, "feedback": "Very common in Italy."},
                        {"text": "No, vado al cinema subito.", "isCorrect": False, "feedback": "A bit strange to announce."},
                        {"text": "Voglio dormire sul divano.", "isCorrect": False, "feedback": "Not appropriate."}
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "Vuoi un po' di cacao sopra?",
                    "english": "Do you want some cocoa on top?",
                    "choices": [
                        {"text": "Sì, grazie. Solo un po'.", "isCorrect": True, "feedback": "Tasty!"},
                        {"text": "No, voglio tanto sale oggi.", "isCorrect": False, "feedback": "Salt on a cappuccino?"},
                        {"text": "Cosa c'è nel mio zaino?", "isCorrect": False, "feedback": "Nonsense."}
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Bene. Hai già lo scontrino?",
                    "english": "Good. Do you already have the receipt?",
                    "choices": [
                        {"text": "No, devo ancora pagare.", "isCorrect": True, "feedback": "Honest and correct."},
                        {"text": "Sì, l'ho perso ieri sera.", "isCorrect": False, "feedback": "Yesterday's receipt is no good."},
                        {"text": "Non uso mai gli scontrini.", "isCorrect": False, "feedback": "It's the law in Italy!"}
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Va bene, puoi pagare dopo.",
                    "english": "Alright, you can pay after.",
                    "choices": [
                        {"text": "Perfetto, allora faccio colazione.", "isCorrect": True, "feedback": "Enjoy!"},
                        {"text": "Non voglio mangiare più niente.", "isCorrect": False, "feedback": "You just ordered."},
                        {"text": "Esco subito dalla porta.", "isCorrect": False, "feedback": "You haven't eaten or paid."}
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Com'era la brioche? Tutto bene?",
                    "english": "How was the brioche? Everything good?",
                    "choices": [
                        {"text": "Buonissima, grazie. Quanto devo?", "isCorrect": True, "feedback": "Great finish."},
                        {"text": "Era molto cattiva e dura.", "isCorrect": False, "feedback": "A bit rude."},
                        {"text": "Non l'ho ancora mangiata.", "isCorrect": False, "feedback": "You had time to eat it."}
                    ]
                }
            ]
        },
        {
            "id": "paying_first",
            "title": "Paying at the Cashier First",
            "description": "Pay at the cashier before ordering at the bar.",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Buongiorno! Prendi lo scontrino alla cassa.",
                    "english": "Good morning! Get the receipt at the cashier.",
                    "choices": [
                        {"text": "Ah, devo pagare prima? Va bene.", "isCorrect": True, "feedback": "Good realization."},
                        {"text": "Non voglio pagare mai niente.", "isCorrect": False, "feedback": "You have to pay."},
                        {"text": "Voglio il caffè ora subito.", "isCorrect": False, "feedback": "Follow the rules."}
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Sì, le regole sono queste.",
                    "english": "Yes, these are the rules.",
                    "choices": [
                        {"text": "Nessun problema. Vado alla cassa.", "isCorrect": True, "feedback": "Very polite."},
                        {"text": "Le regole non mi piacciono.", "isCorrect": False, "feedback": "Unnecessary."},
                        {"text": "Dove posso ballare adesso?", "isCorrect": False, "feedback": "Irrelevant."}
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Alla cassa: Cosa prendi oggi?",
                    "english": "At the cashier: What are you having today?",
                    "choices": [
                        {"text": "Un caffè macchiato e un cornetto.", "isCorrect": True, "feedback": "Perfect order."},
                        {"text": "Un biglietto per il treno.", "isCorrect": False, "feedback": "Wrong place."},
                        {"text": "Una stanza per la notte.", "isCorrect": False, "feedback": "This is a bar, not a hotel."}
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Il cornetto alla crema o al cioccolato?",
                    "english": "The croissant with cream or chocolate?",
                    "choices": [
                        {"text": "Alla crema, grazie. È il mio preferito.", "isCorrect": True, "feedback": "Good choice."},
                        {"text": "Non mi piace il cornetto.", "isCorrect": False, "feedback": "But you just ordered one."},
                        {"text": "Voglio un panino con salame.", "isCorrect": False, "feedback": "Not what was asked."}
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Sono tre euro in tutto.",
                    "english": "It's three euros in total.",
                    "choices": [
                        {"text": "Ecco tre euro esatti, grazie.", "isCorrect": True, "feedback": "Easy transaction."},
                        {"text": "Posso pagare con un bacio?", "isCorrect": False, "feedback": "No, you can't."},
                        {"text": "Ti do cinquanta euro, dai il resto.", "isCorrect": False, "feedback": "A bit big, but 'esatti' is better."}
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Ecco lo scontrino. Vai al banco.",
                    "english": "Here is the receipt. Go to the counter.",
                    "choices": [
                        {"text": "Grazie. Vado subito al banco.", "isCorrect": True, "feedback": "Following instructions."},
                        {"text": "Non voglio andare al banco.", "isCorrect": False, "feedback": "Then you won't get your coffee."},
                        {"text": "Posso bere il caffè qui?", "isCorrect": False, "feedback": "You need to go to the counter."}
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "Al banco: Ciao, dammi lo scontrino.",
                    "english": "At the counter: Hi, give me the receipt.",
                    "choices": [
                        {"text": "Eccolo qui. Un caffè macchiato, per favore.", "isCorrect": True, "feedback": "Perfect handover and reminder of the order."},
                        {"text": "Non so dov'è lo scontrino.", "isCorrect": False, "feedback": "You just got it."},
                        {"text": "Voglio un bicchiere di vino.", "isCorrect": False, "feedback": "Wrong order."}
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Certo, arrivo subito con il caffè.",
                    "english": "Sure, I'll be right back with the coffee.",
                    "choices": [
                        {"text": "E il cornetto alla crema, per favore.", "isCorrect": True, "feedback": "Good reminder for the food."},
                        {"text": "Voglio andare a casa adesso.", "isCorrect": False, "feedback": "Wait for your coffee."},
                        {"text": "Non ho tempo per aspettare.", "isCorrect": False, "feedback": "It's a quick espresso, just wait a second."}
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Ah sì, ecco il tuo cornetto.",
                    "english": "Ah yes, here is your croissant.",
                    "choices": [
                        {"text": "Sembra delizioso, grazie mille.", "isCorrect": True, "feedback": "Polite and appreciative."},
                        {"text": "È troppo piccolo per me.", "isCorrect": False, "feedback": "Rude."},
                        {"text": "Voglio un altro scontrino.", "isCorrect": False, "feedback": "You don't need one."}
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Buona colazione! Arrivederci.",
                    "english": "Enjoy your breakfast! Goodbye.",
                    "choices": [
                        {"text": "Grazie, arrivederci e buona giornata!", "isCorrect": True, "feedback": "Perfect ending."},
                        {"text": "Non voglio dire arrivederci.", "isCorrect": False, "feedback": "Rude."},
                        {"text": "Quanto costa tutto questo?", "isCorrect": False, "feedback": "You already paid."}
                    ]
                }
            ]
        },
        {
            "id": "sitting_at_table",
            "title": "Sitting at a Table",
            "description": "Sit at a table and order breakfast.",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Buongiorno, volete sedervi al tavolo?",
                    "english": "Good morning, do you want to sit at the table?",
                    "choices": [
                        {"text": "Sì, siamo in due. C'è posto?", "isCorrect": True, "feedback": "Perfect way to ask for a table."},
                        {"text": "No, non ci piace stare seduti.", "isCorrect": False, "feedback": "Then why are you here?"},
                        {"text": "Voglio dormire sul letto.", "isCorrect": False, "feedback": "Nonsense."}
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Certo, prego, accomodatevi qui.",
                    "english": "Sure, please, make yourselves comfortable here.",
                    "choices": [
                        {"text": "Grazie. Il cameriere arriva subito?", "isCorrect": True, "feedback": "Good question."},
                        {"text": "Non voglio questo tavolo brutto.", "isCorrect": False, "feedback": "Rude."},
                        {"text": "Dove posso lavare le mie mani?", "isCorrect": False, "feedback": "Maybe later."}
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Sì, arrivo per l'ordinazione.",
                    "english": "Yes, I'm coming for the order.",
                    "choices": [
                        {"text": "Prendiamo il menu, per favore.", "isCorrect": True, "feedback": "Good request."},
                        {"text": "Voglio andare via subito.", "isCorrect": False, "feedback": "You just sat down."},
                        {"text": "Siamo molto arrabbiati oggi.", "isCorrect": False, "feedback": "Not necessary."}
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Ecco i menu. Avete già deciso?",
                    "english": "Here are the menus. Have you already decided?",
                    "choices": [
                        {"text": "Sì. Due cappuccini e due brioche.", "isCorrect": True, "feedback": "Clear and simple order."},
                        {"text": "Vogliamo due pizze calde.", "isCorrect": False, "feedback": "It's breakfast time."},
                        {"text": "Non sappiamo cosa vogliamo mai.", "isCorrect": False, "feedback": "A bit strange."}
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "Brioche vuote o farcite?",
                    "english": "Plain or filled croissants?",
                    "choices": [
                        {"text": "Una al cioccolato e una alla crema.", "isCorrect": True, "feedback": "Delicious choice."},
                        {"text": "Una con carne e una con pesce.", "isCorrect": False, "feedback": "Yuck, not for breakfast."},
                        {"text": "Vogliamo solo due bicchieri d'acqua.", "isCorrect": False, "feedback": "You just ordered croissants."}
                    ]
                },
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Va bene. Porto subito.",
                    "english": "Alright. I'll bring it right away.",
                    "choices": [
                        {"text": "Grazie mille, aspettiamo qui.", "isCorrect": True, "feedback": "Polite."},
                        {"text": "Sbrigatevi, abbiamo molta fretta.", "isCorrect": False, "feedback": "Too aggressive."},
                        {"text": "Non vogliamo più niente ora.", "isCorrect": False, "feedback": "Make up your mind."}
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "Ecco i vostri cappuccini. Attenti, scotta!",
                    "english": "Here are your cappuccinos. Careful, it's hot!",
                    "choices": [
                        {"text": "Ah, grazie. Hanno un profumo buonissimo.", "isCorrect": True, "feedback": "Nice compliment."},
                        {"text": "Voglio un caffè freddo invece.", "isCorrect": False, "feedback": "You ordered hot cappuccino."},
                        {"text": "Non posso bere niente caldo.", "isCorrect": False, "feedback": "Then why order it?"}
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "E le brioche. Buon appetito!",
                    "english": "And the croissants. Enjoy your meal!",
                    "choices": [
                        {"text": "Grazie! Possiamo avere anche dell'acqua?", "isCorrect": True, "feedback": "Good follow-up request."},
                        {"text": "Non voglio mangiare questo.", "isCorrect": False, "feedback": "Rude."},
                        {"text": "Andiamo a casa adesso.", "isCorrect": False, "feedback": "You just got your food!"}
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "Certo, naturale o frizzante?",
                    "english": "Sure, still or sparkling?",
                    "choices": [
                        {"text": "Frizzante, grazie. Molto gentile.", "isCorrect": True, "feedback": "Perfect."},
                        {"text": "Voglio acqua dal rubinetto.", "isCorrect": False, "feedback": "Usually you order bottled water at a table."},
                        {"text": "Non ho sete per niente.", "isCorrect": False, "feedback": "You just asked for water."}
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Porto subito. Il conto lo porto dopo.",
                    "english": "I'll bring it right away. I'll bring the bill later.",
                    "choices": [
                        {"text": "Va benissimo, facciamo con calma.", "isCorrect": True, "feedback": "Good, you are at a table so take your time."},
                        {"text": "Voglio pagare in anticipo.", "isCorrect": False, "feedback": "At a table you usually pay after."},
                        {"text": "Non vogliamo pagare il conto.", "isCorrect": False, "feedback": "You must pay!"}
                    ]
                }
            ]
        }
    ]
}

with open("src/data/exports/dining/breakfast_bar/conversations.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
