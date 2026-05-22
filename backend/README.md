# Parli Italiano Backend

This is the Django REST Framework backend for the Parli Italiano language learning application.

## Prerequisites

- Python 3.10+
- `pip` or `yarn` (for managing some scripts)

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # Or if you are using the provided virtual environment:
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file in the `backend/` directory based on the following list:

   ```env
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3
   
   # Stripe Configuration
   STRIPE_PUBLIC_KEY=pk_test_...
   STRIPE_SECRET_KEY=sk_test_...
   STRIPE_WEBHOOK_SECRET=whsec_...
   STRIPE_PREMIUM_PRICE_ID=price_...
   STRIPE_PREMIUM_PLUS_PRICE_ID=price_...
   ```

3. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Import Italian Content:**
   This command imports scenarios from the `exported-content.json` file in the project root.
   ```bash
   python manage.py import_italian_content
   ```

5. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://localhost:8000/`.

## Stripe Webhook Setup

To test subscription updates locally:

1. Install the Stripe CLI.
2. Login to your Stripe account: `stripe login`.
3. Start the webhook forwarding:
   ```bash
   stripe listen --forward-to localhost:8000/api/v1/subscription/webhook/stripe/
   ```
4. Copy the `whsec_...` secret from the output and add it to your `.env` as `STRIPE_WEBHOOK_SECRET`.

## Adding a New Language

To add support for a new language (e.g., Spanish):

1. **Backend:**
   - Log in to the Django Admin (`/admin/`).
   - Create a new `Language` record:
     - **Name:** Spanish
     - **Code:** es
   - (Optional) Use a management command or the Admin to upload content for this language.

2. **Frontend:**
   - Create new JSON files in `src/data/` for the new language (e.g., `scenarios_es.json`).
   - Update the frontend configuration to allow selecting the new language.

## API Documentation

- **Auth Endpoints:**
  - `POST /api/v1/auth/register/`: Register a new user.
  - `POST /api/v1/auth/login/`: Login and receive JWT tokens.
- **Progress Endpoints:**
  - `POST /api/v1/users/me/progress/scenario/`: Sync scenario progress. Include `?language=it` in the query or `language: "it"` in the body.
- **Webhook Endpoints:**
  - `POST /api/v1/subscription/webhook/stripe/`: Handles Stripe events.
