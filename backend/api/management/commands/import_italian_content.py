import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from api.models import Language, Scenario

class Command(BaseCommand):
    help = 'Import Italian scenarios from exported-content.json'

    def handle(self, *args, **options):
        # 1. Path to the JSON file
        # settings.BASE_DIR is 'backend/' as per Path(__file__).resolve().parent.parent in core/settings.py
        json_path = os.path.join(settings.BASE_DIR.parent, 'exported-content.json')
        
        self.stdout.write(f'Attempting to import from: {json_path}')
        
        if not os.path.exists(json_path):
            self.stderr.write(self.style.ERROR(f'File not found: {json_path}'))
            return

        # 2. Ensure Italian language exists
        italian, created = Language.objects.get_or_create(
            code='it',
            defaults={'name': 'Italian', 'is_active': True}
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created Language: Italian'))
        else:
            self.stdout.write(f'Using existing Language: Italian')

        # 3. Read and parse JSON
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error reading JSON: {e}'))
            return

        if isinstance(data, dict):
            scenarios_data = data.get('scenarios', [])
        elif isinstance(data, list):
            scenarios_data = data
        else:
            self.stderr.write(self.style.ERROR('Unexpected JSON format (neither list nor dict with "scenarios" key)'))
            return

        # 4. Import Scenarios
        count = 0
        for item in scenarios_data:
            # item could be a scenario object
            scenario_id = str(item.get('id'))
            if not scenario_id:
                self.stdout.write(self.style.WARNING(f'Skipping item without id: {item.get("title")}'))
                continue
            
            title = item.get('title', 'Untitled')
            # category and difficulty might not be in the JSON, default as requested
            category = item.get('category', 'General')
            difficulty = item.get('difficulty', 1)
            
            scenario, created = Scenario.objects.update_or_create(
                id=scenario_id,
                language=italian,
                defaults={
                    'title': title,
                    'category': category,
                    'difficulty': difficulty,
                }
            )
            
            if created:
                self.stdout.write(f'Created scenario: {title} (ID: {scenario_id})')
            else:
                self.stdout.write(f'Updated scenario: {title} (ID: {scenario_id})')
            count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} scenarios.'))
