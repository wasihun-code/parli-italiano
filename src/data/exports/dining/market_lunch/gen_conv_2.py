import json
import os

conversations = [
  {
    "id": "asking_recommendations",
    "title": "Asking for Recommendations",
    "description": "Ask a market vendor for recommendations on fresh local products.",
    "messages": [
      {
        "id": "msg1",
        "role": "host",
        "text": "Buongiorno! Cerca qualcosa in particolare al nostro mercato?",
        "english": "Good morning! Are you looking for anything in particular at our market?",
        "choices": [
          {"text": "Buongiorno! Quali sono i vostri prodotti tipici?", "english": "Good morning! What are your typical products?", "isCorrect": True},
          {"text": "Buongiorno! Voglio comprare un biglietto.", "english": "Good morning! I want to buy a ticket.", "isCorrect": False},
          {"text": "Buongiorno! Dov'è la stazione degli autobus?", "english": "Good morning! Where is the bus station?", "isCorrect": False}
        ]
      },
      {
        "id": "msg2",
        "role": "host",
        "text": "Abbiamo formaggi freschi, salumi e pane fatto in casa.",
        "english": "We have fresh cheeses, cured meats, and homemade bread.",
        "choices": [
          {"text": "Ottimo, vorrei vedere i formaggi freschi.", "english": "Great, I would like to see the fresh cheeses.", "isCorrect": True},
          {"text": "Ottimo, vorrei vedere i vostri vestiti.", "english": "Great, I would like to see your clothes.", "isCorrect": False},
          {"text": "Ottimo, vorrei affittare una macchina.", "english": "Great, I would like to rent a car.", "isCorrect": False}
        ]
      },
      {
        "id": "msg3",
        "role": "host",
        "text": "Questo formaggio è fatto con latte locale, è molto saporito.",
        "english": "This cheese is made with local milk, it is very tasty.",
        "choices": [
          {"text": "Sembra delizioso. Ne prendo un pezzo, grazie.", "english": "It looks delicious. I'll take a piece, thank you.", "isCorrect": True},
          {"text": "Sembra costoso. Non mi piace la carne.", "english": "It looks expensive. I don't like meat.", "isCorrect": False},
          {"text": "Sembra sporco. Posso avere un tovagliolo?", "english": "It looks dirty. Can I have a napkin?", "isCorrect": False}
        ]
      },
      {
        "id": "msg4",
        "role": "host",
        "text": "Certo. Vuole anche dei salumi per accompagnarlo?",
        "english": "Of course. Do you also want some cured meats to accompany it?",
        "choices": [
          {"text": "Sì, mi consiglia un buon salame locale?", "english": "Yes, can you recommend a good local salami?", "isCorrect": True},
          {"text": "Sì, mi consiglia un buon albergo qui vicino?", "english": "Yes, can you recommend a good hotel nearby?", "isCorrect": False},
          {"text": "Sì, mi consiglia un dottore per favore?", "english": "Yes, can you recommend a doctor please?", "isCorrect": False}
        ]
      },
      {
        "id": "msg5",
        "role": "host",
        "text": "Questo salame con il pepe nero è molto popolare. Ne taglio un po'?",
        "english": "This salami with black pepper is very popular. Shall I cut some?",
        "choices": [
          {"text": "Perfetto, mi tagli due etti per favore.", "english": "Perfect, slice two hundred grams for me, please.", "isCorrect": True},
          {"text": "Perfetto, mi tagli due metri per favore.", "english": "Perfect, slice two meters for me, please.", "isCorrect": False},
          {"text": "Perfetto, mi porti due bottiglie per favore.", "english": "Perfect, bring me two bottles, please.", "isCorrect": False}
        ]
      },
      {
        "id": "msg6",
        "role": "host",
        "text": "Subito! Desidera che lo affetti sottile o più spesso?",
        "english": "Right away! Do you want it sliced thin or thicker?",
        "choices": [
          {"text": "Fette sottili, per favore, è più buono.", "english": "Thin slices, please, it's better.", "isCorrect": True},
          {"text": "Fette rosse, per favore, è più freddo.", "english": "Red slices, please, it's colder.", "isCorrect": False},
          {"text": "Fette rumorose, per favore, è più scuro.", "english": "Noisy slices, please, it's darker.", "isCorrect": False}
        ]
      },
      {
        "id": "msg7",
        "role": "host",
        "text": "Ecco qui le fette sottili. C'è altro che le serve oggi?",
        "english": "Here are the thin slices. Is there anything else you need today?",
        "choices": [
          {"text": "Avete anche della frutta fresca di stagione?", "english": "Do you also have fresh seasonal fruit?", "isCorrect": True},
          {"text": "Avete anche una doccia nella stanza?", "english": "Do you also have a shower in the room?", "isCorrect": False},
          {"text": "Avete anche un posto al finestrino?", "english": "Do you also have a window seat?", "isCorrect": False}
        ]
      },
      {
        "id": "msg8",
        "role": "host",
        "text": "Noi non vendiamo frutta, ma c'è una bancarella fantastica lì accanto.",
        "english": "We don't sell fruit, but there is a fantastic stall right next door.",
        "choices": [
          {"text": "Ah, grazie mille per il suggerimento.", "english": "Ah, thank you so much for the suggestion.", "isCorrect": True},
          {"text": "Ah, grazie mille per le scarpe nuove.", "english": "Ah, thank you so much for the new shoes.", "isCorrect": False},
          {"text": "Ah, grazie mille per il gatto nero.", "english": "Ah, thank you so much for the black cat.", "isCorrect": False}
        ]
      },
      {
        "id": "msg9",
        "role": "host",
        "text": "Si figuri! Allora, in totale per formaggio e salame sono quindici euro.",
        "english": "Don't mention it! So, in total for cheese and salami it is fifteen euros.",
        "choices": [
          {"text": "Ecco i quindici euro. Tenga il resto.", "english": "Here are the fifteen euros. Keep the change.", "isCorrect": True},
          {"text": "Ecco la carta d'imbarco. Grazie.", "english": "Here is the boarding pass. Thank you.", "isCorrect": False},
          {"text": "Ecco la valigia verde. Grazie.", "english": "Here is the green suitcase. Thank you.", "isCorrect": False}
        ]
      },
      {
        "id": "msg10",
        "role": "host",
        "text": "Grazie a lei! Spero che i nostri prodotti le piacciano. Arrivederci!",
        "english": "Thank you! I hope you like our products. Goodbye!",
        "choices": [
          {"text": "Sono sicuro di sì! Arrivederci e buona giornata.", "english": "I am sure I will! Goodbye and have a good day.", "isCorrect": True},
          {"text": "Sono sicuro di no! Buonanotte.", "english": "I am sure not! Good night.", "isCorrect": False},
          {"text": "Sono molto alto! A domani.", "english": "I am very tall! See you tomorrow.", "isCorrect": False}
        ]
      }
    ]
  },
  {
    "id": "buying_cheese_meats",
    "title": "Buying Cheese and Cured Meats",
    "description": "Specify weights like 'etto' and 'chilo' when ordering.",
    "messages": [
      {
        "id": "msg1",
        "role": "host",
        "text": "Prego signore, a chi tocca?",
        "english": "Go ahead sir, whose turn is it?",
        "choices": [
          {"text": "Tocca a me. Vorrei comprare del prosciutto.", "english": "It's my turn. I would like to buy some ham.", "isCorrect": True},
          {"text": "Tocca a me. Vorrei comprare un biglietto.", "english": "It's my turn. I would like to buy a ticket.", "isCorrect": False},
          {"text": "Tocca a me. Dov'è la fermata del tram?", "english": "It's my turn. Where is the tram stop?", "isCorrect": False}
        ]
      },
      {
        "id": "msg2",
        "role": "host",
        "text": "Prosciutto crudo o prosciutto cotto oggi?",
        "english": "Cured ham or cooked ham today?",
        "choices": [
          {"text": "Prosciutto crudo, per favore. Quello dolce.", "english": "Cured ham, please. The sweet one.", "isCorrect": True},
          {"text": "Prosciutto crudo, per favore. Quello stanco.", "english": "Cured ham, please. The tired one.", "isCorrect": False},
          {"text": "Prosciutto crudo, per favore. Quello giallo.", "english": "Cured ham, please. The yellow one.", "isCorrect": False}
        ]
      },
      {
        "id": "msg3",
        "role": "host",
        "text": "Eccolo, è freschissimo. Quanto ne vuole?",
        "english": "Here it is, it's very fresh. How much do you want?",
        "choices": [
          {"text": "Ne vorrei circa due etti e mezzo, grazie.", "english": "I would like about two hundred and fifty grams, thanks.", "isCorrect": True},
          {"text": "Ne vorrei circa due litri e mezzo, grazie.", "english": "I would like about two and a half liters, thanks.", "isCorrect": False},
          {"text": "Ne vorrei circa due chilometri, grazie.", "english": "I would like about two kilometers, thanks.", "isCorrect": False}
        ]
      },
      {
        "id": "msg4",
        "role": "host",
        "text": "Sono tre etti, lascio o tolgo una fetta?",
        "english": "It's three hundred grams, should I leave it or take a slice off?",
        "choices": [
          {"text": "Lascio pure, non c'è problema.", "english": "Leave it, no problem.", "isCorrect": True},
          {"text": "Lascio pure, non c'è nessun treno.", "english": "Leave it, there is no train.", "isCorrect": False},
          {"text": "Lascio pure, non c'è molta luce.", "english": "Leave it, there is not much light.", "isCorrect": False}
        ]
      },
      {
        "id": "msg5",
        "role": "host",
        "text": "Perfetto. Desidera anche del formaggio con il prosciutto?",
        "english": "Perfect. Do you also want some cheese with the ham?",
        "choices": [
          {"text": "Sì, mezzo chilo di formaggio stagionato, per favore.", "english": "Yes, half a kilo of aged cheese, please.", "isCorrect": True},
          {"text": "Sì, mezza bottiglia di vino rosso, per favore.", "english": "Yes, half a bottle of red wine, please.", "isCorrect": False},
          {"text": "Sì, mezzo litro d'acqua gassata, per favore.", "english": "Yes, half a liter of sparkling water, please.", "isCorrect": False}
        ]
      },
      {
        "id": "msg6",
        "role": "host",
        "text": "Ottima scelta. Abbiamo un formaggio di fossa eccellente.",
        "english": "Excellent choice. We have an excellent pit cheese.",
        "choices": [
          {"text": "Va benissimo. Prendo quello, grazie.", "english": "That's fine. I'll take that, thanks.", "isCorrect": True},
          {"text": "Va malissimo. Prendo il computer, grazie.", "english": "That's terrible. I'll take the computer, thanks.", "isCorrect": False},
          {"text": "Va benissimo. Prendo l'autobus, grazie.", "english": "That's fine. I'll take the bus, thanks.", "isCorrect": False}
        ]
      },
      {
        "id": "msg7",
        "role": "host",
        "text": "C'è qualcos'altro che posso offrirle dalla mia bancarella?",
        "english": "Is there anything else I can offer you from my stall?",
        "choices": [
          {"text": "Solo del pane fresco, se ne avete.", "english": "Just some fresh bread, if you have any.", "isCorrect": True},
          {"text": "Solo una camera matrimoniale, se ne avete.", "english": "Just a double room, if you have one.", "isCorrect": False},
          {"text": "Solo un volo diretto, se ne avete.", "english": "Just a direct flight, if you have one.", "isCorrect": False}
        ]
      },
      {
        "id": "msg8",
        "role": "host",
        "text": "Sì, abbiamo delle pagnotte integrali calde.",
        "english": "Yes, we have some warm wholemeal loaves.",
        "choices": [
          {"text": "Perfetto, me ne dia una grande.", "english": "Perfect, give me a large one.", "isCorrect": True},
          {"text": "Perfetto, me ne dia una verde.", "english": "Perfect, give me a green one.", "isCorrect": False},
          {"text": "Perfetto, me ne dia una arrabbiata.", "english": "Perfect, give me an angry one.", "isCorrect": False}
        ]
      },
      {
        "id": "msg9",
        "role": "host",
        "text": "Benissimo. Il totale è venti euro.",
        "english": "Very well. The total is twenty euros.",
        "choices": [
          {"text": "Ecco a lei venti euro in contanti.", "english": "Here are twenty euros in cash.", "isCorrect": True},
          {"text": "Ecco a lei la chiave della stanza.", "english": "Here is the room key for you.", "isCorrect": False},
          {"text": "Ecco a lei il biglietto aereo.", "english": "Here is the flight ticket for you.", "isCorrect": False}
        ]
      },
      {
        "id": "msg10",
        "role": "host",
        "text": "La ringrazio molto. Buon appetito!",
        "english": "Thank you very much. Enjoy your meal!",
        "choices": [
          {"text": "Grazie, buon lavoro e a presto!", "english": "Thanks, good work and see you soon!", "isCorrect": True},
          {"text": "Grazie, buon sonno e a ieri!", "english": "Thanks, sleep well and see you yesterday!", "isCorrect": False},
          {"text": "Grazie, buona pioggia e a dopo!", "english": "Thanks, good rain and see you later!", "isCorrect": False}
        ]
      }
    ]
  },
  {
    "id": "tasting_before_buying",
    "title": "Tasting Before Buying",
    "description": "Ask to taste a sample before committing to a purchase.",
    "messages": [
      {
        "id": "msg1",
        "role": "host",
        "text": "Buongiorno signora, guardi che belle olive fresche!",
        "english": "Good morning madam, look at these beautiful fresh olives!",
        "choices": [
          {"text": "Buongiorno. Posso assaggiare prima di comprare?", "english": "Good morning. Can I taste before buying?", "isCorrect": True},
          {"text": "Buongiorno. Posso dormire prima di mangiare?", "english": "Good morning. Can I sleep before eating?", "isCorrect": False},
          {"text": "Buongiorno. Posso guidare prima di comprare?", "english": "Good morning. Can I drive before buying?", "isCorrect": False}
        ]
      },
      {
        "id": "msg2",
        "role": "host",
        "text": "Ma certo! Provi questa oliva verde, è molto dolce.",
        "english": "But of course! Try this green olive, it's very sweet.",
        "choices": [
          {"text": "Mmm, è davvero squisita. Mi piace molto.", "english": "Mmm, it is really exquisite. I like it a lot.", "isCorrect": True},
          {"text": "Mmm, è davvero difficile. Mi piace leggere.", "english": "Mmm, it is really difficult. I like to read.", "isCorrect": False},
          {"text": "Mmm, è davvero lontana. Mi piace camminare.", "english": "Mmm, it is really far. I like to walk.", "isCorrect": False}
        ]
      },
      {
        "id": "msg3",
        "role": "host",
        "text": "Bene. Quante ne prepariamo per oggi?",
        "english": "Good. How many shall we prepare for today?",
        "choices": [
          {"text": "Ne prendo un chilo intero, per favore.", "english": "I'll take a whole kilo, please.", "isCorrect": True},
          {"text": "Ne prendo un anno intero, per favore.", "english": "I'll take a whole year, please.", "isCorrect": False},
          {"text": "Ne prendo un libro intero, per favore.", "english": "I'll take a whole book, please.", "isCorrect": False}
        ]
      },
      {
        "id": "msg4",
        "role": "host",
        "text": "Ottima scelta. Vuole assaggiare anche le olive nere al forno?",
        "english": "Excellent choice. Do you also want to taste the baked black olives?",
        "choices": [
          {"text": "Perché no? Sono molto curioso di provarle.", "english": "Why not? I am very curious to try them.", "isCorrect": True},
          {"text": "Perché no? Sono molto arrabbiato di provarle.", "english": "Why not? I am very angry to try them.", "isCorrect": False},
          {"text": "Perché no? Sono molto stanco di provarle.", "english": "Why not? I am very tired to try them.", "isCorrect": False}
        ]
      },
      {
        "id": "msg5",
        "role": "host",
        "text": "Ecco a lei. Attenzione che hanno ancora il nocciolo.",
        "english": "Here you go. Careful that they still have the pit.",
        "choices": [
          {"text": "Sono buonissime, ma preferisco solo quelle verdi oggi.", "english": "They are delicious, but I prefer only the green ones today.", "isCorrect": True},
          {"text": "Sono bellissime, ma preferisco solo la gonna blu oggi.", "english": "They are beautiful, but I prefer only the blue skirt today.", "isCorrect": False},
          {"text": "Sono lunghissime, ma preferisco solo la macchina nera oggi.", "english": "They are very long, but I prefer only the black car today.", "isCorrect": False}
        ]
      },
      {
        "id": "msg6",
        "role": "host",
        "text": "Come desidera. Allora le metto solo un chilo di olive verdi.",
        "english": "As you wish. Then I'll only put a kilo of green olives for you.",
        "choices": [
          {"text": "Sì, esatto. Le metta in un sacchetto resistente.", "english": "Yes, exactly. Put them in a sturdy bag.", "isCorrect": True},
          {"text": "Sì, esatto. Le metta nel frigorifero piccolo.", "english": "Yes, exactly. Put them in the small fridge.", "isCorrect": False},
          {"text": "Sì, esatto. Le metta sotto il letto.", "english": "Yes, exactly. Put them under the bed.", "isCorrect": False}
        ]
      },
      {
        "id": "msg7",
        "role": "host",
        "text": "Uso un contenitore di plastica chiusa, così non si rovesciano.",
        "english": "I use a closed plastic container, so they don't spill.",
        "choices": [
          {"text": "È un'ottima idea, così viaggio tranquillo.", "english": "It's a great idea, so I travel peacefully.", "isCorrect": True},
          {"text": "È un'ottima idea, così piove forte.", "english": "It's a great idea, so it rains hard.", "isCorrect": False},
          {"text": "È un'ottima idea, così sono arrabbiato.", "english": "It's a great idea, so I am angry.", "isCorrect": False}
        ]
      },
      {
        "id": "msg8",
        "role": "host",
        "text": "Ecco pronte le sue olive. Sono otto euro.",
        "english": "Here are your olives ready. It's eight euros.",
        "choices": [
          {"text": "Prego, ecco una banconota da dieci.", "english": "Here you go, here is a ten note.", "isCorrect": True},
          {"text": "Prego, ecco il passaporto verde.", "english": "Here you go, here is the green passport.", "isCorrect": False},
          {"text": "Prego, ecco una scarpa vecchia.", "english": "Here you go, here is an old shoe.", "isCorrect": False}
        ]
      },
      {
        "id": "msg9",
        "role": "host",
        "text": "Resto di due euro. Desidera lo scontrino?",
        "english": "Change of two euros. Do you want the receipt?",
        "choices": [
          {"text": "Sì, mi dia lo scontrino per favore.", "english": "Yes, give me the receipt please.", "isCorrect": True},
          {"text": "Sì, mi dia il treno per favore.", "english": "Yes, give me the train please.", "isCorrect": False},
          {"text": "Sì, mi dia l'aereo per favore.", "english": "Yes, give me the plane please.", "isCorrect": False}
        ]
      },
      {
        "id": "msg10",
        "role": "host",
        "text": "Certamente, eccolo qui nel sacchetto. A presto!",
        "english": "Certainly, here it is in the bag. See you soon!",
        "choices": [
          {"text": "Grazie e buon lavoro!", "english": "Thanks and good work!", "isCorrect": True},
          {"text": "Grazie e buon compleanno!", "english": "Thanks and happy birthday!", "isCorrect": False},
          {"text": "Grazie e buona fortuna!", "english": "Thanks and good luck!", "isCorrect": False}
        ]
      }
    ]
  },
  {
    "id": "ordering_quick_lunch",
    "title": "Ordering a Quick Lunch",
    "description": "Order a quick portion of hot food to eat at the market.",
    "messages": [
      {
        "id": "msg1",
        "role": "host",
        "text": "Benvenuti alla nostra rosticceria. Cosa vi servo?",
        "english": "Welcome to our deli. What can I serve you?",
        "choices": [
          {"text": "Salve, vorrei una porzione di lasagne da mangiare qui.", "english": "Hello, I would like a portion of lasagna to eat here.", "isCorrect": True},
          {"text": "Salve, vorrei una camera singola per una notte.", "english": "Hello, I would like a single room for one night.", "isCorrect": False},
          {"text": "Salve, vorrei un volo per Roma domattina.", "english": "Hello, I would like a flight to Rome tomorrow morning.", "isCorrect": False}
        ]
      },
      {
        "id": "msg2",
        "role": "host",
        "text": "Le lasagne sono appena uscite dal forno. C'è altro?",
        "english": "The lasagna just came out of the oven. Is there anything else?",
        "choices": [
          {"text": "Sì, vorrei anche una porzione di verdure grigliate.", "english": "Yes, I would also like a portion of grilled vegetables.", "isCorrect": True},
          {"text": "Sì, vorrei anche un paio di scarpe nuove.", "english": "Yes, I would also like a new pair of shoes.", "isCorrect": False},
          {"text": "Sì, vorrei anche una medicina per il mal di testa.", "english": "Yes, I would also like a medicine for headache.", "isCorrect": False}
        ]
      },
      {
        "id": "msg3",
        "role": "host",
        "text": "Zucchine o melanzane grigliate?",
        "english": "Grilled zucchini or eggplant?",
        "choices": [
          {"text": "Facciamo un po' e un po', se è possibile.", "english": "Let's do half and half, if it's possible.", "isCorrect": True},
          {"text": "Facciamo una borsa grande, se è possibile.", "english": "Let's do a large bag, if it's possible.", "isCorrect": False},
          {"text": "Facciamo un cappotto caldo, se è possibile.", "english": "Let's do a warm coat, if it's possible.", "isCorrect": False}
        ]
      },
      {
        "id": "msg4",
        "role": "host",
        "text": "Certamente. Da bere cosa desiderate?",
        "english": "Certainly. What would you like to drink?",
        "choices": [
          {"text": "Una bottiglietta d'acqua naturale, per favore.", "english": "A small bottle of still water, please.", "isCorrect": True},
          {"text": "Una chiave magnetica per la stanza, per favore.", "english": "A key card for the room, please.", "isCorrect": False},
          {"text": "Una coperta di lana pesante, per favore.", "english": "A heavy wool blanket, please.", "isCorrect": False}
        ]
      },
      {
        "id": "msg5",
        "role": "host",
        "text": "Avete bisogno di posate per mangiare?",
        "english": "Do you need cutlery to eat?",
        "choices": [
          {"text": "Sì, ci servono due forchette e un coltello.", "english": "Yes, we need two forks and a knife.", "isCorrect": True},
          {"text": "Sì, ci servono due biglietti per il museo.", "english": "Yes, we need two tickets for the museum.", "isCorrect": False},
          {"text": "Sì, ci servono due cuscini puliti.", "english": "Yes, we need two clean pillows.", "isCorrect": False}
        ]
      },
      {
        "id": "msg6",
        "role": "host",
        "text": "Eccole. Vi siedete ai tavolini qui fuori?",
        "english": "Here they are. Are you sitting at the tables outside?",
        "choices": [
          {"text": "Sì, fa una bella giornata. Mangiamo fuori.", "english": "Yes, it's a beautiful day. We'll eat outside.", "isCorrect": True},
          {"text": "Sì, fa una bella doccia. Mangiamo fuori.", "english": "Yes, it's a nice shower. We'll eat outside.", "isCorrect": False},
          {"text": "Sì, fa un bel divano. Mangiamo fuori.", "english": "Yes, it's a nice sofa. We'll eat outside.", "isCorrect": False}
        ]
      },
      {
        "id": "msg7",
        "role": "host",
        "text": "D'accordo. Vi scaldo un po' di pane anche?",
        "english": "Alright. Shall I warm some bread for you too?",
        "choices": [
          {"text": "Ottima idea, il pane caldo è sempre buono.", "english": "Great idea, warm bread is always good.", "isCorrect": True},
          {"text": "Ottima idea, il libro caldo è sempre buono.", "english": "Great idea, a warm book is always good.", "isCorrect": False},
          {"text": "Ottima idea, il cappello caldo è sempre buono.", "english": "Great idea, a warm hat is always good.", "isCorrect": False}
        ]
      },
      {
        "id": "msg8",
        "role": "host",
        "text": "Ecco a voi il vassoio. Buon pranzo!",
        "english": "Here is the tray for you. Enjoy your lunch!",
        "choices": [
          {"text": "Grazie, sembra tutto molto appetitoso.", "english": "Thank you, everything looks very appetizing.", "isCorrect": True},
          {"text": "Grazie, sembra tutto molto noioso.", "english": "Thank you, everything looks very boring.", "isCorrect": False},
          {"text": "Grazie, sembra tutto molto veloce.", "english": "Thank you, everything looks very fast.", "isCorrect": False}
        ]
      },
      {
        "id": "msg9",
        "role": "host",
        "text": "In totale sono dodici euro. Paga in contanti o con carta?",
        "english": "In total it is twelve euros. Are you paying cash or by card?",
        "choices": [
          {"text": "Pago in contanti. Ecco venti euro, grazie.", "english": "I'll pay in cash. Here is twenty euros, thank you.", "isCorrect": True},
          {"text": "Pago in farmacia. Ecco la ricetta medica, grazie.", "english": "I'll pay at the pharmacy. Here is the prescription, thank you.", "isCorrect": False},
          {"text": "Pago in ospedale. Ecco il passaporto, grazie.", "english": "I'll pay at the hospital. Here is the passport, thank you.", "isCorrect": False}
        ]
      },
      {
        "id": "msg10",
        "role": "host",
        "text": "Ecco a lei il resto di otto euro. Buona permanenza!",
        "english": "Here is your change of eight euros. Have a good stay!",
        "choices": [
          {"text": "Grazie mille e arrivederci!", "english": "Thank you very much and goodbye!", "isCorrect": True},
          {"text": "Grazie mille e buongiorno!", "english": "Thank you very much and good morning!", "isCorrect": False},
          {"text": "Grazie mille e buonasera!", "english": "Thank you very much and good evening!", "isCorrect": False}
        ]
      }
    ]
  }
]

with open("src/data/exports/dining/market_lunch/conversations.json", "w", encoding="utf-8") as f:
    json.dump({"conversations": conversations}, f, indent=2, ensure_ascii=False)
