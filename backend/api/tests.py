from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Language, ScenarioProgress, UserLanguageProgress
from unittest.mock import patch, MagicMock
import json
from django.utils import timezone

User = get_user_model()

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'Test',
            'last_name': 'User'
        }

    def test_register(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'test@example.com')

    def test_login(self):
        User.objects.create_user(**self.user_data)
        login_data = {'email': 'test@example.com', 'password': 'password123'}
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tokens', response.data)
        self.assertIn('access', response.data['tokens'])

class ProgressTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='password123'
        )
        self.client.force_authenticate(user=self.user)
        self.it_lang = Language.objects.create(code='it', name='Italian')
        self.sync_url = reverse('scenario_sync')

    def test_scenario_sync(self):
        data = {
            'language': 'it',
            'scenario_id': 1,
            'phase': 'practice',
            'completed': True,
            'score': 95
        }
        response = self.client.post(self.sync_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        progress = ScenarioProgress.objects.get(user=self.user, language=self.it_lang, scenario_id=1)
        self.assertEqual(progress.phase, 'practice')
        self.assertTrue(progress.completed)
        self.assertEqual(progress.score, 95)

class StripeWebhookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.webhook_url = reverse('stripe_webhook')
        self.user = User.objects.create_user(
            username='stripeuser', email='stripe@example.com', password='password123',
            id=123
        )

    @patch('stripe.Webhook.construct_event')
    @patch('stripe.Subscription.retrieve')
    def test_checkout_session_completed(self, mock_sub_retrieve, mock_webhook_construct):
        # Mock Stripe event
        mock_webhook_construct.return_value = {
            'type': 'checkout.session.completed',
            'data': {
                'object': {
                    'client_reference_id': '123',
                    'customer': 'cus_123',
                    'subscription': 'sub_123'
                }
            }
        }
        
        # Mock Subscription retrieve
        mock_sub_retrieve.return_value = {
            'items': {
                'data': [{
                    'price': {'id': 'price_premium_id'}
                }]
            },
            'current_period_end': 1735689600 # 2025-01-01
        }

        with self.settings(STRIPE_PREMIUM_PRICE_ID='price_premium_id', STRIPE_WEBHOOK_SECRET='whsec_test'):
            response = self.client.post(
                self.webhook_url,
                data=json.dumps({'id': 'evt_test'}),
                content_type='application/json',
                HTTP_STRIPE_SIGNATURE='test_sig'
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.subscription_plan, 'premium')
        self.assertEqual(self.user.stripe_customer_id, 'cus_123')

    @patch('stripe.Webhook.construct_event')
    def test_subscription_deleted(self, mock_webhook_construct):
        self.user.subscription_plan = 'premium'
        self.user.stripe_customer_id = 'cus_123'
        self.user.save()

        mock_webhook_construct.return_value = {
            'type': 'customer.subscription.deleted',
            'data': {
                'object': {
                    'customer': 'cus_123'
                }
            }
        }

        with self.settings(STRIPE_WEBHOOK_SECRET='whsec_test'):
            response = self.client.post(
                self.webhook_url,
                data=json.dumps({'id': 'evt_test'}),
                content_type='application/json',
                HTTP_STRIPE_SIGNATURE='test_sig'
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.subscription_plan, 'free')

class StreakAndFriendsTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(
            username='user1', email='user1@example.com', password='password123'
        )
        self.user2 = User.objects.create_user(
            username='user2', email='user2@example.com', password='password123'
        )
        self.client.force_authenticate(user=self.user1)

    def test_activity_streak_increment(self):
        # Set last activity to yesterday
        self.user1.last_activity_date = timezone.now().date() - timezone.timedelta(days=1)
        self.user1.streak_days = 5
        self.user1.save()
        
        response = self.client.post(reverse('user_activity'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.streak_days, 6)
        self.assertEqual(self.user1.last_activity_date, timezone.now().date())

    def test_activity_streak_freeze(self):
        # Set last activity to 3 days ago (missed 2 days)
        self.user1.last_activity_date = timezone.now().date() - timezone.timedelta(days=3)
        self.user1.streak_days = 10
        self.user1.streak_freezes_used = 0
        self.user1.streak_freeze_limit = 2
        self.user1.save()
        
        response = self.client.post(reverse('user_activity'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user1.refresh_from_db()
        # Should have used 2 freezes and incremented streak
        self.assertEqual(self.user1.streak_days, 11)
        self.assertEqual(self.user1.streak_freezes_used, 2)

    def test_activity_streak_reset(self):
        # Set last activity to 4 days ago (missed 3 days, only 2 freezes)
        self.user1.last_activity_date = timezone.now().date() - timezone.timedelta(days=4)
        self.user1.streak_days = 10
        self.user1.streak_freezes_used = 0
        self.user1.streak_freeze_limit = 2
        self.user1.save()
        
        response = self.client.post(reverse('user_activity'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user1.refresh_from_db()
        self.assertEqual(self.user1.streak_days, 1)
        self.assertEqual(self.user1.streak_freezes_used, 0)

    def test_friend_request_flow(self):
        # Send request
        response = self.client.post(reverse('friend_request_create'), {'to_user_id': self.user2.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Accept request (as user2)
        self.client.force_authenticate(user=self.user2)
        request_id = response.data['id']
        response = self.client.post(reverse('friend_request_accept', kwargs={'pk': request_id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check friendship
        from api.models import Friendship
        self.assertTrue(Friendship.objects.filter(user=self.user1, friend=self.user2).exists())
        self.assertTrue(Friendship.objects.filter(user=self.user2, friend=self.user1).exists())

    def test_chat_flow(self):
        from api.models import Friendship
        Friendship.objects.create(user=self.user1, friend=self.user2)
        Friendship.objects.create(user=self.user2, friend=self.user1)
        
        # Send message
        response = self.client.post(reverse('chat_send'), {
            'receiver_id': self.user2.id,
            'message': 'Hello friend!'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Get messages
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(reverse('chat_messages', kwargs={'friend_id': self.user1.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['message'], 'Hello friend!')
