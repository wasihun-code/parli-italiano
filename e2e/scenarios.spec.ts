import { test, expect } from '@playwright/test';

test.describe('Scenarios', () => {
  test.beforeEach(async ({ page }) => {
    // Bypass onboarding and set foundations as passed
    await page.addInitScript(() => {
      window.localStorage.setItem('hasSeenOnboarding', 'true');
      window.localStorage.setItem('parla-italiano-auth', JSON.stringify({
        state: {
          users: [{ id: 'e2e-user', name: 'E2E User', email: 'e2e@example.com' }],
          currentUserId: 'e2e-user',
        },
        version: 0,
      }));
      window.localStorage.setItem('parla-italiano-progress', JSON.stringify({
        state: {
          foundationScores: { 1: 100, 2: 100, 3: 100, 4: 100, 5: 100 },
          scenarioProgress: {},
          xp: 0,
          streak: 0,
        },
        version: 0,
      }));
    });
  });

  test('User can navigate to a scenario and start vocabulary training', async ({ page }) => {
    await page.goto('/scenarios');
    
    // Check if we are on scenarios page
    await expect(page.locator('h1')).toContainText('Scenarios');

    // Click on the first scenario card
    await page.locator('.coffee-card').first().click();
    
    // Should be on detail page
    await expect(page.locator('h1')).toBeVisible();
    await expect(page.getByText(/Vocabulary/)).toBeVisible();

    // Start vocabulary
    await page.getByRole('button', { name: /start/i }).first().click();

    // Check if vocabulary training loaded
    await expect(page.locator('[data-testid="scenario-title"]')).toBeVisible();
  });

  test('User can skip to test in a scenario', async ({ page }) => {
    // Go directly to a scenario detail page (assuming ID 1 exists)
    await page.goto('/scenarios/1');

    await page.getByText(/skip to test/i).click();

    // Should see "Skip Test" in header
    await expect(page.locator('[data-testid="scenario-title"]')).toContainText('Skip Test');
  });

  test('Completing vocabulary unlocks phrases', async ({ page }) => {
    // Set vocabulary as completed in localStorage
    await page.addInitScript(() => {
      const progress = JSON.parse(window.localStorage.getItem('parla-italiano-progress') || '{}');
      progress.state.scenarioProgress[1] = {
        vocabularyCompleted: true,
        phraseScore: 0,
        phraseCompleted: false,
        sentenceScore: 0,
        sentenceCompleted: false,
        conversationUnlocked: false,
      };
      window.localStorage.setItem('parla-italiano-progress', JSON.stringify(progress));
    });

    await page.goto('/scenarios/1');

    // Phrases should be unlocked (not having 'locked' class or just check button)
    const phraseCard = page.locator('.card').filter({ hasText: 'Phrases' });
    await expect(phraseCard.getByRole('button', { name: /start/i })).toBeEnabled();
  });

  test('Completing phrases unlocks sentences', async ({ page }) => {
    // Set vocabulary and phrases as completed in localStorage
    await page.addInitScript(() => {
      const progress = JSON.parse(window.localStorage.getItem('parla-italiano-progress') || '{}');
      progress.state.scenarioProgress[1] = {
        vocabularyCompleted: true,
        phraseScore: 90,
        phraseCompleted: true,
        sentenceScore: 0,
        sentenceCompleted: false,
        conversationUnlocked: false,
      };
      window.localStorage.setItem('parla-italiano-progress', JSON.stringify(progress));
    });

    await page.goto('/scenarios/1');

    // Sentences should be unlocked
    const sentenceCard = page.locator('.card').filter({ hasText: 'Sentences' });
    await expect(sentenceCard.getByRole('button', { name: /start/i })).toBeEnabled();
  });
});
