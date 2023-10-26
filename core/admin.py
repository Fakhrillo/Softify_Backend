from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
admin.site.unregister(User)
admin.site.unregister(Group)
# Register your models here.

@admin.register(Service)
class ServiceAdmin(TranslatableAdmin):
    list_display=('id', 'title', 'heading', 'image', 'created_at')
    search_fields = ('id', 'translations__title', 'translations__heading')
    list_display_links = ['id', 'title', 'heading']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'created_at')
    search_fields = ('id', 'name', 'position')
    list_display_links = ('id', 'name')

    fieldsets = (
        ('General Information', {
            'fields': ('name', 'position', 'image')
        }),
        
        ('Social Media Links', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'telegram_url', 'github_url'),
        }),
    )

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display=('id', 'name', 'created_at')
    search_fields = ('id', 'translations__name')
    list_display_links = ['id', 'name']

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'slug', 'category', 'created_at')
    search_fields = ('id', 'name')
    list_display_links = ['id', 'name']
    list_filter = ['category']

@admin.register(Contact)
class ContactAdmin(TranslatableAdmin):
    list_display=('id', 'phone_number', 'email', 'address', 'working_hours', 'created_at')
    search_fields = ('id', 'email', 'phone_number')
    list_display_links = ['id', 'phone_number', 'email']

    fieldsets = (
        ('General Information', {
            'fields': ('phone_number', 'email', 'coordinates')
        }),
        ('Address and Working Hours', {
            'fields': ('address', 'working_hours'),
            'classes': ('collapse',),
        }),
        ('Social Media Links', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'telegram_url', 'github_url'),
        }),
    )

@admin.register(OurClient)
class OurClientAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'created_at')
    search_fields = ('id', 'name')
    list_display_links = ['id', 'name']

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'created_at')
    search_fields = ('id', 'name')
    list_display_links = ['id', 'name']

@admin.register(PortfolioImages)
class PortfolioImagesAdmin(admin.ModelAdmin):
    list_display=('id', 'image', 'main_model', 'created_at')
    list_display_links = ['id', 'image', 'main_model']