import json
import os

scenario_id = 105

# 4 conversations
conversations = []

for c_idx in range(1, 5):
    conv_id = f"c{c_idx}_atm"
    titles = [
        "Withdrawal Basics", 
        "Checking Balance",
        "Understanding Fees",
        "Card Issues"
    ]
    descs = [
        "Withdraw cash at the ATM.",
        "Check your account balance.",
        "Understand the commission fees.",
        "Resolve a small card issue."
    ]
    
    messages = []
    
    for m_idx in range(1, 11):
        msg_id = f"m{m_idx}"
        
        # We need Italian text, english, and 3 choices.
        text_it = f"Benvenuto allo sportello bancomat. Operazione {m_idx} per favore."
        text_en = f"Welcome to the ATM. Operation {m_idx} please."
        
        c1_it = f"Voglio prelevare dei contanti ora {m_idx}."
        c2_it = f"Voglio mangiare una pizza ora {m_idx}."
        c3_it = f"Voglio comprare un gelato ora {m_idx}."
        
        # Make them similar length and no placeholders.
        if c_idx == 1: # Withdrawal Basics
            text_it = f"Sportello bancomat. Inserire la carta per l'operazione {m_idx}."
            text_en = f"ATM. Insert the card for operation {m_idx}."
            c1_it = f"Inserisco la carta e digito il codice PIN ora {m_idx}."
            c2_it = f"Consegno la borsa e chiedo la ricevuta ora {m_idx}."
            c3_it = f"Dimentico la carta e lascio la ricevuta ora {m_idx}."
        
        # ... actually wait, this needs to be high quality Italian, A1-A2, 4 convs.
        pass

# I will write the actual realistic text directly here.
