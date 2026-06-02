
import json

file_path = '/home/waseageru/parli-italiano/src/data/exports/culture/theater_evening/culture_theater_evening_vocabulary.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

translations = {
    "v2": "clothing / dress code",
    "v3": "next to / beside",
    "v9": "at the / to the",
    "v15": "ancient / old",
    "v21": "assistance",
    "v30": "drinks / beverages",
    "v34": "bottle",
    "v35": "short / brief",
    "v43": "I understand",
    "v54": "food",
    "v57": "about / approximately",
    "v58": "code",
    "v61": "to consume",
    "v73": "of the",
    "v74": "inside",
    "v77": "must / has to",
    "v80": "behind",
    "v90": "during",
    "v93": "elegance",
    "v100": "to let her pass",
    "v112": "jacket",
    "v115": "appreciated / welcome",
    "v116": "free of charge",
    "v121": "to show / to indicate",
    "v122": "information",
    "v123": "entrance",
    "v124": "beginnings / starts",
    "v127": "to start / to begin",
    "v130": "Italy",
    "v133": "lights",
    "v134": "never / ever",
    "v138": "wonderful / marvelous",
    "v139": "my",
    "v144": "to show",
    "v162": "excellent / very good",
    "v163": "excellent / very good",
    "v166": "particular / special",
    "v167": "passing",
    "v168": "to pass",
    "v180": "to bring",
    "v186": "place / seat",
    "v199": "first",
    "v200": "main",
    "v203": "really / just",
    "v213": "this",
    "v224": "will be",
    "v228": "excuse me",
    "v230": "we sit down",
    "v237": "you are",
    "v238": "lady / Mrs.",
    "v240": "silence",
    "v246": "go out / turn off",
    "v250": "to move (yourselves)",
    "v251": "I move",
    "v254": "been",
    "v256": "historical",
    "v262": "theaters",
    "v263": "theater",
    "v272": "all",
    "v278": "I go",
    "v281": "we see",
    "v286": "view",
    "v290": "time"
}

for item in data:
    if item['id'] in translations:
        item['english'] = translations[item['id']]

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Updated vocabulary translations.")
