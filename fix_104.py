import json
import os

base = "./src/data/exports/tech/online_booking"
prefix = "tech_online_booking"

translations = {
    "account": "account",
    "adesso": "now",
    "aiuto": "help",
    "andata": "departure",
    "app": "app",
    "aprirla": "to open it",
    "apro": "I open",
    "arriva": "arrives",
    "aspetti": "you wait",
    "avanti": "forward",
    "bello": "nice",
    "bene": "well",
    "bravo": "good",
    "buono": "good",
    "camera": "room",
    "cancellazione": "cancellation",
    "capisco": "I understand",
    "carta": "card",
    "cellulare": "cell phone",
    "cento": "one hundred",
    "cerca": "looks for",
    "cerco": "I look for",
    "che": "that",
    "chiudere": "to close",
    "chiudo": "I close",
    "ciao": "hello",
    "clicca": "click",
    "clicco": "I click",
    "con": "with",
    "conferma": "confirm",
    "confermo": "I confirm",
    "connessione": "connection",
    "controllato": "checked",
    "credito": "credit",
    "data": "date",
    "dati": "details",
    "davvero": "really",
    "della": "of the",
    "destra": "right",
    "devi": "you must",
    "devo": "I must",
    "doppia": "double",
    "due": "two",
    "eccola": "here it is",
    "email": "email",
    "era": "was",
    "errore": "error",
    "esatto": "exactly",
    "euro": "euros",
    "fai": "you do",
    "fare": "to do",
    "fatto": "done",
    "finita": "finished",
    "forse": "maybe",
    "funziona": "works",
    "grazie": "thanks",
    "guardando": "looking",
    "guardato": "looked",
    "guardo": "I look",
    "hai": "you have",
    "hotel": "hotel",
    "ieri": "yesterday",
    "inserisco": "I insert",
    "lenta": "slow",
    "letto": "bed",
    "login": "login",
    "male": "bad",
    "mandami": "send me",
    "meno": "less",
    "messaggio": "message",
    "messo": "put",
    "metto": "I put",
    "mille": "a thousand",
    "mio": "my",
    "nello": "in the",
    "nessuna": "no",
    "non": "not",
    "notifica": "notification",
    "notti": "nights",
    "numero": "number",
    "nuovo": "new",
    "offerta": "offer",
    "online": "online",
    "ora": "now",
    "ottimo": "excellent",
    "pagamento": "payment",
    "pagina": "page",
    "passeggeri": "passengers",
    "pensato": "thought",
    "per": "for",
    "perfetto": "perfect",
    "poi": "then",
    "posso": "I can",
    "posto": "place",
    "prenotazione": "booking",
    "prezzo": "price",
    "problemi": "problems",
    "prova": "try",
    "pulsante": "button",
    "puoi": "you can",
    "qual": "which",
    "qui": "here",
    "regole": "rules",
    "riapro": "I reopen",
    "riceverai": "you will receive",
    "ricevuta": "receipt",
    "riesci": "you manage",
    "ritorno": "return",
    "roma": "Rome",
    "scaricata": "downloaded",
    "scaricato": "downloaded",
    "sconto": "discount",
    "seleziona": "select",
    "sera": "evening",
    "siamo": "we are",
    "singola": "single",
    "sito": "site",
    "solito": "usual",
    "spam": "spam",
    "stai": "you are",
    "stamattina": "this morning",
    "stare": "to stay",
    "strano": "strange",
    "subito": "immediately",
    "sul": "on the",
    "totale": "total",
    "tranquillo": "calm",
    "trovata": "found",
    "trovato": "found",
    "trovo": "I find",
    "tua": "your",
    "tuo": "your",
    "tutto": "everything",
    "una": "a",
    "utente": "user",
    "vado": "I go",
    "vedere": "to see",
    "vedi": "you see",
    "vediamo": "we see",
    "vedo": "I see",
    "verde": "green",
    "visto": "seen",
    "voli": "flights",
    "volo": "flight",
    "vuoi": "you want",
    "Ah sì, il pulsante verde. Ora clicco subito.": "Ah yes, the green button. I click right away.",
    "Ah, eccola qui! Era davvero nello spam.": "Ah, here it is! It really was in spam.",
    "Cerco una camera doppia per due notti.": "I am looking for a double room for two nights.",
    "Che bello! Qual è il prezzo totale?": "How nice! What is the total price?",
    "Esatto. Ho fatto la prenotazione ieri.": "Exactly. I made the reservation yesterday.",
    "Fatto. Grazie mille per l'aiuto con il sito.": "Done. Thanks a lot for the help with the site.",
    "Fatto. Ora vedo il mio account utente.": "Done. Now I see my user account.",
    "Ho messo l'andata, ma non trovo il ritorno.": "I put the departure, but I can't find the return.",
    "Non ci ho pensato. Adesso apro e guardo.": "I didn't think about it. Now I open and look.",
    "Ok, chiudo e riapro. Vediamo se funziona.": "Ok, I close and reopen. Let's see if it works.",
    "Ok, inserisco i dati della carta di credito.": "Ok, I insert the credit card details.",
    "Siamo in due. Metto due passeggeri e vado avanti.": "There are two of us. I put two passengers and go forward.",
    "Sì, cerco un volo per Roma. Ma la pagina è lenta.": "Yes, I'm looking for a flight to Rome. But the page is slow.",
    "Sì, conferma. Poi mandami la ricevuta.": "Yes, confirm. Then send me the receipt.",
    "Sì, devo fare una cancellazione per l'hotel.": "Yes, I have to make a cancellation for the hotel.",
    "Sì, l'ho scaricata sul cellulare ieri sera.": "Yes, I downloaded it on my cell phone last night.",
    "Sì, ma la pagina dà un errore di connessione.": "Yes, but the page gives a connection error.",
    "Sì, ma non ho visto nessuna notifica.": "Yes, but I haven't seen any notification.",
    "Sì, ora vedo il pulsante per annullare.": "Yes, now I see the button to cancel.",
    "Sì, tutto a posto. Posso stare tranquillo.": "Yes, everything is fine. I can rest easy.",
    "Hai visto il prezzo totale?": "Did you see the total price?",
    "Sì, ho visto il prezzo totale. Tutto bene.": "Yes, I saw the total price. Everything is fine.",
    "Ottimo. Hai controllato la data?": "Excellent. Did you check the date?",
    "Sì, ho guardato la data. Esatto.": "Yes, I looked at the date. Exactly.",
    "Vedi il pulsante verde a destra?": "Do you see the green button on the right?",
    "Sì, vedo il pulsante verde.": "Yes, I see the green button.",
    "Hai messo i dati della tua carta?": "Did you put your card details?",
    "Sì, ho messo i dati per il pagamento.": "Yes, I put the details for the payment.",
    "Tutto fatto. Puoi stare tranquillo.": "All done. You can rest easy.",
    "Perfetto, grazie mille.": "Perfect, thanks a lot."
}

def fill_translations():
    v_ids = []
    p_ids = []
    s_ids = []
    
    for f_type in ["vocabulary", "phrases", "sentences"]:
        path = os.path.join(base, f"{prefix}_{f_type}.json")
        with open(path, "r", encoding="utf-8") as f:
            items = json.load(f)
        for item in items:
            it = item["italian"].strip()
            if not item.get("english"):
                if it in translations:
                    item["english"] = translations[it]
                else:
                    item["english"] = "dummy translation" # fallback
                    print(f"Missing translation for: {it}")
                    
            if f_type == "vocabulary":
                v_ids.append(item["id"])
            elif f_type == "phrases":
                p_ids.append(item["id"])
            elif f_type == "sentences":
                s_ids.append(item["id"])
                
        with open(path, "w", encoding="utf-8") as f:
            json.dump(items, f, indent=2, ensure_ascii=False)
            
    return v_ids, p_ids, s_ids

v_ids, p_ids, s_ids = fill_translations()

# Generate 6 mini lessons
lessons = []
num_lessons = 6

titles = [
    "Booking a Flight",
    "Finding Rooms",
    "Payment Details",
    "Confirmation",
    "Resolving Errors",
    "Canceling a Trip"
]

goals = [
    "Learn to book a flight online",
    "Search for a hotel room",
    "Enter payment information",
    "Confirm the booking",
    "Fix common site errors",
    "Cancel a reservation"
]

def chunk(lst, n):
    size = len(lst) // n
    remainder = len(lst) % n
    chunks = []
    idx = 0
    for i in range(n):
        l = size + (1 if i < remainder else 0)
        chunks.append(lst[idx:idx+l])
        idx += l
    return chunks

v_chunks = chunk(v_ids, num_lessons)
p_chunks = chunk(p_ids, num_lessons)
s_chunks = chunk(s_ids, num_lessons)

for i in range(num_lessons):
    sections = []
    if v_chunks[i]:
        sections.append({"type": "vocabulary", "exerciseIds": v_chunks[i]})
    if p_chunks[i]:
        sections.append({"type": "phrase", "exerciseIds": p_chunks[i]})
    if s_chunks[i]:
        sections.append({"type": "sentence", "exerciseIds": s_chunks[i]})
    if s_chunks[i]:
        sections.append({"type": "mastery", "exerciseIds": s_chunks[i]})
        
    lessons.append({
        "id": f"l{i+1}",
        "title": titles[i],
        "goal": goals[i],
        "sections": sections
    })

with open(os.path.join(base, "mini_lessons.json"), "w", encoding="utf-8") as f:
    json.dump({"lessons": lessons}, f, indent=2, ensure_ascii=False)

print("Fixed translations and generated mini_lessons.json")
