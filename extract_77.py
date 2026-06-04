import json
import os
import re
import random

scenario_path = 'src/data/exports/social/apologizing'
conv_file = os.path.join(scenario_path, 'conversations.json')

with open(conv_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

sentences = []
seen_sentences = set()
vocab_set = set()

def clean_word(w):
    w = w.lower()
    w = re.sub(r'[^\w\s\']', '', w)
    return w.strip()

# Correct choice translations mapping
choice_translations = {
    "Sì, scusa il ritardo. C'era un traffico incredibile oggi.": "Yes, sorry for the delay. There was incredible traffic today.",
    "Mi dispiace davvero tanto per l'attesa. Non volevo farti aspettare.": "I am truly very sorry for the wait. I didn't mean to make you wait.",
    "Sì, volentieri. Offro io per farmi perdonare il ritardo.": "Yes, gladly. It's on me to make up for the delay.",
    "Insisto, davvero. È il minimo che posso fare oggi.": "I insist, really. It's the least I can do today.",
    "Prendo un cappuccino e un cornetto alla crema.": "I'll have a cappuccino and a cream croissant.",
    "Sì, ho girato per venti minuti buoni prima di trovarlo.": "Yes, I drove around for a good twenty minutes before finding it.",
    "Abbastanza bene, grazie. Solo un po' di stress ultimamente.": "Quite well, thanks. Just a bit of stress lately.",
    "Mi piacerebbe molto, ma oggi devo finire un progetto.": "I would really like to, but today I have to finish a project.",
    "Sì, il weekend suona perfetto. Sentiamoci venerdì.": "Yes, the weekend sounds perfect. Let's talk on Friday.",
    "Certamente! Grazie ancora per la tua pazienza infinita.": "Certainly! Thanks again for your infinite patience.",
    "Buongiorno. Mi scusi, ho dimenticato l'appuntamento di stamattina.": "Good morning. Excuse me, I forgot this morning's appointment.",
    "Sono Mario Rossi. Avevo l'appuntamento alle dieci.": "I'm Mario Rossi. I had the appointment at ten o'clock.",
    "Ho avuto un imprevisto al lavoro e ho perso la cognizione del tempo.": "I had an unexpected event at work and I lost track of time.",
    "Ha ragione, chiedo scusa. Mi sono sentito davvero in colpa.": "You're right, I apologize. I felt really guilty.",
    "Sì, per favore. Quando sarebbe possibile venire questa settimana?": "Yes, please. When would it be possible to come this week?",
    "Giovedì alle quindici è perfetto. Grazie mille per la disponibilità.": "Thursday at three is perfect. Thank you very much for the availability.",
    "Capisco perfettamente, sarò puntualissimo questa volta.": "I understand perfectly, I will be very punctual this time.",
    "No, grazie. Mi scusi ancora per il disturbo di oggi.": "No, thanks. Excuse me again for the inconvenience today.",
    "Sicuramente. Buona giornata e buon lavoro.": "Definitely. Have a good day and good work.",
    "Arrivederci!": "Goodbye!",
    "Oddio, mi dispiace tantissimo! Ho rotto un bicchiere per sbaglio.": "Oh god, I'm so sorry! I broke a glass by mistake.",
    "No, sto bene. Scusami, sono stato davvero molto distratto.": "No, I'm fine. Sorry, I was really very distracted.",
    "No, faccio io per favore! Mi sento davvero male per l'accaduto.": "No, let me do it please! I feel really bad about what happened.",
    "Va bene, ma lasciami almeno aiutare a buttare via i pezzi grandi.": "Alright, but at least let me help throw away the large pieces.",
    "Grazie. Ti prometto che ti comprerò un set di bicchieri nuovi.": "Thank you. I promise I will buy you a set of new glasses.",
    "Sei troppo gentile. Mi dispiace ancora tanto per il disturbo.": "You're too kind. I'm so sorry again for the inconvenience.",
    "Magari sì, grazie. Ma questa volta terrò il bicchiere con due mani!": "Maybe yes, thanks. But this time I'll hold the glass with two hands!",
    "Cin cin! E grazie per non esserti arrabbiato.": "Cheers! And thanks for not getting angry.",
    "Lo so, sei un vero amico. Mi sento più sollevato ora.": "I know, you're a true friend. I feel more relieved now.",
    "D'accordo! Starò molto più attento, lo giuro.": "Agreed! I will be much more careful, I swear.",
    "Festa? Oh no! Mi sono completamente dimenticato del tuo compleanno!": "Party? Oh no! I completely forgot about your birthday!",
    "Mi dispiace da morire, davvero. Ti prego di perdonarmi.": "I'm terribly sorry, really. Please forgive me.",
    "Hai tutte le ragioni per essere arrabbiato. Sono stato un pessimo amico.": "You have every reason to be angry. I was a terrible friend.",
    "Non è una scusa valida. Avrei dovuto almeno mandarti un messaggio.": "It's not a valid excuse. I should have at least sent you a message.",
    "Posso farmi perdonare offrendoti una cena speciale questo weekend?": "Can I make it up to you by offering you a special dinner this weekend?",
    "In quel nuovo ristorante in centro che volevi provare da tanto.": "In that new restaurant downtown that you've wanted to try for so long.",
    "Grazie di cuore. Mi sento molto meglio ora che mi hai perdonato.": "Thank you from the bottom of my heart. I feel much better now that you've forgiven me.",
    "Facciamo alle venti? Così abbiamo tempo per chiacchierare con calma.": "How about eight o'clock? So we have time to chat calmly.",
    "Anch'io! E ti porterò anche un piccolo regalo che ti piacerà.": "Me too! And I'll also bring you a small gift that you'll like.",
    "A sabato! Buona settimana nel frattempo.": "See you Saturday! Have a good week in the meantime."
}

for conv in data['conversations']:
    for msg in conv['messages']:
        # Host text
        if msg['text'] not in seen_sentences:
            sentences.append({"italian": msg['text'], "english": msg['english']})
            seen_sentences.add(msg['text'])
        
        # User choices (only correct ones)
        for choice in msg['choices']:
            if choice['isCorrect']:
                if choice['text'] not in seen_sentences:
                    eng = choice_translations.get(choice['text'], "")
                    sentences.append({"italian": choice['text'], "english": eng})
                    seen_sentences.add(choice['text'])

# Extract vocabulary from all sentences
all_extracted_text = " ".join([s['italian'] for s in sentences])
words = all_extracted_text.split()
for w in words:
    cw = clean_word(w)
    if cw and len(cw) > 1 and not cw.isdigit():
        vocab_set.add(cw)

sorted_vocab = sorted(list(vocab_set))

# Vocabulary mapping (expanded for scenario 77)
vocab_map = {
    "scusa": "sorry", "ritardo": "delay / lateness", "traffico": "traffic", "incredibile": "incredible",
    "aspettando": "waiting", "preoccupando": "worrying", "disastro": "disaster", "ordinare": "to order",
    "volentieri": "gladly", "perdonare": "to forgive", "metà": "half", "insisto": "I insist",
    "cappuccino": "cappuccino", "cornetto": "croissant", "crema": "cream", "parcheggio": "parking",
    "incubo": "nightmare", "lavoro": "work", "stress": "stress", "cinema": "cinema",
    "progetto": "project", "weekend": "weekend", "venerdì": "Friday", "pazienza": "patience",
    "dimenticato": "forgotten", "appuntamento": "appointment", "stamattina": "this morning",
    "rossi": "Rossi", "imprevisto": "unexpected event", "cognizione": "cognition / sense",
    "tempo": "time", "colpa": "fault", "fissare": "to schedule / fix", "giovedì": "Thursday",
    "disponibilità": "availability", "addebitarle": "to charge you", "costo": "cost",
    "comprensione": "understanding", "disturbo": "disturbance / inconvenience", "rumore": "noise",
    "cucina": "kitchen", "bicchiere": "glass", "sbaglio": "mistake", "distratto": "distracted",
    "scopa": "broom", "accaduto": "happened / event", "ospite": "guest", "vetri": "glass shards",
    "terra": "floor", "tagliarti": "to cut yourself", "paletta": "dustpan", "set": "set",
    "gentile": "kind", "vino": "wine", "mani": "hands", "spiritoso": "funny / witty",
    "arrabbiato": "angry", "amici": "friends", "incidenti": "incidents", "festa": "party",
    "compleanno": "birthday", "pessimo": "terrible / very bad", "messaggio": "message",
    "cena": "dinner", "speciale": "special", "ristorante": "restaurant", "centro": "center",
    "provare": "to try", "cuore": "heart", "perdonato": "forgiven", "sabato": "Saturday",
    "chiacchierare": "to chat", "calma": "calm", "festeggiare": "to celebrate", "regalo": "gift",
    "fantastico": "fantastic", "settimana": "week", "ehi": "hey", "tutto": "everything",
    "bene": "well / good", "grazie": "thanks", "mille": "a thousand", "prego": "you're welcome",
    "buongiorno": "good morning", "arrivederci": "goodbye", "ciao": "hi / bye", "pronto": "ready / hello"
}

# Create vocabulary.json
vocab_output = []
for i, v in enumerate(sorted_vocab):
    eng = vocab_map.get(v, "")
    if not eng: continue # Only keep words we have translations for or are significant
    
    others = [vocab_map[w] for w in vocab_map if w != v]
    distractors = random.sample(others, min(len(others), 3))
    choices = distractors + [eng]
    random.shuffle(choices)
    
    vocab_output.append({
        "id": f"v{i+1}",
        "italian": v,
        "english": eng,
        "choicesEnglish": choices
    })

# Common phrases relevant to scenario 77
common_phrases_list = [
    ("Scusa il ritardo", "Sorry for the delay"),
    ("Mi dispiace", "I'm sorry"),
    ("Nessun problema", "No problem"),
    ("Non ti preoccupare", "Don't worry"),
    ("Faccio io", "I'll do it / Let me do it"),
    ("Per favore", "Please"),
    ("Grazie mille", "Thank you very much"),
    ("Figurati", "Don't mention it / Not at all"),
    ("Va bene", "Alright / Okay"),
    ("D'accordo", "Agreed / Okay"),
    ("A presto", "See you soon"),
    ("Buona giornata", "Have a good day"),
    ("Tutto bene?", "Is everything okay?"),
    ("Hai ragione", "You're right"),
    ("Mi scusi", "Excuse me / I'm sorry (formal)"),
    ("Ci sono rimasto male", "I was hurt / disappointed"),
    ("È colpa mia", "It's my fault"),
    ("Mi sento in colpa", "I feel guilty"),
    ("Cin cin!", "Cheers!"),
    ("Tanti auguri", "Happy birthday / Best wishes")
]

# Create phrases.json
phrases_output = []
p_count = 1
for it, en in common_phrases_list:
    if it.lower() in all_extracted_text.lower():
        phrases_output.append({
            "id": f"p{p_count}",
            "italian": it,
            "english": en
        })
        p_count += 1

# Create sentences.json
sentences_output = []
for i, s in enumerate(sentences):
    sentences_output.append({
        "id": f"s{i+1}",
        "italian": s['italian'],
        "english": s['english']
    })

# Save files without prefixes
with open(os.path.join(scenario_path, 'vocabulary.json'), 'w', encoding='utf-8') as f:
    json.dump(vocab_output, f, indent=2, ensure_ascii=False)

with open(os.path.join(scenario_path, 'phrases.json'), 'w', encoding='utf-8') as f:
    json.dump(phrases_output, f, indent=2, ensure_ascii=False)

with open(os.path.join(scenario_path, 'sentences.json'), 'w', encoding='utf-8') as f:
    json.dump(sentences_output, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(vocab_output)} words, {len(phrases_output)} phrases, {len(sentences_output)} sentences.")
