from django.db.models import fields
from modeltranslation.translator import translator, TranslationOptions
from .models import Email


class EmailTranslationOptions(TranslationOptions):
    fields = ('subject', 'email_body')



translator.register(Email, EmailTranslationOptions)

