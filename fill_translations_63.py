import json
import os

scenario_path = '/home/waseageru/parli-italiano/src/data/exports/workstudy/asking_for_clarification'
base_name = "workstudy_asking_for_clarification"

files = [
    f'{base_name}_vocabulary.json',
    f'{base_name}_phrases.json',
    f'{base_name}_sentences.json'
]

# Manual translations for the ones likely missing
manual_translations = {
    "Sì, il file è pronto. Scusa, puoi ripetere l'ora della riunione?": "Yes, the file is ready. Sorry, can you repeat the time of the meeting?",
    "Scusi, non ho capito bene. Può ripetere l'ora per favore?": "Excuse me, I didn't understand well. Can you repeat the time please?",
    "Sì, adesso è tutto chiaro. Grazie per il chiarimento.": "Yes, now everything is clear. Thank you for the clarification.",
    "Scusa, cosa significa 'stampati'? Puoi spiegare la parola?": "Sorry, what does 'stampati' mean? Can you explain the word?",
    "Ah, capisco. Grazie per la spiegazione, è molto utile.": "Ah, I understand. Thank you for the explanation, it's very useful.",
    "Scusa, cosa intendi per 'programma'? È un software?": "Sorry, what do you mean by 'programma'? Is it a software?",
    "No, non ho il link. Puoi inviarlo di nuovo per favore?": "No, I don't have the link. Can you send it again please?",
    "Puoi ripetere l'indirizzo email lentamente per favore?": "Can you repeat the email address slowly please?",
    "Sì, adesso è chiaro. Grazie per la pazienza.": "Yes, now it's clear. Thank you for the patience.",
    "Va bene, a domani. Grazie ancora per l'aiuto.": "Alright, see you tomorrow. Thanks again for the help.",
    "Scusi, cosa significa la parola 'budget' in italiano?": "Excuse me, what does the word 'budget' mean in Italian?",
    "Grazie, adesso capisco il significato. È molto chiaro.": "Thank you, now I understand the meaning. It's very clear.",
    "Sì, ho un dubbio. Cosa significa 'scadenza' precisamente?": "Yes, I have a doubt. What does 'scadenza' mean precisely?",
    "Capito! Grazie per l'esempio e per la cortesia.": "Understood! Thanks for the example and for the kindness.",
    "Grazie mille. Farò sicuramente altre domande se serve.": "Thank you very much. I will definitely ask other questions if needed.",
    "Scusa, chi sono i 'colleghi'? Puoi spiegare la parola?": "Sorry, who are the 'colleghi'? Can you explain the word?",
    "Ah, capisco. E chi è il 'capo' dell'ufficio?": "Ah, I understand. And who is the 'capo' of the office?",
    "Cosa significa 'pomeridiana'? È dopo pranzo?": "What does 'pomeridiana' mean? Is it after lunch?",
    "Tutto chiaro. Grazie per tutte queste spiegazioni.": "All clear. Thanks for all these explanations.",
    "Sono d'accordo. A più tardi per la riunione!": "I agree. See you later for the meeting!",
    "Scusa, puoi ripetere? Lunedì mattina o martedì?": "Sorry, can you repeat? Monday morning or Tuesday?",
    "Non ho capito bene l'ora. Può parlare più piano?": "I didn't understand the time well. Can you speak more slowly?",
    "Sì, adesso ho capito perfettamente. Grazie mille.": "Yes, now I understood perfectly. Thank you very much.",
    "Sì, ho una domanda. Cosa devo scrivere nel report?": "Yes, I have a question. What should I write in the report?",
    "Va bene, ora è tutto molto chiaro. Grazie ancora.": "Alright, now everything is very clear. Thanks again.",
    "Scusa, cosa significa 'urgente'? È molto importante?": "Sorry, what does 'urgente' mean? Is it very important?",
    "Cosa intendi per 'diciassette'? Sono le cinque di pomeriggio?": "What do you mean by 'diciassette'? Is it five in the afternoon?",
    "Ho capito. Posso finire entro le cinque allora.": "I understood. I can finish by five then.",
    "Scusa, puoi ripetere la domanda per favore?": "Sorry, can you repeat the question please?",
    "Sì, lo porto nel tuo ufficio alle cinque. Grazie!": "Yes, I'll take it to your office at five. Thank you!",
    "Scusa, parli troppo veloce. Puoi parlare più lentamente?": "Sorry, you speak too fast. Can you speak more slowly?",
    "Nessun problema. Può ripetere quello che ha detto?": "No problem. Can you repeat what you said?",
    "Grazie. Può spiegare meglio la parola 'ricerca'?": "Thank you. Can you explain the word 'ricerca' better?",
    "Ah, ho capito. Grazie per la spiegazione chiara.": "Ah, I understood. Thank you for the clear explanation.",
    "Sì, sono pronto. Grazie per la pazienza e l'aiuto.": "Yes, I'm ready. Thank you for the patience and the help.",
    "Scusa, parli di nuovo molto veloce. Puoi rallentare?": "Sorry, you're speaking very fast again. Can you slow down?",
    "Cosa significa 'presentazione'? Puoi spiegare?": "What does 'presentazione' mean? Can you explain?",
    "Capisco. Dove facciamo questa presentazione?": "I understand. Where are we doing this presentation?",
    "Puoi ripetere 'sala conferenze'? Non ho capito bene.": "Can you repeat 'sala conferenze'? I didn't understand well.",
    "Ah, la stanza grande! Ora capisco. Grazie mille.": "Ah, the large room! Now I understand. Thank you very much."
}

for filename in files:
    filepath = os.path.join(scenario_path, filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated = False
    for item in data:
        if not item.get('english'):
            if item['italian'] in manual_translations:
                item['english'] = manual_translations[item['italian']]
                updated = True
            else:
                # Basic fallback if still missing (mostly for vocabulary)
                # But vocabulary should be covered by vocab_map in extract_63.py
                pass
                
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated translations in {filename}")

print("Translation check complete.")
