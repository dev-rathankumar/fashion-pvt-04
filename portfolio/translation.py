from django.db.models import fields
from modeltranslation.translator import translator, TranslationOptions
from .models import Portfolio, PortfolioHeader


class PortfolioTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button_name')


class PortfolioHeaderTranslationOptions(TranslationOptions):
    fields = ('heading', 'sub_heading')


translator.register(Portfolio, PortfolioTranslationOptions)
translator.register(PortfolioHeader, PortfolioHeaderTranslationOptions)