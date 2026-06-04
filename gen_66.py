import json
import os

scenario_id = 66
base_dir = "src/data/exports/workstudy/language_school"
os.makedirs(base_dir, exist_ok=True)

conversations = {
    "scenarioId": scenario_id,
    "conversations": [
        {
            "id": "inquiring_courses",
            "title": "Inquiring about Courses",
            "description": "A student asks the school receptionist about available Italian courses for beginners.",
            "messages": [
                {
                    "id": "m1",
                    "role": "host",
                    "text": "Buongiorno! Come posso aiutare oggi?",
                    "english": "Good morning! How can I help today?",
                    "choices": [
                        {
                            "text": "Buongiorno. Cerco un corso di italiano.",
                            "isCorrect": True,
                            "feedback": "Perfect! You stated your goal clearly."
                        },
                        {
                            "text": "Buonasera. Prendo un pezzo di formaggio.",
                            "isCorrect": False,
                            "feedback": "You are at a language school, not a cheese shop."
                        },
                        {
                            "text": "Arrivederci. Vendo un libro di spagnolo.",
                            "isCorrect": False,
                            "feedback": "You are trying to enroll, not sell a book."
                        }
                    ]
                },
                {
                    "id": "m2",
                    "role": "host",
                    "text": "Bene. Abbiamo molti corsi. Qual è il suo livello?",
                    "english": "Good. We have many courses. What is your level?",
                    "choices": [
                        {
                            "text": "Sono un principiante. Non parlo molto.",
                            "isCorrect": True,
                            "feedback": "Excellent. Stating your level helps them choose the right class."
                        },
                        {
                            "text": "Sono un veterinario. Non dormo tanto.",
                            "isCorrect": False,
                            "feedback": "They are asking for your language level, not your profession."
                        },
                        {
                            "text": "Vedo un termosifone. Non mangio quasi.",
                            "isCorrect": False,
                            "feedback": "Irrelevant response."
                        }
                    ]
                },
                {
                    "id": "m3",
                    "role": "host",
                    "text": "Capisco. Il corso per principianti inizia domani.",
                    "english": "I understand. The course for beginners starts tomorrow.",
                    "choices": [
                        {
                            "text": "Ottimo. Quante ore di lezione fate?",
                            "isCorrect": True,
                            "feedback": "Great question to know the schedule."
                        },
                        {
                            "text": "Niente. Quante api di sapore vuoi?",
                            "isCorrect": False,
                            "feedback": "Nonsense sentence."
                        },
                        {
                            "text": "Subito. Quante zie di collane dai?",
                            "isCorrect": False,
                            "feedback": "This means nothing in this context."
                        }
                    ]
                },
                {
                    "id": "m4",
                    "role": "host",
                    "text": "Facciamo due ore di lezione al giorno.",
                    "english": "We do two hours of lessons a day.",
                    "choices": [
                        {
                            "text": "Va bene. A che ora è la lezione?",
                            "isCorrect": True,
                            "feedback": "Perfect! Asking for the exact time."
                        },
                        {
                            "text": "Ho fame. A che lui è un balcone?",
                            "isCorrect": False,
                            "feedback": "This makes no sense."
                        },
                        {
                            "text": "Di sera. A che lei è un mattone?",
                            "isCorrect": False,
                            "feedback": "Incorrect grammar and context."
                        }
                    ]
                },
                {
                    "id": "m5",
                    "role": "host",
                    "text": "La lezione è la mattina, alle dieci.",
                    "english": "The lesson is in the morning, at ten.",
                    "choices": [
                        {
                            "text": "Perfetto. Come faccio l'iscrizione adesso?",
                            "isCorrect": True,
                            "feedback": "Good! Moving to the next step, enrollment."
                        },
                        {
                            "text": "Sospetto. Come cerco la redazione ancora?",
                            "isCorrect": False,
                            "feedback": "This does not fit the context."
                        },
                        {
                            "text": "Corretto. Come perdo l'estensione sempre?",
                            "isCorrect": False,
                            "feedback": "Wrong vocabulary."
                        }
                    ]
                }
            ]
        },
        {
            "id": "placement_test",
            "title": "Taking a Placement Test",
            "description": "A student asks about the placement test to determine their language level.",
            "messages": [
                {
                    "id": "m6",
                    "role": "host",
                    "text": "Buongiorno. Vuole fare il test di livello?",
                    "english": "Good morning. Do you want to take the level test?",
                    "choices": [
                        {
                            "text": "Sì, grazie. Come funziona il test?",
                            "isCorrect": True,
                            "feedback": "Great question to understand the process."
                        },
                        {
                            "text": "No, prego. Dove scompare il treno?",
                            "isCorrect": False,
                            "feedback": "You are asking about the test, not a train."
                        },
                        {
                            "text": "Ma, chiaro. Come peggiora un letto?",
                            "isCorrect": False,
                            "feedback": "Irrelevant sentence."
                        }
                    ]
                },
                {
                    "id": "m7",
                    "role": "host",
                    "text": "Ci sono domande di grammatica e conversazione.",
                    "english": "There are questions on grammar and conversation.",
                    "choices": [
                        {
                            "text": "Quanto tempo ho per fare il test?",
                            "isCorrect": True,
                            "feedback": "Excellent. Asking about the time limit."
                        },
                        {
                            "text": "Quando canto tu per bere un vino?",
                            "isCorrect": False,
                            "feedback": "Nonsense question."
                        },
                        {
                            "text": "Quante scarpe ha per dare il sole?",
                            "isCorrect": False,
                            "feedback": "You are talking about shoes and sun, not the test."
                        }
                    ]
                },
                {
                    "id": "m8",
                    "role": "host",
                    "text": "Ha un'ora di tempo. Può iniziare subito.",
                    "english": "You have an hour of time. You can start right away.",
                    "choices": [
                        {
                            "text": "Va bene. Posso usare il mio telefono?",
                            "isCorrect": True,
                            "feedback": "Good to ask about the rules of the test."
                        },
                        {
                            "text": "Ho fame. Vendo avere un tuo specchio?",
                            "isCorrect": False,
                            "feedback": "You are talking about a mirror."
                        },
                        {
                            "text": "Di sera. Cerco amare un suo semaforo?",
                            "isCorrect": False,
                            "feedback": "Nonsense."
                        }
                    ]
                },
                {
                    "id": "m9",
                    "role": "host",
                    "text": "No, mi dispiace. Non può usare il telefono.",
                    "english": "No, I'm sorry. You can't use the phone.",
                    "choices": [
                        {
                            "text": "Capisco. Dove devo sedermi per iniziare?",
                            "isCorrect": True,
                            "feedback": "Perfect. Asking for directions to sit."
                        },
                        {
                            "text": "Conosco. Quando vado lavarmi per abitare?",
                            "isCorrect": False,
                            "feedback": "This is completely wrong."
                        },
                        {
                            "text": "Pulisco. Come sono tuffarmi per nuotare?",
                            "isCorrect": False,
                            "feedback": "This means cleaning and swimming."
                        }
                    ]
                },
                {
                    "id": "m10",
                    "role": "host",
                    "text": "Può sedersi a quel tavolo, in fondo.",
                    "english": "You can sit at that table, in the back.",
                    "choices": [
                        {
                            "text": "Grazie. Quando posso sapere il risultato?",
                            "isCorrect": True,
                            "feedback": "Good! Asking about the outcome."
                        },
                        {
                            "text": "Niente. Quanto corro volere un cucchiaio?",
                            "isCorrect": False,
                            "feedback": "You are asking for a spoon while running."
                        },
                        {
                            "text": "Presto. Perché voglio cadere il panettiere?",
                            "isCorrect": False,
                            "feedback": "Nonsense question."
                        }
                    ]
                }
            ]
        },
        {
            "id": "class_times",
            "title": "Asking about Class Times",
            "description": "A student asks about the class schedule and times.",
            "messages": [
                {
                    "id": "m11",
                    "role": "host",
                    "text": "Salve! Ha domande sull'orario delle lezioni?",
                    "english": "Hello! Do you have questions about the lesson schedule?",
                    "choices": [
                        {
                            "text": "Sì. Voglio sapere l'orario del corso serale.",
                            "isCorrect": True,
                            "feedback": "Excellent response confirming what you want to know."
                        },
                        {
                            "text": "No. Prendo vedere un'attrice del posto locale.",
                            "isCorrect": False,
                            "feedback": "This is entirely unrelated."
                        },
                        {
                            "text": "Ma. Pulisco lavare il gatto di zia geniale.",
                            "isCorrect": False,
                            "feedback": "Cleaning the cat is not about class times."
                        }
                    ]
                },
                {
                    "id": "m12",
                    "role": "host",
                    "text": "Il corso serale è dalle diciotto alle venti.",
                    "english": "The evening course is from eighteen to twenty.",
                    "choices": [
                        {
                            "text": "Quali giorni della settimana fate lezione?",
                            "isCorrect": True,
                            "feedback": "Good follow-up question."
                        },
                        {
                            "text": "Quanti nonni sulla bicicletta date melone?",
                            "isCorrect": False,
                            "feedback": "This mentions grandpas and melons."
                        },
                        {
                            "text": "Nuovi forni nella caramella male pensione?",
                            "isCorrect": False,
                            "feedback": "Nonsense."
                        }
                    ]
                },
                {
                    "id": "m13",
                    "role": "host",
                    "text": "Le lezioni sono il lunedì e il mercoledì.",
                    "english": "The lessons are on Monday and Wednesday.",
                    "choices": [
                        {
                            "text": "È possibile cambiare classe la prossima settimana?",
                            "isCorrect": True,
                            "feedback": "Great question regarding flexibility."
                        },
                        {
                            "text": "O adorabile scambiare penne una brutta passeggiata?",
                            "isCorrect": False,
                            "feedback": "This means swapping pens on a bad walk."
                        },
                        {
                            "text": "I probabile comprare pesce una bianca camminata?",
                            "isCorrect": False,
                            "feedback": "Buying fish on a walk."
                        }
                    ]
                },
                {
                    "id": "m14",
                    "role": "host",
                    "text": "Sì, ma deve chiedere prima all'insegnante.",
                    "english": "Yes, but you must ask the teacher first.",
                    "choices": [
                        {
                            "text": "Capisco. Quanti studenti ci sono in classe?",
                            "isCorrect": True,
                            "feedback": "Perfect! Getting details about the class size."
                        },
                        {
                            "text": "Conosco. Quanto profumo ha peso un vassoio?",
                            "isCorrect": False,
                            "feedback": "Perfume on a tray is not relevant."
                        },
                        {
                            "text": "Pulisco. Questo castello no male un divano?",
                            "isCorrect": False,
                            "feedback": "This sentence is nonsense."
                        }
                    ]
                },
                {
                    "id": "m15",
                    "role": "host",
                    "text": "Ci sono massimo dieci studenti per classe.",
                    "english": "There are maximum ten students per class.",
                    "choices": [
                        {
                            "text": "Molto bene. C'è anche una lezione il venerdì?",
                            "isCorrect": True,
                            "feedback": "Good! Clarifying the end of the week."
                        },
                        {
                            "text": "Poco male. C'è oltre una canzone un giovedì?",
                            "isCorrect": False,
                            "feedback": "This talks about a song on a Thursday."
                        },
                        {
                            "text": "Tanto nero. C'è quasi una pozione un martedì?",
                            "isCorrect": False,
                            "feedback": "A potion on a Tuesday."
                        }
                    ]
                }
            ]
        },
        {
            "id": "paying_course",
            "title": "Paying for the Course",
            "description": "A student pays for the course and asks about textbook costs.",
            "messages": [
                {
                    "id": "m16",
                    "role": "host",
                    "text": "Buongiorno. Vuole fare il pagamento per il corso?",
                    "english": "Good morning. Do you want to make the payment for the course?",
                    "choices": [
                        {
                            "text": "Sì, voglio pagare il corso di italiano.",
                            "isCorrect": True,
                            "feedback": "Perfect. You confirmed you want to pay."
                        },
                        {
                            "text": "No, perdo nuotare in parco di spagnolo.",
                            "isCorrect": False,
                            "feedback": "Swimming in a Spanish park."
                        },
                        {
                            "text": "Ma, porto suonare un corno di olandese.",
                            "isCorrect": False,
                            "feedback": "Playing a Dutch horn."
                        }
                    ]
                },
                {
                    "id": "m17",
                    "role": "host",
                    "text": "Il costo del corso è di duecento euro.",
                    "english": "The cost of the course is two hundred euros.",
                    "choices": [
                        {
                            "text": "Il libro di testo è incluso nel prezzo?",
                            "isCorrect": True,
                            "feedback": "Great question to avoid hidden costs."
                        },
                        {
                            "text": "Un litro di latte è confuso nel freddo?",
                            "isCorrect": False,
                            "feedback": "Milk in the cold."
                        },
                        {
                            "text": "La tigre di ferro è delusa sul tetto?",
                            "isCorrect": False,
                            "feedback": "An iron tiger on the roof."
                        }
                    ]
                },
                {
                    "id": "m18",
                    "role": "host",
                    "text": "No, il libro costa venti euro in più.",
                    "english": "No, the book costs twenty euros more.",
                    "choices": [
                        {
                            "text": "Va bene. Pago il corso e il libro.",
                            "isCorrect": True,
                            "feedback": "Perfect! Resolving the payment."
                        },
                        {
                            "text": "Di sera. Bacio un cane e un vetro.",
                            "isCorrect": False,
                            "feedback": "Kissing a dog and a glass."
                        },
                        {
                            "text": "Ho fame. Lavo un treno e un parco.",
                            "isCorrect": False,
                            "feedback": "Washing a train and a park."
                        }
                    ]
                },
                {
                    "id": "m19",
                    "role": "host",
                    "text": "Come vuole pagare? In contanti o con carta?",
                    "english": "How do you want to pay? In cash or with card?",
                    "choices": [
                        {
                            "text": "Voglio pagare con la carta, per favore.",
                            "isCorrect": True,
                            "feedback": "Clear answer about the payment method."
                        },
                        {
                            "text": "Soffro volare con il pollo, dal dottore.",
                            "isCorrect": False,
                            "feedback": "Flying with chicken to the doctor."
                        },
                        {
                            "text": "Prendo andare con una barca, per rumore.",
                            "isCorrect": False,
                            "feedback": "Going with a boat for noise."
                        }
                    ]
                },
                {
                    "id": "m20",
                    "role": "host",
                    "text": "Certamente. Può inserire la carta qui.",
                    "english": "Certainly. You can insert the card here.",
                    "choices": [
                        {
                            "text": "Fatto. Devo inserire anche il mio codice?",
                            "isCorrect": True,
                            "feedback": "Good question about the PIN code."
                        },
                        {
                            "text": "Cotto. Bevo superare oltre un tuo medico?",
                            "isCorrect": False,
                            "feedback": "Nonsense question."
                        },
                        {
                            "text": "Rotto. Cado imparare forse un suo vigile?",
                            "isCorrect": False,
                            "feedback": "This has no meaning."
                        }
                    ]
                }
            ]
        }
    ]
}

with open(f"{base_dir}/conversations.json", "w", encoding="utf-8") as f:
    json.dump(conversations, f, ensure_ascii=False, indent=2)

mini_lessons = {
  "lessons": [
    {
      "id": "l1",
      "title": "Welcome",
      "goal": "Greeting and Inquiring",
      "estimatedDuration": "3 mins",
      "unlockCriteria": "none",
      "nextLesson": "l2",
      "sections": [
        {
          "type": "vocabulary",
          "title": "Core Vocabulary",
          "description": "Learn essential words.",
          "exerciseIds": ["s66-v1", "s66-v2", "s66-v3", "s66-v4"]
        },
        {
          "type": "phrase",
          "title": "Key Phrases",
          "description": "Learn key phrases.",
          "exerciseIds": ["s66-p1", "s66-p2"]
        }
      ]
    },
    {
      "id": "l2",
      "title": "The Schedule",
      "goal": "Asking about class times",
      "estimatedDuration": "3 mins",
      "unlockCriteria": "l1",
      "nextLesson": "l3",
      "sections": [
        {
          "type": "vocabulary",
          "title": "Time Vocabulary",
          "description": "Words about time.",
          "exerciseIds": ["s66-v5", "s66-v6", "s66-v7", "s66-v8"]
        },
        {
          "type": "phrase",
          "title": "Time Phrases",
          "description": "Phrases about schedule.",
          "exerciseIds": ["s66-p3", "s66-p4"]
        }
      ]
    },
    {
      "id": "l3",
      "title": "Placement Test",
      "goal": "Understanding test rules",
      "estimatedDuration": "3 mins",
      "unlockCriteria": "l2",
      "nextLesson": "l4",
      "sections": [
        {
          "type": "vocabulary",
          "title": "Test Vocabulary",
          "description": "Words for testing.",
          "exerciseIds": ["s66-v9", "s66-v10", "s66-v11", "s66-v12"]
        },
        {
          "type": "phrase",
          "title": "Test Phrases",
          "description": "Phrases for taking a test.",
          "exerciseIds": ["s66-p5", "s66-p6"]
        }
      ]
    },
    {
      "id": "l4",
      "title": "Class Rules",
      "goal": "Knowing school rules",
      "estimatedDuration": "3 mins",
      "unlockCriteria": "l3",
      "nextLesson": "l5",
      "sections": [
        {
          "type": "vocabulary",
          "title": "Rules Vocabulary",
          "description": "Words about rules.",
          "exerciseIds": ["s66-v13", "s66-v14", "s66-v15", "s66-v16"]
        },
        {
          "type": "phrase",
          "title": "Rules Phrases",
          "description": "Phrases about rules.",
          "exerciseIds": ["s66-p7", "s66-p8"]
        }
      ]
    },
    {
      "id": "l5",
      "title": "Paying Tuition",
      "goal": "Paying for the course",
      "estimatedDuration": "3 mins",
      "unlockCriteria": "l4",
      "nextLesson": "l6",
      "sections": [
        {
          "type": "vocabulary",
          "title": "Money Vocabulary",
          "description": "Words about paying.",
          "exerciseIds": ["s66-v17", "s66-v18", "s66-v19", "s66-v20"]
        },
        {
          "type": "phrase",
          "title": "Money Phrases",
          "description": "Phrases for paying.",
          "exerciseIds": ["s66-p9", "s66-p10"]
        }
      ]
    },
    {
      "id": "l6",
      "title": "Final Details",
      "goal": "Finishing the enrollment",
      "estimatedDuration": "3 mins",
      "unlockCriteria": "l5",
      "nextLesson": "none",
      "sections": [
        {
          "type": "vocabulary",
          "title": "General Vocabulary",
          "description": "More words.",
          "exerciseIds": ["s66-v21", "s66-v22", "s66-v23", "s66-v24", "s66-v25"]
        },
        {
          "type": "phrase",
          "title": "General Phrases",
          "description": "More phrases.",
          "exerciseIds": ["s66-p11", "s66-p12"]
        }
      ]
    }
  ]
}

with open(f"{base_dir}/mini_lessons.json", "w", encoding="utf-8") as f:
    json.dump(mini_lessons, f, ensure_ascii=False, indent=2)

print("Files created.")
