import { test, expect } from '@playwright/test';

test.describe('Premium Gating', () => {
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

  test('Free user cannot access premium game levels', async ({ page }) => {
    // Set user as free
    await page.addInitScript(() => {
      window.localStorage.setItem('parla-italiano-subscription', JSON.stringify({
        state: { plan: 'free', isValid: false },
        version: 0,
      }));
    });

    await page.goto('/games/gender');

    // Level 2 should have a crown icon and navigate to premium
    const level2Btn = page.getByRole('button', { name: /Level 2/i });
    await expect(level2Btn.getByText('👑')).toBeVisible();
    
    await level2Btn.click();
    await expect(page).toHaveURL(/\/premium/);
  });

  test('Free user cannot send messages in chat', async ({ page }) => {
    // Set user as free and mock a friend
    await page.addInitScript(() => {
      window.localStorage.setItem('parla-italiano-subscription', JSON.stringify({
        state: { plan: 'free', isValid: false },
        version: 0,
      }));
    });

    // Mock friends API
    await page.route('**/api/v1/friends/', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify([{ id: 'friend-1', username: 'Friend1', is_online: true }]),
      });
    });

    // Mock messages API
    await page.route('**/api/v1/chat/messages/?friend_id=friend-1', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify([]),
      });
    });

    await page.goto('/chat/friend-1');

    // Should see premium banner
    await expect(page.getByText(/Upgrade to Premium to send messages/i)).toBeVisible();

    // Input should be disabled
    const input = page.getByPlaceholder(/Upgrade to chat.../i);
    await expect(input).toBeDisabled();
  });
});
