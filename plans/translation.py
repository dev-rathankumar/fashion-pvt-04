from django.db.models import fields
from modeltranslation.translator import translator, TranslationOptions
from .models import Plan


class PlanTranslationOptions(TranslationOptions):
    fields = ('plan_name', 'plan_description')



translator.register(Plan, PlanTranslationOptions)

