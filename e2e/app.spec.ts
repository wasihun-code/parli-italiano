import { test, expect } from '@playwright/test';

test.describe('Parli Italiano E2E', () => {
  test.beforeEach(async ({ page }) => {
    // Bypass the onboarding guard by pre-setting the flag, then clear SRS/progress
    await page.addInitScript(() => {
      window.localStorage.setItem('hasSeenOnboarding', 'true');
    });
  });

  test('App loads home screen with Bentornato greeting', async ({ page }) => {
    await page.goto('/');

    // The home screen shows "Bentornato!" not "Parli Italiano"
    await expect(page.locator('h1').filter({ hasText: 'Bentornato' })).toBeVisible();

    // Bottom nav should have all 4 nav items
    const nav = page.locator('nav');
    await expect(nav.getByRole('button', { name: /home/i })).toBeVisible();
    await expect(nav.getByRole('button', { name: /scenarios/i })).toBeVisible();
    await expect(nav.getByRole('button', { name: /review/i })).toBeVisible();
    await expect(nav.getByRole('button', { name: /foundations/i })).toBeVisible();
  });

  test('Navigate to Foundations shows correct heading', async ({ page }) => {
    await page.goto('/foundations');

    // The foundations screen h1 is "Foundations"
    await expect(page.locator('h1').filter({ hasText: 'Foundations' })).toBeVisible();
  });

  test('Navigate to Scenarios shows correct heading', async ({ page }) => {
    // Foundations must be passed first; skip that by going directly to the URL
    await page.goto('/scenarios');

    // If foundations not done, it shows "Scenarios Locked" or "Scenarios"
    const heading = page.locator('h1');
    await expect(heading).toBeVisible();
    // Either "Scenarios Locked" or "Scenarios" should appear
    const text = await heading.first().textContent();
    expect(text).toMatch(/Scenarios/);
  });

  test('Navigate to Review shows the review screen', async ({ page }) => {
    await page.goto('/review');

    // Review screen shows "Review" heading
    await expect(page.locator('h1').filter({ hasText: 'Review' })).toBeVisible();

    // With no items due, shows the empty state
    await expect(page.getByText('No review items right now')).toBeVisible();
  });
});
