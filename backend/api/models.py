from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Language(models.Model):
    code = models.CharField(max_length=10, unique=True) # e.g., 'en', 'it', 'fr'
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class User(AbstractUser):
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('premium', 'Premium'),
        ('premium_plus', 'Premium Plus'),
    ]
    subscription_plan = models.CharField(max_length=20, choices=PLAN_CHOICES, default='free')
    subscription_valid_until = models.DateTimeField(blank=True, null=True)
    
    total_xp = models.IntegerField(default=0)
    streak_days = models.IntegerField(default=0)
    last_activity_date = models.DateField(blank=True, null=True)
    streak_freezes_used = models.IntegerField(default=0)
    streak_freeze_limit = models.IntegerField(default=2)
    native_language = models.CharField(max_length=10, default='en')

    def __str__(self):
        return self.email or self.username

class FriendRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_requests_sent')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_requests_received')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_user', 'to_user')

class Friendship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_of')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'friend')

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender} to {self.receiver} at {self.timestamp}"

class UserLanguageProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='language_progress')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    total_xp = models.IntegerField(default=0)
    streak_days = models.IntegerField(default=0)
    last_activity = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'language')

    def __str__(self):
        return f"{self.user} - {self.language.code} Progress"

class Scenario(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    difficulty = models.IntegerField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='scenarios')

    def __str__(self):
        return f"{self.title} ({self.language.code})"

class ScenarioProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scenario_progress')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    scenario_id = models.IntegerField()
    phase = models.CharField(max_length=50) # e.g., 'introduction', 'practice', 'test'
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'language', 'scenario_id', 'phase')

class GameProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_progress')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    game_name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    high_score = models.IntegerField(default=0)
    unlocked_levels = models.JSONField(default=list)
    last_played = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'language', 'game_name')

class MasteredItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mastered_items')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    item_id = models.CharField(max_length=255) # Unique ID from the content JSONs
    item_type = models.CharField(max_length=50) # e.g., 'vocabulary', 'phrase', 'grammar'
    text = models.TextField()
    translation = models.TextField()
    mastered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'language', 'item_id', 'item_type')

class SubscriptionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription_history')
    old_plan = models.CharField(max_length=20)
    new_plan = models.CharField(max_length=20)
    changed_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} changed from {self.old_plan} to {self.new_plan} on {self.changed_at}"
