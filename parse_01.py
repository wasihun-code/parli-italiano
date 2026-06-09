import re

with open('docs/curriculum-v4/01_knowledge_graph.md', 'r', encoding='utf-8') as f:
    content = f.read()

words = []
phrases = []

for line in content.split('\n'):
    if line.startswith('|') and not line.startswith('| Italian') and not line.startswith('|---'):
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 4:
            italian = parts[1]
            english = parts[2]
            freq = parts[3]
            if freq.isdigit():
                # could be word or phrase
                if ' ' in italian or "'" in italian:
                    if len(italian) < 40: # rough heuristic
                        pass
                pass

print("We need a better way to separate words from phrases from sentences.")
