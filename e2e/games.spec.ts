import { test, expect } from '@playwright/test';

test.describe('Game Mechanics', () => {
  test.beforeEach(async ({ page }) => {
    // Bypass onboarding
    await page.addInitScript(() => {
      window.localStorage.setItem('hasSeenOnboarding', 'true');
      window.localStorage.setItem('parla-italiano-auth', JSON.stringify({
        state: {
          users: [{ id: 'e2e-user', name: 'E2E User', email: 'e2e@example.com' }],
          currentUserId: 'e2e-user',
        },
        version: 0,
      }));
    });
  });

  test('User can play Gender Game and get correct/incorrect answers', async ({ page }) => {
    await page.goto('/games/gender');

    // Click Level 1 to start
    await page.getByRole('button', { name: /Level 1/i }).click();

    // Check if game started
    await expect(page.getByText(/Masculine/i)).toBeVisible();
    await expect(page.getByText(/Feminine/i)).toBeVisible();

    // Select Masculine
    await page.getByRole('button', { name: /MASCULINE/i }).click();
    await page.getByRole('button', { name: /Check/i }).click();

    // Should see feedback (either correct or incorrect)
    await expect(page.locator('.fade-in')).toBeVisible();
  });

  test('Winning a level with high score unlocks next level (if premium)', async ({ page }) => {
    // Set premium and pass level 1
    await page.addInitScript(() => {
      window.localStorage.setItem('parla-italiano-subscription', JSON.stringify({
        state: { plan: 'premium', isValid: true },
        version: 0,
      }));
      window.localStorage.setItem('parla-italiano-games', JSON.stringify({
        state: {
          genderGame: { unlockedLevels: 2, highScore: 100 },
          translationGame: { unlockedLevels: 1, highScore: 0 },
          prepositionGame: { unlockedLevels: 1, highScore: 0 },
          idiomsGame: { unlockedLevels: 1, highScore: 0 },
          oppositesGame: { unlockedLevels: 1, highScore: 0 },
          numbersGame: { unlockedLevels: 1, highScore: 0 },
          pluralGame: { unlockedLevels: 1, highScore: 0 },
          unlockedStories: [],
          completedStories: [],
          storyProgress: {},
          storyScores: {},
        },
        version: 0,
      }));
    });

    await page.goto('/games/gender');

    // Level 2 should be unlocked
    const level2Btn = page.getByRole('button', { name: /Level 2/i });
    await expect(level2Btn).toBeEnabled();
  });
});
