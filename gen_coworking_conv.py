import json
import os

conversations_data = {
  "scenarioId": 68,
  "conversations": [
    {
      "id": "arrival_and_wifi",
      "title": "Arrivo e Wi-Fi",
      "description": "Arrive at the coworking space and ask for the Wi-Fi password.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Buongiorno e benvenuto nel nostro spazio di coworking. Posso aiutarti?",
          "english": "Good morning and welcome to our coworking space. Can I help you?",
          "choices": [
            {
              "text": "Buongiorno. Sì, ho un abbonamento mensile. Dove posso sedermi?",
              "isCorrect": True,
              "feedback": "Great! You stated your subscription type clearly."
            },
            {
              "text": "Voglio dormire qui stanotte.",
              "isCorrect": False,
              "feedback": "This is a coworking space, not a hotel!"
            },
            {
              "text": "Ho fame, portami una pizza.",
              "isCorrect": False,
              "feedback": "They don't serve food like a restaurant. Be polite!"
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Ottimo. Puoi sederti a qualsiasi scrivania libera nella sala principale.",
          "english": "Excellent. You can sit at any free desk in the main room.",
          "choices": [
            {
              "text": "Grazie. Qual è la password per il Wi-Fi?",
              "isCorrect": True,
              "feedback": "Asking for Wi-Fi is the most important first step!"
            },
            {
              "text": "Voglio una scrivania solo per me, per sempre.",
              "isCorrect": False,
              "feedback": "Dedicated desks usually cost extra. You have a standard pass."
            },
            {
              "text": "Non mi piacciono le scrivanie. Lavoro sul pavimento.",
              "isCorrect": False,
              "feedback": "That's not very comfortable or professional!"
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "La rete è 'Coworking_Guest' e la password è 'Lavoro2024'.",
          "english": "The network is 'Coworking_Guest' and the password is 'Lavoro2024'.",
          "choices": [
            {
              "text": "Perfetto, scrivo subito la password. La connessione è veloce?",
              "isCorrect": True,
              "feedback": "Good question to ensure you can work properly."
            },
            {
              "text": "Non voglio il Wi-Fi. Uso i segnali di fumo.",
              "isCorrect": False,
              "feedback": "That won't work for sending emails!"
            },
            {
              "text": "È una password troppo difficile. Cambiala.",
              "isCorrect": False,
              "feedback": "You can't ask them to change the network password for everyone!"
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Sì, abbiamo la fibra ottica. La connessione è molto rapida.",
          "english": "Yes, we have fiber optic. The connection is very fast.",
          "choices": [
            {
              "text": "Molto bene, devo fare una videochiamata importante oggi.",
              "isCorrect": True,
              "feedback": "A fast connection is essential for video calls."
            },
            {
              "text": "Io scarico tutti i film di internet oggi.",
              "isCorrect": False,
              "feedback": "That might slow down the network for everyone else."
            },
            {
              "text": "Non mi interessa. Non uso internet per lavorare.",
              "isCorrect": False,
              "feedback": "In a coworking space, most people need internet!"
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Per le videochiamate, ti consiglio di usare le cuffie per non disturbare.",
          "english": "For video calls, I recommend using headphones so as not to disturb.",
          "choices": [
            {
              "text": "Certo, ho le mie cuffie nello zaino. Ci sono delle regole per il rumore?",
              "isCorrect": True,
              "feedback": "Asking about noise rules is very considerate."
            },
            {
              "text": "Non uso le cuffie. Tutti devono ascoltare la mia chiamata.",
              "isCorrect": False,
              "feedback": "That's very rude in a shared workspace!"
            },
            {
              "text": "Canto ad alta voce durante la chiamata.",
              "isCorrect": False,
              "feedback": "Definitely not allowed in a coworking space!"
            }
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Sì, chiediamo di parlare a bassa voce nella sala principale.",
          "english": "Yes, we ask to speak softly in the main room.",
          "choices": [
            {
              "text": "Capisco. C'è un posto dove posso parlare ad alta voce se necessario?",
              "isCorrect": True,
              "feedback": "Good question for when you need to make a loud call."
            },
            {
              "text": "Io parlo sempre urlando. È il mio stile.",
              "isCorrect": False,
              "feedback": "You will have to adapt your style here."
            },
            {
              "text": "Allora non parlo mai più nella mia vita.",
              "isCorrect": False,
              "feedback": "That's an overreaction! Just speak softly."
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Certo, abbiamo delle piccole cabine telefoniche vicino al corridoio.",
          "english": "Sure, we have some small phone booths near the corridor.",
          "choices": [
            {
              "text": "Ottima idea. Sono gratuite o devo pagare per usarle?",
              "isCorrect": True,
              "feedback": "Always good to check if there are extra costs."
            },
            {
              "text": "Voglio portare la mia scrivania nella cabina.",
              "isCorrect": False,
              "feedback": "The booths are too small for a full desk."
            },
            {
              "text": "Le cabine sono per Superman, non per me.",
              "isCorrect": False,
              "feedback": "They are for phone calls, not changing into a superhero!"
            }
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Le cabine sono gratuite. Puoi usarle fino a un'ora.",
          "english": "The booths are free. You can use them for up to an hour.",
          "choices": [
            {
              "text": "Perfetto. Un'ultima cosa: dove sono i bagni?",
              "isCorrect": True,
              "feedback": "A very practical and necessary question."
            },
            {
              "text": "Resto nella cabina per dodici ore.",
              "isCorrect": False,
              "feedback": "You can only use them for an hour!"
            },
            {
              "text": "Non vado mai in bagno quando lavoro.",
              "isCorrect": False,
              "feedback": "That's probably not true or healthy!"
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "I bagni sono in fondo al corridoio, a destra.",
          "english": "The bathrooms are down the hall, on the right.",
          "choices": [
            {
              "text": "Grazie mille per tutte le informazioni. Vado a lavorare.",
              "isCorrect": True,
              "feedback": "Polite way to end the orientation."
            },
            {
              "text": "Voglio un bagno privato solo per me.",
              "isCorrect": False,
              "feedback": "Bathrooms are shared in a coworking space."
            },
            {
              "text": "Vado a casa, sono stanco.",
              "isCorrect": False,
              "feedback": "You just arrived to start working!"
            }
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Prego! Se hai bisogno di altro, sono alla reception. Buon lavoro!",
          "english": "You're welcome! If you need anything else, I'm at the reception. Have a good work day!",
          "choices": [
            {
              "text": "Buon lavoro anche a te! A più tardi.",
              "isCorrect": True,
              "feedback": "Perfect response. You are ready to start."
            },
            {
              "text": "Non voglio lavorare oggi.",
              "isCorrect": False,
              "feedback": "Then why are you at the coworking space?"
            },
            {
              "text": "Vieni a lavorare per me, per favore.",
              "isCorrect": False,
              "feedback": "They have their own job at the reception!"
            }
          ]
        }
      ]
    },
    {
      "id": "using_printer",
      "title": "Usare la stampante",
      "description": "Learn how to use the shared printer in the coworking space.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Ciao! Vedo che stai guardando la stampante. Ti serve aiuto?",
          "english": "Hi! I see you are looking at the printer. Do you need help?",
          "choices": [
            {
              "text": "Sì, per favore. Devo stampare alcuni documenti ma non so come fare.",
              "isCorrect": True,
              "feedback": "Asking for help is the right move."
            },
            {
              "text": "No, sto solo ammirando questa bellissima macchina.",
              "isCorrect": False,
              "feedback": "It's just a standard printer!"
            },
            {
              "text": "Voglio distruggere la stampante.",
              "isCorrect": False,
              "feedback": "Please don't break the equipment!"
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Nessun problema. Prima di tutto, devi inviare il documento all'indirizzo email della stampante.",
          "english": "No problem. First of all, you need to send the document to the printer's email address.",
          "choices": [
            {
              "text": "Ah, capisco. Qual è l'indirizzo email della stampante?",
              "isCorrect": True,
              "feedback": "You need the address to send the files."
            },
            {
              "text": "Non uso l'email. Mando un piccione viaggiatore.",
              "isCorrect": False,
              "feedback": "The printer only accepts emails or direct connections!"
            },
            {
              "text": "Mando una lettera per posta alla stampante.",
              "isCorrect": False,
              "feedback": "That will take days!"
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "L'indirizzo è 'stampa@coworking.it'. Invia il file come allegato.",
          "english": "The address is 'stampa@coworking.it'. Send the file as an attachment.",
          "choices": [
            {
              "text": "Fatto! Ho inviato l'email. E adesso cosa devo fare?",
              "isCorrect": True,
              "feedback": "Good follow-up question for the next step."
            },
            {
              "text": "Non voglio allegare il file, lo scrivo nel testo dell'email.",
              "isCorrect": False,
              "feedback": "It's better to send a PDF attachment for formatting."
            },
            {
              "text": "Aspetto qui per tre ore.",
              "isCorrect": False,
              "feedback": "It should be much faster than that!"
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Ora inserisci il tuo codice personale qui sul piccolo schermo della stampante.",
          "english": "Now enter your personal code here on the printer's small screen.",
          "choices": [
            {
              "text": "Il mio codice personale? Dove lo trovo?",
              "isCorrect": True,
              "feedback": "If you don't know your code, asking is necessary."
            },
            {
              "text": "Il mio codice è '1234', lo sanno tutti.",
              "isCorrect": False,
              "feedback": "Don't shout your code out loud!"
            },
            {
              "text": "Non voglio inserire nessun codice, è un segreto.",
              "isCorrect": False,
              "feedback": "You need the code to print your specific documents."
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "È il numero di quattro cifre che hai ricevuto quando hai fatto l'abbonamento.",
          "english": "It's the four-digit number you received when you signed up for the subscription.",
          "choices": [
            {
              "text": "Ah, sì! Controllo sul mio telefono... Trovato. Lo inserisco.",
              "isCorrect": True,
              "feedback": "Checking your phone for the registration info is smart."
            },
            {
              "text": "Ho perso il telefono e la memoria.",
              "isCorrect": False,
              "feedback": "Then you will have to ask the reception to find your code!"
            },
            {
              "text": "Invento un numero a caso e provo.",
              "isCorrect": False,
              "feedback": "That won't work, it needs to match your account."
            }
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Perfetto. Ora vedi il tuo documento sullo schermo? Premi 'Stampa'.",
          "english": "Perfect. Do you see your document on the screen now? Press 'Print'.",
          "choices": [
            {
              "text": "Sì, lo vedo. Premo 'Stampa'. Le stampe sono a pagamento?",
              "isCorrect": True,
              "feedback": "Always check if there are fees for printing."
            },
            {
              "text": "Premo tutti i pulsanti che vedo.",
              "isCorrect": False,
              "feedback": "You might break it or print the wrong things!"
            },
            {
              "text": "Voglio stampare un milione di copie.",
              "isCorrect": False,
              "feedback": "That will definitely cost a lot of money!"
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Hai cinquanta stampe in bianco e nero gratuite ogni mese. Le stampe a colori costano dieci centesimi.",
          "english": "You have fifty free black and white prints every month. Color prints cost ten cents.",
          "choices": [
            {
              "text": "Capito. Questo documento è in bianco e nero, quindi è gratis.",
              "isCorrect": True,
              "feedback": "Correct calculation."
            },
            {
              "text": "Voglio tutto a colori, ma non voglio pagare.",
              "isCorrect": False,
              "feedback": "You have to pay for color!"
            },
            {
              "text": "Dieci centesimi sono troppi, vado in copisteria.",
              "isCorrect": False,
              "feedback": "Ten cents is actually a standard or cheap price."
            }
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Esatto. Ecco i tuoi fogli. Sembra che ci sia poca carta nel cassetto.",
          "english": "Exactly. Here are your papers. It seems there is little paper in the tray.",
          "choices": [
            {
              "text": "Devo aggiungere io la carta o ci pensate voi?",
              "isCorrect": True,
              "feedback": "Good etiquette to ask who is responsible for maintenance."
            },
            {
              "text": "Non è un mio problema, io ho finito.",
              "isCorrect": False,
              "feedback": "A bit selfish in a shared space!"
            },
            {
              "text": "Metto un pezzo di cartone nella stampante.",
              "isCorrect": False,
              "feedback": "That will jam the printer!"
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Di solito la aggiungiamo noi. Vado subito a prendere una risma di carta.",
          "english": "Usually we add it. I'll go get a ream of paper right away.",
          "choices": [
            {
              "text": "Va bene, grazie. Sei stato molto gentile.",
              "isCorrect": True,
              "feedback": "Polite expression of gratitude."
            },
            {
              "text": "Fai in fretta, il prossimo deve stampare.",
              "isCorrect": False,
              "feedback": "Don't give orders to the staff!"
            },
            {
              "text": "Non voglio che tu metta la carta.",
              "isCorrect": False,
              "feedback": "But the printer needs it!"
            }
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Di nulla! Ricorda che per usare lo scanner il procedimento è simile. Buona giornata!",
          "english": "Not at all! Remember that to use the scanner the process is similar. Have a good day!",
          "choices": [
            {
              "text": "Buono a sapersi. Grazie ancora e buona giornata!",
              "isCorrect": True,
              "feedback": "Excellent closing."
            },
            {
              "text": "Non userò mai lo scanner in vita mia.",
              "isCorrect": False,
              "feedback": "Never say never!"
            },
            {
              "text": "Voglio scansionare la mia faccia.",
              "isCorrect": False,
              "feedback": "Not very professional!"
            }
          ]
        }
      ]
    },
    {
      "id": "meeting_room",
      "title": "Prenotare una sala",
      "description": "Reserve a meeting room for a team call.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Ciao! Hai bisogno di aiuto per prenotare la sala riunioni?",
          "english": "Hi! Do you need help booking the meeting room?",
          "choices": [
            {
              "text": "Sì, grazie. Ho un incontro importante domani mattina alle dieci.",
              "isCorrect": True,
              "feedback": "Clear statement of your needs."
            },
            {
              "text": "Voglio comprare la sala riunioni.",
              "isCorrect": False,
              "feedback": "You can only rent or book it, not buy it!"
            },
            {
              "text": "Non mi piacciono le riunioni. Voglio scappare.",
              "isCorrect": False,
              "feedback": "Sometimes we all have to attend meetings!"
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Va bene, guardo subito il calendario. Quante persone sarete?",
          "english": "Alright, I'll check the calendar right away. How many people will you be?",
          "choices": [
            {
              "text": "Saremo in tre qui di persona, e due colleghi in videochiamata.",
              "isCorrect": True,
              "feedback": "Good detail. They need to know if you need video equipment."
            },
            {
              "text": "Saremo cinquanta persone. È una grande festa.",
              "isCorrect": False,
              "feedback": "Meeting rooms are usually for small groups, not 50 people!"
            },
            {
              "text": "Sarò solo io, ma voglio una sala enorme.",
              "isCorrect": False,
              "feedback": "Usually, small rooms are given to single people."
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Capisco. Allora ti serve una sala con lo schermo e il proiettore, giusto?",
          "english": "I understand. Then you need a room with a screen and a projector, right?",
          "choices": [
            {
              "text": "Esattamente. È possibile collegare il mio computer portatile allo schermo?",
              "isCorrect": True,
              "feedback": "Important technical question."
            },
            {
              "text": "No, useremo la telepatia per comunicare.",
              "isCorrect": False,
              "feedback": "Technology is more reliable!"
            },
            {
              "text": "Voglio un televisore degli anni ottanta.",
              "isCorrect": False,
              "feedback": "They only have modern equipment."
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "Sì, c'è un cavo HDMI sul tavolo. La Sala Blu è libera alle dieci.",
          "english": "Yes, there is an HDMI cable on the table. The Blue Room is free at ten.",
          "choices": [
            {
              "text": "Perfetto. Quanto costa prenotare la Sala Blu per due ore?",
              "isCorrect": True,
              "feedback": "Asking about the price for the specific duration."
            },
            {
              "text": "Non mi piace il blu. Cambiate il colore della stanza.",
              "isCorrect": False,
              "feedback": "It's just the name of the room!"
            },
            {
              "text": "Due ore sono poche, la prenoto per un mese intero.",
              "isCorrect": False,
              "feedback": "You can't book a shared meeting room for a whole month."
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Il costo è di quindici euro l'ora, quindi trenta euro in totale.",
          "english": "The cost is fifteen euros an hour, so thirty euros in total.",
          "choices": [
            {
              "text": "Va bene, il prezzo è giusto. Come posso pagare?",
              "isCorrect": True,
              "feedback": "Accepting the price and moving to payment."
            },
            {
              "text": "È troppo caro. Vi do solo cinque euro.",
              "isCorrect": False,
              "feedback": "You can't negotiate fixed prices in a coworking space."
            },
            {
              "text": "Pago con un sorriso e una stretta di mano.",
              "isCorrect": False,
              "feedback": "They need real money!"
            }
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Aggiungiamo il costo direttamente alla tua fattura mensile. Sei d'accordo?",
          "english": "We add the cost directly to your monthly invoice. Do you agree?",
          "choices": [
            {
              "text": "Sì, è molto comodo così. Confermo la prenotazione.",
              "isCorrect": True,
              "feedback": "Confirming the booking is the final step."
            },
            {
              "text": "No, voglio pagare in monete da un centesimo adesso.",
              "isCorrect": False,
              "feedback": "Adding to the invoice is standard procedure and easier."
            },
            {
              "text": "Non voglio pagare nessuna fattura mensile.",
              "isCorrect": False,
              "feedback": "But you have a monthly subscription!"
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Ottimo. Ho riservato la Sala Blu per te domani dalle dieci alle dodici.",
          "english": "Excellent. I have reserved the Blue Room for you tomorrow from ten to twelve.",
          "choices": [
            {
              "text": "Grazie. Riceverò un'email di conferma con i dettagli?",
              "isCorrect": True,
              "feedback": "Good to ask for a written confirmation."
            },
            {
              "text": "Voglio che tu mi mandi un telegramma per confermare.",
              "isCorrect": False,
              "feedback": "An email is much faster and standard."
            },
            {
              "text": "Dimenticherò tutto domani.",
              "isCorrect": False,
              "feedback": "Set an alarm on your phone then!"
            }
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Sì, il nostro sistema ti invierà un'email tra pochi minuti.",
          "english": "Yes, our system will send you an email in a few minutes.",
          "choices": [
            {
              "text": "Ho un'ultima domanda. Posso portare dei caffè nella sala?",
              "isCorrect": True,
              "feedback": "Checking the rules about food and drink is polite."
            },
            {
              "text": "Posso accendere un fuoco nella sala per scaldarmi?",
              "isCorrect": False,
              "feedback": "Absolutely not! That's very dangerous."
            },
            {
              "text": "Voglio cucinare una bistecca durante la riunione.",
              "isCorrect": False,
              "feedback": "You can't cook in a meeting room!"
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Certamente, puoi portare bevande e piccoli snack. Chiediamo solo di lasciare pulito.",
          "english": "Certainly, you can bring drinks and small snacks. We only ask that you leave it clean.",
          "choices": [
            {
              "text": "Certo, lasceremo la sala in perfetto ordine. Grazie mille.",
              "isCorrect": True,
              "feedback": "Reassuring them that you will respect the space."
            },
            {
              "text": "Io lascio sempre tutto sporco, mi dispiace.",
              "isCorrect": False,
              "feedback": "You might lose your coworking pass if you do that!"
            },
            {
              "text": "Porterò un maiale arrosto intero.",
              "isCorrect": False,
              "feedback": "That's not a 'small snack'!"
            }
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Grazie a te. Buona riunione per domani!",
          "english": "Thank you. Have a good meeting tomorrow!",
          "choices": [
            {
              "text": "Crepi il lupo! A domani.",
              "isCorrect": True,
              "feedback": "A standard Italian expression for good luck."
            },
            {
              "text": "Non voglio fare la riunione, vado a piangere.",
              "isCorrect": False,
              "feedback": "Be positive, you can do it!"
            },
            {
              "text": "Spero che la riunione sia un disastro.",
              "isCorrect": False,
              "feedback": "Why would you hope for that?"
            }
          ]
        }
      ]
    },
    {
      "id": "coffee_break",
      "title": "Pausa caffè",
      "description": "Have a coffee break and chat with a coworker.",
      "messages": [
        {
          "id": "m1",
          "role": "host",
          "text": "Ciao! Anche tu qui per una pausa caffè? Questa macchina fa un buon espresso.",
          "english": "Hi! Are you here for a coffee break too? This machine makes a good espresso.",
          "choices": [
            {
              "text": "Ciao! Sì, avevo proprio bisogno di una pausa. Lavoro al computer da ore.",
              "isCorrect": True,
              "feedback": "A natural way to start a conversation with a coworker."
            },
            {
              "text": "Non parlarmi, voglio solo il mio caffè.",
              "isCorrect": False,
              "feedback": "Coworking spaces are for networking too, don't be rude!"
            },
            {
              "text": "Odio il caffè, fa male alla salute.",
              "isCorrect": False,
              "feedback": "Then why are you at the coffee machine?"
            }
          ]
        },
        {
          "id": "m2",
          "role": "host",
          "text": "Ti capisco! Io sono Marco, lavoro come grafico freelance. Tu di cosa ti occupi?",
          "english": "I understand you! I am Marco, I work as a freelance graphic designer. What do you do?",
          "choices": [
            {
              "text": "Piacere Marco. Io sono uno sviluppatore web. Lavoro per un'agenzia straniera.",
              "isCorrect": True,
              "feedback": "Good introduction and sharing of professional background."
            },
            {
              "text": "Il mio lavoro è un segreto di stato.",
              "isCorrect": False,
              "feedback": "A bit weird for casual small talk!"
            },
            {
              "text": "Non faccio niente, guardo lo schermo vuoto tutto il giorno.",
              "isCorrect": False,
              "feedback": "That doesn't sound very productive!"
            }
          ]
        },
        {
          "id": "m3",
          "role": "host",
          "text": "Sviluppatore web, interessante! Lavori sempre in questo spazio di coworking?",
          "english": "Web developer, interesting! Do you always work in this coworking space?",
          "choices": [
            {
              "text": "Sì, vengo qui quasi tutti i giorni. A casa ci sono troppe distrazioni.",
              "isCorrect": True,
              "feedback": "A common and relatable reason for using a coworking space."
            },
            {
              "text": "Vengo qui solo per rubare il caffè gratis.",
              "isCorrect": False,
              "feedback": "You shouldn't admit that!"
            },
            {
              "text": "A casa ho cinquanta gatti rumorosi.",
              "isCorrect": False,
              "feedback": "That's a very specific distraction!"
            }
          ]
        },
        {
          "id": "m4",
          "role": "host",
          "text": "È vero, anche per me è così. Qui l'ambiente è più professionale. Prendi lo zucchero?",
          "english": "It's true, it's the same for me. The environment here is more professional. Do you take sugar?",
          "choices": [
            {
              "text": "No grazie, bevo il caffè amaro. Sai se c'è un posto dove mangiare qui vicino?",
              "isCorrect": True,
              "feedback": "Good transition to asking for local recommendations."
            },
            {
              "text": "Voglio cinque bustine di zucchero nel mio piccolo caffè.",
              "isCorrect": False,
              "feedback": "That's too much sugar!"
            },
            {
              "text": "Metto il sale nel caffè per restare sveglio.",
              "isCorrect": False,
              "feedback": "That sounds terrible!"
            }
          ]
        },
        {
          "id": "m5",
          "role": "host",
          "text": "Sì, c'è una buona panetteria proprio all'angolo. Fanno dei panini fantastici.",
          "english": "Yes, there is a good bakery right on the corner. They make fantastic sandwiches.",
          "choices": [
            {
              "text": "Ottimo consiglio! Forse ci vado per la pausa pranzo. Tu di solito dove mangi?",
              "isCorrect": True,
              "feedback": "Keeping the conversation going smoothly."
            },
            {
              "text": "Odio i panini, voglio un ristorante stellato.",
              "isCorrect": False,
              "feedback": "Usually, lunch breaks are quick and simple."
            },
            {
              "text": "Non mangio mai a pranzo, vivo di solo caffè.",
              "isCorrect": False,
              "feedback": "That's not very healthy!"
            }
          ]
        },
        {
          "id": "m6",
          "role": "host",
          "text": "Io spesso mi porto il pranzo da casa e mangio qui nell'area cucina.",
          "english": "I often bring lunch from home and eat here in the kitchen area.",
          "choices": [
            {
              "text": "È una buona idea per risparmiare. Forse inizierò a farlo anche io.",
              "isCorrect": True,
              "feedback": "Agreeing and showing interest in their habits."
            },
            {
              "text": "Portare il pranzo da casa è da poveri.",
              "isCorrect": False,
              "feedback": "That's very offensive! Many professionals do it."
            },
            {
              "text": "Rubo il cibo degli altri dal frigorifero.",
              "isCorrect": False,
              "feedback": "That is completely unacceptable!"
            }
          ]
        },
        {
          "id": "m7",
          "role": "host",
          "text": "Sì, si risparmia e si mangia più sano. Hai dei progetti importanti in corso?",
          "english": "Yes, you save money and eat healthier. Do you have any important projects going on?",
          "choices": [
            {
              "text": "Sì, sto finendo un sito e-commerce molto complesso. E tu?",
              "isCorrect": True,
              "feedback": "Sharing a bit about your work and asking them back."
            },
            {
              "text": "Non faccio niente di importante, gioco ai videogiochi.",
              "isCorrect": False,
              "feedback": "Maybe keep that to yourself!"
            },
            {
              "text": "Sto progettando una macchina del tempo.",
              "isCorrect": False,
              "feedback": "Very unlikely in a web developer role!"
            }
          ]
        },
        {
          "id": "m8",
          "role": "host",
          "text": "Io sto creando il logo per una nuova startup. Ci vuole molta creatività.",
          "english": "I am creating the logo for a new startup. It takes a lot of creativity.",
          "choices": [
            {
              "text": "Sembra stimolante! Se hai bisogno di un sito web per loro, fammi sapere.",
              "isCorrect": True,
              "feedback": "Great networking! Offering your services to a colleague."
            },
            {
              "text": "Il lavoro di grafico è troppo facile, tutti possono farlo.",
              "isCorrect": False,
              "feedback": "That's insulting to their profession."
            },
            {
              "text": "Disegna il mio viso come logo per la startup.",
              "isCorrect": False,
              "feedback": "That wouldn't make sense for a startup!"
            }
          ]
        },
        {
          "id": "m9",
          "role": "host",
          "text": "Ah, fantastico! È un'ottima idea, potremmo collaborare in futuro. Ti do il mio biglietto da visita.",
          "english": "Ah, fantastic! That's a great idea, we could collaborate in the future. I'll give you my business card.",
          "choices": [
            {
              "text": "Volentieri! Aggiungiamoci anche su LinkedIn. È stato un piacere parlare con te.",
              "isCorrect": True,
              "feedback": "Perfect professional conclusion to the chat."
            },
            {
              "text": "Non voglio il tuo biglietto da visita, lo butto.",
              "isCorrect": False,
              "feedback": "That's incredibly rude!"
            },
            {
              "text": "Io non ho un nome e non uso LinkedIn.",
              "isCorrect": False,
              "feedback": "Networking might be hard for you then!"
            }
          ]
        },
        {
          "id": "m10",
          "role": "host",
          "text": "Il piacere è mio! Ora torno alla mia scrivania. Buon lavoro!",
          "english": "The pleasure is mine! Now I'm going back to my desk. Have a good work day!",
          "choices": [
            {
              "text": "Grazie, buon lavoro anche a te Marco. Ci vediamo in giro.",
              "isCorrect": True,
              "feedback": "Friendly and polite goodbye."
            },
            {
              "text": "Io resto qui a bere caffè tutto il giorno.",
              "isCorrect": False,
              "feedback": "You should probably do some work!"
            },
            {
              "text": "Vai via, non voglio più vederti.",
              "isCorrect": False,
              "feedback": "Completely unnecessary aggression!"
            }
          ]
        }
      ]
    }
  ]
}

with open("src/data/scenarios/workstudy/coworking_space/conversations.json", "w", encoding="utf-8") as f:
    json.dump(conversations_data, f, indent=2, ensure_ascii=False)
