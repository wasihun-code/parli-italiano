from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView, LoginView, GoogleAuthView, LogoutView,
    UserMeView, ProgressOverviewView, ScenarioSyncView,
    GameSyncView, MasteredSyncView, BatchSyncView,
    SubscriptionPlansView, CreateCheckoutSessionView,
    StripeWebhookView, SubscriptionStatusView,
    ActivityUpdateView, UserSearchView, FriendRequestCreateView,
    FriendRequestAcceptView, FriendRequestDeclineView,
    FriendRequestListView, FriendListView, ChatSendMessageView,
    ChatMessageListView, ChatMessageReadView
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
    path('users/me/activity/', ActivityUpdateView.as_view(), name='user_activity'),
    path('users/search/', UserSearchView.as_view(), name='user_search'),
    
    # Friends
    path('friends/request/', FriendRequestCreateView.as_view(), name='friend_request_create'),
    path('friends/request/<int:pk>/accept/', FriendRequestAcceptView.as_view(), name='friend_request_accept'),
    path('friends/request/<int:pk>/decline/', FriendRequestDeclineView.as_view(), name='friend_request_decline'),
    path('friends/requests/', FriendRequestListView.as_view(), name='friend_requests_list'),
    path('friends/list/', FriendListView.as_view(), name='friend_list'),

    # Chat
    path('chat/send/', ChatSendMessageView.as_view(), name='chat_send'),
    path('chat/messages/<int:friend_id>/', ChatMessageListView.as_view(), name='chat_messages'),
    path('chat/messages/read/', ChatMessageReadView.as_view(), name='chat_messages_read'),
    
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
