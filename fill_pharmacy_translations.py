import json

translations = {
    "controllare": "to check",
    "credito": "credit",
    "dare": "to give",
    "darò": "I will give",
    "della": "of the (feminine)",
    "delle": "of the (plural)",
    "dentro": "inside",
    "difficile": "difficult",
    "difficoltà": "difficulty",
    "domani": "tomorrow",
    "domenica": "Sunday",
    "dosaggio": "dosage",
    "essere": "to be",
    "farlo": "to do it",
    "farmaci": "drugs / medications",
    "farmacia": "pharmacy",
    "farò": "I will do",
    "giornata": "day (duration)",
    "giorni": "days",
    "gli": "the (masculine plural)",
    "grandi": "large / big (plural)",
    "grattarsi": "to scratch oneself",
    "importante": "important",
    "lasciarla": "to leave it (feminine)",
    "lei": "she / you (formal)",
    "mal": "pain / ache",
    "mio": "my",
    "molta": "a lot of / much (feminine)",
    "molti": "many",
    "nel": "in the",
    "noi": "we",
    "nulla": "nothing",
    "ottima": "excellent (feminine)",
    "otto": "eight",
    "pago": "I pay",
    "piccole": "small (plural feminine)",
    "preferisco": "I prefer",
    "prende": "takes / you take (formal)",
    "prendo": "I take",
    "presa": "taken / after taking (feminine)",
    "problema": "problem",
    "prurito": "itching / itch",
    "quanto": "how much",
    "questi": "these (masculine plural)",
    "riguardi": "take care (formal imperative)",
    "sabato": "Saturday",
    "sappia": "know (subjunctive)",
    "scontrino": "receipt",
    "scritto": "written",
    "senta": "feel (formal imperative / subjunctive)",
    "sente": "feels / you feel (formal)",
    "senz": "without (shortened)",
    "sia": "is (subjunctive) / be",
    "siamo": "we are",
    "siete": "you are (plural)",
    "speriamo": "we hope",
    "spero": "I hope"
}

file_path = 'src/data/exports/health/pharmacy_symptoms/health_pharmacy_symptoms_vocabulary.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

updated_count = 0
for item in data:
    if item['english'] == "" and item['italian'] in translations:
        item['english'] = translations[item['italian']]
        updated_count += 1

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated {updated_count} translations.")
