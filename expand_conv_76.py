import json

def create_choice(text, is_correct=False, feedback=""):
    return {"text": text, "isCorrect": is_correct, "feedback": feedback}

data = {
  "scenarioId": 76,
  "conversations": [
    {
      "id": "asking_where_someone_is",
      "title": "Asking Where Someone Is",
      "description": "Find out where your friend is and when they will arrive.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Ciao! Dove sei? Ti sto aspettando davanti al bar.",
          "english": "Hi! Where are you? I'm waiting for you in front of the bar.",
          "choices": [
            create_choice("Sono in strada, arrivo tra cinque minuti. Scusa!", True, "Good! You apologized and gave an estimated time."),
            create_choice("Il bar è molto bello e grande. Mi piace molto.", False, "Irrelevant. You need to say where you are!"),
            create_choice("Voglio un caffè caldo e un cornetto dolce ora.", False, "A bit selfish! Answer the question first.")
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Va bene, non ti preoccupare. Sei a piedi o in bici?",
          "english": "Alright, don't worry. Are you on foot or by bike?",
          "choices": [
            create_choice("Sono a piedi, sto camminando velocemente verso di te.", True, "Perfect. You answered clearly."),
            create_choice("La mia bici è rossa e molto vecchia, non funziona.", False, "Too much detail about the bike, just answer if you are on it."),
            create_choice("Le scarpe sono nuove e mi fanno male ai piedi.", False, "Complaining about shoes doesn't answer the question.")
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Ok. C'è molta gente al bar, meglio sedersi fuori?",
          "english": "Ok. It's crowded at the bar, better to sit outside?",
          "choices": [
            create_choice("Sì, certo. Fuori si sta bene, c'è il sole oggi.", True, "Great! You agreed and gave a reason."),
            create_choice("No, dentro è troppo freddo e non mi piace affatto.", False, "The host suggested outside because it's crowded, not about temperature."),
            create_choice("Il tavolo è sporco e non voglio sedermi lì ora.", False, "You haven't arrived yet, so you don't know if it's dirty!")
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Fuori si sta bene, c'è anche un po' di musica. La senti?",
          "english": "It's nice outside, there's even some music. Do you hear it?",
          "choices": [
            create_choice("Sì, la sento! È una bellissima canzone, mi piace.", True, "Perfect, you engaged with the observation."),
            create_choice("La musica è troppo forte e non posso parlare bene.", False, "A bit negative for a casual chat."),
            create_choice("Non mi piace ballare in pubblico davanti alla gente.", False, "Nobody asked you to dance!")
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Ottimo. Vuoi qualcosa da bere intanto che aspetti?",
          "english": "Great. Do you want something to drink while you wait?",
          "choices": [
            create_choice("Un bicchiere d'acqua naturale, per favore. Ho sete.", True, "Polite and direct."),
            create_choice("La bottiglia di vino costa troppo in questo bar.", False, "A bit negative. Just say what you want."),
            create_choice("Mi piace bere il latte freddo la mattina presto.", False, "Irrelevant preference.")
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Un bicchiere d'acqua naturale o frizzante?",
          "english": "A glass of still or sparkling water?",
          "choices": [
            create_choice("Naturale va benissimo, grazie mille.", True, "Clear choice."),
            create_choice("L'acqua del mare è troppo salata per i pesci.", False, "Completely irrelevant."),
            create_choice("Voglio una birra fredda e molto grande adesso.", False, "You just agreed to water!")
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "D'accordo. Prendo anche un piccolo dolce per noi?",
          "english": "Agreed. Should I also get a small sweet for us?",
          "choices": [
            create_choice("Sì, volentieri! Adoro i dolci di questo bar.", True, "Enthusiastic agreement."),
            create_choice("La torta è troppo dolce e mi fa male ai denti.", False, "A bit complainy."),
            create_choice("Non ho fame perché ho mangiato molto a pranzo.", False, "Try to be more social.")
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Perfetto. Hai visto che bel sole c'è oggi?",
          "english": "Perfect. Did you see how beautiful the sun is today?",
          "choices": [
            create_choice("Sì, è vero! È una giornata perfetta per uscire.", True, "Agrees with the host."),
            create_choice("Il sole brucia la pelle e non mi piace affatto.", False, "Too negative."),
            create_choice("La luna è molto grande e bianca stasera in cielo.", False, "It's daytime!")
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Sì, è una giornata bellissima. Sei quasi arrivato?",
          "english": "Yes, it's a beautiful day. Are you almost here?",
          "choices": [
            create_choice("Certamente! Sono quasi arrivato, vedo l'insegna ora.", True, "Perfect progress update."),
            create_choice("La strada è lunga e io sono molto stanco di correre.", False, "A bit dramatic."),
            create_choice("Il mio amico arriva domani con il treno delle otto.", False, "Wrong person, wrong day.")
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Ricevuto. Ti aspetto qui. Mandami un messaggio quando arrivi!",
          "english": "Got it. Waiting for you here. Send me a message when you arrive!",
          "choices": [
            create_choice("Va bene, a tra poco allora! Ciao ciao.", True, "Friendly closing."),
            create_choice("Non ho il tuo numero di telefono salvato qui.", False, "You are literally texting them!"),
            create_choice("La radio è accesa e non sento bene il messaggio.", False, "It's a text message!")
          ]
        }
      ]
    },
    {
      "id": "sending_a_quick_update",
      "title": "Sending a Quick Update",
      "description": "Tell your friend you are running late and why.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Ehi, dove sei finito? Il film inizia tra poco!",
          "english": "Hey, where did you end up? The movie starts soon!",
          "choices": [
            create_choice("Scusa, sono ancora in ufficio. C'è molto lavoro oggi.", True, "Honest and explains the delay."),
            create_choice("Il cinema è lontano e non trovo il mio portafoglio.", False, "A bit chaotic."),
            create_choice("Mi piace guardare i film d'azione con gli amici.", False, "Irrelevant.")
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Oh no! Quanto tempo ti serve ancora per finire?",
          "english": "Oh no! How much more time do you need to finish?",
          "choices": [
            create_choice("Almeno venti minuti. Mandami un messaggio se iniziate.", True, "Good estimation."),
            create_choice("Il tempo è denaro e io ne ho molto poco adesso.", False, "Too philosophical."),
            create_choice("Ho fame e voglio mangiare una pizza dopo il film.", False, "Irrelevant.")
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Va bene. Vuoi che ti compri il biglietto intanto?",
          "english": "Alright. Do you want me to buy your ticket in the meantime?",
          "choices": [
            create_choice("Sì, grazie mille! Ti mando i soldi con l'app ora.", True, "Helpful and proactive."),
            create_choice("Il biglietto costa dieci euro ed è molto caro qui.", False, "Just say yes or no!"),
            create_choice("Non mi piacciono i posti in prima fila, sono scomodi.", False, "Answer the offer first.")
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Ok, biglietto preso. Ti aspetto all'ingresso allora.",
          "english": "Ok, ticket bought. I'll wait for you at the entrance then.",
          "choices": [
            create_choice("Perfetto. Corro subito appena finisco di scrivere.", True, "Shows urgency."),
            create_choice("L'ingresso è chiuso e non vedo nessuno fuori ora.", False, "You're still at the office!"),
            create_choice("Il mio capo è molto simpatico e lavora con me qui.", False, "Irrelevant.")
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "C'è molta fila alla cassa, meno male che ho l'app.",
          "english": "There's a long line at the checkout, luckily I have the app.",
          "choices": [
            create_choice("Hai ragione, l'app è molto utile in questi casi.", True, "Agrees with the host."),
            create_choice("La cassa è fatta di legno e di metallo grigio.", False, "Weird observation."),
            create_choice("Non mi piace pagare con i soldi perché sono sporchi.", False, "Irrelevant.")
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Hai già mangiato qualcosa o hai fame?",
          "english": "Have you already eaten something or are you hungry?",
          "choices": [
            create_choice("Ho molta fame! Non ho mangiato nulla oggi.", True, "Answers the question."),
            create_choice("La mela è un frutto rosso e molto buono da mangiare.", False, "Generic fact."),
            create_choice("Mangio sempre alle otto di sera a casa mia.", False, "Irrelevant.")
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Allora prendo dei popcorn grandi per noi due.",
          "english": "Then I'll get large popcorn for the two of us.",
          "choices": [
            create_choice("Ottimo! Mi piacciono molto quelli salati.", True, "Good reaction."),
            create_choice("I popcorn sono bianchi e sembrano piccole nuvole.", False, "Too poetic."),
            create_choice("Non voglio sporcare il mio vestito nuovo oggi.", False, "A bit fussy.")
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Va bene. Ti tengo il posto vicino al corridoio?",
          "english": "Alright. Should I save the seat near the aisle for you?",
          "choices": [
            create_choice("Sì, grazie. Così arrivo senza disturbare nessuno.", True, "Practical reason."),
            create_choice("Il corridoio è lungo e molto buio in questo cinema.", False, "Irrelevant description."),
            create_choice("Preferisco sedermi sul pavimento perché è più comodo.", False, "No one does that!")
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Ottimo. Sbrigati, le luci si stanno spegnendo!",
          "english": "Great. Hurry up, the lights are going out!",
          "choices": [
            create_choice("Sto arrivando! Sono già fuori dal mio ufficio.", True, "Action-oriented."),
            create_choice("Le luci della città sono molto belle di notte.", False, "Irrelevant observation."),
            create_choice("Voglio comprare una lampada nuova per la mia camera.", False, "Wrong topic.")
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Fai con calma, non correre troppo. A tra poco!",
          "english": "Take your time, don't run too much. See you soon!",
          "choices": [
            create_choice("Grazie, sei molto gentile. Ci vediamo tra poco!", True, "Friendly closing."),
            create_choice("La mia macchina è molto lenta e vecchia.", False, "Irrelevant."),
            create_choice("Non mi piace correre perché sudo molto.", False, "Too much info.")
          ]
        }
      ]
    },
    {
      "id": "confirming_a_meeting_time",
      "title": "Confirming a Meeting Time",
      "description": "Agree on a time and place to meet a friend tomorrow.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Ciao! Sei libero domani per un caffè in centro?",
          "english": "Hi! Are you free tomorrow for a coffee downtown?",
          "choices": [
            create_choice("Sì, sono libero. A che ora ci vediamo domani?", True, "Accepts and asks for time."),
            create_choice("Il caffè in Italia è molto buono e molto forte.", False, "Generic fact."),
            create_choice("Domani piove e non voglio uscire di casa affatto.", False, "Negative.")
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Che ne dici delle tre del pomeriggio? Va bene?",
          "english": "How about three in the afternoon? Is that okay?",
          "choices": [
            create_choice("Le tre va benissimo per me. Dove ci incontriamo?", True, "Confirms time."),
            create_choice("Ho tre gatti a casa e sono molto carini e dolci.", False, "Misunderstanding."),
            create_choice("Il pomeriggio dormo sempre e non voglio uscire mai.", False, "Lazy.")
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Davanti alla fontana in piazza. La conosci?",
          "english": "In front of the fountain in the square. Do you know it?",
          "choices": [
            create_choice("Sì, la conosco bene. È un posto molto bello.", True, "Confirms knowledge."),
            create_choice("L'acqua della fontana è fredda e non si beve.", False, "Irrelevant fact."),
            create_choice("La piazza è grande e ci sono molte macchine ora.", False, "Irrelevant.")
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Perfetto. Se piove ci spostiamo nel bar vicino.",
          "english": "Perfect. If it rains we'll move to the nearby bar.",
          "choices": [
            create_choice("Ottima idea! Quel bar è molto carino e accogliente.", True, "Agrees with backup plan."),
            create_choice("L'ombrello è rotto e non posso usarlo se piove.", False, "Irrelevant."),
            create_choice("Il bar vicino vende solo bibite calde e dolci.", False, "Irrelevant.")
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Sai se quel bar è aperto anche di domenica?",
          "english": "Do you know if that bar is open on Sundays too?",
          "choices": [
            create_choice("Sì, credo di sì. Di solito è sempre aperto.", True, "Answers the question."),
            create_choice("La domenica è l'ultimo giorno della settimana.", False, "Generic fact."),
            create_choice("Voglio andare in chiesa la domenica mattina.", False, "Irrelevant.")
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Spero di sì, fanno dei cornetti spettacolari.",
          "english": "I hope so, they make spectacular croissants.",
          "choices": [
            create_choice("Davvero? Allora dobbiamo provarli assolutamente!", True, "Engaged response."),
            create_choice("Il cornetto è un corno piccolo e molto duro.", False, "Literal translation error."),
            create_choice("Non mi piace lo zucchero perché fa male alla salute.", False, "Too health-conscious.")
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Vuoi invitare anche Marco o preferisci solo noi?",
          "english": "Do you want to invite Marco too or do you prefer just us?",
          "choices": [
            create_choice("Preferisco solo noi due, così parliamo con calma.", True, "Clear preference."),
            create_choice("Marco è un nome molto comune in Italia oggi.", False, "Generic fact."),
            create_choice("Non conosco nessun Marco che vive in questa città.", False, "Maybe you do and forgot?")
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Va bene, allora siamo solo io e te.",
          "english": "Alright, then it's just you and me.",
          "choices": [
            create_choice("Perfetto, mi fa molto piacere vederti.", True, "Friendly statement."),
            create_choice("Tu sei alto e io sono basso in questa foto.", False, "Irrelevant comparison."),
            create_choice("Due più due fa quattro e non cinque.", False, "Math?")
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Ti mando un messaggio domani mattina per conferma.",
          "english": "I'll send you a message tomorrow morning to confirm.",
          "choices": [
            create_choice("D'accordo, aspetto il tuo messaggio allora.", True, "Accepts the plan."),
            create_choice("La mattina bevo sempre un bicchiere di latte.", False, "Irrelevant."),
            create_choice("Il mio telefono non riceve messaggi di mattina.", False, "Why not?")
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Certo! Ti mando un messaggio se cambio programma.",
          "english": "Sure! I'll send you a message if I change plans.",
          "choices": [
            create_choice("Va bene, a domani! Buona serata intanto.", True, "Friendly closing."),
            create_choice("Il cambio della macchina è rotto e non va.", False, "Misunderstanding 'cambio'."),
            create_choice("Non mi piace guardare i programmi in televisione.", False, "Misunderstanding 'programma'.")
          ]
        }
      ]
    },
    {
      "id": "sharing_a_funny_moment",
      "title": "Sharing a Funny Moment",
      "description": "React to a funny photo or message sent by your friend.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Guarda questa foto del mio cane! Sembra un umano.",
          "english": "Look at this photo of my dog! He looks like a human.",
          "choices": [
            create_choice("Ahaha! È bellissima, mi fa ridere molto!", True, "Natural reaction."),
            create_choice("Il cane mangia carne e corre nel parco.", False, "Boring."),
            create_choice("Non vedo nulla, la foto è tutta nera.", False, "Rude.")
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Vero? Ha anche gli occhiali da sole in testa!",
          "english": "Right? He even has sunglasses on his head!",
          "choices": [
            create_choice("Che buffo! Dove hai comprato quegli occhiali?", True, "Engaged."),
            create_choice("Il sole è forte oggi e servono gli occhiali.", False, "Serious."),
            create_choice("La testa del cane è piccola e tonda.", False, "Weird.")
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Li ho presi al mercato. Vuoi venire a trovarlo?",
          "english": "I got them at the market. Do you want to come visit him?",
          "choices": [
            create_choice("Volentieri! Posso venire sabato pomeriggio?", True, "Accepts."),
            create_choice("Il mercato è aperto solo la mattina presto.", False, "Doesn't answer."),
            create_choice("Non mi piacciono i cani che abbaiano forte.", False, "Negative.")
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Sabato va bene. Ti preparo una torta allora!",
          "english": "Saturday is fine. I'll bake you a cake then!",
          "choices": [
            create_choice("Ottimo, adoro i dolci! Grazie per l'invito.", True, "Polite."),
            create_choice("La torta di mele è meglio della torta al cioccolato.", False, "Picky."),
            create_choice("Cucinare è difficile e io non so fare nulla.", False, "Irrelevant.")
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Preferisci la torta al cioccolato o alla frutta?",
          "english": "Do you prefer chocolate or fruit cake?",
          "choices": [
            create_choice("Quella al cioccolato è la mia preferita!", True, "Clear choice."),
            create_choice("La frutta è piena di vitamine e fa bene.", False, "Generic fact."),
            create_choice("Il cioccolato è marrone e la frutta è colorata.", False, "Obvious.")
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Ottimo, adoro cucinare quando ho tempo.",
          "english": "Great, I love cooking when I have time.",
          "choices": [
            create_choice("Anche a me piace, ma non sono molto bravo.", True, "Relatable."),
            create_choice("L'orologio segna le dieci e mezza ora.", False, "Irrelevant."),
            create_choice("Il tempo vola quando ci si diverte molto.", False, "Proverb.")
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Ti mando anche il video dove il cane balla?",
          "english": "Should I also send you the video where the dog dances?",
          "choices": [
            create_choice("Sì, per favore! Deve essere divertente.", True, "Engaged."),
            create_choice("Il video è una sequenza di immagini veloci.", False, "Definition."),
            create_choice("Non mi piace ballare perché mi stanco subito.", False, "It's about the dog!")
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Ahaha, è davvero buffo, lo so!",
          "english": "Ahaha, he's really funny, I know!",
          "choices": [
            create_choice("Sì, i tuoi messaggi mi fanno sempre ridere.", True, "Compliment."),
            create_choice("Il riso è un cereale che cresce nell'acqua.", False, "Pun error (ridere/riso)."),
            create_choice("So tutto di te e della tua famiglia ora.", False, "Creepy.")
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Allora ci vediamo sabato verso le quattro?",
          "english": "So shall we meet Saturday around four?",
          "choices": [
            create_choice("Sì, perfetto. Ci vediamo sabato allora!", True, "Confirms."),
            create_choice("Quattro è un numero pari e non dispari.", False, "Math."),
            create_choice("Il sabato sera vado sempre a ballare in discoteca.", False, "Irrelevant.")
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Figurati! Ci aggiorniamo venerdì per l'orario.",
          "english": "Don't mention it! We'll catch up on Friday for the time.",
          "choices": [
            create_choice("D'accordo, a venerdì allora. Un abbraccio!", True, "Friendly closing."),
            create_choice("Venerdì è un giorno sfortunato per me.", False, "Negative."),
            create_choice("L'orario del treno è cambiato ieri sera.", False, "Irrelevant.")
          ]
        }
      ]
    }
  ]
}

with open("/home/waseageru/parli-italiano/src/data/exports/social/texting_a_friend/conversations.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
