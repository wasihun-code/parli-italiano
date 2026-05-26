import json

scenario_path = 'src/data/exports/dining/gelato_shop/dining_gelato_shop_sentences.json'
with open(scenario_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_sentences = [
    {
        "id": f"s22-s{i}",
        "italian": italian,
        "english": english,
        "type": "sentence",
        "choicesItalian": choices_it,
        "choicesEnglish": choices_en,
        "correctAnswerItalian": italian,
        "correctAnswerEnglish": english,
        "feedback": {
            "correctItalian": "Esatto! Un'ottima interazione per la gelateria.",
            "incorrectItalian": "Fai attenzione al contesto: si parla di gusti di gelato, coni e coppette.",
            "correctEnglish": "Exactly! A great interaction for the ice cream shop.",
            "incorrectEnglish": "Pay attention to the context: we're talking about ice cream flavors, cones, and cups."
        }
    } for i, (italian, english, choices_it, choices_en) in enumerate([
        (
            "\"Com'è il gusto del mese?\" \"È dolce ma non troppo. Ha pezzetti di fichi veri.\"",
            "\"How is the flavor of the month?\" \"It's sweet but not too much. It has pieces of real figs.\"",
            [
                "\"Com'è il gusto del mese?\" \"È dolce ma non troppo. Ha pezzetti di fichi veri.\"",
                "\"Com'è il film del mese?\" \"È triste ma non troppo. Ha pezzetti di storie vere.\"",
                "\"Com'è il libro del mese?\" \"È lungo ma non troppo. Ha pezzetti di parole vere.\"",
                "\"Com'è il caffè del mese?\" \"È caldo ma non troppo. Ha pezzetti di tazze vere.\""
            ],
            [
                "\"How is the flavor of the month?\" \"It's sweet but not too much. It has pieces of real figs.\"",
                "\"How is the movie of the month?\" \"It's sad but not too much. It has pieces of real stories.\"",
                "\"How is the book of the month?\" \"It's long but not too much. It has pieces of real words.\"",
                "\"How is the coffee of the month?\" \"It's hot but not too much. It has pieces of real cups.\""
            ]
        ),
        (
            "\"Vuole assaggiarlo? Posso darle un cucchiaino.\" \"Sì, grazie!\"",
            "\"Do you want to taste it? I can give you a small spoon.\" \"Yes, thank you!\"",
            [
                "\"Vuole assaggiarlo? Posso darle un cucchiaino.\" \"Sì, grazie!\"",
                "\"Vuole guardarlo? Posso darle un occhiale.\" \"Sì, grazie!\"",
                "\"Vuole ascoltarlo? Posso darle un telefono.\" \"Sì, grazie!\"",
                "\"Vuole scriverlo? Posso darle un quaderno.\" \"Sì, grazie!\""
            ],
            [
                "\"Do you want to taste it? I can give you a small spoon.\" \"Yes, thank you!\"",
                "\"Do you want to look at it? I can give you a glass.\" \"Yes, thank you!\"",
                "\"Do you want to listen to it? I can give you a phone.\" \"Yes, thank you!\"",
                "\"Do you want to write it? I can give you a notebook.\" \"Yes, thank you!\""
            ]
        ),
        (
            "\"Cono o coppetta?\" \"Come preferisce.\"",
            "\"Cone or cup?\" \"As you prefer.\"",
            [
                "\"Cono o coppetta?\" \"Come preferisce.\"",
                "\"Mela o pera?\" \"Come cammina.\"",
                "\"Tavolo o sedia?\" \"Come dorme.\"",
                "\"Porta o finestra?\" \"Come guarda.\""
            ],
            [
                "\"Cone or cup?\" \"As you prefer.\"",
                "\"Apple or pear?\" \"As you walk.\"",
                "\"Table or chair?\" \"As you sleep.\"",
                "\"Door or window?\" \"As you look.\""
            ]
        ),
        (
            "\"Cono più croccante, coppetta più comoda se si sporca.\" \"Mmm, cono.\"",
            "\"Crunchier cone, more comfortable cup if you get dirty.\" \"Mmm, cone.\"",
            [
                "\"Cono più croccante, coppetta più comoda se si sporca.\" \"Mmm, cono.\"",
                "\"Auto più veloce, bici più comoda se piove.\" \"Mmm, auto.\"",
                "\"Letto più grande, divano più comodo se si dorme.\" \"Mmm, letto.\"",
                "\"Piatto più pulito, bicchiere più comodo se si beve.\" \"Mmm, piatto.\""
            ],
            [
                "\"Crunchier cone, more comfortable cup if you get dirty.\" \"Mmm, cone.\"",
                "\"Faster car, more comfortable bike if it rains.\" \"Mmm, car.\"",
                "\"Larger bed, more comfortable sofa if you sleep.\" \"Mmm, bed.\"",
                "\"Cleaner plate, more comfortable glass if you drink.\" \"Mmm, plate.\""
            ]
        ),
        (
            "\"Quanti gusti posso mettere?\" \"Vorrei due gusti.\"",
            "\"How many flavors can I put?\" \"I would like two flavors.\"",
            [
                "\"Quanti gusti posso mettere?\" \"Vorrei due gusti.\"",
                "\"Quanti posti posso prendere?\" \"Vorrei due tavoli.\"",
                "\"Quanti biglietti posso comprare?\" \"Vorrei due treni.\"",
                "\"Quanti film posso guardare?\" \"Vorrei due cinema.\""
            ],
            [
                "\"How many flavors can I put?\" \"I would like two flavors.\"",
                "\"How many seats can I take?\" \"I would like two tables.\"",
                "\"How many tickets can I buy?\" \"I would like two trains.\"",
                "\"How many movies can I watch?\" \"I would like two cinemas.\""
            ]
        ),
        (
            "\"Panna montata sopra?\" \"No, senza panna, grazie.\"",
            "\"Whipped cream on top?\" \"No, without cream, thank you.\"",
            [
                "\"Panna montata sopra?\" \"No, senza panna, grazie.\"",
                "\"Sale grosso sopra?\" \"No, senza sale, grazie.\"",
                "\"Acqua calda sopra?\" \"No, senza acqua, grazie.\"",
                "\"Mela verde sopra?\" \"No, senza mela, grazie.\""
            ],
            [
                "\"Whipped cream on top?\" \"No, without cream, thank you.\"",
                "\"Coarse salt on top?\" \"No, without salt, thank you.\"",
                "\"Hot water on top?\" \"No, without water, thank you.\"",
                "\"Green apple on top?\" \"No, without apple, thank you.\""
            ]
        ),
        (
            "\"Ecco il suo cono: fichi e noci sotto, cioccolato sopra.\" \"Grazie!\"",
            "\"Here is your cone: figs and walnuts on the bottom, chocolate on top.\" \"Thank you!\"",
            [
                "\"Ecco il suo cono: fichi e noci sotto, cioccolato sopra.\" \"Grazie!\"",
                "\"Ecco la sua pizza: sale e pepe sotto, pomodoro sopra.\" \"Grazie!\"",
                "\"Ecco il suo tavolo: sedia e porta sotto, finestra sopra.\" \"Grazie!\"",
                "\"Ecco la sua borsa: chiave e carta sotto, soldi sopra.\" \"Grazie!\""
            ],
            [
                "\"Here is your cone: figs and walnuts on the bottom, chocolate on top.\" \"Thank you!\"",
                "\"Here is your pizza: salt and pepper on the bottom, tomato on top.\" \"Thank you!\"",
                "\"Here is your table: chair and door on the bottom, window on top.\" \"Thank you!\"",
                "\"Here is your bag: key and paper on the bottom, money on top.\" \"Thank you!\""
            ]
        ),
        (
            "\"Mamma, voglio il gelato! Posso prenderne uno grande?\" \"No, piccolo.\"",
            "\"Mom, I want ice cream! Can I get a big one?\" \"No, small.\"",
            [
                "\"Mamma, voglio il gelato! Posso prenderne uno grande?\" \"No, piccolo.\"",
                "\"Mamma, voglio il cane! Posso prenderne uno nero?\" \"No, bianco.\"",
                "\"Mamma, voglio il libro! Posso prenderne uno pesante?\" \"No, leggero.\"",
                "\"Mamma, voglio il letto! Posso prenderne uno freddo?\" \"No, caldo.\""
            ],
            [
                "\"Mom, I want ice cream! Can I get a big one?\" \"No, small.\"",
                "\"Mom, I want the dog! Can I get a black one?\" \"No, white.\"",
                "\"Mom, I want the book! Can I get a heavy one?\" \"No, light.\"",
                "\"Mom, I want the bed! Can I get a cold one?\" \"No, warm.\""
            ]
        ),
        (
            "\"E per me, una coppetta media con pistacchio e stracciatella.\" \"Senza panna.\"",
            "\"And for me, a medium cup with pistachio and stracciatella.\" \"Without cream.\"",
            [
                "\"E per me, una coppetta media con pistacchio e stracciatella.\" \"Senza panna.\"",
                "\"E per me, un tavolo medio con sedia e porta.\" \"Senza finestra.\"",
                "\"E per me, un treno medio con biglietto e stazione.\" \"Senza valigia.\"",
                "\"E per me, un mare medio con acqua e sale.\" \"Senza pesce.\""
            ],
            [
                "\"And for me, a medium cup with pistachio and stracciatella.\" \"Without cream.\"",
                "\"And for me, a medium table with chair and door.\" \"Without window.\"",
                "\"And for me, a medium train with ticket and station.\" \"Without suitcase.\"",
                "\"And for me, a medium sea with water and salt.\" \"Without fish.\""
            ]
        ),
        (
            "\"Vi faccio anche un po' di cioccolato fuso sopra al cono?\" \"Sì, ma poco.\"",
            "\"Should I also do a little melted chocolate on top of the cone?\" \"Yes, but a little.\"",
            [
                "\"Vi faccio anche un po' di cioccolato fuso sopra al cono?\" \"Sì, ma poco.\"",
                "\"Vi faccio anche un po' di sale grosso sopra al pane?\" \"Sì, ma bianco.\"",
                "\"Vi faccio anche un po' di acqua calda sopra al mare?\" \"Sì, ma dolce.\"",
                "\"Vi faccio anche un po' di vento forte sopra al cielo?\" \"Sì, ma caldo.\""
            ],
            [
                "\"Should I also do a little melted chocolate on top of the cone?\" \"Yes, but a little.\"",
                "\"Should I also do a little coarse salt on top of the bread?\" \"Yes, but white.\"",
                "\"Should I also do a little hot water on top of the sea?\" \"Yes, but sweet.\"",
                "\"Should I also do a little strong wind on top of the sky?\" \"Yes, but hot.\""
            ]
        ),
        (
            "\"Ecco il cono. Attenzione che cola.\" \"Totale 5 euro.\"",
            "\"Here is the cone. Be careful it drips.\" \"Total 5 euros.\"",
            [
                "\"Ecco il cono. Attenzione che cola.\" \"Totale 5 euro.\"",
                "\"Ecco il muro. Attenzione che piove.\" \"Totale 5 ore.\"",
                "\"Ecco il cane. Attenzione che corre.\" \"Totale 5 passi.\"",
                "\"Ecco il libro. Attenzione che dorme.\" \"Totale 5 fogli.\""
            ],
            [
                "\"Here is the cone. Be careful it drips.\" \"Total 5 euros.\"",
                "\"Here is the wall. Be careful it rains.\" \"Total 5 hours.\"",
                "\"Here is the dog. Be careful it runs.\" \"Total 5 steps.\"",
                "\"Here is the book. Be careful it sleeps.\" \"Total 5 pages.\""
            ]
        ),
        (
            "\"Quali gusti avete di frutta? Sono astemio ai latticini.\" \"Tutti senza latte.\"",
            "\"What fruit flavors do you have? I am dairy-free.\" \"All without milk.\"",
            [
                "\"Quali gusti avete di frutta? Sono astemio ai latticini.\" \"Tutti senza latte.\"",
                "\"Quali gusti avete di pesce? Sono astemio alle verdure.\" \"Tutti senza mare.\"",
                "\"Quali gusti avete di carne? Sono astemio alle patate.\" \"Tutti senza fuoco.\"",
                "\"Quali gusti avete di pane? Sono astemio alle porte.\" \"Tutti senza legno.\""
            ],
            [
                "\"What fruit flavors do you have? I am dairy-free.\" \"All without milk.\"",
                "\"What fish flavors do you have? I am vegetable-free.\" \"All without sea.\"",
                "\"What meat flavors do you have? I am potato-free.\" \"All without fire.\"",
                "\"What bread flavors do you have? I am door-free.\" \"All without wood.\""
            ]
        ),
        (
            "\"Posso avere un po' di cioccolato fuso sopra? O quello ha latte?\" \"È puro cioccolato.\"",
            "\"Can I have some melted chocolate on top? Or does that have milk?\" \"It's pure chocolate.\"",
            [
                "\"Posso avere un po' di cioccolato fuso sopra? O quello ha latte?\" \"È puro cioccolato.\"",
                "\"Posso avere un po' di sale grosso sopra? O quello ha pepe?\" \"È puro sale.\"",
                "\"Posso avere un po' di acqua calda sopra? O quello ha vino?\" \"È pura acqua.\"",
                "\"Posso avere un po' di burro giallo sopra? O quello ha olio?\" \"È puro burro.\""
            ],
            [
                "\"Can I have some melted chocolate on top? Or does that have milk?\" \"It's pure chocolate.\"",
                "\"Can I have some coarse salt on top? Or does that have pepper?\" \"It's pure salt.\"",
                "\"Can I have some hot water on top? Or does that have wine?\" \"It's pure water.\"",
                "\"Can I have some yellow butter on top? Or does that have oil?\" \"It's pure butter.\""
            ]
        ),
        (
            "\"Il pistacchio di Bronte ha latte?\" \"Sì, il pistacchio è con latte.\"",
            "\"Does the Bronte pistachio have milk?\" \"Yes, the pistachio is with milk.\"",
            [
                "\"Il pistacchio di Bronte ha latte?\" \"Sì, il pistacchio è con latte.\"",
                "\"Il sole di Roma ha pioggia?\" \"Sì, il sole è con pioggia.\"",
                "\"Il muro di casa ha porte?\" \"Sì, il muro è con porte.\"",
                "\"Il tavolo di legno ha sedie?\" \"Sì, il tavolo è con sedie.\""
            ],
            [
                "\"Does the Bronte pistachio have milk?\" \"Yes, the pistachio is with milk.\"",
                "\"Does the Rome sun have rain?\" \"Yes, the sun is with rain.\"",
                "\"Does the house wall have doors?\" \"Yes, the wall is with doors.\"",
                "\"Does the wood table have chairs?\" \"Yes, the table is with chairs.\""
            ]
        ),
        (
            "\"Il gusto del mese cambia ogni mese.\" \"Questo mese è cassata siciliana.\"",
            "\"The flavor of the month changes every month.\" \"This month it's Sicilian cassata.\"",
            [
                "\"Il gusto del mese cambia ogni mese.\" \"Questo mese è cassata siciliana.\"",
                "\"Il vento del mare cambia ogni ora.\" \"Questo mare è acqua dolce.\"",
                "\"Il libro del sole cambia ogni anno.\" \"Questo sole è fuoco freddo.\"",
                "\"Il cielo del tavolo cambia ogni giorno.\" \"Questo cielo è nuvola rossa.\""
            ],
            [
                "\"The flavor of the month changes every month.\" \"This month it's Sicilian cassata.\"",
                "\"The sea wind changes every hour.\" \"This sea is sweet water.\"",
                "\"The sun book changes every year.\" \"This sun is cold fire.\"",
                "\"The table sky changes every day.\" \"This sky is red cloud.\""
            ]
        ),
        (
            "\"Buono, ma troppo dolce per me.\" \"Allora prendo un cono medio con cioccolato.\"",
            "\"Good, but too sweet for me.\" \"Then I'll take a medium cone with chocolate.\"",
            [
                "\"Buono, ma troppo dolce per me.\" \"Allora prendo un cono medio con cioccolato.\"",
                "\"Bello, ma troppo scuro per me.\" \"Allora prendo un muro grande con finestra.\"",
                "\"Freddo, ma troppo caldo per me.\" \"Allora prendo un letto piccolo con coperta.\"",
                "\"Veloce, ma troppo lento per me.\" \"Allora prendo un treno rosso con ruote.\""
            ],
            [
                "\"Good, but too sweet for me.\" \"Then I'll take a medium cone with chocolate.\"",
                "\"Beautiful, but too dark for me.\" \"Then I'll take a big wall with a window.\"",
                "\"Cold, but too hot for me.\" \"Then I'll take a small bed with a blanket.\"",
                "\"Fast, but too slow for me.\" \"Then I'll take a red train with wheels.\""
            ]
        ),
        (
            "\"È possibile avere tre gusti in questo cono?\" \"Medio può avere fino a tre gusti.\"",
            "\"Is it possible to have three flavors in this cone?\" \"Medium can have up to three flavors.\"",
            [
                "\"È possibile avere tre gusti in questo cono?\" \"Medio può avere fino a tre gusti.\"",
                "\"È possibile avere tre porte in questo muro?\" \"Lungo può avere fino a tre porte.\"",
                "\"È possibile avere tre sedie in questo tavolo?\" \"Largo può avere fino a tre sedie.\"",
                "\"È possibile avere tre ruote in questa auto?\" \"Veloce può avere fino a tre ruote.\""
            ],
            [
                "\"Is it possible to have three flavors in this cone?\" \"Medium can have up to three flavors.\"",
                "\"Is it possible to have three doors in this wall?\" \"Long can have up to three doors.\"",
                "\"Is it possible to have three chairs at this table?\" \"Wide can have up to three chairs.\"",
                "\"Is it possible to have three wheels in this car?\" \"Fast can have up to three wheels.\""
            ]
        ),
        (
            "\"Panna montata sopra? Come vuole.\" \"Costa 50 centesimi in più.\"",
            "\"Whipped cream on top? As you wish.\" \"It costs 50 cents more.\"",
            [
                "\"Panna montata sopra? Come vuole.\" \"Costa 50 centesimi in più.\"",
                "\"Sale grosso sopra? Come vuole.\" \"Costa 50 euro in meno.\"",
                "\"Acqua calda sopra? Come vuole.\" \"Costa 50 litri in più.\"",
                "\"Carta verde sopra? Come vuole.\" \"Costa 50 fogli in meno.\""
            ],
            [
                "\"Whipped cream on top? As you wish.\" \"It costs 50 cents more.\"",
                "\"Coarse salt on top? As you wish.\" \"It costs 50 euros less.\"",
                "\"Hot water on top? As you wish.\" \"It costs 50 liters more.\"",
                "\"Green paper on top? As you wish.\" \"It costs 50 pages less.\""
            ]
        ),
        (
            "\"Un gelato veloce! Fa caldissimo.\" \"Qualcosa di fresco. Quali gusti avete alla frutta?\"",
            "\"A quick ice cream! It's very hot.\" \"Something fresh. What fruit flavors do you have?\"",
            [
                "\"Un gelato veloce! Fa caldissimo.\" \"Qualcosa di fresco. Quali gusti avete alla frutta?\"",
                "\"Un caffè lento! Fa freddissimo.\" \"Qualcosa di caldo. Quali gusti avete alla carne?\"",
                "\"Un tavolo largo! Fa comodissimo.\" \"Qualcosa di duro. Quali gusti avete al legno?\"",
                "\"Un treno rosso! Fa lentissimo.\" \"Qualcosa di blu. Quali gusti avete al mare?\""
            ],
            [
                "\"A quick ice cream! It's very hot.\" \"Something fresh. What fruit flavors do you have?\"",
                "\"A slow coffee! It's very cold.\" \"Something hot. What meat flavors do you have?\"",
                "\"A wide table! It's very comfortable.\" \"Something hard. What wood flavors do you have?\"",
                "\"A red train! It's very slow.\" \"Something blue. What sea flavors do you have?\""
            ]
        ),
        (
            "\"Prendo limone e anguria. In coppetta grande.\" \"Quanti gusti posso mettere?\"",
            "\"I'll take lemon and watermelon. In a large cup.\" \"How many flavors can I put?\"",
            [
                "\"Prendo limone e anguria. In coppetta grande.\" \"Quanti gusti posso mettere?\"",
                "\"Prendo sale e pepe. In borsa piccola.\" \"Quante chiavi posso chiudere?\"",
                "\"Prendo pane e acqua. In bottiglia verde.\" \"Quante sedie posso aprire?\"",
                "\"Prendo sole e vento. In mare blu.\" \"Quanti pesci posso pesare?\""
            ],
            [
                "\"I'll take lemon and watermelon. In a large cup.\" \"How many flavors can I put?\"",
                "\"I'll take salt and pepper. In a small bag.\" \"How many keys can I close?\"",
                "\"I'll take bread and water. In a green bottle.\" \"How many chairs can I open?\"",
                "\"I'll take sun and wind. In a blue sea.\" \"How many fish can I weigh?\""
            ]
        ),
        (
            "\"Coppetta grande anche quattro gusti.\" \"Ma due vanno bene.\"",
            "\"Large cup even four flavors.\" \"But two are fine.\"",
            [
                "\"Coppetta grande anche quattro gusti.\" \"Ma due vanno bene.\"",
                "\"Tavolo grande anche quattro porte.\" \"Ma due vanno lenti.\"",
                "\"Auto grande anche quattro cieli.\" \"Ma due vanno rossi.\"",
                "\"Muro grande anche quattro acque.\" \"Ma due vanno dolci.\""
            ],
            [
                "\"Large cup even four flavors.\" \"But two are fine.\"",
                "\"Large table even four doors.\" \"But two are slow.\"",
                "\"Large car even four skies.\" \"But two are red.\"",
                "\"Large wall even four waters.\" \"But two are sweet.\""
            ]
        ),
        (
            "\"Metta un po' di menta sopra? Avete menta?\" \"Abbiamo lo sciroppo alla menta.\"",
            "\"Put a little mint on top? Do you have mint?\" \"We have mint syrup.\"",
            [
                "\"Metta un po' di menta sopra? Avete menta?\" \"Abbiamo lo sciroppo alla menta.\"",
                "\"Metta un po' di sale sopra? Avete sale?\" \"Abbiamo lo zucchero al mare.\"",
                "\"Metta un po' di pepe sopra? Avete pepe?\" \"Abbiamo lo sciroppo alla porta.\"",
                "\"Metta un po' di carta sopra? Avete carta?\" \"Abbiamo lo zucchero al tavolo.\""
            ],
            [
                "\"Put a little mint on top? Do you have mint?\" \"We have mint syrup.\"",
                "\"Put a little salt on top? Do you have salt?\" \"We have sugar at the sea.\"",
                "\"Put a little pepper on top? Do you have pepper?\" \"We have syrup at the door.\"",
                "\"Put a little paper on top? Do you have paper?\" \"We have sugar at the table.\""
            ]
        ),
        (
            "\"Ne metto un filo?\" \"Sì, perfetto. Così è ancora più fresco.\"",
            "\"Should I put a drizzle?\" \"Yes, perfect. That way it's even fresher.\"",
            [
                "\"Ne metto un filo?\" \"Sì, perfetto. Così è ancora più fresco.\"",
                "\"Ne chiudo un filo?\" \"Sì, perfetto. Così è ancora più rosso.\"",
                "\"Ne mangio un filo?\" \"Sì, perfetto. Così è ancora più stanco.\"",
                "\"Ne dormo un filo?\" \"Sì, perfetto. Così è ancora più veloce.\""
            ],
            [
                "\"Should I put a drizzle?\" \"Yes, perfect. That way it's even fresher.\"",
                "\"Should I close a drizzle?\" \"Yes, perfect. That way it's even redder.\"",
                "\"Should I eat a drizzle?\" \"Yes, perfect. That way it's even more tired.\"",
                "\"Should I sleep a drizzle?\" \"Yes, perfect. That way it's even faster.\""
            ]
        ),
        (
            "\"Mi dà un tovagliolo? Sto sudando.\" \"Ecco. Buona pedalata!\"",
            "\"Can you give me a napkin? I'm sweating.\" \"Here. Have a good ride!\"",
            [
                "\"Mi dà un tovagliolo? Sto sudando.\" \"Ecco. Buona pedalata!\"",
                "\"Mi dà un martello? Sto cantando.\" \"Ecco. Buona nuotata!\"",
                "\"Mi dà un cuscino? Sto correndo.\" \"Ecco. Buona dormita!\"",
                "\"Mi dà un coltello? Sto ridendo.\" \"Ecco. Buona passeggiata!\""
            ],
            [
                "\"Can you give me a napkin? I'm sweating.\" \"Here. Have a good ride!\"",
                "\"Can you give me a hammer? I'm singing.\" \"Here. Have a good swim!\"",
                "\"Can you give me a pillow? I'm running.\" \"Here. Have a good sleep!\"",
                "\"Can you give me a knife? I'm laughing.\" \"Here. Have a good walk!\""
            ]
        ),
        (
            "\"Io vorrei un cono piccolo, due gusti: cioccolato e pistacchio.\" \"Tu?\"",
            "\"I would like a small cone, two flavors: chocolate and pistachio.\" \"You?\"",
            [
                "\"Io vorrei un cono piccolo, due gusti: cioccolato e pistacchio.\" \"Tu?\"",
                "\"Io vorrei un muro grande, due porte: legno e ferro.\" \"Tu?\"",
                "\"Io vorrei un treno veloce, due posti: sedia e letto.\" \"Tu?\"",
                "\"Io vorrei un mare calmo, due pesci: sale e pepe.\" \"Tu?\""
            ],
            [
                "\"I would like a small cone, two flavors: chocolate and pistachio.\" \"You?\"",
                "\"I would like a big wall, two doors: wood and iron.\" \"You?\"",
                "\"I would like a fast train, two seats: chair and bed.\" \"You?\"",
                "\"I would like a calm sea, two fish: salt and pepper.\" \"You?\""
            ]
        ),
        (
            "\"Credevo di aver preso solo cioccolato e pistacchio.\" \"Io volevo anche fragola.\"",
            "\"I thought I only got chocolate and pistachio.\" \"I wanted strawberry too.\"",
            [
                "\"Credevo di aver preso solo cioccolato e pistacchio.\" \"Io volevo anche fragola.\"",
                "\"Credevo di aver dormito solo muro e porta.\" \"Io volevo anche finestra.\"",
                "\"Credevo di aver corso solo mare e sole.\" \"Io volevo anche nuvola.\"",
                "\"Credevo di aver cantato solo sedia e tavolo.\" \"Io volevo anche libro.\""
            ],
            [
                "\"I thought I only got chocolate and pistachio.\" \"I wanted strawberry too.\"",
                "\"I thought I only slept wall and door.\" \"I wanted window too.\"",
                "\"I thought I only ran sea and sun.\" \"I wanted cloud too.\"",
                "\"I thought I only sang chair and table.\" \"I wanted book too.\""
            ]
        ),
        (
            "\"No, tu hai detto fragola e limone.\" \"Ti piace?\"",
            "\"No, you said strawberry and lemon.\" \"Do you like it?\"",
            [
                "\"No, tu hai detto fragola e limone.\" \"Ti piace?\"",
                "\"No, tu hai dormito muro e porta.\" \"Ti corre?\"",
                "\"No, tu hai cantato sedia e tavolo.\" \"Ti nuota?\"",
                "\"No, tu hai pianto sole e mare.\" \"Ti vola?\""
            ],
            [
                "\"No, you said strawberry and lemon.\" \"Do you like it?\"",
                "\"No, you slept wall and door.\" \"Does it run you?\"",
                "\"No, you sang chair and table.\" \"Does it swim you?\"",
                "\"No, you cried sun and sea.\" \"Does it fly you?\""
            ]
        ),
        (
            "\"Sì, ma sento il cioccolato... Ah no, è mio.\" \"Scusa, confusione.\"",
            "\"Yes, but I taste chocolate... Oh no, it's mine.\" \"Sorry, confusion.\"",
            [
                "\"Sì, ma sento il cioccolato... Ah no, è mio.\" \"Scusa, confusione.\"",
                "\"Sì, ma guardo la sedia... Ah no, è tua.\" \"Scusa, attenzione.\"",
                "\"Sì, ma ascolto la porta... Ah no, è nostra.\" \"Scusa, stazione.\"",
                "\"Sì, ma tocco la finestra... Ah no, è loro.\" \"Scusa, porzione.\""
            ],
            [
                "\"Yes, but I taste chocolate... Oh no, it's mine.\" \"Sorry, confusion.\"",
                "\"Yes, but I look at the chair... Oh no, it's yours.\" \"Sorry, attention.\"",
                "\"Yes, but I listen to the door... Oh no, it's ours.\" \"Sorry, station.\"",
                "\"Yes, but I touch the window... Oh no, it's theirs.\" \"Sorry, portion.\""
            ]
        ),
        (
            "\"Sì, mangiamoli prima che si sciolgano.\" \"Ciao!\"",
            "\"Yes, let's eat them before they melt.\" \"Bye!\"",
            [
                "\"Sì, mangiamoli prima che si sciolgano.\" \"Ciao!\"",
                "\"Sì, dormiamoli prima che si rompano.\" \"Ciao!\"",
                "\"Sì, leggiamoli prima che si lavino.\" \"Ciao!\"",
                "\"Sì, corriamoli prima che si chiudano.\" \"Ciao!\""
            ],
            [
                "\"Yes, let's eat them before they melt.\" \"Bye!\"",
                "\"Yes, let's sleep them before they break.\" \"Bye!\"",
                "\"Yes, let's read them before they wash.\" \"Bye!\"",
                "\"Yes, let's run them before they close.\" \"Bye!\""
            ]
        ),
        (
            "\"Questo mese è cassata siciliana, con ricotta e canditi.\" \"Molto buono.\"",
            "\"This month is Sicilian cassata, with ricotta and candied fruit.\" \"Very good.\"",
            [
                "\"Questo mese è cassata siciliana, con ricotta e canditi.\" \"Molto buono.\"",
                "\"Questo muro è cassata siciliana, con mattoni e cemento.\" \"Molto veloce.\"",
                "\"Questo treno è cassata siciliana, con ruote e ferro.\" \"Molto caldo.\"",
                "\"Questo cielo è cassata siciliana, con nuvole e pioggia.\" \"Molto stanco.\""
            ],
            [
                "\"This month is Sicilian cassata, with ricotta and candied fruit.\" \"Very good.\"",
                "\"This wall is Sicilian cassata, with bricks and cement.\" \"Very fast.\"",
                "\"This train is Sicilian cassata, with wheels and iron.\" \"Very warm.\"",
                "\"This sky is Sicilian cassata, with clouds and rain.\" \"Very tired.\""
            ]
        )
    ], start=21)
]

data.extend(new_sentences)

with open(scenario_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated gelato_shop sentences", len(data))
