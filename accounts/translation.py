from modeltranslation.translator import translator, TranslationOptions
from .models import User, Business, Customer


class UserTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')


class BusinessTranslationOptions(TranslationOptions):
    fields = ('company_name', 'address_line_1', 'address_line_2', 'city')


class CustomerTranslationOptions(TranslationOptions):
    fields = ('address_line_1', 'address_line_2', 'city')


translator.register(User, UserTranslationOptions)
translator.register(Business, BusinessTranslationOptions)
translator.register(Customer, CustomerTranslationOptions)