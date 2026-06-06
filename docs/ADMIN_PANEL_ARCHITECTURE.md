# Parla Italiano Admin Panel Architecture

## 1. Features
The Admin Panel serves as the operational control center for the Parla Italiano platform. It integrates tightly with the Factory V2 infrastructure to allow administrators to:
- Monitor and manage the entire curriculum of 116 Gold Standard scenarios.
- Inspect conversations, vocabulary, phrases, sentences, and mini-lessons.
- Validate and monitor audio asset coverage, including deterministic hash resolution.
- Track certification status and execute factory audit tools.
- Manage users, view their learning progress, and track accuracy.
- Analyze global learning metrics to guide curriculum improvements.
- Execute Factory Operations (rebuilding curriculums, regenerating lessons, running certification) directly from the UI.

## 2. Pages
The Admin Panel consists of the following primary views:
- **AdminDashboard (`/admin`)**: High-level metrics, total scenarios, pass rates, user counts, and recent factory runs.
- **ScenarioBrowser (`/admin/curriculum`)**: Searchable and filterable list of all scenarios.
- **ScenarioDetailView (`/admin/curriculum/:scenarioId`)**: Deep dive into a specific scenario with tabs for Overview, Vocabulary, Phrases, Sentences, Mini Lessons, Conversations, and Audits.
- **ConversationInspector (Component within ScenarioDetailView)**: Tree-based visualization of conversation branching, host lines, user choices, translations, and audio status.
- **AudioDashboard (`/admin/audio`)**: Project-wide audio metrics, missing assets, and deterministic resolution tracking.
- **CertificationDashboard (`/admin/certification`)**: Status of all scenarios (PASS/FAIL), historical reports, and manual triggers for audits.
- **UserManagement (`/admin/users`)**: List of all users, streaks, and scenario completion rates.
- **UserDetailView (`/admin/users/:userId`)**: Specific user progress, accuracy, and mastered scenarios.
- **AnalyticsDashboard (`/admin/analytics`)**: Aggregate metrics on most/least completed scenarios, frequent failures, and average times.
- **FactoryOperations (`/admin/factory`)**: Control interface for running Python scripts (build, audit, regenerate) via backend endpoints or mocked adapters.

## 3. Navigation
A dedicated, desktop-first layout will be utilized.
- **Top Navigation**: Displays current user, basic settings, and quick actions.
- **Sidebar**: Sticky left navigation containing links to Dashboard, Curriculum, Audio, Certification, Users, Analytics, Factory, and System logs.

## 4. Permissions
- The Admin Panel is restricted to users with the `is_staff` or `is_superuser` flag.
- Normal users attempting to access `/admin` will be redirected to the consumer home screen.
- Factory operations may require additional `is_superuser` privileges to prevent accidental data overwrites.

## 5. Data Sources
- **Curriculum Data**: Loaded from `src/data/corpusLoader.ts` and underlying JSON files (`exports/`).
- **Certification Data**: Loaded from `reports/` JSON files (e.g., `reports/global_certification.json`).
- **User & Analytics Data**: Pulled from the Django backend API (`/api/v1/users/`, `/api/v1/analytics/`). Where endpoints are not yet available, mock adapters will simulate the responses to unblock UI development.
- **Factory Triggers**: Will communicate with a new backend endpoint (e.g., `/api/v1/factory/execute/`) which spawns the corresponding Python scripts (e.g., `scripts/certify_all.py`).

## 6. Factory Integration
The UI bridges the gap between the TypeScript frontend and the Python Factory V2 pipeline. 
- The **Factory Operations** page will dispatch requests to run scripts like `build_and_certify_scenario.py`.
- The **Certification Dashboard** reads the resulting `.md` and `.json` reports to display live health metrics without requiring terminal access.

## 7. Future Expansion
- **Live Editing**: While currently read-only to preserve determinism, future iterations may allow editing JSON configurations directly from the UI, automatically triggering a factory rebuild.
- **Audio Synthesis**: Integration with Edge-TTS or Spark-TTS to generate missing audio files on-the-fly via the Admin UI.
- **A/B Testing**: Creating variants of mini-lessons and tracking completion rates in the Analytics Dashboard.
