import json
import os

scenario_path = './src/data/exports/daily_life/talking_to_a_neighbor'

# Vocabulary translation audit
with open(os.path.join(scenario_path, 'vocabulary.json'), 'r') as f:
    vocab = json.load(f)

missing_vocab = [v['italian'] for v in vocab if not v['english']]
if missing_vocab:
    print(f"Missing vocab translations: {len(missing_vocab)}")
    # I'll provide a mapping for these missing ones in the final application
else:
    print("All vocab translated.")

# Sentence translation audit
with open(os.path.join(scenario_path, 'sentences.json'), 'r') as f:
    sentences = json.load(f)

missing_sentences = [s['italian'] for s in sentences if not s['english']]
print(f"Missing sentence translations: {len(missing_sentences)}")

sentence_translations = {
    "Buongiorno! Sì, piacere, mi sono trasferito ieri.": "Good morning! Yes, nice to meet you, I moved in yesterday.",
    "Molto gentile, Mario. Io mi chiamo Marco, piacere.": "Very kind, Mario. My name is Marco, nice to meet you.",
    "Grazie! Sembra un bel condominio, molto pulito.": "Thanks! It looks like a nice building, very clean.",
    "Sì, le ho ricevute. La mia cassetta è quella con il mio nome.": "Yes, I received them. My mailbox is the one with my name.",
    "Grazie mille! Qual è il giorno in cui puliscono le scale?": "Thank you very much! Which day do they clean the stairs?",
    "Capito, non lascerò niente sul pianerottolo. Grazie per l'avviso.": "Understood, I won't leave anything on the landing. Thanks for the notice.",
    "Ah, bene. Spero che l'appartamento sia caldo in inverno.": "Ah, good. I hope the apartment is warm in winter.",
    "Spero di non averne bisogno, ma è utile saperlo. Grazie Mario.": "I hope I won't need it, but it's useful to know. Thanks Mario.",
    "Non ancora, andrò a vederlo domani. Sembra perfetto.": "Not yet, I'll go see it tomorrow. It seems perfect.",
    "Piacere mio, Mario! Buona giornata e a presto.": "My pleasure, Mario! Have a good day and see you soon.",
    "Salve! Sì, grazie. Dove sono i bidoni della differenziata?": "Hi! Yes, thanks. Where are the recycling bins?",
    "Non sono sicuro. Qual è il bidone per la plastica?": "I'm not sure. Which is the bin for plastic?",
    "Capito. Giallo plastica, blu carta e verde vetro. Grazie!": "Understood. Yellow plastic, blue paper, and green glass. Thanks!",
    "Ah, c'è un calendario per la raccolta? Dove posso trovarlo?": "Ah, is there a collection calendar? Where can I find it?",
    "Ottima idea. E per le pile scariche o le lampadine?": "Great idea. And for dead batteries or lightbulbs?",
    "Ah, capisco. È importante non inquinare.": "Ah, I see. It's important not to pollute.",
    "Va bene. Vengono a prenderli a casa?": "Alright. Do they come to pick them up at the house?",
    "Grazie, ora vado a buttare questi sacchetti di carta.": "Thanks, now I'm going to throw away these paper bags.",
    "Sì, ne ho comprati un pacco ieri al supermercato.": "Yes, I bought a pack yesterday at the supermarket.",
    "Grazie mille per la pazienza. Buona serata a lei!": "Thank you very much for your patience. Good evening to you!",
    "Buonasera! Mi dica pure, c'è qualche problema?": "Good evening! Please tell me, is there a problem?",
    "Oh, mi scusi tanto! Non pensavo si sentisse così forte.": "Oh, I'm so sorry! I didn't think it could be heard so loudly.",
    "La capisco perfettamente. Abbasso subito il volume, scusi ancora.": "I understand you perfectly. I'll lower the volume right away, sorry again.",
    "Non lo sapevo, starò più attento in futuro. Userò le cuffie.": "I didn't know, I'll be more careful in the future. I'll use headphones.",
    "Sì, così posso ascoltare quello che voglio senza disturbare.": "Yes, so I can listen to what I want without disturbing.",
    "Starò attento anche a quello, meglio usare le pantofole.": "I'll be careful with that too, better to use slippers.",
    "Sono d'accordo. Il buon vicinato è molto importante.": "I agree. Good neighborly relations are very important.",
    "Grazie dell'invito. A che ora è la riunione?": "Thanks for the invitation. What time is the meeting?",
    "Cercherò di esserci. Grazie per l'informazione.": "I'll try to be there. Thanks for the information.",
    "Buonanotte a lei e scusi ancora. A domani!": "Goodnight to you and sorry again. See you tomorrow!",
    "Salve! Abbastanza bene, ma devo ancora scoprire i negozi vicini.": "Hi! Pretty well, but I still have to discover the nearby shops.",
    "Sì, vorrei sapere se c'è un buon panettiere qui vicino.": "Yes, I'd like to know if there's a good baker nearby.",
    "Ottimo! È aperto anche la domenica mattina?": "Great! Is it open on Sunday morning too?",
    "Perfetto. E per la spesa più grande? C'è un supermercato?": "Perfect. And for larger shopping? Is there a supermarket?",
    "Bene, così non devo usare la macchina. È aperto fino a tardi?": "Good, so I don't have to use the car. Is it open until late?",
    "Capito. Sa se c'è anche una farmacia qui vicino?": "Understood. Do you know if there's also a pharmacy nearby?",
    "Piazza Garibaldi, d'accordo. È una zona molto centrale allora.": "Piazza Garibaldi, alright. It's a very central area then.",
    "Buono a sapersi! Mi piace fare colazione fuori ogni tanto.": "Good to know! I like having breakfast out every now and then.",
    "Hanno prodotti locali? Mi piace comprare cose fresche.": "Do they have local products? I like buying fresh things.",
    "Grazie mille per tutti i consigli! Buona giornata.": "Thank you very much for all the tips! Have a good day."
}

for s in sentences:
    if not s['english']:
        if s['italian'] in sentence_translations:
            s['english'] = sentence_translations[s['italian']]
        else:
            print(f"STILL MISSING: {s['italian']}")

with open(os.path.join(scenario_path, 'sentences.json'), 'w') as f:
    json.dump(sentences, f, indent=2)

print("Applied sentence translations.")
