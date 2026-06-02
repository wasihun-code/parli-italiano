import json

vocab_count = 160
phrase_count = 20
sentence_count = 44

titles = ['At the Shop', 'Postcards & Magnets', 'Local Crafts', 'Asking for Gifts', 'Prices', 'Final Purchase']

lessons = []
v_idx = 1
p_idx = 1
s_idx = 1

for i, title in enumerate(titles):
    v_end = v_idx + (vocab_count // 6) + (1 if i < (vocab_count % 6) else 0)
    p_end = p_idx + (phrase_count // 6) + (1 if i < (phrase_count % 6) else 0)
    s_end = s_idx + (sentence_count // 6) + (1 if i < (sentence_count % 6) else 0)
    
    sections = []
    
    v_ids = [f"v{j}" for j in range(v_idx, v_end)]
    if v_ids:
        sections.append({"type": "vocabulary", "exerciseIds": v_ids})
        
    p_ids = [f"p{j}" for j in range(p_idx, p_end)]
    if p_ids:
        sections.append({"type": "phrase", "exerciseIds": p_ids})
        
    s_ids = [f"s{j}" for j in range(s_idx, s_end)]
    if s_ids:
        sections.append({"type": "sentence", "exerciseIds": s_ids})
        
    lessons.append({
        "id": f"l{i+1}",
        "title": title,
        "goal": f"Learn {title.lower()}",
        "sections": sections
    })
    
    v_idx = v_end
    p_idx = p_end
    s_idx = s_end

with open("src/data/exports/shopping/souvenir_shop/mini_lessons.json", "w") as f:
    json.dump({"lessons": lessons}, f, indent=2)
print("mini_lessons.json generated")
