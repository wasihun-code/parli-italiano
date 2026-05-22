from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Language, User, UserLanguageProgress, ScenarioProgress, 
    GameProgress, MasteredItem, SubscriptionHistory
)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'subscription_plan', 'total_xp', 'streak_days', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Learning App Info', {'fields': (
            'stripe_customer_id', 'subscription_plan', 'subscription_valid_until', 
            'total_xp', 'streak_days', 'last_activity_date', 'native_language'
        )}),
    )

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'is_active']
    list_filter = ['is_active']

@admin.register(UserLanguageProgress)
class UserLanguageProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'language', 'total_xp', 'streak_days', 'last_activity']
    list_filter = ['language']
    search_fields = ['user__email', 'user__username']

@admin.register(ScenarioProgress)
class ScenarioProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'language', 'scenario_id', 'phase', 'completed', 'score']
    list_filter = ['language', 'completed', 'phase']
    search_fields = ['user__email', 'user__username', 'scenario_id']

@admin.register(GameProgress)
class GameProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'language', 'game_name', 'level', 'high_score']
    list_filter = ['language', 'game_name']
    search_fields = ['user__email', 'user__username', 'game_name']

@admin.register(MasteredItem)
class MasteredItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'language', 'item_id', 'item_type', 'text', 'mastered_at']
    list_filter = ['language', 'item_type']
    search_fields = ['user__email', 'user__username', 'item_id', 'text']

@admin.register(SubscriptionHistory)
class SubscriptionHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'old_plan', 'new_plan', 'changed_at']
    list_filter = ['old_plan', 'new_plan']
    search_fields = ['user__email', 'user__username']
