import json

file_path = 'src/data/exports/miscellaneous/time_and_dates/miscellaneous_time_and_dates_vocabulary.json'

with open(file_path, 'r') as f:
    vocab = json.load(f)

translations = {
    "aiuto": "help",
    "angolo": "corner",
    "appuntamento": "appointment",
    "avete": "you have (plural)",
    "biglietto": "ticket",
    "buono": "good / delicious",
    "cento": "hundred",
    "centro": "center / downtown",
    "chiudiamo": "we close",
    "cinque": "five",
    "conosco": "I know",
    "costa": "it costs",
    "così": "so / like this",
    "dei": "of the",
    "delle": "of the",
    "destra": "right (direction)",
    "deve": "he-she must",
    "dietro": "behind",
    "documenti": "documents",
    "dodici": "twelve",
    "dopo": "after",
    "dov": "where",
    "dove": "where",
    "dritto": "straight",
    "euro": "euro",
    "farò": "I will do",
    "fortuna": "luck",
    "fretta": "hurry",
    "gente": "people",
    "giorni": "days",
    "giri": "you turn (formal)",
    "guidata": "guided",
    "guidate": "guided",
    "incontrarsi": "to meet each other",
    "invece": "instead",
    "italiana": "Italian",
    "mangiamo": "we eat",
    "meglio": "better",
    "meno": "less",
    "metri": "meters",
    "minuti": "minutes",
    "mio": "my",
    "nel": "in the",
    "non": "not",
    "nuova": "new",
    "orario": "schedule",
    "ottima": "excellent",
    "parte": "leaves / part",
    "però": "however",
    "piace": "he-she-it pleases / like",
    "piazza": "square",
    "più": "more",
    "porto": "I bring / port",
    "preferisce": "he-she prefers",
    "prima": "before / first",
    "proprio": "exactly / really",
    "puntuale": "on time",
    "può": "he-she-it can",
    "qualcosa": "something",
    "questa": "this",
    "quindici": "fifteen",
    "ricordi": "remember",
    "sei": "six",
    "settimanale": "weekly",
    "solo": "only",
    "spesso": "often",
    "spiegare": "to explain",
    "stazione": "station",
    "stesso": "same",
    "strada": "road",
    "suo": "his / her / your (formal)",
    "treni": "trains",
    "tutti": "everyone / all",
    "ufficio": "office",
    "vada": "go (formal)",
    "vedere": "to see",
    "venti": "twenty",
    "visite": "visits",
    "vuoi": "you want"
}

updated_count = 0
for item in vocab:
    if item['english'] == "" and item['italian'] in translations:
        item['english'] = translations[item['italian']]
        updated_count += 1

with open(file_path, 'w') as f:
    json.dump(vocab, f, indent=2, ensure_ascii=False)

print(f"Updated {updated_count} vocabulary items.")
