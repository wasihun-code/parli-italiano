
import json

file_path = '/home/waseageru/parli-italiano/src/data/exports/daily_life/talking_to_a_neighbor/daily_life_talking_to_a_neighbor_phrases.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

translations = {
    "Ah, bene. Spero che l'appartamento sia caldo in inverno.": "Ah, good. I hope the apartment is warm in winter.",
    "Ah, capisco. È importante non inquinare.": "Ah, I see. It is important not to pollute.",
    "Bene, così non devo usare la macchina. È aperto fino a tardi?": "Good, so I don't have to use the car. Is it open until late?",
    "Buonanotte a lei e scusi ancora. A domani!": "Goodnight to you and sorry again. See you tomorrow!",
    "Buono a sapersi! Mi piace fare colazione fuori ogni tanto.": "Good to know! I like having breakfast out every now and then.",
    "Capito, non lascerò niente sul pianerottolo. Grazie per l'avviso.": "Understood, I won't leave anything on the landing. Thanks for the notice.",
    "Capito. Sa se c'è anche una farmacia qui vicino?": "Understood. Do you know if there is also a pharmacy nearby?",
    "Cercherò di esserci. Grazie per l'informazione.": "I'll try to be there. Thanks for the information.",
    "Grazie dell'invito. A che ora è la riunione?": "Thanks for the invitation. What time is the meeting?",
    "Grazie mille per la pazienza. Buona serata a lei!": "Thank you very much for the patience. Good evening to you!",
    "Grazie mille per tutti i consigli! Buona giornata.": "Thank you very much for all the advice! Have a good day.",
    "Grazie mille! Qual è il giorno in cui puliscono le scale?": "Thank you very much! Which day do they clean the stairs?",
    "Grazie, ora vado a buttare questi sacchetti di carta.": "Thanks, now I'm going to throw away these paper bags.",
    "Hanno prodotti locali? Mi piace comprare cose fresche.": "Do they have local products? I like to buy fresh things.",
    "Non ancora, andrò a vederlo domani. Sembra perfetto.": "Not yet, I will go see it tomorrow. It seems perfect.",
    "Non lo sapevo, starò più attento in futuro. Userò le cuffie.": "I didn't know, I'll be more careful in the future. I'll use headphones.",
    "Ottima idea. E per le pile scariche o le lampadine?": "Great idea. And for the dead batteries or light bulbs?",
    "Perfetto. E per la spesa più grande? C'è un supermercato?": "Perfect. And for larger shopping? Is there a supermarket?",
    "Piacere mio, Mario! Buona giornata e a presto.": "My pleasure, Mario! Have a good day and see you soon.",
    "Piazza Garibaldi, d'accordo. È una zona molto centrale allora.": "Piazza Garibaldi, okay. It's a very central area then.",
    "Sono d'accordo. Il buon vicinato è molto importante.": "I agree. Good neighborly relations are very important.",
    "Spero di non averne bisogno, ma è utile saperlo. Grazie Mario.": "I hope I don't need it, but it's useful to know. Thanks Mario.",
    "Starò attento anche a quello, meglio usare le pantofole.": "I'll be careful with that too, it's better to use slippers.",
    "Sì, così posso ascoltare quello che voglio senza disturbare.": "Yes, so I can listen to what I want without disturbing.",
    "Sì, ne ho comprati un pacco ieri al supermercato.": "Yes, I bought a pack yesterday at the supermarket.",
    "Va bene. Vengono a prenderli a casa?": "Okay. Do they come to pick them up at home?"
}

updated_count = 0
for item in data:
    if item['english'] == "":
        italian = item['italian']
        if italian in translations:
            item['english'] = translations[italian]
            updated_count += 1
        else:
            print(f"Warning: No translation found for '{italian}'")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Updated {updated_count} translations.")
