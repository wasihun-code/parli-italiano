import json

mapping = {
    "A dopo allora, buona serata anche a te!": "See you later then, good evening to you too!",
    "Buongiorno, sono Luca. Vorrei parlare con Paolo.": "Good morning, this is Luca. I would like to speak with Paolo.",
    "Capisco. È in casa o è uscito adesso?": "I understand. Is he at home or has he gone out now?",
    "Certamente, non vedo l'ora di vederti.": "Certainly, I can't wait to see you.",
    "Che bello! Spero che ci sia il sole.": "How nice! I hope it's sunny.",
    "Ciao Giulia, sono io. Ti ho chiamato ora.": "Hi Giulia, it's me. I just called you now.",
    "D'accordo, alle cinque in piazza va bene.": "Agreed, five o'clock in the square is fine.",
    "D'accordo, vicino alla fontana alle otto.": "Agreed, near the fountain at eight o'clock.",
    "D'accordo. Posso richiamare più tardi allora?": "Agreed. Can I call back later then?",
    "Ero occupato stamattina, ma ora sono libero.": "I was busy this morning, but now I'm free.",
    "Grazie ancora e buona giornata anche a Lei!": "Thanks again and have a good day to you too!",
    "Grazie mille, è molto gentile da parte Sua.": "Thank you very much, that is very kind of you.",
    "Grazie, ma conosco bene la strada. A dopo!": "Thanks, but I know the way well. See you later!",
    "Hai ragione, proverò a scrivergli un messaggio.": "You're right, I'll try to write him a message.",
    "Hai ragione, è facile trovarsi lì.": "You're right, it's easy to meet there.",
    "No, grazie. Voglio riattaccare ora. Ciao.": "No, thanks. I want to hang up now. Bye.",
    "No, il messaggio mi sembra chiaro. Grazie.": "No, the message seems clear to me. Thanks.",
    "No, non ho finito. Volevo anche dirti una cosa.": "No, I haven't finished. I also wanted to tell you something.",
    "No, non voglio riascoltare. Va bene così.": "No, I don't want to listen again. It's fine like this.",
    "Non ti preoccupare, io ti aspetto lì.": "Don't worry, I'll wait for you there.",
    "Oh, scusa. Comunque il mio numero lo hai.": "Oh, sorry. Anyway, you have my number.",
    "Ottima idea, il parco è molto grande.": "Great idea, the park is very large.",
    "Ottimo. Spero che Giulia lo senta presto.": "Excellent. I hope Giulia hears it soon.",
    "Sì, ho il suo numero. Ma non rispondeva prima.": "Yes, I have his number. But he wasn't answering before.",
    "Sì, la conosco bene. Ci vediamo lì allora.": "Yes, I know it well. See you there then.",
    "Sì, la ricordo bene. Prendo l'autobus.": "Yes, I remember it well. I'll take the bus.",
    "Sì, mi piacerebbe molto fare una passeggiata.": "Yes, I would really like to go for a walk.",
    "Va bene, a domani Marco. Ciao!": "Alright, see you tomorrow Marco. Bye!",
    "Va bene, alle otto in piazza è perfetto.": "Alright, eight o'clock in the square is perfect.",
    "Va bene, aspetterò la sua chiamata allora.": "Alright, I'll wait for his call then.",
    "Va bene, non voglio disturbarlo allora.": "Alright, I don't want to disturb him then.",
    "Va bene, premo tre per inviare il messaggio.": "Alright, I'll press three to send the message.",
    "Va bene, ti chiamo se non trovo la fontana.": "Alright, I'll call you if I don't find the fountain.",
    "Va bene. Spero che tu possa richiamarmi.": "Alright. I hope you can call me back.",
    "Volevo chiederti se stasera sei libera.": "I wanted to ask you if you are free tonight."
}

file_path = 'src/data/exports/social/phone_call/social_phone_call_phrases.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for item in data:
    if not item['english'] and item['italian'] in mapping:
        item['english'] = mapping[item['italian']]
        count += 1

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated {count} phrase translations.")
