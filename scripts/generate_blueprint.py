import json
import re

# 1. Parse 02_dependency_graph.md for mappings
word_map = {}
phrase_map = {}

with open('docs/curriculum-v4/02_dependency_graph.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract words
word_matches = re.finditer(r'\{ "id": "(w_\d+)", "italian": "([^"]+)"', content)
for match in word_matches:
    w_id = match.group(1)
    w_ita = match.group(2).lower().strip()
    word_map[w_ita] = w_id

# Extract phrases
phrase_matches = re.finditer(r'\{\s*"id": "(p_\d+)",\s*"italian": "([^"]+)"', content)
for match in phrase_matches:
    p_id = match.group(1)
    p_ita = match.group(2).lower().strip()
    phrase_map[p_ita] = p_id

# Extract sentences
# Wait, sentences in 03 are like "s_001", we just need to expand them to "s_000001" or keep them as is?
# Let's map s_XXX to s_000XXX
def normalize_id(id_str, prefix):
    # s_001 -> s_000001
    parts = id_str.split('_')
    if len(parts) == 2:
        return f"{prefix}_{parts[1].zfill(6)}"
    return id_str

# 2. Parse 03_micro_lesson_structure.md
blueprint = []

with open('docs/curriculum-v4/03_micro_lesson_structure.md', 'r', encoding='utf-8') as f:
    ml_content = f.read()

# We look for blocks like:
# ### ML_001
# - **W**: ciao, piacere, ...
# - **P**: —
# - **S**: —
# - **T**: —

ml_blocks = re.split(r'### (ML_\d+[a-z]?)', ml_content)

exercise_flows = {
    'word': ['Listen', 'ListenChoose', 'Recall'],
    'phrase': ['Listen', 'Match', 'Recall', 'BuildSentence'],
    'sentence': ['Listen', 'Reading', 'Assembly', 'Dictation'],
    'turn': ['Conversation']
}

for i in range(1, len(ml_blocks), 2):
    ml_id = ml_blocks[i].lower()
    block_text = ml_blocks[i+1]
    
    w_line = re.search(r'- \*\*W\*\*: (.*)', block_text)
    p_line = re.search(r'- \*\*P\*\*: (.*)', block_text)
    s_line = re.search(r'- \*\*S\*\*: (.*)', block_text)
    t_line = re.search(r'- \*\*T\*\*: (.*)', block_text)
    
    entities = []
    
    if w_line and w_line.group(1).strip() != '—' and '(no new words' not in w_line.group(1):
        words = [w.strip().lower() for w in w_line.group(1).split(',')]
        for w in words:
            # Handle special cases in docs
            w_clean = re.sub(r'\(.*?\)', '', w).strip()
            if w_clean in word_map:
                entities.append({
                    "entity_id": word_map[w_clean],
                    "entity_type": "word",
                    "exercise_flow": exercise_flows['word']
                })
            else:
                print(f"Warning: Word not found in map: {w_clean}")
                
    if p_line and p_line.group(1).strip() != '—':
        phrases = [p.strip().lower() for p in p_line.group(1).split(',')]
        for p in phrases:
            if p in phrase_map:
                entities.append({
                    "entity_id": phrase_map[p],
                    "entity_type": "phrase",
                    "exercise_flow": exercise_flows['phrase']
                })
            else:
                print(f"Warning: Phrase not found in map: {p}")
                
    if s_line and s_line.group(1).strip() != '—':
        sentences = [s.strip() for s in s_line.group(1).replace('…', '...').split(',')]
        # Handle ranges like s_011 ... s_020
        final_sentences = []
        for s in sentences:
            if '...' in s:
                start, end = s.split('...')
                start_num = int(start.split('_')[1])
                end_num = int(end.split('_')[1])
                for num in range(start_num, end_num + 1):
                    final_sentences.append(f"s_{str(num).zfill(3)}")
            else:
                final_sentences.append(s)
        
        for s in final_sentences:
            entities.append({
                "entity_id": normalize_id(s, 's'),
                "entity_type": "sentence",
                "exercise_flow": exercise_flows['sentence']
            })
            
    if t_line and t_line.group(1).strip() != '—':
        turns = [t.strip() for t in t_line.group(1).replace('…', '...').split(',')]
        final_turns = []
        for t in turns:
            if '...' in t:
                start, end = t.split('...')
                start_num = int(start.split('_')[1])
                end_num = int(end.split('_')[1])
                for num in range(start_num, end_num + 1):
                    final_turns.append(f"t_{str(num).zfill(3)}")
            else:
                final_turns.append(t)
                
        for t in final_turns:
            entities.append({
                "entity_id": normalize_id(t, 't'),
                "entity_type": "turn",
                "exercise_flow": exercise_flows['turn']
            })
            
    blueprint.append({
        "micro_lesson_id": ml_id,
        "entities": entities
    })

with open('reports/blueprint_dataset.json', 'w', encoding='utf-8') as f:
    json.dump(blueprint, f, indent=2)

print(f"Generated blueprint with {len(blueprint)} micro-lessons.")
