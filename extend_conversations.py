import json

path = '/home/waseageru/parli-italiano/src/data/exports/workstudy/job_interview/conversations.json'

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extensions
ext = {
    "introducing_experience": [
        {
          "id": "m7",
          "role": "host",
          "text": "In passato ha dovuto gestire progetti in autonomia?",
          "english": "In the past did you have to manage projects independently?",
          "choices": [
            {"text": "Sì, ho seguito diversi progetti dall'inizio alla fine.", "isCorrect": True, "feedback": "Good description of independence."},
            {"text": "Preferisco mangiare la pizza da solo.", "isCorrect": False, "feedback": "Food related distractors."},
            {"text": "Ho perso il mio passaporto ieri.", "isCorrect": False, "feedback": "Travel related distractors."}
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Molto interessante. Che strumenti usa per organizzare il suo lavoro?",
          "english": "Very interesting. What tools do you use to organize your work?",
          "choices": [
            {"text": "Uso un'agenda digitale e dei software specifici.", "isCorrect": True, "feedback": "Professional tools."},
            {"text": "Uso il forno a microonde tutti i giorni.", "isCorrect": False, "feedback": "Kitchen tools."},
            {"text": "Non ho mai guidato un treno.", "isCorrect": False, "feedback": "Travel tools."}
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Capisco. È abituato a rispettare scadenze molto strette?",
          "english": "I see. Are you used to meeting very tight deadlines?",
          "choices": [
            {"text": "Assolutamente, so gestire bene il tempo a disposizione.", "isCorrect": True, "feedback": "Good time management."},
            {"text": "Il mio orologio si è rotto l'anno scorso.", "isCorrect": False, "feedback": "Literal clock."},
            {"text": "Mi piace fare lunghe passeggiate al mare.", "isCorrect": False, "feedback": "Beach activities."}
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Perfetto. C'è qualche altra esperienza che vuole aggiungere?",
          "english": "Perfect. Is there any other experience you want to add?",
          "choices": [
            {"text": "Penso di aver coperto i punti principali, grazie.", "isCorrect": True, "feedback": "Polite completion."},
            {"text": "Voglio comprare un biglietto per il teatro.", "isCorrect": False, "feedback": "Theater."} ,
            {"text": "Vado spesso al parco giochi la domenica.", "isCorrect": False, "feedback": "Playground."}
          ]
        }
    ],
    "discussing_skills": [
        {
          "id": "m7",
          "role": "host",
          "text": "Quale considera la sua più grande sfida professionale finora?",
          "english": "What do you consider your biggest professional challenge so far?",
          "choices": [
            {"text": "Sicuramente imparare a usare il nuovo sistema informatico.", "isCorrect": True, "feedback": "IT challenges."},
            {"text": "Scalare una montagna molto alta in estate.", "isCorrect": False, "feedback": "Physical challenge."},
            {"text": "Mangiare un piatto di pasta piccante.", "isCorrect": False, "feedback": "Food challenge."}
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "E come ha superato questa sfida?",
          "english": "And how did you overcome this challenge?",
          "choices": [
            {"text": "Ho studiato molto e ho chiesto aiuto ai colleghi.", "isCorrect": True, "feedback": "Good problem solving."},
            {"text": "Ho comprato un ombrello nuovo in centro.", "isCorrect": False, "feedback": "Shopping."},
            {"text": "Ho nuotato nel fiume per due ore.", "isCorrect": False, "feedback": "Swimming."}
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "È un ottimo approccio. Come si aggiorna sulle novità del settore?",
          "english": "That's a great approach. How do you stay updated on industry news?",
          "choices": [
            {"text": "Leggo articoli specializzati e partecipo ai corsi.", "isCorrect": True, "feedback": "Professional updates."},
            {"text": "Guardo sempre i cartoni animati in televisione.", "isCorrect": False, "feedback": "Cartoons."},
            {"text": "Non mi piace leggere il menu del ristorante.", "isCorrect": False, "feedback": "Menu reading."}
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Bene. Ritiene di avere buone doti di leadership?",
          "english": "Good. Do you believe you have good leadership skills?",
          "choices": [
            {"text": "Sì, ho guidato un piccolo team in passato.", "isCorrect": True, "feedback": "Leadership experience."},
            {"text": "Ho una macchina rossa molto veloce.", "isCorrect": False, "feedback": "Driving a car."},
            {"text": "Faccio una passeggiata al parco ogni sera.", "isCorrect": False, "feedback": "Park walk."}
          ]
        }
    ],
    "why_this_company": [
        {
          "id": "m7",
          "role": "host",
          "text": "Se dovesse descrivere la nostra azienda in una parola, quale sceglierebbe?",
          "english": "If you had to describe our company in one word, which would you choose?",
          "choices": [
            {"text": "Direi innovativa, per i vostri progetti recenti.", "isCorrect": True, "feedback": "Good answer."},
            {"text": "Direi rumorosa, come una strada trafficata.", "isCorrect": False, "feedback": "Negative word."},
            {"text": "Direi salata, come l'acqua del mare.", "isCorrect": False, "feedback": "Taste word."}
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Grazie. Conosce i nostri principali concorrenti sul mercato?",
          "english": "Thank you. Do you know our main competitors on the market?",
          "choices": [
            {"text": "Sì, ho studiato le altre aziende del vostro settore.", "isCorrect": True, "feedback": "Good knowledge."},
            {"text": "Sì, conosco tutti i ristoranti della città.", "isCorrect": False, "feedback": "Restaurant knowledge."},
            {"text": "No, non guardo mai le partite di calcio.", "isCorrect": False, "feedback": "Sports."}
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "E cosa ci distingue dai nostri concorrenti secondo lei?",
          "english": "And what distinguishes us from our competitors in your opinion?",
          "choices": [
            {"text": "La qualità del vostro servizio clienti è superiore.", "isCorrect": True, "feedback": "Good insight."},
            {"text": "I vostri gelati sono i più buoni in assoluto.", "isCorrect": False, "feedback": "Ice cream."},
            {"text": "I vostri biglietti del treno costano meno.", "isCorrect": False, "feedback": "Train tickets."}
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Sono d'accordo. È disposto a viaggiare per lavoro, se necessario?",
          "english": "I agree. Are you willing to travel for work, if necessary?",
          "choices": [
            {"text": "Certamente, sono disponibile a fare trasferte brevi.", "isCorrect": True, "feedback": "Willing to travel."},
            {"text": "Voglio solo andare in vacanza su un'isola.", "isCorrect": False, "feedback": "Vacation."},
            {"text": "Vado in bicicletta la domenica mattina.", "isCorrect": False, "feedback": "Bike riding."}
          ]
        }
    ],
    "asking_next_steps": [
        {
          "id": "m7",
          "role": "host",
          "text": "Ha bisogno di qualche giorno per pensarci prima di accettare?",
          "english": "Do you need a few days to think about it before accepting?",
          "choices": [
            {"text": "No, sono molto sicuro di volere questo lavoro.", "isCorrect": True, "feedback": "Confident answer."},
            {"text": "Sì, devo chiedere al mio cuoco personale.", "isCorrect": False, "feedback": "Personal chef."},
            {"text": "Voglio guardare un altro film al cinema.", "isCorrect": False, "feedback": "Cinema."}
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Ottimo. Sa che richiederemo delle referenze ai suoi precedenti datori di lavoro?",
          "english": "Great. Do you know we will require references from your previous employers?",
          "choices": [
            {"text": "Nessun problema, posso fornirvi i loro contatti.", "isCorrect": True, "feedback": "Good reference check."},
            {"text": "Devo comprare un nuovo tavolo da pranzo.", "isCorrect": False, "feedback": "Table."},
            {"text": "Le mie valigie sono già in aeroporto.", "isCorrect": False, "feedback": "Luggage."}
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Perfetto. Ci sarà anche una visita medica di controllo da superare.",
          "english": "Perfect. There will also be a medical check-up to pass.",
          "choices": [
            {"text": "Va bene, sono pronto anche per la visita medica.", "isCorrect": True, "feedback": "Medical check."},
            {"text": "Voglio ordinare una bottiglia di vino rosso.", "isCorrect": False, "feedback": "Wine."},
            {"text": "Il mare oggi è troppo mosso per nuotare.", "isCorrect": False, "feedback": "Sea."}
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Bene, è tutto chiaro. Riceverà una mail con i dettagli, ha un indirizzo valido?",
          "english": "Good, everything is clear. You will receive an email with the details, do you have a valid address?",
          "choices": [
            {"text": "Sì, vi ho lasciato il mio indirizzo email sul curriculum.", "isCorrect": True, "feedback": "Email provided."},
            {"text": "Abito vicino alla stazione centrale.", "isCorrect": False, "feedback": "Home address."},
            {"text": "Il mio ombrello è rimasto sul treno.", "isCorrect": False, "feedback": "Umbrella."}
          ]
        }
    ]
}

for conv in data['conversations']:
    cid = conv['id']
    if cid in ext:
        # Avoid duplicate extensions
        if len(conv['messages']) < 10:
            conv['messages'].extend(ext[cid])

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Conversations expanded.")
