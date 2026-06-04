import json

files = [
    "src/data/exports/workstudy/job_interview/workstudy_job_interview_vocabulary.json",
    "src/data/exports/workstudy/job_interview/workstudy_job_interview_phrases.json",
    "src/data/exports/workstudy/job_interview/workstudy_job_interview_sentences.json"
]

missing = []

for f in files:
    try:
        with open(f, 'r') as fp:
            data = json.load(fp)
            for item in data:
                if not item.get("english"):
                    missing.append({"id": item["id"], "italian": item["italian"]})
    except:
        pass

print(f"Missing count: {len(missing)}")
with open("missing.json", "w") as fp:
    json.dump(missing, fp, indent=2, ensure_ascii=False)
