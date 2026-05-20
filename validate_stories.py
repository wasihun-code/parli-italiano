import json
import os

stories_path = '/home/waseageru/parli-italiano/src/data/stories.json'
distractors_path = '/home/waseageru/parli-italiano/src/data/stories_distractors.json'

def validate():
    if not os.path.exists(stories_path):
        print(f"Error: {stories_path} not found")
        return
    if not os.path.exists(distractors_path):
        print(f"Error: {distractors_path} not found")
        return

    with open(stories_path, 'r') as f:
        data = json.load(f)

    stories = data.get('stories', [])
    
    errors = []
    
    # 1. Verify exactly 13 stories
    if len(stories) != 13:
        errors.append(f"Expected 13 stories, found {len(stories)}")

    expected_distractor_keys = []

    for i, story in enumerate(stories):
        title = story.get('title', f"Story {i}")
        
        # 2. Check story fields
        if 'title' not in story:
            errors.append(f"Story {i}: Missing 'title'")
        if 'difficulty' not in story:
            errors.append(f"Story '{title}': Missing 'difficulty'")
        elif story['difficulty'] not in [1, 2, 3]:
            errors.append(f"Story '{title}': Invalid difficulty {story['difficulty']}")
            
        if 'parts' not in story or not isinstance(story['parts'], list):
            errors.append(f"Story '{title}': Missing or invalid 'parts' array")
        
        if 'overall_questions' not in story or not isinstance(story['overall_questions'], list):
            errors.append(f"Story '{title}': Missing or invalid 'overall_questions' array")
        elif len(story['overall_questions']) != 10:
            errors.append(f"Story '{title}': 'overall_questions' has {len(story['overall_questions'])} questions, expected 10")
        else:
            for j in range(len(story['overall_questions'])):
                expected_distractor_keys.append(f"{title}_overall_{j}")

        # 3. Check parts and pages
        parts = story.get('parts', [])
        for p_idx, part in enumerate(parts):
            pages = part.get('pages', [])
            if not isinstance(pages, list):
                errors.append(f"Story '{title}', Part {p_idx+1}: 'pages' is not an array")
                continue
            
            for pg_idx, page in enumerate(pages):
                page_id = f"Story '{title}', Part {p_idx+1}, Page {pg_idx+1}"
                
                required_fields = ['page_number', 'italian_text', 'english_text', 'questions']
                for field in required_fields:
                    if field not in page:
                        errors.append(f"{page_id}: Missing field '{field}'")
                
                if 'questions' in page:
                    questions = page['questions']
                    q_required = ['vocabulary', 'translation', 'comprehension']
                    for q_field in q_required:
                        if q_field not in questions or not isinstance(questions[q_field], list):
                            errors.append(f"{page_id}: Missing or invalid questions field '{q_field}'")
                    
                    if 'comprehension' in questions:
                        for c_idx in range(len(questions['comprehension'])):
                            # Format: Title_PartNumber_PageNumber_CompIndex
                            # Note: Part and Page numbers seem to be used in the key, not 0-based index?
                            # Looking at "Fortune and the man_1_1_0", it matches Part 1, Page 1, Comp 0.
                            p_num = part.get('part_number', p_idx + 1)
                            pg_num = page.get('page_number', pg_idx + 1)
                            expected_distractor_keys.append(f"{title}_{p_num}_{pg_num}_{c_idx}")

    # 4. Verify distractors
    with open(distractors_path, 'r') as f:
        distractors = json.load(f)

    missing_keys = []
    for key in expected_distractor_keys:
        if key not in distractors:
            missing_keys.append(key)
    
    if missing_keys:
        errors.append(f"Missing distractors for keys: {', '.join(missing_keys)}")

    # Report results
    if not errors:
        print("Success: All checks passed!")
    else:
        print("Validation failed with the following errors:")
        for error in errors:
            print(f"- {error}")

if __name__ == "__main__":
    validate()
