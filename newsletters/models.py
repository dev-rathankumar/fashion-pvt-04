from django.db import models
import uuid


class NewsletterUser(models.Model):
    email = models.EmailField(max_length=255)
    hash = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
