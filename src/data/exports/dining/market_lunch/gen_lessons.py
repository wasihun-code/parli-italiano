import json
import os

lessons = [
  {
    "id": "at_the_market",
    "title": "At the Market",
    "description": "Learn to ask for typical products at the local market.",
    "objectives": [
      "Understand host greetings",
      "Ask for typical products"
    ],
    "exercises": [
      {
        "type": "vocabulary",
        "word": "mercato"
      },
      {
        "type": "vocabulary",
        "word": "tipico"
      },
      {
        "type": "phrase",
        "phrase": "Quali sono i vostri prodotti tipici?"
      }
    ]
  },
  {
    "id": "weights_measures",
    "title": "Weights & Measures",
    "description": "Learn to specify quantities like etto and chilo.",
    "objectives": [
      "Specify weights in grams",
      "Specify weights in kilos"
    ],
    "exercises": [
      {
        "type": "vocabulary",
        "word": "etto"
      },
      {
        "type": "vocabulary",
        "word": "chilo"
      },
      {
        "type": "phrase",
        "phrase": "Ne vorrei circa due etti e mezzo, grazie."
      },
      {
        "type": "phrase",
        "phrase": "Mezzo chilo di formaggio stagionato, per favore."
      }
    ]
  },
  {
    "id": "tasting",
    "title": "Tasting",
    "description": "Learn to ask for a sample before buying.",
    "objectives": [
      "Ask to taste",
      "Give feedback on a sample"
    ],
    "exercises": [
      {
        "type": "vocabulary",
        "word": "assaggiare"
      },
      {
        "type": "phrase",
        "phrase": "Posso assaggiare prima di comprare?"
      },
      {
        "type": "phrase",
        "phrase": "È davvero squisita. Mi piace molto."
      }
    ]
  },
  {
    "id": "local_foods",
    "title": "Local Foods",
    "description": "Learn vocabulary for local cheeses and cured meats.",
    "objectives": [
      "Identify local foods",
      "Ask for a recommendation"
    ],
    "exercises": [
      {
        "type": "vocabulary",
        "word": "formaggio"
      },
      {
        "type": "vocabulary",
        "word": "salumi"
      },
      {
        "type": "vocabulary",
        "word": "fresco"
      },
      {
        "type": "phrase",
        "phrase": "Mi consiglia un buon salame locale?"
      }
    ]
  },
  {
    "id": "ordering_lunch",
    "title": "Ordering Lunch",
    "description": "Order a quick portion of food at the market deli.",
    "objectives": [
      "Order a portion of food",
      "Ask for drinks"
    ],
    "exercises": [
      {
        "type": "vocabulary",
        "word": "porzione"
      },
      {
        "type": "phrase",
        "phrase": "Vorrei una porzione di lasagne da mangiare qui."
      },
      {
        "type": "phrase",
        "phrase": "Una bottiglietta d'acqua naturale, per favore."
      }
    ]
  },
  {
    "id": "final_payment",
    "title": "Final Payment",
    "description": "Learn to pay in cash for your market purchases.",
    "objectives": [
      "Understand total cost",
      "Pay with cash"
    ],
    "exercises": [
      {
        "type": "phrase",
        "phrase": "Pago in contanti. Ecco venti euro, grazie."
      }
    ]
  }
]

with open("src/data/exports/dining/market_lunch/mini_lessons.json", "w", encoding="utf-8") as f:
    json.dump({"lessons": lessons}, f, indent=2, ensure_ascii=False)
