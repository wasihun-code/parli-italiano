import json

# Conversation 1 already done in gen_conv_78_part1.py, let's include it here too.
conv1 = {
  "id": "new_outfit",
  "title": "Complimenting a New Outfit",
  "description": "Give a compliment about a friend's new clothes.",
  "messages": [
    {
      "id": "m1", "role": "host", "text": "Ciao! Come stai oggi? Sei pronto per uscire?", "english": "Hi! How are you today? Are you ready to go out?",
      "choices": [
        {"text": "Ciao! Sto bene, grazie. Che bella giacca che indossi oggi!", "isCorrect": True, "feedback": "Great start by complimenting the jacket."},
        {"text": "Ciao! Sto bene, grazie. Che bella finestra che abbiamo oggi!", "isCorrect": False, "feedback": "You are talking about a window, not an outfit."},
        {"text": "Ciao! Sto bene, grazie. Che bella porta che chiudiamo oggi!", "isCorrect": False, "feedback": "Focus on the person's appearance, not the door."}
      ]
    },
    {
      "id": "m2", "role": "host", "text": "Grazie mille! L'ho comprata proprio ieri in centro.", "english": "Thank you very much! I bought it just yesterday downtown.",
      "choices": [
        {"text": "Hai fatto un ottimo acquisto. Il colore ti sta benissimo.", "isCorrect": True, "feedback": "Nice specific compliment about the color."},
        {"text": "Hai fatto un ottimo sbaglio. Il lavoro ti sta malissimo.", "isCorrect": False, "feedback": "You should compliment, not criticize."},
        {"text": "Hai fatto un ottimo pasto. Il tavolo ti sta benissimo.", "isCorrect": False, "feedback": "You are talking about a jacket, not a meal."}
      ]
    },
    {
      "id": "m3", "role": "host", "text": "Davvero? Ero un po' indeciso tra questo blu e il nero.", "english": "Really? I was a bit undecided between this blue and black.",
      "choices": [
        {"text": "Il blu è perfetto. È molto elegante e davvero originale.", "isCorrect": True, "feedback": "Confirming their choice with positive adjectives."},
        {"text": "Il muro è perfetto. È molto elegante e davvero originale.", "isCorrect": False, "feedback": "You are talking about the jacket color, not a wall."},
        {"text": "Il tetto è perfetto. È molto divertente e davvero stupendo.", "isCorrect": False, "feedback": "You are talking about a color, not a roof."}
      ]
    },
    {
      "id": "m4", "role": "host", "text": "Sei molto gentile. Anche le tue scarpe nuove sono belle.", "english": "You are very kind. Your new shoes are beautiful too.",
      "choices": [
        {"text": "Grazie! Anche a me piacciono molto. Sono comodissime.", "isCorrect": True, "feedback": "Accepting the compliment and adding a detail."},
        {"text": "Grazie! Anche a me mancano molto. Sono velocissime.", "isCorrect": False, "feedback": "You already have the shoes, they are not missing."},
        {"text": "Grazie! Anche a me scrivono molto. Sono simpatiche.", "isCorrect": False, "feedback": "Shoes do not write or have a personality."}
      ]
    },
    {
      "id": "m5", "role": "host", "text": "Sembrano perfette per camminare a lungo. Dove le hai prese?", "english": "They look perfect for walking a long time. Where did you get them?",
      "choices": [
        {"text": "Le ho trovate in un piccolo negozio qui vicino a casa.", "isCorrect": True, "feedback": "Answering the question naturally."},
        {"text": "Le ho trovate in un grande piatto qui vicino a casa.", "isCorrect": False, "feedback": "You find shoes in a store, not in a plate."},
        {"text": "Le ho trovate in un piccolo tavolo qui vicino a casa.", "isCorrect": False, "feedback": "You buy shoes in a store, not a table."}
      ]
    },
    {
      "id": "m6", "role": "host", "text": "Ottimo affare. Hai sempre molto gusto nel vestire.", "english": "Great deal. You always have a lot of taste in dressing.",
      "choices": [
        {"text": "Ti ringrazio, è un bel complimento. Cerco sempre di fare attenzione.", "isCorrect": True, "feedback": "Graciously accepting the compliment about style."},
        {"text": "Ti ringrazio, è un bel problema. Cerco sempre di fare attenzione.", "isCorrect": False, "feedback": "A compliment is not a problem."},
        {"text": "Ti ringrazio, è un bel giardino. Cerco sempre di fare attenzione.", "isCorrect": False, "feedback": "You are talking about a compliment, not a garden."}
      ]
    },
    {
      "id": "m7", "role": "host", "text": "Si vede! Ogni dettaglio è curato, anche la camicia.", "english": "It shows! Every detail is neat, even the shirt.",
      "choices": [
        {"text": "Grazie ancora! Questa camicia è un regalo di mia sorella.", "isCorrect": True, "feedback": "Providing more context about the complimented item."},
        {"text": "Grazie ancora! Questa pioggia è un regalo di mia sorella.", "isCorrect": False, "feedback": "You are talking about a shirt, not the rain."},
        {"text": "Grazie ancora! Questa strada è un regalo di mia sorella.", "isCorrect": False, "feedback": "You are talking about clothes, not a street."}
      ]
    },
    {
      "id": "m8", "role": "host", "text": "Tua sorella ha ottimo gusto. Il regalo perfetto per te.", "english": "Your sister has excellent taste. The perfect gift for you.",
      "choices": [
        {"text": "Sì, mi conosce molto bene. Sa sempre cosa mi piace.", "isCorrect": True, "feedback": "Agreeing and expanding on the relationship."},
        {"text": "Sì, mi dimentica molto bene. Sa sempre cosa mi piace.", "isCorrect": False, "feedback": "If she knows what you like, she doesn't forget you."},
        {"text": "Sì, mi saluta molto bene. Sa sempre cosa mi piace.", "isCorrect": False, "feedback": "Greeting is not relevant to choosing a gift."}
      ]
    },
    {
      "id": "m9", "role": "host", "text": "Beh, siamo pronti. Andiamo a fare questa passeggiata?", "english": "Well, we are ready. Shall we go take this walk?",
      "choices": [
        {"text": "Certamente, andiamo! Sono sicuro che ci divertiremo molto.", "isCorrect": True, "feedback": "Agreeing to start the activity."},
        {"text": "Certamente, dormiamo! Sono sicuro che ci divertiremo molto.", "isCorrect": False, "feedback": "You are going for a walk, not sleeping."},
        {"text": "Certamente, lavoriamo! Sono sicuro che ci divertiremo molto.", "isCorrect": False, "feedback": "The host suggested a walk, not working."}
      ]
    },
    {
      "id": "m10", "role": "host", "text": "Sì, è una giornata stupenda. Sarà un bel pomeriggio.", "english": "Yes, it's a wonderful day. It will be a nice afternoon.",
      "choices": [
        {"text": "Hai ragione. La tua giacca blu è perfetta per oggi.", "isCorrect": True, "feedback": "A nice wrap-up referring back to the initial compliment."},
        {"text": "Hai torto. La tua giacca blu è terribile per oggi.", "isCorrect": False, "feedback": "You shouldn't suddenly be rude!"},
        {"text": "Hai freddo. La tua giacca blu è bagnata per oggi.", "isCorrect": False, "feedback": "You are going for a walk, the jacket is fine."}
      ]
    }
  ]
}

conv2 = {
  "id": "praising_presentation",
  "title": "Praising a Colleague's Presentation",
  "description": "Compliment a colleague on their work presentation.",
  "messages": [
    {
      "id": "m1", "role": "host", "text": "Ehi! Cosa pensi della mia presentazione di oggi?", "english": "Hey! What do you think of my presentation today?",
      "choices": [
        {"text": "È stata un capolavoro! Hai fatto davvero un ottimo lavoro.", "isCorrect": True, "feedback": "A strong compliment for a good presentation."},
        {"text": "È stata un pavimento! Hai fatto davvero un ottimo albero.", "isCorrect": False, "feedback": "A presentation is not a floor or a tree."},
        {"text": "È stata un animale! Hai fatto davvero un ottimo gatto.", "isCorrect": False, "feedback": "You are talking about work, not animals."}
      ]
    },
    {
      "id": "m2", "role": "host", "text": "Grazie! Ero un po' nervoso prima di iniziare a parlare.", "english": "Thank you! I was a bit nervous before starting to speak.",
      "choices": [
        {"text": "Non si vedeva per niente. Sembravi molto sicuro e preparato.", "isCorrect": True, "feedback": "Reassuring them that they looked confident."},
        {"text": "Non si vedeva per niente. Sembravi molto sporco e bagnato.", "isCorrect": False, "feedback": "That's insulting and irrelevant to a presentation."},
        {"text": "Non si vedeva per niente. Sembravi molto alto e quadrato.", "isCorrect": False, "feedback": "You should compliment their skills, not their shape."}
      ]
    },
    {
      "id": "m3", "role": "host", "text": "Meno male! Ho lavorato a questo progetto per due mesi.", "english": "Thank goodness! I worked on this project for two months.",
      "choices": [
        {"text": "Tutto questo impegno si vede. Il risultato è davvero eccellente.", "isCorrect": True, "feedback": "Acknowledging their hard work and the good result."},
        {"text": "Tutto questo sonno si vede. Il divano è davvero eccellente.", "isCorrect": False, "feedback": "You are talking about a project, not sleeping on a sofa."},
        {"text": "Tutto questo freddo si vede. Il mare è davvero eccellente.", "isCorrect": False, "feedback": "Stay on the topic of their work presentation."}
      ]
    },
    {
      "id": "m4", "role": "host", "text": "Ho cercato di rendere i dati chiari e facili da leggere.", "english": "I tried to make the data clear and easy to read.",
      "choices": [
        {"text": "Ci sei riuscito perfettamente. I grafici erano molto belli.", "isCorrect": True, "feedback": "Praising a specific aspect of the presentation."},
        {"text": "Ci sei riuscito perfettamente. I cani erano molto belli.", "isCorrect": False, "feedback": "There are no dogs in a data presentation!"},
        {"text": "Ci sei riuscito perfettamente. I fiori erano molto belli.", "isCorrect": False, "feedback": "You are talking about data, not flowers."}
      ]
    },
    {
      "id": "m5", "role": "host", "text": "Mi fa piacere sentirlo. Credi che le idee siano buone?", "english": "I'm glad to hear that. Do you think the ideas are good?",
      "choices": [
        {"text": "Sì, le tue idee sono sempre originali e molto interessanti.", "isCorrect": True, "feedback": "Complimenting their creativity and thinking."},
        {"text": "Sì, le tue scarpe sono sempre originali e molto interessanti.", "isCorrect": False, "feedback": "You are talking about ideas, not shoes."},
        {"text": "Sì, le tue finestre sono sempre originali e molto grandi.", "isCorrect": False, "feedback": "You are discussing a project, not windows."}
      ]
    },
    {
      "id": "m6", "role": "host", "text": "Apprezzo molto il tuo supporto. Lavorare insieme è bello.", "english": "I really appreciate your support. Working together is nice.",
      "choices": [
        {"text": "Il piacere è mio. Sei un collega con un grande talento.", "isCorrect": True, "feedback": "Returning the sentiment and adding another compliment."},
        {"text": "Il piacere è mio. Sei un fiume con un grande ponte.", "isCorrect": False, "feedback": "You are talking to a colleague, not a river."},
        {"text": "Il piacere è mio. Sei un sole con un grande cielo.", "isCorrect": False, "feedback": "Keep the compliments professional and realistic."}
      ]
    },
    {
      "id": "m7", "role": "host", "text": "Grazie! Anche tu sei molto bravo nel tuo lavoro quotidiano.", "english": "Thank you! You are also very good at your daily work.",
      "choices": [
        {"text": "Grazie, sei molto gentile. Facciamo davvero una bella squadra.", "isCorrect": True, "feedback": "Accepting the compliment and emphasizing teamwork."},
        {"text": "Grazie, sei molto veloce. Facciamo davvero una bella torta.", "isCorrect": False, "feedback": "You are working in an office, not baking a cake."},
        {"text": "Grazie, sei molto alto. Facciamo davvero una bella casa.", "isCorrect": False, "feedback": "You are working together on projects, not building houses."}
      ]
    },
    {
      "id": "m8", "role": "host", "text": "Esatto! Spero che il direttore approvi la nostra proposta.", "english": "Exactly! I hope the director approves our proposal.",
      "choices": [
        {"text": "Con una presentazione così, il successo è sicuramente garantito.", "isCorrect": True, "feedback": "Showing confidence in their work."},
        {"text": "Con una presentazione così, il muro è sicuramente garantito.", "isCorrect": False, "feedback": "A presentation does not guarantee a wall."},
        {"text": "Con una presentazione così, il cane è sicuramente garantito.", "isCorrect": False, "feedback": "A presentation does not guarantee a dog."}
      ]
    },
    {
      "id": "m9", "role": "host", "text": "Speriamo bene. Ora andiamo a prendere un caffè insieme?", "english": "Let's hope for the best. Shall we go get a coffee together now?",
      "choices": [
        {"text": "Ottima idea! Festeggiamo questo tuo grande traguardo di oggi.", "isCorrect": True, "feedback": "Agreeing to celebrate their success."},
        {"text": "Ottima idea! Piangiamo questo tuo grande traguardo di oggi.", "isCorrect": False, "feedback": "You celebrate a success, you don't cry over it."},
        {"text": "Ottima idea! Dimentichiamo questo tuo grande traguardo di oggi.", "isCorrect": False, "feedback": "You should celebrate, not forget it."}
      ]
    },
    {
      "id": "m10", "role": "host", "text": "Perfetto, offro io questa volta. Te lo meriti tutto.", "english": "Perfect, it's on me this time. You deserve it all.",
      "choices": [
        {"text": "Grazie mille, accetto con molto piacere. Andiamo subito allora!", "isCorrect": True, "feedback": "Politely accepting the offer."},
        {"text": "Grazie mille, chiudo con molto piacere. Andiamo subito allora!", "isCorrect": False, "feedback": "You are accepting a coffee, not closing something."},
        {"text": "Grazie mille, apro con molto piacere. Andiamo subito allora!", "isCorrect": False, "feedback": "You accept an offer, you don't open it."}
      ]
    }
  ]
}

conv3 = {
  "id": "complimenting_cooking",
  "title": "Complimenting the Host's Cooking",
  "description": "Give compliments to your host about their delicious dinner.",
  "messages": [
    {
      "id": "m1", "role": "host", "text": "Benvenuti! Spero che vi piaccia la cena che ho preparato.", "english": "Welcome! I hope you like the dinner I prepared.",
      "choices": [
        {"text": "Grazie per l'invito! L'aspetto di questi piatti è meraviglioso.", "isCorrect": True, "feedback": "A great initial compliment on the food's appearance."},
        {"text": "Grazie per l'invito! L'aspetto di questi muri è meraviglioso.", "isCorrect": False, "feedback": "You are looking at food, not the walls."},
        {"text": "Grazie per l'invito! L'aspetto di questi sassi è meraviglioso.", "isCorrect": False, "feedback": "You are eating food, not stones."}
      ]
    },
    {
      "id": "m2", "role": "host", "text": "Siete molto gentili. Prego, sedetevi e iniziamo a mangiare.", "english": "You are very kind. Please, sit down and let's start eating.",
      "choices": [
        {"text": "Il profumo è davvero delizioso. Cosa hai cucinato di buono?", "isCorrect": True, "feedback": "Complimenting the smell and asking about the dish."},
        {"text": "Il rumore è davvero delizioso. Cosa hai cantato di buono?", "isCorrect": False, "feedback": "You smell food, you don't hear it."},
        {"text": "Il silenzio è davvero delizioso. Cosa hai dormito di buono?", "isCorrect": False, "feedback": "You are at a dinner, not in bed."}
      ]
    },
    {
      "id": "m3", "role": "host", "text": "Ho fatto una pasta al forno con una mia ricetta segreta.", "english": "I made a baked pasta with a secret recipe of mine.",
      "choices": [
        {"text": "Che delizia! Sei un cuoco fantastico, è davvero molto gustosa.", "isCorrect": True, "feedback": "Praising their cooking skills directly."},
        {"text": "Che delizia! Sei un albero fantastico, è davvero molto gustosa.", "isCorrect": False, "feedback": "The host is a cook, not a tree."},
        {"text": "Che delizia! Sei un libro fantastico, è davvero molto gustosa.", "isCorrect": False, "feedback": "You eat food, not books."}
      ]
    },
    {
      "id": "m4", "role": "host", "text": "Grazie, sono felice che ti piaccia. Vuoi un altro po'?", "english": "Thank you, I am happy you like it. Do you want a little more?",
      "choices": [
        {"text": "Volentieri! È così squisito che non riesco a smettere.", "isCorrect": True, "feedback": "Enthusiastically accepting more food is a great compliment."},
        {"text": "Volentieri! È così difficile che non riesco a smettere.", "isCorrect": False, "feedback": "Food is not 'difficult' to eat in a good way."},
        {"text": "Volentieri! È così pesante che non riesco a smettere.", "isCorrect": False, "feedback": "Calling food 'heavy' is not a compliment."}
      ]
    },
    {
      "id": "m5", "role": "host", "text": "Ecco a te. Ho preparato anche un secondo piatto di carne.", "english": "Here you go. I also prepared a second dish of meat.",
      "choices": [
        {"text": "Non vedo l'ora di assaggiarlo. La tua cucina è ottima.", "isCorrect": True, "feedback": "Expressing excitement for the next dish."},
        {"text": "Non vedo l'ora di lavarlo. La tua piscina è ottima.", "isCorrect": False, "feedback": "You eat meat, you don't wash it in a pool."},
        {"text": "Non vedo l'ora di perderlo. La tua montagna è ottima.", "isCorrect": False, "feedback": "You are at a dinner table, not on a mountain."}
      ]
    },
    {
      "id": "m6", "role": "host", "text": "Spero che la carne non sia troppo cotta per i vostri gusti.", "english": "I hope the meat is not too cooked for your tastes.",
      "choices": [
        {"text": "Al contrario, è cotta alla perfezione. È molto tenera.", "isCorrect": True, "feedback": "Reassuring the host that the food is perfect."},
        {"text": "Al contrario, è cruda alla perfezione. È molto dura.", "isCorrect": False, "feedback": "Saying meat is raw and tough is an insult."},
        {"text": "Al contrario, è fredda alla perfezione. È molto vecchia.", "isCorrect": False, "feedback": "Nobody likes cold, old meat!"}
      ]
    },
    {
      "id": "m7", "role": "host", "text": "Meno male! E come vi sembra il vino che ho scelto?", "english": "Thank goodness! And how does the wine I chose seem to you?",
      "choices": [
        {"text": "Hai fatto un'ottima scelta. Si abbina perfettamente al pasto.", "isCorrect": True, "feedback": "Complimenting their choice of wine."},
        {"text": "Hai fatto una brutta scelta. Si abbina perfettamente al tavolo.", "isCorrect": False, "feedback": "You should compliment, not criticize the wine."},
        {"text": "Hai fatto una rossa scelta. Si abbina perfettamente al divano.", "isCorrect": False, "feedback": "Wine pairs with food, not sofas."}
      ]
    },
    {
      "id": "m8", "role": "host", "text": "È un vino locale. Mi piace sostenere i produttori della zona.", "english": "It is a local wine. I like to support local producers.",
      "choices": [
        {"text": "È una bella idea. Ha un sapore davvero molto elegante.", "isCorrect": True, "feedback": "Agreeing and adding another compliment on the taste."},
        {"text": "È una bella pietra. Ha un rumore davvero molto elegante.", "isCorrect": False, "feedback": "Wine is a drink, not a stone with noise."},
        {"text": "È una bella porta. Ha un silenzio davvero molto elegante.", "isCorrect": False, "feedback": "You are drinking wine, not looking at a door."}
      ]
    },
    {
      "id": "m9", "role": "host", "text": "Siamo quasi alla fine. Avete ancora un po' di spazio per il dolce?", "english": "We are almost at the end. Do you still have a little room for dessert?",
      "choices": [
        {"text": "Certamente! C'è sempre spazio per i tuoi dolci favolosi.", "isCorrect": True, "feedback": "Showing excitement for their dessert."},
        {"text": "Certamente! C'è sempre spazio per i tuoi muri favolosi.", "isCorrect": False, "feedback": "You eat dessert, not walls."},
        {"text": "Certamente! C'è sempre spazio per i tuoi sassi favolosi.", "isCorrect": False, "feedback": "You can't eat stones for dessert."}
      ]
    },
    {
      "id": "m10", "role": "host", "text": "Ho fatto una torta al cioccolato. Spero vi piacerà molto.", "english": "I made a chocolate cake. I hope you will like it a lot.",
      "choices": [
        {"text": "Non ne dubito. Grazie ancora per questa ospitalità eccezionale.", "isCorrect": True, "feedback": "A final compliment summarizing the host's hospitality."},
        {"text": "Non ne dubito. Grazie ancora per questa pioggia eccezionale.", "isCorrect": False, "feedback": "You are indoors eating, rain is irrelevant."},
        {"text": "Non ne dubito. Grazie ancora per questa strada eccezionale.", "isCorrect": False, "feedback": "Hospitality is about how you are treated at home, not a street."}
      ]
    }
  ]
}

conv4 = {
  "id": "receiving_compliment",
  "title": "Receiving a Compliment Graciously",
  "description": "Learn how to accept a compliment from a friend.",
  "messages": [
    {
      "id": "m1", "role": "host", "text": "Ciao! Devo dire che hai sempre un sorriso così contagioso.", "english": "Hi! I have to say you always have such a contagious smile.",
      "choices": [
        {"text": "Ciao! Grazie, sei davvero molto gentile a dirmi questo.", "isCorrect": True, "feedback": "A polite and gracious way to accept a compliment."},
        {"text": "Ciao! Grazie, sei davvero molto cattivo a dirmi questo.", "isCorrect": False, "feedback": "A compliment is kind, not mean."},
        {"text": "Ciao! Grazie, sei davvero molto freddo a dirmi questo.", "isCorrect": False, "feedback": "Being cold is not a good response to warmth."}
      ]
    },
    {
      "id": "m2", "role": "host", "text": "È la verità. Metti sempre tutti di buon umore qui.", "english": "It is the truth. You always put everyone in a good mood here.",
      "choices": [
        {"text": "Mi fa piacere saperlo. Credo che essere positivi sia importante.", "isCorrect": True, "feedback": "Explaining your positive attitude."},
        {"text": "Mi fa piacere saperlo. Credo che essere tristi sia importante.", "isCorrect": False, "feedback": "Being sad does not put people in a good mood."},
        {"text": "Mi fa piacere saperlo. Credo che essere arrabbiati sia importante.", "isCorrect": False, "feedback": "Anger doesn't create a contagious smile."}
      ]
    },
    {
      "id": "m3", "role": "host", "text": "Assolutamente. E ho notato che hai molta pazienza con tutti.", "english": "Absolutely. And I noticed you have a lot of patience with everyone.",
      "choices": [
        {"text": "Ti ringrazio. Cerco sempre di ascoltare le altre persone.", "isCorrect": True, "feedback": "Connecting patience with listening skills."},
        {"text": "Ti ringrazio. Cerco sempre di ignorare le altre persone.", "isCorrect": False, "feedback": "Ignoring people is the opposite of being patient."},
        {"text": "Ti ringrazio. Cerco sempre di scappare dalle altre persone.", "isCorrect": False, "feedback": "Running away is not a sign of patience."}
      ]
    },
    {
      "id": "m4", "role": "host", "text": "È una dote rara. Sei una persona davvero molto speciale.", "english": "It is a rare gift. You are a really very special person.",
      "choices": [
        {"text": "Non so cosa dire, mi fai arrossire. Troppi complimenti oggi!", "isCorrect": True, "feedback": "A humble and charming way to react to high praise."},
        {"text": "Non so cosa dire, mi fai dormire. Troppi complimenti oggi!", "isCorrect": False, "feedback": "Compliments shouldn't put you to sleep."},
        {"text": "Non so cosa dire, mi fai piangere. Troppi complimenti oggi!", "isCorrect": False, "feedback": "Unless they are tears of joy, this is unusual."}
      ]
    },
    {
      "id": "m5", "role": "host", "text": "Meriti queste parole. Anche il tuo ultimo progetto è fantastico.", "english": "You deserve these words. Also your latest project is fantastic.",
      "choices": [
        {"text": "Grazie di cuore. Ho messo molto impegno in quel lavoro.", "isCorrect": True, "feedback": "Accepting the praise for your hard work."},
        {"text": "Grazie di cuore. Ho messo molta acqua in quel lavoro.", "isCorrect": False, "feedback": "You put effort into a project, not water."},
        {"text": "Grazie di cuore. Ho messo molta sabbia in quel lavoro.", "isCorrect": False, "feedback": "Projects don't require sand, they require effort."}
      ]
    },
    {
      "id": "m6", "role": "host", "text": "I risultati si vedono. Sei sempre molto attento ai dettagli.", "english": "The results are visible. You are always very attentive to details.",
      "choices": [
        {"text": "È bello che tu l'abbia notato. Apprezzo davvero il tuo parere.", "isCorrect": True, "feedback": "Valuing the other person's opinion."},
        {"text": "È bello che tu l'abbia mangiato. Apprezzo davvero il tuo parere.", "isCorrect": False, "feedback": "You notice details, you don't eat them."},
        {"text": "È bello che tu l'abbia rotto. Apprezzo davvero il tuo parere.", "isCorrect": False, "feedback": "Breaking things is not a good thing."}
      ]
    },
    {
      "id": "m7", "role": "host", "text": "Prego. Spero di poter imparare qualcosa dal tuo metodo di lavoro.", "english": "You're welcome. I hope I can learn something from your working method.",
      "choices": [
        {"text": "Ma certo! Possiamo lavorare insieme qualche volta se ti va.", "isCorrect": True, "feedback": "Offering collaboration is a generous response."},
        {"text": "Ma certo! Possiamo dormire insieme qualche volta se ti va.", "isCorrect": False, "feedback": "You collaborate on work, you don't sleep at work."},
        {"text": "Ma certo! Possiamo piangere insieme qualche volta se ti va.", "isCorrect": False, "feedback": "Working together shouldn't make you cry."}
      ]
    },
    {
      "id": "m8", "role": "host", "text": "Sarebbe fantastico. Sei sempre pronto ad aiutare gli amici.", "english": "That would be fantastic. You are always ready to help friends.",
      "choices": [
        {"text": "Per me è un piacere. L'amicizia è una cosa importante.", "isCorrect": True, "feedback": "A warm statement about friendship."},
        {"text": "Per me è un dolore. L'amicizia è una cosa importante.", "isCorrect": False, "feedback": "Helping friends should be a pleasure, not a pain."},
        {"text": "Per me è un fastidio. L'amicizia è una cosa importante.", "isCorrect": False, "feedback": "Calling friendship annoying is bad."}
      ]
    },
    {
      "id": "m9", "role": "host", "text": "Sono fortunato ad averti come amico. Grazie per esserci sempre.", "english": "I am lucky to have you as a friend. Thank you for always being there.",
      "choices": [
        {"text": "Anche io sono fortunato. E anche tu sei una persona stupenda.", "isCorrect": True, "feedback": "Returning the compliment to your friend."},
        {"text": "Anche io sono stanco. E anche tu sei una persona stupenda.", "isCorrect": False, "feedback": "Being tired doesn't fit the context here."},
        {"text": "Anche io sono arrabbiato. E anche tu sei una persona stupenda.", "isCorrect": False, "feedback": "Anger doesn't make sense after a nice compliment."}
      ]
    },
    {
      "id": "m10", "role": "host", "text": "Bene, ora torniamo al lavoro, altrimenti non finiamo più oggi!", "english": "Well, now let's go back to work, otherwise we won't finish today!",
      "choices": [
        {"text": "Hai ragione. Grazie ancora per questa bella chiacchierata. A dopo!", "isCorrect": True, "feedback": "Politely concluding the conversation and returning to work."},
        {"text": "Hai ragione. Grazie ancora per questa brutta corsa. A dopo!", "isCorrect": False, "feedback": "It was a nice chat, not a bad run."},
        {"text": "Hai ragione. Grazie ancora per questa lenta camminata. A dopo!", "isCorrect": False, "feedback": "You were chatting, not walking slowly."}
      ]
    }
  ]
}

data = {
  "scenarioId": 78,
  "conversations": [conv1, conv2, conv3, conv4]
}

with open("src/data/exports/social/compliments/conversations.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Now, generate mini_lessons.json
lessons = {
  "scenario_id": 78,
  "domain": "social/compliments",
  "lessons": [
    {
      "id": "compliment_clothes",
      "title": "Complimenting Clothes",
      "description": "Learn how to compliment someone's outfit and accessories.",
      "grammar_focus": "Adjectives of appearance",
      "vocabulary": ["vestito", "bello", "elegante", "scarpe", "giacca"]
    },
    {
      "id": "compliment_work",
      "title": "Praising Good Work",
      "description": "Learn to give positive feedback on a colleague's professional effort.",
      "grammar_focus": "Expressing admiration",
      "vocabulary": ["ottimo", "lavoro", "presentazione", "progetto", "risultato"]
    },
    {
      "id": "compliment_food",
      "title": "Complimenting Food",
      "description": "Express appreciation for a host's cooking and the meal.",
      "grammar_focus": "Food-related adjectives",
      "vocabulary": ["buono", "delizioso", "gustoso", "squisito", "cucina"]
    },
    {
      "id": "accepting_compliments",
      "title": "Accepting Compliments",
      "description": "How to politely receive a compliment and show gratitude.",
      "grammar_focus": "Polite responses",
      "vocabulary": ["grazie", "gentile", "apprezzare", "piacere", "onore"]
    },
    {
      "id": "compliment_character",
      "title": "Praising Character",
      "description": "Compliment a person's character traits like patience or kindness.",
      "grammar_focus": "Abstract qualities",
      "vocabulary": ["gentilezza", "sorriso", "simpatia", "talento", "capacità"]
    },
    {
      "id": "returning_compliment",
      "title": "Returning a Compliment",
      "description": "How to naturally return a compliment to the person who gave it.",
      "grammar_focus": "Reciprocal expressions",
      "vocabulary": ["anche", "davvero", "fantastico", "meraviglioso", "stupendo"]
    }
  ]
}

with open("src/data/exports/social/compliments/mini_lessons.json", "w") as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Created conversations.json and mini_lessons.json")
