import json
import os
import random

def generate_scenario(category, scenario_name, scenario_id, vocab_data, phrases_data, sentences_data):
    base_path = f"src/data/exports/{category}/{scenario_name}/"
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    # Vocabulary
    vocab_json = []
    for i, (it, en) in enumerate(vocab_data):
        distractors = [v for v in vocab_data if v != (it, en)]
        selected_distractors = random.sample(distractors, 3)
        choices_it = [it] + [d[0] for d in selected_distractors]
        choices_en = [en] + [d[1] for d in selected_distractors]
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        
        vocab_json.append({
            "id": f"{scenario_id}-v{i+1}",
            "type": "vocabulary",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correctItalian": f"Ottimo! '{it}' significa '{en}'.",
                "incorrectItalian": f"No, '{it}' significa '{en}'.",
                "correctEnglish": f"Great! '{en}' is '{it}' in Italian.",
                "incorrectEnglish": f"Actually, '{en}' is '{it}'."
            }
        })

    # Phrases
    phrases_json = []
    for i, (it, en) in enumerate(phrases_data):
        distractors = [p for p in phrases_data if p != (it, en)]
        selected_distractors = random.sample(distractors, 3)
        choices_it = [it] + [d[0] for d in selected_distractors]
        choices_en = [en] + [d[1] for d in selected_distractors]
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        phrases_json.append({
            "id": f"{scenario_id}-p{i+1}",
            "type": "phrase",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correctItalian": f"Bravissimo! '{it}' significa '{en}'.",
                "incorrectItalian": f"Non esattamente, '{it}' è '{en}'.",
                "correctEnglish": f"Correct! '{en}' translates to '{it}'.",
                "incorrectEnglish": f"Actually, '{en}' is translated as '{it}'."
            }
        })

    # Sentences
    sentences_json = []
    for i, (it, en) in enumerate(sentences_data):
        distractors = [s for s in sentences_data if s != (it, en)]
        selected_distractors = random.sample(distractors, 3)
        choices_it = [it] + [d[0] for d in selected_distractors]
        choices_en = [en] + [d[1] for d in selected_distractors]
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        sentences_json.append({
            "id": f"{scenario_id}-s{i+1}",
            "type": "sentence",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correctItalian": f"Perfetto! '{it}' si traduce correttamente.",
                "incorrectItalian": f"No, la traduzione corretta è '{it}'.",
                "correctEnglish": f"Perfect! The Italian translation is '{it}'.",
                "incorrectEnglish": f"Actually, the translation should be '{it}'."
            }
        })

    with open(os.path.join(base_path, f"{category}_{scenario_name}_vocabulary.json"), "w", encoding="utf-8") as f:
        json.dump(vocab_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"{category}_{scenario_name}_phrases.json"), "w", encoding="utf-8") as f:
        json.dump(phrases_json, f, ensure_ascii=False, indent=2)
    with open(os.path.join(base_path, f"{category}_{scenario_name}_sentences.json"), "w", encoding="utf-8") as f:
        json.dump(sentences_json, f, ensure_ascii=False, indent=2)

# Haircut (s37)
vocab_s37 = [
    ("parrucchiere", "hairdresser"), ("barbiere", "barber"), ("taglio", "haircut"), ("shampoo", "shampoo"),
    ("piega", "styling/blow-dry"), ("tinta", "hair dye"), ("riflessi", "highlights"), ("spuntatina", "trim"),
    ("punte", "ends (of hair)"), ("frangetta", "bangs/fringe"), ("ciocca", "strand"), ("riga", "parting"),
    ("forbici", "scissors"), ("pettine", "comb"), ("spazzola", "brush"), ("phon", "hair dryer"),
    ("piastra", "straightener"), ("lacca", "hairspray"), ("gel", "gel"), ("schiuma", "mousse"),
    ("rasoio", "razor"), ("macchinetta", "clippers"), ("mantellina", "cape"), ("lavandino", "sink/basin"),
    ("poltrona", "chair"), ("specchio", "mirror"), ("lunghezza", "length"), ("volume", "volume"),
    ("scalati", "layered"), ("sfoltire", "to thin out"), ("accorciare", "to shorten"), ("tagliare", "to cut"),
    ("pettinare", "to comb"), ("asciugare", "to dry"), ("lavare", "to wash"), ("sciacquare", "to rinse"),
    ("rovinati", "damaged"), ("doppie punte", "split ends"), ("secchi", "dry (hair)"), ("grassi", "oily (hair)"),
    ("mossi", "wavy"), ("lisci", "straight"), ("ricci", "curly"), ("corti", "short"),
    ("lunghi", "long"), ("chiari", "light"), ("scuri", "dark"), ("biondi", "blonde"),
    ("castani", "brown (hair)"), ("rossi", "red (hair)"), ("neri", "black (hair)"), ("grigi", "gray (hair)")
]
phrases_s37 = [
    ("Vorrei un taglio", "I would like a haircut"), ("Solo una spuntatina", "Just a trim"),
    ("Tagli pure", "Go ahead and cut"), ("Non troppo corti", "Not too short"),
    ("Quanto tagliamo?", "How much should we cut?"), ("Due centimetri", "Two centimeters"),
    ("Scalati davanti", "Layered in the front"), ("Senza frangetta", "Without bangs"),
    ("Mi faccia vedere", "Show me"), ("Va bene così?", "Is it okay like this?"),
    ("Un po' di più", "A little bit more"), ("Basta così", "That's enough"),
    ("Ho un appuntamento", "I have an appointment"), ("A che nome?", "In what name?"),
    ("Per sabato pomeriggio", "For Saturday afternoon"), ("Alle sedici", "At four PM"),
    ("C'è un buco?", "Is there a slot?"), ("Si sieda pure", "Please have a seat"),
    ("Prego, da questa parte", "This way, please"), ("Vuole lo shampoo?", "Do you want shampoo?"),
    ("Taglio a secco", "Dry cut"), ("Acqua tiepida?", "Lukewarm water?"),
    ("Scotti?", "Is it burning?"), ("No, va bene", "No, it's fine"),
    ("Un po' più calda", "A little warmer"), ("Un po' più fredda", "A little colder"),
    ("Che tipo di tinta?", "What kind of dye?"), ("Coprire i capelli bianchi", "To cover gray hair"),
    ("Colore naturale", "Natural color"), ("Riflessi dorati", "Golden highlights"),
    ("Quanto tempo?", "How long?"), ("Venti minuti", "Twenty minutes"),
    ("Posso leggere?", "Can I read?"), ("Vuole un caffè?", "Do you want a coffee?"),
    ("La piega mossa", "Wavy blow-dry"), ("Lisci con la piastra", "Straight with the iron"),
    ("Un po' di lacca", "A bit of hairspray"), ("Niente gel", "No gel"),
    ("Sfoltire un po'", "To thin out a bit"), ("Accorciare le basette", "Shorten the sideburns"),
    ("Pulire il collo", "Clean the neck"), ("Quanto le devo?", "How much do I owe you?"),
    ("Cinquanta euro", "Fifty euros"), ("Tenga il resto", "Keep the change"),
    ("Grazie, arrivederci", "Thank you, goodbye"), ("A presto", "See you soon"),
    ("Mi piace molto", "I like it a lot"), ("Ottimo lavoro", "Great job"),
    ("Si sente meglio", "It feels better"), ("Capelli sani", "Healthy hair")
]
sentences_s37 = [
    ("Buongiorno, vorrei solo una spuntatina alle punte perché sono un po' rovinate.", "Good morning, I'd just like a trim on the ends because they are a bit damaged."),
    ("Quanto vuole tagliare esattamente in termini di lunghezza?", "How much exactly do you want to cut in terms of length?"),
    ("Direi un paio di centimetri, non vorrei che diventassero troppo corti.", "I'd say a couple of centimeters, I wouldn't want them to become too short."),
    ("Mi piacerebbe anche scalarli un po' davanti per dare volume.", "I would also like to layer them a bit in the front to give volume."),
    ("Procediamo prima con lo shampoo o preferisce il taglio a secco?", "Shall we proceed with the shampoo first or do you prefer a dry cut?"),
    ("L'acqua va bene così o è troppo calda per lei?", "Is the water okay like this or is it too hot for you?"),
    ("Vorrei prendere un appuntamento per una tinta e una piega per sabato.", "I would like to make an appointment for a dye and a blow-dry for Saturday."),
    ("Abbiamo un buco alle sedici, se per lei va bene.", "We have a slot at four PM, if that's okay with you."),
    ("Ho i capelli molto secchi, mi consiglia un trattamento particolare?", "My hair is very dry, do you recommend a particular treatment?"),
    ("Vorrei coprire i capelli bianchi con un colore molto naturale.", "I'd like to cover the gray hairs with a very natural color."),
    ("Può sfoltire un po' i capelli sulla parte superiore?", "Can you thin out the hair on the top part a bit?"),
    ("Preferisce la riga in mezzo o da una parte oggi?", "Do you prefer the parting in the middle or on one side today?"),
    ("Non usi troppa lacca, vorrei che rimanessero morbidi.", "Don't use too much hairspray, I'd like them to stay soft."),
    ("Mi piace molto come sono venuti i riflessi, sono molto delicati.", "I really like how the highlights turned out, they are very delicate."),
    ("Quanto tempo deve stare in posa la tinta prima del risciacquo?", "How long does the dye have to sit before rinsing?"),
    ("Ecco, guardi dietro con lo specchio, le piace il taglio?", "There, look at the back with the mirror, do you like the cut?"),
    ("Sì, è perfetto, proprio come lo volevo, grazie mille.", "Yes, it's perfect, just how I wanted it, thank you very much."),
    ("Posso pagare con la carta di credito o preferisce i contanti?", "Can I pay with a credit card or do you prefer cash?"),
    ("Dovrebbe spazzolare i capelli più delicatamente quando sono bagnati.", "You should brush your hair more gently when it's wet."),
    ("Quanto costa in totale shampoo, taglio e piega oggi?", "How much is the total for shampoo, cut, and blow-dry today?"),
    ("Vorrei provare un colore un po' più chiaro dell'ultima volta.", "I'd like to try a slightly lighter color than last time."),
    ("Mi raccomando, non tagli troppo la frangetta, mi serve lunga.", "Please, don't cut the bangs too much, I need them long."),
    ("Usi pure il rasoio per pulire bene il collo, grazie.", "Go ahead and use the razor to clean the neck well, thanks."),
    ("Sente bruciare la cute o va tutto bene?", "Do you feel your scalp burning or is everything okay?"),
    ("No, sento solo un po' di fresco, non si preoccupi.", "No, I just feel a bit of cool, don't worry."),
    ("Vorrei una piega molto liscia fatta con la piastra.", "I'd like a very straight blow-dry done with the iron."),
    ("Le sciacquo via bene tutto il prodotto dai capelli.", "I'll rinse all the product off your hair well."),
    ("Ha dei capelli molto forti e sani, complimenti.", "You have very strong and healthy hair, congratulations."),
    ("Possiamo fare alle sedici e trenta invece che alle sedici?", "Can we do it at four thirty instead of four?"),
    ("Sì, non c'è problema, la segno per quell'ora allora.", "Yes, no problem, I'll put you down for that time then."),
    ("Mi passi il phon che inizio ad asciugare questa ciocca.", "Pass me the hair dryer, I'm starting to dry this strand."),
    ("Vorrei accorciare un po' le basette, sono troppo lunghe.", "I'd like to shorten the sideburns a bit, they are too long."),
    ("Mettiamo un po' di schiuma per definire i ricci?", "Shall we put some mousse to define the curls?"),
    ("Sì, ma solo sulle punte, non sulla radice.", "Yes, but only on the ends, not on the root."),
    ("Mi scusi, potrebbe abbassare un po' la poltrona?", "Excuse me, could you lower the chair a bit?"),
    ("Certo, mi dica lei quando l'altezza è giusta.", "Of course, tell me when the height is right."),
    ("Ho visto una foto su una rivista, vorrei un taglio così.", "I saw a photo in a magazine, I'd like a cut like that."),
    ("Vediamo... sì, si può fare, ma dobbiamo scalarli molto.", "Let's see... yes, it can be done, but we have to layer them a lot."),
    ("Fa molta fatica a pettinarli la mattina a casa?", "Do you have a lot of trouble combing them in the morning at home?"),
    ("Un po', perché si annodano subito dietro la nuca.", "A bit, because they knot up immediately behind the nape."),
    ("Le metto un balsamo districante allora, aiuta molto.", "I'll put on a detangling conditioner then, it helps a lot."),
    ("Grazie, ne ho proprio bisogno oggi.", "Thanks, I really need it today."),
    ("A che ora chiude il salone stasera?", "What time does the salon close tonight?"),
    ("Chiudiamo alle diciannove e trenta, come sempre.", "We close at seven thirty PM, as always."),
    ("Perfetto, allora faccio in tempo a finire tutto.", "Perfect, then I have time to finish everything."),
    ("Vuole che le metta un po' di gel per fissare?", "Do you want me to put some gel to fix it?"),
    ("No, preferisco che rimangano naturali oggi.", "No, I prefer them to stay natural today."),
    ("Sì, è vero, così si vede meglio il nuovo taglio.", "Yes, that's true, this way you can see the new cut better."),
    ("Ci vediamo tra un mese per il ritocco del colore.", "See you in a month for the color touch-up."),
    ("D'accordo, prenoti pure alla cassa uscendo.", "Alright, go ahead and book at the desk on your way out.")
]

generate_scenario("daily_life", "haircut", "s37", vocab_s37, phrases_s37, sentences_s37)

# At the library (s38)
vocab_s38 = [
    ("biblioteca", "library"), ("bibliotecario", "librarian"), ("libro", "book"), ("scaffale", "shelf"),
    ("sezione", "section"), ("piano", "floor/level"), ("prestito", "loan"), ("restituzione", "return"),
    ("rinnovo", "renewal"), ("prenotazione", "reservation/booking"), ("tessera", "card (library card)"), ("consultazione", "consultation"),
    ("ricerca", "research/search"), ("catalogo", "catalog"), ("autore", "author"), ("titolo", "title"),
    ("genere", "genre"), ("romanzo", "novel"), ("saggio", "essay/non-fiction"), ("rivista", "magazine"),
    ("giornale", "newspaper"), ("enciclopedia", "encyclopedia"), ("dizionario", "dictionary"), ("fumetto", "comic book"),
    ("scadenza", "deadline/expiry"), ("multa", "fine"), ("ritardo", "delay"), ("silenzio", "silence"),
    ("sala lettura", "reading room"), ("studio", "study"), ("carrello", "cart/trolley"), ("etichetta", "label"),
    ("codice a barre", "barcode"), ("copertina", "cover"), ("pagina", "page"), ("indice", "index"),
    ("bibliografia", "bibliography"), ("citazione", "citation"), ("stampante", "printer"), ("fotocopiatrice", "photocopier"),
    ("computer", "computer"), ("wifi", "wifi"), ("presa", "outlet/socket"), ("scrivania", "desk"),
    ("sedia", "chair"), ("lampada", "lamp"), ("zaino", "backpack"), ("armadietto", "locker"),
    ("storia", "history"), ("arte", "art"), ("letteratura", "literature"), ("scienza", "science")
]
phrases_s38 = [
    ("Cerco un libro", "I am looking for a book"), ("In che sezione?", "In which section?"),
    ("Al secondo piano", "On the second floor"), ("Sugli scaffali", "On the shelves"),
    ("Posso prenderlo?", "Can I take it?"), ("Solo consultazione", "Consultation only"),
    ("Per trenta giorni", "For thirty days"), ("Etichetta rossa", "Red label"),
    ("Etichetta verde", "Green label"), ("Vorrei restituire", "I would like to return"),
    ("Rinnovare il prestito", "To renew the loan"), ("È già prenotato", "It's already reserved"),
    ("Entro oggi", "By today"), ("Che peccato!", "What a pity!"),
    ("In sala lettura", "In the reading room"), ("Nel carrello", "In the cart"),
    ("Serve la tessera?", "Do I need the card?"), ("Ho perso la tessera", "I lost my card"),
    ("Fare una fotocopia", "To make a photocopy"), ("Dov'è la stampante?", "Where is the printer?"),
    ("C'è il wifi?", "Is there wifi?"), ("Qual è la password?", "What is the password?"),
    ("Fare silenzio", "To be quiet"), ("Non si può mangiare", "No eating allowed"),
    ("Solo acqua", "Only water"), ("A che ora chiude?", "What time does it close?"),
    ("Sabato pomeriggio", "Saturday afternoon"), ("Sempre aperto", "Always open"),
    ("Cercare nel catalogo", "Search in the catalog"), ("Per autore", "By author"),
    ("Per titolo", "By title"), ("Non lo trovo", "I can't find it"),
    ("È in prestito", "It's out on loan"), ("Quando torna?", "When does it come back?"),
    ("Fra una settimana", "In a week"), ("Può prenotarlo", "You can reserve it"),
    ("Mi avvisate?", "Will you let me know?"), ("Via email", "Via email"),
    ("Ho una multa", "I have a fine"), ("Due euro", "Two euros"),
    ("Posso pagare qui?", "Can I pay here?"), ("Al banco", "At the counter"),
    ("Studiare insieme", "To study together"), ("Senza parlare", "Without talking"),
    ("Posto libero", "Free seat"), ("È occupato?", "Is it occupied?"),
    ("Prego, si sieda", "Go ahead, sit down"), ("Buono studio!", "Happy studying!"),
    ("Grazie mille", "Thank you very much"), ("Di nulla", "You're welcome")
]
sentences_s38 = [
    ("Scusi, sto cercando dei libri sulla storia dell'arte rinascimentale.", "Excuse me, I'm looking for some books on the history of Renaissance art."),
    ("In che sezione posso guardare per trovare testi di letteratura straniera?", "In which section can I look to find foreign literature texts?"),
    ("Si trovano al secondo piano, sezione 'Arte', scaffali dal quattrocento al quattrocentocinquanta.", "They are on the second floor, 'Art' section, shelves from four hundred to four hundred and fifty."),
    ("Posso anche prenderli in prestito o sono solo per la consultazione interna?", "Can I also take them on loan or are they for internal consultation only?"),
    ("Quelli con l'etichetta verde si possono prendere per trenta giorni consecutivi.", "Those with the green label can be taken for thirty consecutive days."),
    ("Quelli con l'etichetta rossa invece sono solo per consultazione qui in sala.", "Those with the red label instead are only for consultation here in the room."),
    ("Buongiorno, vorrei restituire questi tre libri e rinnovare il prestito per quest'altro.", "Good morning, I'd like to return these three books and renew the loan for this other one."),
    ("Questo libro è già stato prenotato da un altro utente, quindi non posso rinnovarlo.", "This book has already been reserved by another user, so I cannot renew it."),
    ("Deve restituirlo entro oggi, altrimenti dovrà pagare una piccola multa per il ritardo.", "You must return it by today, otherwise you'll have to pay a small fine for the delay."),
    ("Ah, che peccato, mi mancavano solo poche pagine per finire di leggerlo tutto.", "Ah, what a pity, I only had a few pages left to finish reading it all."),
    ("Certo, può stare qui in sala quanto vuole e finire la lettura con calma.", "Of course, you can stay here in the room as long as you want and finish reading calmly."),
    ("Poi lo lasci pure nel carrello delle restituzioni vicino all'ingresso principale.", "Then just leave it in the returns cart near the main entrance."),
    ("Dov'è il catalogo elettronico per cercare la collocazione di un volume?", "Where is the electronic catalog to search for the location of a volume?"),
    ("Può usare i computer che vede laggiù, vicino alla sezione dei giornali.", "You can use the computers you see over there, near the newspapers section."),
    ("Serve la tessera della biblioteca per accedere ai servizi internet?", "Do you need the library card to access internet services?"),
    ("Sì, deve inserire il numero della tessera e la sua password personale.", "Yes, you must enter the card number and your personal password."),
    ("Mi potrebbe aiutare a trovare questo titolo? Sul catalogo risulta disponibile.", "Could you help me find this title? It appears as available in the catalog."),
    ("Vediamo... a volte i libri vengono rimessi a posto nello scaffale sbagliato.", "Let's see... sometimes books are put back on the wrong shelf."),
    ("C'è una fotocopiatrice che posso usare per riprodurre alcune pagine?", "Is there a photocopier I can use to reproduce some pages?"),
    ("Sì, ma deve prima acquistare una tessera prepagata al banco informazioni.", "Yes, but you must first buy a prepaid card at the information desk."),
    ("È possibile prenotare una sala studio per un gruppo di quattro persone?", "Is it possible to reserve a study room for a group of four people?"),
    ("Le sale studio sono tutte occupate per oggi pomeriggio, mi dispiace molto.", "The study rooms are all occupied for this afternoon, I'm very sorry."),
    ("Si ricordi che in tutta la biblioteca è necessario mantenere il silenzio.", "Remember that in the whole library it is necessary to maintain silence."),
    ("Posso portare il mio computer portatile e caricarlo a una presa di corrente?", "Can I bring my laptop and charge it at a power outlet?"),
    ("Ci sono delle prese sotto ogni scrivania nella sala lettura principale.", "There are outlets under every desk in the main reading room."),
    ("A che ora chiude la biblioteca il sabato sera? Vorrei studiare fino tardi.", "What time does the library close on Saturday night? I'd like to study until late."),
    ("Il sabato chiudiamo alle diciotto, ma durante la settimana restiamo aperti fino alle ventidue.", "On Saturdays we close at six PM, but during the week we stay open until ten PM."),
    ("Ho perso la mia tessera, come posso fare per averne una nuova?", "I lost my card, what can I do to get a new one?"),
    ("Deve compilare questo modulo e pagare cinque euro per il duplicato.", "You must fill out this form and pay five euros for the duplicate."),
    ("Quanti libri posso prendere in prestito contemporaneamente col mio profilo?", "How many books can I borrow at the same time with my profile?"),
    ("Può prendere fino a un massimo di cinque volumi per volta.", "You can take up to a maximum of five volumes at a time."),
    ("C'è una sezione dedicata ai fumetti e alle graphic novel qui?", "Is there a section dedicated to comics and graphic novels here?"),
    ("Sì, è nell'ala nord, proprio accanto alla sezione della saggistica.", "Yes, it's in the north wing, right next to the non-fiction section."),
    ("Mi scusi, sa se questo posto è libero o se c'è qualcuno seduto?", "Excuse me, do you know if this seat is free or if someone is sitting here?"),
    ("No, è libero, può accomodarsi tranquillamente, non si preoccupi.", "No, it's free, you can take a seat, don't worry."),
    ("Grazie mille, spero di non disturbare con il rumore dei tasti.", "Thank you very much, I hope I won't disturb with the sound of the keys."),
    ("Non si preoccupi, siamo tutti qui per lavorare e studiare sodo.", "Don't worry, we are all here to work and study hard."),
    ("È possibile ricevere un avviso via email quando un libro prenotato torna?", "Is it possible to receive an email notification when a reserved book returns?"),
    ("Certamente, il sistema le invia un messaggio automatico appena viene scansionato.", "Certainly, the system sends you an automatic message as soon as it is scanned."),
    ("Quanto tempo ho per venire a ritirarlo dopo aver ricevuto l'avviso?", "How much time do I have to come and pick it up after receiving the notice?"),
    ("Il libro resta bloccato per lei al banco prestiti per tre giorni lavorativi.", "The book remains held for you at the loan desk for three working days."),
    ("C'è una zona dove è permesso parlare o fare delle chiamate brevi?", "Is there an area where talking or making short calls is allowed?"),
    ("Sì, c'è un'area relax vicino alla caffetteria al piano terra.", "Yes, there is a relaxation area near the cafeteria on the ground floor."),
    ("Non trovo lo scaffale numero trecentoventi, mi sono perso.", "I can't find shelf number three hundred and twenty, I'm lost."),
    ("Segua le indicazioni blu sul pavimento, la porteranno proprio lì.", "Follow the blue signs on the floor, they will take you right there."),
    ("I dizionari sono disponibili per il prestito a casa o solo qui?", "Are dictionaries available for home loan or only here?"),
    ("Purtroppo i dizionari sono solo per la consultazione interna, mi spiace.", "Unfortunately, dictionaries are for internal consultation only, I'm sorry."),
    ("Posso rinnovare il prestito online dal sito della biblioteca?", "Can I renew the loan online from the library's website?"),
    ("Sì, basta fare il login con le sue credenziali entro la data di scadenza.", "Yes, just log in with your credentials by the expiration date."),
    ("Grazie per l'aiuto, è stata davvero molto gentile e disponibile.", "Thanks for the help, you were really very kind and helpful.")
]

generate_scenario("daily_life", "at_the_library", "s38", vocab_s38, phrases_s38, sentences_s38)

# Household Repair (s39)
vocab_s39 = [
    ("idraulico", "plumber"), ("elettricista", "electrician"), ("tecnico", "technician"), ("riparazione", "repair"),
    ("guasto", "breakdown/fault"), ("perdita", "leak"), ("gocciolio", "dripping"), ("tubo", "pipe"),
    ("lavandino", "sink"), ("rubinetto", "faucet/tap"), ("valvola", "valve"), ("scarico", "drain"),
    ("caldaia", "boiler"), ("termosifone", "radiator"), ("riscaldamento", "heating"), ("luce", "light"),
    ("elettricità", "electricity"), ("corrente", "current/power"), ("presa", "outlet/socket"), ("interruttore", "switch"),
    ("filo", "wire"), ("cavo", "cable"), ("fusibile", "fuse"), ("quadro elettrico", "electrical panel"),
    ("contatore", "meter"), ("elettrodomestico", "appliance"), ("forno", "oven"), ("lavatrice", "washing machine"),
    ("lavastoviglie", "dishwasher"), ("frigorifero", "refrigerator"), ("aria condizionata", "air conditioning"), ("chiave inglese", "wrench"),
    ("cacciavite", "screwdriver"), ("martello", "hammer"), ("pinze", "pliers"), ("trapano", "drill"),
    ("vite", "screw"), ("bullone", "bolt"), ("guarnizione", "gasket/seal"), ("nastro isolante", "insulating tape"),
    ("muro", "wall"), ("soffitto", "ceiling"), ("pavimento", "floor"), ("tetto", "roof"),
    ("serratura", "lock"), ("chiave", "key"), ("finestra", "window"), ("vetro", "glass"),
    ("preventivo", "estimate/quote"), ("costo", "cost"), ("urgenza", "urgency"), ("appuntamento", "appointment")
]
phrases_s39 = [
    ("C'è una perdita", "There is a leak"), ("Sotto il lavandino", "Under the sink"),
    ("Gocciola tutto", "It's all dripping"), ("Perdita forte", "Strong leak"),
    ("Chiudere la valvola", "To close the valve"), ("Valvola generale", "Main valve"),
    ("Manca la luce", "The power is out"), ("È saltata la corrente", "The power tripped"),
    ("Un fusibile bruciato", "A blown fuse"), ("Nel quadro elettrico", "In the electrical panel"),
    ("Non funziona niente", "Nothing is working"), ("Problema grave", "Serious problem"),
    ("Cavi nel muro", "Cables in the wall"), ("Impianto a posto", "System is okay"),
    ("Chiamare il tecnico", "Call the technician"), ("Può passare oggi?", "Can you come by today?"),
    ("Verso le quattro", "Around four o'clock"), ("Oggi pomeriggio", "This afternoon"),
    ("Domattina presto", "Early tomorrow morning"), ("È urgente", "It's urgent"),
    ("Serve un preventivo", "Need an estimate"), ("Quanto costa?", "How much does it cost?"),
    ("Troppo caro", "Too expensive"), ("Prezzo onesto", "Fair price"),
    ("Pezzo di ricambio", "Spare part"), ("Bisogna cambiarlo", "It needs to be changed"),
    ("È rotto", "It's broken"), ("Si è bloccato", "It got stuck"),
    ("Fare un buco", "To drill a hole"), ("Attento ai tubi", "Watch out for the pipes"),
    ("Tutto sistemato", "Everything fixed"), ("Funziona di nuovo", "It works again"),
    ("Grazie del consiglio", "Thanks for the advice"), ("Non usare insieme", "Don't use together"),
    ("Troppi elettrodomestici", "Too many appliances"), ("Si surriscalda", "It overheats"),
    ("Puzza di bruciato", "Smells like burning"), ("Fa uno strano rumore", "It makes a strange noise"),
    ("Dov'è il contatore?", "Where is the meter?"), ("In cantina", "In the basement"),
    ("Fuori sul balcone", "Outside on the balcony"), ("Dietro la porta", "Behind the door"),
    ("Mi aiuti a spostare?", "Can you help me move?"), ("È pesante", "It's heavy"),
    ("Tenga pure la borsa", "Keep the bag (tools)"), ("Vado a prendere l'attrezzo", "I'll go get the tool"),
    ("Torno subito", "I'll be right back"), ("Ecco fatto", "There we go/Done"),
    ("A posto così", "That's fine as is"), ("Buon lavoro", "Good work")
]
sentences_s39 = [
    ("Buongiorno, chiamo perché ho una perdita d'acqua sotto il lavandino della cucina.", "Good morning, I'm calling because I have a water leak under the kitchen sink."),
    ("È una perdita molto forte o si tratta solo di un piccolo gocciolio?", "Is it a very strong leak or is it just a small drip?"),
    ("All'inizio gocciolava appena, ma ora sta uscendo parecchia acqua dal tubo.", "At first it was barely dripping, but now a lot of water is coming out of the pipe."),
    ("Ho dovuto chiudere la valvola generale dell'acqua per evitare di allagare tutto.", "I had to close the main water valve to avoid flooding everything."),
    ("Posso passare oggi pomeriggio verso le sedici, le va bene come orario?", "I can come by this afternoon around 4 PM, does that time work for you?"),
    ("Sì, la prego, mi serve la cucina perfettamente funzionante per stasera.", "Yes, please, I need the kitchen perfectly functional for tonight."),
    ("Ecco fatto, era solo un fusibile bruciato all'interno del quadro elettrico.", "There we go, it was just a blown fuse inside the electrical panel."),
    ("Meno male! Temevo fosse un problema molto più grave ai cavi nel muro.", "Thank goodness! I was afraid it was a much more serious problem with the cables in the wall."),
    ("No, l'impianto è a posto, ma le consiglio di non usare troppi elettrodomestici insieme.", "No, the system is fine, but I advise you not to use too many appliances at once."),
    ("Ha ragione, la luce salta sempre quando accendiamo contemporaneamente forno e lavatrice.", "You're right, the power always trips when we turn on the oven and washing machine at the same time."),
    ("Quanto le devo per l'uscita e per la sostituzione del pezzo guasto?", "How much do I owe you for the call-out and for replacing the faulty part?"),
    ("La caldaia fa uno strano rumore metallico ogni volta che apro l'acqua calda.", "The boiler makes a strange metallic noise every time I turn on the hot water."),
    ("Bisogna cambiare la guarnizione del rubinetto perché continua a perdere.", "The faucet gasket needs to be changed because it keeps leaking."),
    ("Potrebbe farmi un preventivo scritto prima di iniziare i lavori di ristrutturazione?", "Could you give me a written estimate before starting the renovation work?"),
    ("Dov'è posizionato il contatore della luce in questo condominio?", "Where is the electricity meter located in this apartment building?"),
    ("Solitamente si trova nel vano scale al piano terra o in cantina.", "Usually it's in the stairwell on the ground floor or in the basement."),
    ("Mi serve una chiave inglese più grande per svitare questo bullone arrugginito.", "I need a larger wrench to unscrew this rusty bolt."),
    ("Attenzione a non toccare quei fili scoperti, c'è ancora tensione.", "Be careful not to touch those bare wires, there is still voltage."),
    ("Ho staccato l'interruttore generale, ora si può lavorare in sicurezza.", "I've turned off the main switch, now we can work safely."),
    ("Il tecnico dell'aria condizionata verrà domani mattina alle otto in punto.", "The air conditioning technician will come tomorrow morning at eight o'clock sharp."),
    ("C'è una macchia di umidità sul soffitto del bagno, forse c'è una perdita sopra.", "There is a damp stain on the bathroom ceiling, maybe there's a leak above."),
    ("Bisogna chiamare l'inquilino del piano di sopra per controllare il suo scarico.", "We need to call the upstairs tenant to check their drain."),
    ("Il mio forno elettrico non scalda più, credo che la resistenza sia rotta.", "My electric oven doesn't heat up anymore, I think the heating element is broken."),
    ("È un modello molto vecchio, forse conviene comprarne uno nuovo invece di ripararlo.", "It's a very old model, maybe it's better to buy a new one instead of repairing it."),
    ("Le pinze sono nella cassetta degli attrezzi che ho lasciato in corridoio.", "The pliers are in the toolbox I left in the hallway."),
    ("Speriamo che il pezzo di ricambio arrivi entro la fine della settimana.", "Let's hope the spare part arrives by the end of the week."),
    ("Non c'è pressione nell'impianto di riscaldamento, i termosifoni sono freddi.", "There is no pressure in the heating system, the radiators are cold."),
    ("Deve aprire la valvola sotto la caldaia e caricare l'acqua fino a un bar.", "You must open the valve under the boiler and charge the water up to one bar."),
    ("Ah, ora capisco, non sapevo come funzionasse questo modello particolare.", "Ah, now I understand, I didn't know how this particular model worked."),
    ("La serratura della porta d'ingresso è bloccata, non riesco a girare la chiave.", "The front door lock is stuck, I can't turn the key."),
    ("Metta un po' di lubrificante spray e vedrà che si sbloccherà subito.", "Put some spray lubricant on it and you'll see it will unblock immediately."),
    ("Ho provato, ma sembra che ci sia qualcosa di rotto all'interno del meccanismo.", "I tried, but it seems there's something broken inside the mechanism."),
    ("Allora bisogna chiamare un fabbro urgente per non restare fuori casa.", "Then we need to call an urgent locksmith so as not to stay locked out."),
    ("Lo scarico della doccia è intasato da capelli e residui di sapone.", "The shower drain is clogged with hair and soap residue."),
    ("Usi questo prodotto liquido, lo lasci agire per mezz'ora e poi sciacqui.", "Use this liquid product, let it act for half an hour and then rinse."),
    ("Se non funziona, dovrò usare la sonda flessibile per liberare il tubo.", "If it doesn't work, I'll have to use the flexible snake to clear the pipe."),
    ("Il tecnico ha detto che l'impianto elettrico non è a norma di legge.", "The technician said the electrical system is not up to legal standards."),
    ("Dobbiamo rifare tutto il cablaggio per evitare cortocircuiti e incendi.", "We have to redo all the wiring to avoid short circuits and fires."),
    ("Quanto tempo ci vorrà per completare tutti questi lavori in casa?", "How much time will it take to complete all these works in the house?"),
    ("Direi almeno una settimana, se non troviamo altri intoppi imprevisti.", "I'd say at least a week, if we don't find other unexpected hitches."),
    ("Mi raccomando, cerchi di sporcare il meno possibile durante il lavoro.", "Please, try to make as little mess as possible during the work."),
    ("Non si preoccupi, mettiamo dei teli protettivi su tutti i mobili e sul pavimento.", "Don't worry, we put protective sheets on all the furniture and on the floor."),
    ("Grazie, ci tengo molto perché il parquet è stato appena lucidato.", "Thanks, it's very important to me because the parquet has just been polished."),
    ("Ho trovato il guasto: era un piccolo cavo che si era scollegato.", "I found the fault: it was a small cable that had disconnected."),
    ("Ora la lavastoviglie dovrebbe riprendere il ciclo di lavaggio normalmente.", "Now the dishwasher should resume the wash cycle normally."),
    ("Meno male, lavare tutto a mano per una famiglia di cinque persone è dura!", "Thank goodness, washing everything by hand for a family of five is hard!"),
    ("Le lascio la fattura sul tavolo, può pagare tramite bonifico bancario.", "I'll leave the invoice on the table, you can pay via bank transfer."),
    ("Va benissimo, lo farò stasera stessa appena rientra mio marito.", "That's fine, I'll do it tonight as soon as my husband returns."),
    ("Se ha altri problemi in futuro, non esiti a chiamarmi di nuovo.", "If you have other problems in the future, don't hesitate to call me again."),
    ("Certamente, grazie mille per la sua professionalità e rapidità.", "Certainly, thank you very much for your professionalism and speed.")
]

generate_scenario("daily_life", "household_repair", "s39", vocab_s39, phrases_s39, sentences_s39)

# Making an Appointment (s40)
vocab_s40 = [
    ("appuntamento", "appointment"), ("prenotazione", "booking/reservation"), ("fissare", "to set/fix (an appointment)"), ("spostare", "to move/reschedule"),
    ("disdire", "to cancel"), ("confermare", "to confirm"), ("disponibilità", "availability"), ("libero", "free/available"),
    ("occupato", "busy/occupied"), ("orario", "time/schedule"), ("data", "date"), ("calendario", "calendar"),
    ("studio", "office/practice"), ("dentista", "dentist"), ("medico", "doctor"), ("segretaria", "secretary"),
    ("paziente", "patient"), ("cliente", "client"), ("controllo", "check-up"), ("pulizia", "cleaning"),
    ("visita", "visit/examination"), ("urgenza", "urgency"), ("ritardo", "delay"), ("anticipo", "early/advance"),
    ("mattina", "morning"), ("pomeriggio", "afternoon"), ("sera", "evening"), ("tardo pomeriggio", "late afternoon"),
    ("prossima settimana", "next week"), ("domani", "tomorrow"), ("dopodomani", "day after tomorrow"), ("lunedì", "Monday"),
    ("martedì", "Tuesday"), ("mercoledì", "Wednesday"), ("giovedì", "Thursday"), ("venerdì", "Friday"),
    ("sabato", "Saturday"), ("domenica", "Sunday"), ("ora", "hour"), ("minuto", "minute"),
    ("sessione", "session"), ("lezione", "lesson"), ("individuale", "individual"), ("gruppo", "group"),
    ("palestra", "gym"), ("personal trainer", "personal trainer"), ("asciugamano", "towel"), ("acqua", "water"),
    ("faticare", "to work hard/toil"), ("portare", "to bring"), ("chiedere", "to ask"), ("rispondere", "to answer")
]
phrases_s40 = [
    ("Vorrei un appuntamento", "I would like an appointment"), ("Per un controllo", "For a check-up"),
    ("Pulizia dei denti", "Teeth cleaning"), ("Quando c'è posto?", "When is there a spot?"),
    ("La prima disponibilità", "The first availability"), ("Martedì prossimo", "Next Tuesday"),
    ("Alle dieci", "At ten"), ("Lavoro a quell'ora", "I work at that time"),
    ("Nel tardo pomeriggio", "In the late afternoon"), ("Giovedì alle diciotto", "Thursday at six PM"),
    ("Va benissimo", "That's perfect"), ("Grazie mille", "Thank you very much"),
    ("Prenotare una sessione", "To book a session"), ("Per mercoledì", "For Wednesday"),
    ("Chi preferisce?", "Who do you prefer?"), ("Marco alle undici", "Marco at eleven"),
    ("Giulia alle quindici", "Giulia at three PM"), ("Giulia va bene", "Giulia is fine"),
    ("La prima volta", "The first time"), ("Lezione individuale", "Individual lesson"),
    ("Devo portare qualcosa?", "Do I need to bring anything?"), ("Solo un asciugamano", "Just a towel"),
    ("Tanta voglia di faticare", "A lot of desire to work hard"), ("A che ora?", "At what time?"),
    ("Dov'è lo studio?", "Where is the practice?"), ("In centro", "In the center"),
    ("Vicino alla stazione", "Near the station"), ("Posso spostare?", "Can I move it?"),
    ("Vorrei disdire", "I would like to cancel"), ("Ho un imprevisto", "Something came up"),
    ("C'è una penale?", "Is there a fee?"), ("No, non si preoccupi", "No, don't worry"),
    ("Posso venire prima?", "Can I come earlier?"), ("Sì, se vuole", "Yes, if you want"),
    ("Siamo in anticipo", "We are early"), ("Scusi il ritardo", "Sorry for the delay"),
    ("C'era traffico", "There was traffic"), ("Non importa", "It doesn't matter"),
    ("A che nome?", "In what name?"), ("A nome Rossi", "Under the name Rossi"),
    ("Il suo numero?", "Your number?"), ("Ecco il mio cellulare", "Here is my cell phone"),
    ("Le mando un SMS", "I'll send you a text"), ("Come promemoria", "As a reminder"),
    ("Ci vediamo giovedì", "See you Thursday"), ("A presto", "See you soon"),
    ("Buona giornata", "Have a good day"), ("Altrettanto", "Likewise"),
    ("D'accordo", "Agreed/Alright"), ("Perfetto così", "Perfect like that")
]
sentences_s40 = [
    ("Buongiorno, vorrei fissare un appuntamento per una pulizia dei denti e un controllo.", "Good morning, I'd like to set an appointment for a teeth cleaning and a check-up."),
    ("La nostra prima disponibilità è per martedì prossimo alle dieci del mattino.", "Our first availability is for next Tuesday at ten in the morning."),
    ("Purtroppo lavoro a quell'ora e non posso proprio liberarmi.", "Unfortunately I work at that time and I really can't get free."),
    ("Avreste qualcosa nel tardo pomeriggio, magari dopo le diciassette?", "Would you have something in the late afternoon, maybe after 5 PM?"),
    ("Posso proporle giovedì alle diciotto, è l'ultimo orario disponibile.", "I can offer you Thursday at 6 PM, it's the last available time."),
    ("Perfetto, giovedì alle diciotto va benissimo per me, grazie.", "Perfect, Thursday at 6 PM is very good for me, thanks."),
    ("Vorrei prenotare una sessione con un personal trainer per mercoledì pomeriggio.", "I would like to book a session with a personal trainer for Wednesday afternoon."),
    ("Mercoledì abbiamo Marco libero alle undici o Giulia alle quindici, chi preferisce?", "On Wednesday we have Marco free at eleven or Giulia at three PM, who do you prefer?"),
    ("Giulia va bene, mi hanno parlato molto bene del suo metodo di allenamento.", "Giulia is fine, they have spoken very well of her training method."),
    ("È la prima volta che faccio una lezione individuale, devo portare qualcosa?", "It's the first time I do an individual lesson, do I need to bring anything?"),
    ("Porti solo un asciugamano, dell'acqua e tanta voglia di faticare!", "Just bring a towel, some water and a lot of desire to work hard!"),
    ("Salve, chiamo per confermare l'appuntamento di domani con il dottor Bianchi.", "Hello, I'm calling to confirm tomorrow's appointment with Doctor Bianchi."),
    ("Mi dispiace, ma devo disdire la mia prenotazione per stasera a causa di un imprevisto.", "I'm sorry, but I have to cancel my booking for tonight due to an unexpected event."),
    ("Sarebbe possibile spostare la visita a venerdì mattina alla stessa ora?", "Would it be possible to move the visit to Friday morning at the same time?"),
    ("Devo chiedere al dottore se ha dei buchi liberi in agenda per quel giorno.", "I have to ask the doctor if he has any free slots in the diary for that day."),
    ("Se vuole posso metterla in lista d'attesa e chiamarla se qualcuno disdice.", "If you want I can put you on the waiting list and call you if someone cancels."),
    ("Sì, grazie, sarebbe molto gentile, ne avrei davvero urgenza.", "Yes, thanks, that would be very kind, I'd really have an urgency for it."),
    ("A che nome devo segnare la prenotazione per il campo da tennis?", "In what name should I put the reservation for the tennis court?"),
    ("Segni pure a nome Rossi, siamo in quattro per le diciannove.", "Put it under the name Rossi, there are four of us for 7 PM."),
    ("Le invieremo un SMS di promemoria ventiquattro ore prima dell'appuntamento.", "We will send you a reminder text message twenty-four hours before the appointment."),
    ("Scusi, sono in ritardo di dieci minuti perché non trovavo parcheggio.", "Sorry, I'm ten minutes late because I couldn't find parking."),
    ("Non si preoccupi, il medico è ancora impegnato con il paziente precedente.", "Don't worry, the doctor is still busy with the previous patient."),
    ("Potrebbe anticipare il mio appuntamento di mezz'ora se fosse possibile?", "Could you move my appointment forward by half an hour if it were possible?"),
    ("Vediamo... sì, la persona prima di lei ha appena finito in anticipo.", "Let's see... yes, the person before you just finished early."),
    ("Dove si trova esattamente il vostro studio? Non sono della zona.", "Where exactly is your practice located? I'm not from the area."),
    ("Siamo in via Roma numero dieci, proprio di fronte alla banca principale.", "We are in via Roma number ten, right in front of the main bank."),
    ("C'è una penale da pagare se disdico l'appuntamento all'ultimo minuto?", "Is there a fee to pay if I cancel the appointment at the last minute?"),
    ("Chiediamo di avvisare almeno un giorno prima, altrimenti dobbiamo addebitare il costo.", "We ask to notify at least one day in advance, otherwise we have to charge the cost."),
    ("Capisco perfettamente, cercherò di essere puntuale allora.", "I understand perfectly, I will try to be punctual then."),
    ("Vorrei fissare un controllo generale, è da molto che non vengo.", "I'd like to set a general check-up, it's been a long time since I came."),
    ("Ha preferenze per un medico in particolare o va bene chiunque?", "Do you have a preference for a particular doctor or is anyone okay?"),
    ("Il dottor Neri mi ha seguito l'ultima volta, preferirei lui.", "Doctor Neri followed me last time, I would prefer him."),
    ("Il dottor Neri è in ferie questa settimana, torna lunedì prossimo.", "Doctor Neri is on vacation this week, he returns next Monday."),
    ("Allora aspetto che torni, non è una cosa urgentissima.", "Then I'll wait until he returns, it's not a very urgent thing."),
    ("D'accordo, allora la segno per mercoledì della settimana successiva.", "Alright, then I'll put you down for Wednesday of the following week."),
    ("A che ora preferisce? Mattina o pomeriggio dopo il lavoro?", "What time do you prefer? Morning or afternoon after work?"),
    ("Il pomeriggio verso le diciassette e trenta sarebbe l'ideale per me.", "The afternoon around 5:30 PM would be ideal for me."),
    ("Perfetto, allora ci vediamo mercoledì alle diciassette e trenta.", "Perfect, then see you Wednesday at 5:30 PM."),
    ("Grazie mille per la sua disponibilità, arrivederci e buon lavoro.", "Thank you very much for your availability, goodbye and good work."),
    ("Arrivederci a lei, buona giornata e a presto.", "Goodbye to you, have a good day and see you soon."),
    ("Ho dimenticato di chiedere se posso portare un accompagnatore.", "I forgot to ask if I can bring a companion."),
    ("Sì, certo, ma deve aspettare in sala d'attesa durante la visita.", "Yes, of course, but they must wait in the waiting room during the visit."),
    ("Va benissimo, mio marito mi accompagnerà in macchina.", "That's fine, my husband will accompany me by car."),
    ("Ricordi di portare con sé la tessera sanitaria e gli esami precedenti.", "Remember to bring your health card and previous exams with you."),
    ("Sì, ho già preparato tutto nella cartellina blu.", "Yes, I've already prepared everything in the blue folder."),
    ("C'è molta attesa solitamente o siete puntuali con gli orari?", "Is there usually a lot of waiting or are you punctual with the times?"),
    ("Cerchiamo di essere il più precisi possibile, ma a volte ci sono urgenze.", "We try to be as precise as possible, but sometimes there are emergencies."),
    ("Spero di non dover aspettare troppo, ho un altro impegno dopo.", "I hope I don't have to wait too long, I have another commitment after."),
    ("Faremo il possibile per farla entrare subito all'orario stabilito.", "We will do our best to let you in right at the set time."),
    ("Grazie, apprezzo molto la vostra professionalità.", "Thanks, I very much appreciate your professionalism.")
]

generate_scenario("daily_life", "making_an_appointment", "s40", vocab_s40, phrases_s40, sentences_s40)

# At the Post Office (s41)
vocab_s41 = [
    ("ufficio postale", "post office"), ("impiegato", "clerk/employee"), ("cliente", "customer"), ("sportello", "counter"),
    ("pacco", "package/parcel"), ("lettera", "letter"), ("busta", "envelope"), ("francobollo", "stamp"),
    ("raccomandata", "registered mail"), ("spedizione", "shipping"), ("consegna", "delivery"), ("indirizzo", "address"),
    ("destinatario", "recipient"), ("mittente", "sender"), ("tracciabile", "trackable"), ("codice di tracciamento", "tracking code"),
    ("bilancia", "scale"), ("peso", "weight"), ("chilo", "kilogram"), ("grammo", "gram"),
    ("modulo", "form"), ("compilare", "to fill out"), ("firmare", "to sign"), ("dogana", "customs"),
    ("bollettino", "bill/payment slip"), ("pagamento", "payment"), ("commissione", "fee/commission"), ("ricevuta", "receipt"),
    ("posta prioritaria", "priority mail"), ("posta aerea", "airmail"), ("scatola", "box"), ("nastro adesivo", "adhesive tape"),
    ("bancomat", "debit card"), ("carta di credito", "credit card"), ("contanti", "cash"), ("resto", "change"),
    ("codice PIN", "PIN code"), ("lettore", "reader"), ("timbro", "stamp/seal"), ("scadenza", "deadline/expiry"),
    ("assicurata", "insured mail"), ("valore", "value"), ("contenuto", "content"), ("regalo", "gift"),
    ("Germania", "Germany"), ("Europa", "Europe"), ("estero", "abroad"), ("prezzo", "price"),
    ("costo", "cost"), ("euro", "euro"), ("centesimo", "cent"), ("prossimo", "next")
]
phrases_s41 = [
    ("Buongiorno, prossimo!", "Good morning, next!"), ("Vorrei spedire", "I would like to send"),
    ("Questo pacco", "This package"), ("In Germania", "To Germany"),
    ("È un regalo", "It's a gift"), ("Sulla bilancia", "On the scale"),
    ("Quanto pesa?", "How much does it weigh?"), ("Due chili e mezzo", "Two and a half kilos"),
    ("Spedizione tracciabile", "Trackable shipping"), ("Raccomandata internazionale", "International registered mail"),
    ("Quanto costa?", "How much does it cost?"), ("Ventotto euro", "Twenty-eight euros"),
    ("Compilare questo modulo", "Fill out this form"), ("Per la dogana", "For customs"),
    ("Dentro l'Unione Europea", "Inside the European Union"), ("Per precauzione", "As a precaution"),
    ("Pagare un bollettino", "To pay a bill"), ("Bollettino della luce", "Electricity bill"),
    ("Certamente", "Certainly"), ("Ottantacinque euro", "Eighty-five euros"),
    ("Venti centesimi", "Twenty cents"), ("C'è una commissione", "There is a fee"),
    ("Due euro", "Two euros"), ("Posso pagare col Bancomat?", "Can I pay with the debit card?"),
    ("Inserisca la carta", "Insert the card"), ("Digiti il PIN", "Type the PIN"),
    ("Ecco la ricevuta", "Here is the receipt"), ("Serve un francobollo", "Need a stamp"),
    ("Per l'Italia", "For Italy"), ("Posta prioritaria", "Priority mail"),
    ("Dove devo firmare?", "Where do I have to sign?"), ("Qui in basso", "Here at the bottom"),
    ("Chi è il mittente?", "Who is the sender?"), ("Scriva l'indirizzo", "Write the address"),
    ("Il destinatario è a Londra", "The recipient is in London"), ("Quanto tempo ci vuole?", "How long does it take?"),
    ("Cinque giorni lavorativi", "Five working days"), ("È assicurata?", "Is it insured?"),
    ("Voglio assicurarlo", "I want to insure it"), ("Valore dichiarato", "Declared value"),
    ("Cento euro", "One hundred euros"), ("Prenda il numero", "Take a number"),
    ("Qual è il mio turno?", "What is my turn?"), ("Lo sportello tre", "Counter three"),
    ("Mi serve una busta", "I need an envelope"), ("Grande o piccola?", "Large or small?"),
    ("A imbottitura", "Padded"), ("Ecco a lei", "Here you go"),
    ("Grazie mille", "Thank you very much"), ("Buona giornata", "Have a good day")
]
sentences_s41 = [
    ("Buongiorno, vorrei spedire questo pacco in Germania, è un regalo per un amico.", "Good morning, I'd like to send this package to Germany, it's a gift for a friend."),
    ("Lo metta pure sulla bilancia per favore, così vediamo quanto pesa esattamente.", "Please put it on the scale, so we can see exactly how much it weighs."),
    ("Il pacco pesa due chili e mezzo, vuole una spedizione semplice o tracciabile?", "The package weighs two and a half kilos, do you want simple or trackable shipping?"),
    ("Preferirei una spedizione tracciabile, quanto costa la raccomandata internazionale?", "I would prefer trackable shipping, how much does the international registered mail cost?"),
    ("Il costo totale è di ventotto euro, compresa l'assicurazione base sul contenuto.", "The total cost is twenty-eight euros, including basic insurance on the content."),
    ("Deve compilare questo modulo per la dogana, anche se la destinazione è in Europa.", "You must fill out this customs form, even if the destination is in Europe."),
    ("Buongiorno, dovrei pagare questo bollettino della luce che scade domani.", "Good morning, I have to pay this electricity bill that expires tomorrow."),
    ("Certamente, sono ottantacinque euro e venti centesimi più due euro di commissione.", "Certainly, it's eighty-five euros and twenty cents plus a two-euro fee."),
    ("Posso pagare con il Bancomat o accettate solo pagamenti in contanti?", "Can I pay with the debit card or do you only accept cash payments?"),
    ("Sì, inserisca pure la carta nel lettore, digiti il PIN e attenda la conferma.", "Yes, go ahead and insert the card in the reader, type the PIN and wait for confirmation."),
    ("Ecco a lei la ricevuta del pagamento, la conservi per almeno cinque anni.", "Here is your payment receipt, keep it for at least five years."),
    ("Mi serve un francobollo per spedire una lettera ordinaria in Italia.", "I need a stamp to send an ordinary letter in Italy."),
    ("Vuole la posta prioritaria così arriva domani o quella normale che costa meno?", "Do you want priority mail so it arrives tomorrow or normal mail which costs less?"),
    ("Quella normale va benissimo, non ho particolare fretta per questa lettera.", "Normal is fine, I'm not in a particular hurry for this letter."),
    ("Deve scrivere l'indirizzo del mittente sul retro della busta, per favore.", "You must write the sender's address on the back of the envelope, please."),
    ("Scusi, dove posso prendere il numero per fare la fila allo sportello?", "Excuse me, where can I take the number to queue at the counter?"),
    ("C'è la macchinetta gialla all'ingresso, deve premere il tasto 'Spedizioni'.", "There's the yellow machine at the entrance, you have to press the 'Shipping' button."),
    ("Quanto tempo ci mette solitamente un pacco ad arrivare negli Stati Uniti?", "How long does a package usually take to arrive in the United States?"),
    ("Con la posta aerea ci vogliono circa dieci giorni lavorativi, salvo ritardi doganali.", "With airmail it takes about ten working days, barring customs delays."),
    ("Vorrei assicurare questa spedizione per un valore dichiarato di cinquecento euro.", "I would like to insure this shipment for a declared value of five hundred euros."),
    ("In quel caso deve usare il modulo specifico per le assicurate internazionali.", "In that case you must use the specific form for international insured mail."),
    ("Posso comprare anche delle buste imbottite di diverse dimensioni qui?", "Can I also buy padded envelopes of different sizes here?"),
    ("Sì, le trova esposte lì a sinistra, scelga pure quella che le serve.", "Yes, you can find them displayed there on the left, just choose the one you need."),
    ("Mi dà anche un rotolo di nastro adesivo per chiudere bene questa scatola?", "Will you also give me a roll of adhesive tape to close this box well?"),
    ("Certo, sono altri tre euro da aggiungere al totale della spedizione.", "Sure, that's another three euros to add to the shipping total."),
    ("Ho ricevuto un avviso di giacenza, dove posso ritirare la mia raccomandata?", "I received a notice of non-delivery, where can I pick up my registered mail?"),
    ("Deve venire qui domani mattina dopo le dieci con un documento d'identità.", "You must come here tomorrow morning after ten with an ID document."),
    ("Posso delegare un'altra persona al ritiro firmando il modulo sul retro?", "Can I delegate another person for pickup by signing the form on the back?"),
    ("Sì, ma la persona delegata deve portare anche una fotocopia del suo documento.", "Yes, but the delegated person must also bring a photocopy of your document."),
    ("A che ora chiude l'ufficio postale il sabato pomeriggio?", "What time does the post office close on Saturday afternoon?"),
    ("Il sabato siamo aperti solo la mattina fino alle dodici e trenta.", "On Saturdays we are only open in the morning until 12:30 PM."),
    ("C'è molta gente oggi, spero che il mio numero venga chiamato presto.", "There are a lot of people today, I hope my number gets called soon."),
    ("Lo sportello numero tre si è appena liberato, tocca a lei signora.", "Counter number three just became free, it's your turn, madam."),
    ("Buongiorno, vorrei ritirare il pacco che è arrivato a nome di mio marito.", "Good morning, I'd like to pick up the package that arrived in my husband's name."),
    ("Ecco la delega firmata e i documenti originali di entrambi.", "Here is the signed delegation and the original documents of both."),
    ("Benissimo, un attimo che controllo nel magazzino sul retro.", "Very well, just a moment while I check in the warehouse at the back."),
    ("Mi dispiace, il pacco non è ancora arrivato in questo ufficio.", "I'm sorry, the package has not yet arrived at this office."),
    ("Controlli pure il codice di tracciamento sul sito, dovrebbe essere in transito.", "Check the tracking code on the website, it should be in transit."),
    ("Ah, vedo che è fermo al centro di smistamento di Milano da due giorni.", "Ah, I see it's been stuck at the sorting center in Milan for two days."),
    ("Speriamo che lo sblocchino presto, lo aspetto con impazienza.", "Let's hope they unblock it soon, I'm waiting for it impatiently."),
    ("Posso ricaricare la mia carta prepagata allo sportello?", "Can I top up my prepaid card at the counter?"),
    ("Sì, mi servono la carta, il suo codice fiscale e i contanti per la ricarica.", "Yes, I need the card, your tax code and the cash for the top-up."),
    ("Qual è la commissione per l'operazione di ricarica della carta?", "What is the fee for the card top-up operation?"),
    ("La commissione è di un euro fisso per ogni operazione di ricarica.", "The fee is a fixed one euro for each top-up operation."),
    ("Perfetto, vorrei caricare cento euro sulla mia carta, grazie.", "Perfect, I'd like to load one hundred euros on my card, thanks."),
    ("Digiti pure il PIN sul tastierino per confermare l'operazione.", "Type the PIN on the keypad to confirm the operation."),
    ("Ecco la sua ricevuta, il saldo sarà aggiornato immediatamente.", "Here is your receipt, the balance will be updated immediately."),
    ("Grazie mille per l'aiuto e per la sua cortesia, buona giornata.", "Thank you very much for the help and for your courtesy, good day."),
    ("Di nulla, arrivederci e alla prossima volta!", "You're welcome, goodbye and until next time!")
]

generate_scenario("daily_life", "at_the_post_office", "s41", vocab_s41, phrases_s41, sentences_s41)
