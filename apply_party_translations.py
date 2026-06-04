import json
import os

base_path = 'src/data/exports/social/at_a_party/'

vocab_file = os.path.join(base_path, 'social_at_a_party_vocabulary.json')
phrases_file = os.path.join(base_path, 'social_at_a_party_phrases.json')
sentences_file = os.path.join(base_path, 'social_at_a_party_sentences.json')

vocab_trans = {
    "v6": "friend (female)",
    "v8": "I love",
    "v12": "to go there",
    "v13": "to go",
    "v14": "gone/went",
    "v15": "year",
    "v18": "to listen",
    "v20": "absolutely",
    "v21": "atmosphere",
    "v24": "very beautiful",
    "v33": "bruschettas",
    "v40": "I understand",
    "v41": "house/home",
    "v50": "classic",
    "v54": "with",
    "v55": "concerts",
    "v56": "concerto",
    "v57": "I agree",
    "v58": "to know/meet",
    "v59": "to meet you",
    "v62": "recommendations",
    "v63": "recommendation",
    "v64": "contact",
    "v67": "crystal clear",
    "v68": "kitchen",
    "v70": "from the",
    "v74": "of the",
    "v75": "of the",
    "v76": "tell me",
    "v80": "we must",
    "v83": "where",
    "v84": "here is",
    "v85": "Elena",
    "v86": "energy",
    "v87": "summer",
    "v92": "fantastic",
    "v93": "fantastic",
    "v94": "to do/make",
    "v99": "proud",
    "v101": "very fresh",
    "v104": "people",
    "v108": "already",
    "v109": "the",
    "v111": "group",
    "v112": "taste",
    "v114": "they have",
    "v115": "idea",
    "v116": "incredible",
    "v118": "together",
    "v124": "jazz",
    "v126": "to read",
    "v127": "free",
    "v128": "local",
    "v130": "maybe",
    "v134": "sea",
    "v136": "marvel/wonder",
    "v137": "wonderful",
    "v140": "best",
    "v142": "minimalist",
    "v143": "my",
    "v144": "modern",
    "v149": "moment",
    "v151": "Måneskin",
    "v152": "in the",
    "v154": "numbers",
    "v155": "number",
    "v156": "new",
    "v157": "beyond/besides",
    "v165": "people",
    "v166": "they like",
    "v169": "would like",
    "v170": "fully",
    "v174": "tomato",
    "v176": "we can",
    "v177": "you prefer",
    "v178": "I prefer",
    "v182": "I introduce",
    "v184": "purpose/by the way",
    "v185": "next",
    "v186": "tried",
    "v187": "Puglia",
    "v191": "that",
    "v194": "you tell/stories",
    "v196": "reason",
    "v197": "recent",
    "v198": "rest",
    "v199": "renovated",
    "v203": "would be",
    "v204": "to exchange",
    "v207": "last/past",
    "v209": "simplicity",
    "v210": "always",
    "v213": "I hear/feel",
    "v216": "Sicily",
    "v217": "nice/likeable",
    "v219": "only/alone",
    "v221": "especially",
    "v223": "sport",
    "v228": "been (female)",
    "v229": "been/state",
    "v230": "style",
    "v231": "wonderful/gorgeous",
    "v232": "wonderful",
    "v233": "appetizers",
    "v235": "immediately",
    "v237": "south",
    "v238": "on the",
    "v239": "so much",
    "v241": "table",
    "v242": "time",
    "v243": "let's keep",
    "v244": "terrace",
    "v247": "your (plural)",
    "v248": "all/entire",
    "v250": "last",
    "v253": "I go",
    "v255": "to see",
    "v260": "travels",
    "v261": "to travel",
    "v262": "you come/come",
    "v264": "visited",
    "v265": "view",
    "v268": "alive/I live",
    "v269": "gladly",
    "v270": "time",
    "v271": "I would like"
}

phrases_trans = {
    "p2": "I love going to concerts! The atmosphere is fantastic.",
    "p4": "Certainly, here is my number!",
    "p6": "How wonderful! You can see the whole city.",
    "p7": "Hi Elena, nice to meet you!",
    "p9": "I fully agree with you.",
    "p13": "You're right, the sea there is crystal clear.",
    "p15": "I really like reading and doing sports.",
    "p18": "No, I only know you and Paolo.",
    "p19": "No, not yet. What do you recommend?",
    "p20": "Great idea, I'll take one right away.",
    "p21": "I prefer modern and minimalist style.",
    "p23": "That would be fantastic! I like them a lot too.",
    "p25": "I went to see a local jazz group.",
    "p27": "Yes, absolutely! I feel very alive.",
    "p29": "Yes, I visited Sicily last year.",
    "p33": "Yes, I'd love to!",
    "p37": "Traveling is wonderful! Where have you been recently?",
    "p38": "Gladly! I like meeting new people.",
    "p39": "Gladly, let's keep in touch!",
    "p40": "It's gorgeous! You have great taste."
}

def update_json(file_path, translations):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated = False
    for item in data:
        if item['id'] in translations and item['english'] == "":
            item['english'] = translations[item['id']]
            updated = True
            
    if updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated {file_path}")
    else:
        print(f"No updates for {file_path}")

update_json(vocab_file, vocab_trans)
update_json(phrases_file, phrases_trans)
update_json(sentences_file, {}) # Sentences seemed okay but can add if needed
