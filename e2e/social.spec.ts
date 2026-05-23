import { test, expect } from '@playwright/test';

test.describe('Social Flow', () => {
  test.beforeEach(async ({ page }) => {
    // Bypass onboarding and set as premium to test chat
    await page.addInitScript(() => {
      window.localStorage.setItem('hasSeenOnboarding', 'true');
      window.localStorage.setItem('parla-italiano-auth', JSON.stringify({
        state: {
          users: [{ id: 'e2e-user', name: 'E2E User', email: 'e2e@example.com' }],
          currentUserId: 'e2e-user',
        },
        version: 0,
      }));
      window.localStorage.setItem('parla-italiano-subscription', JSON.stringify({
        state: { plan: 'premium', isValid: true },
        version: 0,
      }));
    });
  });

  test('User can search and send friend request', async ({ page }) => {
    // Mock search results
    await page.route('**/api/v1/users/search/?q=OtherUser', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify([{ id: 'user-2', username: 'OtherUser' }]),
      });
    });

    // Mock send request
    await page.route('**/api/v1/friends/requests/', async (route) => {
      await route.fulfill({
        status: 201,
        contentType: 'application/json',
        body: JSON.stringify({ message: 'Request sent' }),
      });
    });

    await page.goto('/friends');

    await page.getByPlaceholder(/Enter username or email/i).fill('OtherUser');
    await page.getByRole('button', { name: /Search/i }).click();

    await expect(page.getByText('OtherUser')).toBeVisible();
    
    // Setup dialog listener for the alert
    page.on('dialog', dialog => dialog.dismiss());
    
    await page.getByRole('button', { name: /Add/i }).click();
  });

  test('User can accept friend request', async ({ page }) => {
    // Mock pending requests
    await page.route('**/api/v1/friends/requests/', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify([{ id: 1, from_user: { id: 'user-3', username: 'Requestor' } }]),
      });
    });

    // Mock accept request
    await page.route('**/api/v1/friends/requests/1/accept/', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ message: 'Accepted' }),
      });
    });

    await page.goto('/friends');

    await expect(page.getByText('Pending Requests')).toBeVisible();
    await expect(page.getByText('Requestor')).toBeVisible();

    await page.getByRole('button', { name: /Accept/i }).click();
    
    // Pending request should disappear (or list should update)
    await expect(page.getByText('Requestor')).not.toBeVisible();
  });

  test('Premium user can send chat messages', async ({ page }) => {
    // Mock friends list
    await page.route('**/api/v1/friends/', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify([{ id: 'friend-1', username: 'Friend1', is_online: true }]),
      });
    });

    // Mock messages
    await page.route('**/api/v1/chat/messages/?friend_id=friend-1', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify([]),
      });
    });

    // Mock send message
    await page.route('**/api/v1/chat/messages/', async (route) => {
      await route.fulfill({
        status: 201,
        contentType: 'application/json',
        body: JSON.stringify({ id: 100, sender_id: 'e2e-user', message: 'Ciao!', timestamp: new Date().toISOString() }),
      });
    });

    await page.goto('/chat/friend-1');

    const input = page.getByPlaceholder(/Type a message.../i);
    await input.fill('Ciao!');
    await page.locator('button[type="submit"]').click();

    // Message should appear in chat
    await expect(page.getByText('Ciao!')).toBeVisible();
  });
});
