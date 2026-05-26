import json

scenario_path = 'src/data/exports/dining/food_allergies/dining_food_allergies_sentences.json'
with open(scenario_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_sentences = [
    {
        "id": f"s31-s{i}",
        "italian": italian,
        "english": english,
        "type": "sentence",
        "choicesItalian": choices_it,
        "choicesEnglish": choices_en,
        "correctAnswerItalian": italian,
        "correctAnswerEnglish": english,
        "feedback": {
            "correctItalian": "Esatto! Ottima comprensione del dialogo.",
            "incorrectItalian": "Fai attenzione al contesto dell'allergia e alle alternative proposte.",
            "correctEnglish": "Exactly! Great understanding of the dialogue.",
            "incorrectEnglish": "Pay attention to the allergy context and the proposed alternatives."
        }
    } for i, (italian, english, choices_it, choices_en) in enumerate([
        (
            "\"Mi assicura che non ci sia nemmeno tracce?\" \"Non posso garantire al 100%.\"",
            "\"Can you assure me there are not even traces?\" \"I can't guarantee 100%.\"",
            [
                "\"Mi assicura che non ci sia nemmeno tracce?\" \"Non posso garantire al 100%.\"",
                "\"Mi assicura che non ci sia nessun problema?\" \"Non posso dormire al 100%.\"",
                "\"Mi assicura che non ci sia il conto?\" \"Non posso pagare al 100%.\"",
                "\"Mi assicura che non ci sia il tavolo?\" \"Non posso mangiare al 100%.\""
            ],
            [
                "\"Can you assure me there are not even traces?\" \"I can't guarantee 100%.\"",
                "\"Can you assure me there is no problem?\" \"I can't sleep 100%.\"",
                "\"Can you assure me there is no bill?\" \"I can't pay 100%.\"",
                "\"Can you assure me there is no table?\" \"I can't eat 100%.\""
            ]
        ),
        (
            "\"Allora meglio evitare. Prendo un'insalata.\" \"Sì, l'insalata mista ha solo verdure.\"",
            "\"Then better to avoid. I'll take a salad.\" \"Yes, the mixed salad has only vegetables.\"",
            [
                "\"Allora meglio evitare. Prendo un'insalata.\" \"Sì, l'insalata mista ha solo verdure.\"",
                "\"Allora meglio correre. Prendo una mela.\" \"Sì, la mela mista ha solo frutta.\"",
                "\"Allora meglio dormire. Prendo un letto.\" \"Sì, il letto misto ha solo cuscini.\"",
                "\"Allora meglio guidare. Prendo un'auto.\" \"Sì, l'auto mista ha solo ruote.\""
            ],
            [
                "\"Then better to avoid. I'll take a salad.\" \"Yes, the mixed salad has only vegetables.\"",
                "\"Then better to run. I'll take an apple.\" \"Yes, the mixed apple has only fruit.\"",
                "\"Then better to sleep. I'll take a bed.\" \"Yes, the mixed bed has only pillows.\"",
                "\"Then better to drive. I'll take a car.\" \"Yes, the mixed car has only wheels.\""
            ]
        ),
        (
            "\"Posso farla preparare con attrezzi puliti.\" \"Perfetto, grazie.\"",
            "\"I can have it prepared with clean tools.\" \"Perfect, thank you.\"",
            [
                "\"Posso farla preparare con attrezzi puliti.\" \"Perfetto, grazie.\"",
                "\"Posso farla mangiare con mani pulite.\" \"Perfetto, grazie.\"",
                "\"Posso farla comprare con soldi puliti.\" \"Perfetto, grazie.\"",
                "\"Posso farla dormire con lenzuola pulite.\" \"Perfetto, grazie.\""
            ],
            [
                "\"I can have it prepared with clean tools.\" \"Perfect, thank you.\"",
                "\"I can have it eaten with clean hands.\" \"Perfect, thank you.\"",
                "\"I can have it bought with clean money.\" \"Perfect, thank you.\"",
                "\"I can have it slept with clean sheets.\" \"Perfect, thank you.\""
            ]
        ),
        (
            "\"La cotoletta ha uova nella panatura?\" \"Sì, allora no.\"",
            "\"Does the cutlet have eggs in the breading?\" \"Yes, then no.\"",
            [
                "\"La cotoletta ha uova nella panatura?\" \"Sì, allora no.\"",
                "\"La mela ha semi nella buccia?\" \"Sì, allora no.\"",
                "\"La porta ha chiavi nella toppa?\" \"Sì, allora no.\"",
                "\"La sedia ha gambe nel legno?\" \"Sì, allora no.\""
            ],
            [
                "\"Does the cutlet have eggs in the breading?\" \"Yes, then no.\"",
                "\"Does the apple have seeds in the peel?\" \"Yes, then no.\"",
                "\"Does the door have keys in the keyhole?\" \"Yes, then no.\"",
                "\"Does the chair have legs in the wood?\" \"Yes, then no.\""
            ]
        ),
        (
            "\"Posso offrire un petto di pollo ai ferri.\" \"Va bene, prendo quello.\"",
            "\"I can offer a grilled chicken breast.\" \"Okay, I'll take that.\"",
            [
                "\"Posso offrire un petto di pollo ai ferri.\" \"Va bene, prendo quello.\"",
                "\"Posso offrire un bicchiere di vino ai ferri.\" \"Va bene, bevo quello.\"",
                "\"Posso offrire un piatto di pasta ai ferri.\" \"Va bene, mangio quello.\"",
                "\"Posso offrire un tavolo di legno ai ferri.\" \"Va bene, siedo quello.\""
            ],
            [
                "\"I can offer a grilled chicken breast.\" \"Okay, I'll take that.\"",
                "\"I can offer a glass of grilled wine.\" \"Okay, I'll drink that.\"",
                "\"I can offer a plate of grilled pasta.\" \"Okay, I'll eat that.\"",
                "\"I can offer a table of grilled wood.\" \"Okay, I'll sit that.\""
            ]
        ),
        (
            "\"C'è del latte in questo piatto?\" \"La pizza ha mozzarella, quindi sì.\"",
            "\"Is there milk in this dish?\" \"The pizza has mozzarella, so yes.\"",
            [
                "\"C'è del latte in questo piatto?\" \"La pizza ha mozzarella, quindi sì.\"",
                "\"C'è del vino in questo piatto?\" \"La pizza ha pomodoro, quindi sì.\"",
                "\"C'è del pane in questo piatto?\" \"La pizza ha farina, quindi sì.\"",
                "\"C'è dell'acqua in questo piatto?\" \"La pizza ha sale, quindi sì.\""
            ],
            [
                "\"Is there milk in this dish?\" \"The pizza has mozzarella, so yes.\"",
                "\"Is there wine in this dish?\" \"The pizza has tomato, so yes.\"",
                "\"Is there bread in this dish?\" \"The pizza has flour, so yes.\"",
                "\"Is there water in this dish?\" \"The pizza has salt, so yes.\""
            ]
        ),
        (
            "\"Possiamo prepararla senza formaggio. Vuole?\" \"Sì, grazie.\"",
            "\"We can prepare it without cheese. Do you want it?\" \"Yes, thank you.\"",
            [
                "\"Possiamo prepararla senza formaggio. Vuole?\" \"Sì, grazie.\"",
                "\"Possiamo mangiarla senza formaggio. Vuole?\" \"Sì, grazie.\"",
                "\"Possiamo comprarla senza formaggio. Vuole?\" \"Sì, grazie.\"",
                "\"Possiamo vederla senza formaggio. Vuole?\" \"Sì, grazie.\""
            ],
            [
                "\"We can prepare it without cheese. Do you want it?\" \"Yes, thank you.\"",
                "\"We can eat it without cheese. Do you want it?\" \"Yes, thank you.\"",
                "\"We can buy it without cheese. Do you want it?\" \"Yes, thank you.\"",
                "\"We can see it without cheese. Do you want it?\" \"Yes, thank you.\""
            ]
        ),
        (
            "\"L'impasto ha latte?\" \"No, solo acqua, farina, lievito e sale.\"",
            "\"Does the dough have milk?\" \"No, only water, flour, yeast and salt.\"",
            [
                "\"L'impasto ha latte?\" \"No, solo acqua, farina, lievito e sale.\"",
                "\"Il muro ha latte?\" \"No, solo mattoni, cemento, pittura e sole.\"",
                "\"Il tetto ha latte?\" \"No, solo legno, tegole, pioggia e vento.\"",
                "\"Il pavimento ha latte?\" \"No, solo piastrelle, colla, acqua e sapone.\""
            ],
            [
                "\"Does the dough have milk?\" \"No, only water, flour, yeast and salt.\"",
                "\"Does the wall have milk?\" \"No, only bricks, cement, paint and sun.\"",
                "\"Does the roof have milk?\" \"No, only wood, tiles, rain and wind.\"",
                "\"Does the floor have milk?\" \"No, only tiles, glue, water and soap.\""
            ]
        ),
        (
            "\"Le verdure sono grigliate sulla stessa piastra?\" \"Sì, ma la puliamo.\"",
            "\"Are the vegetables grilled on the same griddle?\" \"Yes, but we clean it.\"",
            [
                "\"Le verdure sono grigliate sulla stessa piastra?\" \"Sì, ma la puliamo.\"",
                "\"Le mele sono mangiate sulla stessa sedia?\" \"Sì, ma la rompiamo.\"",
                "\"Le scarpe sono lavate sulla stessa barca?\" \"Sì, ma la vendiamo.\"",
                "\"Le borse sono perse sulla stessa strada?\" \"Sì, ma la troviamo.\""
            ],
            [
                "\"Are the vegetables grilled on the same griddle?\" \"Yes, but we clean it.\"",
                "\"Are the apples eaten on the same chair?\" \"Yes, but we break it.\"",
                "\"Are the shoes washed on the same boat?\" \"Yes, but we sell it.\"",
                "\"Are the bags lost on the same street?\" \"Yes, but we find it.\""
            ]
        ),
        (
            "\"Le assicuro che stiamo attenti.\" \"Va bene, mi fido.\"",
            "\"I assure you we are careful.\" \"Okay, I trust you.\"",
            [
                "\"Le assicuro che stiamo attenti.\" \"Va bene, mi fido.\"",
                "\"Le assicuro che siamo pigri.\" \"Va bene, dormo.\"",
                "\"Le assicuro che siamo tristi.\" \"Va bene, piango.\"",
                "\"Le assicuro che siamo ricchi.\" \"Va bene, pago.\""
            ],
            [
                "\"I assure you we are careful.\" \"Okay, I trust you.\"",
                "\"I assure you we are lazy.\" \"Okay, I sleep.\"",
                "\"I assure you we are sad.\" \"Okay, I cry.\"",
                "\"I assure you we are rich.\" \"Okay, I pay.\""
            ]
        ),
        (
            "\"E senza glutine? No, non sono celiaco.\" \"Ok, allora pizza normale.\"",
            "\"And gluten free? No, I'm not celiac.\" \"Ok, then normal pizza.\"",
            [
                "\"E senza glutine? No, non sono celiaco.\" \"Ok, allora pizza normale.\"",
                "\"E senza latte? No, non sono stanco.\" \"Ok, allora acqua normale.\"",
                "\"E senza uova? No, non sono felice.\" \"Ok, allora carne normale.\"",
                "\"E senza sale? No, non sono arrabbiato.\" \"Ok, allora pesce normale.\""
            ],
            [
                "\"And gluten free? No, I'm not celiac.\" \"Ok, then normal pizza.\"",
                "\"And milk free? No, I'm not tired.\" \"Ok, then normal water.\"",
                "\"And egg free? No, I'm not happy.\" \"Ok, then normal meat.\"",
                "\"And salt free? No, I'm not angry.\" \"Ok, then normal fish.\""
            ]
        ),
        (
            "\"Una brioche, per favore. È senza uova?\" \"Le tradizionali hanno uova.\"",
            "\"A brioche, please. Is it egg-free?\" \"The traditional ones have eggs.\"",
            [
                "\"Una brioche, per favore. È senza uova?\" \"Le tradizionali hanno uova.\"",
                "\"Una torta, per favore. È senza sale?\" \"Le tradizionali hanno sale.\"",
                "\"Una mela, per favore. È senza semi?\" \"Le tradizionali hanno semi.\"",
                "\"Una pera, per favore. È senza buccia?\" \"Le tradizionali hanno buccia.\""
            ],
            [
                "\"A brioche, please. Is it egg-free?\" \"The traditional ones have eggs.\"",
                "\"A cake, please. Is it salt-free?\" \"The traditional ones have salt.\"",
                "\"An apple, please. Is it seed-free?\" \"The traditional ones have seeds.\"",
                "\"A pear, please. Is it peel-free?\" \"The traditional ones have peel.\""
            ]
        ),
        (
            "\"Abbiamo dei biscotti fatti in casa senza uova.\" \"Quali sono gli ingredienti?\"",
            "\"We have homemade cookies without eggs.\" \"What are the ingredients?\"",
            [
                "\"Abbiamo dei biscotti fatti in casa senza uova.\" \"Quali sono gli ingredienti?\"",
                "\"Abbiamo dei libri fatti in casa senza pagine.\" \"Quali sono le parole?\"",
                "\"Abbiamo dei mobili fatti in casa senza legno.\" \"Quali sono i pezzi?\"",
                "\"Abbiamo dei vestiti fatti in casa senza stoffa.\" \"Quali sono i fili?\""
            ],
            [
                "\"We have homemade cookies without eggs.\" \"What are the ingredients?\"",
                "\"We have homemade books without pages.\" \"What are the words?\"",
                "\"We have homemade furniture without wood.\" \"What are the pieces?\"",
                "\"We have homemade clothes without fabric.\" \"What are the threads?\""
            ]
        ),
        (
            "\"È allergico anche al latte?\" \"No, solo uova.\"",
            "\"Are you also allergic to milk?\" \"No, only eggs.\"",
            [
                "\"È allergico anche al latte?\" \"No, solo uova.\"",
                "\"È stanco anche di correre?\" \"No, solo camminare.\"",
                "\"È felice anche di dormire?\" \"No, solo sognare.\"",
                "\"È triste anche di mangiare?\" \"No, solo bere.\""
            ],
            [
                "\"Are you also allergic to milk?\" \"No, only eggs.\"",
                "\"Are you also tired of running?\" \"No, only walking.\"",
                "\"Are you also happy to sleep?\" \"No, only dreaming.\"",
                "\"Are you also sad to eat?\" \"No, only drinking.\""
            ]
        ),
        (
            "\"Cerco un'alternativa sicura per mio figlio.\" \"Capisco, è delicata.\"",
            "\"I'm looking for a safe alternative for my son.\" \"I understand, it's delicate.\"",
            [
                "\"Cerco un'alternativa sicura per mio figlio.\" \"Capisco, è delicata.\"",
                "\"Cerco un treno sicuro per mio amico.\" \"Capisco, è veloce.\"",
                "\"Cerco un libro sicuro per mio nonno.\" \"Capisco, è pesante.\"",
                "\"Cerco un cappello sicuro per mio zio.\" \"Capisco, è caldo.\""
            ],
            [
                "\"I'm looking for a safe alternative for my son.\" \"I understand, it's delicate.\"",
                "\"I'm looking for a safe train for my friend.\" \"I understand, it's fast.\"",
                "\"I'm looking for a safe book for my grandfather.\" \"I understand, it's heavy.\"",
                "\"I'm looking for a safe hat for my uncle.\" \"I understand, it's warm.\""
            ]
        ),
        (
            "\"Le consiglio il risotto allo zafferano.\" \"Nessun latticino, uova, o arachidi.\"",
            "\"I recommend the saffron risotto.\" \"No dairy, eggs, or peanuts.\"",
            [
                "\"Le consiglio il risotto allo zafferano.\" \"Nessun latticino, uova, o arachidi.\"",
                "\"Le consiglio il gelato al limone.\" \"Nessun sale, pepe, o aceto.\"",
                "\"Le consiglio il caffè al bar.\" \"Nessun tavolo, sedia, o porta.\"",
                "\"Le consiglio il vino in bottiglia.\" \"Nessun bicchiere, tazza, o vaso.\""
            ],
            [
                "\"I recommend the saffron risotto.\" \"No dairy, eggs, or peanuts.\"",
                "\"I recommend the lemon ice cream.\" \"No salt, pepper, or vinegar.\"",
                "\"I recommend the coffee at the bar.\" \"No table, chair, or door.\"",
                "\"I recommend the wine in a bottle.\" \"No glass, cup, or vase.\""
            ]
        ),
        (
            "\"Il brodo potrebbe contenere tracce di glutine?\" \"No, brodo vegetale.\"",
            "\"Could the broth contain traces of gluten?\" \"No, vegetable broth.\"",
            [
                "\"Il brodo potrebbe contenere tracce di glutine?\" \"No, brodo vegetale.\"",
                "\"Il mare potrebbe contenere tracce di sale?\" \"No, mare dolce.\"",
                "\"Il cielo potrebbe contenere tracce di nuvole?\" \"No, cielo sereno.\"",
                "\"Il bosco potrebbe contenere tracce di alberi?\" \"No, bosco vuoto.\""
            ],
            [
                "\"Could the broth contain traces of gluten?\" \"No, vegetable broth.\"",
                "\"Could the sea contain traces of salt?\" \"No, sweet sea.\"",
                "\"Could the sky contain traces of clouds?\" \"No, clear sky.\"",
                "\"Could the forest contain traces of trees?\" \"No, empty forest.\""
            ]
        ),
        (
            "\"Mi assicura che non ci sia farina nel sugo?\" \"Posso garantirglielo.\"",
            "\"Can you assure me there is no flour in the sauce?\" \"I can guarantee it.\"",
            [
                "\"Mi assicura che non ci sia farina nel sugo?\" \"Posso garantirglielo.\"",
                "\"Mi assicura che non ci sia sabbia nel mare?\" \"Posso nuotare.\"",
                "\"Mi assicura che non ci sia vento nel cielo?\" \"Posso volare.\"",
                "\"Mi assicura che non ci sia freddo nel ghiaccio?\" \"Posso scivolare.\""
            ],
            [
                "\"Can you assure me there is no flour in the sauce?\" \"I can guarantee it.\"",
                "\"Can you assure me there is no sand in the sea?\" \"I can swim.\"",
                "\"Can you assure me there is no wind in the sky?\" \"I can fly.\"",
                "\"Can you assure me there is no cold in the ice?\" \"I can slide.\""
            ]
        ),
        (
            "\"Vorrei assaggiare questo stufato. Quali sono gli ingredienti?\" \"Carne, patate e spezie.\"",
            "\"I would like to taste this stew. What are the ingredients?\" \"Meat, potatoes and spices.\"",
            [
                "\"Vorrei assaggiare questo stufato. Quali sono gli ingredienti?\" \"Carne, patate e spezie.\"",
                "\"Vorrei guardare questa foto. Quali sono i colori?\" \"Rosso, blu e verde.\"",
                "\"Vorrei ascoltare questa canzone. Quali sono le note?\" \"Do, re e mi.\"",
                "\"Vorrei leggere questo libro. Quali sono le pagine?\" \"Cento, mille e due.\""
            ],
            [
                "\"I would like to taste this stew. What are the ingredients?\" \"Meat, potatoes and spices.\"",
                "\"I would like to look at this photo. What are the colors?\" \"Red, blue and green.\"",
                "\"I would like to listen to this song. What are the notes?\" \"Do, re and mi.\"",
                "\"I would like to read this book. What are the pages?\" \"One hundred, one thousand and two.\""
            ]
        ),
        (
            "\"Usiamo pasta di arachidi per addensare.\" \"Oddio, allora no!\"",
            "\"We use peanut paste to thicken.\" \"Oh god, then no!\"",
            [
                "\"Usiamo pasta di arachidi per addensare.\" \"Oddio, allora no!\"",
                "\"Usiamo vernice di muro per dipingere.\" \"Oddio, allora sì!\"",
                "\"Usiamo acqua di mare per lavare.\" \"Oddio, allora forse!\"",
                "\"Usiamo luce di sole per scaldare.\" \"Oddio, allora mai!\""
            ],
            [
                "\"We use peanut paste to thicken.\" \"Oh god, then no!\"",
                "\"We use wall paint to paint.\" \"Oh god, then yes!\"",
                "\"We use sea water to wash.\" \"Oh god, then maybe!\"",
                "\"We use sun light to warm.\" \"Oh god, then never!\""
            ]
        ),
        (
            "\"Cosa potrei mangiare di sicuro?\" \"Il pollo è senza arachidi.\"",
            "\"What could I eat safely?\" \"The chicken is peanut-free.\"",
            [
                "\"Cosa potrei mangiare di sicuro?\" \"Il pollo è senza arachidi.\"",
                "\"Cosa potrei guardare di sicuro?\" \"Il film è senza pubblicità.\"",
                "\"Cosa potrei leggere di sicuro?\" \"Il libro è senza figure.\"",
                "\"Cosa potrei ascoltare di sicuro?\" \"Il disco è senza rumori.\""
            ],
            [
                "\"What could I eat safely?\" \"The chicken is peanut-free.\"",
                "\"What could I watch safely?\" \"The movie is ad-free.\"",
                "\"What could I read safely?\" \"The book is picture-free.\"",
                "\"What could I listen to safely?\" \"The record is noise-free.\""
            ]
        ),
        (
            "\"Ma mi assicura che non ci sia farina?\" \"No, farina zero.\"",
            "\"But can you assure me there is no flour?\" \"No, zero flour.\"",
            [
                "\"Ma mi assicura che non ci sia farina?\" \"No, farina zero.\"",
                "\"Ma mi assicura che non ci sia buio?\" \"No, buio totale.\"",
                "\"Ma mi assicura che non ci sia vento?\" \"No, vento forte.\"",
                "\"Ma mi assicura che non ci sia freddo?\" \"No, freddo gelido.\""
            ],
            [
                "\"But can you assure me there is no flour?\" \"No, zero flour.\"",
                "\"But can you assure me there is no dark?\" \"No, total dark.\"",
                "\"But can you assure me there is no wind?\" \"No, strong wind.\"",
                "\"But can you assure me there is no cold?\" \"No, freezing cold.\""
            ]
        ),
        (
            "\"Cosa posso mangiare? Quasi tutto contiene uova.\" \"Abbiamo pane integrale e marmellata.\"",
            "\"What can I eat? Almost everything contains eggs.\" \"We have whole wheat bread and jam.\"",
            [
                "\"Cosa posso mangiare? Quasi tutto contiene uova.\" \"Abbiamo pane integrale e marmellata.\"",
                "\"Cosa posso bere? Quasi tutto contiene latte.\" \"Abbiamo acqua minerale e succo.\"",
                "\"Cosa posso comprare? Quasi tutto costa troppo.\" \"Abbiamo sconti speciali e saldi.\"",
                "\"Cosa posso leggere? Quasi tutto annoia molto.\" \"Abbiamo fumetti allegri e libri.\""
            ],
            [
                "\"What can I eat? Almost everything contains eggs.\" \"We have whole wheat bread and jam.\"",
                "\"What can I drink? Almost everything contains milk.\" \"We have mineral water and juice.\"",
                "\"What can I buy? Almost everything costs too much.\" \"We have special discounts and sales.\"",
                "\"What can I read? Almost everything is very boring.\" \"We have cheerful comics and books.\""
            ]
        ),
        (
            "\"Le uova strapazzate sono a parte, può prenderle?\" \"No, sono allergico.\"",
            "\"Scrambled eggs are separate, can you take them?\" \"No, I'm allergic.\"",
            [
                "\"Le uova strapazzate sono a parte, può prenderle?\" \"No, sono allergico.\"",
                "\"Le nuvole grigie sono in cielo, può vederle?\" \"No, sono cieco.\"",
                "\"Le canzoni belle sono alla radio, può ascoltarle?\" \"No, sono sordo.\"",
                "\"Le strade lunghe sono in città, può correrle?\" \"No, sono stanco.\""
            ],
            [
                "\"Scrambled eggs are separate, can you take them?\" \"No, I'm allergic.\"",
                "\"The gray clouds are in the sky, can you see them?\" \"No, I'm blind.\"",
                "\"The beautiful songs are on the radio, can you listen to them?\" \"No, I'm deaf.\"",
                "\"The long streets are in the city, can you run them?\" \"No, I'm tired.\""
            ]
        ),
        (
            "\"Abbiamo fette biscottate senza uova. Vuole?\" \"Sì, prendo pane integrale.\"",
            "\"We have rusks without eggs. Do you want some?\" \"Yes, I'll take whole wheat bread.\"",
            [
                "\"Abbiamo fette biscottate senza uova. Vuole?\" \"Sì, prendo pane integrale.\"",
                "\"Abbiamo finestre pulite senza vetri. Vuole?\" \"Sì, prendo porte chiuse.\"",
                "\"Abbiamo scatole grandi senza fondo. Vuole?\" \"Sì, prendo borse piccole.\"",
                "\"Abbiamo scarpe nuove senza suola. Vuole?\" \"Sì, prendo stivali vecchi.\""
            ],
            [
                "\"We have rusks without eggs. Do you want some?\" \"Yes, I'll take whole wheat bread.\"",
                "\"We have clean windows without glass. Do you want some?\" \"Yes, I'll take closed doors.\"",
                "\"We have large boxes without bottom. Do you want some?\" \"Yes, I'll take small bags.\"",
                "\"We have new shoes without sole. Do you want some?\" \"Yes, I'll take old boots.\""
            ]
        ),
        (
            "\"A volte il pane morbido ha latte.\" \"Il nostro è solo farina e acqua.\"",
            "\"Sometimes soft bread has milk.\" \"Ours is only flour and water.\"",
            [
                "\"A volte il pane morbido ha latte.\" \"Il nostro è solo farina e acqua.\"",
                "\"A volte il muro duro ha vernice.\" \"Il nostro è solo mattoni e calce.\"",
                "\"A volte il tetto rosso ha tegole.\" \"Il nostro è solo legno e paglia.\"",
                "\"A volte il prato verde ha fiori.\" \"Il nostro è solo erba e terra.\""
            ],
            [
                "\"Sometimes soft bread has milk.\" \"Ours is only flour and water.\"",
                "\"Sometimes hard wall has paint.\" \"Ours is only bricks and lime.\"",
                "\"Sometimes red roof has tiles.\" \"Ours is only wood and straw.\"",
                "\"Sometimes green lawn has flowers.\" \"Ours is only grass and soil.\""
            ]
        ),
        (
            "\"Posso portarle la lista ingredienti se vuole.\" \"No, mi fido.\"",
            "\"I can bring you the ingredients list if you want.\" \"No, I trust you.\"",
            [
                "\"Posso portarle la lista ingredienti se vuole.\" \"No, mi fido.\"",
                "\"Posso portarle la lista ospiti se vuole.\" \"No, mi annoio.\"",
                "\"Posso portarle la lista spesa se vuole.\" \"No, mi stanco.\"",
                "\"Posso portarle la lista regali se vuole.\" \"No, mi arrendo.\""
            ],
            [
                "\"I can bring you the ingredients list if you want.\" \"No, I trust you.\"",
                "\"I can bring you the guest list if you want.\" \"No, I'm bored.\"",
                "\"I can bring you the shopping list if you want.\" \"No, I'm tired.\"",
                "\"I can bring you the gift list if you want.\" \"No, I give up.\""
            ]
        ),
        (
            "\"E la marmellata? Senza glutine?\" \"No, non importa.\"",
            "\"And the jam? Gluten free?\" \"No, it doesn't matter.\"",
            [
                "\"E la marmellata? Senza glutine?\" \"No, non importa.\"",
                "\"E la finestra? Senza vetri?\" \"No, non chiude.\"",
                "\"E la porta? Senza maniglia?\" \"No, non apre.\"",
                "\"E la sedia? Senza gambe?\" \"No, non regge.\""
            ],
            [
                "\"And the jam? Gluten free?\" \"No, it doesn't matter.\"",
                "\"And the window? Glass free?\" \"No, it doesn't close.\"",
                "\"And the door? Handle free?\" \"No, it doesn't open.\"",
                "\"And the chair? Leg free?\" \"No, it doesn't support.\""
            ]
        ),
        (
            "\"La prego di informare lo chef della mia allergia.\" \"Lo chef è già informato.\"",
            "\"Please inform the chef of my allergy.\" \"The chef is already informed.\"",
            [
                "\"La prego di informare lo chef della mia allergia.\" \"Lo chef è già informato.\"",
                "\"La prego di informare il vigile della mia fretta.\" \"Il vigile è già andato.\"",
                "\"La prego di informare il medico della mia tosse.\" \"Il medico è già stanco.\"",
                "\"La prego di informare il maestro della mia assenza.\" \"Il maestro è già partito.\""
            ],
            [
                "\"Please inform the chef of my allergy.\" \"The chef is already informed.\"",
                "\"Please inform the traffic cop of my hurry.\" \"The traffic cop is already gone.\"",
                "\"Please inform the doctor of my cough.\" \"The doctor is already tired.\"",
                "\"Please inform the teacher of my absence.\" \"The teacher is already left.\""
            ]
        ),
        (
            "\"Sono molto allergico alle uova.\" \"La cotoletta ha uova nella panatura.\"",
            "\"I am very allergic to eggs.\" \"The cutlet has eggs in the breading.\"",
            [
                "\"Sono molto allergico alle uova.\" \"La cotoletta ha uova nella panatura.\"",
                "\"Sono molto attento alle mosche.\" \"La finestra ha mosche sulla tenda.\"",
                "\"Sono molto vicino alle nuvole.\" \"La montagna ha nuvole sulla cima.\"",
                "\"Sono molto lontano dalle città.\" \"La campagna ha città sulle mappe.\""
            ],
            [
                "\"I am very allergic to eggs.\" \"The cutlet has eggs in the breading.\"",
                "\"I am very careful about flies.\" \"The window has flies on the curtain.\"",
                "\"I am very close to the clouds.\" \"The mountain has clouds on the top.\"",
                "\"I am very far from the cities.\" \"The countryside has cities on the maps.\""
            ]
        )
    ], start=21)
]

data.extend(new_sentences)

with open(scenario_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated food_allergies sentences", len(data))
