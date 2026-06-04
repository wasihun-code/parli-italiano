import json

conversations = {
  "scenarioId": 78,
  "conversations": [
    {
      "id": "new_outfit",
      "title": "Complimenting a New Outfit",
      "description": "Give a compliment about a friend's new clothes.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Ciao! Come stai oggi? Sei pronto per uscire?",
          "english": "Hi! How are you today? Are you ready to go out?",
          "choices": [
            {
              "text": "Ciao! Sto bene, grazie. Che bella giacca che indossi oggi!",
              "isCorrect": true,
              "feedback": "Great start by complimenting the jacket."
            },
            {
              "text": "Ciao! Sto bene, grazie. Che bella finestra che abbiamo oggi!",
              "isCorrect": false,
              "feedback": "You are talking about a window, not an outfit."
            },
            {
              "text": "Ciao! Sto bene, grazie. Che bella porta che chiudiamo oggi!",
              "isCorrect": false,
              "feedback": "Focus on the person's appearance, not the door."
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Grazie mille! L'ho comprata proprio ieri in centro.",
          "english": "Thank you very much! I bought it just yesterday downtown.",
          "choices": [
            {
              "text": "Hai fatto un ottimo acquisto. Il colore ti sta benissimo.",
              "isCorrect": true,
              "feedback": "Nice specific compliment about the color."
            },
            {
              "text": "Hai fatto un ottimo sbaglio. Il lavoro ti sta malissimo.",
              "isCorrect": false,
              "feedback": "You should compliment, not criticize."
            },
            {
              "text": "Hai fatto un ottimo pasto. Il tavolo ti sta benissimo.",
              "isCorrect": false,
              "feedback": "You are talking about a jacket, not a meal."
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Davvero? Ero un po' indeciso tra questo blu e il nero.",
          "english": "Really? I was a bit undecided between this blue and black.",
          "choices": [
            {
              "text": "Il blu è perfetto. È molto elegante e davvero originale.",
              "isCorrect": true,
              "feedback": "Confirming their choice with positive adjectives."
            },
            {
              "text": "Il muro è perfetto. È molto elegante e davvero originale.",
              "isCorrect": false,
              "feedback": "You are talking about the jacket color, not a wall."
            },
            {
              "text": "Il tetto è perfetto. È molto divertente e davvero stupendo.",
              "isCorrect": false,
              "feedback": "You are talking about a color, not a roof."
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Sei molto gentile. Anche le tue scarpe nuove sono belle.",
          "english": "You are very kind. Your new shoes are beautiful too.",
          "choices": [
            {
              "text": "Grazie! Anche a me piacciono molto. Sono comodissime.",
              "isCorrect": true,
              "feedback": "Accepting the compliment and adding a detail."
            },
            {
              "text": "Grazie! Anche a me mancano molto. Sono velocissime.",
              "isCorrect": false,
              "feedback": "You already have the shoes, they are not missing."
            },
            {
              "text": "Grazie! Anche a me scrivono molto. Sono simpatiche.",
              "isCorrect": false,
              "feedback": "Shoes do not write or have a personality."
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Sembrano perfette per camminare a lungo. Dove le hai prese?",
          "english": "They look perfect for walking a long time. Where did you get them?",
          "choices": [
            {
              "text": "Le ho trovate in un piccolo negozio qui vicino a casa.",
              "isCorrect": true,
              "feedback": "Answering the question naturally."
            },
            {
              "text": "Le ho trovate in un grande piatto qui vicino a casa.",
              "isCorrect": false,
              "feedback": "You find shoes in a store, not in a plate."
            },
            {
              "text": "Le ho trovate in un piccolo tavolo qui vicino a casa.",
              "isCorrect": false,
              "feedback": "You buy shoes in a store, not a table."
            }
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Ottimo affare. Hai sempre molto gusto nel vestire.",
          "english": "Great deal. You always have a lot of taste in dressing.",
          "choices": [
            {
              "text": "Ti ringrazio, è un bel complimento. Cerco sempre di fare attenzione.",
              "isCorrect": true,
              "feedback": "Graciously accepting the compliment about style."
            },
            {
              "text": "Ti ringrazio, è un bel problema. Cerco sempre di fare attenzione.",
              "isCorrect": false,
              "feedback": "A compliment is not a problem."
            },
            {
              "text": "Ti ringrazio, è un bel giardino. Cerco sempre di fare attenzione.",
              "isCorrect": false,
              "feedback": "You are talking about a compliment, not a garden."
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Si vede! Ogni dettaglio è curato, anche la camicia.",
          "english": "It shows! Every detail is neat, even the shirt.",
          "choices": [
            {
              "text": "Grazie ancora! Questa camicia è un regalo di mia sorella.",
              "isCorrect": true,
              "feedback": "Providing more context about the complimented item."
            },
            {
              "text": "Grazie ancora! Questa pioggia è un regalo di mia sorella.",
              "isCorrect": false,
              "feedback": "You are talking about a shirt, not the rain."
            },
            {
              "text": "Grazie ancora! Questa strada è un regalo di mia sorella.",
              "isCorrect": false,
              "feedback": "You are talking about clothes, not a street."
            }
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Tua sorella ha ottimo gusto. Il regalo perfetto per te.",
          "english": "Your sister has excellent taste. The perfect gift for you.",
          "choices": [
            {
              "text": "Sì, mi conosce molto bene. Sa sempre cosa mi piace.",
              "isCorrect": true,
              "feedback": "Agreeing and expanding on the relationship."
            },
            {
              "text": "Sì, mi dimentica molto bene. Sa sempre cosa mi piace.",
              "isCorrect": false,
              "feedback": "If she knows what you like, she doesn't forget you."
            },
            {
              "text": "Sì, mi saluta molto bene. Sa sempre cosa mi piace.",
              "isCorrect": false,
              "feedback": "Greeting is not relevant to choosing a gift."
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Beh, siamo pronti. Andiamo a fare questa passeggiata?",
          "english": "Well, we are ready. Shall we go take this walk?",
          "choices": [
            {
              "text": "Certamente, andiamo! Sono sicuro che ci divertiremo molto.",
              "isCorrect": true,
              "feedback": "Agreeing to start the activity."
            },
            {
              "text": "Certamente, dormiamo! Sono sicuro che ci divertiremo molto.",
              "isCorrect": false,
              "feedback": "You are going for a walk, not sleeping."
            },
            {
              "text": "Certamente, lavoriamo! Sono sicuro che ci divertiremo molto.",
              "isCorrect": false,
              "feedback": "The host suggested a walk, not working."
            }
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Sì, è una giornata stupenda. Sarà un bel pomeriggio.",
          "english": "Yes, it's a wonderful day. It will be a nice afternoon.",
          "choices": [
            {
              "text": "Hai ragione. La tua giacca blu è perfetta per oggi.",
              "isCorrect": true,
              "feedback": "A nice wrap-up referring back to the initial compliment."
            },
            {
              "text": "Hai torto. La tua giacca blu è terribile per oggi.",
              "isCorrect": false,
              "feedback": "You shouldn't suddenly be rude!"
            },
            {
              "text": "Hai freddo. La tua giacca blu è bagnata per oggi.",
              "isCorrect": false,
              "feedback": "You are going for a walk, the jacket is fine."
            }
          ]
        }
      ]
    }
  ]
}

with open("src/data/exports/social/compliments/conversations_1.json", "w") as f:
    json.dump(conversations, f, indent=2, ensure_ascii=False)
