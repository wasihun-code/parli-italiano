import json
import os

stories_path = '/home/waseageru/parli-italiano/src/data/stories.json'
distractors_path = '/home/waseageru/parli-italiano/src/data/stories_distractors.json'

def validate():
    with open(stories_path, 'r') as f:
        data = json.load(f)
    with open(distractors_path, 'r') as f:
        distractors = json.load(f)

    stories = data.get('stories', [])
    expected_distractor_keys = []

    for story in stories:
        title = story['title']
        for j in range(len(story['overall_questions'])):
            expected_distractor_keys.append(f"{title}_overall_{j}")

        for p_idx, part in enumerate(story['parts']):
            for pg_idx, page in enumerate(part['pages']):
                p_num = part.get('part_number', p_idx + 1)
                pg_num = page.get('page_number', pg_idx + 1)
                if 'questions' in page and 'comprehension' in page['questions']:
                    for c_idx in range(len(page['questions']['comprehension'])):
                        expected_distractor_keys.append(f"{title}_{p_num}_{pg_num}_{c_idx}")

    missing_keys = [k for k in expected_distractor_keys if k not in distractors]
    extra_keys = [k for k in distractors if k not in expected_distractor_keys]

    if missing_keys:
        print(f"Missing keys: {missing_keys}")
    else:
        print("No missing keys.")

    if extra_keys:
        print(f"Extra keys: {extra_keys}")
    else:
        print("No extra keys.")

if __name__ == "__main__":
    validate()
