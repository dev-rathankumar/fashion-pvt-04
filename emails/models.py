from django.db import models
from accounts.models import User
from ckeditor.fields import RichTextField

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
