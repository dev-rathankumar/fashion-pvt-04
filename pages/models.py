from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import Business
from datetime import datetime


class Team(models.Model):
    business    = models.ForeignKey(Business, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='teams/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100, blank=True)
    twitter_link = models.URLField(max_length=100, blank=True)
    instagram_link = models.URLField(max_length=100, blank=True)
    youtube_link = models.URLField(max_length=100, blank=True)
    linkedin_link = models.URLField(max_length=100, blank=True)
    is_active     = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    # Concatenate first name and last name
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'


class About(models.Model):
    business    = models.ForeignKey(Business, on_delete=models.CASCADE)
    description = RichTextField(blank=True)
    cover_image = models.ImageField(upload_to='pages/%Y/%m/%d', blank=True)
    why_us      = RichTextField(blank=True)
    our_vision  = RichTextField(blank=True)
    our_mission = RichTextField(blank=True)
    our_team    = models.ForeignKey(Team, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'about'

    def __str__(self):
        return self.business.company_name
