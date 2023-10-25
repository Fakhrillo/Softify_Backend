from rest_framework import serializers
from .models import *

from django.utils.translation import get_language_from_path
from parler_rest.serializers import TranslatableModelSerializer

class ServiceSerializer(TranslatableModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'heading', 'description', 'icon', 'image', 'created_at']
        
    def to_representation(self, instance):
        language = get_language_from_path(self.context['request'].path)
        instance.set_current_language(language)
        return super().to_representation(instance)

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class CategorySerializer(TranslatableModelSerializer):
    class Meta:
        model = Category 
        fields = ['id', 'name', 'created_at']

    def to_representation(self, instance):
        language = get_language_from_path(self.context['request'].path)
        instance.set_current_language(language)
        return super().to_representation(instance)

class PortfolioSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'slug', 'description', 'category', 'category_name', 'logo', 'created_at', 'url_1', 'url_2']

class PortfolioImagesSerializer(serializers.ModelSerializer):
    main_model_name = serializers.SerializerMethodField()
    class Meta:
        model = PortfolioImages
        fields = ['id', 'image', 'main_model', 'main_model_name', 'created_at']

    def get_main_model_name(self, obj):
        return obj.main_model.name if obj.main_model else None

class ContactSerializer(TranslatableModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'address', 'working_hours', 'phone_number', 'email', 'coordinates', 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'telegram_url', 'github_url', 'created_at']

    def to_representation(self, instance):
        language = get_language_from_path(self.context['request'].path)
        instance.set_current_language(language)
        return super().to_representation(instance)

class OurClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurClient
        fields = '__all__'

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'