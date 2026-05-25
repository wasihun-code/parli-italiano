import json
import os
import random

def generate_university_class():
    scenario = "workstudy_university_class"
    prefix = "s65"
    base_path = "src/data/exports/workstudy/university_class/"
    
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    # Vocabulary (Min 50)
    vocab_list = [
        ("il professore", "the professor"), ("la studentessa", "the student (female)"),
        ("lo studente", "the student (male)"), ("l'aula", "the classroom"),
        ("l'aula magna", "the lecture hall"), ("la lezione", "the lesson/class"),
        ("il corso", "the course"), ("l'esame", "the exam"), ("gli appunti", "the notes"),
        ("la tesina", "the term paper"), ("il portale", "the portal"), ("caricare", "to upload"),
        ("scaricare", "to download"), ("il libro", "the book"), ("la biblioteca", "the library"),
        ("la mensa", "the canteen"), ("la borsa di studio", "the scholarship"),
        ("la laurea", "the degree"), ("la tesi", "the thesis"), ("il relatore", "the supervisor"),
        ("l'appello", "the exam session/roll call"), ("l'iscrizione", "the enrollment"),
        ("la matricola", "the student ID/freshman"), ("il libretto", "the student record book"),
        ("il voto", "the grade"), ("trenta e lode", "top grade (30 with honors)"),
        ("bocciato", "failed"), ("promosso", "passed"), ("il ricevimento", "the office hours"),
        ("il dipartimento", "the department"), ("la facoltà", "the faculty"),
        ("il semestre", "the semester"), ("la sessione", "the session"),
        ("la bacheca", "the bulletin board"), ("l'orario", "the timetable"),
        ("il credito", "the credit (CFU)"), ("l'esonero", "the partial exam/exemption"),
        ("la prova", "the test"), ("lo scritto", "the written exam"),
        ("l'orale", "the oral exam"), ("la domanda", "the question"),
        ("la risposta", "the answer"), ("la spiegazione", "the explanation"),
        ("l'argomento", "the topic"), ("la ricerca", "the research"),
        ("il laboratorio", "the laboratory"), ("il tirocinio", "the internship"),
        ("il progetto", "the project"), ("la presentazione", "the presentation"),
        ("le slide", "the slides"), ("il ripasso", "the review"),
        ("lo studio", "the study"), ("la penna", "the pen"),
        ("il quaderno", "the notebook"), ("lo zaino", "the backpack"),
        ("il posto", "the seat"), ("libero", "free/vacant"),
        ("occupato", "occupied")
    ]
    
    vocab_data = []
    for i, (it, en) in enumerate(vocab_list):
        choices_it = [it]
        choices_en = [en]
        others = [v for v in vocab_list if v != (it, en)]
        random.seed(i)
        distractors = random.sample(others, 3)
        for d_it, d_en in distractors:
            choices_it.append(d_it)
            choices_en.append(d_en)
        
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        
        vocab_data.append({
            "id": f"{prefix}-v{i+1:02d}",
            "type": "vocabulary",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correctItalian": f"Esatto! '{it}' significa '{en}'.",
                "incorrectItalian": f"Non proprio. '{it}' è la risposta giusta.",
                "correctEnglish": f"Correct! '{en}' is '{it}' in Italian.",
                "incorrectEnglish": f"Not quite. '{en}' is the correct translation."
            }
        })

    # Phrases (Min 50)
    phrase_list = [
        ("Prendere appunti", "To take notes"), ("Seguire le lezioni", "To attend classes"),
        ("Studiare per l'esame", "To study for the exam"), ("Passare l'esame", "To pass the exam"),
        ("Essere bocciato", "To fail / be failed"), ("Iscriversi al corso", "To enroll in the course"),
        ("Caricare sul portale", "To upload to the portal"), ("Consegnare a mano", "To hand in by hand"),
        ("Chiedere il ricevimento", "To ask for office hours"), ("Fare una domanda", "To ask a question"),
        ("Rispondere alla domanda", "To answer the question"), ("Argomento della tesi", "Thesis topic"),
        ("Relatore di tesi", "Thesis supervisor"), ("Sessione estiva", "Summer session"),
        ("Sessione invernale", "Winter session"), ("Ultimo appello", "Last call/exam date"),
        ("Primo semestre", "First semester"), ("Secondo semestre", "Second semester"),
        ("Aula magna", "Great hall"), ("Posto libero", "Free seat"),
        ("Libretto universitario", "University record book"), ("Numero di matricola", "Student ID number"),
        ("Borsa di studio", "Scholarship"), ("Tasse universitarie", "University fees"),
        ("Mensa universitaria", "University canteen"), ("Sala studio", "Study room"),
        ("Prestito libri", "Book loan"), ("Prova parziale", "Partial test"),
        ("Domanda d'esame", "Exam question"), ("Voto finale", "Final grade"),
        ("Trenta e lode", "30 with honors"), ("Fare ricerca", "To do research"),
        ("Preparare la tesina", "To prepare the term paper"), ("Scadenza della tesina", "Term paper deadline"),
        ("Orario delle lezioni", "Class schedule"), ("Crediti formativi", "Educational credits"),
        ("Corso obbligatorio", "Mandatory course"), ("Corso a scelta", "Elective course"),
        ("Frequenza obbligatoria", "Mandatory attendance"), ("Piano di studi", "Study plan"),
        ("Segreteria studenti", "Student office"), ("Tirocinio formativo", "Training internship"),
        ("Progetto di gruppo", "Group project"), ("Presentazione orale", "Oral presentation"),
        ("Esame scritto", "Written exam"), ("Esame orale", "Oral exam"),
        ("Fuoricorso", "Behind schedule / extra-curricular years"), ("Laurea triennale", "Bachelor's degree"),
        ("Laurea magistrale", "Master's degree"), ("Dottorato di ricerca", "PhD"),
        ("Scambiare appunti", "To exchange notes"), ("Studiare in biblioteca", "To study in the library")
    ]
    
    phrase_data = []
    for i, (it, en) in enumerate(phrase_list):
        choices_it = [it]
        choices_en = [en]
        others = [p for p in phrase_list if p != (it, en)]
        random.seed(i+100)
        distractors = random.sample(others, 3)
        for d_it, d_en in distractors:
            choices_it.append(d_it)
            choices_en.append(d_en)
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        
        phrase_data.append({
            "id": f"{prefix}-p{i+1:02d}",
            "type": "phrase",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correctItalian": f"Ottimo! '{it}' si traduce come '{en}'.",
                "incorrectItalian": f"Quasi, ma la risposta corretta è '{it}'.",
                "correctEnglish": f"Great! '{en}' means '{it}' in Italian.",
                "incorrectEnglish": f"Actually, the correct translation is '{en}'."
            }
        })

    # Sentences (Min 60) - Dialogue-like
    sentence_list = [
        ("È libero questo posto?", "Is this seat free?"),
        ("No, è occupato.", "No, it's occupied."),
        ("Raccoglie le tesine oggi?", "Is he collecting term papers today?"),
        ("Sì, è l'ultimo giorno.", "Yes, it's the last day."),
        ("Hai scelto l'argomento?", "Have you chosen the topic?"),
        ("Sì, sociologia del lavoro.", "Yes, sociology of work."),
        ("Il professore è severo?", "Is the professor strict?"),
        ("Dicono di sì all'esame.", "They say so for the exam."),
        ("Prendi tu gli appunti?", "Are you taking notes?"),
        ("Sì, poi te li passo.", "Yes, I'll give them to you later."),
        ("Dov'è l'aula magna?", "Where is the great hall?"),
        ("In fondo al corridoio.", "At the end of the corridor."),
        ("A che ora inizia?", "What time does it start?"),
        ("Alle nove precise.", "At nine sharp."),
        ("Hai finito la tesina?", "Have you finished the term paper?"),
        ("Quasi, mi manca poco.", "Almost, I'm nearly done."),
        ("Caricala sul portale.", "Upload it to the portal."),
        ("Entro mezzanotte, giusto?", "By midnight, right?"),
        ("Ho preso trenta!", "I got a thirty!"),
        ("Bravissimo, complimenti!", "Well done, congratulations!"),
        ("Mi presti una penna?", "Can you lend me a pen?"),
        ("Sì, tieni pure.", "Yes, here you go."),
        ("Dov'è la segreteria?", "Where is the student office?"),
        ("Al piano terra.", "On the ground floor."),
        ("C'è il wifi qui?", "Is there wifi here?"),
        ("Sì, ma non funziona bene.", "Yes, but it doesn't work well."),
        ("Andiamo in mensa?", "Shall we go to the canteen?"),
        ("Sì, ho una fame!", "Yes, I'm starving!"),
        ("Quanti crediti vale?", "How many credits is it worth?"),
        ("Sei crediti formativi.", "Six educational credits."),
        ("L'esame è scritto?", "Is the exam written?"),
        ("No, solo orale.", "No, only oral."),
        ("Hai visto l'orario?", "Have you seen the timetable?"),
        ("Sì, è in bacheca.", "Yes, it's on the bulletin board."),
        ("Quando ti laurei?", "When do you graduate?"),
        ("Spero a luglio.", "I hope in July."),
        ("Chi è il tuo relatore?", "Who is your supervisor?"),
        ("Il professor Bianchi.", "Professor Bianchi."),
        ("Hai vinto la borsa?", "Did you win the scholarship?"),
        ("Sì, meno male!", "Yes, thank goodness!"),
        ("Studiamo in biblioteca?", "Shall we study in the library?"),
        ("Preferisco a casa.", "I prefer at home."),
        ("Hai le slide?", "Do you have the slides?"),
        ("Le scarico subito.", "I'll download them right now."),
        ("Com'è andata la prova?", "How did the test go?"),
        ("Bene, sono promosso!", "Well, I passed!"),
        ("Ti sei iscritto?", "Did you enroll?"),
        ("Sì, ieri sera.", "Yes, last night."),
        ("Qual è la tua matricola?", "What is your student ID?"),
        ("Non me la ricordo.", "I don't remember it."),
        ("C'è molta gente.", "There are a lot of people."),
        ("Sì, l'aula è piena.", "Yes, the classroom is full."),
        ("Puoi ripetere?", "Can you repeat?"),
        ("Ha parlato troppo veloce.", "He spoke too fast."),
        ("Facciamo un gruppo?", "Shall we make a group?"),
        ("Sì, per il progetto.", "Yes, for the project."),
        ("Hai il libretto?", "Do you have the record book?"),
        ("Sì, è nello zaino.", "Yes, it's in the backpack."),
        ("Quando c'è l'appello?", "When is the exam session?"),
        ("Lunedì alle dieci.", "Monday at ten."),
        ("Ho perso gli appunti.", "I lost my notes."),
        ("Te li do io.", "I'll give them to you."),
        ("Il portale è bloccato.", "The portal is blocked."),
        ("Riprova più tardi.", "Try again later.")
    ]
    
    sentence_data = []
    for i, (it, en) in enumerate(sentence_list):
        choices_it = [it]
        choices_en = [en]
        others = [s for s in sentence_list if s != (it, en)]
        random.seed(i+200)
        distractors = random.sample(others, 3)
        for d_it, d_en in distractors:
            choices_it.append(d_it)
            choices_en.append(d_en)
        combined = list(zip(choices_it, choices_en))
        random.shuffle(combined)
        choices_it, choices_en = zip(*combined)
        
        sentence_data.append({
            "id": f"{prefix}-s{i+1:02d}",
            "type": "sentence",
            "choicesItalian": list(choices_it),
            "choicesEnglish": list(choices_en),
            "correctAnswerItalian": it,
            "correctAnswerEnglish": en,
            "feedback": {
                "correctItalian": f"Perfetto! '{it}' significa '{en}'.",
                "incorrectItalian": f"No, la risposta era '{it}'.",
                "correctEnglish": f"Excellent! '{en}' is the correct meaning.",
                "incorrectEnglish": f"Actually, '{en}' was the correct choice."
            }
        })

    with open(os.path.join(base_path, f"{scenario}_vocabulary.json"), "w") as f:
        json.dump(vocab_data, f, indent=2, ensure_ascii=False)
    with open(os.path.join(base_path, f"{scenario}_phrases.json"), "w") as f:
        json.dump(phrase_data, f, indent=2, ensure_ascii=False)
    with open(os.path.join(base_path, f"{scenario}_sentences.json"), "w") as f:
        json.dump(sentence_data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    generate_university_class()
