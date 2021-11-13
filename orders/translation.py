from django.db.models import fields
from modeltranslation.translator import translator, TranslationOptions
from orders.models import StoreLocation


class StoreLocationTranslationOptions(TranslationOptions):
    fields = ('store_name', 'address_line_1', 'address_line_2', 'city')



translator.register(StoreLocation, StoreLocationTranslationOptions)