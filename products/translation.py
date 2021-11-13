from django.db.models import fields
from modeltranslation.translator import translator, TranslationOptions
from .models import SalesPopup


class SalesPopupTranslationOptions(TranslationOptions):
    fields = ('name', 'location', 'location')


translator.register(SalesPopup, SalesPopupTranslationOptions)