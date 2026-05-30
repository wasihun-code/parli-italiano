import json
import os
import sys

def main(scenario_slug):
    base_path = f"src/data/exports/{scenario_slug}"
    parts = scenario_slug.split('/')
    prefix = "_".join(parts)
    
    try:
        with open(os.path.join(base_path, f"{prefix}_vocabulary.json"), "r", encoding="utf-8") as f:
            vocab = json.load(f)
        with open(os.path.join(base_path, f"{prefix}_phrases.json"), "r", encoding="utf-8") as f:
            phrases = json.load(f)
        with open(os.path.join(base_path, f"{prefix}_sentences.json"), "r", encoding="utf-8") as f:
            sentences = json.load(f)
    except Exception as e:
        print(f"Error loading curriculum files: {e}")
        return False

    # Naive grouping for 6 lessons
    # In a real agent-based system, an LLM would choose which words belong together.
    # Here we simulate the structure.
    
    num_lessons = 6
    lessons = []
    
    v_per_l = len(vocab) // num_lessons
    p_per_l = len(phrases) // num_lessons
    s_per_l = len(sentences) // num_lessons
    
    for i in range(num_lessons):
        l_id = f"l{i+1}"
        
        # Slicing
        v_ids = [v["id"] for v in vocab[i*v_per_l : (i+1)*v_per_l if i < num_lessons-1 else len(vocab)]]
        p_ids = [p["id"] for p in phrases[i*p_per_l : (i+1)*p_per_l if i < num_lessons-1 else len(phrases)]]
        s_ids = [s["id"] for s in sentences[i*s_per_l : (i+1)*s_per_l if i < num_lessons-1 else len(sentences)]]
        
        lessons.append({
            "id": l_id,
            "title": f"Lesson {i+1}", # To be refined by LLM
            "goal": f"Master section {i+1} of the scenario.", # To be refined by LLM
            "sections": [
                {"type": "vocabulary", "exerciseIds": v_ids},
                {"type": "phrase", "exerciseIds": p_ids},
                {"type": "sentence", "exerciseIds": s_ids},
                {"type": "mastery", "exerciseIds": s_ids} # Mastery reuses sentences
            ]
        })

    output = {"lessons": lessons}
    
    with open(os.path.join(base_path, "mini_lessons.json"), "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Created {num_lessons} mini lessons.")
    return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else None
    if not slug: sys.exit(1)
    sys.exit(0 if main(slug) else 1)
