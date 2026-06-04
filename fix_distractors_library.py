import json
import os

file_path = 'src/data/exports/daily_life/at_the_library/conversations.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# finding_books fixes
m1 = data['conversations'][0]['messages'][0]
m1['choices'][1]['text'] = "Mi scusi, saprebbe dirmi dove si trova il bagno più vicino?"
m1['choices'][2]['text'] = "Ho molta fame, saprebbe dirmi se c'è un bar qui nei dintorni?"

m3 = data['conversations'][0]['messages'][2]
m3['choices'][1]['text'] = "Mi scusi, ma potrebbe spiegarmi meglio cos'è un catalogo?"

m4 = data['conversations'][0]['messages'][3]
m4['choices'][1]['text'] = "Non mi piace questo posto, la scrivania mi sembra molto sporca."
m4['choices'][2]['text'] = "Mi dispiace, ma purtroppo non so come si usa questo computer."

m5 = data['conversations'][0]['messages'][4]
m5['choices'][2]['text'] = "Mi dispiace, ma purtroppo non ho ancora fatto la tessera."

m6 = data['conversations'][0]['messages'][5]
m6['choices'][1]['text'] = "Mi dispiace, ma non ho proprio voglia di aspettare così tanto."

m8 = data['conversations'][0]['messages'][7]
m8['choices'][1]['text'] = "Non leggo mai le email, non c'è un altro modo per avvisarmi?"
m8['choices'][2]['text'] = "Vorrei prenotare almeno cento libri, è possibile farlo subito?"

m9 = data['conversations'][0]['messages'][8]
m9['choices'][1]['text'] = "Solo tre libri? Mi sembra che sia un numero davvero esiguo!"

m10 = data['conversations'][0]['messages'][9]
m10['choices'][1]['text'] = "Mi scusi, ma ora devo andare via, ciao!"
m10['choices'][2]['text'] = "Saprebbe dirmi dove si trova l'uscita?"

# library_card fixes
m1_c2 = data['conversations'][1]['messages'][0]
m1_c2['choices'][1]['text'] = "No, grazie, per ora sto solo guardando gli scaffali della sala."
m1_c2['choices'][2]['text'] = "Mi scusi, saprebbe dirmi quanto costa mediamente un libro qui?"

m4_c2 = data['conversations'][1]['messages'][3]
m4_c2['choices'][1]['text'] = "Perché il servizio è gratis? Sinceramente non mi fido affatto."
m4_c2['choices'][2]['text'] = "Preferirei pagare comunque il servizio, non mi piacciono i regali."

m5_c2 = data['conversations'][1]['messages'][4]
m5_c2['choices'][1]['text'] = "Un anno è troppo poco, vorrei una validità di almeno dieci anni."
m5_c2['choices'][2]['text'] = "Non vorrei che questa tessera scadesse mai, è possibile farlo?"

m7_c2 = data['conversations'][1]['messages'][6]
m7_c2['choices'][1]['text'] = "Voglio venire qui ogni giorno, non mi servono affatto i siti online."
m7_c2['choices'][2]['text'] = "Mi scusi, ma potrebbe spiegarmi meglio cos'è questo internet?"

m9_c2 = data['conversations'][1]['messages'][8]
m9_c2['choices'][2]['text'] = "Mi scusi, posso mettere un adesivo colorato sulla tessera?"

m10_c2 = data['conversations'][1]['messages'][9]
m10_c2['choices'][1]['text'] = "No, preferisco perdermi tra gli scaffali da solo, grazie comunque."
m10_c2['choices'][2]['text'] = "Sono molto stanco ora e vorrei tornare subito a casa mia."

# study_room fixes
m1_c3 = data['conversations'][2]['messages'][0]
m1_c3['choices'][1]['text'] = "Voglio dormire un po', c'è un divano comodo da qualche parte?"
m1_c3['choices'][2]['text'] = "C'è troppa gente qui, non riesco a trovare il silenzio che cerco."

m3_c3 = data['conversations'][2]['messages'][2]
m3_c3['choices'][1]['text'] = "Posso ascoltare musica ad alto volume mentre studio la lezione?"
m3_c3['choices'][2]['text'] = "Purtroppo il silenzio assoluto mi mette sempre molta ansia."

m4_c3 = data['conversations'][2]['messages'][3]
m4_c3['choices'][1]['text'] = "Purtroppo non lo vedo, può dirmela lei a voce, per favore?"
m4_c3['choices'][2]['text'] = "Mi scusi, ma onestamente non vedo nessun cartello qui intorno."

m6_c3 = data['conversations'][2]['messages'][5]
m6_c3['choices'][1]['text'] = "Mi scusi, ma purtroppo credo di aver perso la chiave poco fa."
m6_c3['choices'][2]['text'] = "Ho provato ad aprirla, ma mi sembra che la toppa sia rotta."

m7_c3 = data['conversations'][2]['messages'][6]
m7_c3['choices'][1]['text'] = "Aspetto una chiamata molto importante e devo assolutamente rispondere."

m8_c3 = data['conversations'][2]['messages'][7]
m8_c3['choices'][2]['text'] = "Saprebbe indicarmi in quale scaffale si trovano i fumetti?"

m9_c3 = data['conversations'][2]['messages'][8]
m9_c3['choices'][2]['text'] = "Purtroppo non posso bere il caffè perché mi rende molto nervoso."

m10_c3 = data['conversations'][2]['messages'][9]
m10_c3['choices'][1]['text'] = "Spero di finire presto perché onestamente odio molto studiare."
m10_c3['choices'][2]['text'] = "Arrivederci, spero sinceramente di non rivederla mai più!"

# returning_books fixes
m1_c4 = data['conversations'][3]['messages'][0]
m1_c4['choices'][1]['text'] = "No, questi libri mi piacciono e ho deciso di tenerli per sempre."
m1_c4['choices'][2]['text'] = "Purtroppo li ho persi tutti e non so come fare per rimediare."

m2_c4 = data['conversations'][3]['messages'][1]
m2_c4['choices'][2]['text'] = "E allora? Mi sembra che siano passati solo cinque giorni di ritardo."

m3_c4 = data['conversations'][3]['messages'][2]
m3_c4['choices'][1]['text'] = "Non voglio pagare niente, non è colpa mia se ho dimenticato la data."
m3_c4['choices'][2]['text'] = "Secondo me questo è un vero furto, non pagherò mai questa multa!"

m4_c4 = data['conversations'][3]['messages'][3]
m4_c4['choices'][1]['text'] = "È troppo caro per me, non potrei avere uno sconto sulla multa?"
m4_c4['choices'][2]['text'] = "Le do solo dieci centesimi e facciamo finta di essere pari."

m5_c4 = data['conversations'][3]['messages'][4]
m5_c4['choices'][1]['text'] = "Non ho soldi con me oggi, saprebbe dirmi se posso pagare l'anno prossimo?"
m5_c4['choices'][2]['text'] = "Accettate pagamenti in natura? Posso pagare con dei bottoni?"

m7_c4 = data['conversations'][3]['messages'][6]
m7_c4['choices'][2]['text'] = "Mi scusi, saprebbe dirmi onestamente che giorno è oggi, per favore?"

m10_c4 = data['conversations'][3]['messages'][9]
m10_c4['choices'][1]['text'] = "Sì, sì, va bene, ciao, non ho tempo da perdere con lei."
m10_c4['choices'][2]['text'] = "Posso avere un altro libro ora, nonostante la multa che ho pagato?"

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Distractors updated.")
