import json
import random

def generate_vocabulary():
    vocab_data = [
        ("palestra", "gym"), ("allenamento", "workout"), ("esercizio", "exercise"), ("peso", "weight"),
        ("bilanciere", "barbell"), ("manubrio", "dumbbell"), ("panca", "bench"), ("tapis roulant", "treadmill"),
        ("cyclette", "stationary bike"), ("vogatore", "rowing machine"), ("spogliatoio", "locker room"),
        ("armadietto", "locker"), ("asciugamano", "towel"), ("borraccia", "water bottle"), ("tappetino", "mat"),
        ("istruttore", "instructor"), ("allenatore", "coach"), ("abbonamento", "membership"),
        ("iscrizione", "registration"), ("muscolo", "muscle"), ("serie", "set"), ("ripetizione", "repetition"),
        ("riscaldamento", "warm-up"), ("stretching", "stretching"), ("cardio", "cardio"), ("forza", "strength"),
        ("resistenza", "endurance"), ("flessibilità", "flexibility"), ("proteine", "proteins"),
        ("integratore", "supplement"), ("scheda", "workout plan"), ("corso", "class"), ("yoga", "yoga"),
        ("pilates", "pilates"), ("zumba", "zumba"), ("spinning", "spinning"), ("doccia", "shower"),
        ("sauna", "sauna"), ("bagno turco", "steam room"), ("piscina", "pool"), ("reception", "reception"),
        ("certificato medico", "medical certificate"), ("scarpe da ginnastica", "sneakers"), ("tuta", "tracksuit"),
        ("pantaloncini", "shorts"), ("maglietta", "t-shirt"), ("guanti", "gloves"), ("cintura", "belt"),
        ("elastico", "resistance band"), ("corda", "rope"), ("specchio", "mirror"), ("bilancia", "scale")
    ]
    
    output = []
    for i, (it, en) in enumerate(vocab_data):
        distractors = [d for d in vocab_data if d != (it, en)]
        random.shuffle(distractors)
        
        choices_it = [it] + [d[0] for d in distractors[:3]]
        choices_en = [en] + [d[1] for d in distractors[:3]]
        
        # Shuffle both with same seed to maintain alignment
        seed = random.random()
        random.seed(seed)
        random.shuffle(choices_it)
        random.seed(seed)
        random.shuffle(choices_en)
        
        output.append({
            "id": f"s57-v{i+1}",
            "choicesItalian": choices_it,
            "choicesEnglish": choices_en,
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correctItalian": f"Esatto! '{it}' significa '{en}'.",
                "incorrectItalian": f"No, la risposta corretta è '{it}'.",
                "correctEnglish": f"Correct! '{en}' means '{it}'.",
                "incorrectEnglish": f"No, the correct answer is '{en}'."
            }
        })
    return output

def generate_phrases():
    phrases_data = [
        ("Posso usare questa panca?", "Can I use this bench?"),
        ("Quante serie ti mancano?", "How many sets do you have left?"),
        ("Possiamo alternarci?", "Can we alternate?"),
        ("Dove sono gli spogliatoi?", "Where are the locker rooms?"),
        ("C'è un istruttore disponibile?", "Is there an instructor available?"),
        ("Come si usa questa macchina?", "How do you use this machine?"),
        ("Mi serve un asciugamano.", "I need a towel."),
        ("Dove posso riempire la borraccia?", "Where can I refill my water bottle?"),
        ("A che ora inizia il corso?", "What time does the class start?"),
        ("Devo prenotare la lezione?", "Do I need to book the lesson?"),
        ("Ho dimenticato il lucchetto.", "I forgot my padlock."),
        ("Posso avere una scheda personalizzata?", "Can I have a personalized workout plan?"),
        ("Quanto costa l'abbonamento mensile?", "How much does the monthly membership cost?"),
        ("C'è una quota d'iscrizione?", "Is there a registration fee?"),
        ("Mi fa male la schiena.", "My back hurts."),
        ("Sto facendo riscaldamento.", "I'm warming up."),
        ("Faccio un po' di stretching.", "I'm doing some stretching."),
        ("Hai finito con i manubri?", "Are you done with the dumbbells?"),
        ("Posso scaricare i pesi?", "Can I unload the weights?"),
        ("Mi aiuti con questo esercizio?", "Can you help me with this exercise?"),
        ("Qual è il tuo obiettivo?", "What is your goal?"),
        ("Voglio dimagrire.", "I want to lose weight."),
        ("Voglio mettere su muscoli.", "I want to build muscle."),
        ("Oggi faccio gambe.", "Today is leg day."),
        ("Domani faccio pettorali.", "Tomorrow I'm doing chest."),
        ("Quante volte a settimana ti alleni?", "How many times a week do you train?"),
        ("Mi alleno tre volte a settimana.", "I train three times a week."),
        ("Il corso è pieno.", "The class is full."),
        ("C'è ancora posto?", "Is there still room?"),
        ("Mi sono iscritto ieri.", "I signed up yesterday."),
        ("Ho bisogno di un certificato medico.", "I need a medical certificate."),
        ("La palestra chiude alle dieci.", "The gym closes at ten."),
        ("Sabato è aperto?", "Is it open on Saturday?"),
        ("C'è il parcheggio?", "Is there parking?"),
        ("Posso fare una lezione di prova?", "Can I do a trial lesson?"),
        ("Mi sento stanco oggi.", "I feel tired today."),
        ("Ho molta energia.", "I have a lot of energy."),
        ("Bevi molta acqua.", "Drink plenty of water."),
        ("Non dimenticare di respirare.", "Don't forget to breathe."),
        ("Mantieni la schiena dritta.", "Keep your back straight."),
        ("Abbassa le spalle.", "Lower your shoulders."),
        ("Contrai l'addome.", "Contract your abdomen."),
        ("Fai attenzione alla postura.", "Pay attention to your posture."),
        ("Non caricare troppo peso.", "Don't load too much weight."),
        ("Riposati tra una serie e l'altra.", "Rest between sets."),
        ("Quanto tempo recuperi?", "How much time do you recover?"),
        ("Recupero un minuto.", "I recover one minute."),
        ("La musica è troppo alta.", "The music is too loud."),
        ("Posso cambiare canzone?", "Can I change the song?"),
        ("Buon allenamento!", "Have a good workout!")
    ]
    
    output = []
    for i, (it, en) in enumerate(phrases_data):
        distractors = [d for d in phrases_data if d != (it, en)]
        random.shuffle(distractors)
        
        choices_it = [it] + [d[0] for d in distractors[:3]]
        choices_en = [en] + [d[1] for d in distractors[:3]]
        
        seed = random.random()
        random.seed(seed)
        random.shuffle(choices_it)
        random.seed(seed)
        random.shuffle(choices_en)
        
        output.append({
            "id": f"s57-p{i+1}",
            "choicesItalian": choices_it,
            "choicesEnglish": choices_en,
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correctItalian": "Ottimo!",
                "incorrectItalian": f"No, la frase corretta è: {it}",
                "correctEnglish": "Great!",
                "incorrectEnglish": f"No, the correct phrase is: {en}"
            }
        })
    return output

def generate_sentences():
    sentences_data = [
        ("Scusa, hai ancora molti set da fare con questa panca?", "Excuse me, do you still have many sets to do with this bench?"),
        ("Mi manca solo l'ultima serie. Se vuoi possiamo alternarci.", "I only have the last set left. If you want, we can alternate."),
        ("Sì, volentieri. Che peso stai usando?", "Yes, gladly. What weight are you using?"),
        ("Sessanta chili. Ti va bene o devo scaricare un po'?", "Sixty kilos. Is it okay for you or should I unload a bit?"),
        ("No, sessanta va benissimo. Grazie mille.", "No, sixty is fine. Thank you very much."),
        ("Sai per caso a che ora inizia il corso di yoga stasera?", "Do you happen to know what time the yoga class starts tonight?"),
        ("Dovrebbe iniziare alle sette e mezza, in sala B.", "It should start at seven thirty, in room B."),
        ("Ti consiglio di andare un po' prima perché è sempre pieno.", "I recommend you go a bit earlier because it's always full."),
        ("Serve il tappetino personale o lo forniscono loro?", "Is a personal mat needed or do they provide it?"),
        ("Ci sono quelli della palestra, ma molti portano il proprio.", "There are the gym ones, but many bring their own."),
        ("Dove posso trovare l'istruttore per la scheda?", "Where can I find the instructor for the workout plan?"),
        ("L'istruttore è solitamente vicino alla zona pesi liberi.", "The instructor is usually near the free weights area."),
        ("Vorrei iscrivermi per tre mesi, quanto costa?", "I would like to sign up for three months, how much does it cost?"),
        ("L'abbonamento trimestrale costa centoventi euro.", "The three-month membership costs one hundred and twenty euros."),
        ("È inclusa anche la piscina o solo la sala pesi?", "Is the pool also included or just the weight room?"),
        ("La piscina è inclusa nell'abbonamento premium.", "The pool is included in the premium membership."),
        ("Devo portare un lucchetto per l'armadietto?", "Do I need to bring a padlock for the locker?"),
        ("Sì, gli armadietti non hanno la chiave integrata.", "Yes, the lockers do not have an integrated key."),
        ("Qual è l'esercizio migliore per i bicipiti?", "What is the best exercise for biceps?"),
        ("I curl con i manubri sono molto efficaci.", "Dumbbell curls are very effective."),
        ("Non riesco a sollevare questo peso, è troppo pesante.", "I can't lift this weight, it's too heavy."),
        ("Prova a scalare di cinque chili e controlla la tecnica.", "Try to go down by five kilos and check the technique."),
        ("Quante calorie ho bruciato sul tapis roulant?", "How many calories did I burn on the treadmill?"),
        ("Il display mostra che hai bruciato trecento calorie.", "The display shows that you burned three hundred calories."),
        ("Posso avere un asciugamano pulito alla reception?", "Can I have a clean towel at the reception?"),
        ("Certo, il noleggio dell'asciugamano costa due euro.", "Sure, the towel rental costs two euros."),
        ("A che ora chiude la palestra il sabato?", "What time does the gym close on Saturday?"),
        ("Il sabato chiudiamo alle diciotto invece che alle ventidue.", "On Saturday we close at six PM instead of ten PM."),
        ("C'è molta gente in palestra nel pomeriggio?", "Are there many people in the gym in the afternoon?"),
        ("Sì, dalle diciassette alle venti è l'orario di punta.", "Yes, from five PM to eight PM is the peak time."),
        ("Devo fare la doccia prima di entrare in piscina.", "I must take a shower before entering the pool."),
        ("È obbligatorio l'uso della cuffia in acqua.", "The use of a swim cap is mandatory in the water."),
        ("Ho perso la mia tessera della palestra.", "I lost my gym card."),
        ("Possiamo farne una nuova al costo di cinque euro.", "We can make a new one at a cost of five euros."),
        ("Mi sento molto più forte dopo un mese di allenamento.", "I feel much stronger after a month of training."),
        ("La costanza è la chiave per vedere i risultati.", "Consistency is the key to seeing results."),
        ("Posso collegare il mio telefono alla cyclette?", "Can I connect my phone to the stationary bike?"),
        ("Sì, usa il cavo USB o il Bluetooth.", "Yes, use the USB cable or Bluetooth."),
        ("C'è una zona per lo stretching e il corpo libero?", "Is there an area for stretching and bodyweight exercises?"),
        ("Sì, la zona relax è in fondo al corridoio.", "Yes, the relaxation area is at the end of the corridor."),
        ("Mi sono dimenticato le scarpe da ginnastica a casa.", "I forgot my sneakers at home."),
        ("Purtroppo non puoi allenarti con le scarpe normali.", "Unfortunately, you cannot train with regular shoes."),
        ("Quante ripetizioni devo fare per questo esercizio?", "How many repetitions should I do for this exercise?"),
        ("Fai tre serie da dodici ripetizioni ciascuna.", "Do three sets of twelve repetitions each."),
        ("Vorrei provare il corso di pilates domani mattina.", "I would like to try the pilates class tomorrow morning."),
        ("Ricordati di prenotare tramite l'applicazione.", "Remember to book through the application."),
        ("Quanto dura la lezione di spinning?", "How long does the spinning lesson last?"),
        ("La lezione dura quarantacinque minuti intensi.", "The lesson lasts forty-five intense minutes."),
        ("C'è un distributore automatico di bevande energetiche?", "Is there a vending machine for energy drinks?"),
        ("Sì, si trova proprio accanto alla reception.", "Yes, it is located right next to the reception."),
        ("Posso sospendere l'abbonamento durante le vacanze?", "Can I suspend my membership during holidays?"),
        ("Puoi sospenderlo per un massimo di due settimane.", "You can suspend it for a maximum of two weeks."),
        ("L'aria condizionata è troppo fredda in questa sala.", "The air conditioning is too cold in this room."),
        ("Parlerò con lo staff per regolare la temperatura.", "I will speak with the staff to adjust the temperature."),
        ("Qual è la tua routine di allenamento preferita?", "What is your favorite workout routine?"),
        ("Mi piace molto fare allenamento a intervalli.", "I really like doing interval training."),
        ("Hai visto dove ho lasciato la mia borraccia?", "Have you seen where I left my water bottle?"),
        ("Credo di averla vista vicino alla panca piana.", "I think I saw it near the flat bench."),
        ("Devo fare riscaldamento prima di correre.", "I need to warm up before running."),
        ("Dieci minuti di camminata veloce sono sufficienti.", "Ten minutes of brisk walking is enough.")
    ]
    
    output = []
    for i, (it, en) in enumerate(sentences_data):
        distractors = [d for d in sentences_data if d != (it, en)]
        random.shuffle(distractors)
        
        choices_it = [it] + [d[0] for d in distractors[:3]]
        choices_en = [en] + [d[1] for d in distractors[:3]]
        
        seed = random.random()
        random.seed(seed)
        random.shuffle(choices_it)
        random.seed(seed)
        random.shuffle(choices_en)
        
        output.append({
            "id": f"s57-s{i+1}",
            "choicesItalian": choices_it,
            "choicesEnglish": choices_en,
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correctItalian": "Esatto! Ottima comprensione.",
                "incorrectItalian": f"No, la traduzione corretta è: {it}",
                "correctEnglish": "Correct! Great understanding.",
                "incorrectEnglish": f"No, the correct translation is: {en}"
            }
        })
    return output

def main():
    base_path = "/home/waseageru/parli-italiano/src/data/exports/daily/at_the_gym/"
    
    vocab = generate_vocabulary()
    with open(base_path + "daily_at_the_gym_vocabulary.json", "w") as f:
        json.dump(vocab, f, indent=2, ensure_ascii=False)
        
    phrases = generate_phrases()
    with open(base_path + "daily_at_the_gym_phrases.json", "w") as f:
        json.dump(phrases, f, indent=2, ensure_ascii=False)
        
    sentences = generate_sentences()
    with open(base_path + "daily_at_the_gym_sentences.json", "w") as f:
        json.dump(sentences, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
