import re
import json

with open('docs/curriculum-v4/02_dependency_graph.md', 'r') as f:
    c = f.read()

blocks = re.findall(r'```json\n(.*?)\n```', c, re.DOTALL)
words = []
phrases = []
sentences = []
turns = []

for b in blocks:
    try:
        data = json.loads(b)
        if len(data) > 0:
            if 'w_' in data[0]['id']: words.extend(data)
            if 'p_' in data[0]['id']: phrases.extend(data)
            if 's_' in data[0]['id']: sentences.extend(data)
            if 't_' in data[0]['id']: turns.extend(data)
    except:
        pass

print(f"Parsed from 02: Words: {len(words)}, Phrases: {len(phrases)}, Sentences: {len(sentences)}, Turns: {len(turns)}")
