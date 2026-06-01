
import json
import os

scenario_id = 31

conversations = [
    {
        "id": "classic_cone",
        "title": "Classic Cone",
        "description": "Order a simple cone with two flavors.",
        "messages": [
            {
                "id": "m1",
                "role": "host",
                "text": "Buonasera! Benvenuti da noi. Volete un gelato?",
                "english": "Good evening! Welcome to our shop. Would you like a gelato?",
                "choices": [
                    {"text": "Sì, vorrei un gelato, per favore.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "No, grazie, non prendo nulla.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Buonasera, dove sono i bagni?", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m2",
                "role": "host",
                "text": "Certamente. Preferisce un cono o una coppetta?",
                "english": "Certainly. Do you prefer a cone or a cup?",
                "choices": [
                    {"text": "Vorrei un cono, grazie.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Prendo una pizza margherita.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Mi dia un bicchiere d'acqua.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m3",
                "role": "host",
                "text": "Ottimo. Che dimensione desidera per il cono? Piccolo o medio?",
                "english": "Excellent. What size would you like for the cone? Small or medium?",
                "choices": [
                    {"text": "Un cono piccolo va bene.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Un cono molto lontano.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Vorrei un tavolo per quattro.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m4",
                "role": "host",
                "text": "Va bene. Un cono piccolo può avere due gusti. Quali preferisce?",
                "english": "All right. A small cone can have two flavors. Which ones do you prefer?",
                "choices": [
                    {"text": "Vorrei cioccolato e fragola.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Prendo pasta al forno e riso.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Vorrei due chili di mele.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m5",
                "role": "host",
                "text": "Abbiamo il cioccolato fondente o al latte. Quale vuole?",
                "english": "We have dark or milk chocolate. Which one do you want?",
                "choices": [
                    {"text": "Prendo il cioccolato fondente.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Prendo la vaniglia dolce.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Voglio il limone fresco.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m6",
                "role": "host",
                "text": "Perfetto. Vuole assaggiare un altro gusto prima di decidere?",
                "english": "Perfect. Do you want to taste another flavor before deciding?",
                "choices": [
                    {"text": "Sì, posso assaggiare il pistacchio?", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "No, non mi piace la frutta.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Sì, voglio un panino al cotto.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m7",
                "role": "host",
                "text": "Ecco a lei un cucchiaino. Le piace il nostro pistacchio?",
                "english": "Here is a small spoon. Do you like our pistachio?",
                "choices": [
                    {"text": "Sì, è delizioso! Prendo quello.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "No, è troppo salato per me.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Sì, dov'è l'uscita di sicurezza?", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m8",
                "role": "host",
                "text": "Ottima scelta. Vuole della panna montata sopra il gelato?",
                "english": "Excellent choice. Do you want whipped cream on top of the gelato?",
                "choices": [
                    {"text": "No, senza panna, grazie.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Sì, vorrei molta carne.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "No, preferisco il formaggio.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m9",
                "role": "host",
                "text": "Ecco il suo cono con cioccolato e pistacchio. Desidera altro?",
                "english": "Here is your cone with chocolate and pistachio. Do you want anything else?",
                "choices": [
                    {"text": "No, grazie. Quanto costa?", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Grazie, dov'è il mio zaino?", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Prego, posso avere il conto?", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m10",
                "role": "host",
                "text": "Sono tre euro e cinquanta centesimi, per favore.",
                "english": "It's three euros and fifty cents, please.",
                "choices": [
                    {"text": "Ecco a lei. Buona serata!", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Non ho soldi, mi scusi.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Tenga pure il resto caro.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m11",
                "role": "host",
                "text": "Grazie mille. Arrivederci e si goda il suo gelato!",
                "english": "Thank you very much. Goodbye and enjoy your gelato!",
                "choices": [
                    {"text": "Grazie, arrivederci!", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Buongiorno, che ore sono?", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Ciao, dove posso parcheggiare?", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            }
        ]
    },
    {
        "id": "chocolate_cup",
        "title": "Chocolate Cup",
        "description": "Order a medium cup with various chocolate flavors.",
        "messages": [
            {
                "id": "m1",
                "role": "host",
                "text": "Buongiorno! Cosa posso portarvi di buono oggi?",
                "english": "Good morning! What can I get you that's good today?",
                "choices": [
                    {"text": "Vorrei una coppetta di gelato.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Cerco un ombrello per la pioggia.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Vorrei un caffè molto forte.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m2",
                "role": "host",
                "text": "Va bene. Abbiamo tre misure: piccola, media e grande.",
                "english": "All right. We have three sizes: small, medium, and large.",
                "choices": [
                    {"text": "Prendo una coppetta media.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Voglio una sedia media.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Mi dia una borsa grande.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m3",
                "role": "host",
                "text": "Nella coppetta media può mettere tre gusti. Quali sceglie?",
                "english": "In a medium cup, you can put three flavors. Which ones do you choose?",
                "choices": [
                    {"text": "Cioccolato, stracciatella e nocciola.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Pasta, pizza e pane fresco.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Rosso, verde e blu scuro.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m4",
                "role": "host",
                "text": "Ottime scelte! Abbiamo anche il cioccolato bianco.",
                "english": "Excellent choices! We also have white chocolate.",
                "choices": [
                    {"text": "No, grazie, questi tre vanno bene.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Sì, vorrei una mela rossa.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "No, non mi piace il latte.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m5",
                "role": "host",
                "text": "Desidera del cioccolato fuso sopra il suo gelato?",
                "english": "Would you like some melted chocolate on top of your gelato?",
                "choices": [
                    {"text": "Sì, vorrei un po' di cioccolato fuso.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "No, voglio solo del sale.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Sì, mi dia un po' di pepe.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m6",
                "role": "host",
                "text": "Perfetto. Ecco la sua coppetta media. Serve altro?",
                "english": "Perfect. Here is your medium cup. Do you need anything else?",
                "choices": [
                    {"text": "Sì, posso avere un tovagliolo?", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "No, dov'è la stazione?", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Sì, mi serve un giornale.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m7",
                "role": "host",
                "text": "Ecco a lei il tovagliolo. Sono quattro euro in totale.",
                "english": "Here is the napkin for you. It's four euros in total.",
                "choices": [
                    {"text": "Ecco i soldi. Grazie mille.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Non ho fame adesso, grazie.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Il bagno è in fondo a destra.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m8",
                "role": "host",
                "text": "Grazie a lei. Le piace molto il cioccolato, vero?",
                "english": "Thank you. You like chocolate a lot, right?",
                "choices": [
                    {"text": "Sì, il cioccolato è il mio preferito.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "No, preferisco dormire molto.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Sì, la macchina è rossa.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m9",
                "role": "host",
                "text": "Si vede! Vuole sedersi fuori o porta via il gelato?",
                "english": "It shows! Do you want to sit outside or take the gelato away?",
                "choices": [
                    {"text": "Mi siedo fuori, grazie.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Vado in montagna domani.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Compro una bicicletta nuova.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m10",
                "role": "host",
                "text": "Va bene, i tavoli fuori sono liberi. Buona giornata!",
                "english": "All right, the tables outside are free. Have a nice day!",
                "choices": [
                    {"text": "Grazie, buona giornata anche a lei!", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Sì, piove molto forte oggi.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "No, non voglio studiare.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            }
        ]
    },
    {
        "id": "vegan_options",
        "title": "Vegan Options",
        "description": "Order fruit-based gelato without dairy.",
        "messages": [
            {
                "id": "m1",
                "role": "host",
                "text": "Ciao! Cercate qualcosa di fresco e leggero?",
                "english": "Hi! Are you looking for something fresh and light?",
                "choices": [
                    {"text": "Sì, vorrei un gelato alla frutta.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "No, cerco un cappotto pesante.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Sì, mi serve un ombrello.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m2",
                "role": "host",
                "text": "Abbiamo molti gusti alla frutta senza latte. Cono o coppetta?",
                "english": "We have many fruit flavors without milk. Cone or cup?",
                "choices": [
                    {"text": "Una coppetta piccola, per favore.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Un panino al formaggio, grazie.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Vorrei una bistecca al sangue.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m3",
                "role": "host",
                "text": "Va bene. Quali gusti desidera? Abbiamo limone e fragola.",
                "english": "All right. Which flavors do you want? We have lemon and strawberry.",
                "choices": [
                    {"text": "Vorrei limone e fragola, grazie.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Prendo prosciutto e melone.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Voglio sale e pepe nero.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m4",
                "role": "host",
                "text": "Il nostro limone è molto aspro. Le piacciono i gusti aspri?",
                "english": "Our lemon is very sour. Do you like sour flavors?",
                "choices": [
                    {"text": "Sì, mi piace molto il limone.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "No, non mi piace l'acqua.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Sì, preferisco la carne.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m5",
                "role": "host",
                "text": "Perfetto. Vuole aggiungere dei pezzetti di frutta fresca?",
                "english": "Perfect. Do you want to add some pieces of fresh fruit?",
                "choices": [
                    {"text": "No, così va bene. Grazie.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Sì, vorrei del formaggio.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "No, mi dia dello zucchero.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m6",
                "role": "host",
                "text": "Ecco a lei la sua coppetta. Desidera un cucchiaino?",
                "english": "Here is your cup. Would you like a small spoon?",
                "choices": [
                    {"text": "Sì, grazie. Quanto pago?", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "No, ho già una forchetta.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Sì, dov'è il supermercato?", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m7",
                "role": "host",
                "text": "Sono due euro e cinquanta centesimi. Il gelato è vegano.",
                "english": "It's two euros and fifty cents. The gelato is vegan.",
                "choices": [
                    {"text": "Ottimo, ecco a lei i soldi.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Peccato, volevo del latte.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Grazie, a che ora chiude?", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m8",
                "role": "host",
                "text": "Grazie mille. Fa molto caldo oggi, vero?",
                "english": "Thank you very much. It's very hot today, isn't it?",
                "choices": [
                    {"text": "Sì, il gelato è perfetto ora.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "No, piove e fa molto freddo.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Sì, la neve è bianca.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m9",
                "role": "host",
                "text": "È vero! Dove andate a mangiare il gelato?",
                "english": "That's true! Where are you going to eat the gelato?",
                "choices": [
                    {"text": "Vado a fare una passeggiata.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Vado a dormire subito.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Resto qui a pulire terra.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m10",
                "role": "host",
                "text": "Buona passeggiata allora! A presto.",
                "english": "Have a nice walk then! See you soon.",
                "choices": [
                    {"text": "Grazie mille, arrivederci!", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Sì, cerco un taxi veloce.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "No, non ho la chiave.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            }
        ]
    },
    {
        "id": "group_order",
        "title": "Group Order",
        "description": "Ordering gelato for multiple people.",
        "messages": [
            {
                "id": "m1",
                "role": "host",
                "text": "Buonasera! Siete un bel gruppo! Quanti gelati volete?",
                "english": "Good evening! You're a nice group! How many gelatos do you want?",
                "choices": [
                    {"text": "Vorremmo tre gelati in totale.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Vogliamo tre pizze grandi.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Siamo in dieci persone.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m2",
                "role": "host",
                "text": "Benissimo. Iniziamo dal primo: cono o coppetta?",
                "english": "Very well. Let's start with the first one: cone or cup?",
                "choices": [
                    {"text": "Il primo è un cono grande.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Il primo è un libro rosso.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Prendo un cono molto piccolo.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m3",
                "role": "host",
                "text": "D'accordo. E per quanto riguarda il secondo gelato?",
                "english": "Agreed. And what about the second gelato?",
                "choices": [
                    {"text": "Il secondo è una coppetta piccola.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Il secondo è un treno veloce.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Vorrei una coppetta molto cara.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m4",
                "role": "host",
                "text": "Perfetto. E per l'ultimo gelato del gruppo?",
                "english": "Perfect. And for the last gelato of the group?",
                "choices": [
                    {"text": "L'ultimo è un cono medio.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "L'ultimo è un cane nero.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Voglio un cono di plastica.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m5",
                "role": "host",
                "text": "Va bene. Quali sono i gusti per il cono grande?",
                "english": "All right. What are the flavors for the large cone?",
                "choices": [
                    {"text": "Cioccolato, crema e pistacchio.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Mela, pera e banana gialla.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Roma, Milano e Napoli centro.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m6",
                "role": "host",
                "text": "E per la coppetta e l'altro cono? Che gusti mettiamo?",
                "english": "And for the cup and the other cone? What flavors do we put?",
                "choices": [
                    {"text": "Fragola e vaniglia, per favore.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Pane e burro, grazie mille.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Acqua e vino rosso, grazie.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m7",
                "role": "host",
                "text": "Volete la panna montata su tutti i gelati?",
                "english": "Do you want whipped cream on all the gelatos?",
                "choices": [
                    {"text": "No, solo sul cono grande.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "Sì, voglio molta insalata.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "No, preferisco il pesce.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m8",
                "role": "host",
                "text": "Va bene. Preparo tutto subito. Volete pagare insieme?",
                "english": "All right. I'll prepare everything right away. Do you want to pay together?",
                "choices": [
                    {"text": "Sì, paghiamo tutto insieme.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "No, non voglio pagare nulla.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Sì, andiamo al cinema ora.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m9",
                "role": "host",
                "text": "Ottimo. In totale sono dieci euro e cinquanta centesimi.",
                "english": "Excellent. In total it's ten euros and fifty cents.",
                "choices": [
                    {"text": "Ecco a lei. Grazie mille.", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "È troppo caro, non compro.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Mi scusi, dove sono?", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            },
            {
                "id": "m10",
                "role": "host",
                "text": "Ecco i vostri gelati. Attenzione, si sciolgono in fretta!",
                "english": "Here are your gelatos. Careful, they melt quickly!",
                "choices": [
                    {"text": "Grazie, li mangiamo subito!", "isCorrect": True, "audio": {"italian": ""}},
                    {"text": "No, li portiamo in Canada.", "isCorrect": False, "audio": {"italian": ""}},
                    {"text": "Sì, fa molto freddo oggi.", "isCorrect": False, "audio": {"italian": ""}}
                ],
                "audio": {"italian": ""}
            }
        ]
    }
]

data = {
    "scenarioId": scenario_id,
    "conversations": conversations
}

with open("src/data/exports/dining/gelato_shop/conversations.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
