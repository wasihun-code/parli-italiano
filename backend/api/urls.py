from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView, LoginView, GoogleAuthView, LogoutView,
    UserMeView, ProgressOverviewView, ScenarioSyncView,
    GameSyncView, MasteredSyncView, BatchSyncView,
    SubscriptionPlansView, CreateCheckoutSessionView,
    StripeWebhookView, SubscriptionStatusView
)

urlpatterns = [
    # Auth
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/google/', GoogleAuthView.as_view(), name='google_auth'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User
    path('users/me/', UserMeView.as_view(), name='user_me'),
    
    # Progress
    path('users/me/progress/', ProgressOverviewView.as_view(), name='progress_overview'),
    path('users/me/progress/scenario/', ScenarioSyncView.as_view(), name='scenario_sync'),
    path('users/me/progress/game/', GameSyncView.as_view(), name='game_sync'),
    path('users/me/mastered/', MasteredSyncView.as_view(), name='mastered_sync'),
    
    # Sync
    path('sync/', BatchSyncView.as_view(), name='batch_sync'),

    # Subscriptions
    path('subscription/plans/', SubscriptionPlansView.as_view(), name='subscription_plans'),
    path('subscription/create-checkout/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
    path('subscription/webhook/stripe/', StripeWebhookView.as_view(), name='stripe_webhook'),
    path('subscription/status/', SubscriptionStatusView.as_view(), name='subscription_status'),
]
