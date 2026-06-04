import json

translations = {
    "v4": "to the / at the (plural)",
    "v5": "some",
    "v8": "friends",
    "v11": "years",
    "v13": "goodbye",
    "v17": "company",
    "v18": "band",
    "v19": "very beautiful (feminine)",
    "v23": "warm (feminine)",
    "v24": "I understand",
    "v25": "understood",
    "v26": "house / home",
    "v35": "cinema / movies",
    "v36": "five",
    "v37": "about / approximately",
    "v41": "congratulations / compliments",
    "v42": "composer",
    "v44": "I agree",
    "v47": "creative",
    "v49": "dynamic (feminine)",
    "v51": "fun",
    "v53": "have fun / enjoy yourself",
    "v62": "party",
    "v70": "already",
    "v71": "big / great",
    "v73": "you have",
    "v75": "I imagine",
    "v76": "to learn",
    "v77": "incredible",
    "v84": "you read",
    "v85": "I read",
    "v90": "magical (feminine)",
    "v91": "never / ever",
    "v92": "is missing / lacks",
    "v94": "month",
    "v100": "museum",
    "v104": "not",
    "v107": "today",
    "v108": "every / each",
    "v109": "excellent (feminine)",
    "v116": "they please (I like)",
    "v123": "favorite (masculine)",
    "v127": "unfortunately",
    "v129": "some / a few",
    "v131": "how much",
    "v132": "this (feminine)",
    "v135": "recent",
    "v139": "novels",
    "v140": "choice",
    "v141": "last / past",
    "v145": "evening",
    "v146": "nice / likeable (feminine)",
    "v149": "only / alone",
    "v151": "especially / above all",
    "v154": "you are (staying)",
    "v156": "historical (plural)",
    "v158": "instrument",
    "v159": "you study",
    "v162": "wonderful / stupendous",
    "v165": "I play (instrument) / sound",
    "v169": "type / kind",
    "v170": "three",
    "v171": "too much / too",
    "v173": "your (masculine)",
    "v175": "everything / all",
    "v176": "office",
    "v177": "Uffizi (the gallery)",
    "v182": "Venice",
    "v186": "Vivaldi",
    "v190": "weekend"
}

file_path = "src/data/exports/social/introducing_yourself/social_introducing_yourself_vocabulary.json"

with open(file_path, "r") as f:
    data = json.load(f)

for item in data:
    if item["id"] in translations:
        item["english"] = translations[item["id"]]

with open(file_path, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
