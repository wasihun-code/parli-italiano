import json

def update_phrases(file_path, translations):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for item in data:
        if item['italian'] in translations:
            item['english'] = translations[item['italian']]
            
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

phrase_translations = {
    "A volte sono troppo perfezionista nel mio lavoro.": "Sometimes I am too much of a perfectionist in my work.",
    "Assolutamente, so gestire bene il tempo a disposizione.": "Absolutely, I know how to manage the available time well.",
    "Buongiorno, sì, esatto. Grazie mille.": "Good morning, yes, exactly. Thank you very much.",
    "Capisco. È prevista anche una formazione iniziale?": "I see. Is initial training also planned?",
    "Cercavo nuove sfide e opportunità di crescita.": "I was looking for new challenges and growth opportunities.",
    "Cerco sempre di comunicare e trovare una soluzione.": "I always try to communicate and find a solution.",
    "Certamente, sono disponibile a fare trasferte brevi.": "Certainly, I am available to go on short business trips.",
    "Direi innovativa, per i vostri progetti recenti.": "I would say innovative, because of your recent projects.",
    "Gestivo i clienti e preparavo i rapporti mensili.": "I managed clients and prepared monthly reports.",
    "Grazie a lei, buona giornata e a presto.": "Thank you, have a good day and see you soon.",
    "Ho imparato a lavorare bene sotto pressione.": "I have learned to work well under pressure.",
    "Ho studiato molto e ho chiesto aiuto ai colleghi.": "I studied a lot and asked colleagues for help.",
    "La qualità del vostro servizio clienti è superiore.": "The quality of your customer service is superior.",
    "Leggo articoli specializzati e partecipo ai corsi.": "I read specialized articles and participate in courses.",
    "Mi piace collaborare, ma sono anche autonomo.": "I like to collaborate, but I am also independent.",
    "Mi vedo come un manager esperto in questo settore.": "I see myself as an expert manager in this sector.",
    "Nessun problema, posso fornirvi i loro contatti.": "No problem, I can provide you with their contacts.",
    "No, sono molto sicuro di volere questo lavoro.": "No, I am very sure that I want this job.",
    "Ottimo, aspetterò la vostra chiamata allora.": "Great, I will wait for your call then.",
    "Parlo correntemente inglese e un po' di francese.": "I speak English fluently and a little French.",
    "Penso di aver coperto i punti principali, grazie.": "I think I have covered the main points, thank you.",
    "Perché ammiro i vostri progetti e la vostra visione.": "Because I admire your projects and your vision.",
    "Porto la mia energia e le mie nuove idee.": "I bring my energy and my new ideas.",
    "Qual è lo stipendio mensile previsto per il ruolo?": "What is the monthly salary planned for the role?",
    "Sicuramente imparare a usare il nuovo sistema informatico.": "Definitely learning how to use the new IT system.",
    "So che siete leader nel settore delle tecnologie.": "I know that you are leaders in the technology sector.",
    "Sono una persona molto organizzata e puntuale.": "I am a very organized and punctual person.",
    "Sì, che tipo di contratto offrite per questa posizione?": "Yes, what type of contract do you offer for this position?",
    "Sì, come descriverebbe la cultura aziendale?": "Yes, how would you describe the company culture?",
    "Sì, conosco bene il pacchetto Office e altri software.": "Yes, I know the Office suite and other software well.",
    "Sì, ho guidato un piccolo team in passato.": "Yes, I have led a small team in the past.",
    "Sì, ho lavorato per due anni in un'azienda simile.": "Yes, I worked for two years in a similar company.",
    "Sì, ho seguito diversi progetti dall'inizio alla fine.": "Yes, I have followed several projects from start to finish.",
    "Sì, ho studiato le altre aziende del vostro settore.": "Yes, I have studied the other companies in your sector.",
    "Sì, ho una laurea in economia e commercio.": "Yes, I have a degree in economics and business.",
    "Sì, vi ho lasciato il mio indirizzo email sul curriculum.": "Yes, I left my email address for you on my resume.",
    "Uso un'agenda digitale e dei software specifici.": "I use a digital calendar and specific software.",
    "Va bene, grazie. Quando avrò una risposta definitiva?": "Alright, thank you. When will I have a definitive answer?",
    "Va bene, sono pronto anche per la visita medica.": "Alright, I am also ready for the medical check-up.",
    "Vorrei crescere professionalmente in questa società.": "I would like to grow professionally in this company."
}

update_phrases('src/data/exports/workstudy/job_interview/workstudy_job_interview_phrases.json', phrase_translations)
