import { test, expect } from '@playwright/test';

test.describe('Training Screen Flows', () => {
  test.beforeEach(async ({ page }) => {
    await page.addInitScript(() => {
      window.localStorage.setItem('hasSeenOnboarding', 'true');
      // Disable SpeechRecognition to ensure consistent listenRepeat kind
      // @ts-ignore
      window.SpeechRecognition = undefined;
      // @ts-ignore
      window.webkitSpeechRecognition = undefined;
    });
  });

  test('Phrase Training screen loads with scenario title', async ({ page }) => {
    await page.goto('/scenarios/1/phrases');

    // Wait for the scenario title container
    await expect(page.getByTestId('scenario-title')).toBeVisible({ timeout: 15000 });

    // The first exercise is listenRepeat — the heading should contain "Listen and repeat aloud:"
    const heading = page.locator('h2');
    await expect(heading).toBeVisible();
    const text = await heading.textContent();
    expect(text).toMatch(/Listen and repeat aloud:/);
  });

  test('Phrase Training Continue button advances exercise', async ({ page }) => {
    await page.goto('/scenarios/1/phrases');

    // Wait for the screen to load
    await expect(page.getByTestId('scenario-title')).toBeVisible({ timeout: 15000 });

    // listenRepeat exercises have a "Continue" button (no input required)
    const continueBtn = page.getByRole('button', { name: /Continue/i });
    await expect(continueBtn).toBeVisible();
    await continueBtn.click();

    // After clicking, the screen should still be showing a phrase exercise
    await expect(page.locator('h2')).toBeVisible();
  });

  test('Sentence Training screen shows Italian accent keyboard buttons', async ({ page }) => {
    await page.goto('/scenarios/1/sentences');

    // Wait for screen to load
    await expect(page.getByTestId('scenario-title')).toBeVisible({ timeout: 15000 });

    // The Italian keyboard renders buttons with accented characters
    await expect(page.getByRole('button', { name: 'à' })).toBeVisible();
    await expect(page.getByRole('button', { name: 'è' })).toBeVisible();

    // Input field should be visible for typing
    await expect(page.locator('input[type="text"]')).toBeVisible();
  });

  test('Sentence Training: typing wrong answer shows Incorrect feedback', async ({ page }) => {
    await page.goto('/scenarios/1/sentences');

    await expect(page.getByTestId('scenario-title')).toBeVisible({ timeout: 15000 });

    // Fill in a clearly wrong answer
    const input = page.locator('input[type="text"]');
    await input.fill('wrong answer xyz');

    // Click Check
    await page.getByRole('button', { name: /Check/i }).click();

    // Should show "Incorrect." feedback
    await expect(page.getByText(/Incorrect\./)).toBeVisible();

    // Continue button should appear
    await expect(page.getByRole('button', { name: /Continue/i })).toBeVisible();
  });

  test('Vocabulary Training shows PASS THIS PHASE button and starts skip test', async ({ page }) => {
    await page.goto('/scenarios/1/vocabulary');

    // Wait for loading to finish
    await expect(page.getByTestId('scenario-title')).toBeVisible({ timeout: 15000 });

    // The skip button should be visible
    const passBtn = page.getByText('PASS THIS PHASE');
    await expect(passBtn).toBeVisible();

    // Click it to start skip test
    await passBtn.click();

    // Check if it started correctly
    await expect(page.getByText(/Skip Test: 1/)).toBeVisible();
  });
});
