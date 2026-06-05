import os
import shutil

os.makedirs('archive/phase1_generation', exist_ok=True)
root_files = [f for f in os.listdir('.') if os.path.isfile(f) and not f.startswith('.')]

archived = []

for f in root_files:
    if f.endswith('.py') or f.endswith('.ts') or f.endswith('.js') or f.endswith('.txt'):
        # Keep config files
        if f in ['package.json', 'package-lock.json', 'tsconfig.json', 'vite.config.ts', 'tsconfig.app.json', 'tsconfig.node.json', 'eslint.config.js', 'vitest.config.ts', 'playwright.config.ts']:
            continue
        # If it's a test file or a script
        if f.startswith('test') or f.startswith('gen_') or f.startswith('fill_') or f.startswith('apply_') or f.startswith('update_') or f.startswith('fix_') or f.startswith('extract_') or f.startswith('translate_') or f.startswith('generate_') or f.startswith('check_') or f.startswith('s1'):
            shutil.move(f, os.path.join('archive/phase1_generation', f))
            archived.append({'file': f, 'reason': 'One-time generation/migration script'})
        elif f in ['linguistic_extractor.py', 'list_phrases.py', 'list_vocab.py', 'find_missing.py', 'get_missing.py', 'get_missing_104.py', 'get_missing_translations.py', 'get_missing_translations_help.py', 'get_missing_translations_phone.py', 'translations_dict.py', 'overhaul_s65.py', 'build_compliments.py', 'collect_missing_102.py', 'append_cooking_class.py', 'append_food_allergies.py', 'append_gelato_shop.py', 'extend_conversations.py', 'expand_conversations.py', 'expand_bike.py', 'expand_bus.py', 'expand_conv_76.py', 'expand_pharmacy.py', 'add_choice_translations.py', 'add_ids.py', 'temp_fill_vocab.py', 'temp_gen_conv.py', 'temp_gen_lessons.py', 'temp_translate.py']:
            shutil.move(f, os.path.join('archive/phase1_generation', f))
            archived.append({'file': f, 'reason': 'Obsolete/Legacy script (now in scripts/ or no longer used)'})

with open('reports/archived_scripts.md', 'w') as f:
    f.write('# Archived Scripts Report\n\n| Original Location | New Location | Reason |\n| :--- | :--- | :--- |\n')
    for item in archived:
        f.write(f'| `./{item["file"]}` | `archive/phase1_generation/{item["file"]}` | {item["reason"]} |\n')

print(f'Archived {len(archived)} scripts.')
