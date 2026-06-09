import json
import os
import re

def audit():
    os.makedirs('reports', exist_ok=True)
    report_lines = []
    failures = 0
    
    report_lines.append("# Phase 4.05A: Materialization Forensic Audit\n")
    
    # Load datasets
    try:
        with open('data/curriculum-v4/words.json', 'r') as f: words = json.load(f)
        with open('data/curriculum-v4/phrases.json', 'r') as f: phrases = json.load(f)
        with open('data/curriculum-v4/sentences.json', 'r') as f: sentences = json.load(f)
        with open('data/curriculum-v4/turns.json', 'r') as f: turns = json.load(f)
        with open('data/curriculum-v4/micro_lessons.json', 'r') as f: micro_lessons = json.load(f)
    except Exception as e:
        report_lines.append(f"## Error Loading Datasets\n{e}\nOVERALL STATUS: **FAIL**")
        with open('reports/phase405a_forensic_audit.md', 'w') as f:
            f.write('\n'.join(report_lines))
        return

    # ID maps
    word_ids = {w['id']: w for w in words}
    phrase_ids = {p['id']: p for p in phrases}
    sentence_ids = {s['id']: s for s in sentences}
    turn_ids = {t['id']: t for t in turns}

    # 1. Word Registry
    report_lines.append("## 1. Word Registry")
    word_failures = 0
    if len(words) != 142:
        report_lines.append(f"- FAIL: Expected 142 words, found {len(words)}")
        word_failures += 1
    else:
        report_lines.append(f"- PASS: 142 words exist")
        
    if len(word_ids) != len(words):
        report_lines.append("- FAIL: IDs are not unique")
        word_failures += 1
    else:
        report_lines.append("- PASS: IDs are unique")
        
    italian_words = [w['italian'].lower().strip() for w in words]
    if len(set(italian_words)) != len(words):
        report_lines.append("- FAIL: Duplicate Italian entries found")
        word_failures += 1
    else:
        report_lines.append("- PASS: No duplicate Italian entries")
        
    failures += word_failures
    report_lines.append("")

    # 2. Phrase Registry
    report_lines.append("## 2. Phrase Registry")
    phrase_failures = 0
    if len(phrases) != 78:
        report_lines.append(f"- FAIL: Expected 78 phrases, found {len(phrases)}")
        phrase_failures += 1
    else:
        report_lines.append(f"- PASS: 78 phrases exist")
        
    orphan_deps = []
    for p in phrases:
        for dep in p.get('depends_on_words', []):
            if dep not in word_ids:
                orphan_deps.append((p['id'], dep))
    if len(orphan_deps) > 0:
        report_lines.append(f"- FAIL: {len(orphan_deps)} orphan word dependencies found in phrases")
        for o in orphan_deps:
            report_lines.append(f"  - Phrase {o[0]} depends on missing word {o[1]}")
        phrase_failures += 1
    else:
        report_lines.append("- PASS: Every depends_on_words reference exists")
        
    failures += phrase_failures
    report_lines.append("")

    # 3. Sentence Registry
    report_lines.append("## 3. Sentence Registry")
    sentence_failures = 0
    if len(sentences) != 80:
        report_lines.append(f"- FAIL: Expected 80 sentences, found {len(sentences)}")
        sentence_failures += 1
    else:
        report_lines.append(f"- PASS: 80 sentences exist")
        
    orphan_s_deps = []
    for s in sentences:
        for dep in s.get('depends_on_words', []):
            if dep not in word_ids: orphan_s_deps.append((s['id'], dep, 'word'))
        for dep in s.get('depends_on_phrases', []):
            if dep not in phrase_ids: orphan_s_deps.append((s['id'], dep, 'phrase'))
            
    if len(orphan_s_deps) > 0:
        report_lines.append(f"- FAIL: {len(orphan_s_deps)} orphan dependencies found in sentences")
        for o in orphan_s_deps:
            report_lines.append(f"  - Sentence {o[0]} depends on missing {o[2]} {o[1]}")
        sentence_failures += 1
    else:
        report_lines.append("- PASS: Every depends_on_words and depends_on_phrases reference exists")

    failures += sentence_failures
    report_lines.append("")

    # 4. Turn Registry
    report_lines.append("## 4. Turn Registry")
    turn_failures = 0
    if len(turns) != 80:
        report_lines.append(f"- FAIL: Expected 80 turns, found {len(turns)}")
        turn_failures += 1
    else:
        report_lines.append(f"- PASS: 80 turns exist")
        
    orphan_t_deps = []
    for t in turns:
        if t['sentence_id'] not in sentence_ids:
            orphan_t_deps.append((t['id'], t['sentence_id']))
            
    if len(orphan_t_deps) > 0:
        report_lines.append(f"- FAIL: {len(orphan_t_deps)} orphan sentence_id dependencies found in turns")
        for o in orphan_t_deps:
            report_lines.append(f"  - Turn {o[0]} depends on missing sentence {o[1]}")
        turn_failures += 1
    else:
        report_lines.append("- PASS: Every sentence_id exists")

    failures += turn_failures
    report_lines.append("")

    # 5. Micro Lessons
    report_lines.append("## 5. Micro Lessons")
    ml_failures = 0
    literal_strings = []
    missing_refs = []
    
    intro_map = {}
    
    for idx, ml in enumerate(micro_lessons):
        for w in ml.get('new_words', []):
            if not w.startswith('w_'): literal_strings.append((ml['id'], w))
            if w not in word_ids: missing_refs.append((ml['id'], w))
            if w not in intro_map: intro_map[w] = idx
            
        for p in ml.get('new_phrases', []):
            if not p.startswith('p_'): literal_strings.append((ml['id'], p))
            if p not in phrase_ids: missing_refs.append((ml['id'], p))
            if p not in intro_map: intro_map[p] = idx
            
        for s in ml.get('new_sentences', []):
            if not s.startswith('s_'): literal_strings.append((ml['id'], s))
            if s not in sentence_ids: missing_refs.append((ml['id'], s))
            if s not in intro_map: intro_map[s] = idx
            
        for t in ml.get('new_turns', []):
            if not t.startswith('t_'): literal_strings.append((ml['id'], t))
            if t not in turn_ids: missing_refs.append((ml['id'], t))
            if t not in intro_map: intro_map[t] = idx

    if len(literal_strings) > 0:
        report_lines.append(f"- FAIL: {len(literal_strings)} literal Italian strings found instead of IDs")
        for ls in literal_strings[:5]:
            report_lines.append(f"  - ML {ls[0]} has literal string '{ls[1]}'")
        if len(literal_strings) > 5: report_lines.append("  - ...")
        ml_failures += 1
    else:
        report_lines.append("- PASS: IDs only, no literal Italian strings")
        
    if len(missing_refs) > 0:
        report_lines.append(f"- FAIL: {len(missing_refs)} referenced entities do not exist")
        for mr in missing_refs[:5]:
            report_lines.append(f"  - ML {mr[0]} references missing entity '{mr[1]}'")
        if len(missing_refs) > 5: report_lines.append("  - ...")
        ml_failures += 1
    else:
        report_lines.append("- PASS: Every referenced entity exists")
        
    failures += ml_failures
    report_lines.append("")

    # 6. Chronological Integrity
    report_lines.append("## 6. Chronological Integrity")
    chron_violations = []
    
    for p in phrases:
        if p['id'] in intro_map:
            p_idx = intro_map[p['id']]
            for dep in p.get('depends_on_words', []):
                if dep in intro_map and intro_map[dep] > p_idx:
                    chron_violations.append((p['id'], dep, 'word', 'introduced late'))
                elif dep not in intro_map:
                    chron_violations.append((p['id'], dep, 'word', 'never introduced'))
                    
    for s in sentences:
        if s['id'] in intro_map:
            s_idx = intro_map[s['id']]
            for dep in s.get('depends_on_words', []):
                if dep in intro_map and intro_map[dep] > s_idx: 
                    chron_violations.append((s['id'], dep, 'word', 'introduced late'))
                elif dep not in intro_map: 
                    chron_violations.append((s['id'], dep, 'word', 'never introduced'))
            for dep in s.get('depends_on_phrases', []):
                if dep in intro_map and intro_map[dep] > s_idx: 
                    chron_violations.append((s['id'], dep, 'phrase', 'introduced late'))
                elif dep not in intro_map: 
                    chron_violations.append((s['id'], dep, 'phrase', 'never introduced'))
                
    for t in turns:
        if t['id'] in intro_map:
            t_idx = intro_map[t['id']]
            dep = t['sentence_id']
            if dep in intro_map and intro_map[dep] > t_idx: 
                chron_violations.append((t['id'], dep, 'sentence', 'introduced late'))
            elif dep not in intro_map: 
                chron_violations.append((t['id'], dep, 'sentence', 'never introduced'))

    if len(chron_violations) > 0:
        report_lines.append(f"- FAIL: {len(chron_violations)} chronological dependency violations found")
        for cv in chron_violations[:10]:
            report_lines.append(f"  - Entity {cv[0]} depends on {cv[2]} {cv[1]} which is {cv[3]}")
        if len(chron_violations) > 10: report_lines.append("  - ...")
        failures += 1
    else:
        report_lines.append("- PASS: Dependencies introduced chronologically")
        
    report_lines.append("")

    # 7. Coverage Integrity
    report_lines.append("## 7. Coverage Integrity")
    uncovered_entities = []
    
    for w in word_ids:
        if w not in intro_map: uncovered_entities.append(w)
    for p in phrase_ids:
        if p not in intro_map: uncovered_entities.append(p)
    for s in sentence_ids:
        if s not in intro_map: uncovered_entities.append(s)
    for t in turn_ids:
        if t not in intro_map: uncovered_entities.append(t)
        
    if len(uncovered_entities) > 0:
        report_lines.append(f"- FAIL: {len(uncovered_entities)} entities do not appear in any micro lesson")
        for ue in uncovered_entities[:10]:
            report_lines.append(f"  - Entity {ue} is missing from all lessons")
        if len(uncovered_entities) > 10: report_lines.append("  - ...")
        failures += 1
    else:
        report_lines.append("- PASS: Every entity appears in at least one lesson")

    report_lines.append("")
    
    # 8. Determinism
    report_lines.append("## 8. Determinism")
    if len(literal_strings) > 0 or len(missing_refs) > 0:
        report_lines.append("- FAIL: Text matching or unresolvable IDs required")
        failures += 1
    else:
        report_lines.append("- PASS: No text matching required anywhere. Everything resolvable through IDs.")

    report_lines.append("\n## OVERALL STATUS")
    if failures == 0:
        report_lines.append("**PASS**")
    else:
        report_lines.append(f"**FAIL** ({failures} checks failed)")

    with open('reports/phase405a_forensic_audit.md', 'w') as f:
        f.write('\n'.join(report_lines))

if __name__ == '__main__':
    audit()
