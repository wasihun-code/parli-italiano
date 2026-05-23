import requests
import stripe
from django.conf import settings
from django.utils import timezone
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import (
    Language, UserLanguageProgress, ScenarioProgress, 
    GameProgress, MasteredItem, SubscriptionHistory,
    FriendRequest, Friendship, ChatMessage
)
from .serializers import (
    UserSerializer, RegisterSerializer, LoginSerializer,
    UserLanguageProgressSerializer, ScenarioProgressSerializer,
    GameProgressSerializer, MasteredItemSerializer,
    FriendRequestSerializer, FriendshipSerializer, ChatMessageSerializer,
    LeaderboardSerializer
)

User = get_user_model()

class ActivityUpdateView(APIView):
    def post(self, request):
        user = request.user
        today = timezone.now().date()
        
        if user.last_activity_date is None:
            user.streak_days = 1
        elif user.last_activity_date == today:
            pass # Already updated today
        elif user.last_activity_date == today - timezone.timedelta(days=1):
            user.streak_days += 1
        else:
            gap = (today - user.last_activity_date).days
            missed_days = gap - 1
            
            # Update limit based on plan
            if user.subscription_plan in ['premium', 'premium_plus']:
                user.streak_freeze_limit = 6
            else:
                user.streak_freeze_limit = 2
                
            available_freezes = user.streak_freeze_limit - user.streak_freezes_used
            
            if missed_days <= available_freezes:
                user.streak_freezes_used += missed_days
                user.streak_days += 1
            else:
                user.streak_days = 1
                user.streak_freezes_used = 0 # Reset freezes on streak loss
        
        user.last_activity_date = today
        # Re-verify limit on every activity just in case
        if user.subscription_plan in ['premium', 'premium_plus']:
            user.streak_freeze_limit = 6
        else:
            user.streak_freeze_limit = 2
            
        user.save()
        return Response(UserSerializer(user).data)

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if len(query) < 3:
            return User.objects.none()
        return User.objects.filter(
            Q(username__icontains(query)) | Q(email__icontains(query))
        ).exclude(id=self.request.user.id)[:20]

class FriendRequestCreateView(APIView):
    def post(self, request):
        to_user_id = request.data.get('to_user_id')
        to_user = get_object_or_404(User, id=to_user_id)
        
        if to_user == request.user:
            return Response({'error': 'Cannot add yourself'}, status=status.HTTP_400_BAD_REQUEST)
            
        friend_request, created = FriendRequest.objects.get_or_create(
            from_user=request.user,
            to_user=to_user,
            defaults={'status': 'pending'}
        )
        
        if not created and friend_request.status != 'pending':
            friend_request.status = 'pending'
            friend_request.save()
            
        return Response(FriendRequestSerializer(friend_request).data)

class FriendRequestAcceptView(APIView):
    def post(self, request, pk):
        friend_request = get_object_or_404(FriendRequest, id=pk, to_user=request.user, status='pending')
        friend_request.status = 'accepted'
        friend_request.save()
        
        # Create mutual friendships
        Friendship.objects.get_or_create(user=request.user, friend=friend_request.from_user)
        Friendship.objects.get_or_create(user=friend_request.from_user, friend=request.user)
        
        return Response({'status': 'accepted'})

class FriendRequestDeclineView(APIView):
    def post(self, request, pk):
        friend_request = get_object_or_404(FriendRequest, id=pk, to_user=request.user, status='pending')
        friend_request.status = 'declined'
        friend_request.save()
        return Response({'status': 'declined'})

class FriendRequestListView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    
    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user, status='pending')

class FriendListView(generics.ListAPIView):
    serializer_class = FriendshipSerializer
    
    def get_queryset(self):
        return Friendship.objects.filter(user=self.request.user)

class ChatSendMessageView(APIView):
    def post(self, request):
        # Premium check
        if request.user.subscription_plan == 'free':
            return Response(
                {'error': 'Chat is a premium feature. Upgrade to chat with friends.'}, 
                status=status.HTTP_403_FORBIDDEN
            )

        receiver_id = request.data.get('receiver_id')
        message_text = request.data.get('message')
        receiver = get_object_or_404(User, id=receiver_id)
        
        # Check if they are friends
        if not Friendship.objects.filter(user=request.user, friend=receiver).exists():
            return Response({'error': 'You can only message friends'}, status=status.HTTP_403_FORBIDDEN)
            
        message = ChatMessage.objects.create(
            sender=request.user,
            receiver=receiver,
            message=message_text
        )
        return Response(ChatMessageSerializer(message).data)

class ChatMessageListView(generics.ListAPIView):
    serializer_class = ChatMessageSerializer
    
    def get_queryset(self):
        friend_id = self.kwargs.get('friend_id')
        friend = get_object_or_404(User, id=friend_id)
        since = self.request.query_params.get('since')
        
        queryset = ChatMessage.objects.filter(
            (Q(sender=self.request.user) & Q(receiver=friend)) |
            (Q(sender=friend) & Q(receiver=self.request.user))
        )
        
        if since:
            queryset = queryset.filter(timestamp__gt=since)
            
        return queryset.order_by('timestamp')

class ChatMessageReadView(APIView):
    def post(self, request):
        message_ids = request.data.get('message_ids', [])
        ChatMessage.objects.filter(
            id__in=message_ids,
            receiver=request.user
        ).update(is_read=True)
        return Response({'status': 'success'})

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_200_OK)

class GoogleAuthView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        token = request.data.get('access_token')
        if not token:
            return Response({'error': 'No access token provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Verify token with Google
        response = requests.get(f'https://oauth2.googleapis.com/tokeninfo?id_token={token}')
        if response.status_code != 200:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        data = response.json()
        email = data.get('email')
        
        if not email:
            return Response({'error': 'Email not provided by Google'}, status=status.HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(
            email=email,
            defaults={'username': email.split('@')[0]}
        )

        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        })

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_200_OK)

class UserMeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class ProgressBaseView(APIView):
    def get_language(self, request):
        lang_code = request.query_params.get('language', 'it')
        if not lang_code and request.data:
            lang_code = request.data.get('language', 'it')
        return get_object_or_404(Language, code=lang_code)

class ProgressOverviewView(ProgressBaseView):
    def get(self, request):
        language = self.get_language(request)
        user = request.user

        lang_progress = UserLanguageProgress.objects.filter(user=user, language=language).first()
        scenarios = ScenarioProgress.objects.filter(user=user, language=language)
        games = GameProgress.objects.filter(user=user, language=language)
        mastered = MasteredItem.objects.filter(user=user, language=language)

        return Response({
            'language_progress': UserLanguageProgressSerializer(lang_progress).data if lang_progress else None,
            'scenarios': ScenarioProgressSerializer(scenarios, many=True).data,
            'games': GameProgressSerializer(games, many=True).data,
            'mastered': MasteredItemSerializer(mastered, many=True).data
        })

class ScenarioSyncView(ProgressBaseView):
    def post(self, request):
        language = self.get_language(request)
        scenario_id = request.data.get('scenario_id')
        phase = request.data.get('phase')
        
        progress, created = ScenarioProgress.objects.update_or_create(
            user=request.user,
            language=language,
            scenario_id=scenario_id,
            phase=phase,
            defaults={
                'completed': request.data.get('completed', False),
                'score': request.data.get('score', 0)
            }
        )
        return Response(ScenarioProgressSerializer(progress).data)

class GameSyncView(ProgressBaseView):
    def post(self, request):
        language = self.get_language(request)
        game_name = request.data.get('game_name')
        
        progress, created = GameProgress.objects.update_or_create(
            user=request.user,
            language=language,
            game_name=game_name,
            defaults={
                'level': request.data.get('level', 1),
                'high_score': request.data.get('high_score', 0),
                'unlocked_levels': request.data.get('unlocked_levels', [])
            }
        )
        return Response(GameProgressSerializer(progress).data)

class MasteredSyncView(ProgressBaseView):
    def get(self, request):
        language = self.get_language(request)
        items = MasteredItem.objects.filter(user=request.user, language=language)
        return Response(MasteredItemSerializer(items, many=True).data)

    def post(self, request):
        language = self.get_language(request)
        items_data = request.data.get('items', [])
        results = []
        for item in items_data:
            obj, created = MasteredItem.objects.update_or_create(
                user=request.user,
                language=language,
                item_id=item.get('item_id'),
                item_type=item.get('item_type'),
                defaults={
                    'text': item.get('text'),
                    'translation': item.get('translation')
                }
            )
            results.append(obj)
        return Response(MasteredItemSerializer(results, many=True).data)

class BatchSyncView(ProgressBaseView):
    def post(self, request):
        language = self.get_language(request)
        user = request.user
        
        # Sync User stats
        if 'xp' in request.data:
            user.total_xp = request.data.get('xp')
        if 'streak' in request.data:
            user.streak_days = request.data.get('streak')
        if 'last_activity_date' in request.data:
            user.last_activity_date = request.data.get('last_activity_date')
        user.save()

        # Sync Scenarios
        scenarios_data = request.data.get('scenarioProgress', {})
        for scenario_id, progress in scenarios_data.items():
            # Flatten phases into records
            for phase in ['vocabulary', 'phrase', 'sentence']:
                completed_key = f"{phase}Completed"
                score_key = f"{phase}Score"
                
                ScenarioProgress.objects.update_or_create(
                    user=user, language=language, 
                    scenario_id=int(scenario_id), phase=phase,
                    defaults={
                        'completed': progress.get(completed_key, False),
                        'score': progress.get(score_key, 0)
                    }
                )
        
        # Sync Games
        for g in request.data.get('games', []):
            GameProgress.objects.update_or_create(
                user=user, language=language, game_name=g.get('game_name'),
                defaults={
                    'level': g.get('level', 1), 
                    'high_score': g.get('high_score', 0),
                    'unlocked_levels': g.get('unlocked_levels', [1])
                }
            )
            
        # Sync Mastered
        for m in request.data.get('mastered', []):
            MasteredItem.objects.update_or_create(
                user=user, language=language, 
                item_id=m.get('item_id'), item_type=m.get('item_type'),
                defaults={'text': m.get('text'), 'translation': m.get('translation')}
            )
            
        return Response({'status': 'success'})

stripe.api_key = settings.STRIPE_SECRET_KEY

class SubscriptionPlansView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        plans = [
            {
                'id': 'premium',
                'name': 'Premium',
                'price': '$9.99/mo',
                'price_id': settings.STRIPE_PREMIUM_PRICE_ID,
                'features': [
                    'Ad-free experience',
                    'Advanced Grammar lessons (A2+)',
                    'Full access to all Stories',
                    'Unlimited Progress Syncing'
                ]
            },
            {
                'id': 'premium_plus',
                'name': 'Premium Plus',
                'price': '$19.99/mo',
                'price_id': settings.STRIPE_PREMIUM_PLUS_PRICE_ID,
                'features': [
                    'All Premium features',
                    'Early access to new scenarios',
                    'Priority AI conversation support',
                    'Personalized learning reports'
                ]
            },
        ]
        return Response(plans)

class CreateCheckoutSessionView(APIView):
    def post(self, request):
        price_id = request.data.get('price_id')
        if not price_id:
            return Response({'error': 'price_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            session = stripe.checkout.Session.create(
                customer_email=request.user.email,
                client_reference_id=str(request.user.id),
                payment_method_types=['card'],
                line_items=[{
                    'price': price_id,
                    'quantity': 1,
                }],
                mode='subscription',
                success_url='http://localhost:5173/premium?success=true',
                cancel_url='http://localhost:5173/premium?canceled=true',
            )
            return Response({'url': session.url})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StripeWebhookView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        payload = request.body
        sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
            )
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.SignatureVerificationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            client_reference_id = session.get('client_reference_id')
            customer_id = session.get('customer')
            subscription_id = session.get('subscription')
            
            if client_reference_id:
                try:
                    user = User.objects.get(id=client_reference_id)
                    subscription = stripe.Subscription.retrieve(subscription_id)
                    
                    # Map price_id to plan name
                    price_id = subscription['items']['data'][0]['price']['id']
                    new_plan = 'free'
                    if price_id == settings.STRIPE_PREMIUM_PRICE_ID:
                        new_plan = 'premium'
                    elif price_id == settings.STRIPE_PREMIUM_PLUS_PRICE_ID:
                        new_plan = 'premium_plus'
                    
                    old_plan = user.subscription_plan
                    user.subscription_plan = new_plan
                    user.stripe_customer_id = customer_id
                    
                    # Convert timestamp to aware datetime
                    valid_until = timezone.datetime.fromtimestamp(
                        subscription['current_period_end']
                    )
                    if settings.USE_TZ:
                        valid_until = timezone.make_aware(valid_until)
                    
                    user.subscription_valid_until = valid_until
                    user.save()
                    
                    SubscriptionHistory.objects.create(
                        user=user,
                        old_plan=old_plan,
                        new_plan=new_plan,
                        reason='Stripe checkout completed'
                    )
                except User.DoesNotExist:
                    pass

        elif event['type'] == 'customer.subscription.deleted':
            subscription = event['data']['object']
            customer_id = subscription.get('customer')
            
            try:
                user = User.objects.get(stripe_customer_id=customer_id)
                old_plan = user.subscription_plan
                user.subscription_plan = 'free'
                user.subscription_valid_until = timezone.now()
                user.save()
                
                SubscriptionHistory.objects.create(
                    user=user,
                    old_plan=old_plan,
                    new_plan='free',
                    reason='Stripe subscription deleted'
                )
            except User.DoesNotExist:
                pass

        return Response(status=status.HTTP_200_OK)

class SubscriptionStatusView(APIView):
    def get(self, request):
        is_active = False
        if request.user.subscription_plan != 'free':
            if request.user.subscription_valid_until and request.user.subscription_valid_until > timezone.now():
                is_active = True
                
        return Response({
            'plan': request.user.subscription_plan,
            'is_valid': is_active,
            'subscription_valid_until': request.user.subscription_valid_until,
            'stripe_customer_id': request.user.stripe_customer_id,
        })

import requests
from django.http import HttpResponse

class TTSProxyView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        text = request.query_params.get('q')
        if not text:
            return Response({'error': 'No text provided'}, status=status.HTTP_400_BAD_REQUEST)

        url = f'https://translate.google.com/translate_tts?ie=UTF-8&tl=it-IT&client=tw-ob&q={requests.utils.quote(text)}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return HttpResponse(response.content, content_type='audio/mpeg')
            else:
                return Response({'error': 'Failed to fetch TTS from source'}, status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LeaderboardView(generics.ListAPIView):
    serializer_class = LeaderboardSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return User.objects.all().order_by('-total_xp')[:10]
