import json

def generate_lessons():
    vocab = json.load(open('src/data/exports/tech/using_a_map_app/tech_using_a_map_app_vocabulary.json'))
    phrases = json.load(open('src/data/exports/tech/using_a_map_app/tech_using_a_map_app_phrases.json'))
    sentences = json.load(open('src/data/exports/tech/using_a_map_app/tech_using_a_map_app_sentences.json'))
    
    v_ids = [v['id'] for v in vocab]
    p_ids = [p['id'] for p in phrases]
    s_ids = [s['id'] for s in sentences]
    
    # We need 6 lessons. Distribute items evenly or at least put some valid items.
    
    lessons = []
    titles = [
        "Finding Locations",
        "Public Transport",
        "Map Navigation",
        "Fixing GPS Issues",
        "Offline Maps",
        "Arriving at Destination"
    ]
    
    # We have 302 words, 40 phrases, 40 sentences.
    # Take slices of 10 vocab, 4 phrases, 4 sentences per lesson.
    for i in range(6):
        v_slice = v_ids[i*10:(i+1)*10]
        p_slice = p_ids[i*4:(i+1)*4]
        s_slice = s_ids[i*4:(i+1)*4]
        
        # fallback if not enough
        if not v_slice: v_slice = v_ids[:5]
        if not p_slice: p_slice = p_ids[:2]
        if not s_slice: s_slice = s_ids[:2]
        
        mastery_slice = [v_slice[-1], p_slice[-1], s_slice[-1]] if (v_slice and p_slice and s_slice) else []
        
        lesson = {
            "id": f"lesson_{i+1}",
            "title": titles[i],
            "sections": [
                {
                    "type": "vocabulary",
                    "items": v_slice
                },
                {
                    "type": "phrase",
                    "items": p_slice
                },
                {
                    "type": "sentence",
                    "items": s_slice
                },
                {
                    "type": "mastery",
                    "items": mastery_slice
                }
            ]
        }
        lessons.append(lesson)
        
    data = {"lessons": lessons}
    with open('src/data/exports/tech/using_a_map_app/mini_lessons.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    generate_lessons()
    print("mini_lessons.json created.")
