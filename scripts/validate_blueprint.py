import json

with open('reports/blueprint_dataset.json', 'r', encoding='utf-8') as f:
    blueprint = json.load(f)

dependency_report = {
    "status": "PASS",
    "failures": []
}

duplicate_report = {
    "status": "PASS",
    "duplicates": []
}

coverage_report = {
    "total_words": 0,
    "total_phrases": 0,
    "total_sentences": 0,
    "total_turns": 0
}

conversation_readiness_report = {
    "status": "PASS",
    "failures": []
}

seen_entities = set()
introduced_sentences = set()

# Validate
for ml in blueprint:
    ml_id = ml["micro_lesson_id"]
    entities = ml["entities"]
    
    # 4. Word before Phrase, 5. Phrase before Sentence, 6. Sentence before Turn
    order_map = {"word": 1, "phrase": 2, "sentence": 3, "turn": 4}
    current_max_order = 0
    
    for entity in entities:
        e_id = entity["entity_id"]
        e_type = entity["entity_type"]
        
        # Coverage
        if e_type == "word": coverage_report["total_words"] += 1
        elif e_type == "phrase": coverage_report["total_phrases"] += 1
        elif e_type == "sentence": coverage_report["total_sentences"] += 1
        elif e_type == "turn": coverage_report["total_turns"] += 1
        
        # Duplicates
        if e_id in seen_entities:
            duplicate_report["status"] = "FAIL"
            duplicate_report["duplicates"].append({
                "entity_id": e_id,
                "lesson": ml_id,
                "message": f"Entity {e_id} introduced more than once."
            })
        seen_entities.add(e_id)
        
        # Order within ML
        e_order = order_map[e_type]
        if e_order < current_max_order:
            dependency_report["status"] = "FAIL"
            dependency_report["failures"].append({
                "lesson": ml_id,
                "entity_id": e_id,
                "message": f"Entity of type {e_type} appears after a higher-order entity."
            })
        current_max_order = max(current_max_order, e_order)
        
        # Readiness
        if e_type == "sentence":
            introduced_sentences.add(e_id)
        elif e_type == "turn":
            # Assuming t_000001 corresponds to s_000001
            # We check if the corresponding sentence was introduced
            corr_s_id = e_id.replace("t_", "s_")
            if corr_s_id not in introduced_sentences:
                conversation_readiness_report["status"] = "FAIL"
                conversation_readiness_report["failures"].append({
                    "lesson": ml_id,
                    "turn_id": e_id,
                    "message": f"Turn {e_id} introduced before its corresponding sentence {corr_s_id}."
                })

# Write reports
with open('reports/phase4_dependency_validation.json', 'w') as f:
    json.dump(dependency_report, f, indent=2)

with open('reports/phase4_duplicate_introduction.json', 'w') as f:
    json.dump(duplicate_report, f, indent=2)

with open('reports/phase4_coverage.json', 'w') as f:
    json.dump(coverage_report, f, indent=2)

with open('reports/phase4_conversation_readiness.json', 'w') as f:
    json.dump(conversation_readiness_report, f, indent=2)

print("Validation reports generated successfully.")
