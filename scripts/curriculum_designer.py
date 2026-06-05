import json
import os
import sys

def chunk_list(lst, n):
    if not lst:
        return [[] for _ in range(n)]
    chunk_size = len(lst) // n
    remainder = len(lst) % n
    chunks = []
    start = 0
    for i in range(n):
        end = start + chunk_size + (1 if i < remainder else 0)
        chunks.append(lst[start:end])
        start = end
    return chunks

def main(scenario_slug):
    base_path = f"src/data/exports/{scenario_slug}"
    prefix = scenario_slug.replace("/", "_")
    
    # 1. Read existing mini_lessons.json to preserve titles/goals if possible
    lessons_path = os.path.join(base_path, "mini_lessons.json")
    existing_lessons = []
    if os.path.exists(lessons_path):
        try:
            with open(lessons_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                existing_lessons = data.get("lessons", data) if isinstance(data, dict) else data
        except Exception:
            pass

    # Ensure we have exactly 6 templates
    templates = []
    for i in range(6):
        if i < len(existing_lessons) and isinstance(existing_lessons[i], dict):
            templates.append({
                "id": existing_lessons[i].get("id", f"l{i+1}"),
                "title": existing_lessons[i].get("title", f"Lesson {i+1}"),
                "goal": existing_lessons[i].get("goal", "Master this topic.")
            })
        else:
            templates.append({
                "id": f"l{i+1}",
                "title": f"Lesson {i+1}",
                "goal": "Master this topic."
            })

    # 2. Read extracted linguistic files
    def read_ids(filename):
        path = os.path.join(base_path, filename)
        if not os.path.exists(path): return []
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [item["id"] for item in data if "id" in item]

    vocab_ids = read_ids(f"{prefix}_vocabulary.json")
    phrase_ids = read_ids(f"{prefix}_phrases.json")
    sentence_ids = read_ids(f"{prefix}_sentences.json")

    # 3. Distribute across 6 lessons
    v_chunks = chunk_list(vocab_ids, 6)
    p_chunks = chunk_list(phrase_ids, 6)
    s_chunks = chunk_list(sentence_ids, 6)

    new_lessons = []
    for i in range(6):
        lesson = templates[i]
        sections = []
        if v_chunks[i]:
            sections.append({"type": "vocabulary", "exerciseIds": v_chunks[i]})
        if p_chunks[i]:
            sections.append({"type": "phrase", "exerciseIds": p_chunks[i]})
        if s_chunks[i]:
            sections.append({"type": "sentence", "exerciseIds": s_chunks[i]})
            sections.append({"type": "mastery", "exerciseIds": s_chunks[i]})
            
        lesson["sections"] = sections
        new_lessons.append(lesson)

    # 4. Save
    output_data = {"lessons": new_lessons}
    with open(lessons_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
        
    print(f"Created 6 mini lessons for {scenario_slug} with 100% deterministic coverage.")
    print(f"Distributed {len(vocab_ids)} vocab, {len(phrase_ids)} phrases, {len(sentence_ids)} sentences.")
    return True

if __name__ == "__main__":
    slug = sys.argv[1] if len(sys.argv) > 1 else None
    if slug:
        sys.exit(0 if main(slug) else 1)
