import json
import re
import os

def run_audit():
    os.makedirs('reports', exist_ok=True)
    # 1. Load Data
    with open('docs/curriculum-v4/02_dependency_graph.md', 'r') as f:
        content_02 = f.read()
    with open('docs/curriculum-v4/03_micro_lesson_structure.md', 'r') as f:
        content_03 = f.read()

    blocks = re.findall(r'```json\n(.*?)\n```', content_02, re.DOTALL)
    
    registry_words = []
    registry_phrases = []
    registry_sentences = []
    registry_turns = []

    for block in blocks:
        try:
            data = json.loads(block)
            if not isinstance(data, list) or len(data) == 0: continue
            first_id = data[0].get('id', '')
            if first_id.startswith('w_'): registry_words.extend(data)
            elif first_id.startswith('p_'): registry_phrases.extend(data)
            elif first_id.startswith('s_'): registry_sentences.extend(data)
            elif first_id.startswith('t_'): registry_turns.extend(data)
        except:
            pass

    reg_word_strings = {w['italian'].lower().strip(): w['id'] for w in registry_words}
    reg_phrase_strings = {p['italian'].lower().strip(): p['id'] for p in registry_phrases}
    
    reg_word_ids = {w['id'] for w in registry_words}
    reg_phrase_ids = {p['id'] for p in registry_phrases}
    reg_sentence_ids = {s['id'] for s in registry_sentences}
    reg_turn_ids = {t['id'] for t in registry_turns}

    mls = re.split(r'### (ML_\d+[a-z]?)', content_03)
    ml_data = []
    for i in range(1, len(mls), 2):
        ml_id = mls[i].strip()
        block = mls[i+1]
        
        w_line = re.search(r'- \*\*W\*\*: (.*)', block)
        p_line = re.search(r'- \*\*P\*\*: (.*)', block)
        s_line = re.search(r'- \*\*S\*\*: (.*)', block)
        t_line = re.search(r'- \*\*T\*\*: (.*)', block)
        
        words = [w.strip() for w in w_line.group(1).split(',')] if w_line and w_line.group(1).strip() != '—' and '(no new words' not in w_line.group(1) else []
        phrases = [p.strip() for p in p_line.group(1).split(',')] if p_line and p_line.group(1).strip() != '—' else []
        
        sentences = []
        if s_line and s_line.group(1).strip() != '—':
            for s in s_line.group(1).replace('…', '...').split(','):
                s = s.strip()
                if '...' in s:
                    start_num = int(s.split('...')[0].split('_')[1])
                    end_num = int(s.split('...')[1].split('_')[1])
                    for n in range(start_num, end_num + 1): sentences.append(f"s_{str(n).zfill(3)}")
                else: sentences.append(s)
                
        turns = []
        if t_line and t_line.group(1).strip() != '—':
            for t in t_line.group(1).replace('…', '...').split(','):
                t = t.strip()
                if '...' in t:
                    start_num = int(t.split('...')[0].split('_')[1])
                    end_num = int(t.split('...')[1].split('_')[1])
                    for n in range(start_num, end_num + 1): turns.append(f"t_{str(n).zfill(3)}")
                else: turns.append(t)
                
        ml_data.append({"id": ml_id, "words": words, "phrases": phrases, "sentences": sentences, "turns": turns})

    # A01 Word Coverage
    missing_words = []
    ref_words_mapped = set()
    for ml in ml_data:
        for w in ml['words']:
            w_clean = re.sub(r'\(.*?\)', '', w).strip().lower()
            if w_clean not in reg_word_strings:
                missing_words.append({"lesson": ml['id'], "word": w})
            else:
                ref_words_mapped.add(reg_word_strings[w_clean])
    
    unexpected_words = list(reg_word_ids - ref_words_mapped)
    word_coverage = len(ref_words_mapped) / len(reg_word_ids) * 100 if len(reg_word_ids) > 0 else 0

    # A02 Phrase Coverage
    missing_phrases = []
    ref_phrases_mapped = set()
    for ml in ml_data:
        for p in ml['phrases']:
            p_clean = p.lower().strip()
            if p_clean not in reg_phrase_strings:
                missing_phrases.append({"lesson": ml['id'], "phrase": p})
            else:
                ref_phrases_mapped.add(reg_phrase_strings[p_clean])
                
    unexpected_phrases = list(reg_phrase_ids - ref_phrases_mapped)
    phrase_coverage = len(ref_phrases_mapped) / len(reg_phrase_ids) * 100 if len(reg_phrase_ids) > 0 else 0

    # A03 Sentence Coverage
    missing_sentences = []
    ref_sentences_mapped = set()
    for ml in ml_data:
        for s in ml['sentences']:
            s_full = f"s_{s.split('_')[1].zfill(6)}"
            if s_full not in reg_sentence_ids:
                missing_sentences.append({"lesson": ml['id'], "sentence_id": s, "expected_full_id": s_full})
            else:
                ref_sentences_mapped.add(s_full)
                
    unexpected_sentences = list(reg_sentence_ids - ref_sentences_mapped)
    sentence_coverage = len(ref_sentences_mapped) / len(reg_sentence_ids) * 100 if len(reg_sentence_ids) > 0 else 0

    # A04 Turn Coverage
    missing_turns = []
    ref_turns_mapped = set()
    for ml in ml_data:
        for t in ml['turns']:
            t_full = f"t_{t.split('_')[1].zfill(6)}"
            if t_full not in reg_turn_ids:
                missing_turns.append({"lesson": ml['id'], "turn_id": t, "expected_full_id": t_full})
            else:
                ref_turns_mapped.add(t_full)
                
    unexpected_turns = list(reg_turn_ids - ref_turns_mapped)
    turn_coverage = len(ref_turns_mapped) / len(reg_turn_ids) * 100 if len(reg_turn_ids) > 0 else 0

    # A05 Dependency Consistency Audit
    dependency_violations = []
    for p in registry_phrases:
        for dep in p.get('depends_on_words', []):
            if dep not in reg_word_ids:
                dependency_violations.append({"entity": p['id'], "type": "phrase", "missing_dependency": dep})
    for s in registry_sentences:
        for dep in s.get('depends_on_words', []):
            if dep not in reg_word_ids:
                dependency_violations.append({"entity": s['id'], "type": "sentence", "missing_dependency": dep})
        for dep in s.get('depends_on_phrases', []):
            if dep not in reg_phrase_ids:
                dependency_violations.append({"entity": s['id'], "type": "sentence", "missing_dependency": dep})
    for t in registry_turns:
        for dep in t.get('depends_on_sentences', []):
            if dep not in reg_sentence_ids:
                dependency_violations.append({"entity": t['id'], "type": "turn", "missing_dependency": dep})

    # A06 Micro Lesson Consistency Audit
    duplicate_entities = []
    seen = set()
    introduced_order = {}
    ml_order_index = 0
    
    # We map what ML index each entity was introduced
    for ml in ml_data:
        ml_order_index += 1
        for w in ml['words']:
            w_clean = re.sub(r'\(.*?\)', '', w).strip().lower()
            if w_clean in reg_word_strings:
                w_id = reg_word_strings[w_clean]
                if w_id in seen:
                    duplicate_entities.append({"lesson": ml['id'], "entity_id": w_id, "type": "word"})
                seen.add(w_id)
                if w_id not in introduced_order: introduced_order[w_id] = ml_order_index
        for p in ml['phrases']:
            p_clean = p.lower().strip()
            if p_clean in reg_phrase_strings:
                p_id = reg_phrase_strings[p_clean]
                if p_id in seen:
                    duplicate_entities.append({"lesson": ml['id'], "entity_id": p_id, "type": "phrase"})
                seen.add(p_id)
                if p_id not in introduced_order: introduced_order[p_id] = ml_order_index
        for s in ml['sentences']:
            s_full = f"s_{s.split('_')[1].zfill(6)}"
            if s_full in seen:
                duplicate_entities.append({"lesson": ml['id'], "entity_id": s_full, "type": "sentence"})
            seen.add(s_full)
            if s_full not in introduced_order: introduced_order[s_full] = ml_order_index
        for t in ml['turns']:
            t_full = f"t_{t.split('_')[1].zfill(6)}"
            if t_full in seen:
                duplicate_entities.append({"lesson": ml['id'], "entity_id": t_full, "type": "turn"})
            seen.add(t_full)
            if t_full not in introduced_order: introduced_order[t_full] = ml_order_index

    # Check dependency ordering (Did it appear before dependencies?)
    for p in registry_phrases:
        if p['id'] in introduced_order:
            p_ml = introduced_order[p['id']]
            for dep in p.get('depends_on_words', []):
                if dep in introduced_order and introduced_order[dep] > p_ml:
                    dependency_violations.append({"entity": p['id'], "type": "phrase", "dependency_introduced_late": dep})
                elif dep not in introduced_order:
                    dependency_violations.append({"entity": p['id'], "type": "phrase", "dependency_never_introduced": dep})

    for s in registry_sentences:
        if s['id'] in introduced_order:
            s_ml = introduced_order[s['id']]
            for dep in s.get('depends_on_words', []) + s.get('depends_on_phrases', []):
                if dep in introduced_order and introduced_order[dep] > s_ml:
                    dependency_violations.append({"entity": s['id'], "type": "sentence", "dependency_introduced_late": dep})
                elif dep not in introduced_order:
                    dependency_violations.append({"entity": s['id'], "type": "sentence", "dependency_never_introduced": dep})

    # A07 Blueprint Determinism Audit
    determinism_violations = []
    # Any text matching is a defect.
    for ml in ml_data:
        for w in ml['words']:
            determinism_violations.append({"lesson": ml['id'], "type": "text_matching_required", "entity": "word", "value": w})
        for p in ml['phrases']:
            determinism_violations.append({"lesson": ml['id'], "type": "text_matching_required", "entity": "phrase", "value": p})
        for s in ml['sentences']:
            determinism_violations.append({"lesson": ml['id'], "type": "id_padding_required", "entity": "sentence", "value": s})
        for t in ml['turns']:
            determinism_violations.append({"lesson": ml['id'], "type": "id_padding_required", "entity": "turn", "value": t})

    # Save JSON reports
    with open('reports/missing_words.json', 'w') as f:
        json.dump({"missing": missing_words, "unexpected": unexpected_words, "coverage": word_coverage}, f, indent=2)
    with open('reports/missing_phrases.json', 'w') as f:
        json.dump({"missing": missing_phrases, "unexpected": unexpected_phrases, "coverage": phrase_coverage}, f, indent=2)
    with open('reports/missing_sentences.json', 'w') as f:
        json.dump({"missing": missing_sentences, "expected_full_ids_missing": missing_sentences, "unexpected": unexpected_sentences, "coverage": sentence_coverage}, f, indent=2)
    with open('reports/missing_turns.json', 'w') as f:
        json.dump({"missing": missing_turns, "expected_full_ids_missing": missing_turns, "unexpected": unexpected_turns, "coverage": turn_coverage}, f, indent=2)
    with open('reports/dependency_violations.json', 'w') as f:
        json.dump(dependency_violations, f, indent=2)
    with open('reports/duplicate_entities.json', 'w') as f:
        json.dump(duplicate_entities, f, indent=2)
    with open('reports/determinism_violations.json', 'w') as f:
        json.dump(determinism_violations, f, indent=2)

    # Generate Markdown Report
    passed = (len(missing_words) == 0 and len(missing_phrases) == 0 and len(missing_sentences) == 0 and 
              len(missing_turns) == 0 and len(dependency_violations) == 0 and len(duplicate_entities) == 0 and 
              len(determinism_violations) == 0)

    md = f"""# Phase 4.1A: Blueprint Certification Audit

## Overall Status: **{'PASS' if passed else 'FAIL'}**

### A01 Registry Coverage Audit (Words)
- Missing Words: {len(missing_words)}
- Unexpected Words: {len(unexpected_words)}
- Coverage: {word_coverage:.2f}%

### A02 Phrase Coverage Audit
- Missing Phrases: {len(missing_phrases)}
- Unexpected Phrases: {len(unexpected_phrases)}
- Coverage: {phrase_coverage:.2f}%

### A03 Sentence Coverage Audit
- Missing Sentences: {len(missing_sentences)}
- Unexpected Sentences: {len(unexpected_sentences)}
- Coverage: {sentence_coverage:.2f}%

### A04 Turn Coverage Audit
- Missing Turns: {len(missing_turns)}
- Unexpected Turns: {len(unexpected_turns)}
- Coverage: {turn_coverage:.2f}%

### A05 Dependency Consistency Audit
- Dependency Violations: {len([v for v in dependency_violations if 'missing_dependency' in v])}

### A06 Micro Lesson Consistency Audit
- Duplicate Introductions: {len(duplicate_entities)}
- Chronological Dependency Violations: {len([v for v in dependency_violations if 'dependency_introduced_late' in v or 'dependency_never_introduced' in v])}

### A07 Blueprint Determinism Audit
- Determinism Violations: {len(determinism_violations)}

## Detailed Finding Summary
The documentation shows massive structural defects:
1. **Determinism:** `03_micro_lesson_structure.md` introduces words and phrases using literal Italian text strings instead of UUIDs. This forces any engine to use text-matching, which is prohibited. Furthermore, Sentences and Turns are written with shorthand IDs (`s_001` instead of `s_000001`).
2. **Incomplete Registries:** `02_dependency_graph.md` is truncated for brevity. It references 142 words, 78 phrases, 80 sentences, and 80 turns, but explicitly defines only a handful in the JSON blocks (e.g., only 12 sentences are defined). Therefore, cross-referencing fails, resulting in extremely poor coverage metrics.
3. **Dependency Integrity:** Because the registries are truncated in the document, many dependencies are fundamentally unresolvable.
"""

    with open('reports/curriculum_v4_certification.md', 'w') as f:
        f.write(md)

run_audit()
