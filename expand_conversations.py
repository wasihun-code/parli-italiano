import json
import os

path = 'src/data/exports/verbs/are_verbi_in_are/conversations.json'
with open(path, 'r') as f:
    data = json.load(f)

# Conversation 1: studiare_per_esame
new_messages_1 = [
    {
        "id": "s1_m6",
        "role": "host",
        "text": "Il professore arriva presto?",
        "english": "Does the professor arrive early?",
        "choices": [
            {
                "text": "Sì, lui arriva sempre alle otto in punto.",
                "isCorrect": True,
                "feedback": "Correct! 'Arrivare' is used correctly for the professor."
            },
            {
                "text": "Sì, io cucino la pasta in cucina ora.",
                "isCorrect": False,
                "feedback": "The question is about the professor's arrival, not your cooking!"
            },
            {
                "text": "Sì, guardo un film al cinema stasera.",
                "isCorrect": False,
                "feedback": "You are in the library, not at the cinema!"
            }
        ]
    },
    {
        "id": "s1_m7",
        "role": "host",
        "text": "Ottimo. Dove studi di solito?",
        "english": "Great. Where do you usually study?",
        "choices": [
            {
                "text": "Studio a casa o in biblioteca con i miei amici.",
                "isCorrect": True,
                "feedback": "Perfect! 'Studiare' is the right verb for this context."
            },
            {
                "text": "Compro un computer veloce per il mio ufficio.",
                "isCorrect": False,
                "feedback": "The host asked where you study, not what you buy."
            },
            {
                "text": "Mando una richiesta al capo per la riunione.",
                "isCorrect": False,
                "feedback": "Irrelevant to study locations."
            }
        ]
    },
    {
        "id": "s1_m8",
        "role": "host",
        "text": "Parli bene l'italiano! Studi da molto tempo?",
        "english": "You speak Italian well! Have you been studying for a long time?",
        "choices": [
            {
                "text": "Sì, parlo e studio ogni giorno per imparare.",
                "isCorrect": True,
                "feedback": "Excellent! You used 'parlare', 'studiare', and 'imparare' correctly."
            },
            {
                "text": "Sì, mangio il pane con il pomodoro a pranzo.",
                "isCorrect": False,
                "feedback": "Eating is not the same as studying!"
            },
            {
                "text": "Sì, ascolto la musica allegra alla radio ora.",
                "isCorrect": False,
                "feedback": "The host is complimenting your language skills, not your music taste."
            }
        ]
    },
    {
        "id": "s1_m9",
        "role": "host",
        "text": "Cosa mangi dopo lo studio? Hai fame?",
        "english": "What do you eat after studying? Are you hungry?",
        "choices": [
            {
                "text": "Mangio un panino veloce qui vicino.",
                "isCorrect": True,
                "feedback": "Correct use of 'mangiare'."
            },
            {
                "text": "Cerco l'email del professore sul computer.",
                "isCorrect": False,
                "feedback": "Searching for an email doesn't satisfy hunger!"
            },
            {
                "text": "Lavoro al progetto importante stasera.",
                "isCorrect": False,
                "feedback": "The question was about eating."
            }
        ]
    },
    {
        "id": "s1_m10",
        "role": "host",
        "text": "Perfetto. Allora ci vediamo dopo per studiare.",
        "english": "Perfect. Then I'll see you later to study.",
        "choices": [
            {
                "text": "D'accordo! A dopo e buon lavoro.",
                "isCorrect": True,
                "feedback": "A polite way to conclude the conversation."
            },
            {
                "text": "D'accordo! Compro i biglietti per il cinema.",
                "isCorrect": False,
                "feedback": "You are meeting to study, not to go to the cinema!"
            },
            {
                "text": "D'accordo! Aspetto il treno alla stazione.",
                "isCorrect": False,
                "feedback": "Why are you at the station? You just agreed to meet later!"
            }
        ]
    }
]

# Conversation 2: pranzo_tra_amici
new_messages_2 = [
    {
        "id": "s2_m6",
        "role": "host",
        "text": "Compriamo anche la frutta?",
        "english": "Shall we buy fruit too?",
        "choices": [
            {
                "text": "Sì, io compro le mele e le arance al mercato.",
                "isCorrect": True,
                "feedback": "Good use of 'comprare' for groceries."
            },
            {
                "text": "Sì, io studio la lezione di storia oggi.",
                "isCorrect": False,
                "feedback": "Don't study when you should be buying fruit!"
            },
            {
                "text": "Sì, io guardo il film al cinema stasera.",
                "isCorrect": False,
                "feedback": "Not helpful for lunch preparation."
            }
        ]
    },
    {
        "id": "s2_m7",
        "role": "host",
        "text": "Ottima idea. Lavori ancora o pranziamo subito?",
        "english": "Excellent idea. Are you still working or shall we have lunch right away?",
        "choices": [
            {
                "text": "Non lavoro più, sono pronto per mangiare.",
                "isCorrect": True,
                "feedback": "Clear and correct use of 'lavorare' and 'mangiare'."
            },
            {
                "text": "Non parlo più, sono pronto per dormire.",
                "isCorrect": False,
                "feedback": "It's lunchtime, not bedtime!"
            },
            {
                "text": "Non cerco più, sono pronto per arrivare.",
                "isCorrect": False,
                "feedback": "Doesn't make sense in this context."
            }
        ]
    },
    {
        "id": "s2_m8",
        "role": "host",
        "text": "Mandi un messaggio a Marco? Magari pranza con noi.",
        "english": "Are you sending a message to Marco? Maybe he'll have lunch with us?",
        "choices": [
            {
                "text": "Sì, mando subito un messaggio. Lui ama la tua pasta.",
                "isCorrect": True,
                "feedback": "Great use of 'mandare' and 'amare'."
            },
            {
                "text": "Sì, ascolto subito la musica. Lui ama il rock.",
                "isCorrect": False,
                "feedback": "The friend asked to send a message, not listen to music."
            },
            {
                "text": "Sì, guardo subito i documenti. Lui ama l'ufficio.",
                "isCorrect": False,
                "feedback": "Keep work out of the lunch plan!"
            }
        ]
    },
    {
        "id": "s2_m9",
        "role": "host",
        "text": "Perfetto. Cosa raccontiamo a Marco stasera?",
        "english": "Perfect. What are we telling Marco tonight?",
        "choices": [
            {
                "text": "Raccontiamo del nostro nuovo progetto di lavoro.",
                "isCorrect": True,
                "feedback": "Good use of 'raccontare' to share news."
            },
            {
                "text": "Cuciniamo del nostro nuovo computer di lavoro.",
                "isCorrect": False,
                "feedback": "You can't cook a computer!"
            },
            {
                "text": "Studiamo del nostro nuovo pranzo di lavoro.",
                "isCorrect": False,
                "feedback": "The verb 'studiare' doesn't fit here."
            }
        ]
    },
    {
        "id": "s2_m10",
        "role": "host",
        "text": "Ottimo. Allora aspetto la sua risposta.",
        "english": "Great. Then I'll wait for his answer.",
        "choices": [
            {
                "text": "Sì, aspettiamo insieme. Il pranzo è quasi pronto!",
                "isCorrect": True,
                "feedback": "Correct use of 'aspettare'."
            },
            {
                "text": "Sì, arriviamo insieme. Il pranzo è già finito!",
                "isCorrect": False,
                "feedback": "The lunch hasn't even started yet!"
            },
            {
                "text": "Sì, impariamo insieme. Il pranzo è molto difficile!",
                "isCorrect": False,
                "feedback": "Lunch isn't a school subject!"
            }
        ]
    }
]

# Conversation 3: lavoro_in_ufficio
new_messages_3 = [
    {
        "id": "s3_m6",
        "role": "host",
        "text": "Mandi i documenti alla segretaria?",
        "english": "Are you sending the documents to the secretary?",
        "choices": [
            {
                "text": "Sì, mando tutto ora. Lei aspetta la mia email.",
                "isCorrect": True,
                "feedback": "Professional use of 'mandare' and 'aspettare'."
            },
            {
                "text": "Sì, mangio tutto ora. Lei aspetta la mia pasta.",
                "isCorrect": False,
                "feedback": "Don't eat the documents!"
            },
            {
                "text": "Sì, guardo tutto ora. Lei aspetta la mia colonna.",
                "isCorrect": False,
                "feedback": "Doesn't make sense in an office context."
            }
        ]
    },
    {
        "id": "s3_m7",
        "role": "host",
        "text": "Ottimo. Dove lavori domani pomeriggio?",
        "english": "Great. Where are you working tomorrow afternoon?",
        "choices": [
            {
                "text": "Lavoro qui in ufficio o magari a casa.",
                "isCorrect": True,
                "feedback": "A clear answer using 'lavorare'."
            },
            {
                "text": "Cucino qui in ufficio o magari a casa.",
                "isCorrect": False,
                "feedback": "Offices are for working, not cooking!"
            },
            {
                "text": "Ascolto qui in ufficio o magari a casa.",
                "isCorrect": False,
                "feedback": "Vague answer. 'Lavoro' is better."
            }
        ]
    },
    {
        "id": "s3_m8",
        "role": "host",
        "text": "Impari a usare il nuovo software oggi?",
        "english": "Are you learning to use the new software today?",
        "choices": [
            {
                "text": "Sì, imparo con l'aiuto del mio collega.",
                "isCorrect": True,
                "feedback": "Good use of 'imparare'."
            },
            {
                "text": "Sì, compro con l'aiuto del mio professore.",
                "isCorrect": False,
                "feedback": "The question was about learning software."
            },
            {
                "text": "Sì, gioco con l'aiuto del mio attore.",
                "isCorrect": False,
                "feedback": "Inappropriate for the workplace."
            }
        ]
    },
    {
        "id": "s3_m9",
        "role": "host",
        "text": "Cosa ordiniamo per il pranzo in ufficio?",
        "english": "What are we ordering for lunch in the office?",
        "choices": [
            {
                "text": "Ordiniamo una pizza o un'insalata veloce.",
                "isCorrect": True,
                "feedback": "Correct use of 'ordinare' (wait, 'ordinare' is not in vocab? Let's check... No, let's use 'comprare')."
            },
            {
                "text": "Compriamo una pizza o un'insalata veloce.",
                "isCorrect": True,
                "feedback": "Better, 'comprare' is in the vocab."
            },
            {
                "text": "Studiamo una pizza o un'insalata veloce.",
                "isCorrect": False,
                "feedback": "You can't study a pizza!"
            },
            {
                "text": "Guardiamo una pizza o un'insalata veloce.",
                "isCorrect": False,
                "feedback": "You should eat it, not just look at it!"
            }
        ]
    },
    {
        "id": "s3_m10",
        "role": "host",
        "text": "Perfetto. Allora cerco il menu del ristorante.",
        "english": "Perfect. Then I'll look for the restaurant menu.",
        "choices": [
            {
                "text": "D'accordo, grazie mille per l'aiuto!",
                "isCorrect": True,
                "feedback": "A polite conclusion."
            },
            {
                "text": "D'accordo, grazie mille per il film!",
                "isCorrect": False,
                "feedback": "You are at work, not at the cinema!"
            },
            {
                "text": "D'accordo, grazie mille per il progetto!",
                "isCorrect": False,
                "feedback": "The colleague is helping with lunch, not the project right now."
            }
        ]
    }
]

# Note: I'll fix s3_m9 in the script below.

# Conversation 4: serata_al_cinema
new_messages_4 = [
    {
        "id": "s4_m6",
        "role": "host",
        "text": "A che ora arrivi davanti al cinema?",
        "english": "What time do you arrive in front of the cinema?",
        "choices": [
            {
                "text": "Arrivo alle otto meno un quarto, va bene?",
                "isCorrect": True,
                "feedback": "Correct use of 'arrivare'."
            },
            {
                "text": "Lavoro alle otto meno un quarto, va bene?",
                "isCorrect": False,
                "feedback": "Don't work when you're supposed to be at the cinema!"
            },
            {
                "text": "Studio alle otto meno un quarto, va bene?",
                "isCorrect": False,
                "feedback": "Same problem: stay focused on the movie!"
            }
        ]
    },
    {
        "id": "s4_m7",
        "role": "host",
        "text": "Sì, perfetto. Guardiamo il film in italiano?",
        "english": "Yes, perfect. Shall we watch the movie in Italian?",
        "choices": [
            {
                "text": "Sì, guardo volentieri i film in lingua originale.",
                "isCorrect": True,
                "feedback": "Great use of 'guardare' and 'lingua'."
            },
            {
                "text": "Sì, cucino volentieri i film in lingua originale.",
                "isCorrect": False,
                "feedback": "You cannot cook a film!"
            },
            {
                "text": "Sì, mando volentieri i film in lingua originale.",
                "isCorrect": False,
                "feedback": "The verb 'mandare' doesn't fit here."
            }
        ]
    },
    {
        "id": "s4_m8",
        "role": "host",
        "text": "Ami molto il cinema, vero?",
        "english": "You love the cinema a lot, right?",
        "choices": [
            {
                "text": "Sì, amo le storie interessanti e gli attori bravi.",
                "isCorrect": True,
                "feedback": "Excellent use of 'amare', 'storie', and 'attori'."
            },
            {
                "text": "Sì, mangio le storie interessanti e gli attori bravi.",
                "isCorrect": False,
                "feedback": "You are not a cannibal!"
            },
            {
                "text": "Sì, cerco le storie interessanti e gli attori bravi.",
                "isCorrect": False,
                "feedback": "You already found them in the cinema!"
            }
        ]
    },
    {
        "id": "s4_m9",
        "role": "host",
        "text": "Dopo il film, parliamo un po' del finale?",
        "english": "After the movie, shall we talk a bit about the ending?",
        "choices": [
            {
                "text": "Sì, parliamo davanti a un buon bicchiere di vino.",
                "isCorrect": True,
                "feedback": "Correct use of 'parlare' and 'vino'."
            },
            {
                "text": "Sì, studiamo davanti a un buon bicchiere di vino.",
                "isCorrect": False,
                "feedback": "Don't study after the movie, just relax!"
            },
            {
                "text": "Sì, lavoriamo davanti a un buon bicchiere di vino.",
                "isCorrect": False,
                "feedback": "No work talk after the cinema!"
            }
        ]
    },
    {
        "id": "s4_m10",
        "role": "host",
        "text": "Ottima idea! Allora ci vediamo tra poco.",
        "english": "Excellent idea! Then I'll see you shortly.",
        "choices": [
            {
                "text": "Sì, a tra poco! Non vedo l'ora.",
                "isCorrect": True,
                "feedback": "A natural way to conclude."
            },
            {
                "text": "Sì, a tra poco! Non parlo l'ora.",
                "isCorrect": False,
                "feedback": "'Non parlo l'ora' is incorrect; 'non vedo l'ora' is the idiom."
            },
            {
                "text": "Sì, a tra poco! Non mangio l'ora.",
                "isCorrect": False,
                "feedback": "You can't eat time!"
            }
        ]
    }
]

# Adjusting s3_m9
s3_m9_fixed = {
    "id": "s3_m9",
    "role": "host",
    "text": "Cosa compriamo per il pranzo in ufficio?",
    "english": "What are we buying for lunch in the office?",
    "choices": [
        {
            "text": "Compriamo una pizza o un'insalata veloce.",
            "isCorrect": True,
            "feedback": "Correct use of 'comprare'."
        },
        {
            "text": "Studiamo una pizza o un'insalata veloce.",
            "isCorrect": False,
            "feedback": "You can't study a pizza!"
        },
        {
            "text": "Guardiamo una pizza o un'insalata veloce.",
            "isCorrect": False,
            "feedback": "You should eat it, not just look at it!"
        }
    ]
}

data['conversations'][0]['messages'].extend(new_messages_1)
data['conversations'][1]['messages'].extend(new_messages_2)
data['conversations'][2]['messages'].extend([s3_m9_fixed if m['id'] == 's3_m9' else m for m in new_messages_3 if m['id'] != 's3_m9'])
# Wait, my logic for s3_m9 is a bit messy. Let's redo it properly.

# Proper way to add:
data['conversations'][0]['messages'] = data['conversations'][0]['messages'][:5] + new_messages_1
data['conversations'][1]['messages'] = data['conversations'][1]['messages'][:5] + new_messages_2
data['conversations'][2]['messages'] = data['conversations'][2]['messages'][:5] + [
    {
        "id": "s3_m6",
        "role": "host",
        "text": "Mandi i documenti alla segretaria?",
        "english": "Are you sending the documents to the secretary?",
        "choices": [
            {
                "text": "Sì, mando tutto ora. Lei aspetta la mia email.",
                "isCorrect": True,
                "feedback": "Professional use of 'mandare' and 'aspettare'."
            },
            {
                "text": "Sì, mangio tutto ora. Lei aspetta la mia pasta.",
                "isCorrect": False,
                "feedback": "Don't eat the documents!"
            },
            {
                "text": "Sì, guardo tutto ora. Lei aspetta la mia colonna.",
                "isCorrect": False,
                "feedback": "Doesn't make sense in an office context."
            }
        ]
    },
    {
        "id": "s3_m7",
        "role": "host",
        "text": "Ottimo. Dove lavori domani pomeriggio?",
        "english": "Great. Where are you working tomorrow afternoon?",
        "choices": [
            {
                "text": "Lavoro qui in ufficio o magari a casa.",
                "isCorrect": True,
                "feedback": "A clear answer using 'lavorare'."
            },
            {
                "text": "Cucino qui in ufficio o magari a casa.",
                "isCorrect": False,
                "feedback": "Offices are for working, not cooking!"
            },
            {
                "text": "Ascolto qui in ufficio o magari a casa.",
                "isCorrect": False,
                "feedback": "Vague answer. 'Lavoro' is better."
            }
        ]
    },
    {
        "id": "s3_m8",
        "role": "host",
        "text": "Impari a usare il nuovo software oggi?",
        "english": "Are you learning to use the new software today?",
        "choices": [
            {
                "text": "Sì, imparo con l'aiuto del mio collega.",
                "isCorrect": True,
                "feedback": "Good use of 'imparare'."
            },
            {
                "text": "Sì, compro con l'aiuto del mio professore.",
                "isCorrect": False,
                "feedback": "The question was about learning software."
            },
            {
                "text": "Sì, gioco con l'aiuto del mio attore.",
                "isCorrect": False,
                "feedback": "Inappropriate for the workplace."
            }
        ]
    },
    {
        "id": "s3_m9",
        "role": "host",
        "text": "Cosa compriamo per il pranzo in ufficio?",
        "english": "What are we buying for lunch in the office?",
        "choices": [
            {
                "text": "Compriamo una pizza o un'insalata veloce.",
                "isCorrect": True,
                "feedback": "Correct use of 'comprare'."
            },
            {
                "text": "Studiamo una pizza o un'insalata veloce.",
                "isCorrect": False,
                "feedback": "You can't study a pizza!"
            },
            {
                "text": "Guardiamo una pizza o un'insalata veloce.",
                "isCorrect": False,
                "feedback": "You should eat it, not just look at it!"
            }
        ]
    },
    {
        "id": "s3_m10",
        "role": "host",
        "text": "Perfetto. Allora cerco il menu del ristorante.",
        "english": "Perfect. Then I'll look for the restaurant menu.",
        "choices": [
            {
                "text": "D'accordo, grazie mille per l'aiuto!",
                "isCorrect": True,
                "feedback": "A polite conclusion."
            },
            {
                "text": "D'accordo, grazie mille per il film!",
                "isCorrect": False,
                "feedback": "You are at work, not at the cinema!"
            },
            {
                "text": "D'accordo, grazie mille per il progetto!",
                "isCorrect": False,
                "feedback": "The colleague is helping with lunch, not the project right now."
            }
        ]
    }
]
data['conversations'][3]['messages'] = data['conversations'][3]['messages'][:5] + new_messages_4

with open(path, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Conversations expanded.")
