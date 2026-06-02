import json

scenario_id = 39

def make_convo(id_, title, desc, turns_data):
    messages = []
    for i, t in enumerate(turns_data):
        msg = {
            "id": f"m{i+1}",
            "role": "host",
            "text": t["host_it"],
            "english": t["host_en"],
            "choices": [
                {
                    "text": t["correct_it"],
                    "english": t["correct_en"],
                    "isCorrect": True
                },
                {
                    "text": t["d1_it"],
                    "english": t["d1_en"],
                    "isCorrect": False
                },
                {
                    "text": t["d2_it"],
                    "english": t["d2_en"],
                    "isCorrect": False
                }
            ]
        }
        messages.append(msg)
    return {
        "id": id_,
        "title": title,
        "description": desc,
        "messages": messages
    }

conv1 = [
    {
        "host_it": "Buongiorno! Benvenuti al corso di cucina italiana.",
        "host_en": "Good morning! Welcome to the Italian cooking class.",
        "correct_it": "Buongiorno! Sono molto felice di essere qui oggi.",
        "correct_en": "Good morning! I am very happy to be here today.",
        "d1_it": "Buongiorno! Devo andare al supermercato adesso.",
        "d1_en": "Good morning! I have to go to the supermarket now.",
        "d2_it": "Buongiorno! Ho mangiato una pizza molto grande.",
        "d2_en": "Good morning! I ate a very large pizza."
    },
    {
        "host_it": "Oggi impariamo a fare la pasta fresca. Siete pronti?",
        "host_en": "Today we learn to make fresh pasta. Are you ready?",
        "correct_it": "Sì, siamo pronti. Cosa dobbiamo fare prima?",
        "correct_en": "Yes, we are ready. What do we have to do first?",
        "d1_it": "No, non vogliamo fare la pasta in casa.",
        "d1_en": "No, we don't want to make pasta at home.",
        "d2_it": "Forse, ma preferisco guardare un film.",
        "d2_en": "Maybe, but I prefer to watch a movie."
    },
    {
        "host_it": "Prima di tutto, dobbiamo lavare bene le mani.",
        "host_en": "First of all, we have to wash our hands well.",
        "correct_it": "Certo, vado subito a lavarmi le mani.",
        "correct_en": "Sure, I'll go wash my hands right away.",
        "d1_it": "Certo, voglio comprare una bottiglia d'acqua.",
        "d1_en": "Sure, I want to buy a bottle of water.",
        "d2_it": "Certo, preferisco mangiare al ristorante stasera.",
        "d2_en": "Sure, I prefer to eat at the restaurant tonight."
    },
    {
        "host_it": "Perfetto. Ora mettete il grembiule da cucina.",
        "host_en": "Perfect. Now put on your kitchen apron.",
        "correct_it": "Va bene. Il mio grembiule è qui sul tavolo.",
        "correct_en": "Alright. My apron is here on the table.",
        "d1_it": "Va bene. La mia giacca è nella mia camera.",
        "d1_en": "Alright. My jacket is in my room.",
        "d2_it": "Va bene. Le mie scarpe sono molto comode.",
        "d2_en": "Alright. My shoes are very comfortable."
    },
    {
        "host_it": "Molto bene. Conoscete già gli ingredienti per la pasta?",
        "host_en": "Very good. Do you already know the ingredients for pasta?",
        "correct_it": "Penso di sì. Farina, uova e un po' di sale.",
        "correct_en": "I think so. Flour, eggs, and a little salt.",
        "d1_it": "Penso di sì. Pomodori, carne e un po' di pepe.",
        "d1_en": "I think so. Tomatoes, meat, and a little pepper.",
        "d2_it": "Penso di sì. Patate, cipolle e un po' di zucchero.",
        "d2_en": "I think so. Potatoes, onions, and a little sugar."
    },
    {
        "host_it": "Esatto! Siete già dei bravi cuochi. Iniziamo?",
        "host_en": "Exactly! You are already good cooks. Shall we begin?",
        "correct_it": "Sì, iniziamo. Prendo la farina dal sacchetto.",
        "correct_en": "Yes, let's start. I'll get the flour from the bag.",
        "d1_it": "Sì, iniziamo. Bevo un bicchiere di latte freddo.",
        "d1_en": "Yes, let's start. I'll drink a glass of cold milk.",
        "d2_it": "Sì, iniziamo. Mangio un panino con il formaggio.",
        "d2_en": "Yes, let's start. I'll eat a sandwich with cheese."
    },
    {
        "host_it": "Mettete la farina sul tavolo, come una fontana.",
        "host_en": "Put the flour on the table, like a fountain.",
        "correct_it": "Così va bene? Ho fatto un buco al centro.",
        "correct_en": "Is this okay? I made a hole in the center.",
        "d1_it": "Così va bene? Ho bevuto molta acqua oggi.",
        "d1_en": "Is this okay? I drank a lot of water today.",
        "d2_it": "Così va bene? Ho lavato tutti i piatti sporchi.",
        "d2_en": "Is this okay? I washed all the dirty dishes."
    },
    {
        "host_it": "Bravissimi. Ora rompete le uova dentro la farina.",
        "host_en": "Great job. Now break the eggs into the flour.",
        "correct_it": "D'accordo. Quante uova dobbiamo usare per questa ricetta?",
        "correct_en": "Alright. How many eggs should we use for this recipe?",
        "d1_it": "D'accordo. Quanti biglietti dobbiamo comprare per il treno?",
        "d1_en": "Alright. How many tickets should we buy for the train?",
        "d2_it": "D'accordo. Quante persone arrivano domani mattina presto?",
        "d2_en": "Alright. How many people are arriving early tomorrow morning?"
    },
    {
        "host_it": "Usiamo tre uova per questa quantità di farina.",
        "host_en": "We use three eggs for this amount of flour.",
        "correct_it": "Capito. Rompo le uova una alla volta qui dentro.",
        "correct_en": "Understood. I break the eggs one by one in here.",
        "d1_it": "Capito. Mangio le uova con un po' di pane.",
        "d1_en": "Understood. I eat the eggs with some bread.",
        "d2_it": "Capito. Compro le uova al supermercato domani mattina.",
        "d2_en": "Understood. I buy the eggs at the supermarket tomorrow morning."
    },
    {
        "host_it": "Perfetto. Adesso siete pronti per la prossima parte.",
        "host_en": "Perfect. Now you are ready for the next part.",
        "correct_it": "Fantastico! Non vedo l'ora di imparare il resto.",
        "correct_en": "Fantastic! I can't wait to learn the rest.",
        "d1_it": "Fantastico! Non voglio pulire la cucina dopo questo.",
        "d1_en": "Fantastic! I don't want to clean the kitchen after this.",
        "d2_it": "Fantastico! Non mi piace per niente la pasta fresca.",
        "d2_en": "Fantastic! I don't like fresh pasta at all."
    }
]

conv2 = [
    {
        "host_it": "Ora dobbiamo mescolare le uova con la farina.",
        "host_en": "Now we have to mix the eggs with the flour.",
        "correct_it": "Uso una forchetta o uso le mani per mescolare?",
        "correct_en": "Do I use a fork or do I use my hands to mix?",
        "d1_it": "Uso un cucchiaio o uso un coltello per tagliare?",
        "d1_en": "Do I use a spoon or do I use a knife to cut?",
        "d2_it": "Uso una pentola o uso una padella per cuocere?",
        "d2_en": "Do I use a pot or do I use a pan to cook?"
    },
    {
        "host_it": "Iniziate con la forchetta, poi usate le mani.",
        "host_en": "Start with the fork, then use your hands.",
        "correct_it": "Va bene, mescolo le uova e aggiungo la farina piano piano.",
        "correct_en": "Okay, I mix the eggs and add the flour slowly.",
        "d1_it": "Va bene, mangio le uova e lascio la farina qui.",
        "d1_en": "Okay, I eat the eggs and leave the flour here.",
        "d2_it": "Va bene, cucino le uova e preparo un dolce oggi.",
        "d2_en": "Okay, I cook the eggs and prepare a dessert today."
    },
    {
        "host_it": "Esatto. Bisogna impastare per almeno dieci minuti.",
        "host_en": "Exactly. You need to knead for at least ten minutes.",
        "correct_it": "È un po' faticoso, ma l'impasto prende forma.",
        "correct_en": "It's a bit tiring, but the dough is taking shape.",
        "d1_it": "È un po' noioso, ma il libro è molto interessante.",
        "d1_en": "It's a bit boring, but the book is very interesting.",
        "d2_it": "È un po' freddo, ma il sole splende nel cielo.",
        "d2_en": "It's a bit cold, but the sun is shining in the sky."
    },
    {
        "host_it": "Sì, ci vuole forza! L'impasto deve essere liscio.",
        "host_en": "Yes, it takes strength! The dough must be smooth.",
        "correct_it": "Il mio impasto è ancora un po' duro. Cosa faccio?",
        "correct_en": "My dough is still a bit hard. What do I do?",
        "d1_it": "Il mio telefono è ancora spento. Dove lo metto?",
        "d1_en": "My phone is still off. Where do I put it?",
        "d2_it": "Il mio viaggio è ancora lungo. Quando arriviamo lì?",
        "d2_en": "My trip is still long. When do we get there?"
    },
    {
        "host_it": "Aggiungi un cucchiaio di acqua e continua a impastare.",
        "host_en": "Add a tablespoon of water and continue kneading.",
        "correct_it": "Grazie per l'aiuto. Ora è molto più morbido.",
        "correct_en": "Thanks for the help. Now it's much softer.",
        "d1_it": "Grazie per l'acqua. Ora ho molta meno sete.",
        "d1_en": "Thanks for the water. Now I'm much less thirsty.",
        "d2_it": "Grazie per il libro. Ora posso leggere di più.",
        "d2_en": "Thanks for the book. Now I can read more."
    },
    {
        "host_it": "Perfetto. Ora facciamo una palla con l'impasto.",
        "host_en": "Perfect. Now let's make a ball with the dough.",
        "correct_it": "Fatto. Devo coprire l'impasto con un panno pulito?",
        "correct_en": "Done. Do I have to cover the dough with a clean cloth?",
        "d1_it": "Fatto. Devo tagliare l'impasto con un coltello sporco?",
        "d1_en": "Done. Do I have to cut the dough with a dirty knife?",
        "d2_it": "Fatto. Devo mettere l'impasto nel frigorifero adesso?",
        "d2_en": "Done. Do I have to put the dough in the fridge now?"
    },
    {
        "host_it": "Sì, esatto. Deve riposare per circa mezz'ora.",
        "host_en": "Yes, exactly. It must rest for about half an hour.",
        "correct_it": "Mentre riposa, cosa prepariamo? Il sugo al pomodoro?",
        "correct_en": "While it rests, what do we prepare? The tomato sauce?",
        "d1_it": "Mentre riposa, andiamo a dormire in camera da letto?",
        "d1_en": "While it rests, do we go to sleep in the bedroom?",
        "d2_it": "Mentre riposa, ascoltiamo la radio in salotto insieme?",
        "d2_en": "While it rests, do we listen to the radio in the living room together?"
    },
    {
        "host_it": "Proprio così. Puliamo il tavolo prima di iniziare.",
        "host_en": "That's right. Let's clean the table before starting.",
        "correct_it": "Prendo io una spugna per pulire tutto il tavolo.",
        "correct_en": "I'll take a sponge to clean the whole table.",
        "d1_it": "Prendo io una sedia per sedermi a leggere un libro.",
        "d1_en": "I'll take a chair to sit and read a book.",
        "d2_it": "Prendo io una borsa per mettere la mia spesa dentro.",
        "d2_en": "I'll take a bag to put my groceries in."
    },
    {
        "host_it": "Ottimo lavoro di squadra. Il tavolo è di nuovo pulito.",
        "host_en": "Great teamwork. The table is clean again.",
        "correct_it": "Siamo pronti per preparare un sugo delizioso e saporito.",
        "correct_en": "We are ready to prepare a delicious and flavorful sauce.",
        "d1_it": "Siamo pronti per andare al cinema a guardare un film.",
        "d1_en": "We are ready to go to the cinema to watch a movie.",
        "d2_it": "Siamo pronti per fare una passeggiata nel parco vicino.",
        "d2_en": "We are ready to take a walk in the nearby park."
    },
    {
        "host_it": "Andiamo ai fornelli. Ognuno prenda una piccola padella.",
        "host_en": "Let's go to the stove. Everyone take a small pan.",
        "correct_it": "Ho preso la mia padella. Sono pronto a cucinare.",
        "correct_en": "I got my pan. I am ready to cook.",
        "d1_it": "Ho preso il mio ombrello. Sono pronto a uscire fuori.",
        "d1_en": "I got my umbrella. I am ready to go outside.",
        "d2_it": "Ho preso il mio zaino. Sono pronto a studiare adesso.",
        "d2_en": "I got my backpack. I am ready to study now."
    }
]

conv3 = [
    {
        "host_it": "Per il sugo ci servono pomodori freschi, aglio e basilico.",
        "host_en": "For the sauce we need fresh tomatoes, garlic and basil.",
        "correct_it": "Devo tagliare i pomodori a piccoli pezzi?",
        "correct_en": "Should I cut the tomatoes into small pieces?",
        "d1_it": "Devo comprare le mele al supermercato oggi?",
        "d1_en": "Should I buy apples at the supermarket today?",
        "d2_it": "Devo mettere i vestiti nella lavatrice ora?",
        "d2_en": "Should I put the clothes in the washing machine now?"
    },
    {
        "host_it": "Sì, piccoli pezzi. Prima mettiamo l'olio nella padella.",
        "host_en": "Yes, small pieces. First we put oil in the pan.",
        "correct_it": "Quanto olio devo usare per il nostro sugo?",
        "correct_en": "How much oil should I use for our sauce?",
        "d1_it": "Quanta acqua devo bere durante la giornata?",
        "d1_en": "How much water should I drink during the day?",
        "d2_it": "Quanti soldi devo portare in banca domani?",
        "d2_en": "How much money should I bring to the bank tomorrow?"
    },
    {
        "host_it": "Due cucchiai vanno bene. Poi aggiungi uno spicchio d'aglio.",
        "host_en": "Two tablespoons are fine. Then add a clove of garlic.",
        "correct_it": "Ho messo l'aglio. Accendo il fuoco sotto la padella?",
        "correct_en": "I put the garlic. Do I turn on the heat under the pan?",
        "d1_it": "Ho messo la giacca. Apro la porta per uscire?",
        "d1_en": "I put the jacket on. Do I open the door to go out?",
        "d2_it": "Ho messo la musica. Accendo la televisione adesso?",
        "d2_en": "I put the music on. Do I turn on the television now?"
    },
    {
        "host_it": "Sì, fuoco basso. Attenzione a non bruciare l'aglio!",
        "host_en": "Yes, low heat. Careful not to burn the garlic!",
        "correct_it": "L'aglio è dorato. Posso aggiungere i pomodori tagliati?",
        "correct_en": "The garlic is golden. Can I add the chopped tomatoes?",
        "d1_it": "Il pane è pronto. Posso preparare un bel panino?",
        "d1_en": "The bread is ready. Can I prepare a nice sandwich?",
        "d2_it": "Il caffè è caldo. Posso bere una tazza subito?",
        "d2_en": "The coffee is hot. Can I drink a cup right away?"
    },
    {
        "host_it": "Certamente, mettili in padella. E aggiungi un po' di sale.",
        "host_en": "Certainly, put them in the pan. And add a little salt.",
        "correct_it": "Sugo quasi pronto. Aggiungo anche un po' di pepe nero?",
        "correct_en": "Sauce almost ready. Should I also add a little black pepper?",
        "d1_it": "Zuppa quasi fredda. Aggiungo anche un po' di ghiaccio freddo?",
        "d1_en": "Soup almost cold. Should I also add a little cold ice?",
        "d2_it": "Latte quasi finito. Aggiungo anche un po' di zucchero bianco?",
        "d2_en": "Milk almost finished. Should I also add a little white sugar?"
    },
    {
        "host_it": "Se ti piace il pepe, certo! Ora copri la padella.",
        "host_en": "If you like pepper, sure! Now cover the pan.",
        "correct_it": "Va bene. Quanto tempo deve cuocere il sugo?",
        "correct_en": "Alright. How long does the sauce need to cook?",
        "d1_it": "Va bene. Quanto tempo devo studiare la lezione?",
        "d1_en": "Alright. How long do I have to study the lesson?",
        "d2_it": "Va bene. Quanto tempo dobbiamo aspettare il treno?",
        "d2_en": "Alright. How long do we have to wait for the train?"
    },
    {
        "host_it": "Circa quindici minuti. Non dimenticare di mescolare ogni tanto.",
        "host_en": "About fifteen minutes. Don't forget to stir occasionally.",
        "correct_it": "Mescolo subito. Il profumo del pomodoro è buonissimo!",
        "correct_en": "I'll stir right away. The smell of the tomato is very good!",
        "d1_it": "Mangio subito. Il sapore della pizza è fantastico!",
        "d1_en": "I eat right away. The taste of the pizza is fantastic!",
        "d2_it": "Dormo subito. Il letto della camera è comodissimo!",
        "d2_en": "I sleep right away. The bed in the room is very comfortable!"
    },
    {
        "host_it": "Alla fine aggiungiamo il basilico fresco spezzato con le mani.",
        "host_en": "At the end we add fresh basil torn with our hands.",
        "correct_it": "Ho capito. Il basilico dà molto sapore al sugo.",
        "correct_en": "I understand. Basil gives a lot of flavor to the sauce.",
        "d1_it": "Ho capito. La pioggia fa crescere i fiori belli.",
        "d1_en": "I understand. The rain makes beautiful flowers grow.",
        "d2_it": "Ho capito. Il vento porta via tutte le nuvole.",
        "d2_en": "I understand. The wind blows away all the clouds."
    },
    {
        "host_it": "Esattamente. Ora spegni il fuoco. Il sugo è pronto.",
        "host_en": "Exactly. Now turn off the heat. The sauce is ready.",
        "correct_it": "Fatto. Adesso dobbiamo stendere l'impasto e tagliare la pasta?",
        "correct_en": "Done. Now do we have to roll out the dough and cut the pasta?",
        "d1_it": "Fatto. Adesso dobbiamo pulire la casa e lavare tutto?",
        "d1_en": "Done. Now do we have to clean the house and wash everything?",
        "d2_it": "Fatto. Adesso dobbiamo chiamare il medico e andare lì?",
        "d2_en": "Done. Now do we have to call the doctor and go there?"
    },
    {
        "host_it": "Esatto! Siete veloci. Andiamo a riprendere il nostro impasto.",
        "host_en": "Exactly! You are fast. Let's go get our dough back.",
        "correct_it": "Sì, l'impasto ha riposato abbastanza. Possiamo iniziare a lavorarlo.",
        "correct_en": "Yes, the dough has rested enough. We can start working it.",
        "d1_it": "Sì, il gatto ha mangiato abbastanza. Possiamo giocare con lui.",
        "d1_en": "Yes, the cat has eaten enough. We can play with him.",
        "d2_it": "Sì, il bambino ha dormito abbastanza. Possiamo andare al parco.",
        "d2_en": "Yes, the child has slept enough. We can go to the park."
    }
]

conv4 = [
    {
        "host_it": "La pasta è pronta. Adesso la cuociamo in acqua bollente.",
        "host_en": "The pasta is ready. Now we cook it in boiling water.",
        "correct_it": "L'acqua nella pentola bolle. Metto il sale grosso?",
        "correct_en": "The water in the pot is boiling. Do I put coarse salt?",
        "d1_it": "Il latte nella tazza scotta. Metto lo zucchero bianco?",
        "d1_en": "The milk in the cup is burning. Do I put white sugar?",
        "d2_it": "Il caffè nel bicchiere è freddo. Metto il ghiaccio?",
        "d2_en": "The coffee in the glass is cold. Do I put ice?"
    },
    {
        "host_it": "Sì, una manciata di sale grosso. Poi cala la pasta.",
        "host_en": "Yes, a handful of coarse salt. Then drop the pasta.",
        "correct_it": "Quanti minuti serve per cuocere la pasta fresca?",
        "correct_en": "How many minutes are needed to cook fresh pasta?",
        "d1_it": "Quanti giorni serve per arrivare a Roma in macchina?",
        "d1_en": "How many days are needed to arrive in Rome by car?",
        "d2_it": "Quanti anni serve per imparare a suonare il pianoforte?",
        "d2_en": "How many years are needed to learn to play the piano?"
    },
    {
        "host_it": "Pochissimi minuti. Quando sale a galla è pronta.",
        "host_en": "Very few minutes. When it rises to the surface it is ready.",
        "correct_it": "La vedo, sta salendo. La scolo e la metto in padella?",
        "correct_en": "I see it, it's rising. Do I drain it and put it in the pan?",
        "d1_it": "Lo sento, sta cantando. Lo chiamo e lo invito qui?",
        "d1_en": "I hear him, he's singing. Do I call him and invite him here?",
        "d2_it": "La guardo, sta ballando. La saluto e le parlo dopo?",
        "d2_en": "I watch her, she's dancing. Do I greet her and talk to her later?"
    },
    {
        "host_it": "Sì, e accendi di nuovo il fuoco per saltarla nel sugo.",
        "host_en": "Yes, and turn the heat back on to toss it in the sauce.",
        "correct_it": "Che buon profumo! Sembra davvero squisita. Posso assaggiare?",
        "correct_en": "What a good smell! It looks really delicious. Can I taste?",
        "d1_it": "Che bel colore! Sembra davvero nuova. Posso provarla oggi?",
        "d1_en": "What a beautiful color! It looks really new. Can I try it today?",
        "d2_it": "Che brutto tempo! Sembra davvero freddo. Posso chiudere tutto?",
        "d2_en": "What bad weather! It seems really cold. Can I close everything?"
    },
    {
        "host_it": "Un attimo di pazienza. Aggiungi prima un po' di formaggio.",
        "host_en": "A moment of patience. Add a little cheese first.",
        "correct_it": "Mettiamo il parmigiano grattugiato sopra la pasta calda?",
        "correct_en": "Do we put grated parmesan on top of the hot pasta?",
        "d1_it": "Mettiamo le scarpe nuove dentro la scatola vuota?",
        "d1_en": "Do we put the new shoes inside the empty box?",
        "d2_it": "Mettiamo il libro vecchio sopra la mensola alta?",
        "d2_en": "Do we put the old book on top of the high shelf?"
    },
    {
        "host_it": "Perfetto, abbondante! Ora possiamo impiattare e sederci a tavola.",
        "host_en": "Perfect, abundant! Now we can plate and sit at the table.",
        "correct_it": "Prendo i piatti e porto tutto al tavolo per mangiare.",
        "correct_en": "I'll take the plates and bring everything to the table to eat.",
        "d1_it": "Prendo le chiavi e porto la macchina al parcheggio adesso.",
        "d1_en": "I'll take the keys and bring the car to the parking lot now.",
        "d2_it": "Prendo i libri e porto tutto in biblioteca per studiare.",
        "d2_en": "I'll take the books and bring everything to the library to study."
    },
    {
        "host_it": "Buon appetito a tutti! Siete stati degli allievi bravissimi.",
        "host_en": "Enjoy your meal everyone! You have been great students.",
        "correct_it": "Grazie! Anche tu sei un cuoco eccezionale e molto paziente.",
        "correct_en": "Thank you! You are also an exceptional and very patient cook.",
        "d1_it": "Grazie! Anche tu sei un medico bravo e molto attento.",
        "d1_en": "Thank you! You are also a good and very careful doctor.",
        "d2_it": "Grazie! Anche tu sei un cantante famoso e molto ricco.",
        "d2_en": "Thank you! You are also a famous and very rich singer."
    },
    {
        "host_it": "Grazie! Allora, com'è la vostra prima vera pasta italiana?",
        "host_en": "Thank you! So, how is your first real Italian pasta?",
        "correct_it": "È deliziosa! Molto meglio di quella che compro di solito.",
        "correct_en": "It is delicious! Much better than the one I usually buy.",
        "d1_it": "È costosa! Molto peggio di quello che pensavo ieri.",
        "d1_en": "It is expensive! Much worse than what I thought yesterday.",
        "d2_it": "È pesante! Molto difficile da portare per strada da solo.",
        "d2_en": "It is heavy! Very difficult to carry on the street alone."
    },
    {
        "host_it": "Sono felice che vi piaccia. Avete imparato tutti i segreti.",
        "host_en": "I'm glad you like it. You learned all the secrets.",
        "correct_it": "Voglio preparare questa ricetta a casa per i miei amici.",
        "correct_en": "I want to prepare this recipe at home for my friends.",
        "d1_it": "Voglio leggere questo libro a casa per i miei genitori.",
        "d1_en": "I want to read this book at home for my parents.",
        "d2_it": "Voglio comprare questa macchina a Roma per mio fratello.",
        "d2_en": "I want to buy this car in Rome for my brother."
    },
    {
        "host_it": "Saranno sicuramente molto felici. È stato un piacere conoscervi.",
        "host_en": "They will surely be very happy. It was a pleasure meeting you.",
        "correct_it": "Piacere mio. Grazie mille per questa bellissima esperienza in cucina!",
        "correct_en": "My pleasure. Thank you so much for this beautiful experience in the kitchen!",
        "d1_it": "Piacere mio. Grazie mille per questa noiosa lezione di storia!",
        "d1_en": "My pleasure. Thank you so much for this boring history lesson!",
        "d2_it": "Piacere mio. Grazie mille per questa lunga attesa in fila!",
        "d2_en": "My pleasure. Thank you so much for this long wait in line!"
    }
]

data = {
    "scenarioId": scenario_id,
    "conversations": [
        make_convo("starting_the_class", "Starting the Class", "Begin the cooking class and learn the basic ingredients.", conv1),
        make_convo("making_pasta_dough", "Making Pasta Dough", "Learn how to mix eggs and flour and knead the dough.", conv2),
        make_convo("preparing_the_sauce", "Preparing the Sauce", "Chop ingredients and cook a fresh tomato sauce.", conv3),
        make_convo("tasting_the_food", "Tasting the Food", "Cook the fresh pasta, mix it with the sauce, and eat.", conv4)
    ]
}

with open("src/data/exports/dining/cooking_class/conversations.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
