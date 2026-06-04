import json
import re

def tokenize(text):
    text = text.lower()
    text = text.replace("'", " ")
    text = re.sub(r'[^\w\sàèìòùé]', '', text)
    return {w for w in text.split() if len(w) > 2 and not w.isdigit()}

with open('src/data/scenarios/workstudy/email_follow_up/conversations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

conversations = data['conversations']

conv_words = set()
conv_phrases = set()
conv_sentences = set()

for conv in conversations:
    for msg in conv.get("messages", []):
        text = msg.get("text")
        if text and msg.get("role") == "host":
            it_text = text.strip()
            conv_sentences.add((it_text, msg.get("english")))
            conv_words.update(tokenize(it_text))
        
        for choice in msg.get("choices", []):
            if choice.get("isCorrect"):
                it_choice = choice["text"].strip()
                # Need english for choices too? conversations.json doesn't have it for choices
                # But phrases.json needs english. 
                # I'll need to map it.
                conv_phrases.add(it_choice)
                conv_words.update(tokenize(it_choice))

# Sort to be deterministic
vocab_list = sorted(list(conv_words))
phrases_list = sorted(list(conv_phrases))
sentences_list = sorted(list(conv_sentences), key=lambda x: x[0])

# We need english translations for vocab. 
# For now I'll just put placeholders or try to find them.
# Better: use Agent 6 (Translation Specialist) later, but I need them now for the files.

# I'll output them as JSON.
with open('extracted_vocab.json', 'w', encoding='utf-8') as f:
    json.dump(vocab_list, f, ensure_ascii=False, indent=2)

with open('extracted_phrases.json', 'w', encoding='utf-8') as f:
    json.dump(phrases_list, f, ensure_ascii=False, indent=2)

with open('extracted_sentences.json', 'w', encoding='utf-8') as f:
    json.dump(sentences_list, f, ensure_ascii=False, indent=2)
