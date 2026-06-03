import json
import os

def fill():
    path = "src/data/exports/tech/wi_fi_problem"
    
    # Load extracted data
    files = ["tech_wi_fi_problem_vocabulary.json", "tech_wi_fi_problem_phrases.json", "tech_wi_fi_problem_sentences.json"]
    
    # Dictionary for translations
    translations = {
        "accensione": "switching on / power on",
        "adesso": "now",
        "anche": "also / even",
        "appartamento": "apartment",
        "aspetta": "wait (imperative)",
        "aspetto": "I wait",
        "avevi": "you had",
        "avvicinarti": "to get closer",
        "bene": "well / good",
        "bisogna": "it is necessary",
        "bisogno": "need",
        "buonasera": "good evening",
        "buongiorno": "good morning",
        "camera": "room",
        "capita": "it happens",
        "caricano": "they load",
        "cavo": "cable",
        "che": "that / what",
        "ciao": "hi / bye",
        "collegati": "connected",
        "comoda": "comfortable",
        "computer": "computer",
        "con": "with",
        "connessione": "connection",
        "controllo": "I check",
        "corrente": "current / power",
        "corridoio": "hallway",
        "cosa": "what / thing",
        "debole": "weak",
        "del": "of the",
        "della": "of the",
        "devo": "I must / I have to",
        "dietro": "behind",
        "dimmi": "tell me",
        "dispiace": "sorry / it's a pity",
        "dispositivi": "devices",
        "diventi": "it becomes",
        "esatto": "exact / exactly",
        "fare": "to do / to make",
        "fissa": "steady / fixed",
        "foglio": "sheet / paper",
        "forse": "maybe",
        "funziona": "it works",
        "grazie": "thanks",
        "guarda": "look",
        "hai": "you have",
        "internet": "internet",
        "lampeggiando": "flashing",
        "lenta": "slow",
        "lettere": "letters",
        "luce": "light",
        "luci": "lights",
        "maiuscolo": "uppercase",
        "mandato": "sent",
        "messaggio": "message",
        "mettere": "to put",
        "migliorare": "to improve",
        "mille": "thousand",
        "minuto": "minute",
        "mio": "my",
        "molti": "many",
        "molto": "very / much",
        "momento": "moment",
        "navigare": "to browse / to sail",
        "nel": "in the",
        "nero": "black",
        "nome": "name",
        "non": "not",
        "normale": "normal",
        "numeri": "numbers",
        "nuovo": "new",
        "ogni": "every / each",
        "ora": "now / hour",
        "pagine": "pages",
        "particolare": "particular",
        "password": "password",
        "per": "for",
        "perfettamente": "perfectly",
        "piano": "slowly / floor",
        "piccolo": "small",
        "posso": "I can",
        "premere": "to press",
        "premuto": "pressed",
        "problema": "problem",
        "pronto": "ready / hello (on phone)",
        "proprio": "really / own",
        "prova": "try",
        "pure": "also / even",
        "purtroppo": "unfortunately",
        "qual": "which",
        "qualcosa": "something",
        "quanti": "how many",
        "quella": "that",
        "rete": "network",
        "riattacca": "reconnect / hang up",
        "riavviare": "to restart",
        "riesci": "you succeed",
        "rossa": "red",
        "router": "router",
        "salotto": "living room",
        "scritta": "written",
        "segnale": "signal",
        "sei": "you are / six",
        "sistemato": "settled / arranged",
        "soggiorno": "stay / living room",
        "solito": "usual",
        "solo": "only",
        "sono": "I am / they are",
        "sopra": "above / on",
        "sparita": "disappeared",
        "spente": "off (plural)",
        "spento": "off (singular)",
        "sposto": "I move",
        "sta": "is / stays",
        "stacca": "unplug / detach",
        "staccare": "to unplug",
        "staccato": "unplugged",
        "strano": "strange",
        "subito": "immediately",
        "succede": "happens",
        "sul": "on the",
        "tablet": "tablet",
        "tanto": "so much",
        "tasto": "key / button",
        "tavolo": "table",
        "telefono": "phone",
        "trattino": "dash",
        "trovi": "you find",
        "tuo": "your",
        "tutta": "all / whole",
        "tutto": "all / everything",
        "vedi": "you see",
        "vedo": "I see",
        "velocità": "speed",
        "veramente": "really",
        "verde": "green",
        "wifi": "wifi"
    }

    # Sentence translations are easier to get from conversations.json if they match exactly
    # But I'll just fill them manually for speed.
    sentences_trans = {
        "Ah, purtroppo ogni tanto capita. Bisogna riavviare.": "Ah, unfortunately it happens every now and then. It needs to be restarted.",
        "Bene. Hai bisogno di qualcosa in particolare?": "Good. Do you need anything in particular?",
        "Buonasera. Va tutto bene per il tuo soggiorno?": "Good evening. Is everything going well with your stay?",
        "Buongiorno! Ti sei sistemato bene in camera?": "Good morning! Have you settled in well in your room?",
        "Ciao! Tutto bene con l'appartamento?": "Hi! Is everything okay with the apartment?",
        "Dimmi pure, cosa succede?": "Tell me, what's happening?",
        "Esatto. È scritta tutta in maiuscolo.": "Exactly. It is written all in uppercase.",
        "Forse il router è spento. È nel salotto.": "Maybe the router is off. It's in the living room.",
        "Forse il segnale è debole in quella camera.": "Maybe the signal is weak in that room.",
        "La trovi su un foglio sopra il tavolo. La vedi?": "You can find it on a sheet of paper on the table. Do you see it?",
        "Mi dispiace. Non riesci a navigare bene?": "I'm sorry. Are you not able to browse well?",
        "No, solo i numeri e le lettere. Prova ora.": "No, just the numbers and the letters. Try now.",
        "Ora riattacca il cavo e guarda le luci.": "Now reconnect the cable and look at the lights.",
        "Pronto? Mi avevi mandato un messaggio?": "Hello? Had you sent me a message?",
        "Prova a premere il tasto di accensione dietro.": "Try pressing the power button on the back.",
        "Prova ad avvicinarti al router nel corridoio.": "Try moving closer to the router in the hallway.",
        "Quanti dispositivi sono collegati?": "How many devices are connected?",
        "Strano, di solito va bene. Vedi la rete?": "Strange, it usually works fine. Do you see the network?",
        "Sì, stacca il cavo nero e aspetta un minuto.": "Yes, unplug the black cable and wait a minute.",
        "È normale. Aspetta che diventi fissa e verde.": "It's normal. Wait for it to become steady and green."
    }

    phrases_trans = {
        "Ah sì, vedo il foglio. È quella con molti numeri?": "Ah yes, I see the paper. Is it the one with many numbers?",
        "Buonasera. La connessione internet è molto lenta.": "Good evening. The internet connection is very slow.",
        "Controllo subito... sì, le luci sono spente.": "I'll check right away... yes, the lights are off.",
        "Cosa posso fare per migliorare la velocità?": "What can I do to improve the speed?",
        "Devo staccare il cavo della corrente?": "Do I have to unplug the power cable?",
        "Funziona perfettamente! Grazie mille.": "It works perfectly! Thanks a lot.",
        "Il wifi non funziona sul mio telefono.": "The wifi doesn't work on my phone.",
        "L'ho premuto. Adesso la luce è verde.": "I pressed it. Now the light is green.",
        "La luce rossa sta lampeggiando adesso.": "The red light is flashing now.",
        "No, le pagine caricano molto piano.": "No, the pages load very slowly.",
        "No, non vedo proprio il nome della rete.": "No, I don't see the network name at all.",
        "Ok, ora è verde. Controllo la connessione.": "Ok, now it's green. I'm checking the connection.",
        "Solo il mio computer e il mio tablet.": "Only my computer and my tablet.",
        "Sì, grazie. È molto comoda.": "Yes, thanks. It is very comfortable.",
        "Sì, la rete internet è sparita di nuovo.": "Yes, the internet network has disappeared again.",
        "Sì, qual è la password del wifi?": "Yes, what is the wifi password?",
        "Va bene, l'ho staccato. Aspetto un momento.": "Alright, I unplugged it. I'll wait a moment.",
        "Va bene, mi sposto subito con il pc.": "Alright, I'll move right away with the pc.",
        "Va bene. Devo mettere anche il trattino?": "Alright. Do I also need to put the dash?",
        "Veramente ho un piccolo problema.": "Actually, I have a small problem."
    }

    for fname in files:
        fpath = os.path.join(path, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            items = json.load(f)
        
        for item in items:
            it = item["italian"].strip()
            if "vocabulary" in fname:
                item["english"] = translations.get(it, "")
            elif "phrases" in fname:
                item["english"] = phrases_trans.get(it, "")
            elif "sentences" in fname:
                item["english"] = sentences_trans.get(it, "")
        
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
    print("Translations filled.")

if __name__ == "__main__":
    fill()
