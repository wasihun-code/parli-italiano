import json

def generate_mini_lessons():
    # Divide 264 words into 6 groups of ~44
    # Divide 40 phrases into 6 groups of ~6-7
    # Divide 40 sentences into 6 groups of ~6-7
    
    lessons = []
    titles = [
        "Document Check",
        "Entry Interview",
        "Finding Luggage",
        "Baggage Issues",
        "Lost and Found",
        "City Transport"
    ]
    goals = [
        "Present your passport and boarding pass correctly.",
        "Answer questions about your trip and stay.",
        "Locate the correct baggage carousel and belt.",
        "Handle baggage collection and help offers.",
        "Report missing items to the appropriate office.",
        "Find the fastest or cheapest way to the city center."
    ]
    
    v_per_lesson = 44
    p_per_lesson = 6
    s_per_lesson = 6
    
    for i in range(6):
        v_start = i * v_per_lesson + 1
        v_end = min((i + 1) * v_per_lesson, 264)
        v_ids = [f"v{j}" for j in range(v_start, v_end + 1)]
        
        p_start = i * p_per_lesson + 1
        p_end = min((i + 1) * p_per_lesson, 40)
        p_ids = [f"p{j}" for j in range(p_start, p_end + 1)]
        
        s_start = i * s_per_lesson + 1
        s_end = min((i + 1) * s_per_lesson, 40)
        s_ids = [f"s{j}" for j in range(s_start, s_end + 1)]
        
        lessons.append({
            "id": f"l{i+1}",
            "title": titles[i],
            "goal": goals[i],
            "sections": [
                {
                    "type": "vocabulary",
                    "exerciseIds": v_ids
                },
                {
                    "type": "phrases",
                    "exerciseIds": p_ids
                },
                {
                    "type": "sentences",
                    "exerciseIds": s_ids
                }
            ]
        })
    
    output = {"lessons": lessons}
    
    with open('src/data/exports/travel/airport_arrival/mini_lessons.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_mini_lessons()
