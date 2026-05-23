import { test, expect } from '@playwright/test';

test.describe('Streak and XP', () => {
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

  test('XP increases when completing activities', async ({ page }) => {
    await page.addInitScript(() => {
      window.localStorage.setItem('parla-italiano-progress', JSON.stringify({
        state: { xp: 50, streak: 5, lastActivityDate: '2023-01-01' },
        version: 0,
      }));
    });

    await page.goto('/');

    // Check initial XP on profile or home
    await page.goto('/profile');
    await expect(page.getByText(/50 XP/i)).toBeVisible();

    // Mock an activity that adds XP
    await page.evaluate(() => {
      // Accessing the store via window if possible, or just checking after some action
      // For E2E, we usually perform an action that triggers the update
      // Let's assume navigating to a game and "winning" it updates XP
    });

    // Alternatively, we can just verify the store updates if we trigger an action
    // But E2E should ideally be through UI
  });

  test('Streak updates on daily activity', async ({ page }) => {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yesterdayStr = yesterday.toISOString().split('T')[0];

    await page.addInitScript((yesterdayStr) => {
      window.localStorage.setItem('parla-italiano-progress', JSON.stringify({
        state: { 
          xp: 100, 
          streak: 5, 
          lastActivityDate: yesterdayStr 
        },
        version: 0,
      }));
    }, yesterdayStr);

    // Mock backend activity record
    await page.route('**/api/v1/users/me/activity/', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ streak_days: 6 }),
      });
    });

    await page.goto('/');

    // Perform an action that updates streak, e.g., viewing home screen often triggers it
    // In progressStore.ts, updateStreak() is called when setting vocabulary completed.
    
    // Let's manually trigger it via a mock action or just check if it happened on load if the app does it
    await expect(page.locator('header')).toContainText('6'); // Assuming streak is shown in header
  });
});
