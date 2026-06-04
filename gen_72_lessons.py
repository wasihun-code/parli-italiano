import json
import os

scenario_dir = "src/data/exports/social/making_plans"

lessons = {
  "scenarioId": 72,
  "lessons": [
    {
      "id": "lesson_1",
      "title": "Suggesting an Activity",
      "focus": "phrases",
      "content": [
        "Hai programmi per questa sera?",
        "Pensavo di andare al cinema.",
        "Ti va?",
        "Oggi c'è il sole. Usciamo?"
      ]
    },
    {
      "id": "lesson_2",
      "title": "Responding to Ideas",
      "focus": "phrases",
      "content": [
        "No, non ho programmi. Tu?",
        "Che bella idea!",
        "È una bella idea.",
        "Sì, volentieri!"
      ]
    },
    {
      "id": "lesson_3",
      "title": "Agreeing on a Time",
      "focus": "phrases",
      "content": [
        "A che ora ci vediamo allora?",
        "Facciamo alle diciannove e mezza?",
        "Facciamo alle quindici?",
        "Va bene per te?"
      ]
    },
    {
      "id": "lesson_4",
      "title": "Agreeing on a Location",
      "focus": "phrases",
      "content": [
        "Dove andiamo?",
        "Conosco una pizzeria molto buona.",
        "Dove ci incontriamo di preciso?",
        "Ci vediamo davanti al cinema."
      ]
    },
    {
      "id": "lesson_5",
      "title": "Making the Arrangement",
      "focus": "phrases",
      "content": [
        "Devo prenotare?",
        "Prenoto subito per due persone.",
        "Porto anche una bottiglia d'acqua."
      ]
    },
    {
      "id": "lesson_6",
      "title": "Confirming the Details",
      "focus": "phrases",
      "content": [
        "Ti scrivo per confermare l'incontro.",
        "È tutto confermato.",
        "Ci vediamo alle diciotto, come d'accordo.",
        "Se faccio tardi ti scrivo un messaggio."
      ]
    }
  ]
}

os.makedirs(scenario_dir, exist_ok=True)
with open(os.path.join(scenario_dir, "mini_lessons.json"), "w", encoding="utf-8") as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Created mini_lessons.json")
