import json

vocab_translations = {
    "v1": "subscription/pass", "v2": "accepts", "v3": "make yourself comfortable", "v4": "now", "v5": "help you",
    "v6": "help", "v7": "at the", "v8": "then/so", "v9": "other/another", "v10": "also/too",
    "v11": "yet/still", "v12": "to go", "v13": "open", "v14": "as soon as", "v15": "arrives",
    "v16": "arriving", "v17": "to arrive", "v18": "arrived", "v19": "goodbye", "v20": "we arrive",
    "v21": "waits", "v22": "careful", "v23": "driver", "v24": "bus", "v25": "had",
    "v26": "bar/cafe", "v27": "enough", "v28": "well", "v29": "very well", "v30": "tickets",
    "v31": "ticket", "v32": "is necessary", "v33": "board", "v34": "good", "v35": "good",
    "v36": "good morning", "v37": "bus", "v38": "I understand", "v39": "understood", "v40": "terminus",
    "v41": "dear/expensive", "v42": "book of tickets", "v43": "card/paper", "v44": "central", "v45": "central",
    "v46": "center", "v47": "certainly", "v48": "sure", "v49": "that/which", "v50": "is named",
    "v51": "to ask", "v52": "hi/bye", "v53": "fifty", "v54": "five", "v55": "about",
    "v56": "house number", "v57": "code", "v58": "convenient", "v59": "to buy", "v60": "bought",
    "v61": "bought", "v62": "with", "v63": "contactless", "v64": "continuation", "v65": "control/check",
    "v66": "inspectors", "v67": "to validate", "v68": "to validate it", "v69": "it's worth", "v70": "correct",
    "v71": "costs", "v72": "credit", "v73": "from the", "v74": "of the", "v75": "of the",
    "v76": "of the", "v77": "of the", "v78": "right", "v79": "must/has to", "v80": "I must",
    "v81": "I say", "v82": "ten", "v83": "behind", "v84": "direction", "v85": "tell me",
    "v86": "display", "v87": "have fun", "v88": "twelve", "v89": "after", "v90": "where",
    "v91": "should", "v92": "two", "v93": "during", "v94": "here is", "v95": "newsstand",
    "v96": "euro", "v97": "suburban", "v98": "I will do", "v99": "done", "v100": "favor",
    "v111": "day", "v112": "right/correct", "v113": "already", "v114": "it to him", "v115": "thank you",
    "v116": "look", "v117": "you have", "v118": "information", "v119": "to insert", "v120": "together",
    "v121": "instead", "v122": "you", "v123": "reader", "v124": "line", "v125": "machine",
    "v126": "machines", "v127": "is missing", "v128": "are missing", "v129": "Tuesday", "v130": "better",
    "v131": "monthly", "v132": "thousand", "v133": "minutes", "v134": "my", "v135": "very",
    "v136": "fines", "v137": "museum", "v138": "necessary", "v139": "in the", "v140": "not",
    "v141": "today", "v142": "each", "v143": "schedule", "v144": "excellent", "v145": "passes",
    "v146": "pass", "v147": "for", "v148": "to lose them", "v149": "perfect", "v150": "square",
    "v151": "small", "v152": "pin", "v153": "more", "v154": "few", "v155": "bridge",
    "v156": "door", "v157": "wallet", "v158": "doors", "v159": "I can", "v160": "rear",
    "v161": "previous", "v162": "you're welcome", "v163": "to press", "v164": "to press it", "v165": "press",
    "v166": "to take", "v167": "I take", "v168": "to request the stop", "v169": "get ready", "v170": "before",
    "v171": "main", "v172": "really", "v173": "next", "v174": "next", "v175": "button",
    "v176": "just", "v177": "can", "v178": "what", "v179": "which", "v180": "when",
    "v181": "how much", "v182": "almost", "v183": "four", "v184": "that", "v185": "that one",
    "v186": "this", "v187": "this", "v188": "here", "v189": "fifteen", "v190": "hold on",
    "v191": "remember", "v192": "return", "v193": "red", "v194": "you know", "v195": "boards",
    "v196": "we board", "v197": "gets off", "v198": "to get off", "v199": "written", "v200": "excuse me",
    "v201": "according to", "v202": "to sit down", "v203": "certainly", "v204": "is needed", "v205": "is",
    "v206": "we are", "v207": "certainly", "v208": "I sit", "v209": "single", "v210": "only",
    "v211": "they are", "v212": "I hope", "v213": "often", "v214": "is being", "v215": "this morning",
    "v216": "station", "v217": "historic", "v218": "immediately", "v219": "on the", "v220": "passed",
    "v221": "tobacco shop", "v222": "stops", "v223": "button", "v224": "time", "v225": "I keep",
    "v226": "to stamp it", "v227": "total", "v228": "between", "v229": "three", "v230": "is located",
    "v231": "your", "v232": "all", "v233": "everything", "v234": "one", "v235": "urban",
    "v236": "I go", "v237": "you go", "v238": "to validate", "v239": "I see", "v240": "twenty-two",
    "v241": "towards", "v242": "journey", "v243": "near", "v244": "near", "v245": "to visit",
    "v246": "gladly", "v247": "I would like", "v248": "wants",
    # Filling in some missing ones I might have skipped
    "v101": "stops", "v102": "stop", "v103": "stops", "v104": "until", "v105": "tight",
    "v106": "outside", "v107": "kind", "v108": "yellow", "v109": "day", "v110": "days"
}

phrase_translations = {
    "p1": "Ah, I see. I'm only here for a few days.",
    "p2": "Ah, look! The bus is arriving now.",
    "p3": "Ah, I see it. Thank you. Excuse me, does this bus go downtown?",
    "p4": "Great. Do I need to validate the ticket on the bus?",
    "p5": "Good morning! I would like a bus ticket.",
    "p6": "Good morning. Can I buy the ticket here on board?",
    "p7": "I understand. I already bought it at the tobacco shop.",
    "p8": "Understood. Do I need to request the stop with the button?",
    "p9": "Where is the machine to validate?",
    "p10": "Here you go. Do you accept credit cards?",
    "p11": "Done. Do I also need to enter my PIN code?",
    "p12": "Thanks for the help! Have a good continuation of your journey.",
    "p13": "Thanks for the information. I'm going to sit down.",
    "p14": "Thank you, have a good day too. Goodbye!",
    "p15": "Thank you, you're very kind. I'll sit nearby.",
    "p16": "Thank you. Which line should I take for the center?",
    "p17": "Thank you. I hope the museum is open today.",
    "p18": "Thank you. Is it necessary to request the stop?",
    "p19": "Thank you. Is this the right direction for the square?",
    "p20": "I understand. Should I press it long before the stop?",
    "p21": "I'll keep them safe in my wallet. Are we almost there?",
    "p22": "I'll certainly do that. Have a good day, driver.",
    "p23": "I will definitely do it. Bye and thanks again!",
    "p24": "Is it far to get to that stop?",
    "p25": "I need a city ticket for the center.",
    "p26": "I'll take two, please. One for the return.",
    "p27": "Great. Do you have a bus ticket for the return as well?",
    "p28": "Great. Do you know when the next one arrives?",
    "p29": "Perfect, then I'll also check the display. Thank you.",
    "p30": "Perfect. Do I need to buy the ticket on board?",
    "p31": "Perfect. Where is the nearest stop?",
    "p32": "Perfect. Can you tell me when we arrive at the square?",
    "p33": "Yes, I bought two this morning at the newsstand.",
    "p34": "Yes, do you know if line twenty-two passes by here?",
    "p35": "Yes, I know that fines are very expensive here.",
    "p36": "Yes, I would like to visit the museum. Do you know which stop it is?",
    "p37": "Alright, I understood everything. Thank you very much for the help.",
    "p38": "Alright, I didn't have time to go to the newsstand.",
    "p39": "Alright. Can you get off through all the doors?",
    "p40": "Gladly. Do you know where I should get off for the museum?"
}

def update_json(file_path, translations):
    with open(file_path, 'r') as f:
        data = json.load(f)
    for item in data:
        if item['id'] in translations:
            item['english'] = translations[item['id']]
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

update_json('src/data/exports/travel/bus_ticket/travel_bus_ticket_vocabulary.json', vocab_translations)
update_json('src/data/exports/travel/bus_ticket/travel_bus_ticket_phrases.json', phrase_translations)
print("Updated vocabulary and phrases.")
