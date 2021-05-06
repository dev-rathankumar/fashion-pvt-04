from django.db import models
from accounts.models import User, Business
from ckeditor.fields import RichTextField
from django import forms

# Create your models here.

# def get_emails(request):
#     customers = User.objects.filter(is_customer=True, is_active=True)
#     emails = []
#     for i in customers:
#         emails.append(i.email)
#     return emails


class Email(models.Model):
    to_address = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    subject = models.CharField(max_length=255, blank=True)
    email_body = RichTextField(blank=True)
    is_sent = models.BooleanField(default=False)
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class BusinessEmailSetting(models.Model):
    USE_TLS_CHOICES = (
        ('True', 'Yes'),
        ('False', 'No'),
    )
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    email_host = models.CharField(max_length=100, blank=True)
    email_host_user = models.EmailField(max_length=100, blank=True)
    email_host_password = models.CharField(max_length=50, blank=True)
    port = models.IntegerField(null=True, blank=True)
    email_use_tls = models.CharField(max_length=10, choices=USE_TLS_CHOICES, default='True')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business.company_name
