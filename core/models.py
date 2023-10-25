from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField
from django.contrib.gis.geos import Point

# Create your models here.
class Service(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        heading = models.CharField(max_length=255),
        description = RichTextField()
    )
    icon = models.ImageField(upload_to='media/service/icon/')
    image = models.FileField(upload_to='media/service/img/')
    created_at = models.DateTimeField(auto_now_add=True)
    
class Team(models.Model):
    name = models.CharField(max_length=155)
    position = models.CharField(max_length=155)
    image = models.ImageField(upload_to='media/team_members/', blank=True, null=True)
    
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    telegram_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Team"
    
class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=255),)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=155)
    slug = models.CharField(unique=True, max_length=200)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    logo = models.ImageField(upload_to='media/portfolio/logo/')
    created_at = models.DateTimeField(auto_now_add=True)

    url_1 = models.URLField(max_length=200, blank=True, null=True)
    url_2 = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class PortfolioImages(models.Model):
    image = models.ImageField(upload_to='media/portfolio/')
    main_model = models.ForeignKey(Portfolio, related_name='images', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Contact(TranslatableModel):
    translations = TranslatedFields(
        address = models.CharField(max_length=255),
        working_hours = models.CharField(max_length=255)
    )

    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=254)
    coordinates = PlainLocationField(based_fields=['address'], zoom=11, default=Point(69.2401, 41.2995))
    
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    telegram_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

class OurClient(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/clients/')
    created_at = models.DateTimeField(auto_now_add=True)

class Tool(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/tools/')
    created_at = models.DateTimeField(auto_now_add=True)