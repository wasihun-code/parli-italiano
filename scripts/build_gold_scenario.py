import json
import os

conversations = [
    {
        "id": "smooth_check_in",
        "title": "Smooth Check-In",
        "description": "Meet your host and enter the building normally.",
        "messages": [
            {
                "id": "m1",
                "role": "host",
                "text": "Ciao! Piacere di conoscerti. Sei arrivato davanti al palazzo?",
                "english": "Hi! Nice to meet you. Have you arrived in front of the building?",
                "choices": [
                    {
                        "text": "Sì, sono appena arrivato. Sono davanti al palazzo.",
                        "isCorrect": True,
                        "feedback": "Perfetto! Politeness and location confirmation are key."
                    },
                    {
                        "text": "Dove sono le chiavi? Ho fretta.",
                        "isCorrect": False,
                        "feedback": "A bit rude! Italian hosts appreciate a warmer greeting."
                    },
                    {
                        "text": "Il portone è chiuso, non posso entrare.",
                        "isCorrect": False,
                        "feedback": "True, but start with a greeting!"
                    }
                ]
            },
            {
                "id": "m2",
                "role": "host",
                "text": "Ottimo. Il portone è chiuso? Hai il codice per entrare?",
                "english": "Excellent. Is the main door closed? Do you have the code to enter?",
                "choices": [
                    {
                        "text": "No, purtroppo non ho il codice per entrare. Dove lo trovo?",
                        "isCorrect": True,
                        "feedback": "Exactly. Reporting the missing info clearly."
                    },
                    {
                        "text": "Suona a Bianchi L., terzo piano.",
                        "isCorrect": False,
                        "feedback": "That's an instruction for you, not something you say now!"
                    },
                    {
                        "text": "La chiave è sotto lo zerbino.",
                        "isCorrect": False,
                        "feedback": "You aren't inside the building yet!"
                    }
                ]
            },
            {
                "id": "m3",
                "role": "host",
                "text": "Scusa, pensavo di averlo mandato. Il codice è 4832, poi premi il tasto chiave. Prova!",
                "english": "Sorry, I thought I had sent it. The code is 4832, then press the key button. Try it!",
                "choices": [
                    {
                        "text": "4832... tasto chiave. Ah sì, ha funzionato! Entro.",
                        "isCorrect": True,
                        "feedback": "Success! You handled the keypad correctly."
                    },
                    {
                        "text": "La serratura è dura, non gira.",
                        "isCorrect": False,
                        "feedback": "You are at the main building door keypad, not the apartment lock yet."
                    },
                    {
                        "text": "Vengo su io, aspettami.",
                        "isCorrect": False,
                        "feedback": "The host said they are already up there!"
                    }
                ]
            },
            {
                "id": "m4",
                "role": "host",
                "text": "Benissimo. Sali al terzo piano, porta B. C'è una cassetta di sicurezza con le chiavi. Il codice è 7788.",
                "english": "Great. Go up to the third floor, door B. There is a lockbox with the keys. The code is 7788.",
                "choices": [
                    {
                        "text": "Terzo piano, porta B, codice 7788. Ricevuto, grazie!",
                        "isCorrect": True,
                        "feedback": "Great job repeating the info to confirm understanding."
                    },
                    {
                        "text": "Non ho un posto al coperto.",
                        "isCorrect": False,
                        "feedback": "You are already inside the building now!"
                    },
                    {
                        "text": "Il traffico è terribile.",
                        "isCorrect": False,
                        "feedback": "Irrelevant now that you are checking in."
                    }
                ]
            },
            {
                "id": "m5",
                "role": "host",
                "text": "Perfetto. Se hai problemi con la cassetta, chiamami. Buon soggiorno!",
                "english": "Perfect. If you have problems with the lockbox, call me. Have a good stay!",
                "choices": [
                    {
                        "text": "Grazie mille, a dopo! Ti faccio sapere se ho problemi.",
                        "isCorrect": True,
                        "feedback": "Polite exit. You are ready to start your stay."
                    },
                    {
                        "text": "Non riesco ad aprire.",
                        "isCorrect": False,
                        "feedback": "You haven't tried yet!"
                    },
                    {
                        "text": "Dov'è il router?",
                        "isCorrect": False,
                        "feedback": "You should open the door first before asking about internet."
                    }
                ]
            }
        ]
    },
    {
        "id": "cant_find_building",
        "title": "Can't Find the Building",
        "description": "Navigate a confusing street and find the correct entrance.",
        "messages": [
            {
                "id": "m1",
                "role": "host",
                "text": "Pronto? Sono l'host. Dove sei? Dovresti essere qui alle tre.",
                "english": "Hello? I am the host. Where are you? You were supposed to be here at three.",
                "choices": [
                    {
                        "text": "Ciao! Sono in ritardo, scusa. Il traffico è terribile.",
                        "isCorrect": True,
                        "feedback": "Good apology. Explaining the delay helps the host."
                    },
                    {
                        "text": "Non ho il codice.",
                        "isCorrect": False,
                        "feedback": "The host is asking where you are, not about the code yet."
                    },
                    {
                        "text": "A quale nome devo suonare?",
                        "isCorrect": False,
                        "feedback": "You haven't reached the building yet!"
                    }
                ]
            },
            {
                "id": "m2",
                "role": "host",
                "text": "Capisco. Sei sulla strada principale? Vedi il bar 'Caffè del Corso'?",
                "english": "I understand. Are you on the main street? Do you see the bar 'Caffè del Corso'?",
                "choices": [
                    {
                        "text": "Sì, vedo il bar. Ma non vedo il numero civico 42.",
                        "isCorrect": True,
                        "feedback": "Describing what you see is helpful."
                    },
                    {
                        "text": "L'ascensore è in fondo a sinistra.",
                        "isCorrect": False,
                        "feedback": "You are still outside on the street!"
                    },
                    {
                        "text": "La chiave è sotto lo zerbino.",
                        "isCorrect": False,
                        "feedback": "Too early for that!"
                    }
                ]
            },
            {
                "id": "m3",
                "role": "host",
                "text": "Ah, l'ingresso è un po' nascosto. C'è un ingresso secondario nel vicolo accanto al bar.",
                "english": "Ah, the entrance is a bit hidden. There is a secondary entrance in the alley next to the bar.",
                "choices": [
                    {
                        "text": "Un ingresso secondario? Ok, entro nel vicolo.",
                        "isCorrect": True,
                        "feedback": "Following directions correctly."
                    },
                    {
                        "text": "Piacere di conoscerti.",
                        "isCorrect": False,
                        "feedback": "You are on the phone, wait until you meet!"
                    },
                    {
                        "text": "Solleva la maniglia.",
                        "isCorrect": False,
                        "feedback": "You aren't at a door yet."
                    }
                ]
            },
            {
                "id": "m4",
                "role": "host",
                "text": "Vedi un cancello di ferro verde? Quello è il cortile interno.",
                "english": "Do you see a green iron gate? That is the internal courtyard.",
                "choices": [
                    {
                        "text": "Sì, vedo il cancello di ferro. C'è un tastierino qui.",
                        "isCorrect": True,
                        "feedback": "Accurate reporting."
                    },
                    {
                        "text": "Sono al terzo piano.",
                        "isCorrect": False,
                        "feedback": "Not yet!"
                    },
                    {
                        "text": "Il wifi non funziona.",
                        "isCorrect": False,
                        "feedback": "You are outside."
                    }
                ]
            },
            {
                "id": "m5",
                "role": "host",
                "text": "Esatto. Digita 5590 per aprire il cancelletto e attraversa il cortile.",
                "english": "Exactly. Type 5590 to open the small gate and cross the courtyard.",
                "choices": [
                    {
                        "text": "5590... fatto! Che sollievo, finalmente sono entrato nel cortile.",
                        "isCorrect": True,
                        "feedback": "You found it! Good job navigating."
                    },
                    {
                        "text": "Tira verso il basso.",
                        "isCorrect": False,
                        "feedback": "That's for a lockbox, not the gate keypad."
                    },
                    {
                        "text": "Sono l'ospite di Marco.",
                        "isCorrect": False,
                        "feedback": "There is no one to tell this to here."
                    }
                ]
            },
            {
                "id": "m6",
                "role": "host",
                "text": "Bravo. Ora entra nel portone a vetri e sali al secondo piano. Io ti aspetto lì.",
                "english": "Good. Now enter the glass door and go up to the second floor. I am waiting for you there.",
                "choices": [
                    {
                        "text": "Perfetto, salgo subito. Grazie per l'aiuto.",
                        "isCorrect": True,
                        "feedback": "Polite finish. You arrived."
                    },
                    {
                        "text": "La serratura è dura.",
                        "isCorrect": False,
                        "feedback": "You aren't at the lock yet."
                    },
                    {
                        "text": "Non ho il codice.",
                        "isCorrect": False,
                        "feedback": "You just entered it!"
                    }
                ]
            }
        ]
    },
    {
        "id": "intercom_problem",
        "title": "Intercom Problem",
        "description": "Handle a broken intercom and identify yourself to the host's neighbor.",
        "messages": [
            {
                "id": "m1",
                "role": "host",
                "text": "Buongiorno. L'aspettavo, ma non la vedo sul monitor. È davanti al portone?",
                "english": "Good morning. I was expecting you, but I don't see you on the monitor. Are you in front of the main door?",
                "choices": [
                    {
                        "text": "Sì, sono qui. Ma il citofono non funziona, non sento niente.",
                        "isCorrect": True,
                        "feedback": "Correct. Explaining the technical issue clearly."
                    },
                    {
                        "text": "Sono l'ospite di Marco, mi apre per favore?",
                        "isCorrect": False,
                        "feedback": "The host doesn't know who is speaking yet if the intercom is broken!"
                    },
                    {
                        "text": "Ho suonato a Verdi, ma non risponde nessuno.",
                        "isCorrect": False,
                        "feedback": "You already tried that, tell the host it seems broken."
                    }
                ]
            },
            {
                "id": "m2",
                "role": "host",
                "text": "Maledizione, quel citofono è sempre rotto. Provi a suonare a 'Bianchi L.', il mio vicino al terzo piano.",
                "english": "Damn, that intercom is always broken. Try ringing 'Bianchi L.', my neighbor on the third floor.",
                "choices": [
                    {
                        "text": "Bianchi L... trovato. Suono subito.",
                        "isCorrect": True,
                        "feedback": "Good. Following the alternative instruction."
                    },
                    {
                        "text": "Dove trovo il codice?",
                        "isCorrect": False,
                        "feedback": "The host just gave you a different instruction!"
                    },
                    {
                        "text": "Non ho un posto al coperto.",
                        "isCorrect": False,
                        "feedback": "Not helpful for the intercom situation."
                    }
                ]
            },
            {
                "id": "m3",
                "role": "host",
                "text": "(Il vicino risponde) Chi è?",
                "english": "(The neighbor answers) Who is it?",
                "choices": [
                    {
                        "text": "Buongiorno, sono l'ospite di Marco. Mi apre il portone per favore?",
                        "isCorrect": True,
                        "feedback": "Perfect identification. Neighbors are more likely to open if you mention the host's name."
                    },
                    {
                        "text": "Apro io per farti vedere.",
                        "isCorrect": False,
                        "feedback": "You are the one who needs the door opened!"
                    },
                    {
                        "text": "Sono appena arrivato.",
                        "isCorrect": False,
                        "feedback": "Vague. Tell them why you are ringing their bell."
                    }
                ]
            },
            {
                "id": "m4",
                "role": "host",
                "text": "Ah sì, Marco mi ha avvisato. Le apro subito il portone. Entri pure.",
                "english": "Ah yes, Marco warned me. I'll open the main door for you right away. Come on in.",
                "choices": [
                    {
                        "text": "Grazie mille, gentilissimo! Salgo subito.",
                        "isCorrect": True,
                        "feedback": "Polite and efficient. You are in!"
                    },
                    {
                        "text": "La chiave gira ma non si apre.",
                        "isCorrect": False,
                        "feedback": "They buzzed you in, no key needed."
                    },
                    {
                        "text": "Il traffico è terribile.",
                        "isCorrect": False,
                        "feedback": "No need to complain to the neighbor!"
                    }
                ]
            }
        ]
    },
    {
        "id": "wrong_entrance",
        "title": "Wrong Apartment Entrance",
        "description": "Deal with a stiff lock and ensure you are at the right door.",
        "messages": [
            {
                "id": "m1",
                "role": "host",
                "text": "Sei arrivato alla porta? È la numero 12, al terzo piano.",
                "english": "Have you arrived at the door? It's number 12, on the third floor.",
                "choices": [
                    {
                        "text": "Sì, sono qui. Ma la chiave gira e la porta non si apre.",
                        "isCorrect": True,
                        "feedback": "Good. Describing the mechanical issue."
                    },
                    {
                        "text": "La chiave è sotto lo zerbino.",
                        "isCorrect": False,
                        "feedback": "You already have the key in your hand!"
                    },
                    {
                        "text": "In una bustina di plastica.",
                        "isCorrect": False,
                        "feedback": "That's where you found the key, but now the problem is the lock!"
                    }
                ]
            },
            {
                "id": "m2",
                "role": "host",
                "text": "Strano. Forse stai spingendo poco. Hai provato a sollevare la maniglia mentre giri?",
                "english": "Strange. Maybe you are not pushing enough. Have you tried lifting the handle while turning?",
                "choices": [
                    {
                        "text": "Sollevare la maniglia? Ci provo... ancora niente. È bloccata.",
                        "isCorrect": True,
                        "feedback": "Trying the suggested solution and reporting failure."
                    },
                    {
                        "text": "Ho paura di romperla.",
                        "isCorrect": False,
                        "feedback": "Valid fear, but try the instruction first!"
                    },
                    {
                        "text": "Tira la levetta.",
                        "isCorrect": False,
                        "feedback": "That's for a lockbox, not a door handle."
                    }
                ]
            },
            {
                "id": "m3",
                "role": "host",
                "text": "Ma sei sicuro di essere al piano giusto? Sulla porta c'è scritto 'Interno 12'?",
                "english": "But are you sure you are on the right floor? Does it say 'Internal 12' on the door?",
                "choices": [
                    {
                        "text": "Aspetta... no, qui c'è scritto Interno 10. Ho sbagliato porta!",
                        "isCorrect": True,
                        "feedback": "Oops! Finding the root cause."
                    },
                    {
                        "text": "Questa serratura è dura.",
                        "isCorrect": False,
                        "feedback": "Maybe it's the wrong lock entirely!"
                    },
                    {
                        "text": "A quale nome devo suonare?",
                        "isCorrect": False,
                        "feedback": "You are already inside at the apartment doors."
                    }
                ]
            },
            {
                "id": "m4",
                "role": "host",
                "text": "Ah ecco! La 12 è quella in fondo al corridoio. Prova lì.",
                "english": "Ah there you go! 12 is the one at the end of the hallway. Try there.",
                "choices": [
                    {
                        "text": "Trovata! Questa si apre al primo colpo. Grazie per la pazienza.",
                        "isCorrect": True,
                        "feedback": "Success! You are finally in the right place."
                    },
                    {
                        "text": "Non si apre.",
                        "isCorrect": False,
                        "feedback": "Actually, it should open fine if it's the right door."
                    },
                    {
                        "text": "Dovrebbe aprirsi.",
                        "isCorrect": False,
                        "feedback": "You need to confirm it opened."
                    }
                ]
            },
            {
                "id": "m5",
                "role": "host",
                "text": "Meno male! Ricordati di dare due mandate quando esci.",
                "english": "Thank goodness! Remember to give it two turns when you leave.",
                "choices": [
                    {
                        "text": "Certamente, darò due mandate. A presto!",
                        "isCorrect": True,
                        "feedback": "Good acknowledgement of security rules."
                    },
                    {
                        "text": "La chiave è sotto lo zerbino.",
                        "isCorrect": False,
                        "feedback": "Don't leave the key there when you go out."
                    },
                    {
                        "text": "Vengo su io.",
                        "isCorrect": False,
                        "feedback": "You are already there."
                    }
                ]
            }
        ]
    }
]

# Next we write a script to extract vocabulary, phrases, sentences from this.
def extract_curriculum():
    words = set()
    phrases_set = set()
    sentences_list = []
    
    # Simple tokenizer
    import re
    def tokenize(text):
        text = text.lower()
        text = re.sub(r"[^\w\sàèìòùé]", "", text)
        return set(text.split())
        
    for conv in conversations:
        for msg in conv["messages"]:
            # Host text goes to sentences
            sentences_list.append({
                "italian": msg["text"],
                "english": msg["english"],
                "grammarPoint": "Conversation line"
            })
            words.update(tokenize(msg["text"]))
            
            # User correct text goes to phrases
            for choice in msg["choices"]:
                if choice["isCorrect"]:
                    phrases_set.add(choice["text"])
                    words.update(tokenize(choice["text"]))
                    
    # Generate Vocab list
    vocab_list = [{"italian": w, "english": "translation needed"} for w in sorted(list(words)) if len(w) > 2]
    
    return list(phrases_set), sentences_list, vocab_list

print("Writing conversations.json...")
with open("src/data/exports/accommodation/apartment_key_pickup/conversations.json", "w", encoding="utf-8") as f:
    json.dump({
        "scenarioId": 22,
        "conversations": conversations
    }, f, ensure_ascii=False, indent=2)

print("Conversations written.")

