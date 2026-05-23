# End-to-End Tests for Parli Italiano

This directory contains Playwright E2E tests for the Parli Italiano application.

## Prerequisites

Ensure you have the development server running or a build available. 
The tests are configured to run against the URL specified in `playwright.config.ts`.

## Running Tests

To run all E2E tests:

```bash
npx playwright test
```

To run a specific test file:

```bash
npx playwright test e2e/auth.spec.ts
```

To run tests in UI mode:

```bash
npx playwright test --ui
```

## Test Coverage

- `auth.spec.ts`: User registration, login, and error handling.
- `scenarios.spec.ts`: Scenario navigation, vocabulary training, and phase unlocking.
- `games.spec.ts`: Game mechanics (Gender game), scoring, and level unlocking.
- `premium.spec.ts`: Premium gating for games and social features.
- `social.spec.ts`: Friend search, requests, and premium chat flow.
- `progress.spec.ts`: XP tracking and daily streak updates.

## Mocking

These tests use Playwright's `page.route` to mock backend API responses, allowing them to run without a live backend. Local storage is also manipulated to set specific user states (e.g., premium status, progress).
