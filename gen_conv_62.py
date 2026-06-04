import json

data = {
  "scenarioId": 62,
  "conversations": [
    {
      "id": "starting_the_meeting",
      "title": "Starting the Meeting",
      "description": "Greeting the team and introducing the agenda.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Buongiorno a tutti! Grazie per essere qui oggi.",
          "english": "Good morning everyone! Thank you for being here today.",
          "choices": [
            {
              "text": "Buongiorno! Siamo pronti per iniziare la riunione.",
              "isCorrect": True,
              "feedback": "Perfect response to start."
            },
            {
              "text": "Buonasera! Siamo andati per finire la colazione.",
              "isCorrect": False,
              "feedback": "Wrong time and context."
            },
            {
              "text": "Buonanotte! Siamo stanchi per dormire sul divano.",
              "isCorrect": False,
              "feedback": "Wrong context."
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Oggi abbiamo molte cose da fare. Avete letto l'ordine del giorno?",
          "english": "Today we have many things to do. Have you read the agenda?",
          "choices": [
            {
              "text": "Sì, ho letto tutto l'ordine del giorno stamattina.",
              "isCorrect": True,
              "feedback": "Good confirmation."
            },
            {
              "text": "No, ho rotto tutto il vetro della mia macchina.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Sì, ho visto tutto il concerto dalla mia finestra.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Bene. Il primo punto è il nostro nuovo progetto.",
          "english": "Good. The first point is our new project.",
          "choices": [
            {
              "text": "Sono molto felice di lavorare a questo progetto.",
              "isCorrect": True,
              "feedback": "Positive and relevant."
            },
            {
              "text": "Sono molto stanco di nuotare in questa piscina.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Sono molto triste di studiare per questo esame.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Dobbiamo collaborare bene come una squadra. Siete d'accordo?",
          "english": "We must collaborate well as a team. Do you agree?",
          "choices": [
            {
              "text": "Assolutamente, la squadra è molto importante per noi.",
              "isCorrect": True,
              "feedback": "Strong agreement."
            },
            {
              "text": "Assolutamente, la valigia è molto pesante per lui.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Assolutamente, la chitarra è molto difficile per me.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Abbiamo poco tempo per finire tutto. Qual è la scadenza?",
          "english": "We have little time to finish everything. What is the deadline?",
          "choices": [
            {
              "text": "La scadenza è il prossimo venerdì, abbiamo pochi giorni.",
              "isCorrect": True,
              "feedback": "Correctly answers the deadline."
            },
            {
              "text": "La partenza è il prossimo martedì, abbiamo poche borse.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "La camicia è nel primo cassetto, abbiamo molti vestiti.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Giusto. Dobbiamo rispettare questa scadenza senza fare ritardi.",
          "english": "Right. We must meet this deadline without making delays.",
          "choices": [
            {
              "text": "Sì, possiamo farcela se lavoriamo tutti i giorni.",
              "isCorrect": True,
              "feedback": "Positive attitude."
            },
            {
              "text": "No, possiamo dormirci se chiudiamo tutti i libri.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Sì, possiamo perderla se camminiamo tutti i mesi.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Chi vuole presentare le prime idee per il progetto?",
          "english": "Who wants to present the first ideas for the project?",
          "choices": [
            {
              "text": "Posso iniziare io, ho preparato una breve presentazione.",
              "isCorrect": True,
              "feedback": "Volunteers to present."
            },
            {
              "text": "Posso guidare io, ho comprato una nuova automobile.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Posso dormire io, ho preparato una grande coperta.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Grazie. Possiamo guardare la tua presentazione adesso?",
          "english": "Thank you. Can we look at your presentation now?",
          "choices": [
            {
              "text": "Certo, condivido subito lo schermo del mio computer.",
              "isCorrect": True,
              "feedback": "Appropriate action."
            },
            {
              "text": "Certo, lavo subito i piatti della mia cucina.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Certo, pulisco subito il pavimento del mio bagno.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Perfetto. Sembra davvero un'ottima idea per noi.",
          "english": "Perfect. It really seems like an excellent idea for us.",
          "choices": [
            {
              "text": "Sono contento che vi piaccia questa nuova idea.",
              "isCorrect": True,
              "feedback": "Polite response."
            },
            {
              "text": "Sono dispiaciuto che vi manchi questa vecchia borsa.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Sono sorpreso che vi serva questa piccola pianta.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Ci sono altre domande sull'ordine del giorno di oggi?",
          "english": "Are there other questions about today's agenda?",
          "choices": [
            {
              "text": "No, per me è tutto molto chiaro. Andiamo avanti.",
              "isCorrect": True,
              "feedback": "Good concluding statement."
            },
            {
              "text": "Sì, per me è tutto molto freddo. Andiamo fuori.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "No, per me è tutto molto scuro. Andiamo via.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        }
      ]
    },
    {
      "id": "project_status_update",
      "title": "Project Status Update",
      "description": "Discuss the progress of the current project.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Ciao a tutti. Iniziamo con l'aggiornamento sul progetto.",
          "english": "Hello everyone. Let's start with the update on the project.",
          "choices": [
            {
              "text": "Ottimo, sono pronto a parlare del nostro lavoro.",
              "isCorrect": True,
              "feedback": "Ready to participate."
            },
            {
              "text": "Pessimo, sono pronto a parlare del nostro treno.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Strano, sono pronto a parlare del nostro parco.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "A che punto siamo con il lavoro di questa settimana?",
          "english": "Where are we with this week's work?",
          "choices": [
            {
              "text": "Abbiamo quasi finito la prima parte del progetto.",
              "isCorrect": True,
              "feedback": "Gives a status update."
            },
            {
              "text": "Abbiamo quasi comprato la prima parte del viaggio.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Abbiamo quasi perso la prima parte del libro.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Molto bene. Ci sono problemi con la scadenza prevista?",
          "english": "Very good. Are there problems with the expected deadline?",
          "choices": [
            {
              "text": "Forse abbiamo bisogno di due giorni in più.",
              "isCorrect": True,
              "feedback": "Honest assessment."
            },
            {
              "text": "Forse abbiamo bisogno di due scarpe in più.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Forse abbiamo bisogno di due alberi in più.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Capisco. Forse dobbiamo lavorare un po' di più domani.",
          "english": "I understand. Maybe we have to work a bit more tomorrow.",
          "choices": [
            {
              "text": "Va bene, posso rimanere in ufficio fino a tardi.",
              "isCorrect": True,
              "feedback": "Willing to help."
            },
            {
              "text": "Va male, posso rimanere in macchina fino a domani.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Va bene, posso rimanere in cucina fino a cena.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Chi si occupa della presentazione per i nostri clienti?",
          "english": "Who is taking care of the presentation for our clients?",
          "choices": [
            {
              "text": "Me ne occupo io, ho già scritto alcune idee.",
              "isCorrect": True,
              "feedback": "Takes responsibility."
            },
            {
              "text": "Me ne vado io, ho già chiuso alcune porte.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Me ne lavo io, ho già aperto alcune finestre.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Perfetto. Hai bisogno di aiuto dalla nostra squadra?",
          "english": "Perfect. Do you need help from our team?",
          "choices": [
            {
              "text": "Sì, mi serve un po' di aiuto con i numeri.",
              "isCorrect": True,
              "feedback": "Asks for specific help."
            },
            {
              "text": "No, mi serve un po' di acqua con i limoni.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Sì, mi serve un po' di tempo con i bambini.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Va bene, posso aiutarti io giovedì mattina. Va bene?",
          "english": "Alright, I can help you Thursday morning. Is that okay?",
          "choices": [
            {
              "text": "Sì, giovedì mattina è perfetto per me. Grazie mille.",
              "isCorrect": True,
              "feedback": "Agrees to the time."
            },
            {
              "text": "Sì, giovedì sera è perfetto per te. Buona notte.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Sì, martedì mattina è perfetto per noi. Buon viaggio.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Abbiamo raggiunto il nostro obiettivo mensile, secondo voi?",
          "english": "Have we reached our monthly goal, in your opinion?",
          "choices": [
            {
              "text": "Credo di sì, abbiamo lavorato molto duramente questo mese.",
              "isCorrect": True,
              "feedback": "Positive confirmation."
            },
            {
              "text": "Credo di no, abbiamo dormito molto profondamente questo mese.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Credo di sì, abbiamo guidato molto velocemente questo mese.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Ottimo lavoro. Dobbiamo solo finire le ultime cose.",
          "english": "Great job. We just have to finish the last things.",
          "choices": [
            {
              "text": "Esatto, mancano solo due documenti da leggere e correggere.",
              "isCorrect": True,
              "feedback": "Confirms the remaining tasks."
            },
            {
              "text": "Esatto, mancano solo due bicchieri da bere e lavare.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Esatto, mancano solo due vestiti da piegare e stirare.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Siete contenti dei risultati di questo lungo progetto?",
          "english": "Are you happy with the results of this long project?",
          "choices": [
            {
              "text": "Sì, penso che abbiamo fatto un ottimo lavoro insieme.",
              "isCorrect": True,
              "feedback": "Good team spirit."
            },
            {
              "text": "No, penso che abbiamo comprato un brutto vestito rosso.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Sì, penso che abbiamo mangiato un dolce molto buono.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        }
      ]
    },
    {
      "id": "brainstorming_ideas",
      "title": "Brainstorming Ideas",
      "description": "Sharing and discussing new ideas.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Ora dobbiamo trovare nuove idee per il nostro progetto.",
          "english": "Now we need to find new ideas for our project.",
          "choices": [
            {
              "text": "Sono d'accordo, abbiamo bisogno di qualcosa di nuovo.",
              "isCorrect": True,
              "feedback": "Agrees with the premise."
            },
            {
              "text": "Sono d'accordo, abbiamo bisogno di qualcosa da bere.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Sono d'accordo, abbiamo bisogno di qualcosa di caldo.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Qualcuno ha un'idea interessante da condividere con la squadra?",
          "english": "Does anyone have an interesting idea to share with the team?",
          "choices": [
            {
              "text": "Io ho un'idea: possiamo cambiare i colori della presentazione.",
              "isCorrect": True,
              "feedback": "Suggests an idea."
            },
            {
              "text": "Io ho un libro: possiamo leggere i capitoli della storia.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Io ho un tavolo: possiamo pulire le sedie della sala.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Mi piace questa idea. Come possiamo realizzarla in pratica?",
          "english": "I like this idea. How can we make it happen in practice?",
          "choices": [
            {
              "text": "Possiamo usare un programma speciale per il computer.",
              "isCorrect": True,
              "feedback": "Offers a practical solution."
            },
            {
              "text": "Possiamo usare un cappotto speciale per il freddo.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Possiamo usare un cuscino speciale per il letto.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "È una buona strategia. Chi vuole lavorare su questo?",
          "english": "It's a good strategy. Who wants to work on this?",
          "choices": [
            {
              "text": "Posso farlo io, conosco molto bene quel programma.",
              "isCorrect": True,
              "feedback": "Volunteers and justifies."
            },
            {
              "text": "Posso farlo io, conosco molto bene quel negozio.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Posso averlo io, conosco molto bene quel dottore.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Abbiamo bisogno di altre idee per attirare i clienti.",
          "english": "We need other ideas to attract clients.",
          "choices": [
            {
              "text": "Cosa ne pensate di creare un breve video online?",
              "isCorrect": True,
              "feedback": "Suggests a modern idea."
            },
            {
              "text": "Cosa ne pensate di comprare un nuovo frigorifero bianco?",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Cosa ne pensate di lavare un grande tappeto blu?",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Forse possiamo usare più immagini e meno parole lunghe.",
          "english": "Maybe we can use more images and fewer long words.",
          "choices": [
            {
              "text": "Sì, un'immagine è spesso più chiara di molte parole.",
              "isCorrect": True,
              "feedback": "Agrees with the statement."
            },
            {
              "text": "Sì, una bicicletta è spesso più veloce di molte macchine.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Sì, una scarpa è spesso più stretta di molti calzini.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Siete tutti d'accordo con questa nuova idea visiva?",
          "english": "Do you all agree with this new visual idea?",
          "choices": [
            {
              "text": "Sì, siamo tutti d'accordo con questo approccio moderno.",
              "isCorrect": True,
              "feedback": "Confirms consensus."
            },
            {
              "text": "No, siamo tutti arrabbiati con questo orologio rotto.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Sì, siamo tutti d'accordo con questo divano comodo.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Bene, abbiamo un buon accordo nella nostra squadra oggi.",
          "english": "Good, we have a good agreement in our team today.",
          "choices": [
            {
              "text": "Questo è il modo migliore per lavorare bene insieme.",
              "isCorrect": True,
              "feedback": "Positive reinforcement."
            },
            {
              "text": "Questo è il tavolo migliore per mangiare bene insieme.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Questo è il libro migliore per dormire bene insieme.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Dobbiamo scrivere tutte queste idee sul documento ufficiale.",
          "english": "We must write all these ideas on the official document.",
          "choices": [
            {
              "text": "Prendo io gli appunti e li mando a tutti.",
              "isCorrect": True,
              "feedback": "Takes on the task."
            },
            {
              "text": "Prendo io i biscotti e li mangio con tutti.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Prendo io i vestiti e li lavo per tutti.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Grazie a tutti per la vostra grande creatività oggi.",
          "english": "Thank you all for your great creativity today.",
          "choices": [
            {
              "text": "Di nulla, è stato un piacere collaborare in squadra.",
              "isCorrect": True,
              "feedback": "Polite sign-off."
            },
            {
              "text": "Di nulla, è stato un dolore camminare nel bosco.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Di nulla, è stato un favore pulire la macchina.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        }
      ]
    },
    {
      "id": "setting_next_steps",
      "title": "Setting Next Steps",
      "description": "Agreeing on what needs to be done next.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Passiamo all'ultimo punto: i prossimi passi da fare.",
          "english": "Let's move to the last point: the next steps to take.",
          "choices": [
            {
              "text": "Certo, vediamo cosa dobbiamo fare nei prossimi giorni.",
              "isCorrect": True,
              "feedback": "Ready to plan."
            },
            {
              "text": "Certo, vediamo cosa dobbiamo bere nei prossimi minuti.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Certo, vediamo cosa dobbiamo lavare nei prossimi mesi.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Cosa dobbiamo fare esattamente prima di domani sera?",
          "english": "What exactly do we need to do before tomorrow evening?",
          "choices": [
            {
              "text": "Dobbiamo finire le prime cinque pagine della presentazione.",
              "isCorrect": True,
              "feedback": "Specifies the task."
            },
            {
              "text": "Dobbiamo finire le prime cinque fette della torta.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Dobbiamo finire le prime cinque miglia della corsa.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Esatto. Chi prepara il documento per il nostro cliente?",
          "english": "Exactly. Who is preparing the document for our client?",
          "choices": [
            {
              "text": "Lo preparo io stasera, sarà pronto per domani.",
              "isCorrect": True,
              "feedback": "Takes the task."
            },
            {
              "text": "Lo lavo io stasera, sarà pulito per domani.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Lo bevo io stasera, sarà vuoto per domani.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Perfetto. Qual è il nostro obiettivo per la prossima settimana?",
          "english": "Perfect. What is our goal for next week?",
          "choices": [
            {
              "text": "Il nostro obiettivo è completare l'intero progetto insieme.",
              "isCorrect": True,
              "feedback": "States the goal."
            },
            {
              "text": "Il nostro divano è completare l'intero viaggio insieme.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Il nostro orologio è completare l'intero bagno insieme.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Dobbiamo rispettare questa nuova scadenza, è molto importante.",
          "english": "We must respect this new deadline, it is very important.",
          "choices": [
            {
              "text": "Sì, non possiamo permetterci di fare nessun ritardo.",
              "isCorrect": True,
              "feedback": "Understands the importance."
            },
            {
              "text": "Sì, non possiamo permetterci di fare nessun viaggio.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Sì, non possiamo permetterci di fare nessun bagno.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Lavoriamo insieme per non avere problemi di tempo.",
          "english": "Let's work together to not have time problems.",
          "choices": [
            {
              "text": "Se collaboriamo, finiremo tutto nei tempi previsti.",
              "isCorrect": True,
              "feedback": "Shows teamwork."
            },
            {
              "text": "Se dormiamo, finiremo tutto nei tempi previsti.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Se corriamo, finiremo tutto nei tempi previsti.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Abbiamo bisogno di un'altra riunione per venerdì pomeriggio?",
          "english": "Do we need another meeting for Friday afternoon?",
          "choices": [
            {
              "text": "Sì, penso che sia utile per controllare il lavoro.",
              "isCorrect": True,
              "feedback": "Agrees to another meeting."
            },
            {
              "text": "Sì, penso che sia utile per controllare il motore.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Sì, penso che sia utile per controllare il giardino.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Va bene, organizziamo una riunione breve venerdì mattina.",
          "english": "Alright, let's organize a short meeting Friday morning.",
          "choices": [
            {
              "text": "Manderò io l'invito a tutti i membri della squadra.",
              "isCorrect": True,
              "feedback": "Takes initiative."
            },
            {
              "text": "Manderò io il pacco a tutti i membri della famiglia.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Manderò io il gatto a tutti i membri della classe.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "C'è qualcos'altro da dire prima di chiudere la riunione?",
          "english": "Is there anything else to say before closing the meeting?",
          "choices": [
            {
              "text": "Da parte mia, no. Grazie per l'incontro di oggi.",
              "isCorrect": True,
              "feedback": "No further comments."
            },
            {
              "text": "Da parte mia, sì. Grazie per il pane di ieri.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Da parte mia, no. Grazie per il gatto di oggi.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Allora abbiamo finito. Grazie per il vostro tempo prezioso.",
          "english": "Then we are done. Thank you for your valuable time.",
          "choices": [
            {
              "text": "Grazie a te. Buona giornata e buon lavoro a tutti.",
              "isCorrect": True,
              "feedback": "Polite goodbye."
            },
            {
              "text": "Grazie a te. Buona passeggiata e buon sonno a tutti.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            },
            {
              "text": "Grazie a te. Buona cena e buon bagno a tutti.",
              "isCorrect": False,
              "feedback": "Irrelevant."
            }
          ]
        }
      ]
    }
  ]
}

with open("src/data/exports/workstudy/team_meeting/conversations.json", "w") as f:
    json.dump(data, f, indent=2)
