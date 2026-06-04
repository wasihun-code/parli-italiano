import json
import os

conversations_data = {
  "scenarioId": 65,
  "conversations": [
    {
      "id": "asking_a_question",
      "title": "Asking a Question in Class",
      "description": "A student asks the professor a question during the lecture.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Buongiorno ragazzi, oggi parliamo della storia romana.",
          "english": "Good morning guys, today we talk about Roman history."
        },
        {
          "id": "m2",
          "role": "learner",
          "text": "Scusi professore, ho una domanda sulla lezione.",
          "english": "Excuse me professor, I have a question about the lecture.",
          "choices": [
            {
              "text": "Scusi professore, ho una domanda sulla lezione.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Scusi professore, ho una cipolla sulla zanzara.",
              "isCorrect": False,
              "feedback": "Nonsensical."
            },
            {
              "text": "Scusi infermiere, ho una maniglia sulla porta.",
              "isCorrect": False,
              "feedback": "Wrong vocabulary."
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Certo, dimmi pure. Cosa non è chiaro?",
          "english": "Sure, go ahead. What is not clear?"
        },
        {
          "id": "m4",
          "role": "learner",
          "text": "Non ho capito bene la data dell'esame finale.",
          "english": "I didn't quite understand the date of the final exam.",
          "choices": [
            {
              "text": "Non ho capito bene la data dell'esame finale.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Non ho mangiato bene la torta dell'amico finale.",
              "isCorrect": False,
              "feedback": "Wrong verbs and nouns."
            },
            {
              "text": "Non ho creduto bene la luna dell'albero finale.",
              "isCorrect": False,
              "feedback": "Nonsensical."
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "L'esame sarà il quindici dicembre in quest'aula.",
          "english": "The exam will be on December 15th in this classroom."
        },
        {
          "id": "m6",
          "role": "learner",
          "text": "Grazie mille, lo scrivo subito nei miei appunti.",
          "english": "Thank you very much, I'll write it down in my notes right away.",
          "choices": [
            {
              "text": "Grazie mille, lo scrivo subito nei miei appunti.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Grazie mille, lo ballo subito nei miei biscotti.",
              "isCorrect": False,
              "feedback": "Nonsense."
            },
            {
              "text": "Grazie mille, lo taglio subito nei miei cappotti.",
              "isCorrect": False,
              "feedback": "Nonsense."
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Hai altre domande sul capitolo tre del libro?",
          "english": "Do you have other questions on chapter three of the book?"
        },
        {
          "id": "m8",
          "role": "learner",
          "text": "No, per ora è tutto chiaro, grazie professore.",
          "english": "No, for now everything is clear, thank you professor.",
          "choices": [
            {
              "text": "No, per ora è tutto chiaro, grazie professore.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "No, per ora è tutto amaro, grazie controllore.",
              "isCorrect": False,
              "feedback": "Wrong."
            },
            {
              "text": "No, per ora è tutto scuro, grazie viaggiatore.",
              "isCorrect": False,
              "feedback": "Wrong."
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Molto bene, allora possiamo continuare la lezione.",
          "english": "Very well, then we can continue the lecture."
        },
        {
          "id": "m10",
          "role": "learner",
          "text": "Perfetto, sono pronto per prendere altri appunti.",
          "english": "Perfect, I am ready to take more notes.",
          "choices": [
            {
              "text": "Perfetto, sono pronto per prendere altri appunti.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Perfetto, sono giunto per spingere altri appunti.",
              "isCorrect": False,
              "feedback": "Wrong verbs."
            },
            {
              "text": "Perfetto, sono fritto per vendere altri appunti.",
              "isCorrect": False,
              "feedback": "Wrong."
            }
          ]
        }
      ]
    },
    {
      "id": "talking_syllabus",
      "title": "Talking about the Syllabus",
      "description": "Two students talk about the syllabus for the semester.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Ciao! Hai già letto il programma del corso?",
          "english": "Hi! Have you already read the course syllabus?"
        },
        {
          "id": "m2",
          "role": "learner",
          "text": "Ciao, sì, l'ho appena scaricato dal sito dell'università.",
          "english": "Hi, yes, I just downloaded it from the university website.",
          "choices": [
            {
              "text": "Ciao, sì, l'ho appena scaricato dal sito dell'università.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Ciao, sì, l'ho appena dimenticato dal muro dell'università.",
              "isCorrect": False,
              "feedback": "Wrong."
            },
            {
              "text": "Ciao, sì, l'ho appena masticato dal sito dell'università.",
              "isCorrect": False,
              "feedback": "Wrong."
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Sembra che ci siano molti libri da leggere quest'anno.",
          "english": "It seems there are many books to read this year."
        },
        {
          "id": "m4",
          "role": "learner",
          "text": "È vero, credo che andrò in biblioteca questo pomeriggio.",
          "english": "That's true, I think I will go to the library this afternoon.",
          "choices": [
            {
              "text": "È vero, credo che andrò in biblioteca questo pomeriggio.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "È vero, credo che andrò in discoteca questo pomeriggio.",
              "isCorrect": False,
              "feedback": "Wrong context."
            },
            {
              "text": "È vero, credo che andrò in farmacia questo pomeriggio.",
              "isCorrect": False,
              "feedback": "Wrong context."
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Anch'io devo studiare. Studiamo insieme in aula studio?",
          "english": "I have to study too. Shall we study together in the study room?"
        },
        {
          "id": "m6",
          "role": "learner",
          "text": "Ottima idea, così possiamo aiutarci con gli appunti.",
          "english": "Great idea, that way we can help each other with the notes.",
          "choices": [
            {
              "text": "Ottima idea, così possiamo aiutarci con gli appunti.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Ottima idea, così possiamo truccarci con gli specchi.",
              "isCorrect": False,
              "feedback": "Wrong."
            },
            {
              "text": "Ottima idea, così possiamo lanciarci con gli stivali.",
              "isCorrect": False,
              "feedback": "Wrong."
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Ci vediamo lì verso le tre del pomeriggio?",
          "english": "See you there around three in the afternoon?"
        },
        {
          "id": "m8",
          "role": "learner",
          "text": "Perfetto, porto anche il mio computer per cercare online.",
          "english": "Perfect, I'll also bring my computer to search online.",
          "choices": [
            {
              "text": "Perfetto, porto anche il mio computer per cercare online.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Perfetto, porto anche il mio gatto per cercare online.",
              "isCorrect": False,
              "feedback": "Wrong."
            },
            {
              "text": "Perfetto, porto anche il mio cuscino per dormire online.",
              "isCorrect": False,
              "feedback": "Wrong."
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "A più tardi allora, non fare ritardo!",
          "english": "See you later then, don't be late!"
        },
        {
          "id": "m10",
          "role": "learner",
          "text": "Tranquillo, sarò puntuale come sempre. A dopo!",
          "english": "Don't worry, I'll be punctual as always. See you later!",
          "choices": [
            {
              "text": "Tranquillo, sarò puntuale come sempre. A dopo!",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Tranquillo, sarò noioso come sempre. A dopo!",
              "isCorrect": False,
              "feedback": "Wrong."
            },
            {
              "text": "Tranquillo, sarò bagnato come sempre. A dopo!",
              "isCorrect": False,
              "feedback": "Wrong."
            }
          ]
        }
      ]
    },
    {
      "id": "borrowing_notes",
      "title": "Borrowing Notes from a Classmate",
      "description": "A student asks to borrow a classmate's notes from a missed lecture.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Ehi, dove eri ieri? Non ti ho visto a lezione.",
          "english": "Hey, where were you yesterday? I didn't see you in class."
        },
        {
          "id": "m2",
          "role": "learner",
          "text": "Ero malato e non sono potuto venire all'università.",
          "english": "I was sick and couldn't come to the university.",
          "choices": [
            {
              "text": "Ero malato e non sono potuto venire all'università.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Ero gelato e non sono potuto partire all'università.",
              "isCorrect": False,
              "feedback": "Wrong words."
            },
            {
              "text": "Ero salato e non sono potuto volare all'università.",
              "isCorrect": False,
              "feedback": "Wrong words."
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Mi dispiace, stai meglio oggi?",
          "english": "I'm sorry, are you better today?"
        },
        {
          "id": "m4",
          "role": "learner",
          "text": "Sì, grazie. Potresti prestarmi i tuoi appunti di ieri?",
          "english": "Yes, thanks. Could you lend me your notes from yesterday?",
          "choices": [
            {
              "text": "Sì, grazie. Potresti prestarmi i tuoi appunti di ieri?",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Sì, grazie. Potresti mangiarmi i tuoi appunti di ieri?",
              "isCorrect": False,
              "feedback": "Wrong verb."
            },
            {
              "text": "Sì, grazie. Potresti gettarmi i tuoi appunti di ieri?",
              "isCorrect": False,
              "feedback": "Wrong verb."
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Certamente! Il professore ha spiegato un nuovo capitolo importante.",
          "english": "Certainly! The professor explained an important new chapter."
        },
        {
          "id": "m6",
          "role": "learner",
          "text": "Posso fare delle fotocopie prima della prossima lezione?",
          "english": "Can I make some photocopies before the next class?",
          "choices": [
            {
              "text": "Posso fare delle fotocopie prima della prossima lezione?",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Posso fare delle fotografie prima della prossima lezione?",
              "isCorrect": False,
              "feedback": "Wrong."
            },
            {
              "text": "Posso fare delle melodie prima della prossima lezione?",
              "isCorrect": False,
              "feedback": "Wrong."
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Sì, andiamo in biblioteca insieme, ci sono le stampanti.",
          "english": "Yes, let's go to the library together, there are printers."
        },
        {
          "id": "m8",
          "role": "learner",
          "text": "Perfetto, ti offro un caffè per ringraziarti.",
          "english": "Perfect, I'll buy you a coffee to thank you.",
          "choices": [
            {
              "text": "Perfetto, ti offro un caffè per ringraziarti.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Perfetto, ti offro un pesce per ringraziarti.",
              "isCorrect": False,
              "feedback": "Wrong context."
            },
            {
              "text": "Perfetto, ti offro un cane per ringraziarti.",
              "isCorrect": False,
              "feedback": "Wrong context."
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Accetto volentieri, un caffè mi serve per restare sveglio.",
          "english": "I accept gladly, I need a coffee to stay awake."
        },
        {
          "id": "m10",
          "role": "learner",
          "text": "Ottimo, poi studiamo insieme in aula.",
          "english": "Excellent, then we study together in the classroom.",
          "choices": [
            {
              "text": "Ottimo, poi studiamo insieme in aula.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Ottimo, poi balliamo insieme in aula.",
              "isCorrect": False,
              "feedback": "Wrong context."
            },
            {
              "text": "Ottimo, poi nuotiamo insieme in aula.",
              "isCorrect": False,
              "feedback": "Wrong context."
            }
          ]
        }
      ]
    },
    {
      "id": "exam_dates",
      "title": "Inquiring about Exam Dates",
      "description": "A student asks the administration office about the exam dates.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Buongiorno, segreteria studenti. Come posso aiutarla?",
          "english": "Good morning, student secretariat. How can I help you?"
        },
        {
          "id": "m2",
          "role": "learner",
          "text": "Buongiorno, vorrei delle informazioni sulle date degli esami.",
          "english": "Good morning, I would like some information on the exam dates.",
          "choices": [
            {
              "text": "Buongiorno, vorrei delle informazioni sulle date degli esami.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Buongiorno, vorrei delle mutazioni sulle date degli esami.",
              "isCorrect": False,
              "feedback": "Wrong words."
            },
            {
              "text": "Buongiorno, vorrei delle informazioni sulle pere degli esami.",
              "isCorrect": False,
              "feedback": "Wrong words."
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Di quale corso di laurea stiamo parlando?",
          "english": "Which degree course are we talking about?"
        },
        {
          "id": "m4",
          "role": "learner",
          "text": "Sono uno studente di economia, primo anno.",
          "english": "I am an economics student, first year.",
          "choices": [
            {
              "text": "Sono uno studente di economia, primo anno.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Sono un serpente di economia, primo anno.",
              "isCorrect": False,
              "feedback": "Wrong noun."
            },
            {
              "text": "Sono uno studente di pasticceria, primo anno.",
              "isCorrect": False,
              "feedback": "Wrong context."
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Le date sono sul portale. Devi fare l'iscrizione online.",
          "english": "The dates are on the portal. You must register online."
        },
        {
          "id": "m6",
          "role": "learner",
          "text": "Entro quando devo iscrivermi per la prima sessione?",
          "english": "By when do I have to register for the first session?",
          "choices": [
            {
              "text": "Entro quando devo iscrivermi per la prima sessione?",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Entro quando devo nascondermi per la prima sessione?",
              "isCorrect": False,
              "feedback": "Wrong verb."
            },
            {
              "text": "Entro quando devo lavarmi per la prima sessione?",
              "isCorrect": False,
              "feedback": "Wrong verb."
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Hai tempo fino alla fine di questa settimana.",
          "english": "You have time until the end of this week."
        },
        {
          "id": "m8",
          "role": "learner",
          "text": "Grazie, posso anche chiedere informazioni sulla borsa di studio?",
          "english": "Thank you, can I also ask for information about the scholarship?",
          "choices": [
            {
              "text": "Grazie, posso anche chiedere informazioni sulla borsa di studio?",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "Grazie, posso anche chiedere informazioni sulla borsa di ghiaccio?",
              "isCorrect": False,
              "feedback": "Wrong."
            },
            {
              "text": "Grazie, posso anche chiedere informazioni sulla borsa di plastica?",
              "isCorrect": False,
              "feedback": "Wrong."
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Sì, per la borsa di studio devi andare allo sportello tre.",
          "english": "Yes, for the scholarship you must go to counter three."
        },
        {
          "id": "m10",
          "role": "learner",
          "text": "La ringrazio molto per il suo aiuto, arrivederci.",
          "english": "Thank you very much for your help, goodbye.",
          "choices": [
            {
              "text": "La ringrazio molto per il suo aiuto, arrivederci.",
              "isCorrect": True,
              "feedback": "Correct."
            },
            {
              "text": "La ringrazio molto per il suo maiale, arrivederci.",
              "isCorrect": False,
              "feedback": "Wrong word."
            },
            {
              "text": "La ringrazio molto per il suo stivale, arrivederci.",
              "isCorrect": False,
              "feedback": "Wrong word."
            }
          ]
        }
      ]
    }
  ]
}

os.makedirs('src/data/exports/workstudy/university_class', exist_ok=True)
with open('src/data/exports/workstudy/university_class/conversations.json', 'w') as f:
    json.dump(conversations_data, f, indent=2)

print("Created conversations.json")
