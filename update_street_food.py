import json

# 1. Update vocabulary translations
vocab_file = 'src/data/exports/dining/street_food/dining_street_food_vocabulary.json'
with open(vocab_file, 'r', encoding='utf-8') as f:
    vocab_data = json.load(f)

translations = {
    'abbiamo': 'we have', 'abbondante': 'abundant', 'acqua': 'water', 'aggiungere': 'to add', 'all': 'at the / to the',
    'alla': 'at the / to the', 'altro': 'other / another', 'anche': 'also / too', 'ancora': 'still / yet / again',
    'angolo': 'corner', 'appena': 'just', 'appetito': 'appetite', 'arancini': 'arancini (rice balls)',
    'arancino': 'arancino', 'arrivederci': 'goodbye', 'attento': 'careful', 'avere': 'to have', 'ben': 'well',
    'bene': 'well / good', 'bibita': 'drink', 'bisogno': 'need', 'bollente': 'boiling hot', 'bottiglia': 'bottle',
    'bottiglietta': 'small bottle', 'buon': 'good', 'buona': 'good', 'buongiorno': 'good morning', 'buonissima': 'very good',
    'buono': 'good', 'butterò': 'I will throw', 'butti': 'you throw', 'calda': 'hot', 'caldi': 'hot', 'caldo': 'hot',
    'carta': 'paper', 'casa': 'home / house', 'ceci': 'chickpeas', 'centro': 'center', 'certamente': 'certainly',
    'certo': 'sure', 'cestino': 'bin / basket', 'che': 'that / what', 'ciao': 'hello / bye', 'cinquanta': 'fifty',
    'cinque': 'five', 'con': 'with', 'consiglio': 'advice', 'continuazione': 'continuation', 'cosa': 'what / thing',
    'costa': 'costs', 'così': 'like this / so', 'crudo': 'raw / cured (prosciutto)', 'davvero': 'really', 'dei': 'some / of the',
    'del': 'of the', 'dell': 'of the', 'della': 'of the', 'dentro': 'inside', 'desideri': 'you desire',
    'differenziata': 'recycling', 'dopo': 'after', 'ecco': 'here is / here are', 'era': 'was', 'esatto': 'exactly',
    'euro': 'euro', 'facciamo': 'we make / we do', 'farina': 'flour', 'farinata': 'farinata (chickpea pancake)',
    'fatta': 'made', 'fatti': 'made', 'favore': 'favor', 'finito': 'finished', 'forchetta': 'fork', 'fredda': 'cold',
    'fresca': 'fresh / cold', 'fresche': 'fresh', 'gentile': 'kind', 'gentilissimo': 'very kind', 'giornata': 'day',
    'gli': 'the (plural)', 'grazie': 'thank you', 'hai': 'you have', 'ingredienti': 'ingredients', 'lavoro': 'work',
    'mai': 'never', 'maionese': 'mayonnaise', 'manca': 'is missing', 'mangi': 'you eat', 'mangiarla': 'to eat it',
    'mangiarlo': 'to eat it', 'mangio': 'I eat', 'mettiamo': 'we put', 'metto': 'I put', 'mille': 'thousand',
    'molta': 'much / a lot', 'molto': 'very / a lot', 'momento': 'moment', 'naturale': 'natural / still (water)',
    'nel': 'in the', 'nero': 'black', 'non': 'not', 'nostra': 'our', 'oggi': 'today', 'ogni': 'every', 'olio': 'oil',
    'ora': 'hour / now', 'ottima': 'excellent', 'ottimo': 'excellent', 'paio': 'pair', 'panino': 'sandwich',
    'passeggiata': 'walk', 'pepe': 'pepper', 'per': 'for', 'perfetto': 'perfect', 'piace': 'likes', 'piaciuto': 'liked',
    'piadina': 'piadina (flatbread)', 'piastra': 'griddle / hotplate', 'piazza': 'square', 'piedi': 'feet / standing',
    'plastica': 'plastic', 'pochino': 'a little bit', 'portarla': 'to bring it', 'portarlo': 'to bring it',
    'porzione': 'portion', 'possibile': 'possible', 'posso': 'I can', 'preferisci': 'you prefer', 'preferisco': 'I prefer',
    'prego': 'you are welcome', 'preparo': 'I prepare', 'presto': 'soon', 'proprio': 'just / exactly',
    'prosciutto': 'ham', 'prossima': 'next', 'provare': 'to try', 'provata': 'tried', 'puliti': 'clean',
    'pulizia': 'cleanliness', 'pure': 'also / go ahead', 'quanto': 'how much', 'quattro': 'four', 'qui': 'here',
    'ragù': 'ragout / meat sauce', 'resto': 'change (money)', 'rucola': 'arugula', 'sacchetto': 'bag', 'sale': 'salt',
    'salse': 'sauces', 'scaldata': 'heated', 'scelta': 'choice', 'scontrino': 'receipt', 'sei': 'six / you are',
    'sembra': 'seems', 'senza': 'without', 'serata': 'evening', 'serve': 'is needed', 'servirebbero': 'they would be needed',
    'sete': 'thirst', 'sicuramente': 'surely', 'solo': 'only', 'sono': 'are / I am', 'sopra': 'on top',
    'specialità': 'specialty', 'squacquerone': 'squacquerone (cheese)', 'squisito': 'exquisite / delicious',
    'starò': 'I will stay / I will be', 'subito': 'immediately', 'sul': 'on the', 'sulla': 'on the',
    'tenga': 'keep / hold (formal)', 'teniamo': 'we care / we keep', 'tieni': 'keep / hold', 'torna': 'come back',
    'tovaglioli': 'napkins', 'tovagliolo': 'napkin', 'tre': 'three', 'trovarci': 'to visit us / to find us',
    'tua': 'your', 'tutto': 'all / everything', 'una': 'a / one', 'vedo': 'I see', 'verso': 'towards',
    'via': 'street / away', 'vie': 'streets', 'volentieri': 'gladly', 'vorrei': 'I would like', 'vuoi': 'you want'
}

for item in vocab_data:
    if not item.get('english'):
        it = item['italian']
        if it in translations:
            item['english'] = translations[it]
        else:
            print(f"Missing translation for: {it}")

with open(vocab_file, 'w', encoding='utf-8') as f:
    json.dump(vocab_data, f, indent=2, ensure_ascii=False)


# 2. Extend conversations
conv_file = 'src/data/exports/dining/street_food/conversations.json'
with open(conv_file, 'r', encoding='utf-8') as f:
    conv_data = json.load(f)

# Conversation 1: classic_arancino
c1 = conv_data['conversations'][0]
c1['messages'][4]['choices'][0]['text'] = "Scusi, un'ultima cosa. Avete anche dei dolci tipici qui?"

c1_ext = [
    {
        "id": "m6",
        "role": "host",
        "text": "Certo! Abbiamo dei piccoli cannoli siciliani appena riempiti. Vuoi provarne uno?",
        "english": "Sure! We have small Sicilian cannoli just filled. Do you want to try one?",
        "choices": [
            {
                "text": "Sì, ne vorrei uno, per favore. Sono con la ricotta?",
                "isCorrect": True,
                "feedback": "Great question! Ricotta is the traditional filling."
            },
            {
                "text": "Vorrei una camera per la notte.",
                "isCorrect": False,
                "feedback": "Wrong domain! Focus on the cannolo."
            },
            {
                "text": "Avete dei biglietti per il museo?",
                "isCorrect": False,
                "feedback": "Wrong domain! You are at a food stall."
            }
        ]
    },
    {
        "id": "m7",
        "role": "host",
        "text": "Sì, ricotta di pecora fresca e granella di pistacchio. Una vera delizia!",
        "english": "Yes, fresh sheep's milk ricotta and chopped pistachios. A real delight!",
        "choices": [
            {
                "text": "Sembra perfetto. Lo prendo. Quanto costa il cannolo?",
                "isCorrect": True,
                "feedback": "Perfect! You decided to buy it and asked for the price."
            },
            {
                "text": "Dov'è il bagno del ristorante?",
                "isCorrect": False,
                "feedback": "You are at a street stall, not a restaurant."
            },
            {
                "text": "Vorrei noleggiare una bicicletta.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m8",
        "role": "host",
        "text": "Il cannolo costa due euro. Te lo metto nel sacchetto insieme all'arancino?",
        "english": "The cannolo costs two euros. Shall I put it in the bag with the arancino?",
        "choices": [
            {
                "text": "Sì, grazie, è un'ottima idea. Così mangio prima il salato.",
                "isCorrect": True,
                "feedback": "Good organization! Salty first, sweet after."
            },
            {
                "text": "Sì, vorrei prenotare un volo.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Vorrei un cappotto più caldo.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m9",
        "role": "host",
        "text": "Perfetto, ecco a te! Ti serviranno altri tovaglioli con il cannolo?",
        "english": "Perfect, here you go! Will you need more napkins with the cannolo?",
        "choices": [
            {
                "text": "Ne ho ancora un paio, bastano quelli. Grazie mille.",
                "isCorrect": True,
                "feedback": "Polite and practical."
            },
            {
                "text": "Vorrei un altro cuscino per il letto.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "C'è un treno per Firenze?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m10",
        "role": "host",
        "text": "Benissimo! Allora buon pranzo e buon dolce! Torna a trovarci.",
        "english": "Very well! Then enjoy your lunch and your dessert! Come visit us again.",
        "choices": [
            {
                "text": "Grazie ancora, buona giornata e buon lavoro! A presto.",
                "isCorrect": True,
                "feedback": "Excellent farewell."
            },
            {
                "text": "Dove posso ritirare i bagagli?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Vorrei parlare con il medico.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    }
]
c1['messages'].extend(c1_ext)

# Conversation 2: piadina_selection
c2 = conv_data['conversations'][1]
c2['messages'][4]['choices'][0]['text'] = "Grazie! Avete anche qualcosa da bere? Ho cambiato idea."

c2_ext = [
    {
        "id": "m6",
        "role": "host",
        "text": "Certo, abbiamo acqua, birra e alcune bibite gassate. Cosa preferisci?",
        "english": "Sure, we have water, beer and some fizzy drinks. What do you prefer?",
        "choices": [
            {
                "text": "Prendo una birra piccola, per favore. È fresca?",
                "isCorrect": True,
                "feedback": "Great choice with a piadina!"
            },
            {
                "text": "Vorrei un biglietto per il teatro.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Mi fa male la pancia.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m7",
        "role": "host",
        "text": "Sì, è fredda di frigorifero. Costa due euro e cinquanta.",
        "english": "Yes, it's cold from the fridge. It costs two euros and fifty.",
        "choices": [
            {
                "text": "Ecco tre euro. Tenga pure il resto.",
                "isCorrect": True,
                "feedback": "Generous and efficient."
            },
            {
                "text": "Dove si trova l'aeroporto?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Vorrei una mappa della città.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m8",
        "role": "host",
        "text": "Grazie mille! Ti serve un apribottiglie o la apro io?",
        "english": "Thank you very much! Do you need a bottle opener or should I open it?",
        "choices": [
            {
                "text": "La apra lei, per favore. Così la bevo subito.",
                "isCorrect": True,
                "feedback": "Practical. Eating and drinking on the spot."
            },
            {
                "text": "Vorrei fare il check-out ora.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Mi scusi, ho perso il treno.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m9",
        "role": "host",
        "text": "Ecco fatto. Attento a non rovesciarla mentre cammini!",
        "english": "Here you go. Careful not to spill it while walking!",
        "choices": [
            {
                "text": "Starò attento, non si preoccupi. Grazie del consiglio.",
                "isCorrect": True,
                "feedback": "Good acknowledgment of the warning."
            },
            {
                "text": "Il mio volo parte tra poco.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Dove posso cambiare i miei soldi?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m10",
        "role": "host",
        "text": "Perfetto! Goditi la piadina e la birra. Alla prossima!",
        "english": "Perfect! Enjoy the piadina and the beer. See you next time!",
        "choices": [
            {
                "text": "Grazie ancora, gentilissimo! Buona serata.",
                "isCorrect": True,
                "feedback": "Nice and polite wrap-up."
            },
            {
                "text": "Voglio denunciare un furto.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "A che ora chiude la banca?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    }
]
c2['messages'].extend(c2_ext)

# Conversation 3: napkins_and_drinks
c3 = conv_data['conversations'][2]
c3['messages'][4]['choices'][0]['text'] = "Grazie! C'è un bagno pubblico qui vicino per lavarmi le mani?"

c3_ext = [
    {
        "id": "m6",
        "role": "host",
        "text": "Sì, c'è un bar qui di fronte. Di solito fanno usare il bagno se prendi un caffè.",
        "english": "Yes, there's a bar across the street. Usually they let you use the bathroom if you have a coffee.",
        "choices": [
            {
                "text": "Buona idea, magari prendo un caffè veloce. Grazie per l'informazione.",
                "isCorrect": True,
                "feedback": "A very common unwritten rule in Italy!"
            },
            {
                "text": "Voglio comprare un biglietto aereo.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Dove posso parcheggiare la macchina?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m7",
        "role": "host",
        "text": "Figurati! Ti è piaciuta la salsa piccante nel panino?",
        "english": "Don't mention it! Did you like the spicy sauce in the sandwich?",
        "choices": [
            {
                "text": "Sì, molto buona! Dava un sapore speciale senza essere troppo forte.",
                "isCorrect": True,
                "feedback": "Great feedback on the food."
            },
            {
                "text": "La mia stanza è molto fredda.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Vorrei noleggiare una macchina.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m8",
        "role": "host",
        "text": "Mi fa piacere. La facciamo noi ogni mattina con peperoncini freschi.",
        "english": "I'm glad. We make it every morning with fresh chili peppers.",
        "choices": [
            {
                "text": "Complimenti, si sente che è un prodotto artigianale.",
                "isCorrect": True,
                "feedback": "Complimenting the artisan quality is highly appreciated."
            },
            {
                "text": "Dov'è il binario del mio treno?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Quanto costa un mese di abbonamento in palestra?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m9",
        "role": "host",
        "text": "Grazie, ci mettiamo molta passione. Sei qui in vacanza?",
        "english": "Thank you, we put a lot of passion into it. Are you here on vacation?",
        "choices": [
            {
                "text": "Sì, sono qui per qualche giorno. È una bellissima città.",
                "isCorrect": True,
                "feedback": "Friendly small talk is common with street vendors."
            },
            {
                "text": "Vorrei denunciare lo smarrimento della valigia.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Devo fare il biglietto per l'autobus.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m10",
        "role": "host",
        "text": "Goditi la visita allora! Se hai di nuovo fame, sai dove trovarci.",
        "english": "Enjoy your visit then! If you get hungry again, you know where to find us.",
        "choices": [
            {
                "text": "Certamente! Grazie ancora e buon lavoro.",
                "isCorrect": True,
                "feedback": "Perfect goodbye."
            },
            {
                "text": "Posso cambiare il cuscino della mia camera?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Dove trovo la polizia?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    }
]
c3['messages'].extend(c3_ext)

# Conversation 4: local_specialty
c4 = conv_data['conversations'][3]
c4['messages'][4]['choices'][0]['text'] = "Scusi, che altri cibi locali mi consiglia di provare in città?"

c4_ext = [
    {
        "id": "m6",
        "role": "host",
        "text": "Dovresti assolutamente provare la focaccia al formaggio. È un'altra nostra specialità.",
        "english": "You should absolutely try the cheese focaccia. It's another specialty of ours.",
        "choices": [
            {
                "text": "Interessante! Ma si mangia calda o fredda?",
                "isCorrect": True,
                "feedback": "Good question about how to consume it."
            },
            {
                "text": "Voglio comprare una giacca nuova.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Avete una camera matrimoniale disponibile?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m7",
        "role": "host",
        "text": "Si mangia calda, appena uscita dal forno. Il formaggio deve essere fuso.",
        "english": "You eat it hot, fresh out of the oven. The cheese must be melted.",
        "choices": [
            {
                "text": "Sembra deliziosa. La proverò domani a pranzo.",
                "isCorrect": True,
                "feedback": "Sounds like a solid food plan."
            },
            {
                "text": "Dove posso noleggiare una barca?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Ho mal di pancia.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m8",
        "role": "host",
        "text": "Ottima idea. C'è un panificio molto buono nella via principale.",
        "english": "Great idea. There's a very good bakery on the main street.",
        "choices": [
            {
                "text": "Grazie per il consiglio. Come si chiama il panificio?",
                "isCorrect": True,
                "feedback": "Smart to ask for the name."
            },
            {
                "text": "A che ora parte l'aereo per Roma?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Dove posso comprare una medicina?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m9",
        "role": "host",
        "text": "Si chiama 'Il Fornaio'. Lo vedi subito, c'è sempre un po' di fila.",
        "english": "It's called 'Il Fornaio'. You'll see it right away, there's always a bit of a line.",
        "choices": [
            {
                "text": "Perfetto, me lo segno subito. Grazie mille per l'aiuto.",
                "isCorrect": True,
                "feedback": "You are ready for your next meal!"
            },
            {
                "text": "Vorrei un ombrello per la pioggia.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "A che ora servite la colazione in hotel?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    },
    {
        "id": "m10",
        "role": "host",
        "text": "Di nulla! È un piacere aiutare i visitatori. Buona passeggiata e goditi la farinata!",
        "english": "You're welcome! It's a pleasure helping visitors. Have a nice walk and enjoy the farinata!",
        "choices": [
            {
                "text": "Lo farò sicuramente! Arrivederci e buona giornata!",
                "isCorrect": True,
                "feedback": "Great closing!"
            },
            {
                "text": "Devo fare una denuncia alla polizia.",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            },
            {
                "text": "Dov'è il check-in dell'aeroporto?",
                "isCorrect": False,
                "feedback": "Wrong domain!"
            }
        ]
    }
]
c4['messages'].extend(c4_ext)

with open(conv_file, 'w', encoding='utf-8') as f:
    json.dump(conv_data, f, indent=2, ensure_ascii=False)

print("Done updating vocabulary and conversations.")
