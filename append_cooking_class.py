import json
import os

scenario_path = 'src/data/exports/dining/cooking_class/dining_cooking_class_sentences.json'
with open(scenario_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_sentences = [
    {
        "id": "s30-s31",
        "italian": "\"Quanta farina serve per l'impasto?\" \"La ricetta dice 400 grammi.\"",
        "english": "\"How much flour is needed for the dough?\" \"The recipe says 400 grams.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Quanta farina serve per l'impasto?\" \"La ricetta dice 400 grammi.\"",
            "\"Quanta acqua serve per bere?\" \"La bottiglia dice 400 metri.\"",
            "\"Quanto sale serve per il dolce?\" \"Il barattolo dice 400 grammi.\"",
            "\"Quanta polvere serve per la sala?\" \"Il muro dice 400 metri.\""
        ],
        "choicesEnglish": [
            "\"How much flour is needed for the dough?\" \"The recipe says 400 grams.\"",
            "\"How much water is needed to drink?\" \"The bottle says 400 meters.\"",
            "\"How much salt is needed for the dessert?\" \"The jar says 400 grams.\"",
            "\"How much dust is needed for the hall?\" \"The wall says 400 meters.\""
        ],
        "correctAnswerItalian": "\"Quanta farina serve per l'impasto?\" \"La ricetta dice 400 grammi.\"",
        "correctAnswerEnglish": "\"How much flour is needed for the dough?\" \"The recipe says 400 grams.\"",
        "feedback": {
            "correctItalian": "Ottimo! Una classica domanda sugli ingredienti.",
            "incorrectItalian": "No, presta attenzione alle quantità e all'ingrediente corretto.",
            "correctEnglish": "Great! A classic question about ingredients.",
            "incorrectEnglish": "No, pay attention to the quantities and the correct ingredient."
        }
    },
    {
        "id": "s30-s32",
        "italian": "\"Ma non abbiamo la bilancia, come faccio?\" \"Usiamo una tazza, è circa 200 grammi.\"",
        "english": "\"But we don't have the scale, what do I do?\" \"We use a cup, it's about 200 grams.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Ma non abbiamo la bilancia, come faccio?\" \"Usiamo una tazza, è circa 200 grammi.\"",
            "\"Ma non abbiamo il treno, come faccio?\" \"Usiamo una borsa, è circa 200 grammi.\"",
            "\"Ma non abbiamo la borsa, come faccio?\" \"Usiamo un biglietto, è circa 200 euro.\"",
            "\"Ma non abbiamo la luce, come faccio?\" \"Usiamo una porta, è circa 200 litri.\""
        ],
        "choicesEnglish": [
            "\"But we don't have the scale, what do I do?\" \"We use a cup, it's about 200 grams.\"",
            "\"But we don't have the train, what do I do?\" \"We use a bag, it's about 200 grams.\"",
            "\"But we don't have the bag, what do I do?\" \"We use a ticket, it's about 200 euros.\"",
            "\"But we don't have the light, what do I do?\" \"We use a door, it's about 200 liters.\""
        ],
        "correctAnswerItalian": "\"Ma non abbiamo la bilancia, come faccio?\" \"Usiamo una tazza, è circa 200 grammi.\"",
        "correctAnswerEnglish": "\"But we don't have the scale, what do I do?\" \"We use a cup, it's about 200 grams.\"",
        "feedback": {
            "correctItalian": "Esatto. Risolvere un problema comune in cucina.",
            "incorrectItalian": "No, qui si parla di misurare senza bilancia.",
            "correctEnglish": "Exactly. Solving a common problem in the kitchen.",
            "incorrectEnglish": "No, this is about measuring without a scale."
        }
    },
    {
        "id": "s30-s33",
        "italian": "\"Cosa vuol dire fare la fontana?\" \"Disponi la farina a forma di vulcano.\"",
        "english": "\"What does making a fountain mean?\" \"Arrange the flour in the shape of a volcano.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Cosa vuol dire fare la fontana?\" \"Disponi la farina a forma di vulcano.\"",
            "\"Cosa vuol dire fare la doccia?\" \"Disponi la carta a forma di vulcano.\"",
            "\"Cosa vuol dire fare il bagno?\" \"Disponi l'acqua a forma di vulcano.\"",
            "\"Cosa vuol dire fare la spesa?\" \"Disponi le borse a forma di vulcano.\""
        ],
        "choicesEnglish": [
            "\"What does making a fountain mean?\" \"Arrange the flour in the shape of a volcano.\"",
            "\"What does taking a shower mean?\" \"Arrange the paper in the shape of a volcano.\"",
            "\"What does taking a bath mean?\" \"Arrange the water in the shape of a volcano.\"",
            "\"What does doing the shopping mean?\" \"Arrange the bags in the shape of a volcano.\""
        ],
        "correctAnswerItalian": "\"Cosa vuol dire fare la fontana?\" \"Disponi la farina a forma di vulcano.\"",
        "correctAnswerEnglish": "\"What does making a fountain mean?\" \"Arrange the flour in the shape of a volcano.\"",
        "feedback": {
            "correctItalian": "Perfetto! Un termine tecnico spiegato in modo semplice.",
            "incorrectItalian": "No, la fontana si fa con la farina.",
            "correctEnglish": "Perfect! A technical term explained simply.",
            "incorrectEnglish": "No, the fountain is made with flour."
        }
    },
    {
        "id": "s30-s34",
        "italian": "\"Ho le mani tutte appiccicose!\" \"È perfetto, l'impasto prende forma.\"",
        "english": "\"My hands are all sticky!\" \"It's perfect, the dough is taking shape.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Ho le mani tutte appiccicose!\" \"È perfetto, l'impasto prende forma.\"",
            "\"Ho le mani tutte sporche!\" \"È perfetto, la porta prende forma.\"",
            "\"Ho i piedi tutti bagnati!\" \"È perfetto, la pioggia prende forma.\"",
            "\"Ho i capelli tutti lunghi!\" \"È perfetto, il libro prende forma.\""
        ],
        "choicesEnglish": [
            "\"My hands are all sticky!\" \"It's perfect, the dough is taking shape.\"",
            "\"My hands are all dirty!\" \"It's perfect, the door is taking shape.\"",
            "\"My feet are all wet!\" \"It's perfect, the rain is taking shape.\"",
            "\"My hair is all long!\" \"It's perfect, the book is taking shape.\""
        ],
        "correctAnswerItalian": "\"Ho le mani tutte appiccicose!\" \"È perfetto, l'impasto prende forma.\"",
        "correctAnswerEnglish": "\"My hands are all sticky!\" \"It's perfect, the dough is taking shape.\"",
        "feedback": {
            "correctItalian": "Giusto! Un'espressione molto naturale e spontanea.",
            "incorrectItalian": "Attenzione al contesto: si parla dell'impasto che si attacca alle mani.",
            "correctEnglish": "Right! A very natural and spontaneous expression.",
            "incorrectEnglish": "Pay attention to the context: it's about the dough sticking to your hands."
        }
    },
    {
        "id": "s30-s35",
        "italian": "\"Devo tagliare le verdure fini?\" \"Sì, a cubetti non troppo grandi.\"",
        "english": "\"Should I cut the vegetables finely?\" \"Yes, into not too large cubes.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Devo tagliare le verdure fini?\" \"Sì, a cubetti non troppo grandi.\"",
            "\"Devo tagliare le carte fini?\" \"Sì, a quadrati non troppo piccoli.\"",
            "\"Devo tagliare i mobili fini?\" \"Sì, a cerchi non troppo lunghi.\"",
            "\"Devo tagliare le nuvole fini?\" \"Sì, a linee non troppo basse.\""
        ],
        "choicesEnglish": [
            "\"Should I cut the vegetables finely?\" \"Yes, into not too large cubes.\"",
            "\"Should I cut the papers finely?\" \"Yes, into not too small squares.\"",
            "\"Should I cut the furniture finely?\" \"Yes, into not too long circles.\"",
            "\"Should I cut the clouds finely?\" \"Yes, into not too low lines.\""
        ],
        "correctAnswerItalian": "\"Devo tagliare le verdure fini?\" \"Sì, a cubetti non troppo grandi.\"",
        "correctAnswerEnglish": "\"Should I cut the vegetables finely?\" \"Yes, into not too large cubes.\"",
        "feedback": {
            "correctItalian": "Esatto! Chiedere chiarimenti sul taglio delle verdure.",
            "incorrectItalian": "Scegli l'opzione che parla di verdure e cubetti.",
            "correctEnglish": "Exactly! Asking for clarification on cutting vegetables.",
            "incorrectEnglish": "Choose the option that talks about vegetables and cubes."
        }
    },
    {
        "id": "s30-s36",
        "italian": "\"Le patate le taglio io. Va bene?\" \"Perfetto. A cubetti di un centimetro.\"",
        "english": "\"I'll cut the potatoes. Is that okay?\" \"Perfect. Into one-centimeter cubes.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Le patate le taglio io. Va bene?\" \"Perfetto. A cubetti di un centimetro.\"",
            "\"Le banane le mangio io. Va bene?\" \"Perfetto. A morsi di un centimetro.\"",
            "\"Le fragole le lavo io. Va bene?\" \"Perfetto. A gocce di un centimetro.\"",
            "\"Le pere le bevo io. Va bene?\" \"Perfetto. A sorsi di un centimetro.\""
        ],
        "choicesEnglish": [
            "\"I'll cut the potatoes. Is that okay?\" \"Perfect. Into one-centimeter cubes.\"",
            "\"I'll eat the bananas. Is that okay?\" \"Perfect. Into one-centimeter bites.\"",
            "\"I'll wash the strawberries. Is that okay?\" \"Perfect. Into one-centimeter drops.\"",
            "\"I'll drink the pears. Is that okay?\" \"Perfect. Into one-centimeter sips.\""
        ],
        "correctAnswerItalian": "\"Le patate le taglio io. Va bene?\" \"Perfetto. A cubetti di un centimetro.\"",
        "correctAnswerEnglish": "\"I'll cut the potatoes. Is that okay?\" \"Perfect. Into one-centimeter cubes.\"",
        "feedback": {
            "correctItalian": "Giusto! Dividersi i compiti in cucina.",
            "incorrectItalian": "Il contesto è la preparazione delle patate, non della frutta.",
            "correctEnglish": "Right! Dividing tasks in the kitchen.",
            "incorrectEnglish": "The context is preparing potatoes, not fruit."
        }
    },
    {
        "id": "s30-s37",
        "italian": "\"Oddio, schizzano dappertutto!\" \"Copri con un coperchio, ma lascia uno spiraglio.\"",
        "english": "\"Oh my god, they're splattering everywhere!\" \"Cover with a lid, but leave a crack.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Oddio, schizzano dappertutto!\" \"Copri con un coperchio, ma lascia uno spiraglio.\"",
            "\"Oddio, dormono dappertutto!\" \"Copri con un tappeto, ma lascia un cuscino.\"",
            "\"Oddio, corrono dappertutto!\" \"Copri con una porta, ma lascia una chiave.\"",
            "\"Oddio, cadono dappertutto!\" \"Copri con un ombrello, ma lascia una nuvola.\""
        ],
        "choicesEnglish": [
            "\"Oh my god, they're splattering everywhere!\" \"Cover with a lid, but leave a crack.\"",
            "\"Oh my god, they're sleeping everywhere!\" \"Cover with a rug, but leave a pillow.\"",
            "\"Oh my god, they're running everywhere!\" \"Cover with a door, but leave a key.\"",
            "\"Oh my god, they're falling everywhere!\" \"Cover with an umbrella, but leave a cloud.\""
        ],
        "correctAnswerItalian": "\"Oddio, schizzano dappertutto!\" \"Copri con un coperchio, ma lascia uno spiraglio.\"",
        "correctAnswerEnglish": "\"Oh my god, they're splattering everywhere!\" \"Cover with a lid, but leave a crack.\"",
        "feedback": {
            "correctItalian": "Ottimo! Una reazione realistica all'olio caldo che schizza.",
            "incorrectItalian": "No, \"schizzare\" si riferisce ai liquidi caldi, quindi serve un coperchio.",
            "correctEnglish": "Great! A realistic reaction to splattering hot oil.",
            "incorrectEnglish": "No, \"schizzare\" refers to hot liquids, so you need a lid."
        }
    },
    {
        "id": "s30-s38",
        "italian": "\"Ma come, non si pesa?\" \"In cucina si va a occhio, a sensazione.\"",
        "english": "\"But how come we don't weigh it?\" \"In the kitchen you go by eye, by feeling.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Ma come, non si pesa?\" \"In cucina si va a occhio, a sensazione.\"",
            "\"Ma come, non si corre?\" \"In ufficio si va a corsa, a sensazione.\"",
            "\"Ma come, non si dorme?\" \"In strada si va a caso, a sensazione.\"",
            "\"Ma come, non si canta?\" \"In barca si va a voce, a sensazione.\""
        ],
        "choicesEnglish": [
            "\"But how come we don't weigh it?\" \"In the kitchen you go by eye, by feeling.\"",
            "\"But how come we don't run?\" \"In the office you go by running, by feeling.\"",
            "\"But how come we don't sleep?\" \"In the street you go randomly, by feeling.\"",
            "\"But how come we don't sing?\" \"In the boat you go by voice, by feeling.\""
        ],
        "correctAnswerItalian": "\"Ma come, non si pesa?\" \"In cucina si va a occhio, a sensazione.\"",
        "correctAnswerEnglish": "\"But how come we don't weigh it?\" \"In the kitchen you go by eye, by feeling.\"",
        "feedback": {
            "correctItalian": "Esatto! Un concetto classico della cucina italiana.",
            "incorrectItalian": "Scegli l'opzione che parla di pesare (misurare) e cucinare.",
            "correctEnglish": "Exactly! A classic concept of Italian cooking.",
            "incorrectEnglish": "Choose the option that talks about weighing (measuring) and cooking."
        }
    },
    {
        "id": "s30-s39",
        "italian": "\"Quanta acqua?\" \"Almeno due litri per 400 grammi di pasta.\"",
        "english": "\"How much water?\" \"At least two liters for 400 grams of pasta.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Quanta acqua?\" \"Almeno due litri per 400 grammi di pasta.\"",
            "\"Quanto vino?\" \"Almeno due chili per 400 grammi di carne.\"",
            "\"Quanta birra?\" \"Almeno due bottiglie per 400 grammi di pane.\"",
            "\"Quanto latte?\" \"Almeno due tazze per 400 grammi di caffè.\""
        ],
        "choicesEnglish": [
            "\"How much water?\" \"At least two liters for 400 grams of pasta.\"",
            "\"How much wine?\" \"At least two kilos for 400 grams of meat.\"",
            "\"How much beer?\" \"At least two bottles for 400 grams of bread.\"",
            "\"How much milk?\" \"At least two cups for 400 grams of coffee.\""
        ],
        "correctAnswerItalian": "\"Quanta acqua?\" \"Almeno due litri per 400 grammi di pasta.\"",
        "correctAnswerEnglish": "\"How much water?\" \"At least two liters for 400 grams of pasta.\"",
        "feedback": {
            "correctItalian": "Perfetto. Informazione vitale per cuocere la pasta correttamente.",
            "incorrectItalian": "Attenzione: si parla di acqua per la pasta, non di altre bevande.",
            "correctEnglish": "Perfect. Vital information for cooking pasta correctly.",
            "incorrectEnglish": "Attention: we're talking about water for pasta, not other drinks."
        }
    },
    {
        "id": "s30-s40",
        "italian": "\"L'acqua bolle già! Mettiamo la pasta?\" \"Sì, ma prima assaggia l'acqua.\"",
        "english": "\"The water is already boiling! Should we put the pasta in?\" \"Yes, but first taste the water.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"L'acqua bolle già! Mettiamo la pasta?\" \"Sì, ma prima assaggia l'acqua.\"",
            "\"L'acqua piove già! Mettiamo la sedia?\" \"Sì, ma prima assaggia l'aria.\"",
            "\"L'acqua scende già! Mettiamo la barca?\" \"Sì, ma prima assaggia il mare.\"",
            "\"L'acqua sale già! Mettiamo la scala?\" \"Sì, ma prima assaggia il tetto.\""
        ],
        "choicesEnglish": [
            "\"The water is already boiling! Should we put the pasta in?\" \"Yes, but first taste the water.\"",
            "\"The water is raining already! Should we put the chair in?\" \"Yes, but first taste the air.\"",
            "\"The water is going down already! Should we put the boat in?\" \"Yes, but first taste the sea.\"",
            "\"The water is going up already! Should we put the ladder in?\" \"Yes, but first taste the roof.\""
        ],
        "correctAnswerItalian": "\"L'acqua bolle già! Mettiamo la pasta?\" \"Sì, ma prima assaggia l'acqua.\"",
        "correctAnswerEnglish": "\"The water is already boiling! Should we put the pasta in?\" \"Yes, but first taste the water.\"",
        "feedback": {
            "correctItalian": "Ottimo. Bisogna sempre assicurarsi che l'acqua sia salata.",
            "incorrectItalian": "Il verbo corretto qui è \"bollire\" (to boil).",
            "correctEnglish": "Great. You must always make sure the water is salty.",
            "incorrectEnglish": "The correct verb here is \"bollire\" (to boil)."
        }
    },
    {
        "id": "s30-s41",
        "italian": "\"Mantecare? Cos'è?\" \"Vuol dire mescolare bene a fuoco vivo.\"",
        "english": "\"Mantecare? What is it?\" \"It means mixing well over high heat.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Mantecare? Cos'è?\" \"Vuol dire mescolare bene a fuoco vivo.\"",
            "\"Mantecare? Cos'è?\" \"Vuol dire tagliare bene a luce viva.\"",
            "\"Mantecare? Cos'è?\" \"Vuol dire saltare bene a freddo vivo.\"",
            "\"Mantecare? Cos'è?\" \"Vuol dire dormire bene a sole vivo.\""
        ],
        "choicesEnglish": [
            "\"Mantecare? What is it?\" \"It means mixing well over high heat.\"",
            "\"Mantecare? What is it?\" \"It means cutting well under bright light.\"",
            "\"Mantecare? What is it?\" \"It means jumping well in extreme cold.\"",
            "\"Mantecare? What is it?\" \"It means sleeping well in bright sun.\""
        ],
        "correctAnswerItalian": "\"Mantecare? Cos'è?\" \"Vuol dire mescolare bene a fuoco vivo.\"",
        "correctAnswerEnglish": "\"Mantecare? What is it?\" \"It means mixing well over high heat.\"",
        "feedback": {
            "correctItalian": "Giusto! 'Mantecare' è un termine culinario essenziale.",
            "incorrectItalian": "Ricorda che 'mantecare' ha a che fare col mescolare sul fuoco.",
            "correctEnglish": "Right! 'Mantecare' is an essential culinary term.",
            "incorrectEnglish": "Remember that 'mantecare' has to do with mixing over the heat."
        }
    },
    {
        "id": "s30-s42",
        "italian": "\"Devo tagliare le mele fini?\" \"Sottili, sì. E poi le disponi a raggiera.\"",
        "english": "\"Should I cut the apples finely?\" \"Thinly, yes. And then you arrange them in a circle.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Devo tagliare le mele fini?\" \"Sottili, sì. E poi le disponi a raggiera.\"",
            "\"Devo tagliare le porte fini?\" \"Spesse, sì. E poi le disponi a raggiera.\"",
            "\"Devo tagliare le scarpe fini?\" \"Strette, sì. E poi le disponi a raggiera.\"",
            "\"Devo tagliare le borse fini?\" \"Laghe, sì. E poi le disponi a raggiera.\""
        ],
        "choicesEnglish": [
            "\"Should I cut the apples finely?\" \"Thinly, yes. And then you arrange them in a circle.\"",
            "\"Should I cut the doors finely?\" \"Thickly, yes. And then you arrange them in a circle.\"",
            "\"Should I cut the shoes finely?\" \"Tightly, yes. And then you arrange them in a circle.\"",
            "\"Should I cut the bags finely?\" \"Widely, yes. And then you arrange them in a circle.\""
        ],
        "correctAnswerItalian": "\"Devo tagliare le mele fini?\" \"Sottili, sì. E poi le disponi a raggiera.\"",
        "correctAnswerEnglish": "\"Should I cut the apples finely?\" \"Thinly, yes. And then you arrange them in a circle.\"",
        "feedback": {
            "correctItalian": "Perfetto. Si descrive come preparare le mele per la torta.",
            "incorrectItalian": "Questa frase parla delle mele.",
            "correctEnglish": "Perfect. Describes how to prepare apples for the cake.",
            "incorrectEnglish": "This sentence is about apples."
        }
    },
    {
        "id": "s30-s43",
        "italian": "\"Che fatica impastare!\" \"Dai, ancora un minuto. Se premi, torna su.\"",
        "english": "\"What an effort to knead!\" \"Come on, one more minute. If you press, it springs back.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Che fatica impastare!\" \"Dai, ancora un minuto. Se premi, torna su.\"",
            "\"Che fatica cantare!\" \"Dai, ancora un minuto. Se ascolti, torna su.\"",
            "\"Che fatica dormire!\" \"Dai, ancora un minuto. Se chiudi, torna su.\"",
            "\"Che fatica guidare!\" \"Dai, ancora un minuto. Se fermi, torna su.\""
        ],
        "choicesEnglish": [
            "\"What an effort to knead!\" \"Come on, one more minute. If you press, it springs back.\"",
            "\"What an effort to sing!\" \"Come on, one more minute. If you listen, it springs back.\"",
            "\"What an effort to sleep!\" \"Come on, one more minute. If you close, it springs back.\"",
            "\"What an effort to drive!\" \"Come on, one more minute. If you stop, it springs back.\""
        ],
        "correctAnswerItalian": "\"Che fatica impastare!\" \"Dai, ancora un minuto. Se premi, torna su.\"",
        "correctAnswerEnglish": "\"What an effort to knead!\" \"Come on, one more minute. If you press, it springs back.\"",
        "feedback": {
            "correctItalian": "Esatto! Un test classico per controllare l'elasticità dell'impasto.",
            "incorrectItalian": "Il contesto è la stanchezza fisica legata all'impastare ('impastare').",
            "correctEnglish": "Exactly! A classic test to check dough elasticity.",
            "incorrectEnglish": "The context is physical tiredness related to kneading ('impastare')."
        }
    },
    {
        "id": "s30-s44",
        "italian": "\"Il pesto è pronto! Che profumo!\" \"Assaggiamo. Manca sale?\"",
        "english": "\"The pesto is ready! What a smell!\" \"Let's taste. Is it missing salt?\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Il pesto è pronto! Che profumo!\" \"Assaggiamo. Manca sale?\"",
            "\"Il buio è pronto! Che silenzio!\" \"Ascoltiamo. Manca un rumore?\"",
            "\"Il fuoco è pronto! Che caldo!\" \"Guardiamo. Manca una fiamma?\"",
            "\"Il vento è pronto! Che freddo!\" \"Sentiamo. Manca una sciarpa?\""
        ],
        "choicesEnglish": [
            "\"The pesto is ready! What a smell!\" \"Let's taste. Is it missing salt?\"",
            "\"The dark is ready! What a silence!\" \"Let's listen. Is it missing a noise?\"",
            "\"The fire is ready! What a heat!\" \"Let's look. Is it missing a flame?\"",
            "\"The wind is ready! What a cold!\" \"Let's feel. Is it missing a scarf?\""
        ],
        "correctAnswerItalian": "\"Il pesto è pronto! Che profumo!\" \"Assaggiamo. Manca sale?\"",
        "correctAnswerEnglish": "\"The pesto is ready! What a smell!\" \"Let's taste. Is it missing salt?\"",
        "feedback": {
            "correctItalian": "Ottimo! La soddisfazione per un buon pesto.",
            "incorrectItalian": "Scegli l'opzione che parla di cibo (pesto e sale).",
            "correctEnglish": "Great! Satisfaction for a good pesto.",
            "incorrectEnglish": "Choose the option that talks about food (pesto and salt)."
        }
    },
    {
        "id": "s30-s45",
        "italian": "\"La pasta è buonissima. Un po' spessa però.\" \"La prossima volta la stendi di più.\"",
        "english": "\"The pasta is very good. A bit thick though.\" \"Next time you roll it out more.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"La pasta è buonissima. Un po' spessa però.\" \"La prossima volta la stendi di più.\"",
            "\"La pasta è freddissima. Un po' lunga però.\" \"La prossima volta la stendi di meno.\"",
            "\"La pasta è carissima. Un po' corta però.\" \"La prossima volta la compri di più.\"",
            "\"La pasta è altissima. Un po' bassa però.\" \"La prossima volta la vendi di meno.\""
        ],
        "choicesEnglish": [
            "\"The pasta is very good. A bit thick though.\" \"Next time you roll it out more.\"",
            "\"The pasta is very cold. A bit long though.\" \"Next time you roll it out less.\"",
            "\"The pasta is very expensive. A bit short though.\" \"Next time you buy it more.\"",
            "\"The pasta is very high. A bit low though.\" \"Next time you sell it less.\""
        ],
        "correctAnswerItalian": "\"La pasta è buonissima. Un po' spessa però.\" \"La prossima volta la stendi di più.\"",
        "correctAnswerEnglish": "\"The pasta is very good. A bit thick though.\" \"Next time you roll it out more.\"",
        "feedback": {
            "correctItalian": "Perfetto. Un commento costruttivo finale sul risultato.",
            "incorrectItalian": "'Spessa' significa che è troppo grossa o spessa.",
            "correctEnglish": "Perfect. A final constructive comment on the result.",
            "incorrectEnglish": "'Spessa' means it's too thick."
        }
    },
    {
        "id": "s30-s46",
        "italian": "\"Il pesto è buono, ma troppo aglio. Come si aggiusta?\" \"Ormai è tardi.\"",
        "english": "\"The pesto is good, but too much garlic. How do you fix it?\" \"It's too late now.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Il pesto è buono, ma troppo aglio. Come si aggiusta?\" \"Ormai è tardi.\"",
            "\"Il pesto è buono, ma troppo zucchero. Come si aggiusta?\" \"Ormai è presto.\"",
            "\"Il pesto è buono, ma troppo limone. Come si aggiusta?\" \"Ormai è notte.\"",
            "\"Il pesto è buono, ma troppo miele. Come si aggiusta?\" \"Ormai è giorno.\""
        ],
        "choicesEnglish": [
            "\"The pesto is good, but too much garlic. How do you fix it?\" \"It's too late now.\"",
            "\"The pesto is good, but too much sugar. How do you fix it?\" \"It's too early now.\"",
            "\"The pesto is good, but too much lemon. How do you fix it?\" \"It's night now.\"",
            "\"The pesto is good, but too much honey. How do you fix it?\" \"It's day now.\""
        ],
        "correctAnswerItalian": "\"Il pesto è buono, ma troppo aglio. Come si aggiusta?\" \"Ormai è tardi.\"",
        "correctAnswerEnglish": "\"The pesto is good, but too much garlic. How do you fix it?\" \"It's too late now.\"",
        "feedback": {
            "correctItalian": "Giusto. Il pesto classico ha l'aglio, ma si può sbagliare dose.",
            "incorrectItalian": "Il pesto si fa con basilico, pinoli e aglio, non ingredienti dolci.",
            "correctEnglish": "Right. Classic pesto has garlic, but you can mistake the dose.",
            "incorrectEnglish": "Pesto is made with basil, pine nuts, and garlic, not sweet ingredients."
        }
    },
    {
        "id": "s30-s47",
        "italian": "\"Manca solo il caffè. Chi lo fa?\" \"Io faccio il caffè. Moka o macchinetta?\"",
        "english": "\"Only the coffee is missing. Who's making it?\" \"I'll make the coffee. Moka or machine?\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Manca solo il caffè. Chi lo fa?\" \"Io faccio il caffè. Moka o macchinetta?\"",
            "\"Manca solo l'acqua. Chi la beve?\" \"Io bevo l'acqua. Bicchiere o bottiglia?\"",
            "\"Manca solo il tè. Chi lo beve?\" \"Io bevo il tè. Tazza o pentola?\"",
            "\"Manca solo il vino. Chi lo apre?\" \"Io apro il vino. Tappo o vetro?\""
        ],
        "choicesEnglish": [
            "\"Only the coffee is missing. Who's making it?\" \"I'll make the coffee. Moka or machine?\"",
            "\"Only the water is missing. Who's drinking it?\" \"I'll drink the water. Glass or bottle?\"",
            "\"Only the tea is missing. Who's drinking it?\" \"I'll drink the tea. Cup or pot?\"",
            "\"Only the wine is missing. Who's opening it?\" \"I'll open the wine. Cork or glass?\""
        ],
        "correctAnswerItalian": "\"Manca solo il caffè. Chi lo fa?\" \"Io faccio il caffè. Moka o macchinetta?\"",
        "correctAnswerEnglish": "\"Only the coffee is missing. Who's making it?\" \"I'll make the coffee. Moka or machine?\"",
        "feedback": {
            "correctItalian": "Perfetto. La degna conclusione di un pasto italiano.",
            "incorrectItalian": "La moka è la tipica caffettiera italiana.",
            "correctEnglish": "Perfect. The fitting end to an Italian meal.",
            "incorrectEnglish": "The moka is the typical Italian coffee maker."
        }
    },
    {
        "id": "s30-s48",
        "italian": "\"Grazie! È stata un'esperienza bellissima.\" \"Tornerò per la pizza.\"",
        "english": "\"Thank you! It was a beautiful experience.\" \"I will return for the pizza.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Grazie! È stata un'esperienza bellissima.\" \"Tornerò per la pizza.\"",
            "\"Grazie! È stata un'esperienza brutta.\" \"Non tornerò mai più.\"",
            "\"Grazie! È stata un'esperienza noiosa.\" \"Scappo dalla pizza.\"",
            "\"Grazie! È stata un'esperienza fredda.\" \"Piangerò per la pizza.\""
        ],
        "choicesEnglish": [
            "\"Thank you! It was a beautiful experience.\" \"I will return for the pizza.\"",
            "\"Thank you! It was a bad experience.\" \"I will never return again.\"",
            "\"Thank you! It was a boring experience.\" \"I escape from the pizza.\"",
            "\"Thank you! It was a cold experience.\" \"I will cry for the pizza.\""
        ],
        "correctAnswerItalian": "\"Grazie! È stata un'esperienza bellissima.\" \"Tornerò per la pizza.\"",
        "correctAnswerEnglish": "\"Thank you! It was a beautiful experience.\" \"I will return for the pizza.\"",
        "feedback": {
            "correctItalian": "Ottimo. Una conclusione amichevole del corso.",
            "incorrectItalian": "L'esperienza descritta nella conversazione è positiva.",
            "correctEnglish": "Great. A friendly conclusion to the course.",
            "incorrectEnglish": "The experience described in the conversation is positive."
        }
    },
    {
        "id": "s30-s49",
        "italian": "\"C'è scritto di fare la fontana. Cosa vuol dire?\" \"Vuol dire fare un buco al centro.\"",
        "english": "\"It says to make a fountain. What does it mean?\" \"It means making a hole in the center.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"C'è scritto di fare la fontana. Cosa vuol dire?\" \"Vuol dire fare un buco al centro.\"",
            "\"C'è scritto di fare la porta. Cosa vuol dire?\" \"Vuol dire fare un muro al centro.\"",
            "\"C'è scritto di fare la finestra. Cosa vuol dire?\" \"Vuol dire fare un tetto al centro.\"",
            "\"C'è scritto di fare la scala. Cosa vuol dire?\" \"Vuol dire fare un piano al centro.\""
        ],
        "choicesEnglish": [
            "\"It says to make a fountain. What does it mean?\" \"It means making a hole in the center.\"",
            "\"It says to make a door. What does it mean?\" \"It means making a wall in the center.\"",
            "\"It says to make a window. What does it mean?\" \"It means making a roof in the center.\"",
            "\"It says to make a ladder. What does it mean?\" \"It means making a floor in the center.\""
        ],
        "correctAnswerItalian": "\"C'è scritto di fare la fontana. Cosa vuol dire?\" \"Vuol dire fare un buco al centro.\"",
        "correctAnswerEnglish": "\"It says to make a fountain. What does it mean?\" \"It means making a hole in the center.\"",
        "feedback": {
            "correctItalian": "Esatto! La fontana serve a contenere le uova nell'impasto.",
            "incorrectItalian": "Si parla della tecnica culinaria per l'impasto.",
            "correctEnglish": "Exactly! The fountain is used to contain the eggs in the dough.",
            "incorrectEnglish": "We're talking about the culinary technique for dough."
        }
    },
    {
        "id": "s30-s50",
        "italian": "\"Ho aggiunto le uova tutte insieme. È un problema?\" \"Un po', ma non grave.\"",
        "english": "\"I added all the eggs together. Is it a problem?\" \"A bit, but not serious.\"",
        "type": "sentence",
        "choicesItalian": [
            "\"Ho aggiunto le uova tutte insieme. È un problema?\" \"Un po', ma non grave.\"",
            "\"Ho rotto le uova tutte insieme. È un problema?\" \"Tanto, è molto grave.\"",
            "\"Ho mangiato le uova tutte insieme. È un problema?\" \"Troppo, è un disastro.\"",
            "\"Ho comprato le uova tutte insieme. È un problema?\" \"Poco, è un miracolo.\""
        ],
        "choicesEnglish": [
            "\"I added all the eggs together. Is it a problem?\" \"A bit, but not serious.\"",
            "\"I broke all the eggs together. Is it a problem?\" \"A lot, it's very serious.\"",
            "\"I ate all the eggs together. Is it a problem?\" \"Too much, it's a disaster.\"",
            "\"I bought all the eggs together. Is it a problem?\" \"A little, it's a miracle.\""
        ],
        "correctAnswerItalian": "\"Ho aggiunto le uova tutte insieme. È un problema?\" \"Un po', ma non grave.\"",
        "correctAnswerEnglish": "\"I added all the eggs together. Is it a problem?\" \"A bit, but not serious.\"",
        "feedback": {
            "correctItalian": "Perfetto. Un piccolo errore comune per i principianti.",
            "incorrectItalian": "Non è un disastro, solo un piccolo inconveniente.",
            "correctEnglish": "Perfect. A small common mistake for beginners.",
            "incorrectEnglish": "It's not a disaster, just a small inconvenience."
        }
    }
]

data.extend(new_sentences)

with open(scenario_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated cooking_class sentences")
