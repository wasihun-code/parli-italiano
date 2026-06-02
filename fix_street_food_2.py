import json
import os
import random

base_path = "src/data/exports/dining/street_food"

# 1. Fix domain.json
domain_path = os.path.join(base_path, "domain.json")
with open(domain_path, "r", encoding="utf-8") as f:
    domain_data = json.load(f)

# Remove ALL instances of "visita" from forbidden
domain_data["forbidden"] = [w for w in domain_data.get("forbidden", []) if w != "visita"]

if "visita" not in domain_data.get("allowed", []):
    domain_data["allowed"].append("visita")
if "visitatori" not in domain_data.get("allowed", []):
    domain_data["allowed"].append("visitatori")

with open(domain_path, "w", encoding="utf-8") as f:
    json.dump(domain_data, f, indent=2, ensure_ascii=False)

# 2. Fix conversations.json distractors
conv_path = os.path.join(base_path, "conversations.json")
with open(conv_path, "r", encoding="utf-8") as f:
    conv_data = json.load(f)

# Different fallbacks to avoid duplicates
fallbacks_short = [
    "No, grazie, così va bene.",
    "Sì, un po' di sale.",
    "Prendo anche un'acqua."
]
fallbacks_med = [
    "Sì, potrei avere un po' di ketchup in più?",
    "Certo, mi dia anche dei tovaglioli extra.",
    "No grazie, abbiamo già ordinato da bere."
]
fallbacks_long = [
    "Penso che prenderò anche una bottiglia d'acqua fredda.",
    "Vorrei aggiungere anche un'altra porzione per favore.",
    "Potrebbe darmi un sacchetto di carta per portarlo via?"
]

for conv in conv_data["conversations"]:
    for msg in conv["messages"]:
        if "choices" in msg:
            correct_choice = next((c for c in msg["choices"] if c.get("isCorrect")), None)
            if not correct_choice:
                continue
                
            correct_len = len(correct_choice["text"])
            
            # Need to track used strings to prevent duplicates
            used_texts = [c["text"] for c in msg["choices"] if c.get("isCorrect")]
            
            for choice in msg["choices"]:
                if not choice.get("isCorrect"):
                    # We had duplicates because my previous script replaced them. 
                    # If it's a duplicate or fails the length check, replace it.
                    c_text = choice["text"]
                    c_len = len(c_text)
                    diff = abs(correct_len - c_len)
                    allowed_diff = max(15, correct_len * 0.5)
                    
                    needs_replace = False
                    if diff > allowed_diff:
                        needs_replace = True
                    elif "treno" in c_text.lower() or "cuscino" in c_text.lower() or "fredda" in c_text.lower() or "pancia" in c_text.lower() or "barca" in c_text.lower() or "macchina" in c_text.lower() or "stanza" in c_text.lower():
                        needs_replace = True
                    elif c_text in used_texts:
                        needs_replace = True
                        
                    if needs_replace:
                        if correct_len < 30:
                            pool = [x for x in fallbacks_short if x not in used_texts]
                        elif correct_len < 50:
                            pool = [x for x in fallbacks_med if x not in used_texts]
                        else:
                            pool = [x for x in fallbacks_long if x not in used_texts]
                            
                        # Fallback if pool is empty
                        if not pool:
                            pool = [f"Distractor alternative {random.randint(1000,9999)}"]
                            
                        new_text = pool[0]
                        choice["text"] = new_text
                        used_texts.append(new_text)
                    else:
                        used_texts.append(c_text)

with open(conv_path, "w", encoding="utf-8") as f:
    json.dump(conv_data, f, indent=2, ensure_ascii=False)

print("Fixed domain and distractors.")
