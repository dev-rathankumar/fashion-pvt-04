from django.db.models import fields
from modeltranslation.translator import translator, TranslationOptions
from .models import AboutContent, AboutPage, ContactPage, Footer, Header, ParallaxBackground, Policy, Service, ServicePageCTA, TermsAndCondition, Topbar, BannerImage, StoreFeature, VideoBanner


class TopbarTranslationOptions(TranslationOptions):
    fields = ('topbar_text',)


class BannerImageTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'button_name')


class StoreFeatureTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')


class ParallaxBackgroundTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button_name')


class VideoBannerTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'button_name')


class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class AboutPageTranslationOptions(TranslationOptions):
    fields = ('heading', 'sub_heading')


class AboutContentTranslationOptions(TranslationOptions):
    fields = ('header', 'header_text')


class HeaderTranslationOptions(TranslationOptions):
    fields = ('site_title',)


class FooterTranslationOptions(TranslationOptions):
    fields = ('footer_text',)


class ContactPageTranslationOptions(TranslationOptions):
    fields = ('address_line_1', 'address_line_2', 'city')


class PolicyTranslationOptions(TranslationOptions):
    fields = ('heading', 'content')


class TermsAndConditionTranslationOptions(TranslationOptions):
    fields = ('heading', 'content')


class ServicePageCTATranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'button_name')



translator.register(Topbar, TopbarTranslationOptions)
translator.register(BannerImage, BannerImageTranslationOptions)
translator.register(StoreFeature, StoreFeatureTranslationOptions)
translator.register(ParallaxBackground, ParallaxBackgroundTranslationOptions)
translator.register(VideoBanner, VideoBannerTranslationOptions)
translator.register(Service, ServiceTranslationOptions)
translator.register(AboutPage, AboutPageTranslationOptions)
translator.register(AboutContent, AboutContentTranslationOptions)
translator.register(Header, HeaderTranslationOptions)
translator.register(Footer, FooterTranslationOptions)
translator.register(ContactPage, ContactPageTranslationOptions)
translator.register(Policy, PolicyTranslationOptions)
translator.register(TermsAndCondition, TermsAndConditionTranslationOptions)
translator.register(ServicePageCTA, ServicePageCTATranslationOptions)

