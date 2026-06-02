import json
import os

scenario_id = "s92"
dir_path = "src/data/exports/culture/local_history/"

paths = {
    "vocab": os.path.join(dir_path, "culture_local_history_vocabulary.json"),
    "phrases": os.path.join(dir_path, "culture_local_history_phrases.json"),
    "sentences": os.path.join(dir_path, "culture_local_history_sentences.json")
}

for key, path in paths.items():
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for item in data:
        if not item['id'].startswith(scenario_id + "-"):
            item['id'] = f"{scenario_id}-{item['id']}"
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

domain_data = {
  "allowed": [
    "museo", "storia", "città", "romana", "romano", "medioevo", "medievale", "archivio", "documenti", "palazzo", "famiglia", "nobile", "statua", "monumento", "tradizione", "leggenda", "campana", "chiesa", "targa", "iscrizione", "scrittore", "filosofo", "architetto", "ritratti", "galleria", "arte", "tessuti", "artigiani", "agricoltori", "teatro", "reperti", "origini", "fondazione", "secoli", "secolo", "epoca", "passato", "legame", "pace", "trattato", "cerimonia", "maggio", "ottocento", "settecento", "seicento", "dodicesimo", "quattordicesimo", "libertà", "diritti", "governo", "comune", "uffici", "botteghe", "scure", "pietre", "antico", "antica", "antiche", "affreschi", "battaglie", "incendio", "pericolo", "tempesta", "suonare", "svegliare", "spegnere", "fuoco", "sacra", "conoscitore", "curioso", "turisti", "guida", "buongiorno", "grazie", "prego", "volentieri", "certamente", "incredibile", "interessante", "affascinante", "vero", "immagino", "capisco", "vedete", "vediamo", "andiamo", "seguitemi", "entriamo", "aperto", "libero", "ingresso", "pubblico", "visitare", "imparare", "sapere", "vedere", "leggere", "parlare", "raccontare", "successo", "accaduto", "accadde", "risale", "fondata", "vissuto", "nato", "morto", "famoso", "importante", "significativo", "tipico", "moderno", "moderna", "attuale", "sì", "no", "chi", "cosa", "dove", "quando", "perché", "come"
  ],
  "forbidden": [
    "ristorante", "menu", "cameriere", "pizza", "pasta", "gelato", "caffè", "cornetto",
    "aeroporto", "volo", "bagaglio", "passaporto", "decollo",
    "medico", "ospedale", "medicina", "farmacia",
    "hotel", "prenotazione", "colazione", "reception",
    "treno", "binario", "biglietto", "ferrovia"
  ]
}

with open(os.path.join(dir_path, "domain.json"), 'w', encoding='utf-8') as f:
    json.dump(domain_data, f, ensure_ascii=False, indent=2)

