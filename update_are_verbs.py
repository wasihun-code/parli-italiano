import json
import os

base_path = 'src/data/exports/verbs/are_verbi_in_are'

vocab_translations = {
    "v1": "agreement",
    "v2": "water",
    "v3": "help",
    "v4": "at the",
    "v5": "at the",
    "v6": "cheerful",
    "v7": "then",
    "v8": "I love",
    "v9": "to arrive",
    "v10": "arrived",
    "v11": "you listen",
    "v12": "I listen",
    "v13": "you wait",
    "v14": "I wait",
    "v15": "actors",
    "v16": "beautiful",
    "v17": "well",
    "v18": "tickets",
    "v19": "good",
    "v20": "good morning",
    "v21": "good",
    "v22": "I understand",
    "v23": "boss",
    "v24": "home",
    "v25": "drawer",
    "v26": "you look for",
    "v27": "I look for",
    "v28": "hi",
    "v29": "cinema",
    "v30": "colleague",
    "v31": "column",
    "v32": "to buy",
    "v33": "you buy",
    "v34": "I buy",
    "v35": "computer",
    "v36": "with",
    "v37": "what",
    "v38": "we cook",
    "v39": "in front of",
    "v40": "of the",
    "v41": "of the",
    "v42": "you desire",
    "v43": "I desire",
    "v44": "difficult",
    "v45": "documents",
    "v46": "tomorrow",
    "v47": "after",
    "v48": "where",
    "v49": "email",
    "v50": "exam",
    "v51": "hunger",
    "v52": "movie",
    "v53": "forks",
    "v54": "kind",
    "v55": "the",
    "v56": "thank you",
    "v57": "you watch",
    "v58": "I watch",
    "v59": "you have",
    "v60": "idea",
    "v61": "you learn",
    "v62": "I learn",
    "v63": "important",
    "v64": "together",
    "v65": "interesting",
    "v66": "you work",
    "v67": "I work",
    "v68": "lesson",
    "v69": "books",
    "v70": "language",
    "v71": "he",
    "v72": "I send",
    "v73": "we eat",
    "v74": "while",
    "v75": "thousand",
    "v76": "a lot of",
    "v77": "many",
    "v78": "much",
    "v79": "moment",
    "v80": "music",
    "v81": "in the",
    "v82": "not",
    "v83": "new",
    "v84": "today",
    "v85": "now",
    "v86": "excellent",
    "v87": "eight",
    "v88": "bread",
    "v89": "you speak",
    "v90": "we speak",
    "v91": "I speak",
    "v92": "pasta",
    "v93": "pen",
    "v94": "pens",
    "v95": "for",
    "v96": "because",
    "v97": "perfect",
    "v98": "more",
    "v99": "afternoon",
    "v100": "popcorn",
    "v101": "I bring",
    "v102": "we have lunch",
    "v103": "lunch",
    "v104": "professor",
    "v105": "project",
    "v106": "ready",
    "v107": "this",
    "v108": "this",
    "v109": "here",
    "v110": "to tell",
    "v111": "request",
    "v112": "meeting",
    "v113": "I write",
    "v114": "you are",
    "v115": "it seems",
    "v116": "always",
    "v117": "sound",
    "v118": "tonight",
    "v119": "history",
    "v120": "stories",
    "v121": "you study",
    "v122": "to study",
    "v123": "I study",
    "v124": "on the",
    "v125": "late",
    "v126": "table",
    "v127": "three",
    "v128": "you find",
    "v129": "I find",
    "v130": "office",
    "v131": "a",
    "v132": "we see",
    "v133": "I see",
    "v134": "fast",
    "v135": "wine"
}

phrase_translations = {
    "p1": "Thanks a lot! You are always very kind.",
    "p2": "Thanks! Let's eat this pasta, it looks good.",
    "p3": "I am learning history. It is very interesting tonight.",
    "p4": "Perfect! See you tonight, I can't wait.",
    "p5": "Perfect, see you later! Thanks a lot for the help.",
    "p6": "Yes, I am listening to the lesson and writing with the pen.",
    "p7": "Yes, I am listening to music. It is very beautiful and cheerful.",
    "p8": "Yes, I am waiting in front of the cinema. Don't be late!",
    "p9": "Yes, I am waiting here. Where do you find the forks?",
    "p10": "Yes, I am looking for the email and looking at the documents.",
    "p11": "Yes, I am buying the popcorn. Are you buying the tickets?",
    "p12": "Yes, we are cooking the pasta. I'll buy the wine.",
    "p13": "Yes, I want to buy a faster computer.",
    "p14": "Yes, I want to study together. It's a good idea.",
    "p15": "Yes, I am watching the movie because I love the actors.",
    "p16": "Yes, I am very hungry! What good things are we eating?",
    "p17": "Yes, I am working tonight because the project is important.",
    "p18": "Yes, we talk a lot. I have many stories to tell.",
    "p19": "Yes, I am talking with him this afternoon at three.",
    "p20": "Yes, I am studying a lot because the exam is difficult."
}

def update_json(filename, translations):
    path = os.path.join(base_path, filename)
    with open(path, 'r') as f:
        data = json.load(f)
    for item in data:
        if item['id'] in translations:
            item['english'] = translations[item['id']]
    with open(path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

update_json('verbs_are_verbi_in_are_vocabulary.json', vocab_translations)
update_json('verbs_are_verbi_in_are_phrases.json', phrase_translations)

# Update mini_lessons.json
lessons_path = os.path.join(base_path, 'mini_lessons.json')
with open(lessons_path, 'r') as f:
    lessons_data = json.load(f)

new_titles = ['Study Session', 'Lunch Time', 'Office Work', 'Watching TV', 'General Actions', 'Final Review']
for i, lesson in enumerate(lessons_data['lessons']):
    if i < len(new_titles):
        lesson['title'] = new_titles[i]

with open(lessons_path, 'w') as f:
    json.dump(lessons_data, f, indent=2, ensure_ascii=False)

print("Updates complete.")
