# Parla Italiano Admin Panel: Developer Guide

This document outlines the technical architecture and implementation details of the Admin Panel, which serves as the UI for the Factory V2 infrastructure.

## Architecture Overview
The Admin Panel is built as a distinct routing subtree (`/admin/*`) within the React frontend, utilizing `react-router-dom` for navigation. It employs a layout wrapper (`AdminLayout`) to isolate the admin UI from the consumer-facing application.

### Key Components
- **AdminLayout**: The root component containing the `AdminSidebar` and `AdminTopNav`. It manages the grid structure.
- **Data Loaders**: The admin panel heavily relies on `src/data/corpusLoader.ts` to eagerly load and inspect the JSON datasets (vocabulary, phrases, conversations) without needing to fetch from a backend database.
- **Mock Adapters**: Currently, some advanced features like User Management and real-time Analytics rely on mocked JSON data within the components. Future backend work will replace these with real `fetch` calls to Django endpoints.

## Integrating with the Factory Pipeline
The most complex part of the Admin Panel is the **Factory Operations** view.

### Current Implementation
The `FactoryOperations.tsx` component provides a UI to trigger backend Python scripts (e.g., `build_and_certify_scenario.py`, `curriculum_designer.py`). 

### Bridging the Gap
To execute these commands, the React app must communicate with the Django backend.
1. **Frontend**: Sends a POST request to `/api/v1/factory/execute/` with the command name.
2. **Backend**: A secure Django view (restricted to `is_superuser`) uses Python's `subprocess` module to spawn the script.
3. **WebSockets (Future)**: For real-time log streaming (as mocked in the UI), the backend should implement Django Channels to stream `stdout` back to the React component.

## Adding New Admin Views
To extend the Admin Panel:
1. Create a new component in `src/screens/admin/`.
2. Ensure it utilizes the shared styles defined in `src/screens/admin/AdminCommon.css`.
3. Add the route to the `<Route path="/admin">` block in `src/App.tsx`.
4. Update `AdminSidebar.tsx` to include the new navigation link and an appropriate `react-icon`.

## Security Considerations
- **Route Guards**: Ensure that the `/admin` routes remain protected by a robust authentication guard that checks the user's role.
- **Determinism**: The Admin Panel is deliberately designed to be **read-only** for curriculum data. Direct editing of JSON files via the UI is discouraged to maintain the deterministic nature of the Factory pipeline. If changes are needed, they should be made to the source `conversations.json` and the factory rebuilt.
