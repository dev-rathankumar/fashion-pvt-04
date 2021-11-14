from modeltranslation.translator import translator, TranslationOptions
from .models import Inquiry, SiteContact


class InquiryTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'inq_message')


class SiteContactTranslationOptions(TranslationOptions):
    fields = ('name', 'subject', 'contact_message')



translator.register(Inquiry, InquiryTranslationOptions)
translator.register(SiteContact, SiteContactTranslationOptions)