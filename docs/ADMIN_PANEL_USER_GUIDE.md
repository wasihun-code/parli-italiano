# Parla Italiano Admin Panel: User Guide

Welcome to the Parla Italiano Admin Panel. This tool is designed to give you complete operational control over the language curriculum, user progression, and system infrastructure.

## Getting Started
Access the admin panel by navigating to `/admin` while logged in as a Staff or Superuser. If you do not have these privileges, you will be redirected to the main application.

## Dashboard
The **Dashboard** provides a high-level overview of the entire system. It displays key metrics such as:
- Total number of scenarios and their certification status.
- Total lessons and scripted conversations.
- Overall audio coverage percentage.
- Total active users.
- The current Factory version and the timestamp of the last global certification run.

## Curriculum Management
Navigate to **Curriculum** to view the entire scenario catalog.
- **Search & Filter**: Quickly find scenarios by name or category.
- **Inspect**: Click on any scenario to view its detailed breakdown.
  - **Overview**: Read the description and see item counts.
  - **Vocabulary/Phrases/Sentences**: View the exact extracted linguistic items and their English translations.
  - **Conversations**: Review the branching dialogue trees and verify the number of turns.

## Audio Dashboard
The **Audio** section tracks the health of the text-to-speech corpus.
- **Metrics**: View the total assets on disk versus those referenced in the manifests.
- **Deterministic Hashes**: See how many audio files are resolved dynamically via SHA-1 hashing.
- **Actions**: Trigger audio audits or command the system to generate missing audio.

## Certification Dashboard
The **Certification** page is your window into the automated QA pipeline.
- View the PASS/FAIL status of all 116 scenarios.
- See exactly when the last audit was run.
- Manually trigger a re-certification for a specific scenario or the entire project.

## Factory Operations
The **Factory** page bridges the UI with the backend Python automation scripts.
- **Rebuild Curriculum**: Automatically regenerates `mini_lessons.json` for all scenarios based on the latest extracted data.
- **Run Extraction**: Parses `conversations.json` to identify new vocabulary.
- **Global Certify**: Runs the full 13-audit pipeline to guarantee Gold Standard compliance.
- **Logs**: Watch real-time terminal output directly in the browser as the factory runs.

## User Management & Analytics
- **Users**: Search for users, view their streaks, and drill down into their specific progression and accuracy metrics.
- **Analytics**: Identify the most (and least) popular scenarios. Use the failure metrics (e.g., "Most Failed Lessons") to guide future curriculum adjustments.
