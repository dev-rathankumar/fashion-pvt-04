from django.db.models import fields
from modeltranslation.translator import translator, TranslationOptions
from orders.models import Order, StoreLocation


class StoreLocationTranslationOptions(TranslationOptions):
    fields = ('store_name', 'address_line_1', 'address_line_2', 'city')


class OrderTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'address_line_1', 'address_line_2', 'city', 'note')


translator.register(StoreLocation, StoreLocationTranslationOptions)
translator.register(Order, OrderTranslationOptions)