import json
import os

file_path = 'src/data/exports/culture/sports_match/culture_sports_match_phrases.json'

phrase_translations = {
    "Ah, il derby! Lo stadio è grandissimo, vero? È molto lontano?": "Ah, the derby! The stadium is huge, right? Is it very far?",
    "Ah, peccato. Allora pago in contanti. Ecco venti euro.": "Ah, too bad. Then I'll pay in cash. Here are twenty euros.",
    "Arrivederci e buona partita! Finalmente mi siedo.": "Goodbye and have a good match! Finally I'm sitting down.",
    "Assolutamente sì. È stato un intervento molto duro.": "Absolutely yes. It was a very hard tackle.",
    "Bellissimo! Che emozione. Tutto lo stadio sta urlando.": "Beautiful! What an emotion. The whole stadium is shouting.",
    "Capito, settore 4. Dove si trova? Devo salire le scale?": "Understood, sector 4. Where is it? Do I have to go up the stairs?",
    "Certamente, ecco il mio biglietto. Dove devo andare?": "Certainly, here is my ticket. Where should I go?",
    "Due tovaglioli extra, grazie. Siamo molto di fretta.": "Two extra napkins, please. We are in a great hurry.",
    "Fammi vedere... Ah, io ho il settore B, lei ha il C!": "Let me see... Ah, I have sector B, she has C!",
    "Fila 12, perfetto. E il numero del mio posto qual è?": "Row 12, perfect. And what is my seat number?",
    "Grazie mille, gentilissimo! Andiamo di corsa allora.": "Thanks a lot, very kind! Let's go quickly then.",
    "Grazie, scotta molto? Lo prendo con un tovagliolo.": "Thanks, is it very hot? I'll take it with a napkin.",
    "Grazie. Quanto costa in tutto? Pago con la carta.": "Thanks. How much is it in total? I'm paying by card.",
    "Ha ragione, erano tutti fermi. Che errore grave!": "You're right, they were all still. What a serious mistake!",
    "Hai ragione, andiamo! Prendiamo l'autobus o andiamo a piedi?": "You're right, let's go! Should we take the bus or walk?",
    "Hai ragione, è incredibile! L'arbitro è molto scarso.": "You're right, it's incredible! The referee is very poor.",
    "Lo so, è una partita importante. Dobbiamo stare attenti.": "I know, it's an important match. We have to be careful.",
    "Lui vorrebbe un'acqua naturale e delle patatine.": "He would like a still water and some chips.",
    "Mamma mia, che gol! Ha tirato sotto l'incrocio!": "My goodness, what a goal! He shot right under the crossbar!",
    "Nessun problema, succede. Buona partita nel settore C!": "No problem, it happens. Have a good match in sector C!",
    "Oh, mi scusi. Mi fa vedere il suo biglietto, per favore?": "Oh, excuse me. Can you show me your ticket, please?",
    "Ottimo, grazie. C'è molta tensione oggi tra i tifosi.": "Great, thanks. There is a lot of tension today among the fans.",
    "Prego! Goditi la partita. Forza Roma, speriamo bene!": "You're welcome! Enjoy the match. Go Roma, let's hope for the best!",
    "Scaldato, grazie. Mi piace il pane caldo e croccante.": "Warmed up, thanks. I like warm and crunchy bread.",
    "Speriamo! Grazie mille e buona serata. Arrivederci!": "Let's hope! Thanks a lot and have a good evening. Goodbye!",
    "Spero di no! Guardo il guardalinee... no, è gol!": "I hope not! I'm looking at the linesman... no, it's a goal!",
    "Sì, al cento per cento. Possiamo entrare senza problemi.": "Yes, one hundred percent. We can enter without any problems.",
    "Sì, andiamo subito. C'è molta gente e molta fila.": "Yes, let's go right away. There are many people and a long line.",
    "Sì, ce l'ho! È nello zaino. Sono pronto per tifare la Roma.": "Yes, I have it! It's in the backpack. I'm ready to cheer for Roma.",
    "Sì, certo! Per quale squadra tifi? Non mi ricordo più.": "Yes, sure! Which team do you cheer for? I don't remember anymore.",
    "Sì, dobbiamo tornare subito al nostro posto numerato.": "Yes, we have to go back to our numbered seat immediately.",
    "Sì, le vedo! Che emozione. Forza Roma, andiamo a vincere!": "Yes, I see them! What an emotion. Go Roma, let's go win!",
    "Sì, li ho controllati stamattina. Sono posti numerati.": "Yes, I checked them this morning. They are numbered seats.",
    "Sì, mancano solo due minuti. Dobbiamo stare calmi.": "Yes, only two minutes left. We have to stay calm.",
    "Sì, saliamo. Spero che non ci sia troppa gente a bordo.": "Yes, let's get on. I hope there aren't too many people on board.",
    "Sì, velocissimi! Speriamo che facciano un bel cross.": "Yes, very fast! Let's hope they make a nice cross.",
    "Sì, è proprio dietro la curva. Deve tornare indietro.": "Yes, it's right behind the curve. You have to go back.",
    "Tutto chiaro, grazie mille. Fila 12, posto 8. Vado!": "All clear, thanks a lot. Row 12, seat 8. I'm going!",
    "Va bene, così vediamo la città. Quanto manca allo stadio?": "Okay, so we can see the city. How much longer to the stadium?",
    "Vorrei una birra media e un panino con il salame.": "I would like a medium beer and a salami sandwich."
}

with open(file_path, 'r', encoding='utf-8') as f:
    items = json.load(f)

updated_count = 0
missing_phrases = []
for item in items:
    if not item.get("english"):
        it = item["italian"].strip()
        if it in phrase_translations:
            item["english"] = phrase_translations[it]
            updated_count += 1
        else:
            missing_phrases.append(it)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

print(f"Updated {updated_count} translations.")
if missing_phrases:
    print(f"Still missing {len(missing_phrases)} translations: {missing_phrases}")
else:
    print("All translations filled!")
