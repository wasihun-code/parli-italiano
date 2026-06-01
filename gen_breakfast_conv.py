import json

def len_match(target, text1, text2):
    # This is a helper, but I will hardcode the distractors with roughly similar lengths.
    pass

conversations = []

# Helper to generate a conversation
def make_conv(conv_id, title, desc, turns_data):
    messages = []
    for i, t in enumerate(turns_data):
        messages.append({
            "id": f"{conv_id}_m{i+1}",
            "role": "waiter",
            "text": t["w_it"],
            "english": t["w_en"],
            "choices": [
                {
                    "text": t["c_it"],
                    "isCorrect": True,
                    "english": t["c_en"]
                },
                {
                    "text": t["d1_it"],
                    "isCorrect": False
                },
                {
                    "text": t["d2_it"],
                    "isCorrect": False
                }
            ]
        })
    return {
        "id": conv_id,
        "title": title,
        "description": desc,
        "messages": messages
    }

conv1 = make_conv(
    "ordering_coffee", "Ordering Coffee", "Order a coffee and a croissant for breakfast.",
    [
        {
            "w_it": "Buongiorno! Prego, accomodatevi.", "w_en": "Good morning! Please, have a seat.",
            "c_it": "Grazie, c'è un tavolo libero?", "c_en": "Thank you, is there a free table?",
            "d1_it": "Prego, è un piatto caldo?",
            "d2_it": "Subito, ho un treno oggi?"
        },
        {
            "w_it": "Sì, questo tavolo vicino alla finestra è libero.", "w_en": "Yes, this table near the window is free.",
            "c_it": "Perfetto, mi siedo qui.", "c_en": "Perfect, I sit here.",
            "d1_it": "Nessuno, io vado via.",
            "d2_it": "Stanco, io dormo ora."
        },
        {
            "w_it": "Cosa vi porto da bere?", "w_en": "What can I bring you to drink?",
            "c_it": "Vorrei un cappuccino, per favore.", "c_en": "I would like a cappuccino, please.",
            "d1_it": "Voglio un biglietto, di corsa.",
            "d2_it": "Vedo un giardino, per strada."
        },
        {
            "w_it": "Un cappuccino. E da mangiare?", "w_en": "A cappuccino. And to eat?",
            "c_it": "Un cornetto al cioccolato, grazie.", "c_en": "A chocolate croissant, thank you.",
            "d1_it": "Un momento di speranza, subito.",
            "d2_it": "Un quaderno di appunti, bianco."
        },
        {
            "w_it": "I cornetti sono sul tavolo del buffet.", "w_en": "The croissants are on the buffet table.",
            "c_it": "Ah, capisco. Vado a prenderlo.", "c_en": "Ah, I understand. I go to get it.",
            "d1_it": "Oh, mangio. Corro a vederlo.",
            "d2_it": "Eh, dormo. Vado a cantarlo."
        },
        {
            "w_it": "Volete anche un succo di frutta?", "w_en": "Do you also want a fruit juice?",
            "c_it": "Sì, un succo di arancia.", "c_en": "Yes, an orange juice.",
            "d1_it": "No, un litro di acqua.",
            "d2_it": "Sì, un gatto di marmo."
        },
        {
            "w_it": "Il succo d'arancia è finito, mi dispiace.", "w_en": "The orange juice is finished, I'm sorry.",
            "c_it": "Allora prendo un succo di mela.", "c_en": "Then I take an apple juice.",
            "d1_it": "Adesso lascio un sacco di neve.",
            "d2_it": "Oppure scrivo un libro di mare."
        },
        {
            "w_it": "Certo. Vi porto tutto subito.", "w_en": "Sure. I'll bring you everything right away.",
            "c_it": "Grazie mille, molto gentile.", "c_en": "Thank you very much, very kind.",
            "d1_it": "Troppo forte, quasi chiuso.",
            "d2_it": "Niente male, molto povero."
        },
        {
            "w_it": "Ecco il vostro cappuccino e il succo.", "w_en": "Here is your cappuccino and the juice.",
            "c_it": "Lo zucchero è sul tavolo?", "c_en": "Is the sugar on the table?",
            "d1_it": "Il quaderno è sul divano?",
            "d2_it": "Il telefono è sul cuscino?"
        },
        {
            "w_it": "Sì, trovate lo zucchero in quelle bustine.", "w_en": "Yes, you find the sugar in those sachets.",
            "c_it": "Perfetto, buona giornata.", "c_en": "Perfect, have a good day.",
            "d1_it": "Pessimo, brutta mattina.",
            "d2_it": "Normale, senza pensieri."
        }
    ]
)

conv2 = make_conv(
    "buffet_inquiry", "Buffet Inquiry", "Ask about the buffet options.",
    [
        {
            "w_it": "Buongiorno, la colazione è inclusa.", "w_en": "Good morning, breakfast is included.",
            "c_it": "Grazie. Il buffet è da questa parte?", "c_en": "Thank you. Is the buffet this way?",
            "d1_it": "Prego. Il cinema è da questa porta?",
            "d2_it": "Subito. Il medico è da quella parte?"
        },
        {
            "w_it": "Sì, il buffet è in fondo alla sala.", "w_en": "Yes, the buffet is at the back of the room.",
            "c_it": "Posso prendere quello che voglio?", "c_en": "Can I take whatever I want?",
            "d1_it": "Devo lasciare quello che trovo?",
            "d2_it": "Posso suonare quello che guardo?"
        },
        {
            "w_it": "Certo, è a volontà per tutti gli ospiti.", "w_en": "Sure, it is all-you-can-eat for all guests.",
            "c_it": "Avete anche opzioni salate oggi?", "c_en": "Do you also have savory options today?",
            "d1_it": "Siete anche persone felici domani?",
            "d2_it": "Dovete anche cantare stasera qui?"
        },
        {
            "w_it": "Sì, ci sono uova, formaggio e prosciutto.", "w_en": "Yes, there are eggs, cheese, and ham.",
            "c_it": "Le uova sono calde o fredde?", "c_en": "Are the eggs hot or cold?",
            "d1_it": "Le case sono vuote o piene?",
            "d2_it": "Le sedie sono basse o alte?"
        },
        {
            "w_it": "Le uova sono calde, preparate stamattina.", "w_en": "The eggs are hot, prepared this morning.",
            "c_it": "Prendo un po' di uova e pane.", "c_en": "I take some eggs and bread.",
            "d1_it": "Mangio un po' di sassi e neve.",
            "d2_it": "Lascio un po' di carte e libri."
        },
        {
            "w_it": "Ottima scelta. Volete anche dei cereali?", "w_en": "Excellent choice. Do you also want some cereals?",
            "c_it": "No grazie, preferisco la frutta.", "c_en": "No thank you, I prefer fruit.",
            "d1_it": "Sì prego, detesto la palla.",
            "d2_it": "No grazie, finisco la corsa."
        },
        {
            "w_it": "La frutta fresca è vicino allo yogurt.", "w_en": "The fresh fruit is near the yogurt.",
            "c_it": "Benissimo, prendo una mela rossa.", "c_en": "Very good, I take a red apple.",
            "d1_it": "Malissimo, lascio una scarpa blu.",
            "d2_it": "Subitissimo, tocco una porta rotta."
        },
        {
            "w_it": "Se avete bisogno di altro, chiedete pure.", "w_en": "If you need anything else, just ask.",
            "c_it": "Siete molto gentili, grazie.", "c_en": "You are very kind, thank you.",
            "d1_it": "Siamo poco lontani, scusa.",
            "d2_it": "Siete tanto veloci, prego."
        },
        {
            "w_it": "I piatti puliti sono sotto il tavolo.", "w_en": "The clean plates are under the table.",
            "c_it": "Ho trovato un piatto, grazie.", "c_en": "I found a plate, thank you.",
            "d1_it": "Ho perso un gatto, pronto.",
            "d2_it": "Ho preso un libro, scusa."
        },
        {
            "w_it": "Buon appetito e buona colazione!", "w_en": "Enjoy your meal and have a good breakfast!",
            "c_it": "Grazie, sembra tutto molto buono.", "c_en": "Thank you, everything looks very good.",
            "d1_it": "Prego, suona tutto molto strano.",
            "d2_it": "Scusa, piove tutto molto forte."
        }
    ]
)

conv3 = make_conv(
    "breakfast_times", "Breakfast Times", "Ask about when the breakfast service ends.",
    [
        {
            "w_it": "Buongiorno! Il numero della vostra camera?", "w_en": "Good morning! Your room number?",
            "c_it": "Buongiorno, la camera è la duecento.", "c_en": "Good morning, the room is two hundred.",
            "d1_it": "Buonasera, la strada è la prima.",
            "d2_it": "Buonanotte, la sedia è la rossa."
        },
        {
            "w_it": "Perfetto, siete sulla lista. Prego.", "w_en": "Perfect, you are on the list. Please.",
            "c_it": "Fino a che ora servite la colazione?", "c_en": "Until what time do you serve breakfast?",
            "d1_it": "Dopo di che giorno chiudete la porta?",
            "d2_it": "Prima di che anno comprate la borsa?"
        },
        {
            "w_it": "La colazione è servita fino alle dieci.", "w_en": "Breakfast is served until ten o'clock.",
            "c_it": "Quindi abbiamo ancora un'ora di tempo.", "c_en": "So we still have an hour of time.",
            "d1_it": "Allora corriamo ancora un'ora al parco.",
            "d2_it": "Forse dormiamo ancora un'ora in auto."
        },
        {
            "w_it": "Esattamente. Non c'è fretta.", "w_en": "Exactly. There is no rush.",
            "c_it": "Possiamo sederci ovunque vogliamo noi?", "c_en": "Can we sit wherever we want?",
            "d1_it": "Dobbiamo saltare ovunque crediamo noi?",
            "d2_it": "Vogliamo parlare ovunque pensiamo noi?"
        },
        {
            "w_it": "Sì, scegliete pure un tavolo libero.", "w_en": "Yes, just choose a free table.",
            "c_it": "Ci sediamo in quell'angolo tranquillo.", "c_en": "We sit in that quiet corner.",
            "d1_it": "Vi perdiamo in quest'albero grande.",
            "d2_it": "Ci alziamo in quell'ultimo momento."
        },
        {
            "w_it": "Volete che vi porti subito un caffè?", "w_en": "Do you want me to bring you a coffee right away?",
            "c_it": "Sì, due caffè macchiati, per favore.", "c_en": "Yes, two macchiato coffees, please.",
            "d1_it": "No, due gatti neri, di fretta.",
            "d2_it": "Sì, due cani bianchi, per strada."
        },
        {
            "w_it": "Arrivano subito. Il buffet è lì.", "w_en": "They are coming right away. The buffet is there.",
            "c_it": "Posso prendere anche dell'acqua frizzante?", "c_en": "Can I also take some sparkling water?",
            "d1_it": "Devo lasciare anche della terra bagnata?",
            "d2_it": "Voglio suonare anche della chitarra vecchia?"
        },
        {
            "w_it": "Sì, le bottiglie sono in quel frigorifero.", "w_en": "Yes, the bottles are in that fridge.",
            "c_it": "Vedo, sono proprio di fianco ai succhi.", "c_en": "I see, they are right next to the juices.",
            "d1_it": "Sento, sono proprio di fronte ai gatti.",
            "d2_it": "Parlo, sono proprio di sopra ai libri."
        },
        {
            "w_it": "Se alle dieci non avete finito, potete restare.", "w_en": "If at ten you haven't finished, you can stay.",
            "c_it": "Siete molto comprensivi, grazie mille davvero.", "c_en": "You are very understanding, thank you very much indeed.",
            "d1_it": "Siamo tanto distanti, scusa poco sicuro.",
            "d2_it": "Sono poco interessati, prego sempre qua."
        },
        {
            "w_it": "È un piacere avervi come nostri ospiti.", "w_en": "It is a pleasure to have you as our guests.",
            "c_it": "Ora vado a prendere qualcosa da mangiare.", "c_en": "Now I go to get something to eat.",
            "d1_it": "Ieri sono a lasciare qualcosa da leggere.",
            "d2_it": "Dopo vado a trovare qualcosa da perdere."
        }
    ]
)

conv4 = make_conv(
    "missing_cutlery", "Missing Cutlery", "Ask a waiter for some missing items like forks and napkins.",
    [
        {
            "w_it": "Tutto bene al vostro tavolo, signori?", "w_en": "Is everything fine at your table, gentlemen?",
            "c_it": "Scusi, mi manca una forchetta per mangiare.", "c_en": "Excuse me, I am missing a fork to eat.",
            "d1_it": "Prego, ti serve una coperta per dormire.",
            "d2_it": "Pronto, gli cade una scarpa per correre."
        },
        {
            "w_it": "Mi scusi, ve ne porto subito una.", "w_en": "Excuse me, I'll bring you one right away.",
            "c_it": "Potrebbe portare anche dei tovaglioli di carta?", "c_en": "Could you also bring some paper napkins?",
            "d1_it": "Dovrebbe lasciare anche dei quaderni di legno?",
            "d2_it": "Vorrebbe suonare anche dei campanelli di ferro?"
        },
        {
            "w_it": "Certamente, le porto forchetta e tovaglioli.", "w_en": "Certainly, I'll bring you a fork and napkins.",
            "c_it": "Anche un coltello, se è possibile.", "c_en": "Also a knife, if it is possible.",
            "d1_it": "Anche un tappeto, se è probabile.",
            "d2_it": "Anche un pennello, se è difficile."
        },
        {
            "w_it": "Nessun problema. Vi serve altro?", "w_en": "No problem. Do you need anything else?",
            "c_it": "Mio marito vorrebbe un cucchiaino per il caffè.", "c_en": "My husband would like a teaspoon for the coffee.",
            "d1_it": "Mio fratello vorrebbe un martello per il muro.",
            "d2_it": "Mio nonno vorrebbe un cappello per il vento."
        },
        {
            "w_it": "Ecco a voi: forchetta, coltello, cucchiaino e tovaglioli.", "w_en": "Here you go: fork, knife, teaspoon, and napkins.",
            "c_it": "Siete stati velocissimi, vi ringrazio tanto.", "c_en": "You have been very fast, I thank you very much.",
            "d1_it": "Siamo stati lentissimi, ti salutiamo poco.",
            "d2_it": "Siete stati tristissimi, ci scusiamo male."
        },
        {
            "w_it": "Manca per caso il latte per il caffè?", "w_en": "Are you missing the milk for the coffee by any chance?",
            "c_it": "No, il latte lo abbiamo già preso.", "c_en": "No, we have already taken the milk.",
            "d1_it": "Sì, il sasso lo abbiamo già perso.",
            "d2_it": "No, il gatto lo abbiamo già dato."
        },
        {
            "w_it": "La macchina del caffè funziona bene?", "w_en": "Is the coffee machine working well?",
            "c_it": "Sì, fa un caffè davvero molto buono.", "c_en": "Yes, it makes a really very good coffee.",
            "d1_it": "No, fa un rumore davvero molto basso.",
            "d2_it": "Sì, fa un salto davvero molto lento."
        },
        {
            "w_it": "Ottimo. Volete della marmellata per il pane?", "w_en": "Excellent. Do you want some jam for the bread?",
            "c_it": "Abbiamo preso il burro, grazie lo stesso.", "c_en": "We took the butter, thanks anyway.",
            "d1_it": "Avete perso il cane, prego lo stesso.",
            "d2_it": "Abbiamo visto il mare, scusa lo stesso."
        },
        {
            "w_it": "I bicchieri per l'acqua sono puliti?", "w_en": "Are the water glasses clean?",
            "c_it": "Sì, è tutto a posto e pulito.", "c_en": "Yes, everything is fine and clean.",
            "d1_it": "No, è niente a terra e sporco.",
            "d2_it": "Sì, è sempre al buio e chiuso."
        },
        {
            "w_it": "Molto bene. Se serve qualcosa chiamatemi.", "w_en": "Very well. If you need anything call me.",
            "c_it": "Senz'altro, per ora abbiamo tutto qui.", "c_en": "Certainly, for now we have everything here.",
            "d1_it": "Nessuno, per dopo perdiamo niente lì.",
            "d2_it": "Tuttavia, per sempre lasciamo poco su."
        }
    ]
)

final_data = {
    "scenarioId": 21,
    "conversations": [conv1, conv2, conv3, conv4]
}

with open("src/data/exports/accommodation/breakfast_at_hotel/conversations.json", "w", encoding="utf-8") as f:
    json.dump(final_data, f, indent=2, ensure_ascii=False)
