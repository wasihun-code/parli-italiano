import json
import os

scenario_id = "market_lunch"  # Note: The JSON uses string ID for scenarios in recent updates, I'll put "market_lunch". Or let's just omit scenarioId or use 40.

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
          {
            "text": "Buongiorno! Quali sono i vostri prodotti tipici?",
            "english": "Good morning! What are your typical products?",
            "isCorrect": True
          },
          {
            "text": "Buongiorno! Voglio comprare un biglietto del treno.",
            "english": "Good morning! I want to buy a train ticket.",
            "isCorrect": False
          },
          {
            "text": "Buongiorno! Dov'è la stazione degli autobus?",
            "english": "Good morning! Where is the bus station?",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg2",
        "role": "host",
        "text": "Abbiamo formaggi freschi, salumi e pane fatto in casa.",
        "english": "We have fresh cheeses, cured meats, and homemade bread.",
        "choices": [
          {
            "text": "Ottimo, vorrei vedere i formaggi freschi.",
            "english": "Great, I would like to see the fresh cheeses.",
            "isCorrect": True
          },
          {
            "text": "Ottimo, vorrei vedere i vostri vestiti.",
            "english": "Great, I would like to see your clothes.",
            "isCorrect": False
          },
          {
            "text": "Ottimo, vorrei affittare una macchina.",
            "english": "Great, I would like to rent a car.",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg3",
        "role": "host",
        "text": "Questo formaggio è fatto con latte locale, è molto saporito.",
        "english": "This cheese is made with local milk, it is very tasty.",
        "choices": [
          {
            "text": "Sembra delizioso. Ne prendo un pezzo, grazie.",
            "english": "It looks delicious. I'll take a piece, thank you.",
            "isCorrect": True
          },
          {
            "text": "Sembra costoso. Non mi piace la carne.",
            "english": "It looks expensive. I don't like meat.",
            "isCorrect": False
          },
          {
            "text": "Sembra sporco. Posso avere un tovagliolo?",
            "english": "It looks dirty. Can I have a napkin?",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg4",
        "role": "host",
        "text": "Certo. Vuole anche dei salumi per accompagnarlo?",
        "english": "Of course. Do you also want some cured meats to accompany it?",
        "choices": [
          {
            "text": "Sì, mi consiglia un buon salame locale?",
            "english": "Yes, can you recommend a good local salami?",
            "isCorrect": True
          },
          {
            "text": "Sì, mi consiglia un buon albergo qui vicino?",
            "english": "Yes, can you recommend a good hotel nearby?",
            "isCorrect": False
          },
          {
            "text": "Sì, mi consiglia un dottore per favore?",
            "english": "Yes, can you recommend a doctor please?",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg5",
        "role": "host",
        "text": "Questo salame con il pepe nero è molto popolare. Ne taglio un po'?",
        "english": "This salami with black pepper is very popular. Shall I cut some?",
        "choices": [
          {
            "text": "Perfetto, mi tagli due etti per favore.",
            "english": "Perfect, slice two hundred grams for me, please.",
            "isCorrect": True
          },
          {
            "text": "Perfetto, mi tagli due metri per favore.",
            "english": "Perfect, slice two meters for me, please.",
            "isCorrect": False
          },
          {
            "text": "Perfetto, mi porti due bottiglie per favore.",
            "english": "Perfect, bring me two bottles, please.",
            "isCorrect": False
          }
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
          {
            "text": "Tocca a me. Vorrei comprare del prosciutto.",
            "english": "It's my turn. I would like to buy some ham.",
            "isCorrect": True
          },
          {
            "text": "Tocca a me. Vorrei comprare un biglietto.",
            "english": "It's my turn. I would like to buy a ticket.",
            "isCorrect": False
          },
          {
            "text": "Tocca a me. Dov'è la fermata del tram?",
            "english": "It's my turn. Where is the tram stop?",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg2",
        "role": "host",
        "text": "Prosciutto crudo o prosciutto cotto oggi?",
        "english": "Cured ham or cooked ham today?",
        "choices": [
          {
            "text": "Prosciutto crudo, per favore. Quello dolce.",
            "english": "Cured ham, please. The sweet one.",
            "isCorrect": True
          },
          {
            "text": "Prosciutto crudo, per favore. Quello stanco.",
            "english": "Cured ham, please. The tired one.",
            "isCorrect": False
          },
          {
            "text": "Prosciutto crudo, per favore. Quello giallo.",
            "english": "Cured ham, please. The yellow one.",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg3",
        "role": "host",
        "text": "Eccolo, è freschissimo. Quanto ne vuole?",
        "english": "Here it is, it's very fresh. How much do you want?",
        "choices": [
          {
            "text": "Ne vorrei circa due etti e mezzo, grazie.",
            "english": "I would like about two hundred and fifty grams, thanks.",
            "isCorrect": True
          },
          {
            "text": "Ne vorrei circa due litri e mezzo, grazie.",
            "english": "I would like about two and a half liters, thanks.",
            "isCorrect": False
          },
          {
            "text": "Ne vorrei circa due chilometri, grazie.",
            "english": "I would like about two kilometers, thanks.",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg4",
        "role": "host",
        "text": "Sono tre etti, lascio o tolgo una fetta?",
        "english": "It's three hundred grams, should I leave it or take a slice off?",
        "choices": [
          {
            "text": "Lascio pure, non c'è problema.",
            "english": "Leave it, no problem.",
            "isCorrect": True
          },
          {
            "text": "Lascio pure, non c'è nessun treno.",
            "english": "Leave it, there is no train.",
            "isCorrect": False
          },
          {
            "text": "Lascio pure, non c'è molta luce.",
            "english": "Leave it, there is not much light.",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg5",
        "role": "host",
        "text": "Perfetto. Desidera anche del formaggio con il prosciutto?",
        "english": "Perfect. Do you also want some cheese with the ham?",
        "choices": [
          {
            "text": "Sì, mezzo chilo di formaggio stagionato, per favore.",
            "english": "Yes, half a kilo of aged cheese, please.",
            "isCorrect": True
          },
          {
            "text": "Sì, mezza bottiglia di vino rosso, per favore.",
            "english": "Yes, half a bottle of red wine, please.",
            "isCorrect": False
          },
          {
            "text": "Sì, mezzo litro d'acqua gassata, per favore.",
            "english": "Yes, half a liter of sparkling water, please.",
            "isCorrect": False
          }
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
          {
            "text": "Buongiorno. Posso assaggiare prima di comprare?",
            "english": "Good morning. Can I taste before buying?",
            "isCorrect": True
          },
          {
            "text": "Buongiorno. Posso dormire prima di mangiare?",
            "english": "Good morning. Can I sleep before eating?",
            "isCorrect": False
          },
          {
            "text": "Buongiorno. Posso guidare prima di comprare?",
            "english": "Good morning. Can I drive before buying?",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg2",
        "role": "host",
        "text": "Ma certo! Provi questa oliva verde, è molto dolce.",
        "english": "But of course! Try this green olive, it's very sweet.",
        "choices": [
          {
            "text": "Mmm, è davvero squisita. Mi piace molto.",
            "english": "Mmm, it is really exquisite. I like it a lot.",
            "isCorrect": True
          },
          {
            "text": "Mmm, è davvero difficile. Mi piace leggere.",
            "english": "Mmm, it is really difficult. I like to read.",
            "isCorrect": False
          },
          {
            "text": "Mmm, è davvero lontana. Mi piace camminare.",
            "english": "Mmm, it is really far. I like to walk.",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg3",
        "role": "host",
        "text": "Bene. Quante ne prepariamo per oggi?",
        "english": "Good. How many shall we prepare for today?",
        "choices": [
          {
            "text": "Ne prendo un chilo intero, per favore.",
            "english": "I'll take a whole kilo, please.",
            "isCorrect": True
          },
          {
            "text": "Ne prendo un anno intero, per favore.",
            "english": "I'll take a whole year, please.",
            "isCorrect": False
          },
          {
            "text": "Ne prendo un libro intero, per favore.",
            "english": "I'll take a whole book, please.",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg4",
        "role": "host",
        "text": "Ottima scelta. Vuole assaggiare anche le olive nere al forno?",
        "english": "Excellent choice. Do you also want to taste the baked black olives?",
        "choices": [
          {
            "text": "Perché no? Sono molto curioso di provarle.",
            "english": "Why not? I am very curious to try them.",
            "isCorrect": True
          },
          {
            "text": "Perché no? Sono molto arrabbiato di provarle.",
            "english": "Why not? I am very angry to try them.",
            "isCorrect": False
          },
          {
            "text": "Perché no? Sono molto stanco di provarle.",
            "english": "Why not? I am very tired to try them.",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg5",
        "role": "host",
        "text": "Ecco a lei. Attenzione che hanno ancora il nocciolo.",
        "english": "Here you go. Careful that they still have the pit.",
        "choices": [
          {
            "text": "Sono buonissime, ma preferisco solo quelle verdi oggi.",
            "english": "They are delicious, but I prefer only the green ones today.",
            "isCorrect": True
          },
          {
            "text": "Sono bellissime, ma preferisco solo la gonna blu oggi.",
            "english": "They are beautiful, but I prefer only the blue skirt today.",
            "isCorrect": False
          },
          {
            "text": "Sono lunghissime, ma preferisco solo la macchina nera oggi.",
            "english": "They are very long, but I prefer only the black car today.",
            "isCorrect": False
          }
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
          {
            "text": "Salve, vorrei una porzione di lasagne da mangiare qui.",
            "english": "Hello, I would like a portion of lasagna to eat here.",
            "isCorrect": True
          },
          {
            "text": "Salve, vorrei una camera singola per una notte.",
            "english": "Hello, I would like a single room for one night.",
            "isCorrect": False
          },
          {
            "text": "Salve, vorrei un volo per Roma domattina.",
            "english": "Hello, I would like a flight to Rome tomorrow morning.",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg2",
        "role": "host",
        "text": "Le lasagne sono appena uscite dal forno. C'è altro?",
        "english": "The lasagna just came out of the oven. Is there anything else?",
        "choices": [
          {
            "text": "Sì, vorrei anche una porzione di verdure grigliate.",
            "english": "Yes, I would also like a portion of grilled vegetables.",
            "isCorrect": True
          },
          {
            "text": "Sì, vorrei anche un paio di scarpe nuove.",
            "english": "Yes, I would also like a new pair of shoes.",
            "isCorrect": False
          },
          {
            "text": "Sì, vorrei anche una medicina per il mal di testa.",
            "english": "Yes, I would also like a medicine for headache.",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg3",
        "role": "host",
        "text": "Zucchine o melanzane grigliate?",
        "english": "Grilled zucchini or eggplant?",
        "choices": [
          {
            "text": "Facciamo un po' e un po', se è possibile.",
            "english": "Let's do half and half, if it's possible.",
            "isCorrect": True
          },
          {
            "text": "Facciamo una borsa grande, se è possibile.",
            "english": "Let's do a large bag, if it's possible.",
            "isCorrect": False
          },
          {
            "text": "Facciamo un cappotto caldo, se è possibile.",
            "english": "Let's do a warm coat, if it's possible.",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg4",
        "role": "host",
        "text": "Certamente. Da bere cosa desiderate?",
        "english": "Certainly. What would you like to drink?",
        "choices": [
          {
            "text": "Una bottiglietta d'acqua naturale, per favore.",
            "english": "A small bottle of still water, please.",
            "isCorrect": True
          },
          {
            "text": "Una chiave magnetica per la stanza, per favore.",
            "english": "A key card for the room, please.",
            "isCorrect": False
          },
          {
            "text": "Una coperta di lana pesante, per favore.",
            "english": "A heavy wool blanket, please.",
            "isCorrect": False
          }
        ]
      },
      {
        "id": "msg5",
        "role": "host",
        "text": "In totale sono dodici euro. Paga in contanti o con carta?",
        "english": "In total it is twelve euros. Are you paying cash or by card?",
        "choices": [
          {
            "text": "Pago in contanti. Ecco venti euro, grazie.",
            "english": "I'll pay in cash. Here is twenty euros, thank you.",
            "isCorrect": True
          },
          {
            "text": "Pago in farmacia. Ecco la ricetta medica, grazie.",
            "english": "I'll pay at the pharmacy. Here is the prescription, thank you.",
            "isCorrect": False
          },
          {
            "text": "Pago in ospedale. Ecco il passaporto, grazie.",
            "english": "I'll pay at the hospital. Here is the passport, thank you.",
            "isCorrect": False
          }
        ]
      }
    ]
  }
]

with open("src/data/exports/dining/market_lunch/conversations.json", "w", encoding="utf-8") as f:
    json.dump({"conversations": conversations}, f, indent=2, ensure_ascii=False)
