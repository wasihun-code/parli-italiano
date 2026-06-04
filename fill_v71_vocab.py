import json
import os

path = "src/data/exports/social/introducing_yourself/social_introducing_yourself_vocabulary.json"

with open(path, "r", encoding="utf-8") as f:
    vocab = json.load(f)

translations = {
    "agli": "to the (plural)",
    "alcuni": "some",
    "amici": "friends",
    "anni": "years",
    "arrivederci": "goodbye",
    "azienda": "company",
    "band": "band",
    "bellissima": "very beautiful",
    "calorosa": "warm",
    "capisco": "I understand",
    "capito": "understood",
    "casa": "house / home",
    "cinema": "cinema",
    "cinque": "five",
    "circa": "about",
    "complimenti": "congratulations",
    "compositore": "composer",
    "concordo": "I agree",
    "creativo": "creative",
    "dinamica": "dynamic",
    "divertimento": "fun / amusement",
    "divertiti": "have fun",
    "festa": "party / feast",
    "già": "already",
    "grande": "big",
    "hai": "you have",
    "immagino": "I imagine",
    "imparare": "to learn",
    "incredibile": "incredible",
    "leggi": "you read",
    "leggo": "I read",
    "magica": "magical",
    "mai": "never",
    "manca": "miss / lack",
    "mese": "month",
    "museo": "museum",
    "non": "not",
    "oggi": "today",
    "ogni": "every",
    "ottima": "excellent / great (feminine)",
    "piacciono": "they please (I like)",
    "preferito": "favorite (masculine)",
    "purtroppo": "unfortunately",
    "qualche": "some",
    "quanto": "how much",
    "questa": "this (feminine)",
    "recente": "recent",
    "romanzi": "novels",
    "scelta": "choice",
    "scorso": "last / past"
}

for item in vocab:
    if not item.get("english") and item["italian"] in translations:
        item["english"] = translations[item["italian"]]

with open(path, "w", encoding="utf-8") as f:
    json.dump(vocab, f, indent=2, ensure_ascii=False)

print("Filled missing translations in vocabulary.")
