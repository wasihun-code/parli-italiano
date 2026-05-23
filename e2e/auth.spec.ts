import { test, expect } from '@playwright/test';

test.describe('Authentication', () => {
  test.beforeEach(async ({ page }) => {
    // Clear localStorage to start fresh
    await page.addInitScript(() => {
      window.localStorage.clear();
    });
  });

  test('User can sign up', async ({ page }) => {
    // Mock successful signup
    await page.route('**/api/v1/auth/register/', async (route) => {
      await route.fulfill({
        status: 201,
        contentType: 'application/json',
        body: JSON.stringify({ message: 'User created' }),
      });
    });

    // Mock successful login after signup
    await page.route('**/api/v1/auth/login/', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          user: { id: '1', username: 'testuser', email: 'test@example.com' },
          tokens: { access: 'fake-access-token', refresh: 'fake-refresh-token' }
        }),
      });
    });

    await page.goto('/auth');
    await page.getByRole('button', { name: /sign up/i }).first().click();
    
    await page.getByPlaceholder(/name/i).fill('Test User');
    await page.getByPlaceholder(/email/i).fill('test@example.com');
    await page.getByPlaceholder(/password/i).fill('password123');
    
    await page.getByRole('button', { name: /sign up/i }).last().click();

    await expect(page).toHaveURL('/');
  });

  test('User can log in', async ({ page }) => {
    // Mock successful login
    await page.route('**/api/v1/auth/login/', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          user: { id: '1', username: 'testuser', email: 'test@example.com' },
          tokens: { access: 'fake-access-token', refresh: 'fake-refresh-token' }
        }),
      });
    });

    await page.goto('/auth');
    await page.getByPlaceholder(/email/i).fill('test@example.com');
    await page.getByPlaceholder(/password/i).fill('password123');
    
    await page.getByRole('button', { name: /login/i }).last().click();

    await expect(page).toHaveURL('/');
  });

  test('Login fails with incorrect credentials', async ({ page }) => {
    // Mock failed login
    await page.route('**/api/v1/auth/login/', async (route) => {
      await route.fulfill({
        status: 401,
        contentType: 'application/json',
        body: JSON.stringify({ detail: 'Invalid credentials' }),
      });
    });

    await page.goto('/auth');
    await page.getByPlaceholder(/email/i).fill('wrong@example.com');
    await page.getByPlaceholder(/password/i).fill('wrongpassword');
    
    await page.getByRole('button', { name: /login/i }).last().click();

    await expect(page.getByText(/invalid credentials/i)).toBeVisible();
  });
});
