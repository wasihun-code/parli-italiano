import json
import os

def main():
    path = "src/data/exports/dining/street_food/conversations.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Dictionary of translations for correct choices
    translations = {
        "Buongiorno! Vorrei un arancino al ragù, per favore. È molto caldo?": "Good morning! I'd like a ragù arancino, please. Is it very hot?",
        "Lo mangio subito qui in piedi, grazie. Mi serve solo un tovagliolo.": "I'll eat it right here standing up, thanks. I just need a napkin.",
        "Grazie mille, starò attento. Quanto costa in tutto l'arancino?": "Thank you very much, I'll be careful. How much is the arancino in total?",
        "No grazie, solo l'arancino. Ecco cinque euro. Tenga pure il resto.": "No thanks, just the arancino. Here are five euros. Keep the change.",
        "Scusi, un'ultima cosa. Avete anche dei dolci tipici qui?": "Excuse me, one last thing. Do you also have typical sweets here?",
        "Sì, ne vorrei uno, per favore. Sono con la ricotta?": "Yes, I'd like one, please. Are they with ricotta?",
        "Sembra perfetto. Lo prendo. Quanto costa il cannolo?": "Sounds perfect. I'll take it. How much is the cannolo?",
        "Sì, grazie, è un'ottima idea. Così mangio prima il salato.": "Yes, thanks, it's a great idea. That way I eat the salty one first.",
        "Ne ho ancora un paio, bastano quelli. Grazie mille.": "I still have a couple, those are enough. Thanks a lot.",
        "Grazie ancora, buona giornata e buon lavoro! A presto.": "Thanks again, have a nice day and good work! See you soon.",
        "Ciao! Vorrei una piadina con prosciutto crudo, squacquerone e rucola.": "Hi! I'd like a piadina with prosciutto crudo, squacquerone and arugula.",
        "La vorrei ben scaldata e croccante, per favore. Mi piace calda.": "I'd like it well heated and crispy, please. I like it hot.",
        "No, preferisco senza salse. Va bene così, con solo gli ingredienti.": "No, I prefer without sauces. It's fine like this, with only the ingredients.",
        "Ecco i sei euro. Posso avere un sacchetto per portarla via?": "Here are the six euros. Can I have a bag to take it away?",
        "Grazie! Avete anche qualcosa da bere? Ho cambiato idea.": "Thanks! Do you also have something to drink? I changed my mind.",
        "Prendo una birra piccola, per favore. È fresca?": "I'll have a small beer, please. Is it cold?",
        "Ecco tre euro. Tenga pure il resto.": "Here are three euros. Keep the change.",
        "La apra lei, per favore. Così la bevo subito.": "Open it for me, please. So I can drink it right away.",
        "Starò attento, non si preoccupi. Grazie del consiglio.": "I'll be careful, don't worry. Thanks for the advice.",
        "Grazie ancora, gentilissimo! Buona serata.": "Thanks again, very kind! Good evening.",
        "Era ottimo, grazie! Mi servirebbero dei tovaglioli puliti, per favore.": "It was excellent, thanks! I would need some clean napkins, please.",
        "Sì, grazie. Ho molta sete dopo il panino. Quanto costa l'acqua?": "Yes, thanks. I'm very thirsty after the sandwich. How much does the water cost?",
        "Sì, grazie mille. È molto gentile. Ecco l'euro per l'acqua.": "Yes, thank you very much. It's very kind. Here is the euro for the water.",
        "Perfetto, lo vedo. Butterò lì la bottiglia di plastica dopo.": "Perfect, I see it. I'll throw the plastic bottle in there later.",
        "Grazie! C'è un bagno pubblico qui vicino per lavarmi le mani?": "Thanks! Is there a public bathroom nearby to wash my hands?",
        "Buona idea, magari prendo un caffè veloce. Grazie per l'informazione.": "Good idea, maybe I'll have a quick coffee. Thanks for the information.",
        "Sì, molto buona! Dava un sapore speciale senza essere troppo forte.": "Yes, very good! It gave a special flavor without being too strong.",
        "Complimenti, si sente che è un prodotto artigianale.": "Compliments, you can tell it's an artisanal product.",
        "Sì, sono qui per qualche giorno. È una bellissima città.": "Yes, I'm here for a few days. It's a beautiful city.",
        "Certamente! Grazie ancora e buon lavoro.": "Certainly! Thanks again and good work.",
        "Ciao! Sì, volentieri. Non l'ho mai provata. È fatta con i ceci?": "Hi! Yes, gladly. I've never tried it. Is it made with chickpeas?",
        "Sì, grazie. Vorrei anche un po' di pepe nero sopra, se possibile.": "Yes, thanks. I'd also like some black pepper on top, if possible.",
        "La mangio camminando verso la piazza. Mi dà una forchetta?": "I'll eat it walking towards the square. Will you give me a fork?",
        "Ecco i quattro euro. Grazie per il consiglio, sembra buonissima!": "Here are the four euros. Thanks for the advice, it looks delicious!",
        "Scusi, che altri cibi locali mi consiglia di provare in città?": "Excuse me, what other local foods do you recommend I try in the city?",
        "Interessante! Ma si mangia calda o fredda?": "Interesting! But is it eaten hot or cold?",
        "Sembra deliziosa. La proverò domani a pranzo.": "Sounds delicious. I'll try it tomorrow at lunch.",
        "Grazie per il consiglio. Come si chiama il panificio?": "Thanks for the advice. What is the name of the bakery?",
        "Perfetto, me lo segno subito. Grazie mille per l'aiuto.": "Perfect, I'll write it down right away. Thanks a lot for the help.",
        "Lo farò sicuramente! Arrivederci e buona giornata!": "I will definitely do it! Goodbye and have a nice day!"
    }

    for conv in data["conversations"]:
        for msg in conv["messages"]:
            for choice in msg["choices"]:
                if choice["isCorrect"]:
                    text = choice["text"]
                    if text in translations:
                        choice["english"] = translations[text]
                    else:
                        print(f"Missing translation for: {text}")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
