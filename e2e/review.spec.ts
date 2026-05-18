import { test, expect } from '@playwright/test';

test.describe('Review Screen Test', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      window.localStorage.setItem('hasSeenOnboarding', 'true');
      window.localStorage.setItem('parla-italiano-auth', JSON.stringify({
        state: {
          users: [{ id: 'e2e-user', name: 'E2E User', email: 'e2e@example.com', password: 'password' }],
          currentUserId: 'e2e-user',
        },
        version: 0,
      }));
    });
  });

  test('Clicking Review in nav does not crash the app', async ({ page }) => {
    const errors: string[] = [];
    page.on('pageerror', exception => errors.push(exception.message));

    await page.goto('/');

    // Navigate to Review via the bottom nav button
    await page.locator('nav').getByRole('button', { name: /review/i }).click();

    // Page should be stable with the Review heading
    await expect(page.locator('h1').filter({ hasText: 'Review' })).toBeVisible();

    // No crashes
    expect(errors).toHaveLength(0);
  });

  test('Review shows empty state when no items are due', async ({ page }) => {
    await page.goto('/review');

    await expect(page.locator('h1').filter({ hasText: 'Review' })).toBeVisible();
    await expect(page.getByText('Nothing to review right now - come back later!')).toBeVisible();
    await expect(page.getByText('0 learned / 0 total')).toBeVisible();
  });
});
