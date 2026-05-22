from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, UserLanguageProgress, ScenarioProgress, GameProgress, MasteredItem, Language

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'native_language', 
            'total_xp', 'streak_days', 'subscription_plan', 
            'subscription_valid_until'
        ]
        read_only_fields = ['id', 'username', 'email', 'total_xp', 'streak_days', 'subscription_plan', 'subscription_valid_until']

class UserLanguageProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLanguageProgress
        fields = '__all__'

class ScenarioProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScenarioProgress
        fields = '__all__'

class GameProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameProgress
        fields = '__all__'

class MasteredItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasteredItem
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'tokens']
        extra_kwargs = {'email': {'required': True}}

    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data.get('username') or email.split('@')[0]
        
        # Ensure username is unique
        base_username = username
        counter = 1
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        user = User.objects.create_user(
            username=username,
            email=email,
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            # Since we allow login by email, we need to find the user first or use a custom backend
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None
                
            if not user:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'")

        return user
