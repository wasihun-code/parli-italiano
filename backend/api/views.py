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
from .models import (
    Language, UserLanguageProgress, ScenarioProgress, 
    GameProgress, MasteredItem, SubscriptionHistory
)
from .serializers import (
    UserSerializer, RegisterSerializer, LoginSerializer,
    UserLanguageProgressSerializer, ScenarioProgressSerializer,
    GameProgressSerializer, MasteredItemSerializer
)

User = get_user_model()

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
        
        # Sync Scenarios
        for s in request.data.get('scenarios', []):
            ScenarioProgress.objects.update_or_create(
                user=user, language=language, 
                scenario_id=s.get('scenario_id'), phase=s.get('phase'),
                defaults={'completed': s.get('completed'), 'score': s.get('score')}
            )
        
        # Sync Games
        for g in request.data.get('games', []):
            GameProgress.objects.update_or_create(
                user=user, language=language, game_name=g.get('game_name'),
                defaults={
                    'level': g.get('level'), 
                    'high_score': g.get('high_score'),
                    'unlocked_levels': g.get('unlocked_levels')
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
