import json
import os

def fix_translations(scenario_slug):
    base_path = f"src/data/exports/{scenario_slug}"
    parts = scenario_slug.split('/')
    prefix = "_".join(parts)
    
    mapping = {
        "all": "at the",
        "alle": "at the",
        "altra": "another",
        "altri": "others",
        "altro": "other",
        "andare": "to go",
        "apertura": "opening",
        "area": "area",
        "assolutamente": "absolutely",
        "attento": "careful",
        "bagni": "bathrooms",
        "belli": "beautiful",
        "capito": "understood",
        "chiama": "is called",
        "chiamano": "are called",
        "città": "city",
        "colorati": "colorful",
        "come": "how",
        "costano": "they cost",
        "costino": "they cost",
        "credo": "I believe",
        "delle": "of the",
        "domani": "tomorrow",
        "due": "two",
        "esattamente": "exactly",
        "esatto": "exact",
        "fai": "you do",
        "fumare": "to smoke",
        "fumatori": "smokers",
        "fumo": "smoke",
        "fuori": "outside",
        "giovani": "young",
        "giro": "tour",
        "goditi": "enjoy",
        "idea": "idea",
        "indimenticabile": "unforgettable",
        "informazione": "information",
        "informazioni": "information",
        "interno": "inside",
        "locale": "venue",
        "magliette": "t-shirts",
        "mangiare": "to eat",
        "mappa": "map",
        "mezza": "half",
        "nelle": "in the",
        "nove": "nine",
        "nuovo": "new",
        "orientarsi": "to orient oneself",
        "ottima": "excellent",
        "pacchetto": "packet",
        "patatine": "chips",
        "peccato": "pity",
        "più": "more",
        "poster": "poster",
        "prendo": "I take",
        "prezzo": "price",
        "prima": "before",
        "pronto": "ready",
        "proprio": "really",
        "qualcosa": "something",
        "resto": "I stay",
        "ricordare": "to remember",
        "sapere": "to know",
        "sapevo": "I knew",
        "serve": "is needed",
        "sinistra": "left",
        "sono": "I am",
        "spero": "I hope",
        "sposto": "I move",
        "sufficiente": "sufficient",
        "suona": "plays",
        "suonano": "they play",
        "svuota": "empty",
        "tardi": "late",
        "tasche": "pockets",
        "tempo": "time",
        "top": "top",
        "tour": "tour",
        "tovagliolo": "napkin",
        "trenta": "thirty",
        "trovano": "are located",
        "uno": "one",
        "uscita": "exit",
        "utile": "useful",
        "vendono": "they sell",
        "verso": "toward",
        "vietato": "forbidden",
        "visti": "seen",
        "visto": "seen"
    }

    for fname in [f"{prefix}_vocabulary.json", f"{prefix}_phrases.json", f"{prefix}_sentences.json"]:
        p = os.path.join(base_path, fname)
        if not os.path.exists(p): continue
        
        with open(p, "r", encoding="utf-8") as f:
            items = json.load(f)
            
        changed = False
        for item in items:
            if not item.get("english"):
                val = item.get("italian", "").lower()
                if val in mapping:
                    item["english"] = mapping[val]
                    changed = True
                else:
                    # Fallback for phrases/sentences if they are in conversations.json
                    # (Linguistic extractor should have handled this, but just in case)
                    pass
        
        if changed:
            with open(p, "w", encoding="utf-8") as f:
                json.dump(items, f, indent=2, ensure_ascii=False)
            print(f"Updated {fname}")

if __name__ == "__main__":
    fix_translations("culture/live_music")
