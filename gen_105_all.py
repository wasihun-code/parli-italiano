import json
import os

os.makedirs('src/data/exports/tech/atm_machine', exist_ok=True)

# 1. domain.json
domain = {
  "id": "105",
  "category": "tech",
  "name": "atm_machine",
  "title": "At the ATM",
  "description": "Use an ATM, withdraw money, understand fees, and check balance.",
  "required_vocabulary": ["bancomat", "prelevare", "contanti", "carta", "codice PIN", "saldo", "commissione", "ricevuta", "inserire"],
  "forbidden_topics": ["restaurant", "hospital", "museum"]
}
with open('src/data/exports/tech/atm_machine/domain.json', 'w') as f:
    json.dump(domain, f, indent=2)

# Helper for choices
def make_choice(text, is_correct, feedback):
    return {"text": text, "isCorrect": is_correct, "feedback": feedback}

conversations = []

# Conv 1: Withdraw Cash
messages_c1 = []
prompts_c1 = [
    ("Benvenuto. Inserire la carta nel bancomat.", "Welcome. Insert the card into the ATM.", 
     "Inserisco la carta nel bancomat.", "Inserisco la borsa nel bancomat.", "Inserisco la porta nel bancomat."),
    ("Carta accettata. Digitare il codice PIN.", "Card accepted. Enter the PIN code.", 
     "Digito il mio codice PIN segreto.", "Digito il mio numero di telefono.", "Digito il mio indirizzo di casa."),
    ("Codice PIN corretto. Scegliere l'operazione.", "PIN code correct. Choose the operation.", 
     "Voglio prelevare dei contanti oggi.", "Voglio comprare dei pantaloni oggi.", "Voglio restituire dei contanti oggi."),
    ("Scegliere l'importo da prelevare, per favore.", "Choose the amount to withdraw, please.", 
     "Scelgo cinquanta euro in contanti.", "Scelgo cinquanta libri in contanti.", "Scelgo cinquanta cani in contanti."),
    ("Vuole stampare la ricevuta cartacea oggi?", "Do you want to print the paper receipt today?", 
     "Sì, voglio stampare la ricevuta.", "Sì, voglio stampare la maglietta.", "Sì, voglio stampare la bicicletta."),
    ("Attenzione: è prevista una commissione di due euro.", "Warning: there is a commission of two euros.", 
     "Va bene, accetto la commissione.", "Va bene, accetto la televisione.", "Va bene, accetto la conversazione."),
    ("Attendere prego. Elaborazione della richiesta.", "Please wait. Processing the request.", 
     "Attendo con pazienza davanti al bancomat.", "Ballo con pazienza davanti al bancomat.", "Canto con pazienza davanti al bancomat."),
    ("Ritirare i contanti dalla fessura in basso.", "Withdraw the cash from the slot below.", 
     "Prendo i miei contanti dal bancomat.", "Prendo i miei biscotti dal bancomat.", "Prendo i miei documenti dal bancomat."),
    ("Ritirare la ricevuta stampata dalla fessura.", "Withdraw the printed receipt from the slot.", 
     "Prendo la ricevuta e la leggo.", "Prendo la chitarra e la suono.", "Prendo la macchina e la guido."),
    ("Operazione conclusa. Ritirare la carta, grazie.", "Operation completed. Withdraw the card, thank you.", 
     "Prendo la mia carta e vado.", "Prendo la mia scarpa e vado.", "Prendo la mia gatta e vado.")
]
for i, (it, en, c1, c2, c3) in enumerate(prompts_c1):
    messages_c1.append({
        "id": f"c1_m{i+1}", "role": "host", "text": it, "english": en,
        "choices": [
            make_choice(c1, True, "Correct choice!"),
            make_choice(c2, False, "Incorrect context."),
            make_choice(c3, False, "Incorrect context.")
        ]
    })
conversations.append({"id": "c1_withdraw", "title": "Withdraw Cash", "description": "Withdraw cash from the ATM.", "messages": messages_c1})

# Conv 2: Check Balance
messages_c2 = []
prompts_c2 = [
    ("Benvenuto al bancomat. Inserire la carta.", "Welcome to the ATM. Insert the card.", 
     "Inserisco subito la mia carta.", "Inserisco subito la mia scarpa.", "Inserisco subito la mia pianta."),
    ("Per favore, digitare il codice PIN.", "Please, enter the PIN code.", 
     "Digito il codice PIN con cura.", "Digito il numero due con cura.", "Digito il codice a barre con cura."),
    ("Selezionare l'operazione desiderata sullo schermo.", "Select the desired operation on the screen.", 
     "Voglio controllare il mio saldo.", "Voglio controllare il mio gatto.", "Voglio controllare il mio orologio."),
    ("Richiesta saldo in corso. Attendere prego.", "Balance request in progress. Please wait.", 
     "Aspetto di vedere il mio saldo.", "Aspetto di vedere il mio libro.", "Aspetto di vedere il mio amico."),
    ("Il saldo disponibile è di mille euro.", "The available balance is one thousand euros.", 
     "Perfetto, il saldo è molto positivo.", "Perfetto, il caldo è molto positivo.", "Perfetto, il pasto è molto positivo."),
    ("Desidera stampare il saldo su ricevuta?", "Do you want to print the balance on a receipt?", 
     "Sì, voglio una ricevuta cartacea.", "Sì, voglio una cravatta cartacea.", "Sì, voglio una finestra cartacea."),
    ("Stampa della ricevuta in corso. Attendere.", "Printing receipt in progress. Wait.", 
     "Aspetto la stampa della ricevuta.", "Aspetto la stampa della maglietta.", "Aspetto la stampa della settimana."),
    ("Prelevare la ricevuta dalla fessura luminosa.", "Take the receipt from the illuminated slot.", 
     "Prendo la ricevuta con le mani.", "Prendo la ricevuta con le dita.", "Prendo la ricevuta con le braccia."), # Distractors need to be distinct but grammatically similar.
    ("Desidera effettuare un'altra operazione oggi?", "Do you wish to perform another operation today?", 
     "No, non voglio fare altre operazioni.", "No, non voglio bere altre operazioni.", "No, non voglio dire altre operazioni."),
    ("Ritirare la carta. Arrivederci e grazie.", "Withdraw the card. Goodbye and thank you.", 
     "Prendo la carta e vado via.", "Prendo la porta e vado via.", "Prendo la torta e vado via.")
]
# Fix c2_m8 distractors:
prompts_c2[7] = ("Prelevare la ricevuta dalla fessura luminosa.", "Take the receipt from the illuminated slot.", 
     "Prendo la ricevuta dalla fessura.", "Prendo la mela dalla fessura.", "Prendo la pera dalla fessura.")

for i, (it, en, c1, c2, c3) in enumerate(prompts_c2):
    messages_c2.append({
        "id": f"c2_m{i+1}", "role": "host", "text": it, "english": en,
        "choices": [
            make_choice(c1, True, "Correct choice!"),
            make_choice(c2, False, "Incorrect context."),
            make_choice(c3, False, "Incorrect context.")
        ]
    })
conversations.append({"id": "c2_balance", "title": "Check Balance", "description": "Check the account balance.", "messages": messages_c2})

# Conv 3: Commission Fees
messages_c3 = []
prompts_c3 = [
    ("Inserire la carta per iniziare l'operazione.", "Insert the card to begin the operation.", 
     "Metto la carta nel bancomat adesso.", "Metto la sedia nel bancomat adesso.", "Metto la borsa nel bancomat adesso."),
    ("Digitare il codice PIN in modo sicuro.", "Enter the PIN code securely.", 
     "Copro la tastiera e digito il PIN.", "Copro la finestra e digito il PIN.", "Copro la bottiglia e digito il PIN."),
    ("Quale operazione desidera effettuare questa mattina?", "Which operation do you want to perform this morning?", 
     "Voglio prelevare venti euro oggi.", "Voglio comprare venti euro oggi.", "Voglio cucinare venti euro oggi."),
    ("Attenzione: la sua banca applica una commissione.", "Warning: your bank applies a commission fee.", 
     "Quanto costa questa commissione di prelievo?", "Quanto costa questa televisione di prelievo?", "Quanto costa questa colazione di prelievo?"),
    ("La commissione per il prelievo è due euro.", "The withdrawal fee is two euros.", 
     "Due euro di commissione sono troppi.", "Due euro di televisione sono troppi.", "Due euro di colazione sono troppi."),
    ("Vuole annullare l'operazione o continuare comunque?", "Do you want to cancel the operation or continue anyway?", 
     "Voglio annullare l'operazione di prelievo.", "Voglio annullare la partita di calcio.", "Voglio annullare la cena di stasera."),
    ("Operazione annullata. Nessun importo verrà addebitato.", "Operation cancelled. No amount will be charged.", 
     "Va bene, andrò alla mia banca.", "Va bene, andrò alla mia scuola.", "Va bene, andrò alla mia cucina."),
    ("Vuole effettuare una diversa operazione allo sportello?", "Do you want to perform a different operation at the ATM?", 
     "Sì, voglio solo controllare il saldo.", "Sì, voglio solo guardare il cane.", "Sì, voglio solo pulire il pavimento."),
    ("Il saldo non prevede commissioni. Procedere?", "The balance check has no fees. Proceed?", 
     "Sì, procediamo con il saldo.", "Sì, procediamo con il caldo.", "Sì, procediamo con il pasto."),
    ("Ritirare la carta dallo sportello. Arrivederci.", "Withdraw the card from the ATM. Goodbye.", 
     "Ritiro la carta e ringrazio.", "Ritiro la spesa e ringrazio.", "Ritiro la borsa e ringrazio.")
]
for i, (it, en, c1, c2, c3) in enumerate(prompts_c3):
    messages_c3.append({
        "id": f"c3_m{i+1}", "role": "host", "text": it, "english": en,
        "choices": [
            make_choice(c1, True, "Correct choice!"),
            make_choice(c2, False, "Incorrect context."),
            make_choice(c3, False, "Incorrect context.")
        ]
    })
conversations.append({"id": "c3_fees", "title": "Commission Fees", "description": "Understand commission fees and cancel.", "messages": messages_c3})

# Conv 4: Wrong PIN
messages_c4 = []
prompts_c4 = [
    ("Sportello automatico. Inserire la carta, per favore.", "Automatic teller. Insert the card, please.", 
     "Inserisco la carta di credito qui.", "Inserisco la chiave di casa qui.", "Inserisco la patente di guida qui."),
    ("Digitare il codice PIN di cinque cifre.", "Enter the five-digit PIN code.", 
     "Digito il codice molto velocemente.", "Bevo il caffè molto velocemente.", "Leggo il libro molto velocemente."),
    ("Errore. Il codice PIN inserito è errato.", "Error. The entered PIN code is incorrect.", 
     "Oh no, ho sbagliato il codice.", "Oh no, ho mangiato il codice.", "Oh no, ho lavato il codice."),
    ("Rimangono due tentativi prima del blocco carta.", "Two attempts remaining before card block.", 
     "Provo a digitare il codice corretto.", "Provo a mangiare la mela verde.", "Provo a cantare la canzone nuova."),
    ("Inserire nuovamente il codice PIN con attenzione.", "Enter the PIN code again carefully.", 
     "Ecco, digito i numeri giusti stavolta.", "Ecco, mangio i biscotti giusti stavolta.", "Ecco, lavo i piatti giusti stavolta."),
    ("Codice PIN corretto. Accesso consentito al conto.", "PIN code correct. Access granted to account.", 
     "Meno male! Ora voglio prelevare contanti.", "Meno male! Ora voglio mangiare pasta.", "Meno male! Ora voglio bere acqua."),
    ("Selezionare l'importo: venti, cinquanta o cento euro.", "Select the amount: twenty, fifty, or one hundred euros.", 
     "Seleziono cinquanta euro sullo schermo.", "Seleziono cinquanta cani sullo schermo.", "Seleziono cinquanta gatti sullo schermo."),
    ("Erogazione banconote in corso. Attendere un momento.", "Dispensing banknotes. Wait a moment.", 
     "Attendo le banconote dal bancomat.", "Attendo le mele dal bancomat.", "Attendo le patate dal bancomat."),
    ("Ritirare le banconote prima della scadenza del tempo.", "Take the banknotes before the time expires.", 
     "Prendo i soldi velocemente.", "Prendo i libri velocemente.", "Prendo i fiori velocemente."),
    ("Grazie per aver usato il nostro bancomat.", "Thank you for using our ATM.", 
     "Prendo la carta e vado via.", "Prendo la sedia e vado via.", "Prendo la tavola e vado via.")
]
for i, (it, en, c1, c2, c3) in enumerate(prompts_c4):
    messages_c4.append({
        "id": f"c4_m{i+1}", "role": "host", "text": it, "english": en,
        "choices": [
            make_choice(c1, True, "Correct choice!"),
            make_choice(c2, False, "Incorrect context."),
            make_choice(c3, False, "Incorrect context.")
        ]
    })
conversations.append({"id": "c4_wrong_pin", "title": "Wrong PIN", "description": "Enter the wrong PIN and try again.", "messages": messages_c4})

conversations_data = {
    "scenarioId": "105",
    "conversations": conversations
}

with open('src/data/exports/tech/atm_machine/conversations.json', 'w') as f:
    json.dump(conversations_data, f, indent=2)

print("Created domain.json and conversations.json")
