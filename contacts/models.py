from django.db import models
from accounts.models import Business
from datetime import datetime


class Inquiry(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    user_id = models.IntegerField(blank=True)
    product_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    inq_message = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'inquiry'
        verbose_name_plural = 'inquiries'


class SiteContact(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    user_id = models.IntegerField(blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=100)
    contact_message = models.TextField(blank=True)
    otp = models.CharField(max_length=10, default='0')
    is_otp_sent = models.BooleanField(default=False)
    otp_updated_time = models.CharField(default=datetime.now, max_length=255)
    is_otp_verified = models.BooleanField(default=False)
    is_otp_expired = models.BooleanField(default=False)
    otp_resend_counter = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
